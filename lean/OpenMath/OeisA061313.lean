import Mathlib.Data.Rat.Defs
import Mathlib.Data.Rat.Cast.Defs
import Mathlib.Tactic

/-!
# OEIS A061313: Andrei Zabolotskii's Hirzebruch Continued Fraction Conjecture

Primary sources:
- OEIS `A061313` (rev. 58, 2026-11-01):
  - Name: "Minimal number of steps to get from 1 to n by (a) subtracting 1 or (b) multiplying by 2."
  - Formula: `a(2n) = a(n) + 1; a(2n + 1) = a(n + 1) + 2; a(1) = 0.`
  - Comment (Conjecture, Andrei Zabolotskii, Apr 17 2020):
    "Conjecture: a(n) + 2 is the sum of the terms of the Hirzebruch (negative) continued
     fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n)."
- OEIS `A007305` / `A007306`: Numerators and denominators of the Farey / Stern-Brocot
  subtree on `[0, 1]`, starting `0/1, 1/1, 1/2, 1/3, 2/3, 1/4, 2/5, 3/5, 3/4, ...`.

This file proves:
1. Equivalence between the operational shortest-path definition of `A061313` and its recurrence.
2. Exact agreement between the level-by-level Farey/Stern-Brocot mediant construction
   (`A007305`/`A007306`) and the `SL_2(ℤ)` matrix recursion `M(2m - 1) = M(m) L`, `M(2m) = M(m) R`.
3. Uniqueness of canonical Hirzebruch (negative) continued fractions `[[c₀; c₁, ..., c_k]]`
   with `c₁, ..., c_k ≥ 2`.
4. **Main Theorem (`zabolotskii_conjecture_A061313`):** For every `n ≥ 2`, the unique
   canonical Hirzebruch continued fraction `cs` of `A007305(n) / A007306(n)` satisfies
   `cs.sum = a061313 n + 2`.
5. **Sole Boundary Exception (`zabolotskii_boundary_exception_at_one`):** At `n = 1`,
   `A007305(1) / A007306(1) = 1` has unique canonical Hirzebruch expansion `[1]` of sum `1`,
   whereas `a061313 1 + 2 = 2`.
-/

namespace OpenMath.OeisA061313

/-! ## Section 1: OEIS A061313 (Recurrence and Minimal-Steps Characterization) -/

/-- OEIS `A061313`: `a(1) = 0`, `a(2n) = a(n) + 1`, `a(2n + 1) = a(n + 1) + 2` for `n ≥ 1`.
(Conventional value `a(0) = 0` outside the offset-1 domain.) -/
def a061313 : ℕ → ℕ
  | 0 => 0
  | 1 => 0
  | n + 2 =>
    if (n + 2) % 2 = 0 then
      a061313 ((n + 2) / 2) + 1
    else
      a061313 ((n + 2) / 2 + 1) + 2
termination_by n => n
decreasing_by all_goals omega

lemma a061313_one : a061313 1 = 0 := by rw [a061313]

lemma a061313_even {n : ℕ} (hn : 1 ≤ n) : a061313 (2 * n) = a061313 n + 1 := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
  have h : 2 * (1 + m) = (2 * m) + 2 := by omega
  conv_lhs => rw [h, a061313]
  have hev : (2 * m + 2) % 2 = 0 := by omega
  have hdiv : (2 * m + 2) / 2 = 1 + m := by omega
  rw [ite_eq_left hev, hdiv]

lemma a061313_odd {n : ℕ} (hn : 1 ≤ n) : a061313 (2 * n + 1) = a061313 (n + 1) + 2 := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
  have h : 2 * (1 + m) + 1 = (2 * m + 1) + 2 := by omega
  conv_lhs => rw [h, a061313]
  have hodd : ¬ ((2 * m + 1 + 2) % 2 = 0) := by omega
  have hdiv : (2 * m + 1 + 2) / 2 + 1 = 1 + m + 1 := by omega
  rw [ite_eq_right hodd, hdiv]

lemma a061313_two : a061313 2 = 1 := by
  simpa [a061313_one] using a061313_even (n := 1) le_rfl

lemma a061313_two_mul_sub_one {m : ℕ} (hm : 2 ≤ m) :
    a061313 (2 * m - 1) = a061313 m + 2 := by
  have h1 : 2 * m - 1 = 2 * (m - 1) + 1 := by omega
  have h2 : m - 1 + 1 = m := by omega
  rw [h1, a061313_odd (by omega), h2]

/-- One-step relation for the operational definition of `A061313`:
from `x : ℤ` to `y : ℤ` by (a) subtracting `1` (`y = x - 1`) or (b) multiplying by `2` (`y = 2 * x`). -/
inductive Step : ℤ → ℤ → Prop
  | sub_one (x : ℤ) : Step x (x - 1)
  | mul_two (x : ℤ) : Step x (2 * x)

/-- Reachability in `k` steps of (a) subtracting 1 or (b) multiplying by 2. -/
inductive ReachIn : ℕ → ℤ → ℤ → Prop
  | zero (x : ℤ) : ReachIn 0 x x
  | succ {k : ℕ} {x y z : ℤ} : ReachIn k x y → Step y z → ReachIn (k + 1) x z

lemma a061313_sub_one_le : ∀ x : ℕ, 2 ≤ x → a061313 (x - 1) ≤ a061313 x + 1 := by
  intro x
  induction x using Nat.strong_induction_on with
  | ind x ih =>
    intro hx
    rcases Nat.even_or_odd x with ⟨m, hm⟩ | ⟨m, hm⟩
    · have hm1 : 1 ≤ m := by omega
      have hx_eq : x = 2 * m := by omega
      rw [hx_eq]
      by_cases hm2 : 2 ≤ m
      · rw [a061313_two_mul_sub_one hm2, a061313_even hm1]
      · have : m = 1 := by omega
        subst this
        rw [a061313_two, a061313_one]
        omega
    · have hm1 : 1 ≤ m := by omega
      rw [hm, a061313_odd hm1]
      have hsub : 2 * m + 1 - 1 = 2 * m := by omega
      rw [hsub, a061313_even hm1]
      have hih := ih (m + 1) (by omega) (by omega)
      have hm_sub : m + 1 - 1 = m := by omega
      rw [hm_sub] at hih
      omega

lemma reachIn_nonpos_stays_nonpos {k : ℕ} {x y : ℤ} (h : ReachIn k x y) (hx : x ≤ 0) :
    y ≤ 0 := by
  induction h with
  | zero _ => exact hx
  | succ _ hstep ih =>
    cases hstep <;> omega

lemma a061313_le_of_reachIn {k : ℕ} {x y : ℤ} (h : ReachIn k x y) :
    x = 1 → ∀ n : ℕ, 1 ≤ n → y = (n : ℤ) → a061313 n ≤ k := by
  induction h with
  | zero _ =>
    intro hx n _ hn
    have : n = 1 := by omega
    subst this
    simp [a061313_one]
  | @succ k x y z hreach hstep ih =>
    intro hx n hn hz
    cases hstep with
    | sub_one =>
      have hy_pos : 1 ≤ y := by omega
      obtain ⟨m, hm⟩ := Int.eq_ofNat_of_zero_le (by omega : 0 ≤ y)
      have hm2 : 2 ≤ m := by omega
      have hnm : n = m - 1 := by omega
      have hprev := ih hx m (by omega) hm
      have hstep_le := a061313_sub_one_le m hm2
      rw [hnm]
      omega
    | mul_two =>
      have hy_pos : 1 ≤ y := by omega
      obtain ⟨m, hm⟩ := Int.eq_ofNat_of_zero_le (by omega : 0 ≤ y)
      have hm1 : 1 ≤ m := by omega
      have hnm : n = 2 * m := by omega
      have hprev := ih hx m hm1 hm
      rw [hnm, a061313_even hm1]
      omega

lemma reachIn_a061313 : ∀ n : ℕ, 1 ≤ n → ReachIn (a061313 n) 1 (n : ℤ) := by
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    intro hn
    by_cases h1 : n = 1
    · subst h1
      simpa [a061313_one] using ReachIn.zero 1
    · rcases Nat.even_or_odd n with ⟨m, hm⟩ | ⟨m, hm⟩
      · have hm1 : 1 ≤ m := by omega
        have hn_eq : n = 2 * m := by omega
        rw [hn_eq, a061313_even hm1]
        have hprev := ih m (by omega) hm1
        have hcast : ((2 * m : ℕ) : ℤ) = 2 * (m : ℤ) := by push_cast; ring
        rw [hcast]
        exact ReachIn.succ hprev (Step.mul_two (m : ℤ))
      · have hm1 : 1 ≤ m := by omega
        rw [hm, a061313_odd hm1]
        have hprev := ih (m + 1) (by omega) (by omega)
        have h1step : ReachIn (a061313 (m + 1) + 1) 1 (2 * ((m + 1 : ℕ) : ℤ)) :=
          ReachIn.succ hprev (Step.mul_two ((m + 1 : ℕ) : ℤ))
        have hcast : ((2 * m + 1 : ℕ) : ℤ) = 2 * ((m + 1 : ℕ) : ℤ) - 1 := by push_cast; ring
        rw [hcast]
        exact ReachIn.succ h1step (Step.sub_one _)

/-- Fidelity theorem: `a061313 n` is literally the minimal number of `(a) -1 / (b) ×2` steps
to reach `n ≥ 1` from `1` (even allowing arbitrary intermediate integers). -/
theorem a061313_is_min_steps {n : ℕ} (hn : 1 ≤ n) :
    ReachIn (a061313 n) 1 (n : ℤ) ∧ ∀ k, ReachIn k 1 (n : ℤ) → a061313 n ≤ k :=
  ⟨reachIn_a061313 n hn, fun _ h => a061313_le_of_reachIn h rfl n hn rfl⟩

/-! ## Section 2: `SL_2(ℤ)` Matrices and the Stern–Brocot Tree (`A007305` / `A007306`) -/

/-- Lightweight `2 × 2` integer matrices. -/
@[ext]
structure Mat2 where
  m11 : ℤ
  m12 : ℤ
  m21 : ℤ
  m22 : ℤ
deriving DecidableEq

namespace Mat2

def one : Mat2 := ⟨1, 0, 0, 1⟩

def mul (A B : Mat2) : Mat2 :=
  ⟨A.m11 * B.m11 + A.m12 * B.m21,
   A.m11 * B.m12 + A.m12 * B.m22,
   A.m21 * B.m11 + A.m22 * B.m21,
   A.m21 * B.m12 + A.m22 * B.m22⟩

instance : One Mat2 := ⟨Mat2.one⟩
instance : Mul Mat2 := ⟨Mat2.mul⟩

@[simp] lemma one_m11 : (1 : Mat2).m11 = 1 := rfl
@[simp] lemma one_m12 : (1 : Mat2).m12 = 0 := rfl
@[simp] lemma one_m21 : (1 : Mat2).m21 = 0 := rfl
@[simp] lemma one_m22 : (1 : Mat2).m22 = 1 := rfl
@[simp] lemma mul_m11 (A B : Mat2) : (A * B).m11 = A.m11 * B.m11 + A.m12 * B.m21 := rfl
@[simp] lemma mul_m12 (A B : Mat2) : (A * B).m12 = A.m11 * B.m12 + A.m12 * B.m22 := rfl
@[simp] lemma mul_m21 (A B : Mat2) : (A * B).m21 = A.m21 * B.m11 + A.m22 * B.m21 := rfl
@[simp] lemma mul_m22 (A B : Mat2) : (A * B).m22 = A.m21 * B.m12 + A.m22 * B.m22 := rfl

lemma mul_assoc (A B C : Mat2) : (A * B) * C = A * (B * C) := by
  ext <;> simp <;> ring

lemma one_mul (A : Mat2) : 1 * A = A := by
  ext <;> simp

lemma mul_one (A : Mat2) : A * 1 = A := by
  ext <;> simp

/-- Stern-Brocot left-child matrix `L = [[1, 0], [1, 1]]`. -/
def L : Mat2 := ⟨1, 0, 1, 1⟩

/-- Stern-Brocot right-child matrix `R = [[1, 1], [0, 1]]`. -/
def R : Mat2 := ⟨1, 1, 0, 1⟩

/-- Hirzebruch step matrix `H(c) = [[c, -1], [1, 0]]`. -/
def H (c : ℤ) : Mat2 := ⟨c, -1, 1, 0⟩

/-- Conjugation matrix `J = H(1) = [[1, -1], [1, 0]]` and its inverse. -/
def J : Mat2 := H 1
def Jinv : Mat2 := ⟨0, 1, -1, 1⟩

lemma J_mul_Jinv : J * Jinv = 1 := by decide
lemma Jinv_mul_J : Jinv * J = 1 := by decide

/-- Step 2 Identity 1: `L * J = H(1) * H(2)`. -/
lemma L_mul_J : L * J = H 1 * H 2 := by decide

/-- Step 2 Identity 2: `L * J = J * H(2)`. -/
lemma L_mul_J_eq_J_mul_H2 : L * J = J * H 2 := by decide

/-- Step 2 Identity 3: `H(c) * (J⁻¹ * R * J) = H(c + 1)` for every `c : ℤ`. -/
lemma H_mul_conjR (c : ℤ) : H c * (Jinv * R * J) = H (c + 1) := by
  ext <;> simp [H, J, Jinv, R]

lemma R_mul_J_eq_J_mul_conjR : R * J = J * (Jinv * R * J) := by
  rw [← mul_assoc, ← mul_assoc, J_mul_Jinv, one_mul]

end Mat2

/-- Farey ancestor interval matrix `M(m) = [[c_m, a_m], [d_m, b_m]]` for `m ≥ 2`:
`M(2) = [[1, 0], [1, 1]]`, `M(2m - 1) = M(m) * L`, `M(2m) = M(m) * R`. -/
def sbMat : ℕ → Mat2
  | 0 => Mat2.one
  | 1 => Mat2.one
  | 2 => Mat2.L
  | n + 3 =>
    if (n + 3) % 2 = 0 then
      sbMat ((n + 3) / 2) * Mat2.R
    else
      sbMat ((n + 3) / 2 + 1) * Mat2.L
termination_by n => n
decreasing_by all_goals omega

lemma sbMat_two : sbMat 2 = Mat2.L := by rw [sbMat]

lemma sbMat_even {m : ℕ} (hm : 2 ≤ m) : sbMat (2 * m) = sbMat m * Mat2.R := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  have h : 2 * (2 + k) = (2 * k + 1) + 3 := by omega
  conv_lhs => rw [h, sbMat]
  have hev : (2 * k + 1 + 3) % 2 = 0 := by omega
  have hdiv : (2 * k + 1 + 3) / 2 = 2 + k := by omega
  rw [ite_eq_left hev, hdiv]

lemma sbMat_odd {m : ℕ} (hm : 2 ≤ m) : sbMat (2 * m - 1) = sbMat m * Mat2.L := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  have h : 2 * (2 + k) - 1 = (2 * k) + 3 := by omega
  conv_lhs => rw [h, sbMat]
  have hodd : ¬ ((2 * k + 3) % 2 = 0) := by omega
  have hdiv : (2 * k + 3) / 2 + 1 = 2 + k := by omega
  rw [ite_eq_right hodd, hdiv]

/-- Level-`L` Farey/Stern-Brocot intervals on `[0, 1]`, each stored as `((a, b), (c, d))`
representing `[a/b, c/d]` in increasing order (length `2^L`).
Level 0 has `[0/1, 1/1]`; level `L + 1` splits each `[a/b, c/d]` at its mediant `(a+c)/(b+d)`. -/
def fareyIntervals : ℕ → List ((ℤ × ℤ) × (ℤ × ℤ))
  | 0 => [((0, 1), (1, 1))]
  | L + 1 =>
    (fareyIntervals L).flatMap fun iv =>
      let a := iv.1.1; let b := iv.1.2; let c := iv.2.1; let d := iv.2.2
      [((a, b), (a + c, b + d)), ((a + c, b + d), (c, d))]

lemma fareyIntervals_length (L : ℕ) : (fareyIntervals L).length = 2 ^ L := by
  induction L with
  | zero => rfl
  | succ L ih =>
    simp [fareyIntervals, List.length_flatMap, ih]
    ring

/-- Encode an interval `((a, b), (c, d))` as the matrix `[[c, a], [d, b]]`. -/
def intervalMat (iv : (ℤ × ℤ) × (ℤ × ℤ)) : Mat2 :=
  ⟨iv.2.1, iv.1.1, iv.2.2, iv.1.2⟩

/-- Step 1 (Exact equivalence between level-by-level Stern-Brocot mediant splitting and `sbMat`):
For every level `L ≥ 0` and `0 ≤ j < 2^L`, the `j`-th interval of `fareyIntervals L` has matrix
`sbMat (2^L + j + 1)`. -/
theorem fareyIntervals_getElem_eq_sbMat (L : ℕ) :
    ∀ (j : ℕ) (hj : j < (fareyIntervals L).length),
      intervalMat ((fareyIntervals L)[j]) = sbMat (2 ^ L + j + 1) := by
  induction L with
  | zero =>
    intro j hj
    have hj0 : j = 0 := by simp [fareyIntervals] at hj; omega
    subst hj0
    simp [fareyIntervals, intervalMat, sbMat_two, Mat2.L]
  | succ L ih =>
    intro j hj
    have hlenL : (fareyIntervals L).length = 2 ^ L := fareyIntervals_length L
    have hj_bound : j < 2 ^ (L + 1) := by simpa [fareyIntervals_length] using hj
    have hi_lt : j / 2 < (fareyIntervals L).length := by
      rw [hlenL]
      have hpow : 2 ^ (L + 1) = 2 * 2 ^ L := by ring
      omega
    -- Compute the `(j)`-th element of `flatMap` of pairs.
    have hflat : ∀ (xs : List ((ℤ × ℤ) × (ℤ × ℤ))) (k : ℕ) (hk : k < 2 * xs.length),
        let f : ((ℤ × ℤ) × (ℤ × ℤ)) → List ((ℤ × ℤ) × (ℤ × ℤ)) := fun iv =>
          let a := iv.1.1; let b := iv.1.2; let c := iv.2.1; let d := iv.2.2
          [((a, b), (a + c, b + d)), ((a + c, b + d), (c, d))]
        have hk' : k < (xs.flatMap f).length := by
          simp [List.length_flatMap, f]; omega
        intervalMat ((xs.flatMap f)[k]'hk') =
          intervalMat (xs[k / 2]'(by omega)) * (if k % 2 = 0 then Mat2.L else Mat2.R) := by
      intro xs
      induction xs with
      | nil => intro k hk; simp at hk
      | cons hd tl ihtl =>
        intro k hk
        cases k with
        | zero =>
          rcases hd with ⟨⟨a, b⟩, ⟨c, d⟩⟩
          ext <;> simp [intervalMat, Mat2.L] <;> ring
        | succ k' =>
          cases k' with
          | zero =>
            rcases hd with ⟨⟨a, b⟩, ⟨c, d⟩⟩
            ext <;> simp [intervalMat, Mat2.R] <;> ring
          | succ k'' =>
            have hk'' : k'' < 2 * tl.length := by simp at hk; omega
            have hrec := ihtl k'' hk''
            have hmod : (k'' + 2) % 2 = k'' % 2 := by omega
            have hdiv : (k'' + 2) / 2 = k'' / 2 + 1 := by omega
            simpa [List.flatMap_cons, hmod, hdiv] using hrec
    have hj2 : j < 2 * (fareyIntervals L).length := by
      rw [hlenL]
      have hpow : 2 ^ (L + 1) = 2 * 2 ^ L := by ring
      omega
    have hstep := hflat (fareyIntervals L) j hj2
    have hih := ih (j / 2) hi_lt
    have hm_ge2 : 2 ≤ 2 ^ L + j / 2 + 1 := by
      have : 1 ≤ 2 ^ L := Nat.one_le_two_pow
      omega
    have hstep' : intervalMat ((fareyIntervals (L + 1))[j]'hj) =
        intervalMat ((fareyIntervals L)[j / 2]'hi_lt) * (if j % 2 = 0 then Mat2.L else Mat2.R) :=
      hstep
    rw [hstep', hih]
    by_cases hev : j % 2 = 0
    · rw [ite_eq_left hev]
      have hidx : 2 ^ (L + 1) + j + 1 = 2 * (2 ^ L + j / 2 + 1) - 1 := by
        have : 2 ^ (L + 1) = 2 * 2 ^ L := by ring
        omega
      rw [hidx, sbMat_odd hm_ge2]
    · rw [ite_eq_right hev]
      have hidx : 2 ^ (L + 1) + j + 1 = 2 * (2 ^ L + j / 2 + 1) := by
        have : 2 ^ (L + 1) = 2 * 2 ^ L := by ring
        omega
      rw [hidx, sbMat_even hm_ge2]

/-- OEIS `A007305` (numerators of Stern-Brocot / Farey tree fractions on `[0, 1]`).
For `n = 0`: `0`; `n = 1`: `1`; for `n ≥ 2`: mediant numerator `a_n + c_n = M(n).11 + M(n).12`. -/
def a007305 : ℕ → ℤ
  | 0 => 0
  | 1 => 1
  | n + 2 => (sbMat (n + 2)).m11 + (sbMat (n + 2)).m12

/-- OEIS `A007306` (denominators of Stern-Brocot / Farey tree fractions on `[0, 1]`).
For `n = 0`: `1`; `n = 1`: `1`; for `n ≥ 2`: mediant denominator `b_n + d_n = M(n).21 + M(n).22`. -/
def a007306 : ℕ → ℤ
  | 0 => 1
  | 1 => 1
  | n + 2 => (sbMat (n + 2)).m21 + (sbMat (n + 2)).m22

/-- The Stern-Brocot fraction `r(n) = A007305(n) / A007306(n) ∈ ℚ`. -/
def sternBrocotFrac (n : ℕ) : ℚ :=
  (a007305 n : ℚ) / (a007306 n : ℚ)

/-- The first column of `P(n) = M(n) * J` is `(A007305(n), A007306(n))` for all `n ≥ 2`. -/
lemma sbMat_mul_J_first_col {n : ℕ} (hn : 2 ≤ n) :
    (sbMat n * Mat2.J).m11 = a007305 n ∧ (sbMat n * Mat2.J).m21 = a007306 n := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hn
  have h : 2 + k = k + 2 := by omega
  rw [h]
  constructor <;> simp [a007305, a007306, Mat2.J, Mat2.H]

/-! ## Section 3: Canonical Hirzebruch (Negative) Continued Fractions -/

/-- Value of a finite Hirzebruch (negative) continued fraction `[[c₀; c₁, ..., c_k]]`:
`[[c₀]] = c₀` and `[[c₀; c₁, ..., c_k]] = c₀ - 1 / [[c₁; ..., c_k]]`. -/
def hirzebruchEval : List ℤ → ℚ
  | [] => 0
  | [c] => (c : ℚ)
  | c :: rest => (c : ℚ) - (hirzebruchEval rest)⁻¹

/-- A list `[c₀, c₁, ..., c_k]` is a **canonical** Hirzebruch continued fraction
if it is non-empty and every tail entry satisfies `c_i ≥ 2` (`i ≥ 1`). -/
def IsCanonicalHirzebruch : List ℤ → Prop
  | [] => False
  | _ :: rest => ∀ c ∈ rest, 2 ≤ c

/-- Matrix product `H(c₀) * H(c₁) * ... * H(c_k)`. -/
def hirzebruchProd : List ℤ → Mat2
  | [] => 1
  | c :: rest => Mat2.H c * hirzebruchProd rest

lemma hirzebruchProd_append (l₁ l₂ : List ℤ) :
    hirzebruchProd (l₁ ++ l₂) = hirzebruchProd l₁ * hirzebruchProd l₂ := by
  induction l₁ with
  | nil => simp [hirzebruchProd, Mat2.one_mul]
  | cons c rest ih =>
    simp [hirzebruchProd, ih, Mat2.mul_assoc]

/-- For a non-empty list of integers all `≥ 2`, `hirzebruchEval` is strictly greater than `1`. -/
lemma one_lt_hirzebruchEval_of_ge_two :
    ∀ cs : List ℤ, cs ≠ [] → (∀ c ∈ cs, 2 ≤ c) → (1 : ℚ) < hirzebruchEval cs := by
  intro cs
  induction cs with
  | nil => intro h; exact (h rfl).elim
  | cons c rest ih =>
    intro _ hge
    have hc : (2 : ℚ) ≤ (c : ℚ) := by exact_mod_cast hge c (by simp)
    cases rest with
    | nil =>
      dsimp [hirzebruchEval]
      linarith
    | cons d tl =>
      have hrest_gt : (1 : ℚ) < hirzebruchEval (d :: tl) :=
        ih (by simp) (fun x hx => hge x (by simp [hx]))
      have hinv_lt : (hirzebruchEval (d :: tl))⁻¹ < 1 :=
        inv_lt_one_of_one_lt₀ hrest_gt
      change (1 : ℚ) < (c : ℚ) - (hirzebruchEval (d :: tl))⁻¹
      linarith

/-- For any canonical Hirzebruch list `c :: d :: tl`, `c - 1 < hirzebruchEval (c :: d :: tl) < c`. -/
lemma hirzebruchEval_bounds_cons_cons {c d : ℤ} {tl : List ℤ}
    (hcan : IsCanonicalHirzebruch (c :: d :: tl)) :
    (c : ℚ) - 1 < hirzebruchEval (c :: d :: tl) ∧ hirzebruchEval (c :: d :: tl) < (c : ℚ) := by
  have hgt : (1 : ℚ) < hirzebruchEval (d :: tl) :=
    one_lt_hirzebruchEval_of_ge_two (d :: tl) (by simp) hcan
  have hinv_pos : (0 : ℚ) < (hirzebruchEval (d :: tl))⁻¹ := inv_pos.mpr (by linarith)
  have hinv_lt : (hirzebruchEval (d :: tl))⁻¹ < 1 := inv_lt_one_of_one_lt₀ hgt
  change (c : ℚ) - 1 < (c : ℚ) - (hirzebruchEval (d :: tl))⁻¹ ∧
    (c : ℚ) - (hirzebruchEval (d :: tl))⁻¹ < (c : ℚ)
  constructor <;> linarith

/-- **Uniqueness of canonical Hirzebruch continued fractions:**
if `l₁` and `l₂` are canonical and evaluate to the same rational number, then `l₁ = l₂`. -/
theorem hirzebruch_canonical_unique :
    ∀ l₁ l₂ : List ℤ,
      IsCanonicalHirzebruch l₁ →
      IsCanonicalHirzebruch l₂ →
      hirzebruchEval l₁ = hirzebruchEval l₂ →
      l₁ = l₂ := by
  intro l₁
  induction l₁ with
  | nil => intro _ h1; exact False.elim h1
  | cons c₁ r₁ ih =>
    intro l₂ h1 h2 heq
    cases l₂ with
    | nil => exact False.elim h2
    | cons c₂ r₂ =>
      cases r₁ with
      | nil =>
        cases r₂ with
        | nil =>
          dsimp [hirzebruchEval] at heq
          have : c₁ = c₂ := by exact_mod_cast heq
          rw [this]
        | cons d₂ t₂ =>
          have hb := hirzebruchEval_bounds_cons_cons h2
          rw [← heq] at hb
          dsimp [hirzebruchEval] at hb
          have hlt1 : c₂ - 1 < c₁ := by exact_mod_cast hb.1
          have hlt2 : c₁ < c₂ := by exact_mod_cast hb.2
          omega
      | cons d₁ t₁ =>
        cases r₂ with
        | nil =>
          have hb := hirzebruchEval_bounds_cons_cons h1
          rw [heq] at hb
          dsimp [hirzebruchEval] at hb
          have hlt1 : c₁ - 1 < c₂ := by exact_mod_cast hb.1
          have hlt2 : c₂ < c₁ := by exact_mod_cast hb.2
          omega
        | cons d₂ t₂ =>
          have hb1 := hirzebruchEval_bounds_cons_cons h1
          have hb2 := hirzebruchEval_bounds_cons_cons h2
          have hc1_lt : c₁ - 1 < c₂ := by
            have : ((c₁ - 1 : ℤ) : ℚ) < (c₂ : ℚ) := by push_cast; linarith
            exact_mod_cast this
          have hc2_lt : c₂ - 1 < c₁ := by
            have : ((c₂ - 1 : ℤ) : ℚ) < (c₁ : ℚ) := by push_cast; linarith
            exact_mod_cast this
          have hceq : c₁ = c₂ := by omega
          subst hceq
          have hinv_eq : (hirzebruchEval (d₁ :: t₁))⁻¹ = (hirzebruchEval (d₂ :: t₂))⁻¹ := by
            change (c₁ : ℚ) - (hirzebruchEval (d₁ :: t₁))⁻¹ =
              (c₁ : ℚ) - (hirzebruchEval (d₂ :: t₂))⁻¹ at heq
            linarith
          have htail_eq : hirzebruchEval (d₁ :: t₁) = hirzebruchEval (d₂ :: t₂) :=
            inv_injective hinv_eq
          have hcan1 : IsCanonicalHirzebruch (d₁ :: t₁) := fun x hx => h1 x (by simp [hx])
          have hcan2 : IsCanonicalHirzebruch (d₂ :: t₂) := fun x hx => h2 x (by simp [hx])
          have hreq := ih (d₂ :: t₂) hcan1 hcan2 htail_eq
          rw [hreq]

/-- First column `(p, q)` of `hirzebruchProd cs` for a tail of entries `≥ 2` satisfies
`0 < q < p` and `p / q = hirzebruchEval cs`. -/
lemma hirzebruchProd_eval_ge_two :
    ∀ cs : List ℤ, cs ≠ [] → (∀ c ∈ cs, 2 ≤ c) →
      let M := hirzebruchProd cs
      0 < M.m21 ∧ M.m21 < M.m11 ∧ (M.m11 : ℚ) / (M.m21 : ℚ) = hirzebruchEval cs := by
  intro cs
  induction cs with
  | nil => intro h; exact (h rfl).elim
  | cons c rest ih =>
    intro _ hge
    have hc : 2 ≤ c := hge c (by simp)
    cases rest with
    | nil =>
      refine ⟨by simp [hirzebruchProd, Mat2.H], ?_, ?_⟩
      · simp [hirzebruchProd, Mat2.H]; omega
      · simp [hirzebruchProd, Mat2.H, hirzebruchEval]
    | cons d tl =>
      obtain ⟨hq_pos, hq_lt_p, heval⟩ := ih (by simp) (fun x hx => hge x (by simp [hx]))
      set N := hirzebruchProd (d :: tl)
      have hm11 : (hirzebruchProd (c :: d :: tl)).m11 = c * N.m11 - N.m21 := by
        simp [hirzebruchProd, Mat2.H, N]; ring
      have hm21 : (hirzebruchProd (c :: d :: tl)).m21 = N.m11 := by
        simp [hirzebruchProd, Mat2.H, N]
      have hp_pos : (0 : ℤ) < N.m11 := by omega
      have hgt : N.m11 < c * N.m11 - N.m21 := by nlinarith
      refine ⟨by rw [hm21]; exact hp_pos, by rw [hm11, hm21]; exact hgt, ?_⟩
      rw [hm11, hm21]
      change ((c * N.m11 - N.m21 : ℤ) : ℚ) / (N.m11 : ℚ) =
        (c : ℚ) - (hirzebruchEval (d :: tl))⁻¹
      rw [← heval, inv_div]
      have hp_ne : (N.m11 : ℚ) ≠ 0 := by exact_mod_cast hp_pos.ne'
      push_cast
      field_simp [hp_ne]

/-- For any canonical Hirzebruch list `c₀ :: rest` with `rest ≠ []`, the first column `(p, q)`
of `hirzebruchProd (c₀ :: rest)` satisfies `0 < q` and `p / q = hirzebruchEval (c₀ :: rest)`. -/
lemma hirzebruchProd_eval_canonical (c₀ : ℤ) (d : ℤ) (tl : List ℤ)
    (hge : ∀ c ∈ d :: tl, 2 ≤ c) :
    let M := hirzebruchProd (c₀ :: d :: tl)
    0 < M.m21 ∧ (M.m11 : ℚ) / (M.m21 : ℚ) = hirzebruchEval (c₀ :: d :: tl) := by
  obtain ⟨hq_pos, hq_lt_p, heval⟩ := hirzebruchProd_eval_ge_two (d :: tl) (by simp) hge
  set N := hirzebruchProd (d :: tl)
  have hm11 : (hirzebruchProd (c₀ :: d :: tl)).m11 = c₀ * N.m11 - N.m21 := by
    simp [hirzebruchProd, Mat2.H, N]; ring
  have hm21 : (hirzebruchProd (c₀ :: d :: tl)).m21 = N.m11 := by
    simp [hirzebruchProd, Mat2.H, N]
  have hp_pos : (0 : ℤ) < N.m11 := by omega
  refine ⟨by rw [hm21]; exact hp_pos, ?_⟩
  rw [hm11, hm21]
  change ((c₀ * N.m11 - N.m21 : ℤ) : ℚ) / (N.m11 : ℚ) =
    (c₀ : ℚ) - (hirzebruchEval (d :: tl))⁻¹
  rw [← heval, inv_div]
  have hp_ne : (N.m11 : ℚ) ≠ 0 := by exact_mod_cast hp_pos.ne'
  push_cast
  field_simp [hp_ne]

/-! ## Section 4: Structural Induction and Main Theorem -/

/-- Increment the last entry of a list of integers (leaving `[]` unchanged). -/
def incLast : List ℤ → List ℤ
  | [] => []
  | [x] => [x + 1]
  | x :: xs => x :: incLast xs

lemma incLast_ne_nil : ∀ l : List ℤ, l ≠ [] → incLast l ≠ []
  | [], h => (h rfl).elim
  | [_], _ => by simp [incLast]
  | _ :: _ :: _, _ => by simp [incLast]

lemma incLast_ge_two : ∀ l : List ℤ, (∀ c ∈ l, 2 ≤ c) → ∀ c ∈ incLast l, 2 ≤ c := by
  intro l
  induction l with
  | nil => simp [incLast]
  | cons x xs ih =>
    cases xs with
    | nil =>
      intro h c hc
      simp [incLast] at hc
      have hx : 2 ≤ x := h x (by simp)
      omega
    | cons y ys =>
      intro h c hc
      simp only [incLast, List.mem_cons] at hc
      rcases hc with rfl | hmem
      · exact h c (by simp)
      · exact ih (fun z hz => h z (by simp [hz])) c hmem

lemma incLast_sum : ∀ l : List ℤ, l ≠ [] → (incLast l).sum = l.sum + 1 := by
  intro l
  induction l with
  | nil => intro h; exact (h rfl).elim
  | cons x xs ih =>
    cases xs with
    | nil => intro _; simp [incLast]
    | cons y ys =>
      intro _
      have hrec := ih (by simp)
      simp only [incLast, List.sum_cons] at hrec ⊢
      omega

lemma incLast_length : ∀ l : List ℤ, (incLast l).length = l.length := by
  intro l
  induction l with
  | nil => rfl
  | cons x xs ih =>
    cases xs with
    | nil => rfl
    | cons y ys => simp [incLast, ih]

lemma hirzebruchProd_incLast :
    ∀ l : List ℤ, l ≠ [] → hirzebruchProd (incLast l) = hirzebruchProd l * (Mat2.Jinv * Mat2.R * Mat2.J) := by
  intro l
  induction l with
  | nil => intro h; exact (h rfl).elim
  | cons x xs ih =>
    cases xs with
    | nil =>
      intro _
      simp only [incLast, hirzebruchProd, Mat2.mul_one]
      exact (Mat2.H_mul_conjR x).symm
    | cons y ys =>
      intro _
      have hrec := ih (by simp)
      change Mat2.H x * hirzebruchProd (incLast (y :: ys)) =
        (Mat2.H x * hirzebruchProd (y :: ys)) * (Mat2.Jinv * Mat2.R * Mat2.J)
      rw [hrec, ← Mat2.mul_assoc]

/-- The tail `[c₁, ..., c_k]` of the canonical Hirzebruch continued fraction `[[1; c₁, ..., c_k]]`
of `r(n) = A007305(n) / A007306(n)` for `n ≥ 2`. -/
def hirzebruchTail : ℕ → List ℤ
  | 0 => [2]
  | 1 => [2]
  | 2 => [2]
  | n + 3 =>
    if (n + 3) % 2 = 0 then
      incLast (hirzebruchTail ((n + 3) / 2))
    else
      hirzebruchTail ((n + 3) / 2 + 1) ++ [2]
termination_by n => n
decreasing_by all_goals omega

lemma hirzebruchTail_two : hirzebruchTail 2 = [2] := by rw [hirzebruchTail]

lemma hirzebruchTail_even {m : ℕ} (hm : 2 ≤ m) :
    hirzebruchTail (2 * m) = incLast (hirzebruchTail m) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  have h : 2 * (2 + k) = (2 * k + 1) + 3 := by omega
  conv_lhs => rw [h, hirzebruchTail]
  have hev : (2 * k + 1 + 3) % 2 = 0 := by omega
  have hdiv : (2 * k + 1 + 3) / 2 = 2 + k := by omega
  rw [ite_eq_left hev, hdiv]

lemma hirzebruchTail_odd {m : ℕ} (hm : 2 ≤ m) :
    hirzebruchTail (2 * m - 1) = hirzebruchTail m ++ [2] := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
  have h : 2 * (2 + k) - 1 = (2 * k) + 3 := by omega
  conv_lhs => rw [h, hirzebruchTail]
  have hodd : ¬ ((2 * k + 3) % 2 = 0) := by omega
  have hdiv : (2 * k + 3) / 2 + 1 = 2 + k := by omega
  rw [ite_eq_right hodd, hdiv]

/-- Core structural induction (Step 3 of `PROOF.md`):
for every `n ≥ 2`, `hirzebruchTail n` is non-empty, all its entries are `≥ 2`,
`H(1) * hirzebruchProd (hirzebruchTail n) = M(n) * J`, and
`1 + (hirzebruchTail n).sum = a061313 n + 2`. -/
theorem hirzebruchTail_spec :
    ∀ n : ℕ, 2 ≤ n →
      hirzebruchTail n ≠ [] ∧
      (∀ c ∈ hirzebruchTail n, 2 ≤ c) ∧
      hirzebruchProd (1 :: hirzebruchTail n) = sbMat n * Mat2.J ∧
      (1 :: hirzebruchTail n).sum = (a061313 n : ℤ) + 2 := by
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    intro hn
    by_cases h2 : n = 2
    · subst h2
      refine ⟨by simp [hirzebruchTail_two], by simp [hirzebruchTail_two], ?_, ?_⟩
      · rw [hirzebruchTail_two, sbMat_two]
        decide
      · rw [hirzebruchTail_two, a061313_two]
        decide
    · rcases Nat.even_or_odd n with ⟨m, hm⟩ | ⟨m, hm⟩
      · have hm2 : 2 ≤ m := by omega
        have hn_eq : n = 2 * m := by omega
        obtain ⟨hne, hge, hprod, hsum⟩ := ih m (by omega) hm2
        rw [hn_eq, hirzebruchTail_even hm2, sbMat_even hm2, a061313_even (by omega)]
        refine ⟨incLast_ne_nil _ hne, incLast_ge_two _ hge, ?_, ?_⟩
        · simp only [hirzebruchProd]
          rw [hirzebruchProd_incLast _ hne, ← Mat2.mul_assoc]
          change hirzebruchProd (1 :: hirzebruchTail m) * (Mat2.Jinv * Mat2.R * Mat2.J) = _
          rw [hprod, Mat2.mul_assoc, ← Mat2.R_mul_J_eq_J_mul_conjR, ← Mat2.mul_assoc]
        · simp only [List.sum_cons] at hsum ⊢
          rw [incLast_sum _ hne]
          push_cast
          omega
      · set m' := m + 1
        have hm'2 : 2 ≤ m' := by omega
        have hn_eq : n = 2 * m' - 1 := by omega
        obtain ⟨hne, hge, hprod, hsum⟩ := ih m' (by omega) hm'2
        rw [hn_eq, hirzebruchTail_odd hm'2, sbMat_odd hm'2, a061313_two_mul_sub_one hm'2]
        refine ⟨by simp, ?_, ?_, ?_⟩
        · intro c hc
          simp only [List.mem_append, List.mem_singleton] at hc
          rcases hc with hmem | rfl
          · exact hge c hmem
          · omega
        · have hcons : (1 :: (hirzebruchTail m' ++ [2])) = (1 :: hirzebruchTail m') ++ [2] := rfl
          rw [hcons, hirzebruchProd_append, hprod]
          have hH2 : hirzebruchProd [2] = Mat2.H 2 := by simp [hirzebruchProd, Mat2.mul_one]
          rw [hH2, Mat2.mul_assoc, ← Mat2.L_mul_J_eq_J_mul_H2, ← Mat2.mul_assoc]
        · simp only [List.sum_cons, List.sum_append, List.sum_nil] at hsum ⊢
          push_cast
          omega

/-- **Main Theorem (Andrei Zabolotskii's Conjecture on OEIS `A061313`, all `n ≥ 2`):**
For every `n ≥ 2`, the Stern-Brocot fraction `r(n) = A007305(n) / A007306(n)` has a unique
canonical Hirzebruch (negative) continued fraction `cs`, and its sum of terms equals
`a061313 n + 2`. -/
theorem zabolotskii_conjecture_A061313 {n : ℕ} (hn : 2 ≤ n) :
    ∃! cs : List ℤ,
      IsCanonicalHirzebruch cs ∧
      hirzebruchEval cs = sternBrocotFrac n ∧
      cs.sum = (a061313 n : ℤ) + 2 := by
  obtain ⟨hne, hge, hprod, hsum⟩ := hirzebruchTail_spec n hn
  cases htail : hirzebruchTail n with
  | nil => exact (hne htail).elim
  | cons d tl =>
    rw [htail] at hge hprod hsum
    have hcan : IsCanonicalHirzebruch (1 :: d :: tl) := hge
    have heval_mat := hirzebruchProd_eval_canonical 1 d tl hge
    have hcol := sbMat_mul_J_first_col hn
    have heval : hirzebruchEval (1 :: d :: tl) = sternBrocotFrac n := by
      rw [← heval_mat.2, hprod, hcol.1, hcol.2]
      rfl
    refine ⟨1 :: d :: tl, ⟨hcan, heval, hsum⟩, ?_⟩
    intro cs' ⟨hcan', heval', _⟩
    exact hirzebruch_canonical_unique cs' (1 :: d :: tl) hcan' hcan (heval'.trans heval.symm)

/-- Direct universal formulation for `n ≥ 2`: ANY canonical Hirzebruch continued fraction `cs`
representing `A007305(n) / A007306(n)` has `cs.sum = a061313 n + 2`. -/
theorem zabolotskii_sum_eq {n : ℕ} (hn : 2 ≤ n) {cs : List ℤ}
    (hcan : IsCanonicalHirzebruch cs) (heval : hirzebruchEval cs = sternBrocotFrac n) :
    cs.sum = (a061313 n : ℤ) + 2 := by
  obtain ⟨cs₀, ⟨hcan₀, heval₀, hsum₀⟩, _⟩ := zabolotskii_conjecture_A061313 hn
  rw [hirzebruch_canonical_unique cs cs₀ hcan hcan₀ (heval.trans heval₀.symm)]
  exact hsum₀

/-- **Sole Boundary Exception (`n = 1`):**
At `n = 1`, `A007305(1) / A007306(1) = 1`, whose unique canonical Hirzebruch continued fraction
is `[1]` with sum `1 ≠ 2 = a061313 1 + 2`. -/
theorem zabolotskii_boundary_exception_at_one :
    (∃! cs : List ℤ, IsCanonicalHirzebruch cs ∧ hirzebruchEval cs = sternBrocotFrac 1) ∧
    (∀ cs : List ℤ, IsCanonicalHirzebruch cs → hirzebruchEval cs = sternBrocotFrac 1 →
      cs = [1] ∧ cs.sum = 1 ∧ cs.sum ≠ (a061313 1 : ℤ) + 2) := by
  have h1 : sternBrocotFrac 1 = 1 := by norm_num [sternBrocotFrac, a007305, a007306]
  have hcan1 : IsCanonicalHirzebruch [1] := by simp [IsCanonicalHirzebruch]
  have heval1 : hirzebruchEval [1] = sternBrocotFrac 1 := by simp [hirzebruchEval, h1]
  refine ⟨⟨[1], ⟨hcan1, heval1⟩, fun cs ⟨hc, he⟩ =>
    hirzebruch_canonical_unique cs [1] hc hcan1 (he.trans heval1.symm)⟩, ?_⟩
  intro cs hcan heval
  have hcs : cs = [1] := hirzebruch_canonical_unique cs [1] hcan hcan1 (heval.trans heval1.symm)
  subst hcs
  refine ⟨rfl, by simp, ?_⟩
  simp [a061313_one]

#print axioms a061313_is_min_steps
#print axioms fareyIntervals_getElem_eq_sbMat
#print axioms zabolotskii_conjecture_A061313
#print axioms zabolotskii_sum_eq
#print axioms zabolotskii_boundary_exception_at_one

end OpenMath.OeisA061313
