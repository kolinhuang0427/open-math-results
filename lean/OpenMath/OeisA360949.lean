import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Data.Nat.Nth
import Mathlib.Tactic

/-!
# OEIS A360949: Paul D. Hanna's 2023 Mod-4 Thue–Morse Conjecture

Primary sources:
- OEIS **A360949** (author: Paul D. Hanna, Mar 03 2023; rev. 15, `2023-03-05`):
  - Name: *"G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n."*
  - Conjecture (Comment):
    *"Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4).
      A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the
      Thue-Morse sequence."*
- OEIS **A010060** (Thue–Morse sequence: `t(0) = 0`, `t(2n) = t(n)`, `t(2n+1) = 1 - t(n)`).
- OEIS **A161674** (offset `1`: increasing enumeration of `{m : ℕ | t(m) + t(m + 2) = 1}`).

This file formalizes the complete proof (zero `sorry`, zero `native_decide`, standard axioms only):
1. Exact coefficientwise formalization `SatisfiesA360949Eq` of Hanna's functional equation
   `1 = ∑_{n ≥ 0} (-X / 2)^n * (A^n + (-1)^n)^n` in `ℚ⟦X⟧` (with `coeff_hannaTerm_eq_zero_of_lt`
   proving all `n > k` terms contribute `0` to `[X^k]`).
2. Existence, uniqueness, and integrality (`existsUnique_a360949`, `coeff_ASeries`):
   there is a unique `A ∈ ℚ⟦X⟧` satisfying the equation, and its coefficients are integers
   `a : ℕ → ℤ` with `a 0 = 1` and `a k = 2 * b k` for `k ≥ 1`.
3. Mod-2 functional equation in `(ZMod 2)⟦X⟧` (`B2_functional_eq`, `B2_coeff_even`, `CSeries_quad_eq`):
   `(1 + X^2) * B2 = X + X^3 * B2^2`, forcing `b (2k) ≡ 0 (mod 2)` and
   `X^2 * C^2 + (1 + X) * C + 1 = 0` for `C(y) = ∑ b_{2m+1} y^m`.
4. Thue–Morse identification (`Ctilde_quad_eq`, `hanna_conjecture_A360949`,
   `hanna_conjecture_A360949_A161674`): `C` agrees with `∑ (t_m + t_{m+2}) y^m`, proving
   `a 0 = 1`, `a (2 * a161674 k + 1) ≡ 2 [ZMOD 4]` for `k ≥ 1`, and `a n ≡ 0 [ZMOD 4]` otherwise.
-/

namespace OpenMath.OeisA360949

open scoped BigOperators

/-! ## Section 0: Small PowerSeries and Finset Helpers -/

lemma coeff_X_mul_eq {R : Type*} [Semiring R] (k : ℕ) (F : PowerSeries R) :
    PowerSeries.coeff k (PowerSeries.X * F) =
      if 1 ≤ k then PowerSeries.coeff (k - 1) F else 0 := by
  rw [← pow_one (PowerSeries.X : PowerSeries R), PowerSeries.coeff_X_pow_mul']

lemma coeff_X_mul_succ {R : Type*} [Semiring R] (k : ℕ) (F : PowerSeries R) :
    PowerSeries.coeff (k + 1) (PowerSeries.X * F) = PowerSeries.coeff k F := by
  rw [coeff_X_mul_eq]
  simp

lemma sum_Icc_one_eq_sum_range {α : Type*} [AddCommMonoid α] (n : ℕ) (f : ℕ → α) :
    ∑ r ∈ Finset.Icc 1 n, f r = ∑ j ∈ Finset.range n, f (j + 1) := by
  symm
  refine Finset.sum_nbij (· + 1) ?_ ?_ ?_ ?_
  · intro j hj
    have hjn : j < n := Finset.mem_range.mp hj
    exact Finset.mem_Icc.mpr ⟨by omega, by omega⟩
  · intro a _ b _ h
    dsimp at h
    omega
  · intro r hr
    rcases Finset.mem_Icc.mp hr with ⟨h1, hn⟩
    exact ⟨r - 1, Finset.mem_range.mpr (by omega), by dsimp; omega⟩
  · intro _ _; rfl

lemma two_eq_C_two {R : Type*} [Semiring R] :
    (2 : PowerSeries R) = PowerSeries.C (2 : R) := by
  rw [map_ofNat]

/-! ## Section 1: Hanna's Functional Equation and the Integer Auxiliary Series -/

/-- The `n`-th summand `(-X / 2)^n * (A^n + (-1)^n)^n` in Hanna's functional equation over `ℚ⟦X⟧`. -/
noncomputable def hannaTerm (n : ℕ) (A : PowerSeries ℚ) : PowerSeries ℚ :=
  (PowerSeries.C (-1 / 2 : ℚ) * PowerSeries.X) ^ n * (A ^ n + (-1 : PowerSeries ℚ) ^ n) ^ n

lemma coeff_hannaTerm_eq_zero_of_lt {n k : ℕ} (hkn : k < n) (A : PowerSeries ℚ) :
    PowerSeries.coeff k (hannaTerm n A) = 0 := by
  unfold hannaTerm
  rw [mul_pow, ← map_pow PowerSeries.C, mul_assoc, PowerSeries.coeff_C_mul]
  have h0 : PowerSeries.coeff k (PowerSeries.X ^ n * (A ^ n + (-1 : PowerSeries ℚ) ^ n) ^ n) = 0 := by
    rw [PowerSeries.coeff_X_pow_mul']
    exact ite_eq_right (fun h => by omega)
  rw [h0, mul_zero]

/-- Exact coefficientwise statement of `1 = ∑_{n ≥ 0} (-X / 2)^n * (A^n + (-1)^n)^n` in `ℚ⟦X⟧`.
By `coeff_hannaTerm_eq_zero_of_lt`, truncating the sum at `n ≤ k` is exact. -/
def SatisfiesA360949Eq (A : PowerSeries ℚ) : Prop :=
  ∀ k : ℕ,
    (∑ n ∈ Finset.range (k + 1), PowerSeries.coeff k (hannaTerm n A)) =
      if k = 0 then 1 else 0

/-- Over any commutative ring `R`, the integer polynomial `R_n(B)` satisfying
`2 * R_n(B) = (1 + 2 * B)^n + (-1)^n` for `n ≥ 1`. -/
noncomputable def halfTerm {R : Type*} [CommRing R] (n : ℕ) (B : PowerSeries R) : PowerSeries R :=
  (if Even n then 1 else 0) +
    ∑ r ∈ Finset.Icc 1 n,
      PowerSeries.C ((Nat.choose n r * 2 ^ (r - 1) : ℕ) : R) * B ^ r

lemma two_mul_halfTerm {R : Type*} [CommRing R] (n : ℕ) (B : PowerSeries R) :
    (2 : PowerSeries R) * halfTerm n B =
      (1 + (2 : PowerSeries R) * B) ^ n + (-1 : PowerSeries R) ^ n := by
  have hexp : (1 + (2 : PowerSeries R) * B) ^ n =
      1 + ∑ r ∈ Finset.Icc 1 n,
        PowerSeries.C ((Nat.choose n r * 2 ^ r : ℕ) : R) * B ^ r := by
    rw [add_comm, add_pow, Finset.sum_range_succ' _ n]
    simp only [Nat.choose_zero_right, pow_zero, one_pow, mul_one, Nat.cast_one]
    rw [add_comm]
    congr 1
    rw [sum_Icc_one_eq_sum_range]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [mul_pow]
    have h2 : (2 : PowerSeries R) ^ (j + 1) = PowerSeries.C ((2 ^ (j + 1) : ℕ) : R) := by
      simp [two_eq_C_two, ← map_pow]
    have hc : (Nat.choose n (j + 1) : PowerSeries R) = PowerSeries.C (Nat.choose n (j + 1) : R) := by
      simp
    rw [h2, hc, Nat.cast_mul, map_mul]
    ring
  rw [hexp, halfTerm, mul_add, Finset.mul_sum]
  have hsum :
      ∑ r ∈ Finset.Icc 1 n,
        (2 : PowerSeries R) * (PowerSeries.C ((Nat.choose n r * 2 ^ (r - 1) : ℕ) : R) * B ^ r) =
      ∑ r ∈ Finset.Icc 1 n,
        PowerSeries.C ((Nat.choose n r * 2 ^ r : ℕ) : R) * B ^ r := by
    refine Finset.sum_congr rfl fun r hr => ?_
    have hr1 : 1 ≤ r := (Finset.mem_Icc.mp hr).1
    have hpow2 : 2 * 2 ^ (r - 1) = 2 ^ r := by
      cases r with
      | zero => omega
      | succ r' => simp [pow_succ']
    have hpow : 2 * (Nat.choose n r * 2 ^ (r - 1)) = Nat.choose n r * 2 ^ r := by
      rw [← hpow2]; ring
    have h2C : (2 : PowerSeries R) = PowerSeries.C ((2 : ℕ) : R) := by
      rw [Nat.cast_ofNat, two_eq_C_two]
    rw [h2C, ← mul_assoc, ← map_mul, ← Nat.cast_mul, hpow]
  rw [hsum]
  rcases Nat.even_or_odd n with hev | hodd
  · rw [ite_eq_left hev, hev.neg_one_pow]
    ring
  · have hnot : ¬ Even n := Nat.not_even_iff_odd.mpr hodd
    rw [ite_eq_right hnot, hodd.neg_one_pow]
    ring

lemma halfTerm_one {R : Type*} [CommRing R] (B : PowerSeries R) : halfTerm 1 B = B := by
  unfold halfTerm
  have hnot : ¬ Even (1 : ℕ) := by decide
  rw [ite_eq_right hnot, zero_add]
  simp

lemma map_halfTerm {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (n : ℕ) (B : PowerSeries R) :
    PowerSeries.map f (halfTerm n B) = halfTerm n (PowerSeries.map f B) := by
  unfold halfTerm
  rw [map_add, map_sum]
  congr 1
  · split_ifs <;> simp
  · refine Finset.sum_congr rfl fun r _ => ?_
    rw [map_mul, map_pow, PowerSeries.map_C, map_natCast]

lemma hannaTerm_eq_halfTerm (n : ℕ) (B : PowerSeries ℚ) :
    hannaTerm n (1 + (2 : PowerSeries ℚ) * B) =
      (-PowerSeries.X) ^ n * (halfTerm n B) ^ n := by
  unfold hannaTerm
  rw [← two_mul_halfTerm n B, mul_pow (2 : PowerSeries ℚ), ← mul_assoc, ← mul_pow]
  congr 1
  have h2 : (2 : PowerSeries ℚ) = PowerSeries.C (2 : ℚ) := two_eq_C_two
  have hbase : PowerSeries.C (-1 / 2 : ℚ) * PowerSeries.X * (2 : PowerSeries ℚ) =
      -PowerSeries.X := by
    rw [h2]
    calc
      PowerSeries.C (-1 / 2 : ℚ) * PowerSeries.X * PowerSeries.C (2 : ℚ)
          = (PowerSeries.C (-1 / 2 : ℚ) * PowerSeries.C (2 : ℚ)) * PowerSeries.X := by ring
      _ = PowerSeries.C ((-1 / 2 : ℚ) * 2) * PowerSeries.X := by rw [← map_mul]
      _ = -PowerSeries.X := by norm_num
  rw [hbase]

/-! ## Section 2: Coefficient Dependence Lemma (Truncation Invariance) -/

/-- If two power series agree on all coefficients `< d`, then their `m`-th powers agree on all
coefficients `< d`. -/
lemma coeff_pow_congr {R : Type*} [CommRing R] {F G : PowerSeries R} {d : ℕ}
    (h : ∀ j < d, PowerSeries.coeff j F = PowerSeries.coeff j G) :
    ∀ (m k : ℕ), k < d → PowerSeries.coeff k (F ^ m) = PowerSeries.coeff k (G ^ m) := by
  intro m
  induction m with
  | zero => intro k _; simp
  | succ m ih =>
    intro k hk
    rw [pow_succ, pow_succ, PowerSeries.coeff_mul, PowerSeries.coeff_mul]
    refine Finset.sum_congr rfl fun p hp => ?_
    have hp_sum : p.1 + p.2 = k := Finset.mem_antidiagonal.mp hp
    rw [ih p.1 (by omega), h p.2 (by omega)]

lemma coeff_halfTerm_congr {R : Type*} [CommRing R] {B B' : PowerSeries R} {d : ℕ}
    (h : ∀ j < d, PowerSeries.coeff j B = PowerSeries.coeff j B')
    (n k : ℕ) (hk : k < d) :
    PowerSeries.coeff k (halfTerm n B) = PowerSeries.coeff k (halfTerm n B') := by
  unfold halfTerm
  rw [map_add, map_add, map_sum, map_sum]
  congr 1
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [PowerSeries.coeff_C_mul, PowerSeries.coeff_C_mul, coeff_pow_congr h r k hk]

lemma coeff_halfTerm_pow_congr {R : Type*} [CommRing R] {B B' : PowerSeries R} (d : ℕ)
    (h : ∀ j < d, PowerSeries.coeff j B = PowerSeries.coeff j B')
    (n m k : ℕ) (hk : k < d) :
    PowerSeries.coeff k ((halfTerm n B) ^ m) = PowerSeries.coeff k ((halfTerm n B') ^ m) :=
  coeff_pow_congr (fun j hj => coeff_halfTerm_congr h n j hj) m k hk

/-! ## Section 3: Existence, Uniqueness, and Integrality of `A(x) = 1 + 2 B(x)` -/

/-- Recursive construction of the integer coefficients `b(k)` of `B(x) = (A(x) - 1)/2` (`b 0 = 0`). -/
noncomputable def bCoeff : ℕ → ℤ
  | 0 => 0
  | k + 1 =>
    let Bprev : PowerSeries ℤ := PowerSeries.mk fun j => if j < k + 1 then bCoeff j else 0
    ∑ n ∈ Finset.Icc 2 (k + 2),
      (-1 : ℤ) ^ n * PowerSeries.coeff (k + 2 - n) ((halfTerm n Bprev) ^ n)

/-- The integer formal power series `B(x) = ∑_{k ≥ 1} b(k) x^k ∈ x ℤ⟦X⟧`. -/
noncomputable def BInt : PowerSeries ℤ :=
  PowerSeries.mk bCoeff

lemma bCoeff_zero : bCoeff 0 = 0 := by rw [bCoeff]

lemma coeff_zero_BInt : PowerSeries.coeff 0 BInt = 0 := by
  simp [BInt, bCoeff_zero]

/-- Exact integer coefficient equation satisfied by `BInt` for all `k ≥ 1`. -/
lemma BInt_coeff_eq (k : ℕ) :
    ∑ n ∈ Finset.Icc 1 (k + 1),
      PowerSeries.coeff (k + 1) ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n) = 0 := by
  have hsplit : Finset.Icc 1 (k + 1) = insert 1 (Finset.Icc 2 (k + 1)) := by
    ext x; simp only [Finset.mem_Icc, Finset.mem_insert]; omega
  have h1not : (1 : ℕ) ∉ Finset.Icc 2 (k + 1) := by simp
  rw [hsplit, Finset.sum_insert h1not]
  have hterm1 :
      PowerSeries.coeff (k + 1) ((-PowerSeries.X : PowerSeries ℤ) ^ 1 * (halfTerm 1 BInt) ^ 1) =
        -bCoeff k := by
    rw [pow_one, pow_one, halfTerm_one, neg_mul, map_neg, coeff_X_mul_succ]
    simp [BInt]
  rw [hterm1]
  cases k with
  | zero =>
    simp [bCoeff_zero]
  | succ m =>
    have hterms :
        ∑ n ∈ Finset.Icc 2 (m + 2),
          PowerSeries.coeff (m + 2) ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n) =
        bCoeff (m + 1) := by
      conv_rhs => rw [bCoeff]
      refine Finset.sum_congr rfl fun n hn => ?_
      have hn_le : n ≤ m + 2 := (Finset.mem_Icc.mp hn).2
      have hn_ge : 2 ≤ n := (Finset.mem_Icc.mp hn).1
      have hneg : (-PowerSeries.X : PowerSeries ℤ) ^ n =
          PowerSeries.C ((-1 : ℤ) ^ n) * PowerSeries.X ^ n := by
        rw [neg_eq_neg_one_mul, mul_pow]
        have : (-1 : PowerSeries ℤ) ^ n = PowerSeries.C ((-1 : ℤ) ^ n) := by
          rw [← map_one PowerSeries.C, ← map_neg PowerSeries.C, ← map_pow PowerSeries.C]
        rw [this]
      rw [hneg, mul_assoc, PowerSeries.coeff_C_mul, PowerSeries.coeff_X_pow_mul']
      rw [ite_eq_left hn_le]
      congr 1
      refine coeff_halfTerm_pow_congr (m + 1) ?_ n n (m + 2 - n) (by omega)
      intro j hj
      simp only [BInt, PowerSeries.coeff_mk, ite_eq_left hj]
    rw [hterms, neg_add_cancel]

/-- The integer sequence `a(0) = 1`, `a(n) = 2 * b(n)` (`n ≥ 1`) for OEIS `A360949`. -/
noncomputable def a360949 : ℕ → ℤ
  | 0 => 1
  | k + 1 => 2 * bCoeff (k + 1)

/-- The generating function `A(x) = 1 + 2 B(x) ∈ ℚ⟦X⟧`. -/
noncomputable def ASeries : PowerSeries ℚ :=
  1 + (2 : PowerSeries ℚ) * PowerSeries.map (Int.castRingHom ℚ) BInt

lemma coeff_ASeries (k : ℕ) : PowerSeries.coeff k ASeries = (a360949 k : ℚ) := by
  have h2 : (2 : PowerSeries ℚ) = PowerSeries.C (2 : ℚ) := two_eq_C_two
  cases k with
  | zero =>
    rw [ASeries, a360949, map_add, h2, PowerSeries.coeff_C_mul, PowerSeries.coeff_map,
      coeff_zero_BInt, map_zero, mul_zero, add_zero]
    simp
  | succ m =>
    rw [ASeries, a360949, map_add, h2, PowerSeries.coeff_C_mul, PowerSeries.coeff_map,
      BInt, PowerSeries.coeff_mk]
    have h1 : PowerSeries.coeff (m + 1) (1 : PowerSeries ℚ) = 0 := by
      rw [PowerSeries.coeff_one]; exact ite_eq_right (by omega)
    rw [h1, zero_add]
    change (2 : ℚ) * (bCoeff (m + 1) : ℚ) = ((2 * bCoeff (m + 1) : ℤ) : ℚ)
    push_cast
    ring

/-- Existence: `ASeries` satisfies Hanna's functional equation `SatisfiesA360949Eq`. -/
theorem ASeries_satisfies : SatisfiesA360949Eq ASeries := by
  intro k
  cases k with
  | zero =>
    simp [hannaTerm]
  | succ m =>
    rw [ite_eq_right (by omega : m + 1 ≠ 0)]
    rw [Finset.sum_range_succ' _ (m + 1)]
    have h0 : PowerSeries.coeff (m + 1) (hannaTerm 0 ASeries) = 0 := by
      simp [hannaTerm, PowerSeries.coeff_one]
    rw [h0, add_zero]
    rw [← sum_Icc_one_eq_sum_range (m + 1)
      (fun n => PowerSeries.coeff (m + 1) (hannaTerm n ASeries))]
    have hmap :
        ∑ n ∈ Finset.Icc 1 (m + 1), PowerSeries.coeff (m + 1) (hannaTerm n ASeries) =
        ((∑ n ∈ Finset.Icc 1 (m + 1),
          PowerSeries.coeff (m + 1)
            ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n) : ℤ) : ℚ) := by
      push_cast
      refine Finset.sum_congr rfl fun n _ => ?_
      rw [ASeries, hannaTerm_eq_halfTerm n, ← map_halfTerm (Int.castRingHom ℚ)]
      have hterm_map :
          (-PowerSeries.X : PowerSeries ℚ) ^ n *
            (PowerSeries.map (Int.castRingHom ℚ) (halfTerm n BInt)) ^ n =
          PowerSeries.map (Int.castRingHom ℚ)
            ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n) := by
        simp [map_mul, map_pow, map_neg, PowerSeries.map_X]
      rw [hterm_map, PowerSeries.coeff_map]
      rfl
    rw [hmap, BInt_coeff_eq m, Int.cast_zero]

/-- Uniqueness: `ASeries` is the unique formal power series in `ℚ⟦X⟧` satisfying Hanna's equation. -/
theorem eq_ASeries_of_satisfies {A : PowerSeries ℚ} (hA : SatisfiesA360949Eq A) :
    A = ASeries := by
  have ha0 : PowerSeries.coeff 0 A = 1 := by
    have h1 := hA 1
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, zero_add,
      show (1 : ℕ) ≠ 0 by omega, ↓reduceIte] at h1
    have ht0 : PowerSeries.coeff 1 (hannaTerm 0 A) = 0 := by
      simp [hannaTerm, PowerSeries.coeff_one]
    have ht1 : PowerSeries.coeff 1 (hannaTerm 1 A) = (-1 / 2 : ℚ) * (PowerSeries.coeff 0 A - 1) := by
      unfold hannaTerm
      rw [pow_one, pow_one, pow_one, pow_one, mul_assoc, PowerSeries.coeff_C_mul,
        coeff_X_mul_succ 0, map_add, map_neg, PowerSeries.coeff_one]
      simp [sub_eq_add_neg]
    rw [ht0, zero_add, ht1] at h1
    linarith
  let B : PowerSeries ℚ := PowerSeries.C (1 / 2 : ℚ) * (A - 1)
  have hAB : A = 1 + (2 : PowerSeries ℚ) * B := by
    have h2 : (2 : PowerSeries ℚ) = PowerSeries.C (2 : ℚ) := two_eq_C_two
    dsimp only [B]
    rw [h2, ← mul_assoc, ← map_mul]
    have h12 : (2 : ℚ) * (1 / 2 : ℚ) = 1 := by norm_num
    rw [h12, map_one, one_mul]
    ring
  have hB0 : PowerSeries.coeff 0 B = 0 := by
    dsimp only [B]
    rw [PowerSeries.coeff_C_mul, map_sub, ha0, PowerSeries.coeff_one]
    simp
  have hB_eq : ∀ k : ℕ, PowerSeries.coeff k B = (bCoeff k : ℚ) := by
    intro k
    induction k using Nat.strong_induction_on with
    | ind k ih =>
      cases k with
      | zero => rw [hB0, bCoeff_zero, Int.cast_zero]
      | succ m =>
        have hkm := hA (m + 2)
        have hkmA := ASeries_satisfies (m + 2)
        have hdiff :
            ∑ n ∈ Finset.range (m + 3), PowerSeries.coeff (m + 2) (hannaTerm n A) =
            ∑ n ∈ Finset.range (m + 3), PowerSeries.coeff (m + 2) (hannaTerm n ASeries) :=
          hkm.trans hkmA.symm
        rw [Finset.sum_range_succ' _ (m + 2), Finset.sum_range_succ' _ (m + 2)] at hdiff
        have ht0A : PowerSeries.coeff (m + 2) (hannaTerm 0 A) = 0 := by
          simp [hannaTerm, PowerSeries.coeff_one]
        have ht0S : PowerSeries.coeff (m + 2) (hannaTerm 0 ASeries) = 0 := by
          simp [hannaTerm, PowerSeries.coeff_one]
        rw [ht0A, ht0S, add_zero, add_zero] at hdiff
        rw [Finset.sum_range_succ' _ (m + 1), Finset.sum_range_succ' _ (m + 1)] at hdiff
        have htail :
            ∑ n ∈ Finset.range (m + 1), PowerSeries.coeff (m + 2) (hannaTerm (n + 2) A) =
            ∑ n ∈ Finset.range (m + 1), PowerSeries.coeff (m + 2) (hannaTerm (n + 2) ASeries) := by
          refine Finset.sum_congr rfl fun n hn => ?_
          have hn_le : n + 2 ≤ m + 2 := by
            have := Finset.mem_range.mp hn; omega
          rw [hAB, ASeries, hannaTerm_eq_halfTerm (n + 2), hannaTerm_eq_halfTerm (n + 2)]
          have hneg : (-PowerSeries.X : PowerSeries ℚ) ^ (n + 2) =
              PowerSeries.C ((-1 : ℚ) ^ (n + 2)) * PowerSeries.X ^ (n + 2) := by
            rw [neg_eq_neg_one_mul, mul_pow]
            have : (-1 : PowerSeries ℚ) ^ (n + 2) = PowerSeries.C ((-1 : ℚ) ^ (n + 2)) := by
              rw [← map_one PowerSeries.C, ← map_neg PowerSeries.C, ← map_pow PowerSeries.C]
            rw [this]
          rw [hneg, mul_assoc, mul_assoc, PowerSeries.coeff_C_mul, PowerSeries.coeff_C_mul,
            PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_X_pow_mul',
            ite_eq_left hn_le, ite_eq_left hn_le]
          congr 1
          refine coeff_halfTerm_pow_congr (R := ℚ) (m + 1) ?_ (n + 2) (n + 2) (m + 2 - (n + 2)) (by omega)
          intro j hj
          rw [ih j (by omega), PowerSeries.coeff_map, BInt, PowerSeries.coeff_mk]
          rfl
        rw [htail] at hdiff
        have ht1 := add_left_cancel hdiff
        rw [hAB, ASeries, hannaTerm_eq_halfTerm 1, hannaTerm_eq_halfTerm 1] at ht1
        simp only [pow_one, halfTerm_one, neg_mul, map_neg, coeff_X_mul_succ] at ht1
        have hcoef : PowerSeries.coeff (m + 1) B =
            PowerSeries.coeff (m + 1) (PowerSeries.map (Int.castRingHom ℚ) BInt) := by
          linarith
        rw [hcoef, PowerSeries.coeff_map, BInt, PowerSeries.coeff_mk]
        rfl
  rw [hAB, ASeries]
  congr 2
  ext k
  rw [hB_eq k, PowerSeries.coeff_map, BInt, PowerSeries.coeff_mk]
  rfl

/-- Existence and uniqueness of the formal power series solution to Hanna's equation. -/
theorem existsUnique_a360949 : ∃! A : PowerSeries ℚ, SatisfiesA360949Eq A :=
  ⟨ASeries, ASeries_satisfies, fun _ h => eq_ASeries_of_satisfies h⟩

/-! ## Section 4: Reduction Modulo 2 in `(ZMod 2)⟦X⟧` -/

/-- Image of `BInt` in `(ZMod 2)⟦X⟧`. -/
noncomputable def B2 : PowerSeries (ZMod 2) :=
  PowerSeries.map (Int.castRingHom (ZMod 2)) BInt

lemma coeff_B2 (k : ℕ) : PowerSeries.coeff k B2 = (bCoeff k : ZMod 2) := by
  simp [B2, BInt]

lemma zmod2_add_self (a : ZMod 2) : a + a = 0 := by
  fin_cases a <;> rfl

lemma zmod2_neg_eq (a : ZMod 2) : -a = a := by
  fin_cases a <;> rfl

lemma zmod2_sq (a : ZMod 2) : a * a = a := by
  fin_cases a <;> rfl

lemma zmod2_series_add_self (F : PowerSeries (ZMod 2)) : F + F = 0 := by
  ext n; simp [zmod2_add_self]

lemma zmod2_series_neg_eq (F : PowerSeries (ZMod 2)) : -F = F := by
  ext n; rw [map_neg]; exact zmod2_neg_eq _

/-- Frobenius identity on coefficients in `(ZMod 2)⟦X⟧`: odd coefficients of `F ^ 2` vanish. -/
lemma coeff_sq_odd (F : PowerSeries (ZMod 2)) (k : ℕ) :
    PowerSeries.coeff (2 * k + 1) (F ^ 2) = 0 := by
  rw [sq, PowerSeries.coeff_mul]
  have hsum :
      ∑ p ∈ Finset.antidiagonal (2 * k + 1),
        PowerSeries.coeff p.1 F * PowerSeries.coeff p.2 F =
      ∑ p ∈ Finset.antidiagonal (2 * k + 1) with p.1 < p.2,
        (PowerSeries.coeff p.1 F * PowerSeries.coeff p.2 F +
         PowerSeries.coeff p.2 F * PowerSeries.coeff p.1 F) := by
    rw [← Finset.sum_filter_add_sum_filter_not (Finset.antidiagonal (2 * k + 1)) (fun p => p.1 < p.2)]
    rw [Finset.sum_add_distrib]
    congr 1
    refine Finset.sum_nbij Prod.swap ?_ ?_ ?_ ?_
    · rintro ⟨a, b⟩ hp
      simp only [Finset.mem_filter, Finset.mem_antidiagonal, not_lt, Prod.swap] at hp ⊢
      exact ⟨by omega, by omega⟩
    · intro p₁ _ p₂ _ h
      exact Prod.swap_injective h
    · rintro ⟨a, b⟩ hp
      simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_antidiagonal] at hp
      refine ⟨(b, a), ?_, rfl⟩
      simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_antidiagonal, not_lt]
      exact ⟨by omega, by omega⟩
    · rintro ⟨a, b⟩ _; rfl
  rw [hsum]
  refine Finset.sum_eq_zero fun p _ => ?_
  rw [mul_comm (PowerSeries.coeff p.2 F), zmod2_add_self]

/-- Frobenius identity on coefficients in `(ZMod 2)⟦X⟧`: `coeff (2k) (F^2) = coeff k F`. -/
lemma coeff_sq_even (F : PowerSeries (ZMod 2)) (k : ℕ) :
    PowerSeries.coeff (2 * k) (F ^ 2) = PowerSeries.coeff k F := by
  rw [sq, PowerSeries.coeff_mul]
  have hdiag : (k, k) ∈ Finset.antidiagonal (2 * k) := Finset.mem_antidiagonal.mpr (by omega)
  rw [← Finset.add_sum_erase _ _ hdiag, zmod2_sq]
  suffices hrest :
      ∑ p ∈ (Finset.antidiagonal (2 * k)).erase (k, k),
        PowerSeries.coeff p.1 F * PowerSeries.coeff p.2 F = 0 by
    rw [hrest, add_zero]
  let S := (Finset.antidiagonal (2 * k)).erase (k, k)
  have hsum :
      ∑ p ∈ S, PowerSeries.coeff p.1 F * PowerSeries.coeff p.2 F =
      ∑ p ∈ S with p.1 < p.2,
        (PowerSeries.coeff p.1 F * PowerSeries.coeff p.2 F +
         PowerSeries.coeff p.2 F * PowerSeries.coeff p.1 F) := by
    rw [← Finset.sum_filter_add_sum_filter_not S (fun p => p.1 < p.2), Finset.sum_add_distrib]
    congr 1
    refine Finset.sum_nbij Prod.swap ?_ ?_ ?_ ?_
    · rintro ⟨a, b⟩ hp
      simp only [S, Finset.mem_filter, Finset.mem_erase, Finset.mem_antidiagonal, not_lt,
        Prod.swap, ne_eq, Prod.mk.injEq] at hp ⊢
      exact ⟨⟨by omega, by omega⟩, by omega⟩
    · intro p₁ _ p₂ _ h; exact Prod.swap_injective h
    · rintro ⟨a, b⟩ hp
      simp only [S, Finset.mem_coe, Finset.mem_filter, Finset.mem_erase, Finset.mem_antidiagonal,
        ne_eq, Prod.mk.injEq] at hp
      refine ⟨(b, a), ?_, rfl⟩
      simp only [S, Finset.mem_coe, Finset.mem_filter, Finset.mem_erase, Finset.mem_antidiagonal,
        not_lt, ne_eq, Prod.mk.injEq]
      exact ⟨⟨by omega, by omega⟩, by omega⟩
    · rintro ⟨a, b⟩ _; rfl
  rw [hsum]
  refine Finset.sum_eq_zero fun p _ => ?_
  rw [mul_comm (PowerSeries.coeff p.2 F), zmod2_add_self]

/-- Simplification of `halfTerm n F` over `ZMod 2`: equals `1` if `n` is even, `F` if `n` is odd. -/
lemma halfTerm_zmod2 {n : ℕ} (hn : 1 ≤ n) (F : PowerSeries (ZMod 2)) :
    halfTerm n F = if Even n then 1 else F := by
  unfold halfTerm
  have h1mem : (1 : ℕ) ∈ Finset.Icc 1 n := Finset.mem_Icc.mpr ⟨le_rfl, hn⟩
  have hsum :
      ∑ r ∈ Finset.Icc 1 n,
        PowerSeries.C ((Nat.choose n r * 2 ^ (r - 1) : ℕ) : ZMod 2) * F ^ r =
      PowerSeries.C ((n : ℕ) : ZMod 2) * F := by
    rw [Finset.sum_eq_single 1]
    · simp
    · intro r hr hr1
      have hr2 : 2 ≤ r := by
        have := (Finset.mem_Icc.mp hr).1; omega
      have hev : 2 ∣ Nat.choose n r * 2 ^ (r - 1) := by
        have h2 : 2 ∣ 2 ^ (r - 1) := dvd_pow_self 2 (by omega)
        exact dvd_mul_of_dvd_right h2 _
      have hz : ((Nat.choose n r * 2 ^ (r - 1) : ℕ) : ZMod 2) = 0 :=
        (ZMod.natCast_eq_zero_iff _ 2).mpr hev
      rw [hz, map_zero, zero_mul]
    · intro h; exact absurd h1mem h
  rw [hsum]
  rcases Nat.even_or_odd n with hev | hodd
  · rw [ite_eq_left hev, ite_eq_left hev]
    have hz : ((n : ℕ) : ZMod 2) = 0 := (ZMod.natCast_eq_zero_iff n 2).mpr (even_iff_two_dvd.mp hev)
    rw [hz, map_zero, zero_mul, add_zero]
  · have hnot : ¬ Even n := Nat.not_even_iff_odd.mpr hodd
    rw [ite_eq_right hnot, ite_eq_right hnot, zero_add]
    have h1 : ((n : ℕ) : ZMod 2) = 1 := by
      rcases hodd with ⟨m, rfl⟩
      push_cast
      have h2 : (2 : ZMod 2) = 0 := rfl
      rw [h2, zero_mul, zero_add]
    rw [h1, map_one, one_mul]

/-- The even-part series `E2 = ∑_{m ≥ 1} X^(2m)` in `(ZMod 2)⟦X⟧`. -/
noncomputable def E2 : PowerSeries (ZMod 2) :=
  PowerSeries.mk fun k => if Even k ∧ 2 ≤ k then 1 else 0

/-- The odd-part series `O2 = ∑_{m ≥ 0} X^(2m+1) * B2^(2m+1)` in `(ZMod 2)⟦X⟧`. -/
noncomputable def O2 : PowerSeries (ZMod 2) :=
  PowerSeries.mk fun k =>
    ∑ n ∈ Finset.Icc 1 k,
      if Odd n then PowerSeries.coeff k (PowerSeries.X ^ n * B2 ^ n) else 0

lemma one_add_X_sq_mul_E2 :
    (1 + PowerSeries.X ^ 2) * E2 = PowerSeries.X ^ 2 := by
  ext k
  rw [add_mul, one_mul, map_add, PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_X_pow]
  dsimp only [E2]
  rw [PowerSeries.coeff_mk]
  by_cases hk2 : 2 ≤ k
  · rw [ite_eq_left hk2, PowerSeries.coeff_mk]
    by_cases heq : k = 2
    · subst heq; decide
    · rw [ite_eq_right heq]
      have hev_iff : Even (k - 2) ↔ Even k := by
        obtain ⟨r, rfl⟩ := Nat.exists_eq_add_of_le hk2
        simp [Nat.even_add]
      by_cases hev : Even k
      · have hge2 : 2 ≤ k - 2 := by
          rcases hev with ⟨t, ht⟩; omega
        have h1 : Even k ∧ 2 ≤ k := ⟨hev, hk2⟩
        have h2 : Even (k - 2) ∧ 2 ≤ k - 2 := ⟨hev_iff.mpr hev, hge2⟩
        rw [ite_eq_left h1, ite_eq_left h2]
        rfl
      · have h1 : ¬ (Even k ∧ 2 ≤ k) := fun h => hev h.1
        have h2 : ¬ (Even (k - 2) ∧ 2 ≤ k - 2) := fun h => hev (hev_iff.mp h.1)
        rw [ite_eq_right h1, ite_eq_right h2, add_zero]
  · rw [ite_eq_right hk2, add_zero]
    have h1 : ¬ (Even k ∧ 2 ≤ k) := fun h => hk2 h.2
    have h2 : k ≠ 2 := by omega
    rw [ite_eq_right h1, ite_eq_right h2]

lemma one_add_X_sq_B2_sq_mul_O2 :
    (1 + PowerSeries.X ^ 2 * B2 ^ 2) * O2 = PowerSeries.X * B2 := by
  ext k
  rw [add_mul, one_mul, map_add]
  have hterm :
      PowerSeries.coeff k (PowerSeries.X ^ 2 * B2 ^ 2 * O2) =
      ∑ n ∈ Finset.Icc 3 k,
        if Odd n then PowerSeries.coeff k (PowerSeries.X ^ n * B2 ^ n) else 0 := by
    rw [PowerSeries.coeff_mul, Finset.Nat.sum_antidiagonal_eq_sum_range_succ
      (fun a b => PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) * PowerSeries.coeff b O2)]
    simp only [O2, PowerSeries.coeff_mk, Finset.mul_sum]
    have hswap :
        ∑ a ∈ Finset.range (k + 1),
          ∑ n ∈ Finset.Icc 1 (k - a),
            PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
              (if Odd n then PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n) else 0) =
        ∑ n ∈ Finset.Icc 1 k,
          if Odd n then
            ∑ a ∈ Finset.range (k + 1),
              PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
                PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n)
          else 0 := by
      have hpad : ∀ a ∈ Finset.range (k + 1),
          ∑ n ∈ Finset.Icc 1 (k - a),
            PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
              (if Odd n then PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n) else 0) =
          ∑ n ∈ Finset.Icc 1 k,
            PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
              (if Odd n then PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n) else 0) := by
        intro a ha
        have hak : a ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp ha)
        refine Finset.sum_subset (Finset.Icc_subset_Icc_right (by omega)) ?_
        intro n hn hnnot
        have hgt : k - a < n := by
          simp only [Finset.mem_Icc] at hn hnnot; omega
        split_ifs with hodd
        · have hz : PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n) = 0 := by
            rw [PowerSeries.coeff_X_pow_mul']; exact ite_eq_right (by omega)
          rw [hz, mul_zero]
        · rw [mul_zero]
      rw [Finset.sum_congr rfl hpad, Finset.sum_comm]
      refine Finset.sum_congr rfl fun n _ => ?_
      split_ifs with hodd
      · rfl
      · simp
    rw [hswap]
    have hconv : ∀ n ∈ Finset.Icc 1 k,
        (∑ a ∈ Finset.range (k + 1),
          PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
            PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n)) =
        PowerSeries.coeff k (PowerSeries.X ^ (n + 2) * B2 ^ (n + 2)) := by
      intro n _
      rw [← Finset.Nat.sum_antidiagonal_eq_sum_range_succ
        (fun a b => PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
          PowerSeries.coeff b (PowerSeries.X ^ n * B2 ^ n)),
        ← PowerSeries.coeff_mul]
      congr 1
      ring
    have hrew :
        ∑ n ∈ Finset.Icc 1 k,
          (if Odd n then
            ∑ a ∈ Finset.range (k + 1),
              PowerSeries.coeff a (PowerSeries.X ^ 2 * B2 ^ 2) *
                PowerSeries.coeff (k - a) (PowerSeries.X ^ n * B2 ^ n)
          else 0) =
        ∑ n ∈ Finset.Icc 1 k,
          if Odd n then PowerSeries.coeff k (PowerSeries.X ^ (n + 2) * B2 ^ (n + 2)) else 0 := by
      refine Finset.sum_congr rfl fun n hn => ?_
      split_ifs with hodd
      · exact hconv n hn
      · rfl
    rw [hrew]
    have hsplit :
        ∑ n ∈ Finset.Icc 1 k,
          (if Odd n then PowerSeries.coeff k (PowerSeries.X ^ (n + 2) * B2 ^ (n + 2)) else 0) =
        ∑ m ∈ Finset.Icc 3 (k + 2),
          if Odd m then PowerSeries.coeff k (PowerSeries.X ^ m * B2 ^ m) else 0 := by
      refine Finset.sum_nbij (· + 2) ?_ ?_ ?_ ?_
      · intro n hn; simp only [Finset.mem_Icc] at hn ⊢; omega
      · intro a _ b _ h; dsimp at h; omega
      · intro m hm
        simp only [Finset.mem_coe, Finset.mem_Icc] at hm
        exact ⟨m - 2, Finset.mem_coe.mpr (Finset.mem_Icc.mpr ⟨by omega, by omega⟩), by dsimp; omega⟩
      · intro n _
        have hodd_iff : Odd (n + 2) ↔ Odd n := by
          constructor
          · rintro ⟨t, ht⟩; exact ⟨t - 1, by omega⟩
          · rintro ⟨t, ht⟩; exact ⟨t + 1, by omega⟩
        exact (if_congr hodd_iff rfl rfl).symm
    rw [hsplit]
    symm
    refine Finset.sum_subset (Finset.Icc_subset_Icc_right (by omega)) ?_
    intro m hm hmnot
    have hgt : k < m := by simp only [Finset.mem_Icc] at hm hmnot; omega
    split_ifs with hodd
    · rw [PowerSeries.coeff_X_pow_mul']; exact ite_eq_right (by omega)
    · rfl
  rw [hterm]
  dsimp only [O2]
  rw [PowerSeries.coeff_mk]
  cases k with
  | zero =>
    simp
  | succ m =>
    have hIcc : Finset.Icc 1 (m + 1) = insert 1 (Finset.Icc 2 (m + 1)) := by
      ext x; simp only [Finset.mem_Icc, Finset.mem_insert]; omega
    have h1not : (1 : ℕ) ∉ Finset.Icc 2 (m + 1) := by simp
    rw [hIcc, Finset.sum_insert h1not]
    have hodd1 : Odd (1 : ℕ) := odd_one
    rw [ite_eq_left hodd1, pow_one, pow_one]
    have hIcc2 :
        ∑ n ∈ Finset.Icc 2 (m + 1),
          (if Odd n then PowerSeries.coeff (m + 1) (PowerSeries.X ^ n * B2 ^ n) else 0) =
        ∑ n ∈ Finset.Icc 3 (m + 1),
          (if Odd n then PowerSeries.coeff (m + 1) (PowerSeries.X ^ n * B2 ^ n) else 0) := by
      by_cases hm1 : 2 ≤ m + 1
      · have hsplit2 : Finset.Icc 2 (m + 1) = insert 2 (Finset.Icc 3 (m + 1)) := by
          ext x; simp only [Finset.mem_Icc, Finset.mem_insert]; omega
        rw [hsplit2, Finset.sum_insert (by simp)]
        have hnot2 : ¬ Odd (2 : ℕ) := by decide
        rw [ite_eq_right hnot2, zero_add]
      · have h1 : Finset.Icc 2 (m + 1) = ∅ := Finset.Icc_eq_empty (by omega)
        have h2 : Finset.Icc 3 (m + 1) = ∅ := Finset.Icc_eq_empty (by omega)
        rw [h1, h2]
    rw [hIcc2, add_assoc, zmod2_add_self, add_zero]

lemma E2_add_O2_eq_zero : E2 + O2 = 0 := by
  ext k
  rw [map_add, map_zero]
  cases k with
  | zero =>
    simp [E2, O2]
  | succ m =>
    have hZ := congrArg (Int.castRingHom (ZMod 2)) (BInt_coeff_eq m)
    rw [map_zero, map_sum] at hZ
    have hrewrite :
        (∑ n ∈ Finset.Icc 1 (m + 1),
          (Int.castRingHom (ZMod 2))
            (PowerSeries.coeff (m + 1)
              ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n))) =
        PowerSeries.coeff (m + 1) E2 + PowerSeries.coeff (m + 1) O2 := by
      have hterm : ∀ n ∈ Finset.Icc 1 (m + 1),
          (Int.castRingHom (ZMod 2))
            (PowerSeries.coeff (m + 1)
              ((-PowerSeries.X : PowerSeries ℤ) ^ n * (halfTerm n BInt) ^ n)) =
          (if Even n then PowerSeries.coeff (m + 1) (PowerSeries.X ^ n) else 0) +
          (if Odd n then PowerSeries.coeff (m + 1) (PowerSeries.X ^ n * B2 ^ n) else 0) := by
        intro n hn
        have hn1 : 1 ≤ n := (Finset.mem_Icc.mp hn).1
        rw [← PowerSeries.coeff_map, map_mul, map_pow, map_pow, map_neg, PowerSeries.map_X,
          zmod2_series_neg_eq, map_halfTerm, halfTerm_zmod2 hn1]
        rcases Nat.even_or_odd n with hev | hodd
        · have hnot : ¬ Odd n := Nat.not_odd_iff_even.mpr hev
          rw [ite_eq_left hev, ite_eq_left hev, ite_eq_right hnot, one_pow, mul_one, add_zero]
        · have hnot : ¬ Even n := Nat.not_even_iff_odd.mpr hodd
          rw [ite_eq_right hnot, ite_eq_right hnot, ite_eq_left hodd, zero_add]
          rfl
      rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib]
      congr 1
      · dsimp only [E2]
        rw [PowerSeries.coeff_mk]
        simp_rw [PowerSeries.coeff_X_pow]
        by_cases hm : Even (m + 1) ∧ 2 ≤ m + 1
        · rw [ite_eq_left hm, Finset.sum_eq_single (m + 1)]
          · simp [hm.1]
          · intro n _ hne
            by_cases hev : Even n
            · rw [ite_eq_left hev, ite_eq_right (Ne.symm hne)]
            · rw [ite_eq_right hev]
          · intro h
            exact absurd (Finset.mem_Icc.mpr ⟨by omega, le_rfl⟩) h
        · rw [ite_eq_right hm]
          refine Finset.sum_eq_zero fun n hn => ?_
          by_cases hev : Even n
          · rw [ite_eq_left hev]
            by_cases heq : m + 1 = n
            · have h2 : 2 ≤ n := by
                have h1 : 1 ≤ n := (Finset.mem_Icc.mp hn).1
                rcases hev with ⟨t, ht⟩; omega
              exact (hm ⟨heq ▸ hev, heq ▸ h2⟩).elim
            · exact ite_eq_right heq
          · exact ite_eq_right hev
      · simp [O2]
    rw [← hrewrite]
    exact hZ

/-- Key Step-2 functional equation in `(ZMod 2)⟦X⟧`: `(1 + X^2) * B2 = X + X^3 * B2^2`. -/
theorem B2_functional_eq :
    (1 + PowerSeries.X ^ 2) * B2 = PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2 := by
  have hprod :
      ((1 + PowerSeries.X ^ 2) * (1 + PowerSeries.X ^ 2 * B2 ^ 2)) * (E2 + O2) = 0 := by
    rw [E2_add_O2_eq_zero, mul_zero]
  have hexpand :
      ((1 + PowerSeries.X ^ 2) * (1 + PowerSeries.X ^ 2 * B2 ^ 2)) * (E2 + O2) =
      PowerSeries.X * ((1 + PowerSeries.X ^ 2) * B2 + (PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2)) := by
    calc
      ((1 + PowerSeries.X ^ 2) * (1 + PowerSeries.X ^ 2 * B2 ^ 2)) * (E2 + O2)
          = (1 + PowerSeries.X ^ 2 * B2 ^ 2) * ((1 + PowerSeries.X ^ 2) * E2) +
            (1 + PowerSeries.X ^ 2) * ((1 + PowerSeries.X ^ 2 * B2 ^ 2) * O2) := by ring
      _ = (1 + PowerSeries.X ^ 2 * B2 ^ 2) * PowerSeries.X ^ 2 +
          (1 + PowerSeries.X ^ 2) * (PowerSeries.X * B2) := by
            rw [one_add_X_sq_mul_E2, one_add_X_sq_B2_sq_mul_O2]
      _ = PowerSeries.X * ((1 + PowerSeries.X ^ 2) * B2 +
          (PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2)) := by ring
  rw [hexpand] at hprod
  have h0 : (1 + PowerSeries.X ^ 2) * B2 + (PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2) = 0 := by
    apply PowerSeries.X_pow_mul_cancel (k := 1)
    simpa using hprod
  calc
    (1 + PowerSeries.X ^ 2) * B2
        = ((1 + PowerSeries.X ^ 2) * B2 + (PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2)) +
          (PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2) := by
            rw [add_assoc, zmod2_series_add_self, add_zero]
    _ = PowerSeries.X + PowerSeries.X ^ 3 * B2 ^ 2 := by rw [h0, zero_add]

/-- Every even coefficient of `B2` vanishes (`b(2k) ≡ 0 [MOD 2]`). -/
theorem B2_coeff_even (k : ℕ) : PowerSeries.coeff (2 * k) B2 = 0 := by
  induction k with
  | zero =>
    rw [mul_zero, coeff_B2, bCoeff_zero, Int.cast_zero]
  | succ m ih =>
    have h := congrArg (PowerSeries.coeff (2 * (m + 1))) B2_functional_eq
    rw [add_mul, one_mul, map_add, map_add, PowerSeries.coeff_X_pow_mul',
      PowerSeries.coeff_X_pow_mul'] at h
    have hX : PowerSeries.coeff (2 * (m + 1)) (PowerSeries.X : PowerSeries (ZMod 2)) = 0 := by
      rw [PowerSeries.coeff_X]; exact ite_eq_right (by omega)
    rw [hX, zero_add, ite_eq_left (by omega : 2 ≤ 2 * (m + 1))] at h
    have hsub2 : 2 * (m + 1) - 2 = 2 * m := by omega
    rw [hsub2, ih, add_zero] at h
    by_cases hm3 : 3 ≤ 2 * (m + 1)
    · rw [ite_eq_left hm3] at h
      have hodd : 2 * (m + 1) - 3 = 2 * (m - 1) + 1 := by omega
      rw [hodd, coeff_sq_odd] at h
      exact h
    · rw [ite_eq_right hm3] at h
      exact h

/-- Odd-indexed slice `C(y) = ∑_{m ≥ 0} b(2m + 1) y^m ∈ (ZMod 2)⟦X⟧`. -/
noncomputable def CSeries : PowerSeries (ZMod 2) :=
  PowerSeries.mk fun m => PowerSeries.coeff (2 * m + 1) B2

/-- `CSeries` satisfies `X^2 * C^2 + (1 + X) * C + 1 = 0` in `(ZMod 2)⟦X⟧`. -/
theorem CSeries_quad_eq :
    PowerSeries.X ^ 2 * CSeries ^ 2 + (1 + PowerSeries.X) * CSeries + 1 = 0 := by
  ext m
  rw [map_add, map_add, map_zero, add_mul, one_mul, map_add, coeff_X_mul_eq,
    PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_one]
  have h := congrArg (PowerSeries.coeff (2 * m + 1)) B2_functional_eq
  rw [add_mul, one_mul, map_add, map_add, PowerSeries.coeff_X_pow_mul',
    PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_X] at h
  have hXeq : (if 2 * m + 1 = 1 then (1 : ZMod 2) else 0) = (if m = 0 then 1 else 0) := by
    by_cases hm0 : m = 0
    · subst hm0; simp
    · rw [ite_eq_right (by omega), ite_eq_right hm0]
  rw [hXeq] at h
  have hC1 : PowerSeries.coeff m CSeries = PowerSeries.coeff (2 * m + 1) B2 := by
    simp [CSeries]
  have hC2 :
      (if 1 ≤ m then PowerSeries.coeff (m - 1) CSeries else 0) =
      (if 2 ≤ 2 * m + 1 then PowerSeries.coeff (2 * m + 1 - 2) B2 else 0) := by
    by_cases hm1 : 1 ≤ m
    · rw [ite_eq_left hm1, ite_eq_left (by omega : 2 ≤ 2 * m + 1)]
      simp only [CSeries, PowerSeries.coeff_mk]
      have hidx : 2 * (m - 1) + 1 = 2 * m + 1 - 2 := by omega
      rw [hidx]
    · rw [ite_eq_right hm1, ite_eq_right (by omega : ¬ 2 ≤ 2 * m + 1)]
  have hC3 :
      (if 2 ≤ m then PowerSeries.coeff (m - 2) (CSeries ^ 2) else 0) =
      (if 3 ≤ 2 * m + 1 then PowerSeries.coeff (2 * m + 1 - 3) (B2 ^ 2) else 0) := by
    by_cases hm2 : 2 ≤ m
    · rw [ite_eq_left hm2, ite_eq_left (by omega : 3 ≤ 2 * m + 1)]
      have hev : 2 * m + 1 - 3 = 2 * (m - 1) := by omega
      rw [hev, coeff_sq_even]
      rcases Nat.even_or_odd (m - 2) with ⟨j, hj⟩ | ⟨j, hj⟩
      · have h2j : m - 2 = 2 * j := by omega
        have hidx : m - 1 = 2 * j + 1 := by omega
        rw [h2j, coeff_sq_even, hidx]
        simp [CSeries]
      · have hidx : m - 1 = 2 * (j + 1) := by omega
        rw [hj, coeff_sq_odd, hidx, B2_coeff_even]
    · rw [ite_eq_right hm2]
      by_cases hm1 : m = 1
      · subst hm1
        rw [ite_eq_left (by omega : 3 ≤ 2 * 1 + 1)]
        have h0 : 2 * 1 + 1 - 3 = 2 * 0 := rfl
        have hb0 : PowerSeries.coeff 0 B2 = 0 := by simpa using B2_coeff_even 0
        rw [h0, coeff_sq_even, hb0]
      · rw [ite_eq_right (by omega : ¬ 3 ≤ 2 * m + 1)]
  rw [hC1, hC2, hC3, h]
  set x := if 3 ≤ 2 * m + 1 then PowerSeries.coeff (2 * m + 1 - 3) (B2 ^ 2) else 0
  set y := if m = 0 then (1 : ZMod 2) else 0
  calc
    x + (y + x) + y = (x + x) + (y + y) := by ring
    _ = 0 + 0 := by rw [zmod2_add_self, zmod2_add_self]
    _ = 0 := by simp

/-- Uniqueness of the solution to `X^2 * Y^2 + (1 + X) * Y + 1 = 0` in `(ZMod 2)⟦X⟧`. -/
lemma unique_quad_sol {Y₁ Y₂ : PowerSeries (ZMod 2)}
    (h1 : PowerSeries.X ^ 2 * Y₁ ^ 2 + (1 + PowerSeries.X) * Y₁ + 1 = 0)
    (h2 : PowerSeries.X ^ 2 * Y₂ ^ 2 + (1 + PowerSeries.X) * Y₂ + 1 = 0) :
    Y₁ = Y₂ := by
  ext m
  induction m using Nat.strong_induction_on with
  | ind m ih =>
    have hc1 := congrArg (PowerSeries.coeff m) h1
    have hc2 := congrArg (PowerSeries.coeff m) h2
    have hstep : ∀ Y : PowerSeries (ZMod 2),
        PowerSeries.coeff m (PowerSeries.X ^ 2 * Y ^ 2 + (1 + PowerSeries.X) * Y + 1) = 0 →
        PowerSeries.coeff m Y =
          (if 2 ≤ m then PowerSeries.coeff (m - 2) (Y ^ 2) else 0) +
          (if 1 ≤ m then PowerSeries.coeff (m - 1) Y else 0) +
          (if m = 0 then 1 else 0) := by
      intro Y hY
      rw [map_add, map_add, add_mul, one_mul, map_add, PowerSeries.coeff_X_pow_mul',
        coeff_X_mul_eq, PowerSeries.coeff_one] at hY
      set a := if 2 ≤ m then PowerSeries.coeff (m - 2) (Y ^ 2) else 0
      set b := if 1 ≤ m then PowerSeries.coeff (m - 1) Y else 0
      set c := if m = 0 then (1 : ZMod 2) else 0
      set y := PowerSeries.coeff m Y
      calc
        y = (a + (y + b) + c) + (a + b + c) := by
              have : (a + (y + b) + c) + (a + b + c) = y + (a + a) + (b + b) + (c + c) := by ring
              rw [this, zmod2_add_self, zmod2_add_self, zmod2_add_self]; ring
        _ = a + b + c := by rw [hY, zero_add]
    rw [hstep Y₁ hc1, hstep Y₂ hc2]
    congr 1
    congr 1
    · by_cases hm2 : 2 ≤ m
      · rw [ite_eq_left hm2, ite_eq_left hm2]
        rcases Nat.even_or_odd (m - 2) with ⟨j, hj⟩ | ⟨j, hj⟩
        · have h2j : m - 2 = 2 * j := by omega
          rw [h2j, coeff_sq_even, coeff_sq_even, ih j (by omega)]
        · rw [hj, coeff_sq_odd, coeff_sq_odd]
      · rw [ite_eq_right hm2, ite_eq_right hm2]
    · by_cases hm1 : 1 ≤ m
      · rw [ite_eq_left hm1, ite_eq_left hm1, ih (m - 1) (by omega)]
      · rw [ite_eq_right hm1, ite_eq_right hm1]

/-! ## Section 5: Thue–Morse Sequence (`A010060`) and `A161674` Identification -/

/-- OEIS `A010060` (Thue–Morse sequence): `t(0) = 0`, `t(2n) = t(n)`, `t(2n + 1) = 1 - t(n)`. -/
def thueMorse : ℕ → ℕ
  | 0 => 0
  | n + 1 =>
    if (n + 1) % 2 = 0 then thueMorse ((n + 1) / 2) else 1 - thueMorse ((n + 1) / 2)

@[simp] lemma thueMorse_zero : thueMorse 0 = 0 := by rw [thueMorse]

lemma thueMorse_even (n : ℕ) : thueMorse (2 * n) = thueMorse n := by
  cases n with
  | zero => simp
  | succ m =>
    have h : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
    conv_lhs => rw [h, thueMorse]
    rw [ite_eq_left (by omega : (2 * m + 1 + 1) % 2 = 0)]
    congr 1; omega

lemma thueMorse_odd (n : ℕ) : thueMorse (2 * n + 1) = 1 - thueMorse n := by
  conv_lhs => rw [thueMorse]
  rw [ite_eq_right (by omega : ¬ (2 * n + 1) % 2 = 0)]
  congr 2; omega

lemma thueMorse_le_one (n : ℕ) : thueMorse n ≤ 1 := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    cases n with
    | zero => simp
    | succ m =>
      rw [thueMorse]
      split_ifs
      · exact ih ((m + 1) / 2) (by omega)
      · omega

lemma thueMorse_one : thueMorse 1 = 1 := by
  simpa [thueMorse_zero] using thueMorse_odd 0

lemma thueMorse_cast_odd (n : ℕ) :
    (thueMorse (2 * n + 1) : ZMod 2) = 1 + (thueMorse n : ZMod 2) := by
  rw [thueMorse_odd]
  have hle := thueMorse_le_one n
  have hcases : thueMorse n = 0 ∨ thueMorse n = 1 := by omega
  rcases hcases with h | h
  · simp [h]
  · simp [h]; rfl

/-- Thue–Morse generating function `T(y) = ∑_{m ≥ 0} t_m y^m ∈ (ZMod 2)⟦X⟧`. -/
noncomputable def TSeries : PowerSeries (ZMod 2) :=
  PowerSeries.mk fun m => (thueMorse m : ZMod 2)

/-- Indicator series of `A161674`: `C̃(y) = ∑_{m ≥ 0} (t_m + t_{m+2}) y^m ∈ (ZMod 2)⟦X⟧`. -/
noncomputable def Ctilde : PowerSeries (ZMod 2) :=
  PowerSeries.mk fun m => (thueMorse m : ZMod 2) + (thueMorse (m + 2) : ZMod 2)

lemma one_add_X_sq_eq :
    (1 + PowerSeries.X : PowerSeries (ZMod 2)) ^ 2 = 1 + PowerSeries.X ^ 2 := by
  calc
    (1 + PowerSeries.X : PowerSeries (ZMod 2)) ^ 2
        = 1 + (PowerSeries.X + PowerSeries.X) + PowerSeries.X ^ 2 := by ring
    _ = 1 + 0 + PowerSeries.X ^ 2 := by rw [zmod2_series_add_self]
    _ = 1 + PowerSeries.X ^ 2 := by ring

lemma one_add_X_cube_eq :
    (1 + PowerSeries.X : PowerSeries (ZMod 2)) ^ 3 =
      1 + PowerSeries.X + PowerSeries.X ^ 2 + PowerSeries.X ^ 3 := by
  rw [pow_succ, one_add_X_sq_eq]; ring

/-- Step 3 identity 1: `(1 + X)^3 * T^2 + (1 + X)^2 * T + X = 0` in `(ZMod 2)⟦X⟧`. -/
lemma TSeries_eq :
    (1 + PowerSeries.X) ^ 3 * TSeries ^ 2 + (1 + PowerSeries.X) ^ 2 * TSeries +
      PowerSeries.X = 0 := by
  rw [one_add_X_cube_eq, one_add_X_sq_eq]
  ext k
  have hexp :
      (1 + PowerSeries.X + PowerSeries.X ^ 2 + PowerSeries.X ^ 3) * TSeries ^ 2 +
        (1 + PowerSeries.X ^ 2) * TSeries + PowerSeries.X =
      TSeries ^ 2 + PowerSeries.X * TSeries ^ 2 + PowerSeries.X ^ 2 * TSeries ^ 2 +
        PowerSeries.X ^ 3 * TSeries ^ 2 + TSeries + PowerSeries.X ^ 2 * TSeries +
        PowerSeries.X := by ring
  rw [hexp]
  simp only [map_add, map_zero, coeff_X_mul_eq, PowerSeries.coeff_X_pow_mul',
    PowerSeries.coeff_X]
  rcases Nat.even_or_odd k with ⟨m, hm⟩ | ⟨m, hm⟩
  · have hk : k = 2 * m := by omega
    subst hk
    rw [coeff_sq_even]
    have hX0 : (if 2 * m = 1 then (1 : ZMod 2) else 0) = 0 := ite_eq_right (by omega)
    rw [hX0, add_zero]
    have hTm : PowerSeries.coeff (2 * m) TSeries = PowerSeries.coeff m TSeries := by
      simp [TSeries, thueMorse_even]
    have h1 : (if 1 ≤ 2 * m then PowerSeries.coeff (2 * m - 1) (TSeries ^ 2) else 0) = 0 := by
      split_ifs with h
      · have : 2 * m - 1 = 2 * (m - 1) + 1 := by omega
        rw [this, coeff_sq_odd]
      · rfl
    have h3 : (if 3 ≤ 2 * m then PowerSeries.coeff (2 * m - 3) (TSeries ^ 2) else 0) = 0 := by
      split_ifs with h
      · have : 2 * m - 3 = 2 * (m - 2) + 1 := by omega
        rw [this, coeff_sq_odd]
      · rfl
    have h2 :
        (if 2 ≤ 2 * m then PowerSeries.coeff (2 * m - 2) (TSeries ^ 2) else 0) =
        (if 2 ≤ 2 * m then PowerSeries.coeff (2 * m - 2) TSeries else 0) := by
      split_ifs with h
      · have : 2 * m - 2 = 2 * (m - 1) := by omega
        rw [this, coeff_sq_even]
        simp [TSeries, thueMorse_even]
      · rfl
    rw [h1, h3, h2, hTm]
    set a := PowerSeries.coeff m TSeries
    set b := if 2 ≤ 2 * m then PowerSeries.coeff (2 * m - 2) TSeries else 0
    calc
      a + 0 + b + 0 + a + b = (a + a) + (b + b) := by ring
      _ = 0 := by rw [zmod2_add_self, zmod2_add_self, add_zero]
  · subst hm
    rw [coeff_sq_odd, zero_add]
    have h1 : (if 1 ≤ 2 * m + 1 then PowerSeries.coeff (2 * m + 1 - 1) (TSeries ^ 2) else 0) =
        PowerSeries.coeff m TSeries := by
      rw [ite_eq_left (by omega : 1 ≤ 2 * m + 1)]
      have : 2 * m + 1 - 1 = 2 * m := by omega
      rw [this, coeff_sq_even]
    have h2 : (if 2 ≤ 2 * m + 1 then PowerSeries.coeff (2 * m + 1 - 2) (TSeries ^ 2) else 0) = 0 := by
      split_ifs with h
      · have : 2 * m + 1 - 2 = 2 * (m - 1) + 1 := by omega
        rw [this, coeff_sq_odd]
      · rfl
    have hTm : PowerSeries.coeff (2 * m + 1) TSeries = 1 + PowerSeries.coeff m TSeries := by
      simp [TSeries, thueMorse_cast_odd]
    rw [h1, h2, add_zero, hTm]
    cases m with
    | zero =>
      simp only [mul_zero, zero_add, show ¬ (3 ≤ 1) by omega, show ¬ (2 ≤ 1) by omega,
        ↓reduceIte, add_zero]
      set a := PowerSeries.coeff 0 TSeries
      calc
        a + (1 + a) + 1 = (a + a) + (1 + 1) := by ring
        _ = 0 := by rw [zmod2_add_self, zmod2_add_self, add_zero]
    | succ r =>
      rw [ite_eq_left (by omega : 3 ≤ 2 * (r + 1) + 1),
        ite_eq_left (by omega : 2 ≤ 2 * (r + 1) + 1),
        ite_eq_right (by omega : 2 * (r + 1) + 1 ≠ 1), add_zero]
      have h3 : 2 * (r + 1) + 1 - 3 = 2 * r := by omega
      have h2' : 2 * (r + 1) + 1 - 2 = 2 * r + 1 := by omega
      rw [h3, coeff_sq_even, h2']
      have hTr : PowerSeries.coeff (2 * r + 1) TSeries = 1 + PowerSeries.coeff r TSeries := by
        simp [TSeries, thueMorse_cast_odd]
      rw [hTr]
      set a := PowerSeries.coeff (r + 1) TSeries
      set b := PowerSeries.coeff r TSeries
      calc
        a + b + (1 + a) + (1 + b) = (a + a) + (b + b) + (1 + 1) := by ring
        _ = 0 := by rw [zmod2_add_self a, zmod2_add_self b, zmod2_add_self 1]; simp

/-- Step 3 identity 2: `(1 + X)^2 * T = X + X^2 * Ctilde` in `(ZMod 2)⟦X⟧`. -/
lemma TSeries_Ctilde_rel :
    (1 + PowerSeries.X) ^ 2 * TSeries = PowerSeries.X + PowerSeries.X ^ 2 * Ctilde := by
  rw [one_add_X_sq_eq, add_mul, one_mul]
  ext k
  rw [map_add, map_add, PowerSeries.coeff_X_pow_mul', PowerSeries.coeff_X_pow_mul',
    PowerSeries.coeff_X]
  match k with
  | 0 =>
    simp [TSeries, thueMorse_zero]
  | 1 =>
    simp [TSeries, thueMorse_one]
  | m + 2 =>
    rw [ite_eq_left (by omega : 2 ≤ m + 2), ite_eq_left (by omega : 2 ≤ m + 2),
      ite_eq_right (by omega : m + 2 ≠ 1), zero_add]
    simp only [TSeries, Ctilde, PowerSeries.coeff_mk, Nat.add_sub_cancel]
    ring

/-- Step 3 identity 3: `Ctilde` satisfies the same quadratic equation as `CSeries`. -/
lemma Ctilde_quad_eq :
    PowerSeries.X ^ 2 * Ctilde ^ 2 + (1 + PowerSeries.X) * Ctilde + 1 = 0 := by
  have hsq : (1 + PowerSeries.X) ^ 4 * TSeries ^ 2 =
      PowerSeries.X ^ 2 + PowerSeries.X ^ 4 * Ctilde ^ 2 := by
    have h2 : ((1 + PowerSeries.X) ^ 2 * TSeries) ^ 2 =
        (PowerSeries.X + PowerSeries.X ^ 2 * Ctilde) ^ 2 :=
      congrArg (· ^ 2) TSeries_Ctilde_rel
    have hL : ((1 + PowerSeries.X) ^ 2 * TSeries) ^ 2 =
        (1 + PowerSeries.X) ^ 4 * TSeries ^ 2 := by ring
    have hR : (PowerSeries.X + PowerSeries.X ^ 2 * Ctilde) ^ 2 =
        PowerSeries.X ^ 2 + PowerSeries.X ^ 4 * Ctilde ^ 2 := by
      calc
        (PowerSeries.X + PowerSeries.X ^ 2 * Ctilde) ^ 2
            = PowerSeries.X ^ 2 +
              (PowerSeries.X * (PowerSeries.X ^ 2 * Ctilde) +
               PowerSeries.X * (PowerSeries.X ^ 2 * Ctilde)) +
              PowerSeries.X ^ 4 * Ctilde ^ 2 := by ring
        _ = PowerSeries.X ^ 2 + PowerSeries.X ^ 4 * Ctilde ^ 2 := by
              rw [zmod2_series_add_self]; ring
    rw [hL, hR] at h2
    exact h2
  have hmul : (1 + PowerSeries.X) *
      ((1 + PowerSeries.X) ^ 3 * TSeries ^ 2 + (1 + PowerSeries.X) ^ 2 * TSeries +
        PowerSeries.X) = 0 := by
    rw [TSeries_eq, mul_zero]
  have hsub :
      PowerSeries.X ^ 2 * (PowerSeries.X ^ 2 * Ctilde ^ 2 + (1 + PowerSeries.X) * Ctilde + 1) = 0 := by
    have h1 :
        (1 + PowerSeries.X) *
          ((1 + PowerSeries.X) ^ 3 * TSeries ^ 2 + (1 + PowerSeries.X) ^ 2 * TSeries +
            PowerSeries.X) =
        (1 + PowerSeries.X) ^ 4 * TSeries ^ 2 +
          (1 + PowerSeries.X) * ((1 + PowerSeries.X) ^ 2 * TSeries) +
          (1 + PowerSeries.X) * PowerSeries.X := by ring
    rw [h1, hsq, TSeries_Ctilde_rel] at hmul
    have h2 :
        PowerSeries.X ^ 2 + PowerSeries.X ^ 4 * Ctilde ^ 2 +
          (1 + PowerSeries.X) * (PowerSeries.X + PowerSeries.X ^ 2 * Ctilde) +
          (1 + PowerSeries.X) * PowerSeries.X =
        PowerSeries.X ^ 2 * (PowerSeries.X ^ 2 * Ctilde ^ 2 + (1 + PowerSeries.X) * Ctilde + 1) +
          ((1 + PowerSeries.X) * PowerSeries.X + (1 + PowerSeries.X) * PowerSeries.X) := by ring
    rw [h2, zmod2_series_add_self, add_zero] at hmul
    exact hmul
  exact PowerSeries.X_pow_mul_cancel (by simpa using hsub)

theorem CSeries_eq_Ctilde : CSeries = Ctilde :=
  unique_quad_sol CSeries_quad_eq Ctilde_quad_eq

/-! ## Section 6: Main Theorems (Mod-4 Characterization and OEIS `A161674`) -/

/-- Exact mod-2 characterization of `bCoeff (2m + 1)`. -/
lemma bCoeff_odd_zmod2 (m : ℕ) :
    (bCoeff (2 * m + 1) : ZMod 2) = (thueMorse m : ZMod 2) + (thueMorse (m + 2) : ZMod 2) := by
  have h := congrArg (PowerSeries.coeff m) CSeries_eq_Ctilde
  simpa [CSeries, Ctilde, coeff_B2] using h

/-- Predicate defining the set of elements of OEIS `A161674`: `t(m) + t(m + 2) = 1`. -/
def IsA161674 (m : ℕ) : Prop :=
  thueMorse m + thueMorse (m + 2) = 1

instance : DecidablePred IsA161674 :=
  fun m => inferInstanceAs (Decidable (thueMorse m + thueMorse (m + 2) = 1))

lemma isA161674_iff_zmod2 (m : ℕ) :
    IsA161674 m ↔ (thueMorse m : ZMod 2) + (thueMorse (m + 2) : ZMod 2) = 1 := by
  have h1 : thueMorse m = 0 ∨ thueMorse m = 1 := by have := thueMorse_le_one m; omega
  have h2 : thueMorse (m + 2) = 0 ∨ thueMorse (m + 2) = 1 := by
    have := thueMorse_le_one (m + 2); omega
  unfold IsA161674
  rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
  · simp [h1, h2]
  · simp [h1, h2]
  · simp [h1, h2]
  · simp [h1, h2]

/-- `A161674` is infinite (for every `k : ℕ`, `4 * k ∈ A161674`). -/
lemma setOf_isA161674_infinite : Set.Infinite {m : ℕ | IsA161674 m} := by
  refine Set.infinite_of_injective_forall_mem (f := fun k => 4 * k)
    (fun a b h => by dsimp at h; omega) fun k => ?_
  show thueMorse (4 * k) + thueMorse (4 * k + 2) = 1
  have h4k : 4 * k = 2 * (2 * k) := by ring
  have h4k2 : 4 * k + 2 = 2 * (2 * k + 1) := by ring
  rw [h4k2, h4k, thueMorse_even, thueMorse_even, thueMorse_even, thueMorse_odd]
  have := thueMorse_le_one k
  omega

/-- OEIS `A161674` (offset `1`): the `k`-th smallest `m : ℕ` with `t(m) + t(m + 2) = 1` (`k ≥ 1`). -/
noncomputable def a161674 (k : ℕ) : ℕ :=
  Nat.nth IsA161674 (k - 1)

lemma mem_range_a161674_iff (m : ℕ) :
    (∃ k : ℕ, 1 ≤ k ∧ a161674 k = m) ↔ IsA161674 m := by
  constructor
  · rintro ⟨k, _, rfl⟩
    exact Nat.nth_mem_of_infinite setOf_isA161674_infinite (k - 1)
  · intro hm
    refine ⟨Nat.count IsA161674 m + 1, by omega, ?_⟩
    simp only [a161674, Nat.add_sub_cancel]
    exact Nat.nth_count hm

/-- **Main Theorem (Direct Form — Paul D. Hanna's 2023 Conjecture on OEIS `A360949`):**
For the unique formal power series `A(x) = ∑ a(n) x^n ∈ ℚ⟦X⟧` satisfying
`1 = ∑_{n ≥ 0} (-x / 2)^n * (A(x)^n + (-1)^n)^n`:
- `a(0) = 1`,
- for every `n ≥ 1`, if `n = 2m + 1` with `t(m) + t(m + 2) = 1` then `a(n) ≡ 2 [ZMOD 4]`,
- otherwise `a(n) ≡ 0 [ZMOD 4]`. -/
theorem hanna_conjecture_A360949 :
    a360949 0 = 1 ∧
    (∀ n : ℕ, 1 ≤ n →
      ((∃ m : ℕ, n = 2 * m + 1 ∧ IsA161674 m) → a360949 n ≡ 2 [ZMOD 4]) ∧
      (¬ (∃ m : ℕ, n = 2 * m + 1 ∧ IsA161674 m) → a360949 n ≡ 0 [ZMOD 4])) := by
  refine ⟨rfl, fun n hn => ?_⟩
  cases n with
  | zero => omega
  | succ r =>
  constructor
  · rintro ⟨m, heq, hA⟩
    rw [a360949]
    have hz : (bCoeff (r + 1) : ZMod 2) = 1 := by
      rw [heq, bCoeff_odd_zmod2, (isA161674_iff_zmod2 m).mp hA]
    have hsub : ((bCoeff (r + 1) - 1 : ℤ) : ZMod 2) = 0 := by
      push_cast; rw [hz, sub_self]
    have hdvd : (2 : ℤ) ∣ bCoeff (r + 1) - 1 :=
      (ZMod.intCast_zmod_eq_zero_iff_dvd _ 2).mp hsub
    rcases hdvd with ⟨q, hq⟩
    rw [Int.ModEq]
    omega
  · intro hnot
    rw [a360949]
    have hz : (bCoeff (r + 1) : ZMod 2) = 0 := by
      rcases Nat.even_or_odd (r + 1) with ⟨m, hm⟩ | ⟨m, hm⟩
      · have h2m : r + 1 = 2 * m := by omega
        rw [h2m, ← coeff_B2, B2_coeff_even]
      · have hnotA : ¬ IsA161674 m := fun hA => hnot ⟨m, hm, hA⟩
        have hne1 : (thueMorse m : ZMod 2) + (thueMorse (m + 2) : ZMod 2) ≠ 1 := by
          intro h; exact hnotA ((isA161674_iff_zmod2 m).mpr h)
        rw [hm, bCoeff_odd_zmod2]
        generalize (thueMorse m : ZMod 2) + (thueMorse (m + 2) : ZMod 2) = x at hne1 ⊢
        fin_cases x
        · rfl
        · exact (hne1 rfl).elim
    have hdvd : (2 : ℤ) ∣ bCoeff (r + 1) := (ZMod.intCast_zmod_eq_zero_iff_dvd _ 2).mp hz
    rcases hdvd with ⟨q, hq⟩
    rw [Int.ModEq, hq]
    omega

/-- **Main Theorem (OEIS `A161674` Index Form):**
Verbatim statement from OEIS `A360949`: `a(0) = 1`, `a(2 * A161674(k) + 1) ≡ 2 (mod 4)` for all
`k ≥ 1`, and `a(n) ≡ 0 (mod 4)` for all other `n ≥ 1`. -/
theorem hanna_conjecture_A360949_A161674 :
    a360949 0 = 1 ∧
    (∀ k : ℕ, 1 ≤ k → a360949 (2 * a161674 k + 1) ≡ 2 [ZMOD 4]) ∧
    (∀ n : ℕ, 1 ≤ n → (∀ k : ℕ, 1 ≤ k → n ≠ 2 * a161674 k + 1) →
      a360949 n ≡ 0 [ZMOD 4]) := by
  refine ⟨rfl, ?_, ?_⟩
  · intro k hk
    refine (hanna_conjecture_A360949.2 (2 * a161674 k + 1) (by omega)).1 ?_
    exact ⟨a161674 k, rfl, (mem_range_a161674_iff (a161674 k)).mp ⟨k, hk, rfl⟩⟩
  · intro n hn hnot
    refine (hanna_conjecture_A360949.2 n hn).2 ?_
    rintro ⟨m, rfl, hm⟩
    obtain ⟨k, hk, rfl⟩ := (mem_range_a161674_iff m).mpr hm
    exact hnot k hk rfl

#print axioms existsUnique_a360949
#print axioms coeff_ASeries
#print axioms hanna_conjecture_A360949
#print axioms hanna_conjecture_A360949_A161674

end OpenMath.OeisA360949
