import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.RingTheory.PowerSeries.Derivative
import Mathlib.RingTheory.PowerSeries.Inverse
import Mathlib.RingTheory.PowerSeries.Substitution
import Mathlib.Tactic

/-!
# OEIS A177259 — Mathar (2022) D-Finite Recurrence Conjecture

This file formalizes the proof of R. J. Mathar's July 26, 2022 D-finite
recurrence conjecture on OEIS **A177259** (revision 28, offset `0,5`):

* **Name:** Number of derangements of `{1, ..., n}` having no adjacent 3-cycles.
* **Formula:** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/3)} (-1)^(s+t) * (n - 2*t)! / (s! * t!)`.
* **Formula (R. J. Mathar, Jul 26 2022):**
  `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6).`

## Main Results

* `OpenMath.OeisA177259.a177259_eq_coeff`:
  The generating function `y(X) = ∑_{n ≥ 0} a(n) X^n` satisfies
  `(1 + X + X^3) * y(X) = F(X / (1 + X + X^3))`, where `F(u) = ∑_{m ≥ 0} m! u^m`.
* `OpenMath.OeisA177259.ySeries_ode`:
  `X^2 (1 + X + X^3) y'(X) + (-1 + X^2 + X^3 + 3X^4 + 2X^6) y(X) + (1 - 2X^3) = 0`.
* `OpenMath.OeisA177259.mathar_conjecture_A177259`:
  For all `n ≥ 6`,
  `a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6)` (in `ℤ` and `ℚ`).
-/

namespace OpenMath.OeisA177259

open PowerSeries
open scoped BigOperators

/-! ## Section 1: Exact OEIS Formula and Integrality -/

/-- Exact integer formula for OEIS **A177259** (offset `0`):
`a(n) = ∑_{s=0}^n ∑_{t=0}^{(n-s)/3} (-1)^(s+t) * ((n - 2*t)! / (s! * t!))`. -/
def a177259 (n : ℕ) : ℤ :=
  ∑ s ∈ Finset.range (n + 1),
    ∑ t ∈ Finset.range ((n - s) / 3 + 1),
      (-1 : ℤ) ^ (s + t) * (((n - 2 * t).factorial / (s.factorial * t.factorial) : ℕ) : ℤ)

/-- Rational version of the OEIS **A177259** formula with exact field division. -/
def a177259Q (n : ℕ) : ℚ :=
  ∑ s ∈ Finset.range (n + 1),
    ∑ t ∈ Finset.range ((n - s) / 3 + 1),
      (-1 : ℚ) ^ (s + t) * (((n - 2 * t).factorial : ℚ) / ((s.factorial : ℚ) * (t.factorial : ℚ)))

lemma fac_mul_fac_dvd_of_le {s t k : ℕ} (h : s + t ≤ k) :
    s.factorial * t.factorial ∣ k.factorial := by
  have h1 : s.factorial * t.factorial ∣ (s + t).factorial := by
    have hch := Nat.choose_mul_factorial_mul_factorial (Nat.le_add_right s t)
    rw [Nat.add_sub_cancel_left] at hch
    exact ⟨(s + t).choose s, by linarith⟩
  exact h1.trans (Nat.factorial_dvd_factorial h)

lemma a177259_cast_eq (n : ℕ) : (a177259 n : ℚ) = a177259Q n := by
  unfold a177259 a177259Q
  rw [Int.cast_sum]
  refine Finset.sum_congr rfl fun s hs => ?_
  have hsn : s ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hs)
  rw [Int.cast_sum]
  refine Finset.sum_congr rfl fun t ht => ?_
  have ht_le : t ≤ (n - s) / 3 := Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)
  have hst : s + t ≤ n - 2 * t := by omega
  have hdvd : s.factorial * t.factorial ∣ (n - 2 * t).factorial := fac_mul_fac_dvd_of_le hst
  rw [Int.cast_mul, Int.cast_pow, Int.cast_neg, Int.cast_one, Int.cast_natCast,
    Nat.cast_div hdvd (by positivity), Nat.cast_mul]

/-! ## Section 2: Formal Power Series Helpers -/

private lemma coeff_X_mul_eq (f : PowerSeries ℚ) (n : ℕ) :
    coeff n (X * f) = if 1 ≤ n then coeff (n - 1) f else 0 := by
  rw [← pow_one (X : PowerSeries ℚ), PowerSeries.coeff_X_pow_mul']

private lemma C_two_rat : C (2 : ℚ) = (2 : PowerSeries ℚ) := by
  rw [show (2 : ℚ) = 1 + 1 by norm_num, map_add, map_one]; ring

private lemma C_three_rat : C (3 : ℚ) = (3 : PowerSeries ℚ) := by
  rw [show (3 : ℚ) = 1 + 1 + 1 by norm_num, map_add, map_add, map_one]; ring

private lemma subst_X_eq {a : PowerSeries ℚ} (ha : HasSubst a) :
    (X : PowerSeries ℚ).subst a = a := by
  ext e
  rw [PowerSeries.coeff_subst' ha, finsum_eq_single _ 1]
  · simp
  · intro d hd
    have h0 : coeff d (X : PowerSeries ℚ) = 0 := by rw [coeff_X, ite_eq_right hd]
    simp [h0]

/-- Power series `G_m(X) = ∑_{j ≥ 0} choose(j + m, m) X^j = (1 - X)^{-(m + 1)}`. -/
noncomputable def negBinom (m : ℕ) : PowerSeries ℚ :=
  PowerSeries.mk fun j => ((j + m).choose m : ℚ)

lemma one_sub_X_pow_mul_negBinom (m : ℕ) :
    (1 - X : PowerSeries ℚ) ^ (m + 1) * negBinom m = 1 := by
  induction m with
  | zero =>
    rw [pow_one]
    ext k
    have hsplit : (1 - X : PowerSeries ℚ) * negBinom 0 =
        negBinom 0 - X * negBinom 0 := by ring
    rw [hsplit, map_sub, ← pow_one (X : PowerSeries ℚ), PowerSeries.coeff_X_pow_mul', coeff_one]
    cases k with
    | zero => simp [negBinom]
    | succ r =>
      have hr : 1 ≤ r + 1 := Nat.succ_le_succ (Nat.zero_le r)
      rw [ite_eq_left hr, Nat.add_sub_cancel]
      simp [negBinom]
  | succ m ih =>
    have hstep : (1 - X : PowerSeries ℚ) * negBinom (m + 1) = negBinom m := by
      ext k
      have hsplit : (1 - X : PowerSeries ℚ) * negBinom (m + 1) =
          negBinom (m + 1) - X * negBinom (m + 1) := by ring
      rw [hsplit, map_sub, ← pow_one (X : PowerSeries ℚ), PowerSeries.coeff_X_pow_mul']
      cases k with
      | zero => simp [negBinom]
      | succ r =>
        have hr : 1 ≤ r + 1 := Nat.succ_le_succ (Nat.zero_le r)
        rw [ite_eq_left hr, Nat.add_sub_cancel]
        simp only [negBinom, coeff_mk]
        have hpas : (r + 1 + (m + 1)).choose (m + 1) =
            (r + (m + 1)).choose m + (r + (m + 1)).choose (m + 1) := by
          rw [show r + 1 + (m + 1) = (r + (m + 1)) + 1 by omega, Nat.choose_succ_succ]
        have hidx : r + (m + 1) = r + 1 + m := by omega
        rw [hpas, hidx]
        push_cast
        ring
    calc (1 - X : PowerSeries ℚ) ^ (m + 1 + 1) * negBinom (m + 1)
        = (1 - X : PowerSeries ℚ) ^ (m + 1) * ((1 - X : PowerSeries ℚ) * negBinom (m + 1)) := by
          ring
      _ = (1 - X : PowerSeries ℚ) ^ (m + 1) * negBinom m := by rw [hstep]
      _ = 1 := ih

/-- Denominator polynomial `D(X) = 1 + X + X^3` in `ℚ⟦X⟧`. -/
noncomputable def D3 : PowerSeries ℚ :=
  1 + X + X ^ 3

lemma constantCoeff_D3 : constantCoeff D3 = 1 := by
  simp [D3, map_add, map_pow]

lemma constantCoeff_D3_ne : constantCoeff D3 ≠ 0 := by
  rw [constantCoeff_D3]; norm_num

/-- Substitution argument `u(X) = X * D3(X)⁻¹` in `ℚ⟦X⟧`. -/
noncomputable def u3 : PowerSeries ℚ :=
  X * D3⁻¹

lemma constantCoeff_u3 : constantCoeff u3 = 0 := by
  simp [u3, map_mul]

lemma hasSubst_u3 : HasSubst u3 :=
  HasSubst.of_constantCoeff_zero' constantCoeff_u3

/-- The factorial generating function `F(u) = ∑_{m ≥ 0} m! u^m` in `ℚ⟦X⟧`. -/
noncomputable def FSeries : PowerSeries ℚ :=
  PowerSeries.mk fun m => (m.factorial : ℚ)

lemma FSeries_ode :
    X ^ 2 * PowerSeries.derivative FSeries + (X - 1) * FSeries + 1 = 0 := by
  ext n
  have hsplit : X ^ 2 * PowerSeries.derivative FSeries + (X - 1) * FSeries + 1 =
      X ^ 2 * PowerSeries.derivative FSeries + X * FSeries - FSeries + 1 := by ring
  rw [hsplit, map_add, map_sub, map_add, map_zero, PowerSeries.coeff_X_pow_mul',
    coeff_X_mul_eq, coeff_one]
  match n with
  | 0 => simp [FSeries]
  | 1 => simp [FSeries]
  | m + 2 =>
    have h1 : 1 ≤ m + 2 := by omega
    have h2 : 2 ≤ m + 2 := by omega
    rw [ite_eq_left h2, ite_eq_left h1]
    simp only [show m + 2 - 2 = m by omega, show m + 2 - 1 = m + 1 by omega,
      show m + 2 ≠ 0 by omega, ↓reduceIte, add_zero, coeff_derivative, FSeries, coeff_mk]
    rw [Nat.factorial_succ (m + 1)]
    push_cast
    ring

/-- The generating function `y(X) = D3(X)⁻¹ * F(X / D3(X))` in `ℚ⟦X⟧`. -/
noncomputable def ySeries : PowerSeries ℚ :=
  D3⁻¹ * FSeries.subst u3

/-! ## Section 3: Step 1 — Identification `[X^n] y(X) = a177259 n` -/

lemma coeff_one_add_X_sq_pow (j r : ℕ) :
    coeff r ((1 + X ^ 2 : PowerSeries ℚ) ^ j) =
      ∑ t ∈ Finset.range (j + 1), if 2 * t = r then (j.choose t : ℚ) else 0 := by
  have hexp : (1 + X ^ 2 : PowerSeries ℚ) ^ j =
      ∑ t ∈ Finset.range (j + 1), C (j.choose t : ℚ) * X ^ (2 * t) := by
    rw [add_comm, add_pow]
    refine Finset.sum_congr rfl fun t _ => ?_
    rw [one_pow, mul_one, ← pow_mul, mul_comm]
    rw [← map_natCast PowerSeries.C (j.choose t)]
  rw [hexp, map_sum]
  refine Finset.sum_congr rfl fun t _ => ?_
  rw [coeff_C_mul, coeff_X_pow]
  split_ifs with h1 h2
  · ring
  · omega
  · omega
  · ring

lemma D3_inv_pow_eq_subst (m : ℕ) :
    D3⁻¹ ^ (m + 1) = (negBinom m).subst (-(X + X ^ 3)) := by
  set w : PowerSeries ℚ := -(X + X ^ 3)
  have hw : HasSubst w := HasSubst.of_constantCoeff_zero' (by simp [w, map_neg, map_add, map_pow])
  have h1w : (1 - X : PowerSeries ℚ).subst w = D3 := by
    rw [PowerSeries.subst_sub hw, ← PowerSeries.coe_substAlgHom hw, map_one,
      PowerSeries.coe_substAlgHom hw, subst_X_eq hw]
    dsimp [w, D3]
    ring
  have hmul : D3 ^ (m + 1) * (negBinom m).subst w = 1 := by
    have hsub := congrArg (PowerSeries.subst w) (one_sub_X_pow_mul_negBinom m)
    rw [PowerSeries.subst_mul hw, PowerSeries.subst_pow hw, h1w,
      ← PowerSeries.coe_substAlgHom hw, map_one] at hsub
    simpa [PowerSeries.coe_substAlgHom hw] using hsub
  have hcancel : D3⁻¹ ^ (m + 1) * D3 ^ (m + 1) = 1 := by
    rw [← mul_pow, PowerSeries.inv_mul_cancel D3 constantCoeff_D3_ne, one_pow]
  calc D3⁻¹ ^ (m + 1) = D3⁻¹ ^ (m + 1) * 1 := (mul_one _).symm
    _ = D3⁻¹ ^ (m + 1) * (D3 ^ (m + 1) * (negBinom m).subst w) := by rw [hmul]
    _ = (D3⁻¹ ^ (m + 1) * D3 ^ (m + 1)) * (negBinom m).subst w := by ring
    _ = (negBinom m).subst w := by rw [hcancel, one_mul]

/-- Step 1: `[X^n] ySeries = a177259 n` for every `n ≥ 0`. -/
theorem coeff_ySeries_eq_a177259Q (n : ℕ) : coeff n ySeries = a177259Q n := by
  -- Truncate `FSeries.subst u3` at `m ≤ n` since `u3^m` has order ≥ m.
  let Ftrunc : PowerSeries ℚ :=
    ∑ m ∈ Finset.range (n + 1), C (m.factorial : ℚ) * u3 ^ m
  have htrunc_coeff : ∀ k ≤ n, coeff k (FSeries.subst u3) = coeff k Ftrunc := by
    intro k hkn
    rw [PowerSeries.coeff_subst' hasSubst_u3]
    have hfin : finsum (fun m => coeff m FSeries • coeff k (u3 ^ m)) =
        ∑ m ∈ Finset.range (n + 1), coeff m FSeries • coeff k (u3 ^ m) := by
      refine finsum_eq_sum_of_support_subset _ fun m hm => ?_
      rw [Finset.mem_coe, Finset.mem_range]
      by_contra hge
      have hgt : k < m := by omega
      have hu_zero : coeff k (u3 ^ m) = 0 := by
        rw [u3, mul_pow, PowerSeries.coeff_X_pow_mul', ite_eq_right (by omega)]
      simp [Function.mem_support, hu_zero] at hm
    rw [hfin]
    dsimp [Ftrunc]
    rw [map_sum]
    refine Finset.sum_congr rfl fun m _ => ?_
    simp only [coeff_C_mul, FSeries, coeff_mk]
  have hy_trunc : coeff n ySeries = coeff n (D3⁻¹ * Ftrunc) := by
    rw [ySeries, PowerSeries.coeff_mul, PowerSeries.coeff_mul]
    refine Finset.sum_congr rfl fun p hp => ?_
    have hp2 : p.2 ≤ n := (Finset.mem_antidiagonal.mp hp) ▸ Nat.le_add_left p.2 p.1
    rw [htrunc_coeff p.2 hp2]
  have hy_sum1 : coeff n ySeries =
      ∑ m ∈ Finset.range (n + 1), (m.factorial : ℚ) * coeff (n - m) (D3⁻¹ ^ (m + 1)) := by
    rw [hy_trunc]
    dsimp [Ftrunc]
    rw [Finset.mul_sum, map_sum]
    refine Finset.sum_congr rfl fun m hm => ?_
    have hmn : m ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hm)
    have hterm : D3⁻¹ * (C (m.factorial : ℚ) * u3 ^ m) =
        C (m.factorial : ℚ) * (X ^ m * D3⁻¹ ^ (m + 1)) := by
      rw [u3, mul_pow]; ring
    rw [hterm, coeff_C_mul, PowerSeries.coeff_X_pow_mul', ite_eq_left hmn]
  -- Expand each `coeff (n - m) (D3⁻¹ ^ (m + 1))` using `negBinom m` substituted with `-(X + X^3)`.
  set w : PowerSeries ℚ := -(X + X ^ 3)
  have hw : HasSubst w := HasSubst.of_constantCoeff_zero' (by simp [w, map_neg, map_add, map_pow])
  have hw_pow : ∀ j : ℕ, w ^ j = C ((-1 : ℚ) ^ j) * (X ^ j * (1 + X ^ 2 : PowerSeries ℚ) ^ j) := by
    intro j
    have hw1 : w = C (-1 : ℚ) * (X * (1 + X ^ 2 : PowerSeries ℚ)) := by
      dsimp [w]; simp only [map_neg, map_one]; ring
    rw [hw1, mul_pow, mul_pow, ← map_pow PowerSeries.C]
  have hy_triple : coeff n ySeries =
      ∑ m ∈ Finset.range (n + 1),
        ∑ j ∈ Finset.range (n - m + 1),
          ∑ t ∈ Finset.range (j + 1),
            if 2 * t = n - m - j then
              (m.factorial : ℚ) * ((j + m).choose m : ℚ) * (-1 : ℚ) ^ j * (j.choose t : ℚ)
            else 0 := by
    rw [hy_sum1]
    refine Finset.sum_congr rfl fun m hm => ?_
    rw [D3_inv_pow_eq_subst m, PowerSeries.coeff_subst' hw]
    have hfin : finsum (fun j => coeff j (negBinom m) • coeff (n - m) (w ^ j)) =
        ∑ j ∈ Finset.range (n - m + 1), coeff j (negBinom m) • coeff (n - m) (w ^ j) := by
      refine finsum_eq_sum_of_support_subset _ fun j hj => ?_
      rw [Finset.mem_coe, Finset.mem_range]
      by_contra hge
      have hgt : n - m < j := by omega
      have h0 : coeff (n - m) (w ^ j) = 0 := by
        rw [hw_pow j, coeff_C_mul, PowerSeries.coeff_X_pow_mul', ite_eq_right (by omega), mul_zero]
      simp [Function.mem_support, h0] at hj
    rw [hfin, Finset.mul_sum]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hjm : j ≤ n - m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    rw [smul_eq_mul, negBinom, coeff_mk, hw_pow j, coeff_C_mul, PowerSeries.coeff_X_pow_mul',
      ite_eq_left hjm, coeff_one_add_X_sq_pow, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun t _ => ?_
    split_ifs <;> ring
  -- Reindex the triple sum over `(m, j, t)` with `2*t = n - m - j` to `(s, t)` with `s + 3*t ≤ n`.
  rw [hy_triple, a177259Q]
  -- Convert both sides to sums over `Finset.sigma` / product sets and apply `Finset.sum_nbij`.
  let T1 : Finset ((ℕ × ℕ) × ℕ) :=
    (((Finset.range (n + 1)).sigma fun m => Finset.range (n - m + 1)).sigma
      fun mj => Finset.range (mj.2 + 1)).image (fun x => ((x.1.1, x.1.2), x.2))
  let S1 : Finset ((ℕ × ℕ) × ℕ) := T1.filter (fun p => 2 * p.2 = n - p.1.1 - p.1.2)
  let S2 : Finset (ℕ × ℕ) :=
    ((Finset.range (n + 1)).sigma fun s => Finset.range ((n - s) / 3 + 1)).image
      (fun x => (x.1, x.2))
  have hLHS : (∑ m ∈ Finset.range (n + 1),
        ∑ j ∈ Finset.range (n - m + 1),
          ∑ t ∈ Finset.range (j + 1),
            if 2 * t = n - m - j then
              (m.factorial : ℚ) * ((j + m).choose m : ℚ) * (-1 : ℚ) ^ j * (j.choose t : ℚ)
            else 0) =
      ∑ p ∈ S1,
        (p.1.1.factorial : ℚ) * ((p.1.2 + p.1.1).choose p.1.1 : ℚ) *
          (-1 : ℚ) ^ p.1.2 * (p.1.2.choose p.2 : ℚ) := by
    rw [Finset.sum_filter]
    -- Rewrite via `Finset.sum_sigma`
    have hT1 : ∑ p ∈ T1, (if 2 * p.2 = n - p.1.1 - p.1.2 then
          (p.1.1.factorial : ℚ) * ((p.1.2 + p.1.1).choose p.1.1 : ℚ) *
            (-1 : ℚ) ^ p.1.2 * (p.1.2.choose p.2 : ℚ) else 0) =
        ∑ m ∈ Finset.range (n + 1),
          ∑ j ∈ Finset.range (n - m + 1),
            ∑ t ∈ Finset.range (j + 1),
              if 2 * t = n - m - j then
                (m.factorial : ℚ) * ((j + m).choose m : ℚ) * (-1 : ℚ) ^ j * (j.choose t : ℚ)
              else 0 := by
      dsimp [T1]
      rw [Finset.sum_image (by
        rintro ⟨⟨a, b⟩, c⟩ _ ⟨⟨a', b'⟩, c'⟩ _ h
        simp only [Prod.mk.injEq] at h
        rcases h with ⟨⟨rfl, rfl⟩, rfl⟩; rfl)]
      rw [Finset.sum_sigma, Finset.sum_sigma]
    exact hT1.symm
  have hRHS : (∑ s ∈ Finset.range (n + 1),
        ∑ t ∈ Finset.range ((n - s) / 3 + 1),
          (-1 : ℚ) ^ (s + t) * (((n - 2 * t).factorial : ℚ) /
            ((s.factorial : ℚ) * (t.factorial : ℚ)))) =
      ∑ q ∈ S2,
        (-1 : ℚ) ^ (q.1 + q.2) * (((n - 2 * q.2).factorial : ℚ) /
          ((q.1.factorial : ℚ) * (q.2.factorial : ℚ))) := by
    dsimp [S2]
    rw [Finset.sum_image (by
      rintro ⟨a, b⟩ _ ⟨a', b'⟩ _ h
      simp only [Prod.mk.injEq] at h
      rcases h with ⟨rfl, rfl⟩; rfl)]
    rw [Finset.sum_sigma]
  rw [hLHS, hRHS]
  have hmemS1 : ∀ m j t : ℕ, ((m, j), t) ∈ S1 ↔
      m ≤ n ∧ j ≤ n - m ∧ t ≤ j ∧ 2 * t = n - m - j := by
    intro m j t
    simp only [S1, T1, Finset.mem_filter, Finset.mem_image, Finset.mem_sigma, Finset.mem_range,
      Prod.mk.injEq]
    constructor
    · rintro ⟨⟨⟨⟨a, b⟩, c⟩, ⟨⟨ha, hb⟩, hc⟩, ⟨rfl, rfl⟩, rfl⟩, heq⟩
      exact ⟨by omega, by omega, by omega, heq⟩
    · rintro ⟨h1, h2, h3, h4⟩
      exact ⟨⟨⟨⟨m, j⟩, t⟩, ⟨⟨by dsimp; omega, by dsimp; omega⟩, by dsimp; omega⟩, ⟨rfl, rfl⟩, rfl⟩, h4⟩
  have hmemS2 : ∀ s t : ℕ, (s, t) ∈ S2 ↔ s + 3 * t ≤ n := by
    intro s t
    simp only [S2, Finset.mem_image, Finset.mem_sigma, Finset.mem_range, Prod.mk.injEq]
    constructor
    · rintro ⟨⟨a, b⟩, ⟨ha, hb⟩, rfl, rfl⟩; omega
    · intro h
      exact ⟨⟨s, t⟩, ⟨by dsimp; omega, by dsimp; omega⟩, rfl, rfl⟩
  refine Finset.sum_nbij (fun p => (p.1.2 - p.2, p.2)) ?_ ?_ ?_ ?_
  · rintro ⟨⟨m, j⟩, t⟩ hp
    rw [hmemS1] at hp
    dsimp only
    rw [hmemS2]
    omega
  · rintro ⟨⟨m₁, j₁⟩, t₁⟩ hp₁ ⟨⟨m₂, j₂⟩, t₂⟩ hp₂ heq
    rw [Finset.mem_coe, hmemS1] at hp₁ hp₂
    simp only [Prod.mk.injEq] at heq
    have : t₁ = t₂ := heq.2
    subst this
    have : j₁ = j₂ := by omega
    subst this
    have : m₁ = m₂ := by omega
    subst this
    rfl
  · rintro ⟨s, t⟩ hq
    rw [Finset.mem_coe, hmemS2] at hq
    refine ⟨((n - s - 3 * t, s + t), t), ?_, ?_⟩
    · rw [Finset.mem_coe, hmemS1]; omega
    · dsimp only; exact Prod.ext (by omega) rfl
  · rintro ⟨⟨m, j⟩, t⟩ hp
    rw [hmemS1] at hp
    have hj_eq : j = (j - t) + t := by omega
    have hjm_eq : j + m = n - 2 * t := by omega
    have hch1 : ((j + m).choose m : ℚ) * ((m.factorial : ℚ) * (j.factorial : ℚ)) =
        ((j + m).factorial : ℚ) := by
      have h := Nat.choose_mul_factorial_mul_factorial (Nat.le_add_left m j)
      rw [Nat.add_sub_cancel, mul_assoc] at h
      exact_mod_cast h
    have hch2 : (j.choose t : ℚ) * ((t.factorial : ℚ) * ((j - t).factorial : ℚ)) =
        (j.factorial : ℚ) := by
      have h := Nat.choose_mul_factorial_mul_factorial hp.2.2.1
      rw [mul_assoc] at h
      exact_mod_cast h
    have ht_ne : (t.factorial : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero t)
    have hjt_ne : ((j - t).factorial : ℚ) ≠ 0 :=
      Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero (j - t))
    dsimp only
    rw [← hjm_eq, ← hj_eq, mul_div_assoc', eq_div_iff (mul_ne_zero hjt_ne ht_ne)]
    calc (m.factorial : ℚ) * ((j + m).choose m : ℚ) * (-1 : ℚ) ^ j * (j.choose t : ℚ) *
          (((j - t).factorial : ℚ) * (t.factorial : ℚ))
        = (-1 : ℚ) ^ j * ((j + m).choose m : ℚ) * (m.factorial : ℚ) *
          ((j.choose t : ℚ) * ((t.factorial : ℚ) * ((j - t).factorial : ℚ))) := by ring
      _ = (-1 : ℚ) ^ j * (((j + m).choose m : ℚ) * ((m.factorial : ℚ) * (j.factorial : ℚ))) := by
          rw [hch2]; ring
      _ = (-1 : ℚ) ^ j * ((j + m).factorial : ℚ) := by rw [hch1]

/-! ## Section 4: Step 2 — First-Order Linear ODE for `ySeries` -/

lemma derivative_D3 : PowerSeries.derivative D3 = 1 + 3 * X ^ 2 := by
  unfold D3
  rw [map_add, map_add, PowerSeries.derivative_one, PowerSeries.derivative_X,
    PowerSeries.derivative_X_pow]
  norm_num only
  rw [C_three_rat]

lemma derivative_u3 :
    PowerSeries.derivative u3 = (1 - 2 * X ^ 3) * D3⁻¹ ^ 2 := by
  have hcancel : D3 * D3⁻¹ = 1 := PowerSeries.mul_inv_cancel D3 constantCoeff_D3_ne
  unfold u3
  rw [Derivation.leibniz, PowerSeries.derivative_inv', PowerSeries.derivative_X, derivative_D3]
  simp only [smul_eq_mul, mul_one]
  calc X * (-D3⁻¹ ^ 2 * (1 + 3 * X ^ 2)) + D3⁻¹
      = X * (-D3⁻¹ ^ 2 * (1 + 3 * X ^ 2)) + (D3 * D3⁻¹) * D3⁻¹ := by rw [hcancel, one_mul]
    _ = (D3 - X * (1 + 3 * X ^ 2)) * D3⁻¹ ^ 2 := by ring
    _ = (1 - 2 * X ^ 3) * D3⁻¹ ^ 2 := by unfold D3; ring

/-- Step 2: `X^2(1 + X + X^3) y'(X) + (-1 + X^2 + X^3 + 3X^4 + 2X^6) y(X) + (1 - 2X^3) = 0`. -/
theorem ySeries_ode :
    X ^ 2 * (1 + X + X ^ 3) * PowerSeries.derivative ySeries +
      (-1 + X ^ 2 + X ^ 3 + 3 * X ^ 4 + 2 * X ^ 6) * ySeries + (1 - 2 * X ^ 3) = 0 := by
  have hDy : D3 * ySeries = FSeries.subst u3 := by
    rw [ySeries, ← mul_assoc, PowerSeries.mul_inv_cancel D3 constantCoeff_D3_ne, one_mul]
  have hdiff : D3 * PowerSeries.derivative ySeries + (1 + 3 * X ^ 2) * ySeries =
      (PowerSeries.derivative FSeries).subst u3 * ((1 - 2 * X ^ 3) * D3⁻¹ ^ 2) := by
    have h := congrArg PowerSeries.derivative hDy
    rw [Derivation.leibniz, PowerSeries.derivative_subst hasSubst_u3, derivative_D3,
      derivative_u3] at h
    simp only [smul_eq_mul] at h
    linear_combination h
  have hFsub : u3 ^ 2 * (PowerSeries.derivative FSeries).subst u3 = (1 + X ^ 3) * ySeries - 1 := by
    have h := congrArg (PowerSeries.subst u3) FSeries_ode
    rw [← PowerSeries.coe_substAlgHom hasSubst_u3] at h
    simp only [map_add, map_sub, map_mul, map_pow, map_one, map_zero,
      PowerSeries.coe_substAlgHom hasSubst_u3, subst_X_eq hasSubst_u3, ← hDy] at h
    have huD : (u3 - 1) * (D3 * ySeries) = -(1 + X ^ 3) * ySeries := by
      have hcancel : D3⁻¹ * D3 = 1 := PowerSeries.inv_mul_cancel D3 constantCoeff_D3_ne
      calc (u3 - 1) * (D3 * ySeries)
          = (X * (D3⁻¹ * D3) - D3) * ySeries := by unfold u3; ring
        _ = (X - D3) * ySeries := by rw [hcancel, mul_one]
        _ = -(1 + X ^ 3) * ySeries := by unfold D3; ring
    rw [huD] at h
    linear_combination h
  have hmul := congrArg (X ^ 2 * ·) hdiff
  have hX2u2 : X ^ 2 * D3⁻¹ ^ 2 = u3 ^ 2 := by unfold u3; ring
  have hstep : X ^ 2 * D3 * PowerSeries.derivative ySeries + X ^ 2 * (1 + 3 * X ^ 2) * ySeries =
      (1 - 2 * X ^ 3) * ((1 + X ^ 3) * ySeries - 1) := by
    calc X ^ 2 * D3 * PowerSeries.derivative ySeries + X ^ 2 * (1 + 3 * X ^ 2) * ySeries
        = X ^ 2 * (D3 * PowerSeries.derivative ySeries + (1 + 3 * X ^ 2) * ySeries) := by ring
      _ = X ^ 2 * ((PowerSeries.derivative FSeries).subst u3 * ((1 - 2 * X ^ 3) * D3⁻¹ ^ 2)) :=
          hmul
      _ = (1 - 2 * X ^ 3) * ((X ^ 2 * D3⁻¹ ^ 2) * (PowerSeries.derivative FSeries).subst u3) := by
          ring
      _ = (1 - 2 * X ^ 3) * (u3 ^ 2 * (PowerSeries.derivative FSeries).subst u3) := by rw [hX2u2]
      _ = (1 - 2 * X ^ 3) * ((1 + X ^ 3) * ySeries - 1) := by rw [hFsub]
  unfold D3 at hstep
  linear_combination hstep

/-! ## Section 5: Step 3 — Coefficient Extraction and Main Theorem -/

/-- **Main Theorem (R. J. Mathar's Conjecture on OEIS A177259, Jul 26 2022):**
For every integer `n ≥ 6`,
`a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6)`. -/
theorem mathar_conjecture_A177259_rat (n : ℕ) (hn : 6 ≤ n) :
    a177259Q n =
      ((n : ℚ) - 1) * a177259Q (n - 1) + ((n : ℚ) - 1) * a177259Q (n - 2) +
        a177259Q (n - 3) + ((n : ℚ) - 1) * a177259Q (n - 4) + 2 * a177259Q (n - 6) := by
  have h := congrArg (coeff n) ySeries_ode
  have hexp : X ^ 2 * (1 + X + X ^ 3) * PowerSeries.derivative ySeries +
      (-1 + X ^ 2 + X ^ 3 + 3 * X ^ 4 + 2 * X ^ 6) * ySeries + (1 - 2 * X ^ 3) =
      X ^ 2 * PowerSeries.derivative ySeries + X ^ 3 * PowerSeries.derivative ySeries +
        X ^ 5 * PowerSeries.derivative ySeries - ySeries + X ^ 2 * ySeries + X ^ 3 * ySeries +
        C (3 : ℚ) * (X ^ 4 * ySeries) + C (2 : ℚ) * (X ^ 6 * ySeries) + 1 -
        C (2 : ℚ) * X ^ 3 := by
    rw [C_two_rat, C_three_rat]
    ring
  rw [hexp] at h
  simp only [map_add, map_sub, map_zero, coeff_C_mul, PowerSeries.coeff_X_pow_mul',
    coeff_one, coeff_X_pow] at h
  have h2 : 2 ≤ n := by omega
  have h3 : 3 ≤ n := by omega
  have h4 : 4 ≤ n := by omega
  have h5 : 5 ≤ n := by omega
  have h6 : 6 ≤ n := by omega
  have hn0 : n ≠ 0 := by omega
  have hn3 : n ≠ 3 := by omega
  simp only [h2, h3, h4, h5, h6, hn0, hn3, ↓reduceIte] at h
  rw [coeff_derivative, coeff_derivative, coeff_derivative] at h
  have hsub2 : n - 2 + 1 = n - 1 := by omega
  have hsub3 : n - 3 + 1 = n - 2 := by omega
  have hsub5 : n - 5 + 1 = n - 4 := by omega
  rw [hsub2, hsub3, hsub5] at h
  have hc2 : ((n - 2 : ℕ) : ℚ) + 1 = (n : ℚ) - 1 := by
    have : ((n - 2 : ℕ) : ℚ) + 2 = (n : ℚ) := by exact_mod_cast Nat.sub_add_cancel h2
    linarith
  have hc3 : ((n - 3 : ℕ) : ℚ) + 1 = (n : ℚ) - 2 := by
    have : ((n - 3 : ℕ) : ℚ) + 3 = (n : ℚ) := by exact_mod_cast Nat.sub_add_cancel h3
    linarith
  have hc5 : ((n - 5 : ℕ) : ℚ) + 1 = (n : ℚ) - 4 := by
    have : ((n - 5 : ℕ) : ℚ) + 5 = (n : ℚ) := by exact_mod_cast Nat.sub_add_cancel h5
    linarith
  rw [hc2, hc3, hc5] at h
  simp only [coeff_ySeries_eq_a177259Q] at h
  linarith

/-- Exact integer version of Mathar's 2022 recurrence for OEIS **A177259**. -/
theorem mathar_conjecture_A177259 (n : ℕ) (hn : 6 ≤ n) :
    a177259 n =
      ((n : ℤ) - 1) * a177259 (n - 1) + ((n : ℤ) - 1) * a177259 (n - 2) +
        a177259 (n - 3) + ((n : ℤ) - 1) * a177259 (n - 4) + 2 * a177259 (n - 6) := by
  have h := mathar_conjecture_A177259_rat n hn
  simp only [← a177259_cast_eq] at h
  exact_mod_cast h

/-- Initial values `a(0)..a(6) = 1, 0, 1, 1, 9, 41, 258`, matching live OEIS A177259. -/
lemma a177259_initial :
    (a177259 0, a177259 1, a177259 2, a177259 3, a177259 4, a177259 5, a177259 6) =
      (1, 0, 1, 1, 9, 41, 258) := by
  decide

#print axioms a177259_cast_eq
#print axioms coeff_ySeries_eq_a177259Q
#print axioms ySeries_ode
#print axioms mathar_conjecture_A177259_rat
#print axioms mathar_conjecture_A177259

end OpenMath.OeisA177259
