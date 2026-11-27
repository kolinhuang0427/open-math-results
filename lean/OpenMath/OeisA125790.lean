import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Eval.Coeff
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.RingTheory.PowerSeries.Inverse
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Tactic

/-!
# OEIS A125790: Mikhail Kurkov's May 2025 Row Generating Function Conjecture

Primary source:
OEIS **A125790** (author: Paul D. Hanna, Dec 10 2006; rev. 47, `2026-03-22`):
- **Recurrence:** `T(n, k) = T(n, k - 1) + T(n - 1, 2 * k)` for `n > 0, k > 0`, with
  `T(0, n) = T(n, 0) = 1` for `n >= 0`.
- **Conjecture (Mikhail Kurkov, May 03 2025):**
  `g.f. for n-th row is (Sum_{i=0..n-1} x^i Sum_{j=0..i} binomial(n+1,j)*T(n,i-j)*(-1)^j)/(1-x)^(n+1) for n > 0.`

This file formalizes the complete proof with zero `sorry`, zero `native_decide`, and only
standard Lean axioms `[propext, Classical.choice, Quot.sound]`:
1. Exact OEIS recurrence `a125790` (plus axiomatic uniqueness for any `T : ℕ → ℕ → ℕ` satisfying
   the OEIS recurrence).
2. Step 1 (`exists_row_poly`): For every `n : ℕ`, there exists a polynomial `P : ℚ[X]` of degree
   at most `n` such that `P.eval (k : ℚ) = (a125790 n k : ℚ)` for all `k : ℕ`, and for `n ≥ 1`,
   `P.eval (-1 : ℚ) = 0`.
3. Step 2 (`kurkov_row_gf_mul`, `kurkov_row_gf`, `kurkov_row_gf_of_recurrence`): For every `n ≥ 1`,
   in the formal power series ring `ℚ⟦X⟧`,
   `rowGF n = kurkovNum n * ((1 - PowerSeries.X) ^ (n + 1))⁻¹`.
-/

namespace OpenMath.OeisA125790

open Polynomial
open scoped BigOperators

/-! ## Section 1: OEIS A125790 Array Definition -/

/-- OEIS `A125790`: `T(0, k) = 1`, `T(n, 0) = 1`, and
`T(n, k) = T(n, k - 1) + T(n - 1, 2 * k)` for `n > 0, k > 0`. -/
def a125790 : ℕ → ℕ → ℕ
  | 0, _ => 1
  | _ + 1, 0 => 1
  | n + 1, k + 1 => a125790 (n + 1) k + a125790 n (2 * (k + 1))

@[simp] lemma a125790_zero_left (k : ℕ) : a125790 0 k = 1 := by
  rw [a125790]

@[simp] lemma a125790_zero_right (n : ℕ) : a125790 n 0 = 1 := by
  cases n <;> rw [a125790]

lemma a125790_succ_succ (n k : ℕ) :
    a125790 (n + 1) (k + 1) = a125790 (n + 1) k + a125790 n (2 * (k + 1)) := by
  rw [a125790]

/-- Literal OEIS recurrence form for `n > 0, k > 0`. -/
lemma a125790_rec {n k : ℕ} (hn : 0 < n) (hk : 0 < k) :
    a125790 n k = a125790 n (k - 1) + a125790 (n - 1) (2 * k) := by
  obtain ⟨n', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hn.ne'
  obtain ⟨k', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk.ne'
  simp [a125790_succ_succ]

/-! ## Section 2: Polynomial Degree Bounds and Backward Difference Operator `∇` -/

lemma coeff_sum_eq {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) (d : ℕ) :
    (∑ i ∈ s, f i).coeff d = ∑ i ∈ s, (f i).coeff d :=
  map_sum (lcoeff ℚ d) f s

lemma eval_sum_eq {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) (t : ℚ) :
    (∑ i ∈ s, f i).eval t = ∑ i ∈ s, (f i).eval t :=
  map_sum (evalRingHom t) f s

/-- Predicate expressing that all coefficients of `P` of degree `> m` vanish. -/
def HasDegLe (m : ℕ) (P : ℚ[X]) : Prop :=
  ∀ d : ℕ, m < d → P.coeff d = 0

/-- Backward difference operator `(∇ P)(t) = P(t) - P(t - 1)` in `ℚ[X]`. -/
noncomputable def bdiff (P : ℚ[X]) : ℚ[X] :=
  P - P.comp (X - 1)

lemma hasDegLe_zero (m : ℕ) : HasDegLe m 0 := by
  intro d _; simp

lemma hasDegLe_C (m : ℕ) (a : ℚ) : HasDegLe m (C a) := by
  intro d hd
  rw [coeff_C]
  exact ite_eq_right (fun h => by omega)

lemma hasDegLe_one (m : ℕ) : HasDegLe m 1 := by
  simpa using hasDegLe_C m 1

lemma hasDegLe_X_pow (k : ℕ) : HasDegLe k (X ^ k) := by
  intro d hd
  rw [coeff_X_pow]
  exact ite_eq_right (fun h => by omega)

lemma hasDegLe_mono {m m' : ℕ} {P : ℚ[X]} (hmm' : m ≤ m') (hP : HasDegLe m P) :
    HasDegLe m' P :=
  fun d hd => hP d (lt_of_le_of_lt hmm' hd)

lemma hasDegLe_add {m : ℕ} {P Q : ℚ[X]} (hP : HasDegLe m P) (hQ : HasDegLe m Q) :
    HasDegLe m (P + Q) := by
  intro d hd
  rw [coeff_add, hP d hd, hQ d hd, add_zero]

lemma hasDegLe_sub {m : ℕ} {P Q : ℚ[X]} (hP : HasDegLe m P) (hQ : HasDegLe m Q) :
    HasDegLe m (P - Q) := by
  intro d hd
  rw [coeff_sub, hP d hd, hQ d hd, sub_zero]

lemma hasDegLe_C_mul {m : ℕ} (a : ℚ) {P : ℚ[X]} (hP : HasDegLe m P) :
    HasDegLe m (C a * P) := by
  intro d hd
  rw [coeff_C_mul, hP d hd, mul_zero]

lemma hasDegLe_sum {ι : Type*} {s : Finset ι} {m : ℕ} {f : ι → ℚ[X]}
    (hf : ∀ i ∈ s, HasDegLe m (f i)) : HasDegLe m (∑ i ∈ s, f i) := by
  intro d hd
  rw [coeff_sum_eq]
  exact Finset.sum_eq_zero fun i hi => hf i hi d hd

lemma eq_sum_range_of_hasDegLe {m : ℕ} {P : ℚ[X]} (hP : HasDegLe m P) :
    P = ∑ k ∈ Finset.range (m + 1), C (P.coeff k) * X ^ k := by
  ext d
  rw [coeff_sum_eq]
  simp_rw [coeff_C_mul_X_pow]
  by_cases hd : d ≤ m
  · rw [Finset.sum_eq_single d]
    · simp
    · intro k _ hk
      exact ite_eq_right (fun h => hk h.symm)
    · intro h
      exact absurd (Finset.mem_range.mpr (by omega)) h
  · rw [hP d (by omega)]
    symm
    refine Finset.sum_eq_zero fun k hk => ?_
    have hkm : k < m + 1 := Finset.mem_range.mp hk
    exact ite_eq_right (fun h => by omega)

lemma hasDegLe_comp_C_mul_X {m : ℕ} {P : ℚ[X]} (c : ℚ) (hP : HasDegLe m P) :
    HasDegLe m (P.comp (C c * X)) := by
  rw [eq_sum_range_of_hasDegLe hP, sum_comp]
  refine hasDegLe_sum fun k hk => ?_
  have hkm : k ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  rw [mul_comp, C_comp, pow_comp, X_comp, mul_pow, ← C_pow, ← mul_assoc, ← C_mul]
  exact hasDegLe_C_mul _ (hasDegLe_mono hkm (hasDegLe_X_pow k))

@[simp] lemma bdiff_zero : bdiff 0 = 0 := by simp [bdiff]

@[simp] lemma bdiff_C (a : ℚ) : bdiff (C a) = 0 := by simp [bdiff]

@[simp] lemma bdiff_one : bdiff 1 = 0 := by simp [bdiff]

lemma bdiff_add (P Q : ℚ[X]) : bdiff (P + Q) = bdiff P + bdiff Q := by
  simp [bdiff, add_comp]; ring

lemma bdiff_sub (P Q : ℚ[X]) : bdiff (P - Q) = bdiff P - bdiff Q := by
  simp [bdiff, sub_comp]; ring

lemma bdiff_C_mul (a : ℚ) (P : ℚ[X]) : bdiff (C a * P) = C a * bdiff P := by
  simp [bdiff, mul_comp]; ring

lemma bdiff_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) :
    bdiff (∑ i ∈ s, f i) = ∑ i ∈ s, bdiff (f i) := by
  simp [bdiff, sum_comp, Finset.sum_sub_distrib]

lemma bdiff_eval (P : ℚ[X]) (t : ℚ) : (bdiff P).eval t = P.eval t - P.eval (t - 1) := by
  simp [bdiff, eval_comp]

/-- Explicit binomial expansion of `bdiff (X ^ (d + 1))`. -/
lemma bdiff_X_pow_succ (d : ℕ) :
    bdiff (X ^ (d + 1)) =
      C ((d + 1 : ℚ)) * X ^ d -
        ∑ j ∈ Finset.range d,
          C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) * X ^ j := by
  unfold bdiff
  rw [pow_comp, X_comp]
  have hsub : (X - 1 : ℚ[X]) ^ (d + 1) =
      ∑ j ∈ Finset.range (d + 2),
        C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) * X ^ j := by
    have h1 : (X - 1 : ℚ[X]) = X + (-1 : ℚ[X]) := sub_eq_add_neg X 1
    rw [h1, add_pow]
    refine Finset.sum_congr rfl fun j _ => ?_
    have hneg : (-1 : ℚ[X]) ^ (d + 1 - j) = C ((-1 : ℚ) ^ (d + 1 - j)) := by
      rw [← C_1, ← C_neg, ← C_pow]
    rw [hneg, ← C_eq_natCast, C_mul]
    ring
  rw [hsub, Finset.sum_range_succ, Finset.sum_range_succ]
  have htop : C (((-1 : ℚ) ^ (d + 1 - (d + 1))) * (Nat.choose (d + 1) (d + 1) : ℚ)) * X ^ (d + 1) =
      X ^ (d + 1) := by
    simp
  have hmid : C (((-1 : ℚ) ^ (d + 1 - d)) * (Nat.choose (d + 1) d : ℚ)) * X ^ d =
      -(C ((d + 1 : ℚ)) * X ^ d) := by
    have h1 : d + 1 - d = 1 := by omega
    rw [h1, pow_one, Nat.choose_succ_self_right, ← neg_mul]
    congr 1
    rw [← map_neg]
    congr 1
    push_cast
    ring
  rw [htop, hmid]
  ring

/-- Existence of a discrete antiderivative of `X ^ d` of degree `≤ d + 1` vanishing at `0`. -/
lemma exists_bdiff_eq_X_pow :
    ∀ d : ℕ, ∃ Q : ℚ[X], HasDegLe (d + 1) Q ∧ Q.eval 0 = 0 ∧ bdiff Q = X ^ d := by
  intro d
  induction d using Nat.strong_induction_on with
  | ind d ih =>
    choose Q hQ using fun (j : ℕ) (hj : j < d) => ih j hj
    let R : ℚ[X] := ∑ j ∈ Finset.range d,
      C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) *
        if hj : j < d then Q j hj else 0
    have hR_deg : HasDegLe (d + 1) R := by
      refine hasDegLe_sum fun j hj => ?_
      have hj' : j < d := Finset.mem_range.mp hj
      rw [dite_eq_left hj']
      exact hasDegLe_C_mul _ (hasDegLe_mono (by omega) (hQ j hj').1)
    have hR_eval : R.eval 0 = 0 := by
      dsimp only [R]
      rw [eval_sum_eq]
      refine Finset.sum_eq_zero fun j hj => ?_
      have hj' : j < d := Finset.mem_range.mp hj
      rw [dite_eq_left hj', eval_mul, (hQ j hj').2.1, mul_zero]
    have hR_bdiff : bdiff R =
        ∑ j ∈ Finset.range d,
          C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) * X ^ j := by
      simp only [R, bdiff_sum]
      refine Finset.sum_congr rfl fun j hj => ?_
      have hj' : j < d := Finset.mem_range.mp hj
      rw [dite_eq_left hj', bdiff_C_mul, (hQ j hj').2.2]
    let invD : ℚ := ((d + 1 : ℚ))⁻¹
    refine ⟨C invD * (X ^ (d + 1) + R), ?_, ?_, ?_⟩
    · exact hasDegLe_C_mul invD (hasDegLe_add (hasDegLe_X_pow (d + 1)) hR_deg)
    · simp [hR_eval]
    · rw [bdiff_C_mul, bdiff_add, bdiff_X_pow_succ, hR_bdiff]
      have hne : (d + 1 : ℚ) ≠ 0 := by positivity
      have hcancel : C invD * (C (d + 1 : ℚ) * X ^ d) = X ^ d := by
        rw [← mul_assoc, ← C_mul]
        simp [invD, hne]
      calc
        C invD * (C (d + 1 : ℚ) * X ^ d -
            ∑ j ∈ Finset.range d,
              C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) * X ^ j +
            ∑ j ∈ Finset.range d,
              C (((-1 : ℚ) ^ (d + 1 - j)) * (Nat.choose (d + 1) j : ℚ)) * X ^ j)
            = C invD * (C (d + 1 : ℚ) * X ^ d) := by ring
        _ = X ^ d := hcancel

/-- Every polynomial `g` of degree `≤ m` has a discrete antiderivative `F` of degree `≤ m + 1`
vanishing at `0`. -/
lemma exists_bdiff_eq {m : ℕ} {g : ℚ[X]} (hg : HasDegLe m g) :
    ∃ F : ℚ[X], HasDegLe (m + 1) F ∧ F.eval 0 = 0 ∧ bdiff F = g := by
  choose Q hQ using exists_bdiff_eq_X_pow
  refine ⟨∑ d ∈ Finset.range (m + 1), C (g.coeff d) * Q d, ?_, ?_, ?_⟩
  · refine hasDegLe_sum fun d hd => ?_
    have hdm : d ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hd)
    exact hasDegLe_C_mul _ (hasDegLe_mono (by omega) (hQ d).1)
  · rw [eval_sum_eq]
    refine Finset.sum_eq_zero fun d _ => ?_
    rw [eval_mul, (hQ d).2.1, mul_zero]
  · rw [bdiff_sum]
    conv_rhs => rw [eq_sum_range_of_hasDegLe hg]
    refine Finset.sum_congr rfl fun d _ => ?_
    rw [bdiff_C_mul, (hQ d).2.2]

/-! ## Section 3: Vanishing of Iterated Backward Differences -/

lemma bdiff_eq_zero_of_hasDegLe_zero {P : ℚ[X]} (hP : HasDegLe 0 P) : bdiff P = 0 := by
  rw [eq_sum_range_of_hasDegLe hP]
  simp [bdiff_C]

lemma hasDegLe_bdiff {m : ℕ} {P : ℚ[X]} (hP : HasDegLe (m + 1) P) : HasDegLe m (bdiff P) := by
  rw [eq_sum_range_of_hasDegLe hP, bdiff_sum]
  refine hasDegLe_sum fun k hk => ?_
  have hkm : k ≤ m + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  rw [bdiff_C_mul]
  cases k with
  | zero =>
    simp [hasDegLe_zero]
  | succ d =>
    rw [bdiff_X_pow_succ]
    refine hasDegLe_C_mul _ (hasDegLe_sub ?_ ?_)
    · exact hasDegLe_C_mul _ (hasDegLe_mono (by omega) (hasDegLe_X_pow d))
    · refine hasDegLe_sum fun j hj => ?_
      have hjd : j < d := Finset.mem_range.mp hj
      exact hasDegLe_C_mul _ (hasDegLe_mono (by omega) (hasDegLe_X_pow j))

lemma bdiff_iterate_eq_zero_of_hasDegLe :
    ∀ (n : ℕ) {P : ℚ[X]}, HasDegLe n P → bdiff^[n + 1] P = 0
  | 0, P, hP => by
    simpa using bdiff_eq_zero_of_hasDegLe_zero hP
  | n + 1, P, hP => by
    rw [Function.iterate_succ_apply]
    exact bdiff_iterate_eq_zero_of_hasDegLe n (hasDegLe_bdiff hP)

/-- Explicit binomial expansion of the `r`-th iterated backward difference `∇^r P`. -/
lemma bdiff_iterate_eq (r : ℕ) (P : ℚ[X]) :
    bdiff^[r] P =
      ∑ j ∈ Finset.range (r + 1),
        C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ j) * P.comp (X - C (j : ℚ)) := by
  induction r with
  | zero =>
    simp
  | succ r ih =>
    rw [Function.iterate_succ_apply', ih, bdiff_sum]
    have hterm : ∀ j : ℕ,
        bdiff (C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ j) * P.comp (X - C (j : ℚ))) =
          C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ j) * P.comp (X - C (j : ℚ)) +
          C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ (j + 1)) * P.comp (X - C ((j + 1 : ℕ) : ℚ)) := by
      intro j
      rw [bdiff_C_mul]
      unfold bdiff
      rw [comp_assoc]
      have hshift : (X - C (j : ℚ)).comp (X - 1) = X - C ((j + 1 : ℕ) : ℚ) := by
        simp [sub_comp, X_comp, Nat.cast_add, map_add]
        ring
      rw [hshift]
      have hsign : C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ (j + 1)) =
          -(C ((Nat.choose r j : ℚ) * (-1 : ℚ) ^ j)) := by
        rw [pow_succ, ← map_neg]
        congr 1
        ring
      rw [hsign]
      ring
    simp_rw [hterm, Finset.sum_add_distrib]
    rw [Finset.sum_range_succ' _ r, Finset.sum_range_succ _ r]
    symm
    rw [Finset.sum_range_succ' _ (r + 1), Finset.sum_range_succ _ r]
    simp only [Nat.choose_zero_right, Nat.choose_self, Nat.cast_one, pow_zero, one_mul,
      Nat.cast_zero]
    have hmid :
        ∑ k ∈ Finset.range r,
          C ((Nat.choose (r + 1) (k + 1) : ℚ) * (-1 : ℚ) ^ (k + 1)) *
            P.comp (X - C ((k + 1 : ℕ) : ℚ)) =
        (∑ k ∈ Finset.range r,
          C ((Nat.choose r (k + 1) : ℚ) * (-1 : ℚ) ^ (k + 1)) *
            P.comp (X - C ((k + 1 : ℕ) : ℚ))) +
        (∑ k ∈ Finset.range r,
          C ((Nat.choose r k : ℚ) * (-1 : ℚ) ^ (k + 1)) *
            P.comp (X - C ((k + 1 : ℕ) : ℚ))) := by
      rw [← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun k _ => ?_
      rw [Nat.choose_succ_succ, Nat.cast_add]
      have hadd :
          C (((Nat.choose r k : ℚ) + (Nat.choose r (k + 1) : ℚ)) * (-1 : ℚ) ^ (k + 1)) =
          C ((Nat.choose r (k + 1) : ℚ) * (-1 : ℚ) ^ (k + 1)) +
          C ((Nat.choose r k : ℚ) * (-1 : ℚ) ^ (k + 1)) := by
        rw [← map_add]
        congr 1
        ring
      rw [hadd, add_mul]
    rw [hmid]
    ring

/-- If `deg P ≤ n`, then the `(n + 1)`-th backward difference of `P` vanishes at every `t : ℚ`. -/
lemma bdiff_sum_eq_zero_of_hasDegLe {n : ℕ} {P : ℚ[X]} (hP : HasDegLe n P) (t : ℚ) :
    ∑ j ∈ Finset.range (n + 2),
      (Nat.choose (n + 1) j : ℚ) * (-1 : ℚ) ^ j * P.eval (t - (j : ℚ)) = 0 := by
  have hzero : (bdiff^[n + 1] P).eval t = 0 := by
    rw [bdiff_iterate_eq_zero_of_hasDegLe n hP, eval_zero]
  rw [bdiff_iterate_eq, eval_sum_eq] at hzero
  simpa [eval_mul, eval_C, eval_comp, eval_sub, eval_X] using hzero

/-! ## Section 4: Step 1 — Polynomiality of Rows and Boundary Vanishing `P_n(-1) = 0` -/

/-- For every `n : ℕ`, row `n` of OEIS `A125790` agrees with a polynomial `P_n ∈ ℚ[X]` of degree
`≤ n`, and for `n ≥ 1` satisfies `P_n(-1) = 0`. -/
theorem exists_row_poly (n : ℕ) :
    ∃ P : ℚ[X], HasDegLe n P ∧
      (∀ k : ℕ, P.eval (k : ℚ) = (a125790 n k : ℚ)) ∧
      (1 ≤ n → P.eval (-1 : ℚ) = 0) := by
  induction n with
  | zero =>
    refine ⟨1, hasDegLe_one 0, fun k => by simp, fun h => by omega⟩
  | succ n ih =>
    obtain ⟨P_prev, hdeg_prev, heval_prev, _⟩ := ih
    let g : ℚ[X] := P_prev.comp (C 2 * X)
    have hg_deg : HasDegLe n g := hasDegLe_comp_C_mul_X 2 hdeg_prev
    obtain ⟨F, hF_deg, hF_zero, hF_bdiff⟩ := exists_bdiff_eq hg_deg
    refine ⟨F + 1, hasDegLe_add hF_deg (hasDegLe_one (n + 1)), ?_, ?_⟩
    · have hrec : ∀ t : ℚ, (F + 1).eval t - (F + 1).eval (t - 1) = P_prev.eval (2 * t) := by
        intro t
        have h1 : (bdiff (F + 1)).eval t = g.eval t := by
          rw [bdiff_add, bdiff_one, add_zero, hF_bdiff]
        rw [bdiff_eval] at h1
        simpa [g, eval_comp] using h1
      intro k
      induction k with
      | zero =>
        simp [hF_zero]
      | succ k ihk =>
        have hstep := hrec ((k + 1 : ℕ) : ℚ)
        have hsub : ((k + 1 : ℕ) : ℚ) - 1 = (k : ℚ) := by push_cast; ring
        rw [hsub, ihk] at hstep
        have h2 : 2 * ((k + 1 : ℕ) : ℚ) = ((2 * (k + 1) : ℕ) : ℚ) := by push_cast; ring
        rw [h2, heval_prev (2 * (k + 1))] at hstep
        rw [a125790_succ_succ]
        push_cast at hstep ⊢
        linarith
    · intro _
      have h0 : (bdiff (F + 1)).eval 0 = g.eval 0 := by
        rw [bdiff_add, bdiff_one, add_zero, hF_bdiff]
      rw [bdiff_eval] at h0
      have hP0 : (F + 1).eval 0 = 1 := by simp [hF_zero]
      have hg0 : g.eval 0 = 1 := by
        have := heval_prev 0
        simpa [g, eval_comp] using this
      rw [hP0, hg0, zero_sub] at h0
      linarith

/-! ## Section 5: Step 2 — Formal Power Series Identity for Kurkov's Conjecture -/

/-- Ordinary generating function of row `n` of OEIS `A125790` in `ℚ⟦X⟧`. -/
noncomputable def rowGF (n : ℕ) : PowerSeries ℚ :=
  PowerSeries.mk fun k => (a125790 n k : ℚ)

/-- Numerator of Kurkov's conjectured generating function for row `n` (`n > 0`):
`∑_{i=0}^{n-1} x^i ∑_{j=0}^{i} binomial(n+1, j) * T(n, i - j) * (-1)^j`. -/
noncomputable def kurkovNum (n : ℕ) : PowerSeries ℚ :=
  ∑ i ∈ Finset.range n,
    PowerSeries.X ^ i *
      PowerSeries.C
        (∑ j ∈ Finset.range (i + 1),
          (Nat.choose (n + 1) j : ℚ) * (a125790 n (i - j) : ℚ) * (-1 : ℚ) ^ j)

lemma coeff_one_sub_X_pow (m j : ℕ) :
    PowerSeries.coeff j ((1 - PowerSeries.X : PowerSeries ℚ) ^ m) =
      if j ≤ m then (Nat.choose m j : ℚ) * (-1 : ℚ) ^ j else 0 := by
  have hexp : (1 - PowerSeries.X : PowerSeries ℚ) ^ m =
      ∑ r ∈ Finset.range (m + 1),
        PowerSeries.C ((Nat.choose m r : ℚ) * (-1 : ℚ) ^ r) * PowerSeries.X ^ r := by
    have h1 : (1 - PowerSeries.X : PowerSeries ℚ) = (-PowerSeries.X) + 1 := by ring
    rw [h1, add_pow]
    refine Finset.sum_congr rfl fun r _ => ?_
    rw [one_pow, mul_one, neg_eq_neg_one_mul, mul_pow]
    have hneg : (-1 : PowerSeries ℚ) ^ r = PowerSeries.C ((-1 : ℚ) ^ r) := by
      rw [← map_one PowerSeries.C, ← map_neg PowerSeries.C, ← map_pow PowerSeries.C]
    have hnat : (Nat.choose m r : PowerSeries ℚ) = PowerSeries.C (Nat.choose m r : ℚ) := by
      simp
    rw [hneg, hnat, map_mul]
    ring
  rw [hexp, map_sum]
  simp_rw [PowerSeries.coeff_C_mul_X_pow]
  by_cases hj : j ≤ m
  · rw [ite_eq_left hj]
    rw [Finset.sum_eq_single j]
    · simp
    · intro r _ hr
      exact ite_eq_right (fun h => hr h.symm)
    · intro h
      exact absurd (Finset.mem_range.mpr (by omega)) h
  · rw [ite_eq_right (fun h => absurd h hj)]
    refine Finset.sum_eq_zero fun r hr => ?_
    have hrm : r < m + 1 := Finset.mem_range.mp hr
    exact ite_eq_right (fun h => by omega)

lemma coeff_kurkovNum (n i : ℕ) :
    PowerSeries.coeff i (kurkovNum n) =
      if i < n then
        ∑ j ∈ Finset.range (i + 1),
          (Nat.choose (n + 1) j : ℚ) * (a125790 n (i - j) : ℚ) * (-1 : ℚ) ^ j
      else 0 := by
  unfold kurkovNum
  rw [map_sum]
  simp_rw [mul_comm (PowerSeries.X ^ _), PowerSeries.coeff_C_mul_X_pow]
  by_cases hi : i < n
  · rw [ite_eq_left hi]
    rw [Finset.sum_eq_single i]
    · simp
    · intro r _ hr
      exact ite_eq_right (fun h => hr h.symm)
    · intro h
      exact absurd (Finset.mem_range.mpr hi) h
  · rw [ite_eq_right (fun h => absurd h hi)]
    refine Finset.sum_eq_zero fun r hr => ?_
    have hrn : r < n := Finset.mem_range.mp hr
    exact ite_eq_right (fun h => by omega)

/-- Product form of Kurkov's conjecture: for every `n ≥ 1`,
`(1 - X)^(n + 1) * rowGF n = kurkovNum n` in `ℚ⟦X⟧`. -/
theorem kurkov_row_gf_mul {n : ℕ} (hn : 1 ≤ n) :
    (1 - PowerSeries.X : PowerSeries ℚ) ^ (n + 1) * rowGF n = kurkovNum n := by
  obtain ⟨P, hdeg, heval, hneg1⟩ := exists_row_poly n
  have hPneg1 : P.eval (-1 : ℚ) = 0 := hneg1 hn
  ext i
  rw [PowerSeries.coeff_mul, Finset.Nat.sum_antidiagonal_eq_sum_range_succ
    (fun a b => PowerSeries.coeff a ((1 - PowerSeries.X : PowerSeries ℚ) ^ (n + 1)) *
      PowerSeries.coeff b (rowGF n))]
  simp_rw [coeff_one_sub_X_pow, rowGF, PowerSeries.coeff_mk]
  rw [coeff_kurkovNum]
  by_cases hi : i < n
  · rw [ite_eq_left hi]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hji : j ≤ i := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    rw [ite_eq_left (by omega)]
    ring
  · rw [ite_eq_right (fun h => absurd h hi)]
    have hzero := bdiff_sum_eq_zero_of_hasDegLe hdeg (i : ℚ)
    by_cases hin : i = n
    · rw [hin] at hzero ⊢
      rw [Finset.sum_range_succ] at hzero
      have hlast : (Nat.choose (n + 1) (n + 1) : ℚ) * (-1 : ℚ) ^ (n + 1) *
          P.eval ((n : ℚ) - ((n + 1 : ℕ) : ℚ)) = 0 := by
        have hsub : (n : ℚ) - ((n + 1 : ℕ) : ℚ) = -1 := by push_cast; ring
        rw [hsub, hPneg1, mul_zero]
      rw [hlast, add_zero] at hzero
      rw [← hzero]
      refine Finset.sum_congr rfl fun j hj => ?_
      have hjn : j ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
      rw [ite_eq_left (by omega), ← heval (n - j)]
      have hcast : ((n - j : ℕ) : ℚ) = (n : ℚ) - (j : ℚ) := Nat.cast_sub hjn
      rw [hcast]
    · have hi_ge : n + 1 ≤ i := by omega
      have hsum_eq :
          ∑ j ∈ Finset.range (i + 1),
            (if j ≤ n + 1 then (Nat.choose (n + 1) j : ℚ) * (-1 : ℚ) ^ j else 0) *
              (a125790 n (i - j) : ℚ) =
          ∑ j ∈ Finset.range (n + 2),
            (Nat.choose (n + 1) j : ℚ) * (-1 : ℚ) ^ j * (a125790 n (i - j) : ℚ) := by
        rw [← Finset.sum_subset (Finset.range_mono (by omega : n + 2 ≤ i + 1))]
        · refine Finset.sum_congr rfl fun j hj => ?_
          have hjn : j ≤ n + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
          rw [ite_eq_left hjn]
        · intro j _ hjnot
          have hgt : ¬ (j ≤ n + 1) := by
            intro hle
            exact hjnot (Finset.mem_range.mpr (by omega))
          rw [ite_eq_right (fun h => absurd h hgt), zero_mul]
      rw [hsum_eq, ← hzero]
      refine Finset.sum_congr rfl fun j hj => ?_
      have hjn : j ≤ n + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
      have hji : j ≤ i := by omega
      rw [← heval (i - j), Nat.cast_sub hji]

/-- **Main Theorem (Kurkov's May 2025 Conjecture on OEIS `A125790`):**
For every `n ≥ 1`, the row ordinary generating function `rowGF n ∈ ℚ⟦X⟧` equals
`kurkovNum n * ((1 - X) ^ (n + 1))⁻¹`. -/
theorem kurkov_row_gf {n : ℕ} (hn : 1 ≤ n) :
    rowGF n = kurkovNum n * ((1 - PowerSeries.X : PowerSeries ℚ) ^ (n + 1))⁻¹ := by
  have hcc : PowerSeries.constantCoeff ((1 - PowerSeries.X : PowerSeries ℚ) ^ (n + 1)) ≠ 0 := by
    simp
  rw [PowerSeries.eq_mul_inv_iff_mul_eq hcc, mul_comm]
  exact kurkov_row_gf_mul hn

/-- Axiomatic / recurrence-uniqueness version: for ANY array `T : ℕ → ℕ → ℕ` satisfying the OEIS
`A125790` recurrence `T(0, k) = T(n, 0) = 1` and `T(n, k) = T(n, k - 1) + T(n - 1, 2 * k)` for
`n > 0, k > 0`, the row generating function satisfies Kurkov's formula for all `n ≥ 1`. -/
theorem kurkov_row_gf_of_recurrence
    (T : ℕ → ℕ → ℕ)
    (h0_left : ∀ k, T 0 k = 1)
    (h0_right : ∀ n, T n 0 = 1)
    (hrec : ∀ n k, 0 < n → 0 < k → T n k = T n (k - 1) + T (n - 1) (2 * k))
    {n : ℕ} (hn : 1 ≤ n) :
    PowerSeries.mk (fun k => (T n k : ℚ)) =
      (∑ i ∈ Finset.range n,
        PowerSeries.X ^ i *
          PowerSeries.C
            (∑ j ∈ Finset.range (i + 1),
              (Nat.choose (n + 1) j : ℚ) * (T n (i - j) : ℚ) * (-1 : ℚ) ^ j)) *
        ((1 - PowerSeries.X : PowerSeries ℚ) ^ (n + 1))⁻¹ := by
  have hT_eq : ∀ a b, T a b = a125790 a b := by
    intro a
    induction a with
    | zero =>
      intro b
      rw [h0_left b, a125790_zero_left]
    | succ a iha =>
      intro b
      induction b with
      | zero =>
        rw [h0_right (a + 1), a125790_zero_right]
      | succ b ihb =>
        rw [hrec (a + 1) (b + 1) (Nat.succ_pos a) (Nat.succ_pos b)]
        simp only [Nat.add_sub_cancel]
        rw [ihb, iha (2 * (b + 1)), a125790_succ_succ]
  simp_rw [hT_eq]
  exact kurkov_row_gf hn

#print axioms exists_row_poly
#print axioms kurkov_row_gf_mul
#print axioms kurkov_row_gf
#print axioms kurkov_row_gf_of_recurrence

end OpenMath.OeisA125790
