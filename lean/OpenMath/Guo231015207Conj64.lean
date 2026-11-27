import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.Tactic

/-!
# Guo (`arXiv:2310.15207v1`, Section 6, Conjectures 6.4 & 6.3): Dwork-Type `q`-Congruences mod `Φ_{n^s}(q)^2`

This file formalizes the unconditional proof of **both** **Conjecture 6.4** (`\label{conj:4}`,
lines 754–760) and **Conjecture 6.3** (`\label{conj:3}`, lines 749–751; referencing Lemma 2.3
`\label{lem:3}`, lines 277–283) of Victor J. W. Guo,
*"Dwork-type `q`-congruences through the `q`-Lucas theorem"* (`arXiv:2310.15207v1`, `main.tex`):

> **Conjecture 6.4 (`conj:4`).** Let `n ≡ 1 (mod 4)` be an integer greater than `1` and let `r, s`
> be positive integers with `r > s`. Then, modulo `Φ_{n^s}(q)^2`,
> $$\frac{(q; q^2)_{(n^r - 1)/4} (q^{2n}; q^{2n})_{(n^{r-1} - 1)/4}}{(q^2; q^2)_{(n^r - 1)/4} (q^n; q^{2n})_{(n^{r-1} - 1)/4}}
>   \equiv
>   \frac{(q; q^2)_{(n^s - 1)/4} (q^{2n}; q^{2n})_{(n^{s-1} - 1)/4}}{(q^2; q^2)_{(n^s - 1)/4} (q^n; q^{2n})_{(n^{s-1} - 1)/4}}.$$

> **Conjecture 6.3 (`conj:3`).** Under the same hypotheses `n ≡ 1 (mod 4)`, `n > 1`, `r > s ≥ 1`,
> modulo `Φ_{n^s}(q)^2`,
> $$[n]_q \frac{(q^3; q^4)_{(n^r - 1)/2} (q^{5n}; q^{4n})_{(n^{r-1} - 1)/2}}{(q^5; q^4)_{(n^r - 1)/2} (q^{3n}; q^{4n})_{(n^{r-1} - 1)/2}}
>   \equiv
>   [n]_q \frac{(q^3; q^4)_{(n^s - 1)/2} (q^{5n}; q^{4n})_{(n^{s-1} - 1)/2}}{(q^5; q^4)_{(n^s - 1)/2} (q^{3n}; q^{4n})_{(n^{s-1} - 1)/2}}.$$

Here `(a; q)_m = ∏_{k=0}^{m-1} (1 - a q^k)`, `[n]_q = ∑_{k=0}^{n-1} q^k = (1 - q^n)/(1 - q)`,
and `Φ_N(q) = Polynomial.cyclotomic N ℚ`.

## Proof Outline
1. **Rational congruence modulo `Φ_N(q)^2` (`RatCongMod`):** After cancelling common factors in `ℚ[q]`,
   both fractions have denominators coprime to `Φ_N(q)^2`, and their cross-multiplied difference is
   divisible by `Φ_N(q)^2`.
2. **Quotient ring `R₂ = ℚ[q] / (Φ_N(q)^2)`:** Setting `z = 1 - q^N`, we have `z^2 = 0` in `R₂`,
   every `1 - q^a` (`1 ≤ a < N`) is a unit `u_a` in `R₂`, `(1 - q^{a + KN}) = u_a (1 + K w_a z)`
   where `w_a = q^a u_a⁻¹`, and `(w_a + w_{N-a}) z = -z` directly via `z^2 = 0`.
3. **Exact `n`-multiple cancellation & block decomposition:** For both Conjecture 6.4 and
   Conjecture 6.3, the step ratio `T(n, r; q) = R(n, r; q) / R(n, r-1; q)` cancels every `n`-multiple
   factor identically, splits into `M` residue blocks of length `N = n^s`, reduces modulo `Φ_N(q)^2`
   to `1 + M z ∑_{1 ≤ a < N, n ∤ a} ΔQ(a) w_a`, and vanishes by `{a, N - a}` pairing (`ΔQ(N - a) = ΔQ(a)`)
   combined with alternating-sign cancellation on `[1, (N - 1)/2]` and `[1, (N/n - 1)/2]`.
-/

namespace OpenMath.Guo231015207Conj64

open Polynomial

/-! ## Section 1: Primary-Source Definitions (`q`-Pochhammer, `[n]_q`, `Φ_N`, Rational Congruence) -/

/-- `q`-shifted factorial `(a; q)_m = ∏_{k=0}^{m-1} (1 - a q^k)` in `ℚ[q]`. -/
noncomputable def qPoch (a q : Polynomial ℚ) (m : ℕ) : Polynomial ℚ :=
  ∏ k ∈ Finset.range m, (1 - a * q ^ k)

/-- `q`-integer `[n]_q = ∑_{k=0}^{n-1} q^k` in `ℚ[q]`. -/
noncomputable def qNum (n : ℕ) : Polynomial ℚ :=
  ∑ k ∈ Finset.range n, X ^ k

/-- `N`-th cyclotomic polynomial `Φ_N(q)` in `ℚ[q]`. -/
noncomputable def Phi (N : ℕ) : Polynomial ℚ :=
  Polynomial.cyclotomic N ℚ

/-- Exact rational-function congruence `A₁ / B₁ ≡ A₂ / B₂ (mod M)` in `ℚ(q)`:
`B₁, B₂ ≠ 0`, and there exist reduced representations `P₁/Q₁ = A₁/B₁` and `P₂/Q₂ = A₂/B₂`
in `ℚ[q]` with `Q₁, Q₂` coprime to `M` and `M ∣ P₁ * Q₂ - P₂ * Q₁`. -/
def RatCongMod (A₁ B₁ A₂ B₂ M : Polynomial ℚ) : Prop :=
  B₁ ≠ 0 ∧ B₂ ≠ 0 ∧
  ∃ P₁ Q₁ P₂ Q₂ : Polynomial ℚ,
    IsCoprime Q₁ M ∧ IsCoprime Q₂ M ∧
    A₁ * Q₁ = P₁ * B₁ ∧ A₂ * Q₂ = P₂ * B₂ ∧
    M ∣ P₁ * Q₂ - P₂ * Q₁

/-- Numerator of Conjecture 6.4's `R₄(n, r; q)`. -/
noncomputable def num4 (n r : ℕ) : Polynomial ℚ :=
  qPoch X (X ^ 2) ((n ^ r - 1) / 4) * qPoch (X ^ (2 * n)) (X ^ (2 * n)) ((n ^ (r - 1) - 1) / 4)

/-- Denominator of Conjecture 6.4's `R₄(n, r; q)`. -/
noncomputable def den4 (n r : ℕ) : Polynomial ℚ :=
  qPoch (X ^ 2) (X ^ 2) ((n ^ r - 1) / 4) * qPoch (X ^ n) (X ^ (2 * n)) ((n ^ (r - 1) - 1) / 4)

/-- Numerator of Conjecture 6.3's `R₃(n, r; q)`. -/
noncomputable def num3 (n r : ℕ) : Polynomial ℚ :=
  qNum n * qPoch (X ^ 3) (X ^ 4) ((n ^ r - 1) / 2) *
    qPoch (X ^ (5 * n)) (X ^ (4 * n)) ((n ^ (r - 1) - 1) / 2)

/-- Denominator of Conjecture 6.3's `R₃(n, r; q)`. -/
noncomputable def den3 (n r : ℕ) : Polynomial ℚ :=
  qPoch (X ^ 5) (X ^ 4) ((n ^ r - 1) / 2) *
    qPoch (X ^ (3 * n)) (X ^ (4 * n)) ((n ^ (r - 1) - 1) / 2)

/-! ## Section 2: Cyclotomic Coprimality & Arithmetic in `ℚ[q] / (Φ_N(q)^2)` -/

private lemma pow_mod_four_eq_one {n : ℕ} (hn : n % 4 = 1) (k : ℕ) : (n ^ k) % 4 = 1 := by
  induction k with
  | zero => simp
  | succ k ih => rw [pow_succ, Nat.mul_mod, ih, hn]

private lemma one_sub_X_pow_ne_zero {m : ℕ} (hm : 1 ≤ m) :
    (1 - X ^ m : Polynomial ℚ) ≠ 0 := by
  intro h
  have h1 := congrArg (fun p : Polynomial ℚ => p.coeff m) h
  simp only [Polynomial.coeff_sub, Polynomial.coeff_one, Polynomial.coeff_X_pow,
    Polynomial.coeff_zero, ite_true] at h1
  have hm0 : m ≠ 0 := by omega
  simp [hm0] at h1

private lemma qNum_ne_zero {n : ℕ} (hn : 1 ≤ n) : qNum n ≠ 0 := by
  intro h
  have h1 := congrArg (fun p : Polynomial ℚ => p.coeff 0) h
  unfold qNum at h1
  have h0 : (∑ k ∈ Finset.range n, (X ^ k : Polynomial ℚ)).coeff 0 = 1 := by
    change (Polynomial.lcoeff ℚ 0) (∑ k ∈ Finset.range n, (X ^ k : Polynomial ℚ)) = 1
    rw [map_sum]
    simp only [Polynomial.lcoeff_apply, Polynomial.coeff_X_pow]
    rw [Finset.sum_eq_single 0]
    · simp
    · intro k _ hne; simp [Ne.symm hne]
    · intro hmem; exact absurd (Finset.mem_range.mpr hn) hmem
  rw [h0] at h1
  simp at h1

private lemma qNum_mul_one_sub_X (n : ℕ) :
    qNum n * (1 - X) = 1 - X ^ n := by
  unfold qNum
  have h := geom_sum_mul (X : Polynomial ℚ) n
  linear_combination -h

private lemma isCoprime_one_sub_X_pow_Phi {m N : ℕ} (hm : 1 ≤ m) (hndvd : ¬ N ∣ m) :
    IsCoprime (1 - X ^ m : Polynomial ℚ) (Phi N) := by
  have hprod : ∏ d ∈ m.divisors, Phi d = X ^ m - 1 :=
    Polynomial.prod_cyclotomic_eq_X_pow_sub_one hm ℚ
  have hcop_prod : IsCoprime (X ^ m - 1 : Polynomial ℚ) (Phi N) := by
    rw [← hprod]
    refine IsCoprime.prod_left fun d hd => ?_
    have hdne : d ≠ N := fun hEq => hndvd (hEq ▸ Nat.dvd_of_mem_divisors hd)
    exact Polynomial.cyclotomic.isCoprime_rat hdne
  have hneg : (1 - X ^ m : Polynomial ℚ) = -(X ^ m - 1) := by ring
  rw [hneg]
  exact hcop_prod.neg_left

private lemma isCoprime_one_sub_X_pow_Phi_sq {m N : ℕ} (hm : 1 ≤ m) (hndvd : ¬ N ∣ m) :
    IsCoprime (1 - X ^ m : Polynomial ℚ) (Phi N ^ 2) :=
  (isCoprime_one_sub_X_pow_Phi hm hndvd).pow_right

private lemma Phi_dvd_one_sub_X_pow (N : ℕ) :
    Phi N ∣ (1 - X ^ N : Polynomial ℚ) := by
  have h := Polynomial.cyclotomic.dvd_X_pow_sub_one N ℚ
  have hneg : (1 - X ^ N : Polynomial ℚ) = -(X ^ N - 1) := by ring
  rw [hneg]
  exact dvd_neg.mpr h

private lemma isCoprime_qNum_Phi_sq {n N : ℕ} (hn : 1 ≤ n) (hndvd : ¬ N ∣ n) :
    IsCoprime (qNum n) (Phi N ^ 2) := by
  have h1 : IsCoprime (1 - X ^ n : Polynomial ℚ) (Phi N ^ 2) :=
    isCoprime_one_sub_X_pow_Phi_sq hn hndvd
  rw [← qNum_mul_one_sub_X] at h1
  exact h1.of_mul_left_left

/-- Quotient ring `R₂(N) = ℚ[q] / (Φ_N(q)^2)`. -/
private abbrev R2 (N : ℕ) := Polynomial ℚ ⧸ Ideal.span ({Phi N ^ 2} : Set (Polynomial ℚ))

private noncomputable def mk2 (N : ℕ) : Polynomial ℚ →+* R2 N :=
  Ideal.Quotient.mk (Ideal.span ({Phi N ^ 2} : Set (Polynomial ℚ)))

private lemma mk2_eq_iff {N : ℕ} {a b : Polynomial ℚ} :
    mk2 N a = mk2 N b ↔ Phi N ^ 2 ∣ a - b := by
  rw [mk2, Ideal.Quotient.eq, Ideal.mem_span_singleton]

private lemma z_sq_eq_zero (N : ℕ) : (mk2 N (1 - X ^ N)) ^ 2 = 0 := by
  rw [← map_pow, ← map_zero (mk2 N), mk2_eq_iff, sub_zero]
  exact pow_dvd_pow_of_dvd (Phi_dvd_one_sub_X_pow N) 2

private lemma isUnit_mk2_of_isCoprime {N : ℕ} {p : Polynomial ℚ}
    (hcop : IsCoprime p (Phi N ^ 2)) : IsUnit (mk2 N p) := by
  rcases hcop with ⟨u, v, huv⟩
  refine isUnit_iff_exists_inv.mpr ⟨mk2 N u, ?_⟩
  rw [← map_mul, ← map_one (mk2 N), mk2_eq_iff]
  refine ⟨-v, ?_⟩
  linear_combination huv

private lemma one_sub_z_pow {R : Type*} [CommRing R] {z : R} (hz : z ^ 2 = 0) (K : ℕ) :
    (1 - z) ^ K = 1 - (K : R) * z := by
  induction K with
  | zero => simp
  | succ K ih =>
    rw [pow_succ, ih]
    push_cast
    linear_combination (K : R) * hz

/-- Linearization of `1 - q^{a + KN}` in `ℚ[q] / (Φ_N(q)^2)` (Eq. (1) of `PROOF.md`). -/
private lemma mk2_one_sub_X_pow_add_mul {N : ℕ} (a K : ℕ) :
    mk2 N (1 - X ^ (a + K * N)) =
      mk2 N (1 - X ^ a) + (K : R2 N) * mk2 N (X ^ a) * mk2 N (1 - X ^ N) := by
  set z : R2 N := mk2 N (1 - X ^ N)
  have hz2 : z ^ 2 = 0 := z_sq_eq_zero N
  have hXN : mk2 N (X ^ N) = 1 - z := by
    have : (X ^ N : Polynomial ℚ) = 1 - (1 - X ^ N) := by ring
    rw [this, map_sub, map_one]
  have hXpow : mk2 N (X ^ (a + K * N)) = mk2 N (X ^ a) * (1 - (K : R2 N) * z) := by
    rw [pow_add, mul_comm K N, pow_mul, map_mul, map_pow (mk2 N) (X ^ N) K, hXN, one_sub_z_pow hz2 K]
  rw [map_sub, map_one, hXpow, map_sub, map_one]
  ring

/-- Product linearization in any commutative ring with `z ^ 2 = 0`:
`∏ i ∈ S, (1 + c i * z) = 1 + (∑ i ∈ S, c i) * z`. -/
private lemma prod_one_add_mul_z {ι R : Type*} [DecidableEq ι] [CommRing R]
    {z : R} (hz : z ^ 2 = 0) (S : Finset ι) (c : ι → R) :
    ∏ i ∈ S, (1 + c i * z) = 1 + (∑ i ∈ S, c i) * z := by
  induction S using Finset.induction_on with
  | empty => simp
  | insert a S ha ih =>
    rw [Finset.prod_insert ha, Finset.sum_insert ha, ih]
    linear_combination c a * (∑ i ∈ S, c i) * hz

/-- Direct Eq. (2) pairing identity in `ℚ[q] / (Φ_N(q)^2)`:
if `u_a = mk2 N (1 - X^a)` and `u_b = mk2 N (1 - X^(N-a))` are units (`1 ≤ a < N`), then
`(mk2 N (X^a) * u_a⁻¹ + mk2 N (X^(N-a)) * u_b⁻¹) * z = -z`! -/
private lemma pairing_mul_z {N a : ℕ} (_ha1 : 1 ≤ a) (haN : a < N)
    (ua ub : (R2 N)ˣ)
    (hua : (ua : R2 N) = mk2 N (1 - X ^ a))
    (hub : (ub : R2 N) = mk2 N (1 - X ^ (N - a))) :
    (mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) + mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ)) *
      mk2 N (1 - X ^ N) = -mk2 N (1 - X ^ N) := by
  set z : R2 N := mk2 N (1 - X ^ N)
  have hz2 : z ^ 2 = 0 := z_sq_eq_zero N
  have hprod : mk2 N (X ^ a) * mk2 N (X ^ (N - a)) = 1 - z := by
    rw [← map_mul, ← pow_add, Nat.add_sub_cancel' haN.le]
    have : (X ^ N : Polynomial ℚ) = 1 - (1 - X ^ N) := by ring
    rw [this, map_sub, map_one]
  -- Multiply both sides by the unit `ua * ub`!
  have hmul : ((ua : R2 N) * (ub : R2 N)) *
      ((mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) + mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ) + 1) * z) = 0 := by
    have h1 : (ua : R2 N) * (ua⁻¹ : (R2 N)ˣ) = 1 := ua.mul_inv
    have h2 : (ub : R2 N) * (ub⁻¹ : (R2 N)ˣ) = 1 := ub.mul_inv
    have hexpand : ((ua : R2 N) * (ub : R2 N)) *
        (mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) + mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ) + 1) =
        mk2 N (X ^ a) * (ub : R2 N) + mk2 N (X ^ (N - a)) * (ua : R2 N) +
        (ua : R2 N) * (ub : R2 N) := by
      calc _ = ((ua : R2 N) * (ua⁻¹ : (R2 N)ˣ)) * (ub : R2 N) * mk2 N (X ^ a) +
               ((ub : R2 N) * (ub⁻¹ : (R2 N)ˣ)) * (ua : R2 N) * mk2 N (X ^ (N - a)) +
               (ua : R2 N) * (ub : R2 N) := by ring
        _ = _ := by rw [h1, h2]; ring
    rw [← mul_assoc, hexpand, hua, hub, map_sub, map_one, map_sub, map_one]
    have hid : mk2 N (X ^ a) * (1 - mk2 N (X ^ (N - a))) +
        mk2 N (X ^ (N - a)) * (1 - mk2 N (X ^ a)) +
        (1 - mk2 N (X ^ a)) * (1 - mk2 N (X ^ (N - a))) = z := by
      linear_combination -hprod
    rw [hid, ← sq]
    exact hz2
  have hunit : IsUnit ((ua : R2 N) * (ub : R2 N)) := ua.isUnit.mul ub.isUnit
  have hzero : (mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) + mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ) + 1) * z = 0 :=
    hunit.mul_right_eq_zero.mp hmul
  linear_combination hzero

/-- Master Ratio Linearization Lemma in `ℚ[q] / (Φ_N(q)^2)`:
Given finite residue set `S ⊆ {1, ..., N - 1}` and quotient shifts `qNum, qDen : ℕ → ℕ`,
if `(∑ a ∈ S, ((qNum a : ℤ) - (qDen a : ℤ)) * w_a) * z = 0` in `R2 N`, then
`∏ a ∈ S, (1 - X^(a + (c + qNum a) * N)) ≡ ∏ a ∈ S, (1 - X^(a + (c + qDen a) * N)) (mod Φ_N^2)`! -/
private lemma block_prod_congr_mod_Phi_sq {N : ℕ} (S : Finset ℕ)
    (hS : ∀ a ∈ S, 1 ≤ a ∧ a < N)
    (c : ℕ) (qNum qDen : ℕ → ℕ)
    (hsum : ∀ w : ℕ → R2 N,
      (∀ a ∈ S, mk2 N (1 - X ^ a) * w a = mk2 N (X ^ a)) →
      (∑ a ∈ S, (((qNum a : ℤ) - (qDen a : ℤ) : ℤ) : R2 N) * w a) * mk2 N (1 - X ^ N) = 0) :
    mk2 N (∏ a ∈ S, (1 - X ^ (a + (c + qNum a) * N))) =
    mk2 N (∏ a ∈ S, (1 - X ^ (a + (c + qDen a) * N))) := by
  set z : R2 N := mk2 N (1 - X ^ N)
  have hz2 : z ^ 2 = 0 := z_sq_eq_zero N
  -- Choose inverses `w a` of `mk2 N (1 - X ^ a)` times `mk2 N (X ^ a)` for `a ∈ S`
  have hu_ex : ∀ a : ℕ, ∃ w : R2 N, (a ∈ S → mk2 N (1 - X ^ a) * w = mk2 N (X ^ a)) := by
    intro a
    by_cases ha : a ∈ S
    · obtain ⟨ha1, haN⟩ := hS a ha
      have hndvd : ¬ N ∣ a := fun hd => by have := Nat.le_of_dvd ha1 hd; omega
      obtain ⟨u, hu⟩ := isUnit_mk2_of_isCoprime (isCoprime_one_sub_X_pow_Phi_sq ha1 hndvd)
      refine ⟨mk2 N (X ^ a) * (u⁻¹ : (R2 N)ˣ), fun _ => ?_⟩
      rw [← hu]
      calc (u : R2 N) * (mk2 N (X ^ a) * (u⁻¹ : (R2 N)ˣ))
          = ((u : R2 N) * (u⁻¹ : (R2 N)ˣ)) * mk2 N (X ^ a) := by ring
        _ = mk2 N (X ^ a) := by rw [u.mul_inv, one_mul]
    · exact ⟨0, fun h => absurd h ha⟩
  choose w hw using hu_ex
  have hfac : ∀ (f : ℕ → ℕ),
      mk2 N (∏ a ∈ S, (1 - X ^ (a + (c + f a) * N))) =
      (∏ a ∈ S, mk2 N (1 - X ^ a)) * (1 + (∑ a ∈ S, (((c + f a : ℕ) : R2 N) * w a)) * z) := by
    intro f
    rw [map_prod]
    have hpt : ∀ a ∈ S, mk2 N (1 - X ^ (a + (c + f a) * N)) =
        mk2 N (1 - X ^ a) * (1 + ((c + f a : ℕ) : R2 N) * w a * z) := by
      intro a ha
      rw [mk2_one_sub_X_pow_add_mul]
      have hwa := hw a ha
      calc mk2 N (1 - X ^ a) + ((c + f a : ℕ) : R2 N) * mk2 N (X ^ a) * z
          = mk2 N (1 - X ^ a) + ((c + f a : ℕ) : R2 N) * (mk2 N (1 - X ^ a) * w a) * z := by
            rw [hwa]
        _ = mk2 N (1 - X ^ a) * (1 + ((c + f a : ℕ) : R2 N) * w a * z) := by ring
    rw [Finset.prod_congr rfl hpt, Finset.prod_mul_distrib, prod_one_add_mul_z hz2]
  rw [hfac qNum, hfac qDen]
  congr 1
  have hdiff : (∑ a ∈ S, ((c + qNum a : ℕ) : R2 N) * w a) * z -
      (∑ a ∈ S, ((c + qDen a : ℕ) : R2 N) * w a) * z = 0 := by
    rw [← sub_mul, ← Finset.sum_sub_distrib]
    have hterm : ∀ a ∈ S,
        ((c + qNum a : ℕ) : R2 N) * w a - ((c + qDen a : ℕ) : R2 N) * w a =
        (((qNum a : ℤ) - (qDen a : ℤ) : ℤ) : R2 N) * w a := by
      intro a _
      push_cast; ring
    rw [Finset.sum_congr rfl hterm]
    exact hsum w hw
  linear_combination hdiff

/-- Pairing reduction for any symmetric weight `Δ : ℕ → ℤ` (`Δ (N - a) = Δ a`) on a set
`S = {1 ≤ a < N | ¬ n ∣ a}` (`N` odd, `n ∣ N`):
if `∑_{1 ≤ a ≤ (N - 1)/2, ¬ n ∣ a} Δ(a) = 0`, then `(∑_{a ∈ S} Δ(a) * w_a) * z = 0` in `R2 N`! -/
private lemma symmetric_pairing_vanishes {N n : ℕ} (hN_odd : N % 2 = 1) (hn_dvd : n ∣ N)
    (Δ : ℕ → ℤ)
    (hΔ_sym : ∀ a : ℕ, 1 ≤ a → a < N → Δ (N - a) = Δ a)
    (hΔ_half : ∑ a ∈ (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => ¬ n ∣ a), Δ a = 0)
    (w : ℕ → R2 N)
    (hw : ∀ a ∈ (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a),
      mk2 N (1 - X ^ a) * w a = mk2 N (X ^ a)) :
    (∑ a ∈ (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a), (Δ a : R2 N) * w a) *
      mk2 N (1 - X ^ N) = 0 := by
  set z : R2 N := mk2 N (1 - X ^ N)
  set H1 := (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => ¬ n ∣ a)
  set H2 := (Finset.Icc ((N - 1) / 2 + 1) (N - 1)).filter (fun a => ¬ n ∣ a)
  set S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
  have hS_eq : S = H1 ∪ H2 := by
    ext a
    simp only [S, H1, H2, Finset.mem_union, Finset.mem_filter, Finset.mem_Icc]
    omega
  have hdisj : Disjoint H1 H2 := by
    rw [Finset.disjoint_left]
    intro a h1 h2
    simp only [H1, H2, Finset.mem_filter, Finset.mem_Icc] at h1 h2
    omega
  -- Bijection `a ↦ N - a` from `H1` to `H2`
  have hsum_H2 : ∑ a ∈ H2, (Δ a : R2 N) * w a = ∑ a ∈ H1, (Δ a : R2 N) * w (N - a) := by
    symm
    refine Finset.sum_bij (fun a _ => N - a) ?_ ?_ ?_ ?_
    · intro a ha
      simp only [H1, H2, Finset.mem_filter, Finset.mem_Icc] at ha ⊢
      refine ⟨⟨by omega, by omega⟩, fun hd => ha.2 ?_⟩
      have h1 := Nat.dvd_sub hn_dvd hd
      rwa [Nat.sub_sub_self (by omega)] at h1
    · intro a₁ ha₁ a₂ ha₂ hEq
      simp only [H1, Finset.mem_filter, Finset.mem_Icc] at ha₁ ha₂
      omega
    · intro b hb
      simp only [H1, H2, Finset.mem_filter, Finset.mem_Icc] at hb ⊢
      refine ⟨N - b, ⟨⟨by omega, by omega⟩, fun hd => hb.2 ?_⟩, by omega⟩
      have h1 := Nat.dvd_sub hn_dvd hd
      rwa [Nat.sub_sub_self (by omega)] at h1
    · intro a ha
      simp only [H1, Finset.mem_filter, Finset.mem_Icc] at ha
      rw [hΔ_sym a ha.1.1 (by omega)]
  rw [hS_eq, Finset.sum_union hdisj, hsum_H2, ← Finset.sum_add_distrib, Finset.sum_mul]
  have hpair : ∀ a ∈ H1, ((Δ a : R2 N) * w a + (Δ a : R2 N) * w (N - a)) * z =
      -(Δ a : R2 N) * z := by
    intro a ha
    have ha' := Finset.mem_filter.mp ha
    have ha_bounds := Finset.mem_Icc.mp ha'.1
    have ha1 : 1 ≤ a := ha_bounds.1
    have haN : a < N := by omega
    have haS : a ∈ S := Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨ha1, by omega⟩, ha'.2⟩
    have hNaS : N - a ∈ S := by
      refine Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨by omega, by omega⟩, fun hd => ha'.2 ?_⟩
      have h1 := Nat.dvd_sub hn_dvd hd
      rwa [Nat.sub_sub_self haN.le] at h1
    have hndvd_a : ¬ N ∣ a := fun hd => by have := Nat.le_of_dvd ha1 hd; omega
    have hndvd_Na : ¬ N ∣ (N - a) := fun hd => by have := Nat.le_of_dvd (by omega) hd; omega
    obtain ⟨ua, hua⟩ := isUnit_mk2_of_isCoprime (isCoprime_one_sub_X_pow_Phi_sq ha1 hndvd_a)
    obtain ⟨ub, hub⟩ := isUnit_mk2_of_isCoprime (isCoprime_one_sub_X_pow_Phi_sq (by omega) hndvd_Na)
    have hwa : w a = mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) := by
      have h1 := hw a haS
      rw [← hua] at h1
      calc w a = (ua⁻¹ : (R2 N)ˣ) * ((ua : R2 N) * w a) := by rw [← mul_assoc, ua.inv_mul, one_mul]
        _ = (ua⁻¹ : (R2 N)ˣ) * mk2 N (X ^ a) := by rw [h1]
        _ = mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) := mul_comm _ _
    have hwb : w (N - a) = mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ) := by
      have h1 := hw (N - a) hNaS
      rw [← hub] at h1
      calc w (N - a) = (ub⁻¹ : (R2 N)ˣ) * ((ub : R2 N) * w (N - a)) := by
            rw [← mul_assoc, ub.inv_mul, one_mul]
        _ = (ub⁻¹ : (R2 N)ˣ) * mk2 N (X ^ (N - a)) := by rw [h1]
        _ = mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ) := mul_comm _ _
    have hp := pairing_mul_z ha1 haN ua ub hua hub
    rw [hwa, hwb]
    calc ((Δ a : R2 N) * (mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ)) +
          (Δ a : R2 N) * (mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ))) * z
        = (Δ a : R2 N) * ((mk2 N (X ^ a) * (ua⁻¹ : (R2 N)ˣ) +
          mk2 N (X ^ (N - a)) * (ub⁻¹ : (R2 N)ˣ)) * z) := by ring
      _ = (Δ a : R2 N) * (-z) := by rw [hp]
      _ = -(Δ a : R2 N) * z := by ring
  rw [Finset.sum_congr rfl hpair, ← Finset.sum_mul, Finset.sum_neg_distrib]
  have hcast : (∑ a ∈ H1, (Δ a : R2 N)) = ((∑ a ∈ H1, Δ a : ℤ) : R2 N) := by push_cast; rfl
  rw [hcast, hΔ_half, Int.cast_zero, neg_zero, zero_mul]

/-- Telescoping induction for `RatCongMod`: if base `r = s` has reduced representation coprime to `M`,
every `A k, B k ≠ 0` (`s ≤ k`), and each step `k + 1` has ratio `U / V` coprime to `M` with `M ∣ U - V`,
then `RatCongMod (A r) (B r) (A s) (B s) M` for all `r ≥ s`. -/
private lemma ratCongMod_of_telescoping {A B : ℕ → Polynomial ℚ} {M : Polynomial ℚ} {s : ℕ}
    (hA_ne : ∀ k, s ≤ k → A k ≠ 0)
    (hB_ne : ∀ k, s ≤ k → B k ≠ 0)
    (hbase : ∃ P₀ Q₀ : Polynomial ℚ, IsCoprime Q₀ M ∧ A s * Q₀ = P₀ * B s)
    (hstep : ∀ k, s ≤ k →
      ∃ U V : Polynomial ℚ, IsCoprime V M ∧
        A (k + 1) * B k * V = B (k + 1) * A k * U ∧ M ∣ U - V) :
    ∀ r, s ≤ r → RatCongMod (A r) (B r) (A s) (B s) M := by
  obtain ⟨P₀, Q₀, hQ₀, hbase_eq⟩ := hbase
  have haux : ∀ r, s ≤ r → ∃ P Q : Polynomial ℚ,
      IsCoprime Q M ∧ A r * Q = P * B r ∧ M ∣ P * Q₀ - P₀ * Q := by
    intro r hr
    induction r, hr using Nat.le_induction with
    | base => exact ⟨P₀, Q₀, hQ₀, hbase_eq, by simp⟩
    | succ k hk ih =>
      obtain ⟨P, Q, hQ, hPQ, hdiv⟩ := ih
      obtain ⟨U, V, hV, hratio, hUV⟩ := hstep k hk
      refine ⟨P * U, Q * V, hQ.mul_left hV, ?_, ?_⟩
      · have hne : A k * B k ≠ 0 := mul_ne_zero (hA_ne k hk) (hB_ne k hk)
        apply mul_right_cancel₀ hne
        calc A (k + 1) * (Q * V) * (A k * B k)
            = (A (k + 1) * B k * V) * (A k * Q) := by ring
          _ = (B (k + 1) * A k * U) * (P * B k) := by rw [hratio, hPQ]
          _ = (P * U) * B (k + 1) * (A k * B k) := by ring
      · have hdecomp : (P * U) * Q₀ - P₀ * (Q * V) =
            U * (P * Q₀ - P₀ * Q) + P₀ * Q * (U - V) := by ring
        rw [hdecomp]
        exact dvd_add (dvd_mul_of_dvd_right hdiv U) (dvd_mul_of_dvd_right hUV (P₀ * Q))
  intro r hr
  obtain ⟨P, Q, hQ, hPQ, hdiv⟩ := haux r hr
  exact ⟨hB_ne r hr, hB_ne s le_rfl, P, Q, P₀, Q₀, hQ, hQ₀, hPQ, hbase_eq, hdiv⟩

/-! ## Section 3: Proof of Conjecture 6.4 (`conj:4`) -/

private lemma qPoch_X_pow_eq (a b m : ℕ) :
    qPoch (X ^ a) (X ^ b) m = ∏ k ∈ Finset.range m, (1 - X ^ (a + b * k)) := by
  unfold qPoch
  refine Finset.prod_congr rfl fun k _ => ?_
  rw [← pow_mul, ← pow_add]

private lemma qPoch_X_pow_ne_zero (a b m : ℕ) (ha : 1 ≤ a) :
    qPoch (X ^ a) (X ^ b) m ≠ 0 := by
  rw [qPoch_X_pow_eq]
  exact Finset.prod_ne_zero_iff.mpr fun k _ => one_sub_X_pow_ne_zero (by omega)

private lemma num4_ne_zero {n : ℕ} (hn : 1 ≤ n) (r : ℕ) : num4 n r ≠ 0 := by
  unfold num4
  have h1 : qPoch X (X ^ 2) ((n ^ r - 1) / 4) = qPoch (X ^ 1) (X ^ 2) ((n ^ r - 1) / 4) := by
    simp
  rw [h1]
  exact mul_ne_zero (qPoch_X_pow_ne_zero 1 2 _ le_rfl) (qPoch_X_pow_ne_zero (2 * n) (2 * n) _ (by omega))

private lemma den4_ne_zero {n : ℕ} (hn : 1 ≤ n) (r : ℕ) : den4 n r ≠ 0 := by
  unfold den4
  exact mul_ne_zero (qPoch_X_pow_ne_zero 2 2 _ (by decide)) (qPoch_X_pow_ne_zero n (2 * n) _ hn)

private lemma qPoch_split_Ico {a q : Polynomial ℚ} {m₁ m₂ : ℕ} (h : m₁ ≤ m₂) :
    qPoch a q m₂ = qPoch a q m₁ * ∏ k ∈ Finset.Ico m₁ m₂, (1 - a * q ^ k) := by
  unfold qPoch
  have hunion : Finset.range m₂ = Finset.range m₁ ∪ Finset.Ico m₁ m₂ := by
    ext k; simp only [Finset.mem_union, Finset.mem_range, Finset.mem_Ico]; omega
  have hdisj : Disjoint (Finset.range m₁) (Finset.Ico m₁ m₂) := by
    rw [Finset.disjoint_left]
    intro k h1 h2; simp only [Finset.mem_range, Finset.mem_Ico] at h1 h2; omega
  rw [hunion, Finset.prod_union hdisj]

/-- Alternating sum `∑_{a=1}^{2K} (-1)^(a-1) = 0`. -/
private lemma sum_alt_even_zero (K : ℕ) :
    ∑ a ∈ Finset.Icc 1 (2 * K), ((-1 : ℤ) ^ (a - 1)) = 0 := by
  induction K with
  | zero => simp
  | succ K ih =>
    have h1 : Finset.Icc 1 (2 * (K + 1)) =
        insert (2 * K + 2) (insert (2 * K + 1) (Finset.Icc 1 (2 * K))) := by
      ext x; simp only [Finset.mem_insert, Finset.mem_Icc]; omega
    rw [h1, Finset.sum_insert (by simp), Finset.sum_insert (by simp), ih, add_zero]
    have hp1 : (-1 : ℤ) ^ (2 * K + 2 - 1) = -1 := by
      have : 2 * K + 2 - 1 = 2 * K + 1 := by omega
      rw [this, pow_succ, pow_mul]; norm_num
    have hp2 : (-1 : ℤ) ^ (2 * K + 1 - 1) = 1 := by
      have : 2 * K + 1 - 1 = 2 * K := by omega
      rw [this, pow_mul]; norm_num
    rw [hp1, hp2]; ring

/-- Step 1 of Conjecture 6.4: exact `n`-multiple cancellation for `num4 / den4`. -/
private lemma guo64_cancel_step {n k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n) (hk1 : 1 ≤ k) :
    let k0 := (n ^ k - 1) / 4
    let k1 := (n ^ (k + 1) - 1) / 4
    let U : Polynomial ℚ := ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 1)), (1 - X ^ (2 * i + 1))
    let V : Polynomial ℚ := ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 2)), (1 - X ^ (2 * i + 2))
    num4 n (k + 1) * den4 n k * V = den4 n (k + 1) * num4 n k * U := by
  intro k0 k1 U V
  set j0 := (n ^ (k - 1) - 1) / 4
  have hn2 : n % 2 = 1 := by omega
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hnk_prev4 : n ^ (k - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k - 1)
  have hk0_le_k1 : k0 ≤ k1 := by
    have : n ^ k ≤ n ^ (k + 1) := Nat.pow_le_pow_right (by omega) (by omega)
    omega
  have hj0_le_k0 : j0 ≤ k0 := by
    have : n ^ (k - 1) ≤ n ^ k := Nat.pow_le_pow_right (by omega) (by omega)
    omega
  have hnn_prev : n * n ^ (k - 1) = n ^ k := by
    rw [← pow_succ', Nat.sub_add_cancel hk1]
  have hnn_curr : n * n ^ k = n ^ (k + 1) := by rw [← pow_succ']
  have hnum_split : num4 n (k + 1) = num4 n k *
      (∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 1))) *
      (∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 2)))) := by
    unfold num4
    have hk_sub : k + 1 - 1 = k := Nat.add_sub_cancel k 1
    rw [hk_sub, qPoch_split_Ico (a := X) (q := X ^ 2) hk0_le_k1,
      qPoch_split_Ico (a := X ^ (2 * n)) (q := X ^ (2 * n)) hj0_le_k0]
    have h1 : ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) * (X ^ 2) ^ i) =
        ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 1)) :=
      Finset.prod_congr rfl fun i _ => by rw [← pow_mul, ← pow_succ']
    have h2 : ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (2 * n) * (X ^ (2 * n)) ^ j) =
        ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 2))) :=
      Finset.prod_congr rfl fun j _ => by
        rw [← pow_mul, ← pow_add]; congr 2; ring
    rw [h1, h2]; ring
  have hden_split : den4 n (k + 1) = den4 n k *
      (∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 2))) *
      (∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 1)))) := by
    unfold den4
    have hk_sub : k + 1 - 1 = k := Nat.add_sub_cancel k 1
    rw [hk_sub, qPoch_split_Ico (a := X ^ 2) (q := X ^ 2) hk0_le_k1,
      qPoch_split_Ico (a := X ^ n) (q := X ^ (2 * n)) hj0_le_k0]
    have h1 : ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ 2 * (X ^ 2) ^ i) =
        ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 2)) :=
      Finset.prod_congr rfl fun i _ => by rw [← pow_mul, ← pow_add]; congr 2; omega
    have h2 : ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ n * (X ^ (2 * n)) ^ j) =
        ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 1))) :=
      Finset.prod_congr rfl fun j _ => by
        rw [← pow_mul, ← pow_add]; congr 2; ring
    rw [h1, h2]; ring
  have hodd_cancel : ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => n ∣ (2 * i + 1)),
        (1 - (X : Polynomial ℚ) ^ (2 * i + 1)) =
      ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 1))) := by
    symm
    refine Finset.prod_bij (fun j _ => (n * (2 * j + 1) - 1) / 2) ?_ ?_ ?_ ?_
    · intro j hj
      have hjb := Finset.mem_Ico.mp hj
      have hodd : (n * (2 * j + 1)) % 2 = 1 := by rw [Nat.mul_mod, hn2]; omega
      have h2i : 2 * ((n * (2 * j + 1) - 1) / 2) + 1 = n * (2 * j + 1) := by omega
      simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · have h1 : 4 * j0 + 1 = n ^ (k - 1) := by omega
        have h2 : 4 * k0 + 1 = n ^ k := by omega
        have h3 : n * (4 * j0 + 1) < n * (2 * (2 * j + 1)) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * j0 + 1) = 4 * k0 + 1 := by rw [h1, h2, hnn_prev]
        have h5 : n * (2 * (2 * j + 1)) = 2 * (n * (2 * j + 1)) := by ring
        omega
      · have h1 : 4 * k0 + 1 = n ^ k := by omega
        have h2 : 4 * k1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (2 * (2 * j + 1)) < n * (4 * k0 + 1) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * k0 + 1) = 4 * k1 + 1 := by rw [h1, h2, hnn_curr]
        have h5 : n * (2 * (2 * j + 1)) = 2 * (n * (2 * j + 1)) := by ring
        omega
      · rw [h2i]; exact dvd_mul_right n _
    · intro j₁ _ j₂ _ hEq
      have h1 : (n * (2 * j₁ + 1)) % 2 = 1 := by rw [Nat.mul_mod, hn2]; omega
      have h2 : (n * (2 * j₂ + 1)) % 2 = 1 := by rw [Nat.mul_mod, hn2]; omega
      have hmul : n * (2 * j₁ + 1) = n * (2 * j₂ + 1) := by omega
      have hcancel := Nat.eq_of_mul_eq_mul_left (by omega : 0 < n) hmul
      omega
    · intro i hi
      simp only [Finset.mem_filter, Finset.mem_Ico] at hi
      rcases hi.2 with ⟨q, hq⟩
      have hq_odd : q % 2 = 1 := by
        have : (n * q) % 2 = 1 := by omega
        rw [Nat.mul_mod, hn2] at this; omega
      have h2q : 2 * (q / 2) + 1 = q := by omega
      refine ⟨q / 2, Finset.mem_Ico.mpr ⟨?_, ?_⟩, ?_⟩
      · have h1 : 4 * j0 + 1 = n ^ (k - 1) := by omega
        have h2 : 4 * k0 + 1 = n ^ k := by omega
        have h3 : n * (4 * j0 + 1) < n * (2 * q) := by
          calc n * (4 * j0 + 1) = 4 * k0 + 1 := by rw [h1, h2, hnn_prev]
            _ < 2 * (2 * i + 1) := by omega
            _ = n * (2 * q) := by rw [hq]; ring
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · have h1 : 4 * k0 + 1 = n ^ k := by omega
        have h2 : 4 * k1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (2 * q) < n * (4 * k0 + 1) := by
          calc n * (2 * q) = 2 * (2 * i + 1) := by rw [hq]; ring
            _ < 4 * k1 + 1 := by omega
            _ = n * (4 * k0 + 1) := by rw [h1, h2, hnn_curr]
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · rw [h2q, ← hq]; omega
    · intro j _
      have hodd : (n * (2 * j + 1)) % 2 = 1 := by rw [Nat.mul_mod, hn2]; omega
      congr 2; omega
  have heven_cancel : ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => n ∣ (2 * i + 2)),
        (1 - (X : Polynomial ℚ) ^ (2 * i + 2)) =
      ∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 2))) := by
    symm
    refine Finset.prod_bij (fun j _ => (n * (2 * j + 2) - 2) / 2) ?_ ?_ ?_ ?_
    · intro j hj
      have hjb := Finset.mem_Ico.mp hj
      have hev : (n * (2 * j + 2)) % 2 = 0 := by rw [Nat.mul_mod, hn2]; omega
      have hge2 : 2 ≤ n * (2 * j + 2) := by
        have : 1 * 2 ≤ n * (2 * j + 2) := Nat.mul_le_mul (by omega) (by omega)
        omega
      have h2i : 2 * ((n * (2 * j + 2) - 2) / 2) + 2 = n * (2 * j + 2) := by omega
      simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · have h1 : 4 * j0 + 1 = n ^ (k - 1) := by omega
        have h2 : 4 * k0 + 1 = n ^ k := by omega
        have h3 : n * (4 * j0 + 1) < n * (2 * (2 * j + 2)) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * j0 + 1) = 4 * k0 + 1 := by rw [h1, h2, hnn_prev]
        have h5 : n * (2 * (2 * j + 2)) = 2 * (n * (2 * j + 2)) := by ring
        omega
      · have h1 : 4 * k0 + 1 = n ^ k := by omega
        have h2 : 4 * k1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (2 * (2 * j + 2)) < n * (4 * k0 + 1) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * k0 + 1) = 4 * k1 + 1 := by rw [h1, h2, hnn_curr]
        have h5 : n * (2 * (2 * j + 2)) = 2 * (n * (2 * j + 2)) := by ring
        omega
      · rw [h2i]; exact dvd_mul_right n _
    · intro j₁ _ j₂ _ hEq
      have h1 : (n * (2 * j₁ + 2)) % 2 = 0 := by rw [Nat.mul_mod, hn2]; omega
      have h2 : (n * (2 * j₂ + 2)) % 2 = 0 := by rw [Nat.mul_mod, hn2]; omega
      have hg1 : 2 ≤ n * (2 * j₁ + 2) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 2 ≤ 2 * j₁ + 2); omega
      have hg2 : 2 ≤ n * (2 * j₂ + 2) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 2 ≤ 2 * j₂ + 2); omega
      have hmul : n * (2 * j₁ + 2) = n * (2 * j₂ + 2) := by omega
      have hcancel := Nat.eq_of_mul_eq_mul_left (by omega : 0 < n) hmul
      omega
    · intro i hi
      simp only [Finset.mem_filter, Finset.mem_Ico] at hi
      rcases hi.2 with ⟨q, hq⟩
      have hq_even : q % 2 = 0 := by
        have : (n * q) % 2 = 0 := by omega
        rw [Nat.mul_mod, hn2] at this; omega
      have hq_ge2 : 2 ≤ q := by
        have : q ≠ 0 := by intro h0; rw [h0, mul_zero] at hq; omega
        omega
      have h2q : 2 * (q / 2 - 1) + 2 = q := by omega
      refine ⟨q / 2 - 1, Finset.mem_Ico.mpr ⟨?_, ?_⟩, ?_⟩
      · have h1 : 4 * j0 + 1 = n ^ (k - 1) := by omega
        have h2 : 4 * k0 + 1 = n ^ k := by omega
        have h3 : n * (4 * j0 + 1) < n * (2 * q) := by
          calc n * (4 * j0 + 1) = 4 * k0 + 1 := by rw [h1, h2, hnn_prev]
            _ < 2 * (2 * i + 2) := by omega
            _ = n * (2 * q) := by rw [hq]; ring
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · have h1 : 4 * k0 + 1 = n ^ k := by omega
        have h2 : 4 * k1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (2 * q) < n * (4 * k0 + 1) := by
          calc n * (2 * q) = 2 * (2 * i + 2) := by rw [hq]; ring
            _ < 4 * k1 + 1 := by omega
            _ = n * (4 * k0 + 1) := by rw [h1, h2, hnn_curr]
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · rw [h2q, ← hq]; omega
    · intro j _
      have hev : (n * (2 * j + 2)) % 2 = 0 := by rw [Nat.mul_mod, hn2]; omega
      have hge2 : 2 ≤ n * (2 * j + 2) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 2 ≤ 2 * j + 2); omega
      congr 2; omega
  have hsplit_num : ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 1)) =
      (∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 1)))) * U := by
    rw [← hodd_cancel, Finset.prod_filter_mul_prod_filter_not]
  have hsplit_den : ∏ i ∈ Finset.Ico k0 k1, (1 - (X : Polynomial ℚ) ^ (2 * i + 2)) =
      (∏ j ∈ Finset.Ico j0 k0, (1 - (X : Polynomial ℚ) ^ (n * (2 * j + 2)))) * V := by
    rw [← heven_cancel, Finset.prod_filter_mul_prod_filter_not]
  rw [hnum_split, hden_split, hsplit_num, hsplit_den]
  ring

private def qNum4 (N a : ℕ) : ℕ :=
  if a % 2 = 0 then 1 else if a ≤ (N - 1) / 2 then 2 else 0

private def qDen4 (N a : ℕ) : ℕ :=
  if a % 2 = 1 then 1 else if a ≤ (N - 1) / 2 then 2 else 0

private lemma guo64_blocks_U {n s k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hk : s ≤ k) :
    let N := n ^ s
    let k0 := (n ^ k - 1) / 4
    let k1 := (n ^ (k + 1) - 1) / 4
    let K₀ := n ^ (k - s)
    let M := (n - 1) / 4 * K₀
    let c := (K₀ - 1) / 2
    let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
    (∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 1)), (1 - (X : Polynomial ℚ) ^ (2 * i + 1))) =
      ∏ t ∈ Finset.range M, ∏ a ∈ S, (1 - (X : Polynomial ℚ) ^ (a + (2 * t + c + qNum4 N a) * N)) := by
  intro N k0 k1 K₀ M c S
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hK₀4 : K₀ % 4 = 1 := pow_mod_four_eq_one hn4 (k - s)
  have hN_ge5 : 5 ≤ N := by
    have hn5 : 5 ≤ n := by omega
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  have hK₀N : K₀ * N = n ^ k := by
    dsimp [K₀, N]; rw [← pow_add, Nat.sub_add_cancel hk]
  have hk1_sub : k1 - k0 = M * N := by
    have h1 : 4 * (k1 - k0) = n ^ (k + 1) - n ^ k := by omega
    have h2 : n ^ (k + 1) - n ^ k = (n - 1) * (K₀ * N) := by
      rw [hK₀N, pow_succ', Nat.sub_mul, one_mul]
    have h3 : 4 * M = (n - 1) * K₀ := by
      dsimp [M]; have : 4 * ((n - 1) / 4) = n - 1 := by omega
      nlinarith
    nlinarith
  have h2k0 : 2 * k0 + 1 = c * N + (N + 1) / 2 := by
    have h1 : 4 * k0 + 1 = K₀ * N := by rw [hK₀N]; omega
    have h2 : 2 * c + 1 = K₀ := by omega
    have h3 : 2 * ((N + 1) / 2) = N + 1 := by omega
    nlinarith
  rw [← Finset.prod_product']
  refine Finset.prod_bij (fun i _ => ((i - k0) / N, (2 * i + 1) % N)) ?_ ?_ ?_ ?_
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc]
    have hdiv : (i - k0) / N < M := by
      rw [Nat.div_lt_iff_lt_mul (by omega)]; omega
    have hmod_ndvd : ¬ n ∣ (2 * i + 1) % N := by
      intro hd
      have h1 := Nat.dvd_add (dvd_trans hn_dvd_N (dvd_mul_right N ((2 * i + 1) / N))) hd
      rw [Nat.div_add_mod] at h1
      exact hi.2 h1
    have hmod_pos : 1 ≤ (2 * i + 1) % N := by
      by_contra h0
      have hmod0 : (2 * i + 1) % N = 0 := by omega
      exact hmod_ndvd (by rw [hmod0]; exact dvd_zero n)
    have hmod_lt : (2 * i + 1) % N < N := Nat.mod_lt _ (by omega)
    exact ⟨hdiv, ⟨hmod_pos, by omega⟩, hmod_ndvd⟩
  · intro i₁ hi₁ i₂ hi₂ hEq
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi₁ hi₂
    have hq : (i₁ - k0) / N = (i₂ - k0) / N := congrArg Prod.fst hEq
    have hr : (2 * i₁ + 1) % N = (2 * i₂ + 1) % N := congrArg Prod.snd hEq
    set r₁ := (i₁ - k0) % N
    set r₂ := (i₂ - k0) % N
    have hr1_lt : r₁ < N := Nat.mod_lt _ (by omega)
    have hr2_lt : r₂ < N := Nat.mod_lt _ (by omega)
    have he1 : 2 * i₁ + 1 = (2 * ((i₁ - k0) / N) + c) * N + ((N + 1) / 2 + 2 * r₁) := by
      have hi1 : i₁ = k0 + N * ((i₁ - k0) / N) + r₁ := by
        have := Nat.div_add_mod (i₁ - k0) N; omega
      calc 2 * i₁ + 1 = (2 * k0 + 1) + 2 * (N * ((i₁ - k0) / N)) + 2 * r₁ := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * ((i₁ - k0) / N)) + 2 * r₁ := by rw [h2k0]
        _ = (2 * ((i₁ - k0) / N) + c) * N + ((N + 1) / 2 + 2 * r₁) := by ring
    have he2 : 2 * i₂ + 1 = (2 * ((i₂ - k0) / N) + c) * N + ((N + 1) / 2 + 2 * r₂) := by
      have hi2 : i₂ = k0 + N * ((i₂ - k0) / N) + r₂ := by
        have := Nat.div_add_mod (i₂ - k0) N; omega
      calc 2 * i₂ + 1 = (2 * k0 + 1) + 2 * (N * ((i₂ - k0) / N)) + 2 * r₂ := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * ((i₂ - k0) / N)) + 2 * r₂ := by rw [h2k0]
        _ = (2 * ((i₂ - k0) / N) + c) * N + ((N + 1) / 2 + 2 * r₂) := by ring
    have hmod_eq : ((N + 1) / 2 + 2 * r₁) % N = ((N + 1) / 2 + 2 * r₂) % N := by
      rw [he1, he2, Nat.mul_add_mod_self_right, Nat.mul_add_mod_self_right] at hr
      exact hr
    have hr_eq : r₁ = r₂ := by
      have hcop2 : Nat.Coprime N 2 := by
        rw [Nat.coprime_two_right]; exact Nat.odd_iff.mpr (by omega)
      by_cases hle : r₁ ≤ r₂
      · have hdvd : N ∣ 2 * (r₂ - r₁) := by
          have hsub : ((N + 1) / 2 + 2 * r₂) - ((N + 1) / 2 + 2 * r₁) = 2 * (r₂ - r₁) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq
        have hdvd' : N ∣ r₂ - r₁ := hcop2.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₂ - r₁) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
      · have hdvd : N ∣ 2 * (r₁ - r₂) := by
          have hsub : ((N + 1) / 2 + 2 * r₁) - ((N + 1) / 2 + 2 * r₂) = 2 * (r₁ - r₂) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq.symm
        have hdvd' : N ∣ r₁ - r₂ := hcop2.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₁ - r₂) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
    have hdm1 : N * ((i₁ - k0) / N) + r₁ = i₁ - k0 := Nat.div_add_mod (i₁ - k0) N
    have hdm2 : N * ((i₂ - k0) / N) + r₂ = i₂ - k0 := Nat.div_add_mod (i₂ - k0) N
    rw [hq, hr_eq] at hdm1
    omega
  · rintro ⟨t, a⟩ hta
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc] at hta
    rcases hta with ⟨ht, ⟨ha1, haN⟩, ha_ndvd⟩
    let r_idx := (qNum4 N a * N + a - (N + 1) / 2) / 2
    have hr_eq : (N + 1) / 2 + 2 * r_idx = qNum4 N a * N + a := by
      dsimp [r_idx, qNum4]; split_ifs <;> omega
    have hr_lt : r_idx < N := by
      dsimp [r_idx, qNum4]; split_ifs <;> omega
    let i := k0 + t * N + r_idx
    have hi_exp : 2 * i + 1 = (2 * t + c + qNum4 N a) * N + a := by
      calc 2 * i + 1 = (2 * k0 + 1) + 2 * (t * N) + 2 * r_idx := by dsimp [i]; ring
        _ = (c * N + (N + 1) / 2) + 2 * (t * N) + 2 * r_idx := by rw [h2k0]
        _ = c * N + 2 * (t * N) + ((N + 1) / 2 + 2 * r_idx) := by ring
        _ = c * N + 2 * (t * N) + (qNum4 N a * N + a) := by rw [hr_eq]
        _ = (2 * t + c + qNum4 N a) * N + a := by ring
    refine ⟨i, ?_, ?_⟩
    · simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨by omega, ?_⟩, ?_⟩
      · have hlt : t * N + r_idx < M * N := by
          calc t * N + r_idx < t * N + N := by omega
            _ = (t + 1) * N := by ring
            _ ≤ M * N := Nat.mul_le_mul_right N ht
        omega
      · intro hd
        rw [hi_exp] at hd
        have h1 := Nat.dvd_sub hd (dvd_trans hn_dvd_N (dvd_mul_left N (2 * t + c + qNum4 N a)))
        rw [Nat.add_sub_cancel_left] at h1
        exact ha_ndvd h1
    · refine Prod.ext ?_ ?_
      · dsimp [i]
        have : k0 + t * N + r_idx - k0 = r_idx + N * t := by ring_nf; omega
        rw [this, Nat.add_mul_div_left _ _ (by omega), Nat.div_eq_of_lt hr_lt, zero_add]
      · rw [hi_exp, Nat.mul_add_mod_self_right, Nat.mod_eq_of_lt (by omega)]
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    set t := (i - k0) / N
    set r_idx := (i - k0) % N
    set a := (2 * i + 1) % N
    have hr_lt : r_idx < N := Nat.mod_lt _ (by omega)
    have he : 2 * i + 1 = (2 * t + c) * N + ((N + 1) / 2 + 2 * r_idx) := by
      have hi1 : i = k0 + N * t + r_idx := by
        have hdm : N * t + r_idx = i - k0 := Nat.div_add_mod (i - k0) N; omega
      calc 2 * i + 1 = (2 * k0 + 1) + 2 * (N * t) + 2 * r_idx := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * t) + 2 * r_idx := by rw [h2k0]
        _ = (2 * t + c) * N + ((N + 1) / 2 + 2 * r_idx) := by ring
    have ha_eq : a = ((N + 1) / 2 + 2 * r_idx) % N := by
      dsimp [a]; rw [he, Nat.mul_add_mod_self_right]
    have ha_pos : 1 ≤ a := by
      by_contra h0
      have ha0 : a = 0 := by omega
      have hdN : N ∣ 2 * i + 1 := Nat.dvd_of_mod_eq_zero ha0
      exact hi.2 (dvd_trans hn_dvd_N hdN)
    have ha_lt : a < N := Nat.mod_lt _ (by omega)
    have hq_val : ((N + 1) / 2 + 2 * r_idx) = qNum4 N a * N + a := by
      have hdiv_mod := Nat.div_add_mod ((N + 1) / 2 + 2 * r_idx) N
      rw [← ha_eq, mul_comm] at hdiv_mod
      set q := ((N + 1) / 2 + 2 * r_idx) / N
      have hq_le2 : q ≤ 2 := by
        by_contra hgt
        have h3 : 3 ≤ q := by omega
        have : 3 * N ≤ q * N := Nat.mul_le_mul_right N h3
        omega
      have hodd_sum : (q * N + a) % 2 = 1 := by omega
      have hq_eq : q = qNum4 N a := by
        dsimp [qNum4]
        split_ifs with ha_ev ha_half
        · interval_cases q <;> omega
        · interval_cases q <;> omega
        · interval_cases q <;> omega
      rw [← hq_eq]; omega
    congr 2
    rw [he, hq_val]; ring

private lemma guo64_blocks_V {n s k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hk : s ≤ k) :
    let N := n ^ s
    let k0 := (n ^ k - 1) / 4
    let k1 := (n ^ (k + 1) - 1) / 4
    let K₀ := n ^ (k - s)
    let M := (n - 1) / 4 * K₀
    let c := (K₀ - 1) / 2
    let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
    (∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 2)), (1 - (X : Polynomial ℚ) ^ (2 * i + 2))) =
      ∏ t ∈ Finset.range M, ∏ a ∈ S, (1 - (X : Polynomial ℚ) ^ (a + (2 * t + c + qDen4 N a) * N)) := by
  intro N k0 k1 K₀ M c S
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hK₀4 : K₀ % 4 = 1 := pow_mod_four_eq_one hn4 (k - s)
  have hN_ge5 : 5 ≤ N := by
    have hn5 : 5 ≤ n := by omega
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  have hK₀N : K₀ * N = n ^ k := by
    dsimp [K₀, N]; rw [← pow_add, Nat.sub_add_cancel hk]
  have hk1_sub : k1 - k0 = M * N := by
    have h1 : 4 * (k1 - k0) = n ^ (k + 1) - n ^ k := by omega
    have h2 : n ^ (k + 1) - n ^ k = (n - 1) * (K₀ * N) := by
      rw [hK₀N, pow_succ', Nat.sub_mul, one_mul]
    have h3 : 4 * M = (n - 1) * K₀ := by
      dsimp [M]; have : 4 * ((n - 1) / 4) = n - 1 := by omega
      nlinarith
    nlinarith
  have h2k0 : 2 * k0 + 1 = c * N + (N + 1) / 2 := by
    have h1 : 4 * k0 + 1 = K₀ * N := by rw [hK₀N]; omega
    have h2 : 2 * c + 1 = K₀ := by omega
    have h3 : 2 * ((N + 1) / 2) = N + 1 := by omega
    nlinarith
  rw [← Finset.prod_product']
  refine Finset.prod_bij (fun i _ => ((i - k0) / N, (2 * i + 2) % N)) ?_ ?_ ?_ ?_
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc]
    have hdiv : (i - k0) / N < M := by
      rw [Nat.div_lt_iff_lt_mul (by omega)]; omega
    have hmod_ndvd : ¬ n ∣ (2 * i + 2) % N := by
      intro hd
      have h1 := Nat.dvd_add (dvd_trans hn_dvd_N (dvd_mul_right N ((2 * i + 2) / N))) hd
      rw [Nat.div_add_mod] at h1
      exact hi.2 h1
    have hmod_pos : 1 ≤ (2 * i + 2) % N := by
      by_contra h0
      have hmod0 : (2 * i + 2) % N = 0 := by omega
      exact hmod_ndvd (by rw [hmod0]; exact dvd_zero n)
    have hmod_lt : (2 * i + 2) % N < N := Nat.mod_lt _ (by omega)
    exact ⟨hdiv, ⟨hmod_pos, by omega⟩, hmod_ndvd⟩
  · intro i₁ hi₁ i₂ hi₂ hEq
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi₁ hi₂
    have hq : (i₁ - k0) / N = (i₂ - k0) / N := congrArg Prod.fst hEq
    have hr : (2 * i₁ + 2) % N = (2 * i₂ + 2) % N := congrArg Prod.snd hEq
    set r₁ := (i₁ - k0) % N
    set r₂ := (i₂ - k0) % N
    have hr1_lt : r₁ < N := Nat.mod_lt _ (by omega)
    have hr2_lt : r₂ < N := Nat.mod_lt _ (by omega)
    have he1 : 2 * i₁ + 2 = (2 * ((i₁ - k0) / N) + c) * N + ((N + 3) / 2 + 2 * r₁) := by
      have hi1 : i₁ = k0 + N * ((i₁ - k0) / N) + r₁ := by
        have := Nat.div_add_mod (i₁ - k0) N; omega
      have hNhalf : (N + 3) / 2 = (N + 1) / 2 + 1 := by omega
      calc 2 * i₁ + 2 = (2 * k0 + 1) + 2 * (N * ((i₁ - k0) / N)) + 2 * r₁ + 1 := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * ((i₁ - k0) / N)) + 2 * r₁ + 1 := by rw [h2k0]
        _ = (2 * ((i₁ - k0) / N) + c) * N + ((N + 1) / 2 + 1 + 2 * r₁) := by ring
        _ = (2 * ((i₁ - k0) / N) + c) * N + ((N + 3) / 2 + 2 * r₁) := by rw [← hNhalf]
    have he2 : 2 * i₂ + 2 = (2 * ((i₂ - k0) / N) + c) * N + ((N + 3) / 2 + 2 * r₂) := by
      have hi2 : i₂ = k0 + N * ((i₂ - k0) / N) + r₂ := by
        have := Nat.div_add_mod (i₂ - k0) N; omega
      have hNhalf : (N + 3) / 2 = (N + 1) / 2 + 1 := by omega
      calc 2 * i₂ + 2 = (2 * k0 + 1) + 2 * (N * ((i₂ - k0) / N)) + 2 * r₂ + 1 := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * ((i₂ - k0) / N)) + 2 * r₂ + 1 := by rw [h2k0]
        _ = (2 * ((i₂ - k0) / N) + c) * N + ((N + 1) / 2 + 1 + 2 * r₂) := by ring
        _ = (2 * ((i₂ - k0) / N) + c) * N + ((N + 3) / 2 + 2 * r₂) := by rw [← hNhalf]
    have hmod_eq : ((N + 3) / 2 + 2 * r₁) % N = ((N + 3) / 2 + 2 * r₂) % N := by
      rw [he1, he2, Nat.mul_add_mod_self_right, Nat.mul_add_mod_self_right] at hr
      exact hr
    have hr_eq : r₁ = r₂ := by
      have hcop2 : Nat.Coprime N 2 := by
        rw [Nat.coprime_two_right]; exact Nat.odd_iff.mpr (by omega)
      by_cases hle : r₁ ≤ r₂
      · have hdvd : N ∣ 2 * (r₂ - r₁) := by
          have hsub : ((N + 3) / 2 + 2 * r₂) - ((N + 3) / 2 + 2 * r₁) = 2 * (r₂ - r₁) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq
        have hdvd' : N ∣ r₂ - r₁ := hcop2.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₂ - r₁) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
      · have hdvd : N ∣ 2 * (r₁ - r₂) := by
          have hsub : ((N + 3) / 2 + 2 * r₁) - ((N + 3) / 2 + 2 * r₂) = 2 * (r₁ - r₂) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq.symm
        have hdvd' : N ∣ r₁ - r₂ := hcop2.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₁ - r₂) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
    have hdm1 : N * ((i₁ - k0) / N) + r₁ = i₁ - k0 := Nat.div_add_mod (i₁ - k0) N
    have hdm2 : N * ((i₂ - k0) / N) + r₂ = i₂ - k0 := Nat.div_add_mod (i₂ - k0) N
    rw [hq, hr_eq] at hdm1
    omega
  · rintro ⟨t, a⟩ hta
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc] at hta
    rcases hta with ⟨ht, ⟨ha1, haN⟩, ha_ndvd⟩
    let r_idx := (qDen4 N a * N + a - (N + 3) / 2) / 2
    have hr_eq : (N + 3) / 2 + 2 * r_idx = qDen4 N a * N + a := by
      dsimp [r_idx, qDen4]; split_ifs <;> omega
    have hr_lt : r_idx < N := by
      dsimp [r_idx, qDen4]; split_ifs <;> omega
    let i := k0 + t * N + r_idx
    have hi_exp : 2 * i + 2 = (2 * t + c + qDen4 N a) * N + a := by
      have hNhalf : (N + 3) / 2 = (N + 1) / 2 + 1 := by omega
      calc 2 * i + 2 = (2 * k0 + 1) + 2 * (t * N) + 2 * r_idx + 1 := by dsimp [i]; ring
        _ = (c * N + (N + 1) / 2) + 2 * (t * N) + 2 * r_idx + 1 := by rw [h2k0]
        _ = c * N + 2 * (t * N) + ((N + 1) / 2 + 1 + 2 * r_idx) := by ring
        _ = c * N + 2 * (t * N) + ((N + 3) / 2 + 2 * r_idx) := by rw [← hNhalf]
        _ = c * N + 2 * (t * N) + (qDen4 N a * N + a) := by rw [hr_eq]
        _ = (2 * t + c + qDen4 N a) * N + a := by ring
    refine ⟨i, ?_, ?_⟩
    · simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨by omega, ?_⟩, ?_⟩
      · have hlt : t * N + r_idx < M * N := by
          calc t * N + r_idx < t * N + N := by omega
            _ = (t + 1) * N := by ring
            _ ≤ M * N := Nat.mul_le_mul_right N ht
        omega
      · intro hd
        rw [hi_exp] at hd
        have h1 := Nat.dvd_sub hd (dvd_trans hn_dvd_N (dvd_mul_left N (2 * t + c + qDen4 N a)))
        rw [Nat.add_sub_cancel_left] at h1
        exact ha_ndvd h1
    · refine Prod.ext ?_ ?_
      · dsimp [i]
        have : k0 + t * N + r_idx - k0 = r_idx + N * t := by ring_nf; omega
        rw [this, Nat.add_mul_div_left _ _ (by omega), Nat.div_eq_of_lt hr_lt, zero_add]
      · rw [hi_exp, Nat.mul_add_mod_self_right, Nat.mod_eq_of_lt (by omega)]
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    set t := (i - k0) / N
    set r_idx := (i - k0) % N
    set a := (2 * i + 2) % N
    have hr_lt : r_idx < N := Nat.mod_lt _ (by omega)
    have he : 2 * i + 2 = (2 * t + c) * N + ((N + 3) / 2 + 2 * r_idx) := by
      have hi1 : i = k0 + N * t + r_idx := by
        have hdm : N * t + r_idx = i - k0 := Nat.div_add_mod (i - k0) N; omega
      have hNhalf : (N + 3) / 2 = (N + 1) / 2 + 1 := by omega
      calc 2 * i + 2 = (2 * k0 + 1) + 2 * (N * t) + 2 * r_idx + 1 := by omega
        _ = (c * N + (N + 1) / 2) + 2 * (N * t) + 2 * r_idx + 1 := by rw [h2k0]
        _ = (2 * t + c) * N + ((N + 1) / 2 + 1 + 2 * r_idx) := by ring
        _ = (2 * t + c) * N + ((N + 3) / 2 + 2 * r_idx) := by rw [← hNhalf]
    have ha_eq : a = ((N + 3) / 2 + 2 * r_idx) % N := by
      dsimp [a]; rw [he, Nat.mul_add_mod_self_right]
    have ha_pos : 1 ≤ a := by
      by_contra h0
      have ha0 : a = 0 := by omega
      have hdN : N ∣ 2 * i + 2 := Nat.dvd_of_mod_eq_zero ha0
      exact hi.2 (dvd_trans hn_dvd_N hdN)
    have ha_lt : a < N := Nat.mod_lt _ (by omega)
    have hq_val : ((N + 3) / 2 + 2 * r_idx) = qDen4 N a * N + a := by
      have hdiv_mod := Nat.div_add_mod ((N + 3) / 2 + 2 * r_idx) N
      rw [← ha_eq, mul_comm] at hdiv_mod
      set q := ((N + 3) / 2 + 2 * r_idx) / N
      have hq_le2 : q ≤ 2 := by
        by_contra hgt
        have h3 : 3 ≤ q := by omega
        have : 3 * N ≤ q * N := Nat.mul_le_mul_right N h3
        omega
      have hev_sum : (q * N + a) % 2 = 0 := by omega
      have hq_eq : q = qDen4 N a := by
        dsimp [qDen4]
        split_ifs with ha_odd ha_half
        · interval_cases q <;> omega
        · interval_cases q <;> omega
        · interval_cases q <;> omega
      rw [← hq_eq]; omega
    congr 2
    rw [he, hq_val]; ring

/-- **Main Theorem 1 (Guo `arXiv:2310.15207v1`, Section 6, Conjecture 6.4 `conj:4`):**
For every integer `n ≡ 1 (mod 4)` with `n > 1` and all positive integers `r > s`,
`R₄(n, r; q) ≡ R₄(n, s; q) (mod Φ_{n^s}(q)^2)`. -/
theorem guo_conjecture_6_4 {n r s : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hrs : s < r) :
    RatCongMod (num4 n r) (den4 n r) (num4 n s) (den4 n s) (Phi (n ^ s) ^ 2) := by
  set N := n ^ s with hN_def
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hN_ge5 : 5 ≤ N := by
    have hn5 : 5 ≤ n := by omega
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  apply ratCongMod_of_telescoping
    (fun k _ => num4_ne_zero (by omega) k)
    (fun k _ => den4_ne_zero (by omega) k)
  · refine ⟨num4 n s, den4 n s, ?_, rfl⟩
    unfold den4
    rw [qPoch_X_pow_eq, qPoch_X_pow_eq]
    refine IsCoprime.mul_left ?_ ?_
    · refine IsCoprime.prod_left fun k hk => ?_
      have hlt : k < (N - 1) / 4 := Finset.mem_range.mp hk
      exact isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => by
        have := Nat.le_of_dvd (by omega) hd; omega)
    · refine IsCoprime.prod_left fun k hk => ?_
      have hlt : k < (n ^ (s - 1) - 1) / 4 := Finset.mem_range.mp hk
      have hns : n * n ^ (s - 1) = N := by
        rw [hN_def, ← pow_succ', Nat.sub_add_cancel hs]
      have hbound : n + 2 * n * k < N := by
        have h1 : 4 * k + 4 ≤ n ^ (s - 1) - 1 := by
          have := pow_mod_four_eq_one hn4 (s - 1); omega
        have h2 : 2 * k + 1 < n ^ (s - 1) := by omega
        calc n + 2 * n * k = n * (2 * k + 1) := by ring
          _ < n * n ^ (s - 1) := Nat.mul_lt_mul_of_pos_left h2 (by omega)
          _ = N := hns
      exact isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => by
        have := Nat.le_of_dvd (by omega) hd; omega)
  · intro k hk
    set k0 := (n ^ k - 1) / 4
    set k1 := (n ^ (k + 1) - 1) / 4
    let U : Polynomial ℚ := ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 1)), (1 - X ^ (2 * i + 1))
    let V : Polynomial ℚ := ∏ i ∈ (Finset.Ico k0 k1).filter (fun i => ¬ n ∣ (2 * i + 2)), (1 - X ^ (2 * i + 2))
    refine ⟨U, V, ?_, guo64_cancel_step hn4 hn1 (by omega), ?_⟩
    · refine IsCoprime.prod_left fun i hi => ?_
      have hndvd_n : ¬ n ∣ (2 * i + 2) := (Finset.mem_filter.mp hi).2
      exact isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => hndvd_n (dvd_trans hn_dvd_N hd))
    · rw [← mk2_eq_iff]
      dsimp only [U, V, k0, k1]
      rw [guo64_blocks_U hn4 hn1 hs hk, guo64_blocks_V hn4 hn1 hs hk, map_prod, map_prod]
      let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
      let c := (n ^ (k - s) - 1) / 2
      refine Finset.prod_congr rfl fun t _ => ?_
      apply block_prod_congr_mod_Phi_sq S (fun a ha => by
        simp only [S, Finset.mem_filter, Finset.mem_Icc] at ha; omega) (2 * t + c) (qNum4 N) (qDen4 N)
      intro w hw
      let Δ : ℕ → ℤ := fun a => (qNum4 N a : ℤ) - (qDen4 N a : ℤ)
      refine symmetric_pairing_vanishes (by omega) hn_dvd_N Δ ?_ ?_ w hw
      · intro a ha1 haN
        dsimp [Δ, qNum4, qDen4]
        split_ifs <;> omega
      · have hΔ_eq : ∀ a ∈ Finset.Icc 1 ((N - 1) / 2), Δ a = (-1 : ℤ) ^ (a - 1) := by
          intro a ha
          have hab := Finset.mem_Icc.mp ha
          dsimp [Δ, qNum4, qDen4]
          by_cases hev : a % 2 = 0
          · simp [hev, hab.2]
            have hpow : (-1 : ℤ) ^ (a - 1) = -1 := by
              have : Odd (a - 1) := Nat.odd_iff.mpr (by omega)
              exact Odd.neg_one_pow this
            exact hpow.symm
          · have h1 : a % 2 = 1 := by omega
            simp [h1, hab.2]
            have hpow : (-1 : ℤ) ^ (a - 1) = 1 := by
              have : Even (a - 1) := Nat.even_iff.mpr (by omega)
              exact Even.neg_one_pow this
            exact hpow.symm
        have htot : ∑ a ∈ Finset.Icc 1 ((N - 1) / 2), Δ a = 0 := by
          rw [Finset.sum_congr rfl hΔ_eq, show (N - 1) / 2 = 2 * ((N - 1) / 4) by omega]
          exact sum_alt_even_zero _
        have hmult : ∑ a ∈ (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => n ∣ a), Δ a = 0 := by
          rw [Finset.sum_congr rfl (fun a ha => hΔ_eq a (Finset.mem_filter.mp ha).1)]
          have hbij : ∑ a ∈ (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => n ∣ a), (-1 : ℤ) ^ (a - 1) =
              ∑ m ∈ Finset.Icc 1 ((n ^ (s - 1) - 1) / 2), (-1 : ℤ) ^ (m - 1) := by
            have hns : n * n ^ (s - 1) = N := by
              rw [hN_def, ← pow_succ', Nat.sub_add_cancel hs]
            have hs4 : n ^ (s - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (s - 1)
            have hn2 : n % 2 = 1 := by omega
            symm
            refine Finset.sum_bij (fun m _ => n * m) ?_ ?_ ?_ ?_
            · intro m hm
              simp only [Finset.mem_filter, Finset.mem_Icc] at hm ⊢
              refine ⟨⟨by nlinarith, ?_⟩, dvd_mul_right n m⟩
              have h1 : 2 * m < n ^ (s - 1) := by omega
              have h2 : 2 * (n * m) < N := by
                calc 2 * (n * m) = n * (2 * m) := by ring
                  _ < n * n ^ (s - 1) := Nat.mul_lt_mul_of_pos_left h1 (by omega)
                  _ = N := hns
              omega
            · intro m₁ _ m₂ _ hEq
              exact Nat.eq_of_mul_eq_mul_left (by omega) hEq
            · intro a ha
              simp only [Finset.mem_filter, Finset.mem_Icc] at ha
              rcases ha.2 with ⟨m, rfl⟩
              refine ⟨m, Finset.mem_Icc.mpr ⟨?_, ?_⟩, rfl⟩
              · by_contra h0
                have hm0 : m = 0 := by omega
                rw [hm0, mul_zero] at ha
                omega
              · have h1 : 2 * (n * m) < N := by omega
                have h2 : n * (2 * m) < n * n ^ (s - 1) := by rw [hns]; linarith
                have h3 := Nat.lt_of_mul_lt_mul_left h2
                omega
            · intro m hm
              have hm1 := (Finset.mem_Icc.mp hm).1
              have hnm1 : 1 ≤ n * m := by nlinarith
              by_cases hme : m % 2 = 0
              · have h1 : Odd (m - 1) := Nat.odd_iff.mpr (by omega)
                have h2 : Odd (n * m - 1) := Nat.odd_iff.mpr (by
                  have : (n * m) % 2 = 0 := by rw [Nat.mul_mod, hme]; omega
                  omega)
                rw [h1.neg_one_pow, h2.neg_one_pow]
              · have h1 : Even (m - 1) := Nat.even_iff.mpr (by omega)
                have h2 : Even (n * m - 1) := Nat.even_iff.mpr (by
                  have : (n * m) % 2 = 1 := by rw [Nat.mul_mod, hn2]; omega
                  omega)
                rw [h1.neg_one_pow, h2.neg_one_pow]
          rw [hbij]
          have hs4 : n ^ (s - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (s - 1)
          rw [show (n ^ (s - 1) - 1) / 2 = 2 * ((n ^ (s - 1) - 1) / 4) by omega]
          exact sum_alt_even_zero _
        have hsplit := Finset.sum_filter_add_sum_filter_not (Finset.Icc 1 ((N - 1) / 2))
          (fun a => n ∣ a) Δ
        linarith
  · exact hrs.le

/-! ## Section 4: Proof of Conjecture 6.3 (`conj:3`) -/

private lemma num3_ne_zero {n : ℕ} (hn : 1 ≤ n) (r : ℕ) : num3 n r ≠ 0 := by
  unfold num3
  exact mul_ne_zero (mul_ne_zero (qNum_ne_zero hn) (qPoch_X_pow_ne_zero 3 4 _ (by decide)))
    (qPoch_X_pow_ne_zero (5 * n) (4 * n) _ (by omega))

private lemma den3_ne_zero {n : ℕ} (hn : 1 ≤ n) (r : ℕ) : den3 n r ≠ 0 := by
  unfold den3
  exact mul_ne_zero (qPoch_X_pow_ne_zero 5 4 _ (by decide))
    (qPoch_X_pow_ne_zero (3 * n) (4 * n) _ (by omega))

/-- Pair-by-pair cancellation `∑_{a=1}^{2K} Δ₃(a) = 0` where `Δ₃(a) = -2` (`a % 4 ∈ {0, 1}`),
`+2` (`a % 4 ∈ {2, 3}`). -/
private lemma sum_delta3_even_zero (K : ℕ) :
    ∑ a ∈ Finset.Icc 1 (2 * K), (if a % 4 ≤ 1 then (-2 : ℤ) else 2) = 0 := by
  induction K with
  | zero => simp
  | succ K ih =>
    have h1 : Finset.Icc 1 (2 * (K + 1)) =
        insert (2 * K + 2) (insert (2 * K + 1) (Finset.Icc 1 (2 * K))) := by
      ext x; simp only [Finset.mem_insert, Finset.mem_Icc]; omega
    rw [h1, Finset.sum_insert (by simp), Finset.sum_insert (by simp), ih, add_zero]
    split_ifs <;> omega

/-- Step 1 of Conjecture 6.3: exact `n`-multiple cancellation for `num3 / den3`. -/
private lemma guo63_cancel_step {n k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n) (hk1 : 1 ≤ k) :
    let v0 := (n ^ k - 1) / 2
    let v1 := (n ^ (k + 1) - 1) / 2
    let U : Polynomial ℚ := ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 3)), (1 - X ^ (4 * i + 3))
    let V : Polynomial ℚ := ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 5)), (1 - X ^ (4 * i + 5))
    num3 n (k + 1) * den3 n k * V = den3 n (k + 1) * num3 n k * U := by
  intro v0 v1 U V
  set w0 := (n ^ (k - 1) - 1) / 2
  have hn5 : 5 ≤ n := by omega
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hnk_prev4 : n ^ (k - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k - 1)
  have hv0_le_v1 : v0 ≤ v1 := by
    have : n ^ k ≤ n ^ (k + 1) := Nat.pow_le_pow_right (by omega) (by omega)
    omega
  have hw0_le_v0 : w0 ≤ v0 := by
    have : n ^ (k - 1) ≤ n ^ k := Nat.pow_le_pow_right (by omega) (by omega)
    omega
  have hnn_prev : n * n ^ (k - 1) = n ^ k := by
    rw [← pow_succ', Nat.sub_add_cancel hk1]
  have hnn_curr : n * n ^ k = n ^ (k + 1) := by rw [← pow_succ']
  have hnum_split : num3 n (k + 1) = num3 n k *
      (∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 3))) *
      (∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 5)))) := by
    unfold num3
    have hk_sub : k + 1 - 1 = k := Nat.add_sub_cancel k 1
    rw [hk_sub, qPoch_split_Ico (a := X ^ 3) (q := X ^ 4) hv0_le_v1,
      qPoch_split_Ico (a := X ^ (5 * n)) (q := X ^ (4 * n)) hw0_le_v0]
    have h1 : ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ 3 * (X ^ 4) ^ i) =
        ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 3)) :=
      Finset.prod_congr rfl fun i _ => by rw [← pow_mul, ← pow_add]; congr 2; omega
    have h2 : ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (5 * n) * (X ^ (4 * n)) ^ j) =
        ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 5))) :=
      Finset.prod_congr rfl fun j _ => by rw [← pow_mul, ← pow_add]; congr 2; ring
    rw [h1, h2]; ring
  have hden_split : den3 n (k + 1) = den3 n k *
      (∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 5))) *
      (∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 3)))) := by
    unfold den3
    have hk_sub : k + 1 - 1 = k := Nat.add_sub_cancel k 1
    rw [hk_sub, qPoch_split_Ico (a := X ^ 5) (q := X ^ 4) hv0_le_v1,
      qPoch_split_Ico (a := X ^ (3 * n)) (q := X ^ (4 * n)) hw0_le_v0]
    have h1 : ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ 5 * (X ^ 4) ^ i) =
        ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 5)) :=
      Finset.prod_congr rfl fun i _ => by rw [← pow_mul, ← pow_add]; congr 2; omega
    have h2 : ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (3 * n) * (X ^ (4 * n)) ^ j) =
        ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 3))) :=
      Finset.prod_congr rfl fun j _ => by rw [← pow_mul, ← pow_add]; congr 2; ring
    rw [h1, h2]; ring
  have h3_cancel : ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => n ∣ (4 * i + 3)),
        (1 - (X : Polynomial ℚ) ^ (4 * i + 3)) =
      ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 3))) := by
    symm
    refine Finset.prod_bij (fun j _ => (n * (4 * j + 3) - 3) / 4) ?_ ?_ ?_ ?_
    · intro j hj
      have hjb := Finset.mem_Ico.mp hj
      have hmod4 : (n * (4 * j + 3)) % 4 = 3 := by rw [Nat.mul_mod, hn4]; omega
      have hge3 : 3 ≤ n * (4 * j + 3) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 3 ≤ 4 * j + 3); omega
      have h4i : 4 * ((n * (4 * j + 3) - 3) / 4) + 3 = n * (4 * j + 3) := by omega
      simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · have h1 : 2 * w0 + 1 = n ^ (k - 1) := by omega
        have h2 : 2 * v0 + 1 = n ^ k := by omega
        have h3 : n * (4 * w0 + 2) < n * (4 * j + 3) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * w0 + 2) = 4 * v0 + 2 := by
          calc n * (4 * w0 + 2) = 2 * (n * (2 * w0 + 1)) := by ring
            _ = 2 * (2 * v0 + 1) := by rw [h1, hnn_prev, h2]
            _ = 4 * v0 + 2 := by ring
        omega
      · have h1 : 2 * v0 + 1 = n ^ k := by omega
        have h2 : 2 * v1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (4 * j + 3) < n * (4 * v0 + 2) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * v0 + 2) = 4 * v1 + 2 := by
          calc n * (4 * v0 + 2) = 2 * (n * (2 * v0 + 1)) := by ring
            _ = 2 * (2 * v1 + 1) := by rw [h1, hnn_curr, h2]
            _ = 4 * v1 + 2 := by ring
        omega
      · rw [h4i]; exact dvd_mul_right n _
    · intro j₁ _ j₂ _ hEq
      have h1 : (n * (4 * j₁ + 3)) % 4 = 3 := by rw [Nat.mul_mod, hn4]; omega
      have h2 : (n * (4 * j₂ + 3)) % 4 = 3 := by rw [Nat.mul_mod, hn4]; omega
      have hg1 : 3 ≤ n * (4 * j₁ + 3) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 3 ≤ 4 * j₁ + 3); omega
      have hg2 : 3 ≤ n * (4 * j₂ + 3) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 3 ≤ 4 * j₂ + 3); omega
      have hmul : n * (4 * j₁ + 3) = n * (4 * j₂ + 3) := by omega
      have hcancel := Nat.eq_of_mul_eq_mul_left (by omega : 0 < n) hmul
      omega
    · intro i hi
      simp only [Finset.mem_filter, Finset.mem_Ico] at hi
      rcases hi.2 with ⟨q, hq⟩
      have hq4 : q % 4 = 3 := by
        have : (n * q) % 4 = 3 := by omega
        rw [Nat.mul_mod, hn4] at this; omega
      have h4q : 4 * (q / 4) + 3 = q := by omega
      refine ⟨q / 4, Finset.mem_Ico.mpr ⟨?_, ?_⟩, ?_⟩
      · have h1 : 2 * w0 + 1 = n ^ (k - 1) := by omega
        have h2 : 2 * v0 + 1 = n ^ k := by omega
        have h3 : n * (4 * w0 + 2) < n * q := by
          calc n * (4 * w0 + 2) = 2 * (n * (2 * w0 + 1)) := by ring
            _ = 2 * (2 * v0 + 1) := by rw [h1, hnn_prev, h2]
            _ < 4 * i + 3 := by omega
            _ = n * q := hq
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · have h1 : 2 * v0 + 1 = n ^ k := by omega
        have h2 : 2 * v1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * q < n * (4 * v0 + 2) := by
          calc n * q = 4 * i + 3 := hq.symm
            _ < 2 * (2 * v1 + 1) := by omega
            _ = 2 * (n * (2 * v0 + 1)) := by rw [h2, ← hnn_curr, h1]
            _ = n * (4 * v0 + 2) := by ring
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · rw [h4q, ← hq]; omega
    · intro j _
      have hmod4 : (n * (4 * j + 3)) % 4 = 3 := by rw [Nat.mul_mod, hn4]; omega
      have hge3 : 3 ≤ n * (4 * j + 3) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 3 ≤ 4 * j + 3); omega
      congr 2; omega
  have h5_cancel : ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => n ∣ (4 * i + 5)),
        (1 - (X : Polynomial ℚ) ^ (4 * i + 5)) =
      ∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 5))) := by
    symm
    refine Finset.prod_bij (fun j _ => (n * (4 * j + 5) - 5) / 4) ?_ ?_ ?_ ?_
    · intro j hj
      have hjb := Finset.mem_Ico.mp hj
      have hmod4 : (n * (4 * j + 5)) % 4 = 1 := by rw [Nat.mul_mod, hn4]; omega
      have hge5 : 5 ≤ n * (4 * j + 5) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 5 ≤ 4 * j + 5); omega
      have h4i : 4 * ((n * (4 * j + 5) - 5) / 4) + 5 = n * (4 * j + 5) := by omega
      simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · have h1 : 2 * w0 + 1 = n ^ (k - 1) := by omega
        have h2 : 2 * v0 + 1 = n ^ k := by omega
        have h3 : n * (4 * w0 + 2) < n * (4 * j + 5) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * w0 + 2) = 4 * v0 + 2 := by
          calc n * (4 * w0 + 2) = 2 * (n * (2 * w0 + 1)) := by ring
            _ = 2 * (2 * v0 + 1) := by rw [h1, hnn_prev, h2]
            _ = 4 * v0 + 2 := by ring
        omega
      · have h1 : 2 * v0 + 1 = n ^ k := by omega
        have h2 : 2 * v1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * (4 * j + 5) < n * (4 * v0 + 2) :=
          Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
        have h4 : n * (4 * v0 + 2) = 4 * v1 + 2 := by
          calc n * (4 * v0 + 2) = 2 * (n * (2 * v0 + 1)) := by ring
            _ = 2 * (2 * v1 + 1) := by rw [h1, hnn_curr, h2]
            _ = 4 * v1 + 2 := by ring
        omega
      · rw [h4i]; exact dvd_mul_right n _
    · intro j₁ _ j₂ _ hEq
      have h1 : (n * (4 * j₁ + 5)) % 4 = 1 := by rw [Nat.mul_mod, hn4]; omega
      have h2 : (n * (4 * j₂ + 5)) % 4 = 1 := by rw [Nat.mul_mod, hn4]; omega
      have hg1 : 5 ≤ n * (4 * j₁ + 5) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 5 ≤ 4 * j₁ + 5); omega
      have hg2 : 5 ≤ n * (4 * j₂ + 5) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 5 ≤ 4 * j₂ + 5); omega
      have hmul : n * (4 * j₁ + 5) = n * (4 * j₂ + 5) := by omega
      have hcancel := Nat.eq_of_mul_eq_mul_left (by omega : 0 < n) hmul
      omega
    · intro i hi
      simp only [Finset.mem_filter, Finset.mem_Ico] at hi
      rcases hi.2 with ⟨q, hq⟩
      have hq4 : q % 4 = 1 := by
        have : (n * q) % 4 = 1 := by omega
        rw [Nat.mul_mod, hn4] at this; omega
      have hq_ge5 : 5 ≤ q := by
        have h2v0 : 2 * v0 + 1 = n ^ k := by omega
        have hnk_ge : n ≤ n ^ k := by
          calc n = n ^ 1 := (pow_one n).symm
            _ ≤ n ^ k := Nat.pow_le_pow_right (by omega) hk1
        have hlt : n * 1 < n * q := by omega
        have hq_gt1 := Nat.lt_of_mul_lt_mul_left hlt
        omega
      have h4q : 4 * ((q - 5) / 4) + 5 = q := by omega
      refine ⟨(q - 5) / 4, Finset.mem_Ico.mpr ⟨?_, ?_⟩, ?_⟩
      · have h1 : 2 * w0 + 1 = n ^ (k - 1) := by omega
        have h2 : 2 * v0 + 1 = n ^ k := by omega
        have h3 : n * (4 * w0 + 2) < n * q := by
          calc n * (4 * w0 + 2) = 2 * (n * (2 * w0 + 1)) := by ring
            _ = 2 * (2 * v0 + 1) := by rw [h1, hnn_prev, h2]
            _ < 4 * i + 5 := by omega
            _ = n * q := hq
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · have h1 : 2 * v0 + 1 = n ^ k := by omega
        have h2 : 2 * v1 + 1 = n ^ (k + 1) := by omega
        have h3 : n * q < n * (4 * v0 + 2) := by
          calc n * q = 4 * i + 5 := hq.symm
            _ < 2 * (2 * v1 + 1) := by omega
            _ = 2 * (n * (2 * v0 + 1)) := by rw [h2, ← hnn_curr, h1]
            _ = n * (4 * v0 + 2) := by ring
        have h4 := Nat.lt_of_mul_lt_mul_left h3
        omega
      · rw [h4q, ← hq]; omega
    · intro j _
      have hmod4 : (n * (4 * j + 5)) % 4 = 1 := by rw [Nat.mul_mod, hn4]; omega
      have hge5 : 5 ≤ n * (4 * j + 5) := by
        have := Nat.mul_le_mul (by omega : 1 ≤ n) (by omega : 5 ≤ 4 * j + 5); omega
      congr 2; omega
  have hsplit_num : ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 3)) =
      (∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 3)))) * U := by
    rw [← h3_cancel, Finset.prod_filter_mul_prod_filter_not]
  have hsplit_den : ∏ i ∈ Finset.Ico v0 v1, (1 - (X : Polynomial ℚ) ^ (4 * i + 5)) =
      (∏ j ∈ Finset.Ico w0 v0, (1 - (X : Polynomial ℚ) ^ (n * (4 * j + 5)))) * V := by
    rw [← h5_cancel, Finset.prod_filter_mul_prod_filter_not]
  rw [hnum_split, hden_split, hsplit_num, hsplit_den]
  ring

private def qNum3 (a : ℕ) : ℕ := (5 - a % 4) % 4
private def qDen3 (a : ℕ) : ℕ := (7 - a % 4) % 4

private lemma guo63_blocks_U {n s k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hk : s ≤ k) :
    let N := n ^ s
    let v0 := (n ^ k - 1) / 2
    let v1 := (n ^ (k + 1) - 1) / 2
    let K₀ := n ^ (k - s)
    let M₃ := (n - 1) / 2 * K₀
    let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
    (∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 3)), (1 - (X : Polynomial ℚ) ^ (4 * i + 3))) =
      ∏ t ∈ Finset.range M₃, ∏ a ∈ S, (1 - (X : Polynomial ℚ) ^ (a + (4 * t + 2 * K₀ + qNum3 a) * N)) := by
  intro N v0 v1 K₀ M₃ S
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hN_ge5 : 5 ≤ N := by
    have hn5 : 5 ≤ n := by omega
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  have hK₀N : K₀ * N = n ^ k := by
    dsimp [K₀, N]; rw [← pow_add, Nat.sub_add_cancel hk]
  have hv1_sub : v1 - v0 = M₃ * N := by
    have h1 : 2 * (v1 - v0) = n ^ (k + 1) - n ^ k := by omega
    have h2 : n ^ (k + 1) - n ^ k = (n - 1) * (K₀ * N) := by
      rw [hK₀N, pow_succ', Nat.sub_mul, one_mul]
    have h3 : 2 * M₃ = (n - 1) * K₀ := by
      dsimp [M₃]; have : 2 * ((n - 1) / 2) = n - 1 := by omega
      nlinarith
    nlinarith
  have h4v0 : 4 * v0 + 3 = 2 * K₀ * N + 1 := by
    have h1 : 2 * v0 + 1 = K₀ * N := by rw [hK₀N]; omega
    calc 4 * v0 + 3 = 2 * (2 * v0 + 1) + 1 := by ring
      _ = 2 * (K₀ * N) + 1 := by rw [h1]
      _ = 2 * K₀ * N + 1 := by ring
  have hcop4 : Nat.Coprime N 4 := by
    have h2 : Nat.Coprime N 2 := by
      rw [Nat.coprime_two_right]; exact Nat.odd_iff.mpr (by omega)
    have h4 : (4 : ℕ) = 2 ^ 2 := by decide
    rw [h4]
    exact h2.pow_right 2
  rw [← Finset.prod_product']
  refine Finset.prod_bij (fun i _ => ((i - v0) / N, (4 * i + 3) % N)) ?_ ?_ ?_ ?_
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc]
    have hdiv : (i - v0) / N < M₃ := by
      rw [Nat.div_lt_iff_lt_mul (by omega)]; omega
    have hmod_ndvd : ¬ n ∣ (4 * i + 3) % N := by
      intro hd
      have h1 := Nat.dvd_add (dvd_trans hn_dvd_N (dvd_mul_right N ((4 * i + 3) / N))) hd
      rw [Nat.div_add_mod] at h1
      exact hi.2 h1
    have hmod_pos : 1 ≤ (4 * i + 3) % N := by
      by_contra h0
      have hmod0 : (4 * i + 3) % N = 0 := by omega
      exact hmod_ndvd (by rw [hmod0]; exact dvd_zero n)
    have hmod_lt : (4 * i + 3) % N < N := Nat.mod_lt _ (by omega)
    exact ⟨hdiv, ⟨hmod_pos, by omega⟩, hmod_ndvd⟩
  · intro i₁ hi₁ i₂ hi₂ hEq
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi₁ hi₂
    have hq : (i₁ - v0) / N = (i₂ - v0) / N := congrArg Prod.fst hEq
    have hr : (4 * i₁ + 3) % N = (4 * i₂ + 3) % N := congrArg Prod.snd hEq
    set r₁ := (i₁ - v0) % N
    set r₂ := (i₂ - v0) % N
    have hr1_lt : r₁ < N := Nat.mod_lt _ (by omega)
    have hr2_lt : r₂ < N := Nat.mod_lt _ (by omega)
    have he1 : 4 * i₁ + 3 = (4 * ((i₁ - v0) / N) + 2 * K₀) * N + (4 * r₁ + 1) := by
      have hi1 : i₁ = v0 + N * ((i₁ - v0) / N) + r₁ := by
        have := Nat.div_add_mod (i₁ - v0) N; omega
      calc 4 * i₁ + 3 = (4 * v0 + 3) + 4 * (N * ((i₁ - v0) / N)) + 4 * r₁ := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * ((i₁ - v0) / N)) + 4 * r₁ := by rw [h4v0]
        _ = (4 * ((i₁ - v0) / N) + 2 * K₀) * N + (4 * r₁ + 1) := by ring
    have he2 : 4 * i₂ + 3 = (4 * ((i₂ - v0) / N) + 2 * K₀) * N + (4 * r₂ + 1) := by
      have hi2 : i₂ = v0 + N * ((i₂ - v0) / N) + r₂ := by
        have := Nat.div_add_mod (i₂ - v0) N; omega
      calc 4 * i₂ + 3 = (4 * v0 + 3) + 4 * (N * ((i₂ - v0) / N)) + 4 * r₂ := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * ((i₂ - v0) / N)) + 4 * r₂ := by rw [h4v0]
        _ = (4 * ((i₂ - v0) / N) + 2 * K₀) * N + (4 * r₂ + 1) := by ring
    have hmod_eq : (4 * r₁ + 1) % N = (4 * r₂ + 1) % N := by
      rw [he1, he2, Nat.mul_add_mod_self_right, Nat.mul_add_mod_self_right] at hr
      exact hr
    have hr_eq : r₁ = r₂ := by
      by_cases hle : r₁ ≤ r₂
      · have hdvd : N ∣ 4 * (r₂ - r₁) := by
          have hsub : (4 * r₂ + 1) - (4 * r₁ + 1) = 4 * (r₂ - r₁) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq
        have hdvd' : N ∣ r₂ - r₁ := hcop4.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₂ - r₁) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
      · have hdvd : N ∣ 4 * (r₁ - r₂) := by
          have hsub : (4 * r₁ + 1) - (4 * r₂ + 1) = 4 * (r₁ - r₂) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq.symm
        have hdvd' : N ∣ r₁ - r₂ := hcop4.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₁ - r₂) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
    have hdm1 : N * ((i₁ - v0) / N) + r₁ = i₁ - v0 := Nat.div_add_mod (i₁ - v0) N
    have hdm2 : N * ((i₂ - v0) / N) + r₂ = i₂ - v0 := Nat.div_add_mod (i₂ - v0) N
    rw [hq, hr_eq] at hdm1
    omega
  · rintro ⟨t, a⟩ hta
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc] at hta
    rcases hta with ⟨ht, ⟨ha1, haN⟩, ha_ndvd⟩
    let r_idx := (qNum3 a * N + a - 1) / 4
    have hmod_q : (qNum3 a * N + a) % 4 = 1 := by
      rw [Nat.add_mod, Nat.mul_mod, hN4]; dsimp [qNum3]; omega
    have hr_eq : 4 * r_idx + 1 = qNum3 a * N + a := by dsimp [r_idx]; omega
    have hr_lt : r_idx < N := by
      have hq1_le : qNum3 a ≤ 3 := by dsimp [qNum3]; omega
      have hbound : qNum3 a * N + a < 4 * N := by
        have : qNum3 a * N ≤ 3 * N := Nat.mul_le_mul_right N hq1_le; omega
      dsimp [r_idx]; omega
    let i := v0 + t * N + r_idx
    have hi_exp : 4 * i + 3 = (4 * t + 2 * K₀ + qNum3 a) * N + a := by
      calc 4 * i + 3 = (4 * v0 + 3) + 4 * (t * N) + 4 * r_idx := by dsimp [i]; ring
        _ = (2 * K₀ * N + 1) + 4 * (t * N) + 4 * r_idx := by rw [h4v0]
        _ = 2 * K₀ * N + 4 * (t * N) + (4 * r_idx + 1) := by ring
        _ = 2 * K₀ * N + 4 * (t * N) + (qNum3 a * N + a) := by rw [hr_eq]
        _ = (4 * t + 2 * K₀ + qNum3 a) * N + a := by ring
    refine ⟨i, ?_, ?_⟩
    · simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨by omega, ?_⟩, ?_⟩
      · have hlt : t * N + r_idx < M₃ * N := by
          calc t * N + r_idx < t * N + N := by omega
            _ = (t + 1) * N := by ring
            _ ≤ M₃ * N := Nat.mul_le_mul_right N ht
        omega
      · intro hd
        rw [hi_exp] at hd
        have h1 := Nat.dvd_sub hd (dvd_trans hn_dvd_N (dvd_mul_left N (4 * t + 2 * K₀ + qNum3 a)))
        rw [Nat.add_sub_cancel_left] at h1
        exact ha_ndvd h1
    · refine Prod.ext ?_ ?_
      · dsimp [i]
        have : v0 + t * N + r_idx - v0 = r_idx + N * t := by ring_nf; omega
        rw [this, Nat.add_mul_div_left _ _ (by omega), Nat.div_eq_of_lt hr_lt, zero_add]
      · rw [hi_exp, Nat.mul_add_mod_self_right, Nat.mod_eq_of_lt (by omega)]
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    set t := (i - v0) / N
    set r_idx := (i - v0) % N
    set a := (4 * i + 3) % N
    have hr_lt : r_idx < N := Nat.mod_lt _ (by omega)
    have he : 4 * i + 3 = (4 * t + 2 * K₀) * N + (4 * r_idx + 1) := by
      have hi1 : i = v0 + N * t + r_idx := by
        have hdm : N * t + r_idx = i - v0 := Nat.div_add_mod (i - v0) N; omega
      calc 4 * i + 3 = (4 * v0 + 3) + 4 * (N * t) + 4 * r_idx := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * t) + 4 * r_idx := by rw [h4v0]
        _ = (4 * t + 2 * K₀) * N + (4 * r_idx + 1) := by ring
    have ha_eq : a = (4 * r_idx + 1) % N := by
      dsimp [a]; rw [he, Nat.mul_add_mod_self_right]
    have ha_pos : 1 ≤ a := by
      by_contra h0
      have ha0 : a = 0 := by omega
      have hdN : N ∣ 4 * i + 3 := Nat.dvd_of_mod_eq_zero ha0
      exact hi.2 (dvd_trans hn_dvd_N hdN)
    have ha_lt : a < N := Nat.mod_lt _ (by omega)
    have hq_val : 4 * r_idx + 1 = qNum3 a * N + a := by
      have hdiv_mod := Nat.div_add_mod (4 * r_idx + 1) N
      rw [← ha_eq, mul_comm] at hdiv_mod
      set q := (4 * r_idx + 1) / N
      have hq_le3 : q ≤ 3 := by
        by_contra hgt
        have h4 : 4 ≤ q := by omega
        have : 4 * N ≤ q * N := Nat.mul_le_mul_right N h4
        omega
      have hmod4_q : (q * N + a) % 4 = 1 := by omega
      have hq_mod4 : (q + a % 4) % 4 = 1 := by
        rw [Nat.add_mod, Nat.mul_mod, hN4] at hmod4_q
        simpa using hmod4_q
      have hq_eq : q = qNum3 a := by
        dsimp [qNum3]; interval_cases q <;> omega
      rw [← hq_eq]; omega
    congr 2
    rw [he, hq_val]; ring

private lemma guo63_blocks_V {n s k : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hk : s ≤ k) :
    let N := n ^ s
    let v0 := (n ^ k - 1) / 2
    let v1 := (n ^ (k + 1) - 1) / 2
    let K₀ := n ^ (k - s)
    let M₃ := (n - 1) / 2 * K₀
    let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
    (∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 5)), (1 - (X : Polynomial ℚ) ^ (4 * i + 5))) =
      ∏ t ∈ Finset.range M₃, ∏ a ∈ S, (1 - (X : Polynomial ℚ) ^ (a + (4 * t + 2 * K₀ + qDen3 a) * N)) := by
  intro N v0 v1 K₀ M₃ S
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hnk4 : n ^ k % 4 = 1 := pow_mod_four_eq_one hn4 k
  have hnk1_4 : n ^ (k + 1) % 4 = 1 := pow_mod_four_eq_one hn4 (k + 1)
  have hN_ge5 : 5 ≤ N := by
    have hn5 : 5 ≤ n := by omega
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  have hK₀N : K₀ * N = n ^ k := by
    dsimp [K₀, N]; rw [← pow_add, Nat.sub_add_cancel hk]
  have hv1_sub : v1 - v0 = M₃ * N := by
    have h1 : 2 * (v1 - v0) = n ^ (k + 1) - n ^ k := by omega
    have h2 : n ^ (k + 1) - n ^ k = (n - 1) * (K₀ * N) := by
      rw [hK₀N, pow_succ', Nat.sub_mul, one_mul]
    have h3 : 2 * M₃ = (n - 1) * K₀ := by
      dsimp [M₃]; have : 2 * ((n - 1) / 2) = n - 1 := by omega
      nlinarith
    nlinarith
  have h4v0 : 4 * v0 + 3 = 2 * K₀ * N + 1 := by
    have h1 : 2 * v0 + 1 = K₀ * N := by rw [hK₀N]; omega
    calc 4 * v0 + 3 = 2 * (2 * v0 + 1) + 1 := by ring
      _ = 2 * (K₀ * N) + 1 := by rw [h1]
      _ = 2 * K₀ * N + 1 := by ring
  have hcop4 : Nat.Coprime N 4 := by
    have h2 : Nat.Coprime N 2 := by
      rw [Nat.coprime_two_right]; exact Nat.odd_iff.mpr (by omega)
    have h4 : (4 : ℕ) = 2 ^ 2 := by decide
    rw [h4]
    exact h2.pow_right 2
  rw [← Finset.prod_product']
  refine Finset.prod_bij (fun i _ => ((i - v0) / N, (4 * i + 5) % N)) ?_ ?_ ?_ ?_
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc]
    have hdiv : (i - v0) / N < M₃ := by
      rw [Nat.div_lt_iff_lt_mul (by omega)]; omega
    have hmod_ndvd : ¬ n ∣ (4 * i + 5) % N := by
      intro hd
      have h1 := Nat.dvd_add (dvd_trans hn_dvd_N (dvd_mul_right N ((4 * i + 5) / N))) hd
      rw [Nat.div_add_mod] at h1
      exact hi.2 h1
    have hmod_pos : 1 ≤ (4 * i + 5) % N := by
      by_contra h0
      have hmod0 : (4 * i + 5) % N = 0 := by omega
      exact hmod_ndvd (by rw [hmod0]; exact dvd_zero n)
    have hmod_lt : (4 * i + 5) % N < N := Nat.mod_lt _ (by omega)
    exact ⟨hdiv, ⟨hmod_pos, by omega⟩, hmod_ndvd⟩
  · intro i₁ hi₁ i₂ hi₂ hEq
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi₁ hi₂
    have hq : (i₁ - v0) / N = (i₂ - v0) / N := congrArg Prod.fst hEq
    have hr : (4 * i₁ + 5) % N = (4 * i₂ + 5) % N := congrArg Prod.snd hEq
    set r₁ := (i₁ - v0) % N
    set r₂ := (i₂ - v0) % N
    have hr1_lt : r₁ < N := Nat.mod_lt _ (by omega)
    have hr2_lt : r₂ < N := Nat.mod_lt _ (by omega)
    have he1 : 4 * i₁ + 5 = (4 * ((i₁ - v0) / N) + 2 * K₀) * N + (4 * r₁ + 3) := by
      have hi1 : i₁ = v0 + N * ((i₁ - v0) / N) + r₁ := by
        have := Nat.div_add_mod (i₁ - v0) N; omega
      calc 4 * i₁ + 5 = (4 * v0 + 3) + 4 * (N * ((i₁ - v0) / N)) + 4 * r₁ + 2 := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * ((i₁ - v0) / N)) + 4 * r₁ + 2 := by rw [h4v0]
        _ = (4 * ((i₁ - v0) / N) + 2 * K₀) * N + (4 * r₁ + 3) := by ring
    have he2 : 4 * i₂ + 5 = (4 * ((i₂ - v0) / N) + 2 * K₀) * N + (4 * r₂ + 3) := by
      have hi2 : i₂ = v0 + N * ((i₂ - v0) / N) + r₂ := by
        have := Nat.div_add_mod (i₂ - v0) N; omega
      calc 4 * i₂ + 5 = (4 * v0 + 3) + 4 * (N * ((i₂ - v0) / N)) + 4 * r₂ + 2 := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * ((i₂ - v0) / N)) + 4 * r₂ + 2 := by rw [h4v0]
        _ = (4 * ((i₂ - v0) / N) + 2 * K₀) * N + (4 * r₂ + 3) := by ring
    have hmod_eq : (4 * r₁ + 3) % N = (4 * r₂ + 3) % N := by
      rw [he1, he2, Nat.mul_add_mod_self_right, Nat.mul_add_mod_self_right] at hr
      exact hr
    have hr_eq : r₁ = r₂ := by
      by_cases hle : r₁ ≤ r₂
      · have hdvd : N ∣ 4 * (r₂ - r₁) := by
          have hsub : (4 * r₂ + 3) - (4 * r₁ + 3) = 4 * (r₂ - r₁) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq
        have hdvd' : N ∣ r₂ - r₁ := hcop4.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₂ - r₁) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
      · have hdvd : N ∣ 4 * (r₁ - r₂) := by
          have hsub : (4 * r₁ + 3) - (4 * r₂ + 3) = 4 * (r₁ - r₂) := by omega
          rw [← hsub]
          exact (Nat.modEq_iff_dvd' (by omega)).mp hmod_eq.symm
        have hdvd' : N ∣ r₁ - r₂ := hcop4.dvd_of_dvd_mul_left hdvd
        rcases eq_or_ne (r₁ - r₂) 0 with h0 | hne
        · omega
        · have := Nat.le_of_dvd (by omega) hdvd'; omega
    have hdm1 : N * ((i₁ - v0) / N) + r₁ = i₁ - v0 := Nat.div_add_mod (i₁ - v0) N
    have hdm2 : N * ((i₂ - v0) / N) + r₂ = i₂ - v0 := Nat.div_add_mod (i₂ - v0) N
    rw [hq, hr_eq] at hdm1
    omega
  · rintro ⟨t, a⟩ hta
    simp only [Finset.mem_product, Finset.mem_range, S, Finset.mem_filter, Finset.mem_Icc] at hta
    rcases hta with ⟨ht, ⟨ha1, haN⟩, ha_ndvd⟩
    let r_idx := (qDen3 a * N + a - 3) / 4
    have hmod_q : (qDen3 a * N + a) % 4 = 3 := by
      rw [Nat.add_mod, Nat.mul_mod, hN4]; dsimp [qDen3]; omega
    have hge3 : 3 ≤ qDen3 a * N + a := by
      dsimp [qDen3]
      by_cases ha3 : 3 ≤ a
      · omega
      · have : 1 ≤ (7 - a % 4) % 4 := by omega
        have := Nat.mul_le_mul_right N this
        omega
    have hr_eq : 4 * r_idx + 3 = qDen3 a * N + a := by dsimp [r_idx]; omega
    have hr_lt : r_idx < N := by
      have hq2_le : qDen3 a ≤ 3 := by dsimp [qDen3]; omega
      have hbound : qDen3 a * N + a < 4 * N := by
        have : qDen3 a * N ≤ 3 * N := Nat.mul_le_mul_right N hq2_le; omega
      dsimp [r_idx]; omega
    let i := v0 + t * N + r_idx
    have hi_exp : 4 * i + 5 = (4 * t + 2 * K₀ + qDen3 a) * N + a := by
      calc 4 * i + 5 = (4 * v0 + 3) + 4 * (t * N) + 4 * r_idx + 2 := by dsimp [i]; ring
        _ = (2 * K₀ * N + 1) + 4 * (t * N) + 4 * r_idx + 2 := by rw [h4v0]
        _ = 2 * K₀ * N + 4 * (t * N) + (4 * r_idx + 3) := by ring
        _ = 2 * K₀ * N + 4 * (t * N) + (qDen3 a * N + a) := by rw [hr_eq]
        _ = (4 * t + 2 * K₀ + qDen3 a) * N + a := by ring
    refine ⟨i, ?_, ?_⟩
    · simp only [Finset.mem_filter, Finset.mem_Ico]
      refine ⟨⟨by omega, ?_⟩, ?_⟩
      · have hlt : t * N + r_idx < M₃ * N := by
          calc t * N + r_idx < t * N + N := by omega
            _ = (t + 1) * N := by ring
            _ ≤ M₃ * N := Nat.mul_le_mul_right N ht
        omega
      · intro hd
        rw [hi_exp] at hd
        have h1 := Nat.dvd_sub hd (dvd_trans hn_dvd_N (dvd_mul_left N (4 * t + 2 * K₀ + qDen3 a)))
        rw [Nat.add_sub_cancel_left] at h1
        exact ha_ndvd h1
    · refine Prod.ext ?_ ?_
      · dsimp [i]
        have : v0 + t * N + r_idx - v0 = r_idx + N * t := by ring_nf; omega
        rw [this, Nat.add_mul_div_left _ _ (by omega), Nat.div_eq_of_lt hr_lt, zero_add]
      · rw [hi_exp, Nat.mul_add_mod_self_right, Nat.mod_eq_of_lt (by omega)]
  · intro i hi
    simp only [Finset.mem_filter, Finset.mem_Ico] at hi
    set t := (i - v0) / N
    set r_idx := (i - v0) % N
    set a := (4 * i + 5) % N
    have hr_lt : r_idx < N := Nat.mod_lt _ (by omega)
    have he : 4 * i + 5 = (4 * t + 2 * K₀) * N + (4 * r_idx + 3) := by
      have hi1 : i = v0 + N * t + r_idx := by
        have hdm : N * t + r_idx = i - v0 := Nat.div_add_mod (i - v0) N; omega
      calc 4 * i + 5 = (4 * v0 + 3) + 4 * (N * t) + 4 * r_idx + 2 := by omega
        _ = (2 * K₀ * N + 1) + 4 * (N * t) + 4 * r_idx + 2 := by rw [h4v0]
        _ = (4 * t + 2 * K₀) * N + (4 * r_idx + 3) := by ring
    have ha_eq : a = (4 * r_idx + 3) % N := by
      dsimp [a]; rw [he, Nat.mul_add_mod_self_right]
    have ha_pos : 1 ≤ a := by
      by_contra h0
      have ha0 : a = 0 := by omega
      have hdN : N ∣ 4 * i + 5 := Nat.dvd_of_mod_eq_zero ha0
      exact hi.2 (dvd_trans hn_dvd_N hdN)
    have ha_lt : a < N := Nat.mod_lt _ (by omega)
    have hq_val : 4 * r_idx + 3 = qDen3 a * N + a := by
      have hdiv_mod := Nat.div_add_mod (4 * r_idx + 3) N
      rw [← ha_eq, mul_comm] at hdiv_mod
      set q := (4 * r_idx + 3) / N
      have hq_le3 : q ≤ 3 := by
        by_contra hgt
        have h4 : 4 ≤ q := by omega
        have : 4 * N ≤ q * N := Nat.mul_le_mul_right N h4
        omega
      have hmod4_q : (q * N + a) % 4 = 3 := by omega
      have hq_mod4 : (q + a % 4) % 4 = 3 := by
        rw [Nat.add_mod, Nat.mul_mod, hN4] at hmod4_q
        simpa using hmod4_q
      have hq_eq : q = qDen3 a := by
        dsimp [qDen3]; interval_cases q <;> omega
      rw [← hq_eq]; omega
    congr 2
    rw [he, hq_val]; ring

/-- **Main Theorem 2 (Guo `arXiv:2310.15207v1`, Section 6, Conjecture 6.3 `conj:3`):**
For every integer `n ≡ 1 (mod 4)` with `n > 1` and all positive integers `r > s`,
`R₃(n, r; q) ≡ R₃(n, s; q) (mod Φ_{n^s}(q)^2)`. -/
theorem guo_conjecture_6_3 {n r s : ℕ} (hn4 : n % 4 = 1) (hn1 : 1 < n)
    (hs : 1 ≤ s) (hrs : s < r) :
    RatCongMod (num3 n r) (den3 n r) (num3 n s) (den3 n s) (Phi (n ^ s) ^ 2) := by
  set N := n ^ s with hN_def
  have hN4 : N % 4 = 1 := pow_mod_four_eq_one hn4 s
  have hn5 : 5 ≤ n := by omega
  have hN_ge5 : 5 ≤ N := by
    calc 5 ≤ n := hn5
      _ = n ^ 1 := (pow_one n).symm
      _ ≤ n ^ s := Nat.pow_le_pow_right (by omega) hs
  have hn_dvd_N : n ∣ N := dvd_pow_self n (by omega)
  apply ratCongMod_of_telescoping
    (fun k _ => num3_ne_zero (by omega) k)
    (fun k _ => den3_ne_zero (by omega) k)
  · let jstar := (N - 5) / 4
    have hjstar_mem : jstar ∈ Finset.range ((N - 1) / 2) := by
      rw [Finset.mem_range]; omega
    have hjstar_exp : 5 + 4 * jstar = N := by omega
    have hden_erase : qPoch (X ^ 5) (X ^ 4) ((N - 1) / 2) =
        (1 - X ^ N) * ∏ j ∈ (Finset.range ((N - 1) / 2)).erase jstar, (1 - X ^ (5 + 4 * j)) := by
      rw [qPoch_X_pow_eq, ← Finset.mul_prod_erase (Finset.range ((N - 1) / 2))
        (fun j => (1 - X ^ (5 + 4 * j) : Polynomial ℚ)) hjstar_mem, hjstar_exp]
    have hden_erase_cop :
        IsCoprime (∏ j ∈ (Finset.range ((N - 1) / 2)).erase jstar, (1 - X ^ (5 + 4 * j)))
          (Phi N ^ 2) := by
      refine IsCoprime.prod_left fun j hj => ?_
      have hj_ne : j ≠ jstar := (Finset.mem_erase.mp hj).1
      have hj_lt : j < (N - 1) / 2 := Finset.mem_range.mp (Finset.mem_erase.mp hj).2
      refine isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => ?_)
      rcases hd with ⟨q, hq⟩
      have hq1 : q = 1 := by
        have : 5 + 4 * j < 2 * N := by omega
        have hq_pos : 1 ≤ q := by
          by_contra h0
          have hq0 : q = 0 := by omega
          subst hq0; rw [mul_zero] at hq; omega
        nlinarith
      rw [hq1, mul_one] at hq
      exact hj_ne (by omega)
    by_cases hs1 : s = 1
    · subst hs1
      have hN_eq : N = n := pow_one n
      have h0 : (n ^ (1 - 1) - 1) / 2 = 0 := by simp
      refine ⟨qPoch (X ^ 3) (X ^ 4) ((n - 1) / 2),
        (1 - X) * ∏ j ∈ (Finset.range ((n - 1) / 2)).erase jstar, (1 - X ^ (5 + 4 * j)),
        ?_, ?_⟩
      · refine IsCoprime.mul_left ?_ (by simpa [hN_eq] using hden_erase_cop)
        have h1 : (1 - X : Polynomial ℚ) = 1 - X ^ 1 := by simp
        rw [h1]
        exact isCoprime_one_sub_X_pow_Phi_sq le_rfl (fun hd => by
          have := Nat.le_of_dvd Nat.one_pos hd; omega)
      · unfold num3 den3
        have hq0 : ∀ a q : Polynomial ℚ, qPoch a q 0 = 1 := fun _ _ => by simp [qPoch]
        rw [pow_one, h0, hq0, hq0, mul_one, mul_one]
        have hde : qPoch (X ^ 5) (X ^ 4) ((n - 1) / 2) =
            (1 - X ^ n) * ∏ j ∈ (Finset.range ((n - 1) / 2)).erase jstar, (1 - X ^ (5 + 4 * j)) := by
          simpa [hN_eq] using hden_erase
        rw [hde, ← qNum_mul_one_sub_X n]
        ring
    · have hs2 : 2 ≤ s := by omega
      have hns : n * n ^ (s - 1) = N := by
        rw [hN_def, ← pow_succ', Nat.sub_add_cancel hs]
      have hprev4 : n ^ (s - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (s - 1)
      have hprev5 : 5 ≤ n ^ (s - 1) := by
        calc 5 ≤ n := hn5
          _ = n ^ 1 := (pow_one n).symm
          _ ≤ n ^ (s - 1) := Nat.pow_le_pow_right (by omega) (by omega)
      let istar := (n ^ (s - 1) - 5) / 4
      have histar_mem : istar ∈ Finset.range ((n ^ (s - 1) - 1) / 2) := by
        rw [Finset.mem_range]; omega
      have histar_exp : 5 * n + 4 * n * istar = N := by
        have : 5 + 4 * istar = n ^ (s - 1) := by omega
        nlinarith [hns]
      have hnum_erase : qPoch (X ^ (5 * n)) (X ^ (4 * n)) ((n ^ (s - 1) - 1) / 2) =
          (1 - X ^ N) *
            ∏ i ∈ (Finset.range ((n ^ (s - 1) - 1) / 2)).erase istar, (1 - X ^ (5 * n + 4 * n * i)) := by
        rw [qPoch_X_pow_eq, ← Finset.mul_prod_erase (Finset.range ((n ^ (s - 1) - 1) / 2))
          (fun i => (1 - X ^ (5 * n + 4 * n * i) : Polynomial ℚ)) histar_mem, histar_exp]
      refine ⟨qNum n * qPoch (X ^ 3) (X ^ 4) ((N - 1) / 2) *
          ∏ i ∈ (Finset.range ((n ^ (s - 1) - 1) / 2)).erase istar, (1 - X ^ (5 * n + 4 * n * i)),
        (∏ j ∈ (Finset.range ((N - 1) / 2)).erase jstar, (1 - X ^ (5 + 4 * j))) *
          qPoch (X ^ (3 * n)) (X ^ (4 * n)) ((n ^ (s - 1) - 1) / 2),
        ?_, ?_⟩
      · refine IsCoprime.mul_left hden_erase_cop ?_
        rw [qPoch_X_pow_eq]
        refine IsCoprime.prod_left fun i hi => ?_
        have hilt : i < (n ^ (s - 1) - 1) / 2 := Finset.mem_range.mp hi
        refine isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => ?_)
        have hlt2N : 3 * n + 4 * n * i < 2 * N := by
          have h2 : 3 + 4 * i < 2 * n ^ (s - 1) := by omega
          calc 3 * n + 4 * n * i = n * (3 + 4 * i) := by ring
            _ < n * (2 * n ^ (s - 1)) := Nat.mul_lt_mul_of_pos_left h2 (by omega)
            _ = 2 * N := by linarith [hns]
        rcases hd with ⟨q, hq⟩
        have hq1 : q = 1 := by
          have hq_pos : 1 ≤ q := by
            by_contra h0
            have hq0 : q = 0 := by omega
            subst hq0; rw [mul_zero] at hq; omega
          nlinarith
        rw [hq1, mul_one] at hq
        have hmod : (3 + 4 * i) = n ^ (s - 1) := by
          have : n * (3 + 4 * i) = n * n ^ (s - 1) := by nlinarith [hq, hns]
          exact Nat.eq_of_mul_eq_mul_left (by omega) this
        omega
      · unfold num3 den3
        rw [← hN_def, hnum_erase, hden_erase]
        ring
  · intro k hk
    set v0 := (n ^ k - 1) / 2
    set v1 := (n ^ (k + 1) - 1) / 2
    let U : Polynomial ℚ := ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 3)), (1 - X ^ (4 * i + 3))
    let V : Polynomial ℚ := ∏ i ∈ (Finset.Ico v0 v1).filter (fun i => ¬ n ∣ (4 * i + 5)), (1 - X ^ (4 * i + 5))
    refine ⟨U, V, ?_, guo63_cancel_step hn4 hn1 (by omega), ?_⟩
    · refine IsCoprime.prod_left fun i hi => ?_
      have hndvd_n : ¬ n ∣ (4 * i + 5) := (Finset.mem_filter.mp hi).2
      exact isCoprime_one_sub_X_pow_Phi_sq (by omega) (fun hd => hndvd_n (dvd_trans hn_dvd_N hd))
    · rw [← mk2_eq_iff]
      dsimp only [U, V, v0, v1]
      rw [guo63_blocks_U hn4 hn1 hs hk, guo63_blocks_V hn4 hn1 hs hk, map_prod, map_prod]
      let S := (Finset.Icc 1 (N - 1)).filter (fun a => ¬ n ∣ a)
      let K₀ := n ^ (k - s)
      refine Finset.prod_congr rfl fun t _ => ?_
      apply block_prod_congr_mod_Phi_sq S (fun a ha => by
        simp only [S, Finset.mem_filter, Finset.mem_Icc] at ha; omega) (4 * t + 2 * K₀) qNum3 qDen3
      intro w hw
      let Δ : ℕ → ℤ := fun a => (qNum3 a : ℤ) - (qDen3 a : ℤ)
      have hΔ_formula : ∀ a : ℕ, Δ a = if a % 4 ≤ 1 then -2 else 2 := by
        intro a; dsimp [Δ, qNum3, qDen3]; split_ifs <;> omega
      refine symmetric_pairing_vanishes (by omega) hn_dvd_N Δ ?_ ?_ w hw
      · intro a ha1 haN
        rw [hΔ_formula, hΔ_formula]; split_ifs <;> omega
      · have htot : ∑ a ∈ Finset.Icc 1 ((N - 1) / 2), Δ a = 0 := by
          rw [Finset.sum_congr rfl (fun a _ => hΔ_formula a),
            show (N - 1) / 2 = 2 * ((N - 1) / 4) by omega]
          exact sum_delta3_even_zero _
        have hmult : ∑ a ∈ (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => n ∣ a), Δ a = 0 := by
          have hns : n * n ^ (s - 1) = N := by
            rw [hN_def, ← pow_succ', Nat.sub_add_cancel hs]
          have hs4 : n ^ (s - 1) % 4 = 1 := pow_mod_four_eq_one hn4 (s - 1)
          have hbij : ∑ a ∈ (Finset.Icc 1 ((N - 1) / 2)).filter (fun a => n ∣ a), Δ a =
              ∑ m ∈ Finset.Icc 1 ((n ^ (s - 1) - 1) / 2), Δ m := by
            symm
            refine Finset.sum_bij (fun m _ => n * m) ?_ ?_ ?_ ?_
            · intro m hm
              simp only [Finset.mem_filter, Finset.mem_Icc] at hm ⊢
              refine ⟨⟨by nlinarith, ?_⟩, dvd_mul_right n m⟩
              have h1 : 2 * m < n ^ (s - 1) := by omega
              have h2 : 2 * (n * m) < N := by
                calc 2 * (n * m) = n * (2 * m) := by ring
                  _ < n * n ^ (s - 1) := Nat.mul_lt_mul_of_pos_left h1 (by omega)
                  _ = N := hns
              omega
            · intro m₁ _ m₂ _ hEq
              exact Nat.eq_of_mul_eq_mul_left (by omega) hEq
            · intro a ha
              simp only [Finset.mem_filter, Finset.mem_Icc] at ha
              rcases ha.2 with ⟨m, rfl⟩
              refine ⟨m, Finset.mem_Icc.mpr ⟨?_, ?_⟩, rfl⟩
              · by_contra h0
                have hm0 : m = 0 := by omega
                rw [hm0, mul_zero] at ha
                omega
              · have h1 : 2 * (n * m) < N := by omega
                have h2 : n * (2 * m) < n * n ^ (s - 1) := by rw [hns]; linarith
                have h3 := Nat.lt_of_mul_lt_mul_left h2
                omega
            · intro m _
              rw [hΔ_formula, hΔ_formula]
              have hmod : (n * m) % 4 = m % 4 := by rw [Nat.mul_mod, hn4]; omega
              rw [hmod]
          rw [hbij, Finset.sum_congr rfl (fun m _ => hΔ_formula m),
            show (n ^ (s - 1) - 1) / 2 = 2 * ((n ^ (s - 1) - 1) / 4) by omega]
          exact sum_delta3_even_zero _
        have hsplit := Finset.sum_filter_add_sum_filter_not (Finset.Icc 1 ((N - 1) / 2))
          (fun a => n ∣ a) Δ
        linarith
  · exact hrs.le

#print axioms guo_conjecture_6_4
#print axioms guo_conjecture_6_3

end OpenMath.Guo231015207Conj64
