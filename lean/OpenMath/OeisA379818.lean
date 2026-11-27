import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# OEIS A379818: Mikhail Kurkov's Binomial Formula Conjecture

This file formalizes the complete proof of Mikhail Kurkov's conjecture on
OEIS A379818 (rev. 2026-02-26):

Let `a(n)` (`A379818`) be defined by `a(0) = 1`,
- `a(2n + 1) = a(n)` for `n ≥ 0`,
- `a(2n) = a(n) + a(n - 2^f(n)) + a(2n - 2^f(n)) + a(A025480(n - 1))` for `n > 0`,
where `f(n) = A007814(n) = v_2(n)` is the 2-adic valuation of `n` and
`A025480(2n) = n`, `A025480(2n + 1) = A025480(n)`.

Then for all `m ≥ 0` and `k ≥ 0`,
`a(2^m * (2k + 1)) = ∑_{j=0}^{m} (binomial(m + 2, j + 1) - binomial(m, j)) * a(2^j * k)`.
-/

namespace OpenMath.OeisA379818

/-- OEIS `A007814`: 2-adic valuation `v_2(n)` (with `a007814 0 = 0`). -/
def a007814 : ℕ → ℕ
  | 0 => 0
  | n + 1 => if (n + 1) % 2 = 0 then a007814 ((n + 1) / 2) + 1 else 0

lemma a007814_odd (k : ℕ) : a007814 (2 * k + 1) = 0 := by
  rw [a007814]
  simp

lemma a007814_two_mul {n : ℕ} (hn : 0 < n) : a007814 (2 * n) = a007814 n + 1 := by
  cases n with
  | zero => omega
  | succ m =>
    have h : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
    conv_lhs => rw [h, a007814]
    have heven : (2 * m + 1 + 1) % 2 = 0 := by omega
    have hdiv : (2 * m + 1 + 1) / 2 = m + 1 := by omega
    rw [if_pos heven, hdiv]

lemma a007814_pow_two_mul_odd (r k : ℕ) : a007814 (2 ^ r * (2 * k + 1)) = r := by
  induction r with
  | zero =>
    simpa using a007814_odd k
  | succ r ih =>
    have hpos : 0 < 2 ^ r * (2 * k + 1) := by positivity
    have heq : 2 ^ (r + 1) * (2 * k + 1) = 2 * (2 ^ r * (2 * k + 1)) := by ring
    rw [heq, a007814_two_mul hpos, ih]

/-- Fidelity check: `a007814 n` agrees with Mathlib's `n.factorization 2` for all `n : ℕ`. -/
theorem a007814_eq_factorization (n : ℕ) : a007814 n = n.factorization 2 := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    cases n with
    | zero => simp [a007814]
    | succ m =>
      by_cases heven : (m + 1) % 2 = 0
      · set q := (m + 1) / 2
        have hq_pos : 0 < q := by omega
        have hm_eq : m + 1 = 2 * q := by omega
        rw [hm_eq, a007814_two_mul hq_pos, ih q (by omega)]
        rw [Nat.factorization_mul (by norm_num) hq_pos.ne', Finsupp.add_apply,
          Nat.Prime.factorization_self Nat.prime_two]
        omega
      · have hodd : ¬ (2 ∣ m + 1) := by omega
        have ha : a007814 (m + 1) = 0 := by
          rw [a007814]
          simp [heven]
        rw [ha]
        exact (Nat.factorization_eq_zero_of_not_dvd hodd).symm

/-- OEIS `A025480`: `a(2n) = n`, `a(2n + 1) = a(n)` for `n ≥ 0`. -/
def a025480 : ℕ → ℕ
  | 0 => 0
  | n + 1 => if (n + 1) % 2 = 0 then (n + 1) / 2 else a025480 ((n + 1) / 2)

lemma a025480_even (n : ℕ) : a025480 (2 * n) = n := by
  cases n with
  | zero => simp [a025480]
  | succ m =>
    have h : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
    conv_lhs => rw [h, a025480]
    have heven : (2 * m + 1 + 1) % 2 = 0 := by omega
    have hdiv : (2 * m + 1 + 1) / 2 = m + 1 := by omega
    rw [if_pos heven, hdiv]

lemma a025480_odd (n : ℕ) : a025480 (2 * n + 1) = a025480 n := by
  conv_lhs => rw [a025480]
  have hodd : ¬ ((2 * n + 1) % 2 = 0) := by omega
  have hdiv : (2 * n + 1) / 2 = n := by omega
  rw [if_neg hodd, hdiv]

lemma a025480_le (n : ℕ) : a025480 n ≤ n := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    cases n with
    | zero => simp [a025480]
    | succ m =>
      rw [a025480]
      split_ifs with heven
      · omega
      · exact (ih ((m + 1) / 2) (by omega)).trans (by omega)

/-- Shift identity for `A025480`: `A025480(2^r * (2k + 1) - 1) = k`. -/
lemma a025480_pow_two_mul_odd_sub_one (r k : ℕ) :
    a025480 (2 ^ r * (2 * k + 1) - 1) = k := by
  induction r with
  | zero =>
    have h : 2 ^ 0 * (2 * k + 1) - 1 = 2 * k := by omega
    rw [h, a025480_even]
  | succ r ih =>
    have hpos : 1 ≤ 2 ^ r * (2 * k + 1) := by
      have : 1 ≤ 2 ^ r := Nat.one_le_two_pow
      nlinarith
    have hmul : 2 ^ (r + 1) * (2 * k + 1) = 2 * (2 ^ r * (2 * k + 1)) := by ring
    have h : 2 ^ (r + 1) * (2 * k + 1) - 1 = 2 * (2 ^ r * (2 * k + 1) - 1) + 1 := by omega
    rw [h, a025480_odd, ih]

/-- OEIS `A379818`:
`a(0) = 1`, `a(2n + 1) = a(n)`, and
`a(2n) = a(n) + a(n - 2^f(n)) + a(2n - 2^f(n)) + a(A025480(n - 1))` for `n > 0`. -/
def a379818 : ℕ → ℕ
  | 0 => 1
  | m + 1 =>
    if (m + 1) % 2 = 1 then
      a379818 ((m + 1) / 2)
    else
      let n := (m + 1) / 2
      a379818 n + a379818 (n - 2 ^ a007814 n) +
        a379818 (2 * n - 2 ^ a007814 n) + a379818 (a025480 (n - 1))
termination_by m => m
decreasing_by
  all_goals
    have hpow_pos : 0 < 2 ^ a007814 ((m + 1) / 2) := Nat.two_pow_pos _
    have ha_le : a025480 ((m + 1) / 2 - 1) ≤ (m + 1) / 2 - 1 := a025480_le _
    omega

lemma a379818_zero : a379818 0 = 1 := by rw [a379818]

lemma a379818_odd (n : ℕ) : a379818 (2 * n + 1) = a379818 n := by
  conv_lhs => rw [a379818]
  have hodd : (2 * n + 1) % 2 = 1 := by omega
  have hdiv : (2 * n + 1) / 2 = n := by omega
  rw [if_pos hodd, hdiv]

lemma a379818_even {n : ℕ} (hn : 0 < n) :
    a379818 (2 * n) =
      a379818 n + a379818 (n - 2 ^ a007814 n) +
        a379818 (2 * n - 2 ^ a007814 n) + a379818 (a025480 (n - 1)) := by
  cases n with
  | zero => omega
  | succ m =>
    have h : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
    conv_lhs => rw [h, a379818]
    have heven : ¬ ((2 * m + 1 + 1) % 2 = 1) := by omega
    have hdiv : (2 * m + 1 + 1) / 2 = m + 1 := by omega
    rw [if_neg heven]
    dsimp only
    rw [hdiv]

/-- Binomial inequality `C(m, j) ≤ C(m + 2, j + 1)` ensuring exact (non-truncating)
subtraction in `ℕ`. -/
lemma choose_le_choose_add_two (m j : ℕ) :
    Nat.choose m j ≤ Nat.choose (m + 2) (j + 1) := by
  have h1 : Nat.choose m j ≤ Nat.choose (m + 1) (j + 1) := by
    cases j with
    | zero => simp
    | succ i =>
      rw [Nat.choose_succ_succ]
      exact Nat.le_add_right _ _
  have h2 : Nat.choose (m + 1) (j + 1) ≤ Nat.choose (m + 2) (j + 1) := by
    rw [Nat.choose_succ_succ (m + 1) j]
    exact Nat.le_add_left _ _
  exact h1.trans h2

/-- Coefficient `c(m, j) = binomial(m + 2, j + 1) - binomial(m, j)`. -/
def coeff (m j : ℕ) : ℕ :=
  Nat.choose (m + 2) (j + 1) - Nat.choose m j

lemma coeff_zero (m : ℕ) : coeff m 0 = m + 1 := by
  unfold coeff
  rw [Nat.choose_one_right, Nat.choose_zero_right]
  omega

lemma coeff_self (m : ℕ) : coeff m m = m + 1 := by
  unfold coeff
  have h1 : Nat.choose (m + 2) (m + 1) = m + 2 := by
    rw [← Nat.choose_symm (by omega : m + 1 ≤ m + 2)]
    have hsub : m + 2 - (m + 1) = 1 := by omega
    rw [hsub, Nat.choose_one_right]
  rw [h1, Nat.choose_self]
  omega

lemma coeff_pascal (m j : ℕ) :
    coeff (m + 1) (j + 1) = coeff m (j + 1) + coeff m j := by
  unfold coeff
  have h1 : Nat.choose m (j + 1) ≤ Nat.choose (m + 2) (j + 2) := choose_le_choose_add_two m (j + 1)
  have h2 : Nat.choose m j ≤ Nat.choose (m + 2) (j + 1) := choose_le_choose_add_two m j
  have hp1 : Nat.choose (m + 3) (j + 2) =
      Nat.choose (m + 2) (j + 1) + Nat.choose (m + 2) (j + 2) :=
    Nat.choose_succ_succ (m + 2) (j + 1)
  have hp2 : Nat.choose (m + 1) (j + 1) =
      Nat.choose m j + Nat.choose m (j + 1) :=
    Nat.choose_succ_succ m j
  have hm3 : m + 1 + 2 = m + 3 := by omega
  have hj2 : j + 1 + 1 = j + 2 := by omega
  rw [hm3, hj2, hp1, hp2]
  omega

/-- Main Theorem (Mikhail Kurkov's Conjecture on OEIS `A379818`):
For all `m ≥ 0` and `k ≥ 0`,
`a(2^m * (2k + 1)) = ∑_{j=0}^{m} (binomial(m + 2, j + 1) - binomial(m, j)) * a(2^j * k)`. -/
theorem kurkov_conjecture_A379818 (m k : ℕ) :
    a379818 (2 ^ m * (2 * k + 1)) =
      ∑ j ∈ Finset.range (m + 1),
        (Nat.choose (m + 2) (j + 1) - Nat.choose m j) * a379818 (2 ^ j * k) := by
  change a379818 (2 ^ m * (2 * k + 1)) =
    ∑ j ∈ Finset.range (m + 1), coeff m j * a379818 (2 ^ j * k)
  induction m generalizing k with
  | zero =>
    simp [coeff_zero, a379818_odd]
  | succ m ih =>
    set n := 2 ^ m * (2 * k + 1)
    have hn_pos : 0 < n := by positivity
    have h2n : 2 * n = 2 ^ (m + 1) * (2 * k + 1) := by dsimp [n]; ring
    have hf : a007814 n = m := a007814_pow_two_mul_odd m k
    have hsub1 : n - 2 ^ m = 2 ^ (m + 1) * k := by
      dsimp [n]
      have : 2 ^ m * (2 * k + 1) = 2 ^ (m + 1) * k + 2 ^ m := by ring
      omega
    have hsub2 : 2 * n - 2 ^ m = 2 ^ m * (2 * (2 * k) + 1) := by
      dsimp [n]
      have : 2 * (2 ^ m * (2 * k + 1)) = 2 ^ m * (2 * (2 * k) + 1) + 2 ^ m := by ring
      omega
    have hb : a025480 (n - 1) = k := a025480_pow_two_mul_odd_sub_one m k
    rw [← h2n, a379818_even hn_pos, hf, hsub1, hsub2, hb]
    rw [ih k, ih (2 * k)]
    have hshift :
        ∑ i ∈ Finset.range (m + 1), coeff m i * a379818 (2 ^ i * (2 * k)) =
          ∑ i ∈ Finset.range (m + 1), coeff m i * a379818 (2 ^ (i + 1) * k) := by
      refine Finset.sum_congr rfl fun i _ => ?_
      have : 2 ^ i * (2 * k) = 2 ^ (i + 1) * k := by ring
      rw [this]
    rw [hshift]
    set F : ℕ → ℕ := fun j => a379818 (2 ^ j * k)
    have hF0 : a379818 k = F 0 := by simp [F]
    have hFm1 : a379818 (2 ^ (m + 1) * k) = F (m + 1) := rfl
    rw [hF0, hFm1]
    have hleft :
        (∑ j ∈ Finset.range (m + 1), coeff m j * F j) + F (m + 1) =
          ∑ j ∈ Finset.range (m + 2), (if j ≤ m then coeff m j else 1) * F j := by
      symm
      rw [Finset.sum_range_succ]
      have h1 :
          ∑ j ∈ Finset.range (m + 1), (if j ≤ m then coeff m j else 1) * F j =
            ∑ j ∈ Finset.range (m + 1), coeff m j * F j := by
        refine Finset.sum_congr rfl fun j hj => ?_
        have hjm : j ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
        simp [hjm]
      rw [h1]
      have hnot : ¬ (m + 1 ≤ m) := by omega
      simp [hnot]
    have hright :
        (∑ i ∈ Finset.range (m + 1), coeff m i * F (i + 1)) + F 0 =
          ∑ j ∈ Finset.range (m + 2), (if j = 0 then 1 else coeff m (j - 1)) * F j := by
      symm
      rw [Finset.sum_range_succ']
      simp
    have hcomb :
        (∑ j ∈ Finset.range (m + 1), coeff m j * F j) + F (m + 1) +
            (∑ i ∈ Finset.range (m + 1), coeff m i * F (i + 1)) + F 0 =
          ((∑ j ∈ Finset.range (m + 1), coeff m j * F j) + F (m + 1)) +
            ((∑ i ∈ Finset.range (m + 1), coeff m i * F (i + 1)) + F 0) := by
      omega
    rw [hcomb, hleft, hright, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hj_le : j ≤ m + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    rw [← add_mul]
    congr 1
    cases j with
    | zero =>
      simp [coeff_zero]
    | succ i =>
      by_cases hi : i + 1 ≤ m
      · simp [hi, coeff_pascal]
      · have him : i = m := by omega
        rw [him]
        have hnot : ¬ (m + 1 ≤ m) := by omega
        simp [hnot, coeff_self]
        omega

/-- Equivalent integer-valued form of Kurkov's conjecture (avoiding truncated `ℕ` subtraction). -/
theorem kurkov_conjecture_A379818_int (m k : ℕ) :
    (a379818 (2 ^ m * (2 * k + 1)) : ℤ) =
      ∑ j ∈ Finset.range (m + 1),
        ((Nat.choose (m + 2) (j + 1) : ℤ) - (Nat.choose m j : ℤ)) *
          (a379818 (2 ^ j * k) : ℤ) := by
  have h : (a379818 (2 ^ m * (2 * k + 1)) : ℤ) =
      ((∑ j ∈ Finset.range (m + 1),
        (Nat.choose (m + 2) (j + 1) - Nat.choose m j) * a379818 (2 ^ j * k) : ℕ) : ℤ) := by
    exact_mod_cast kurkov_conjecture_A379818 m k
  rw [h]
  push_cast
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [Nat.cast_sub (choose_le_choose_add_two m j)]

/-- Uniqueness / axiomatic version: any sequence `a : ℕ → ℕ` satisfying the OEIS `A379818`
defining recurrence (using Mathlib's `Nat.factorization n 2`) satisfies Kurkov's formula. -/
theorem kurkov_conjecture_A379818_of_recurrence
    (a : ℕ → ℕ)
    (h0 : a 0 = 1)
    (hodd : ∀ n, a (2 * n + 1) = a n)
    (heven : ∀ n, 0 < n →
      a (2 * n) = a n + a (n - 2 ^ n.factorization 2) +
        a (2 * n - 2 ^ n.factorization 2) + a (a025480 (n - 1)))
    (m k : ℕ) :
    a (2 ^ m * (2 * k + 1)) =
      ∑ j ∈ Finset.range (m + 1),
        (Nat.choose (m + 2) (j + 1) - Nat.choose m j) * a (2 ^ j * k) := by
  have heq : ∀ n, a n = a379818 n := by
    intro n
    induction n using Nat.strong_induction_on with
    | ind n ih =>
      cases n with
      | zero => rw [h0, a379818_zero]
      | succ r =>
        rcases Nat.even_or_odd (r + 1) with ⟨t, ht⟩ | ⟨t, ht⟩
        · have ht_pos : 0 < t := by omega
          have h2t : r + 1 = 2 * t := by omega
          rw [h2t, heven t ht_pos, a379818_even ht_pos, ← a007814_eq_factorization]
          have hpow_pos : 0 < 2 ^ a007814 t := Nat.two_pow_pos _
          have ha_le : a025480 (t - 1) ≤ t - 1 := a025480_le _
          rw [ih t (by omega), ih (t - 2 ^ a007814 t) (by omega),
            ih (2 * t - 2 ^ a007814 t) (by omega), ih (a025480 (t - 1)) (by omega)]
        · rw [ht, hodd t, a379818_odd t]
          exact ih t (by omega)
  simp_rw [heq]
  exact kurkov_conjecture_A379818 m k

#print axioms kurkov_conjecture_A379818
#print axioms kurkov_conjecture_A379818_int
#print axioms kurkov_conjecture_A379818_of_recurrence

end OpenMath.OeisA379818
