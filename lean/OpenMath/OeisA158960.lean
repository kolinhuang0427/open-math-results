import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# OEIS A158960 — M. F. Hasler (2014) Denominators of `Hermite(n, 1/5)` Conjecture

This file formalizes the proof of M. F. Hasler's 2014 conjecture on OEIS `A158960`
(revision 28, Comments / Formula, referencing DLMF Table 18.9.1 for physicists' Hermite
polynomials `H_n(x)`):

> **NAME:** Numerator of `Hermite(n, 1/5)`.
> **FORMULA:** `a(n) = 5^n * Hermite(n, 1/5).`
> **COMMENTS:** The denominators are `5^n = A000351(n)` (conjectured). — *M. F. Hasler*, Feb 16 2014

Specifically, for the physicists' Hermite polynomials `H_0(x) = 1`, `H_1(x) = 2x`,
`H_{n+2}(x) = 2x H_{n+1}(x) - 2(n+1) H_n(x)`, we prove that for every `n : ℕ`:
- `b(n) := 5^n * H_n(1/5)` is an integer satisfying `b(0) = 1`, `b(1) = 2`,
  `b(n+2) = 2 b(n+1) - 50 (n+1) b(n)`;
- `b(n) ≡ 2^n (mod 5)`, so `5 ∤ b(n)` and `gcd(|b(n)|, 5^n) = 1`;
- Consequently, the reduced rational number `H_n(1/5) : ℚ` has exact denominator
  `(H_n(1/5)).den = 5^n` and exact numerator `(H_n(1/5)).num = b(n)`.

## Main Results

* `OpenMath.OeisA158960.hermiteEval_eq_div`:
  `Polynomial.eval (1 / 5 : ℚ) (physHermite n) = (a158960 n : ℚ) / (5 ^ n : ℚ)`.
* `OpenMath.OeisA158960.a158960_mod_five`:
  `a158960 n % 5 = (2 ^ n : ℤ) % 5`.
* `OpenMath.OeisA158960.hasler_conjecture_A158960`:
  `(Polynomial.eval (1 / 5 : ℚ) (physHermite n)).den = 5 ^ n ∧`
  `(Polynomial.eval (1 / 5 : ℚ) (physHermite n)).num = a158960 n`.
-/

namespace OpenMath.OeisA158960

open Polynomial

/-- Physicists' Hermite polynomial `H_n(x) ∈ ℚ[X]` (DLMF Table 18.9.1):
`H_0(x) = 1`, `H_1(x) = 2x`, `H_{n+2}(x) = 2x H_{n+1}(x) - 2(n+1) H_n(x)`. -/
noncomputable def physHermite : ℕ → Polynomial ℚ
  | 0 => 1
  | 1 => C 2 * X
  | n + 2 => C 2 * X * physHermite (n + 1) - C (2 * ((n + 1 : ℕ) : ℚ)) * physHermite n

/-- Direct evaluation `H_n(1/5) ∈ ℚ` via the physicists' Hermite recurrence. -/
def hermiteAtFifth : ℕ → ℚ
  | 0 => 1
  | 1 => 2 / 5
  | n + 2 => (2 / 5) * hermiteAtFifth (n + 1) - 2 * ((n + 1 : ℕ) : ℚ) * hermiteAtFifth n

lemma eval_physHermite_fifth (n : ℕ) :
    Polynomial.eval (1 / 5 : ℚ) (physHermite n) = hermiteAtFifth n := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => simp [physHermite, hermiteAtFifth]
    | 1 => simp [physHermite, hermiteAtFifth]; ring
    | k + 2 =>
      simp only [physHermite, hermiteAtFifth, eval_sub, eval_mul, eval_C, eval_X]
      rw [ih (k + 1) (by omega), ih k (by omega)]
      ring

/-- Integer sequence `a158960(n) = 5^n * H_n(1/5)` defined by the recurrence
`a(0) = 1`, `a(1) = 2`, `a(n+2) = 2 a(n+1) - 50 (n+1) a(n)`. -/
def a158960 : ℕ → ℤ
  | 0 => 1
  | 1 => 2
  | n + 2 => 2 * a158960 (n + 1) - 50 * ((n + 1 : ℕ) : ℤ) * a158960 n

lemma hermiteAtFifth_eq_div (n : ℕ) :
    hermiteAtFifth n = (a158960 n : ℚ) / (5 ^ n : ℚ) := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => simp [hermiteAtFifth, a158960]
    | 1 => simp [hermiteAtFifth, a158960]
    | k + 2 =>
      simp only [hermiteAtFifth, a158960]
      rw [ih (k + 1) (by omega), ih k (by omega)]
      push_cast
      have h5 : (5 : ℚ) ^ k ≠ 0 := pow_ne_zero k (by norm_num)
      field_simp [h5]
      ring

/-- Exact rational identity `H_n(1/5) = a158960(n) / 5^n` for all `n ≥ 0`. -/
theorem hermiteEval_eq_div (n : ℕ) :
    Polynomial.eval (1 / 5 : ℚ) (physHermite n) = (a158960 n : ℚ) / (5 ^ n : ℚ) := by
  rw [eval_physHermite_fifth, hermiteAtFifth_eq_div]

/-- `a158960(n) ≡ 2^n (mod 5)` for all `n ≥ 0`. -/
theorem a158960_mod_five (n : ℕ) : a158960 n % 5 = ((2 : ℤ) ^ n) % 5 := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => decide
    | 1 => decide
    | k + 2 =>
      have h1 := ih (k + 1) (by omega)
      simp only [a158960]
      have h50 : (50 * ((k + 1 : ℕ) : ℤ) * a158960 k) % 5 = 0 :=
        Int.emod_eq_zero_of_dvd ⟨10 * ((k + 1 : ℕ) : ℤ) * a158960 k, by ring⟩
      have hmul : (2 * a158960 (k + 1) - 50 * ((k + 1 : ℕ) : ℤ) * a158960 k) % 5 =
          (2 * (a158960 (k + 1) % 5)) % 5 := by omega
      rw [hmul, h1, show (2 : ℤ) ^ (k + 2) = 2 * (2 : ℤ) ^ (k + 1) by ring]
      omega

lemma not_five_dvd_a158960 (n : ℕ) : ¬ ((5 : ℤ) ∣ a158960 n) := by
  intro hdvd
  have hmod : a158960 n % 5 = 0 := Int.emod_eq_zero_of_dvd hdvd
  rw [a158960_mod_five] at hmod
  have h5_2n : (5 : ℤ) ∣ (2 : ℤ) ^ n := Int.dvd_of_emod_eq_zero hmod
  have h5_2n_nat : 5 ∣ 2 ^ n := by
    have : ((5 : ℕ) : ℤ) ∣ ((2 ^ n : ℕ) : ℤ) := by simpa using h5_2n
    exact Int.ofNat_dvd.mp this
  have h5_2 : 5 ∣ 2 := Nat.Prime.dvd_of_dvd_pow (by decide : Nat.Prime 5) h5_2n_nat
  omega

lemma coprime_a158960_five_pow (n : ℕ) : Nat.Coprime (a158960 n).natAbs (5 ^ n) := by
  apply Nat.Coprime.pow_right n
  rw [Nat.coprime_comm, Nat.Prime.coprime_iff_not_dvd (by decide : Nat.Prime 5)]
  intro hdvd
  apply not_five_dvd_a158960 n
  exact Int.natCast_dvd.mpr hdvd

/-- **Main Theorem (M. F. Hasler, OEIS `A158960`, Feb 16 2014):**
For every `n : ℕ`, the reduced rational value `H_n(1/5) ∈ ℚ` of the `n`-th physicists'
Hermite polynomial at `x = 1/5` has exact reduced denominator `5^n` and exact reduced
numerator `a158960(n) = 5^n * H_n(1/5)`. -/
theorem hasler_conjecture_A158960 (n : ℕ) :
    (Polynomial.eval (1 / 5 : ℚ) (physHermite n)).den = 5 ^ n ∧
    (Polynomial.eval (1 / 5 : ℚ) (physHermite n)).num = a158960 n := by
  have hpos : 5 ^ n ≠ 0 := pow_ne_zero n (by decide)
  have hcop : Nat.Coprime (a158960 n).natAbs (5 ^ n) := coprime_a158960_five_pow n
  let r : ℚ := ⟨a158960 n, 5 ^ n, hpos, hcop⟩
  have hr_eq : Polynomial.eval (1 / 5 : ℚ) (physHermite n) = r := by
    rw [hermiteEval_eq_div]
    have hdiv : (r : ℚ) = (r.num : ℚ) / (r.den : ℚ) := (Rat.num_div_den r).symm
    simpa [r] using hdiv.symm
  rw [hr_eq]
  exact ⟨rfl, rfl⟩

/-- Explicit check of the initial OEIS `A158960` values `n = 0..7`:
`1, 2, -46, -292, 6316, 71032, -1436936, -24183472`. -/
theorem a158960_initial :
    (a158960 0, a158960 1, a158960 2, a158960 3, a158960 4, a158960 5, a158960 6, a158960 7) =
    (1, 2, -46, -292, 6316, 71032, -1436936, -24183472) := by
  norm_num [a158960]

#print axioms hermiteEval_eq_div
#print axioms a158960_mod_five
#print axioms hasler_conjecture_A158960

end OpenMath.OeisA158960
