import Mathlib.Analysis.Real.Sqrt
import Mathlib.Basic.Complex.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Nat.Fib.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# Gullerud–Johnson–Mbirika (`arXiv:2201.08490v3`, Section 5.1, Conjecture 5.4): Counterexample `n = 8`

This file formalizes the refutation of Conjecture 5.4 (`\label{conj:ellipse}`) of
Emily Gullerud, Rita Johnson, and aBa Mbirika,
*"Tridiagonal real symmetric matrices with a connection to Pascal's triangle and the Fibonacci
sequence"* (`arXiv:2201.08490v3`, Section 5.1, lines 1171–1173):

> **Conjecture 5.4** (`conj:ellipse`). The roots of `f_n(λ) = F_{n+1}` lie on an ellipse.

Here:
- `A_n` is the `n × n` tridiagonal real symmetric matrix with `0` on the main diagonal and `1`
  on the superdiagonal and subdiagonal (`Definition 2.4`).
- `f_n(λ) = det(A_n - λ I_n)` (`Definition 2.6`), proved below to satisfy `f_0(λ) = 1`,
  `f_1(λ) = -λ`, `f_{n+2}(λ) = -λ f_{n+1}(λ) - f_n(λ)` directly from `Matrix.det`.
- `F_n = Nat.fib n` is the Fibonacci sequence (`F_0 = 0, F_1 = 1, ..., F_9 = 34`).

For `n = 8`, we prove that the complex roots of `det(A_8 - λ I_8) = F_9 = 34` do **not** lie
on any ellipse — in fact, they do not lie on **any** nontrivial real conic section
`A x^2 + B x y + C y^2 + D x + E y + F = 0` in `ℂ ≅ ℝ²`.

## Proof Outline
1. Directly from `Matrix.det`, prove `det(A_n - λ I_n) = fPoly n λ` for all `n : ℕ` via
   two-step cofactor expansion along row `0` and column `0`, yielding
   `det(A_8 - λ I_8) - 34 = (λ^2 + 1) * P(λ^2)` where `P(z) = z^3 - 8 z^2 + 23 z - 33`.
2. By the intermediate value theorem on `[4, 5]` (`P(4) = -5 < 0 < 7 = P(5)`), `P` has a real
   root `z_0 ∈ (4, 5)` and explicit non-real conjugate roots `z_1, conj z_1` with
   `Re(z_1) = 4 - z_0 / 2` and `|z_1|^2 = 33 / z_0`.
3. Taking explicit square roots produces six roots `(0, ±1)`, `(±√z_0, 0)`, `(±x_1, y_1)` of
   `det(A_8 - λ I_8) = 34` with `x_1 > 0`, `y_1 > 0`.
4. Any nontrivial real conic through these six roots must be `x^2 + z_0 y^2 = z_0`, which
   forces `Q(z_0) = 0` where `Q(z) = z(-z^2 + 13z - 8)^2 - 132(z + 1)^2`, hence `R(z_0) = 0`
   where `R(z) = 251 z^2 - 1208 z + 462`, contradicting the exact integer Bézout identity
   `(13858805 - 92031911 z) P(z) + (366661 z^2 - 1223855 z + 2309921) R(z) = 609842937`.
-/

namespace OpenMath.Gullerud220108490Conj54

/-! ## Section 1: Primary-Source Definitions (`A_n`, `f_n(λ) = det(A_n - λ I_n)`, Conics) -/

/-- The `n × n` tridiagonal matrix `A_n` with `1` on the superdiagonal and subdiagonal,
and `0` elsewhere (`Definition 2.4` of `arXiv:2201.08490v3`). -/
def tridiagMat (n : ℕ) : Matrix (Fin n) (Fin n) ℂ :=
  fun i j => if i.1 + 1 = j.1 ∨ j.1 + 1 = i.1 then 1 else 0

/-- The characteristic determinant `f_n(λ) = det(A_n - λ I_n)` (`Definition 2.6`). -/
noncomputable def tridiagDet (n : ℕ) (z : ℂ) : ℂ :=
  (tridiagMat n - z • (1 : Matrix (Fin n) (Fin n) ℂ)).det

/-- Recursive formula for `f_n(λ)`: `f_0 = 1`, `f_1 = -λ`, `f_{n+2} = -λ f_{n+1} - f_n`. -/
def fRec : ℕ → ℂ → ℂ
  | 0, _ => 1
  | 1, z => -z
  | n + 2, z => -z * fRec (n + 1) z - fRec n z

/-- A general real conic section `A x^2 + B x y + C y^2 + D x + E y + F = 0` in `ℂ ≅ ℝ²`,
strictly subsuming every ellipse (of any center, orientation, and semi-axes). -/
structure RealConic where
  A : ℝ
  B : ℝ
  C : ℝ
  D : ℝ
  E : ℝ
  F : ℝ
  nontrivial : A ≠ 0 ∨ B ≠ 0 ∨ C ≠ 0 ∨ D ≠ 0 ∨ E ≠ 0 ∨ F ≠ 0

/-- Predicate stating that `z = x + i y ∈ ℂ` lies on the real conic `K`. -/
def RealConic.Mem (K : RealConic) (z : ℂ) : Prop :=
  K.A * z.re ^ 2 + K.B * z.re * z.im + K.C * z.im ^ 2 + K.D * z.re + K.E * z.im + K.F = 0

/-- An ellipse in `ℂ ≅ ℝ²` (a real conic with positive definite quadratic form `4 A C - B^2 > 0`). -/
structure RealEllipse extends RealConic where
  elliptic : 4 * A * C - B ^ 2 > 0

/-! ## Section 2: Exact Determinant Recurrence `tridiagDet n z = fRec n z` -/

private def Mmat (n : ℕ) (z : ℂ) : Matrix (Fin n) (Fin n) ℂ :=
  tridiagMat n - z • (1 : Matrix (Fin n) (Fin n) ℂ)

private lemma Mmat_apply (n : ℕ) (z : ℂ) (i j : Fin n) :
    Mmat n z i j =
      (if i.1 + 1 = j.1 ∨ j.1 + 1 = i.1 then 1 else 0) - (if i = j then z else 0) := by
  simp [Mmat, tridiagMat, Matrix.one_apply]

private lemma Mmat_submatrix_succ (n : ℕ) (z : ℂ) :
    (Mmat (n + 1) z).submatrix Fin.succ Fin.succ = Mmat n z := by
  ext i j
  simp [Matrix.submatrix_apply, Mmat_apply, Fin.val_succ, Fin.succ_inj]

private lemma Mmat_submatrix_succ_succAbove_one (n : ℕ) (z : ℂ) :
    ((Mmat (n + 2) z).submatrix Fin.succ (Fin.succAbove (1 : Fin (n + 2)))).submatrix
        Fin.succ Fin.succ = Mmat n z := by
  ext i j
  have hs : (1 : Fin (n + 2)).succAbove j.succ = j.succ.succ := by
    apply Fin.succAbove_of_le_castSucc
    show (1 : ℕ) ≤ j.1 + 1
    omega
  simp [Matrix.submatrix_apply, hs, Mmat_apply, Fin.val_succ, Fin.succ_inj]

/-- Literal matrix determinant `det(A_n - λ I_n)` satisfies the three-term recurrence `fRec n λ`
for every `n : ℕ` and `λ ∈ ℂ`. -/
theorem tridiagDet_eq_fRec (n : ℕ) (z : ℂ) : tridiagDet n z = fRec n z := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 =>
      simp [tridiagDet, fRec, Matrix.det_isEmpty]
    | 1 =>
      simp [tridiagDet, fRec, tridiagMat]
    | k + 2 =>
      change (Mmat (k + 2) z).det = -z * fRec (k + 1) z - fRec k z
      rw [Matrix.det_succ_row_zero]
      rw [Fin.sum_univ_succ, Fin.sum_univ_succ]
      -- First term: `j = 0`, entry `(0, 0)` is `-z`, minor is `Mmat (k + 1) z`
      have hterm0 : (-1 : ℂ) ^ (0 : Fin (k + 2)).1 * Mmat (k + 2) z 0 0 *
          ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove 0)).det =
          -z * fRec (k + 1) z := by
        have h00 : Mmat (k + 2) z 0 0 = -z := by simp [Mmat_apply]
        have hsub0 : (Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove 0) = Mmat (k + 1) z := by
          ext i j
          simpa [Fin.succAbove_zero] using congrFun₂ (Mmat_submatrix_succ (k + 1) z) i j
        rw [Fin.val_zero, pow_zero, one_mul, h00, hsub0]
        exact congrArg (-z * ·) (ih (k + 1) (by omega))
      -- Second term: `j = 1`, entry `(0, 1)` is `1`, sign `-1`, minor expands along column `0` to `det(Mmat k z)`
      have hterm1 : (-1 : ℂ) ^ (Fin.succ (0 : Fin (k + 1))).1 *
          Mmat (k + 2) z 0 (Fin.succ 0) *
          ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))).det =
          -fRec k z := by
        have h01 : Mmat (k + 2) z 0 (Fin.succ 0) = 1 := by
          simp [Mmat_apply]
        have hminor1 : ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))).det =
            (Mmat k z).det := by
          rw [Matrix.det_succ_column_zero, Fin.sum_univ_succ]
          have hcol0 : ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))) 0 0 = 1 := by
            simp [Matrix.submatrix_apply, Mmat_apply]
          have hcol_rest : ∀ i : Fin k,
              ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))) i.succ 0 = 0 := by
            intro i
            have hs0 : (Fin.succ (0 : Fin (k + 1))).succAbove 0 = 0 := by
              apply Fin.succAbove_of_castSucc_lt
              show (0 : ℕ) < 1
              omega
            simp only [Matrix.submatrix_apply, hs0, Mmat_apply, Fin.val_succ, Fin.val_zero]
            have hne2 : (i.succ.succ : Fin (k + 2)) ≠ 0 := Fin.succ_ne_zero _
            simp [hne2]
          have hrest0 : ∑ i : Fin k, (-1 : ℂ) ^ i.succ.1 *
              ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))) i.succ 0 *
              (((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))).submatrix
                (Fin.succAbove i.succ) Fin.succ).det = 0 :=
            Finset.sum_eq_zero fun i _ => by rw [hcol_rest i, mul_zero, zero_mul]
          have hsub1 : ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove (Fin.succ 0))).submatrix
              (Fin.succAbove 0) Fin.succ = Mmat k z := by
            have h1eq : (Fin.succ (0 : Fin (k + 1))) = (1 : Fin (k + 2)) := by
              ext; simp
            have hsub := Mmat_submatrix_succ_succAbove_one k z
            rw [← h1eq] at hsub
            simpa [Fin.succAbove_zero] using hsub
          rw [hrest0, add_zero, Fin.val_zero, pow_zero, one_mul, hcol0, one_mul, hsub1]
        rw [Fin.val_succ, Fin.val_zero, pow_one, h01, mul_one, hminor1]
        have hih := ih k (by omega)
        change (-1 : ℂ) * tridiagDet k z = -fRec k z
        rw [hih]; ring
      -- Remaining terms `j ≥ 2` vanish since `Mmat (k + 2) z 0 j = 0`
      have hrest : ∑ j : Fin k, (-1 : ℂ) ^ j.succ.succ.1 *
          Mmat (k + 2) z 0 j.succ.succ *
          ((Mmat (k + 2) z).submatrix Fin.succ (Fin.succAbove j.succ.succ)).det = 0 := by
        refine Finset.sum_eq_zero fun j _ => ?_
        have h0j : Mmat (k + 2) z 0 j.succ.succ = 0 := by
          simp only [Mmat_apply, Fin.val_zero, Fin.val_succ]
          have h2 : (0 : Fin (k + 2)) ≠ j.succ.succ := (Fin.succ_ne_zero _).symm
          simp [h2]
        simp [h0j]
      rw [hterm0, hterm1, hrest, add_zero]
      ring

/-- Exact closed form of `f_8(λ) - F_9` in `ℂ`:
`det(A_8 - λ I_8) - F_9 = (λ^2 + 1) * ((λ^2)^3 - 8 (λ^2)^2 + 23 (λ^2) - 33)`. -/
theorem tridiagDet_eight_sub_fib9 (z : ℂ) :
    tridiagDet 8 z - (Nat.fib 9 : ℂ) =
      (z ^ 2 + 1) * ((z ^ 2) ^ 3 - 8 * (z ^ 2) ^ 2 + 23 * (z ^ 2) - 33) := by
  have hfib : Nat.fib 9 = 34 := by decide
  rw [tridiagDet_eq_fRec, hfib]
  simp only [fRec]
  push_cast
  ring

/-! ## Section 3: Existence of the Real Root `z_0 ∈ (4, 5)` and Explicit Six Roots of `f_8(λ) = 34` -/

/-- The cubic factor `P(z) = z^3 - 8 z^2 + 23 z - 33`. -/
def cubicP (z : ℝ) : ℝ := z ^ 3 - 8 * z ^ 2 + 23 * z - 33

lemma exists_cubicP_root : ∃ z₀ : ℝ, 4 < z₀ ∧ z₀ < 5 ∧ cubicP z₀ = 0 := by
  have hcont : ContinuousOn cubicP (Set.Icc 4 5) := by
    unfold cubicP
    fun_prop
  have h4 : cubicP 4 = -5 := by unfold cubicP; norm_num
  have h5 : cubicP 5 = 7 := by unfold cubicP; norm_num
  have hmem : (0 : ℝ) ∈ Set.Icc (cubicP 4) (cubicP 5) := by rw [h4, h5]; norm_num
  obtain ⟨z₀, hz₀_mem, hz₀_root⟩ := intermediate_value_Icc (by norm_num : (4 : ℝ) ≤ 5) hcont hmem
  refine ⟨z₀, ?_, ?_, hz₀_root⟩
  · rcases lt_or_eq_of_le hz₀_mem.1 with hlt | rfl
    · exact hlt
    · linarith
  · rcases lt_or_eq_of_le hz₀_mem.2 with hlt | rfl
    · exact hlt
    · linarith

/-! ## Section 4: Forced Conic Elimination and Exact Integer Bézout Contradiction -/

private lemma cubic_eval_eq_zero {a b : ℝ}
    (hre : a ^ 3 - 3 * a * b ^ 2 - 8 * (a ^ 2 - b ^ 2) + 23 * a - 33 = 0)
    (him : b * (3 * a ^ 2 - b ^ 2 - 16 * a + 23) = 0) :
    let w : ℂ := ⟨a, b⟩
    w ^ 3 - 8 * w ^ 2 + 23 * w - 33 = 0 := by
  intro w
  apply Complex.ext
  · simp [w, pow_three, pow_two]
    linear_combination hre
  · simp [w, pow_three, pow_two]
    linear_combination him

/-- **Main Refutation (stronger than Conjecture 5.4):**
The complex roots of `f_8(λ) = F_9` (`det(A_8 - λ I_8) = 34`) do not lie on **any** nontrivial
real conic section in `ℂ ≅ ℝ²`. -/
theorem no_real_conic_contains_roots_eight (K : RealConic) :
    ¬ (∀ z : ℂ, tridiagDet 8 z = (Nat.fib 9 : ℂ) → K.Mem z) := by
  intro hall
  -- Step 1: Extract real root `z₀ ∈ (4, 5)` of `P(z) = z^3 - 8z^2 + 23z - 33`
  obtain ⟨z₀, hz₀_lo, hz₀_hi, hz₀_P⟩ := exists_cubicP_root
  have hP0 : z₀ ^ 3 - 8 * z₀ ^ 2 + 23 * z₀ - 33 = 0 := hz₀_P
  have hz₀_pos : 0 < z₀ := by linarith
  -- Step 2: Show `±i` and `±√z₀` are roots of `f_8(λ) = F_9`
  have hroot_of_eq : ∀ z : ℂ,
      (z ^ 2 + 1) * ((z ^ 2) ^ 3 - 8 * (z ^ 2) ^ 2 + 23 * (z ^ 2) - 33) = 0 →
      tridiagDet 8 z = (Nat.fib 9 : ℂ) := by
    intro z hz
    have hsub := tridiagDet_eight_sub_fib9 z
    rw [hz] at hsub
    exact sub_eq_zero.mp hsub
  have hmem_pos_i : K.Mem ⟨0, 1⟩ := by
    apply hall ⟨0, 1⟩
    apply hroot_of_eq
    apply mul_eq_zero_of_left
    apply Complex.ext <;> simp [sq]
  have hmem_neg_i : K.Mem ⟨0, -1⟩ := by
    apply hall ⟨0, -1⟩
    apply hroot_of_eq
    apply mul_eq_zero_of_left
    apply Complex.ext <;> simp [sq]
  let s₀ : ℝ := Real.sqrt z₀
  have hs₀_pos : 0 < s₀ := Real.sqrt_pos.mpr hz₀_pos
  have hs₀_sq : s₀ ^ 2 = z₀ := Real.sq_sqrt hz₀_pos.le
  have hmem_pos_s₀ : K.Mem (s₀ : ℂ) := by
    apply hall (s₀ : ℂ)
    apply hroot_of_eq
    apply mul_eq_zero_of_right
    have hsqC : ((s₀ : ℂ) ^ 2) = (z₀ : ℂ) := by exact_mod_cast hs₀_sq
    rw [hsqC]
    have hcast : ((z₀ : ℂ) ^ 3 - 8 * (z₀ : ℂ) ^ 2 + 23 * (z₀ : ℂ) - 33) =
        ((z₀ ^ 3 - 8 * z₀ ^ 2 + 23 * z₀ - 33 : ℝ) : ℂ) := by push_cast; ring
    rw [hcast, hP0, Complex.ofReal_zero]
  have hmem_neg_s₀ : K.Mem ((-s₀ : ℝ) : ℂ) := by
    apply hall ((-s₀ : ℝ) : ℂ)
    apply hroot_of_eq
    apply mul_eq_zero_of_right
    have hsqR : (-s₀) ^ 2 = z₀ := by rw [neg_sq]; exact hs₀_sq
    have hsqC : (((-s₀ : ℝ) : ℂ) ^ 2) = (z₀ : ℂ) := by exact_mod_cast hsqR
    rw [hsqC]
    have hcast : ((z₀ : ℂ) ^ 3 - 8 * (z₀ : ℂ) ^ 2 + 23 * (z₀ : ℂ) - 33) =
        ((z₀ ^ 3 - 8 * z₀ ^ 2 + 23 * z₀ - 33 : ℝ) : ℂ) := by push_cast; ring
    rw [hcast, hP0, Complex.ofReal_zero]
  -- Step 3: Construct explicit non-real roots `x₁ ± i y₁` with `x₁ > 0, y₁ > 0`
  have hdisc_pos : 0 < 3 * z₀ ^ 2 - 16 * z₀ + 28 := by nlinarith
  let u : ℝ := 4 - z₀ / 2
  let v : ℝ := Real.sqrt (3 * z₀ ^ 2 - 16 * z₀ + 28) / 2
  have hv_pos : 0 < v := by dsimp [v]; positivity
  have hv_sq : v ^ 2 = (3 * z₀ ^ 2 - 16 * z₀ + 28) / 4 := by
    dsimp [v]
    rw [div_pow, Real.sq_sqrt hdisc_pos.le]
    norm_num
  have hmod_sq_eq : u ^ 2 + v ^ 2 = 33 / z₀ := by
    have hzne : z₀ ≠ 0 := hz₀_pos.ne'
    have h1 : u ^ 2 + v ^ 2 = z₀ ^ 2 - 8 * z₀ + 23 := by
      dsimp [u]; linarith [hv_sq]
    rw [h1]
    field_simp [hzne]
    linarith [hP0]
  let r : ℝ := Real.sqrt (33 / z₀)
  have hr_pos : 0 < r := Real.sqrt_pos.mpr (by positivity)
  have hr_sq : r ^ 2 = 33 / z₀ := Real.sq_sqrt (by positivity)
  have hr_gt_abs_u : |u| < r := by
    have h1 : u ^ 2 < r ^ 2 := by nlinarith [hr_sq, hmod_sq_eq, hv_pos]
    have h2 : |u| ^ 2 < r ^ 2 := by simpa [sq_abs] using h1
    nlinarith [abs_nonneg u, hr_pos]
  have hru_pos : 0 < (r + u) / 2 := by linarith [(abs_lt.mp hr_gt_abs_u).1]
  have hrmu_pos : 0 < (r - u) / 2 := by linarith [(abs_lt.mp hr_gt_abs_u).2]
  let x₁ : ℝ := Real.sqrt ((r + u) / 2)
  let y₁ : ℝ := Real.sqrt ((r - u) / 2)
  have hx₁_pos : 0 < x₁ := Real.sqrt_pos.mpr hru_pos
  have hy₁_pos : 0 < y₁ := Real.sqrt_pos.mpr hrmu_pos
  have hx₁_sq : x₁ ^ 2 = (r + u) / 2 := Real.sq_sqrt hru_pos.le
  have hy₁_sq : y₁ ^ 2 = (r - u) / 2 := Real.sq_sqrt hrmu_pos.le
  have h2xy : 2 * x₁ * y₁ = v := by
    have hsq : (2 * x₁ * y₁) ^ 2 = v ^ 2 := by
      calc (2 * x₁ * y₁) ^ 2 = 4 * x₁ ^ 2 * y₁ ^ 2 := by ring
        _ = 4 * ((r + u) / 2) * ((r - u) / 2) := by rw [hx₁_sq, hy₁_sq]
        _ = r ^ 2 - u ^ 2 := by ring
        _ = v ^ 2 := by linarith [hr_sq, hmod_sq_eq]
    exact (sq_eq_sq₀ (by positivity) hv_pos.le).mp hsq
  -- Both `(x₁, y₁)` and `(-x₁, y₁)` square to roots `⟨u, ±v⟩` of `P(z) = 0`
  have hP_uv_re : u ^ 3 - 3 * u * v ^ 2 - 8 * (u ^ 2 - v ^ 2) + 23 * u - 33 = 0 := by
    rw [hv_sq]; dsimp [u]; linear_combination hP0
  have hP_uv_im : 3 * u ^ 2 - v ^ 2 - 16 * u + 23 = 0 := by
    rw [hv_sq]; dsimp [u]; ring
  have hmem_pos_xy : K.Mem ⟨x₁, y₁⟩ := by
    apply hall ⟨x₁, y₁⟩
    apply hroot_of_eq
    apply mul_eq_zero_of_right
    have hsqC : (⟨x₁, y₁⟩ : ℂ) ^ 2 = ⟨u, v⟩ := by
      apply Complex.ext
      · simp only [sq, Complex.mul_re]; linarith [hx₁_sq, hy₁_sq]
      · simp only [sq, Complex.mul_im]; linarith [h2xy]
    rw [hsqC]
    exact cubic_eval_eq_zero hP_uv_re (by rw [hP_uv_im, mul_zero])
  have hmem_neg_xy : K.Mem ⟨-x₁, y₁⟩ := by
    apply hall ⟨-x₁, y₁⟩
    apply hroot_of_eq
    apply mul_eq_zero_of_right
    have hsqC : (⟨-x₁, y₁⟩ : ℂ) ^ 2 = ⟨u, -v⟩ := by
      apply Complex.ext
      · simp only [sq, Complex.mul_re]; linarith [hx₁_sq, hy₁_sq]
      · simp only [sq, Complex.mul_im]; linarith [h2xy]
    rw [hsqC]
    exact cubic_eval_eq_zero (by simpa [neg_sq] using hP_uv_re) (by rw [neg_sq, hP_uv_im, mul_zero])
  -- Step 4: Forced conic coefficients (`D = E = B = 0`, `F = -A z₀`, `C = A z₀`, `A ≠ 0`)
  simp only [RealConic.Mem, Complex.ofReal_re, Complex.ofReal_im] at hmem_pos_i hmem_neg_i hmem_pos_s₀ hmem_neg_s₀ hmem_pos_xy hmem_neg_xy
  have hD : K.D = 0 := by
    have h1 : 2 * s₀ * K.D = 0 := by linear_combination hmem_pos_s₀ - hmem_neg_s₀
    rcases mul_eq_zero.mp h1 with h | h
    · linarith
    · exact h
  have hF : K.F = -K.A * z₀ := by
    linear_combination hmem_pos_s₀ - s₀ * hD - K.A * hs₀_sq
  have hE : K.E = 0 := by
    linear_combination (hmem_pos_i - hmem_neg_i) / 2
  have hC : K.C = K.A * z₀ := by
    linear_combination hmem_pos_i - hE - hF
  have hB : K.B = 0 := by
    have h1 : 2 * x₁ * y₁ * K.B = 0 := by
      linear_combination hmem_pos_xy - hmem_neg_xy - 2 * x₁ * hD
    have h2xy_pos : 0 < 2 * x₁ * y₁ := by positivity
    rcases mul_eq_zero.mp h1 with h | h
    · linarith
    · exact h
  have hA : K.A ≠ 0 := by
    intro hA0
    have hC0 : K.C = 0 := by rw [hC, hA0, zero_mul]
    have hF0 : K.F = 0 := by rw [hF, hA0]; ring
    rcases K.nontrivial with h | h | h | h | h | h <;> exact h (by assumption)
  -- Hence `x₁^2 + z₀ * y₁^2 = z₀`
  have hconic : x₁ ^ 2 + z₀ * y₁ ^ 2 = z₀ := by
    have hAeq : K.A * (x₁ ^ 2 + z₀ * y₁ ^ 2 - z₀) = 0 := by
      linear_combination hmem_pos_xy - (x₁ * y₁) * hB - y₁ ^ 2 * hC - x₁ * hD - y₁ * hE - hF
    rcases mul_eq_zero.mp hAeq with h | h
    · exact absurd h hA
    · linarith
  -- Step 5: Eliminate `r = |z₁|` via `z₀ * r^2 = 33` to obtain `Q(z₀) = 0`, then `R(z₀) = 0`,
  -- and evaluate the exact integer Bézout identity to derive `0 = 609842937`!
  have hrad : 2 * (z₀ + 1) * r = -z₀ ^ 2 + 13 * z₀ - 8 := by
    dsimp [u] at hx₁_sq hy₁_sq
    linear_combination -4 * hx₁_sq - 4 * z₀ * hy₁_sq + 4 * hconic
  have hz₀r2 : z₀ * r ^ 2 = 33 := by
    rw [hr_sq]; exact mul_div_cancel₀ 33 hz₀_pos.ne'
  have hQ : z₀ * (-z₀ ^ 2 + 13 * z₀ - 8) ^ 2 - 132 * (z₀ + 1) ^ 2 = 0 := by
    calc z₀ * (-z₀ ^ 2 + 13 * z₀ - 8) ^ 2 - 132 * (z₀ + 1) ^ 2
        = z₀ * (2 * (z₀ + 1) * r) ^ 2 - 132 * (z₀ + 1) ^ 2 := by rw [← hrad]
      _ = 4 * (z₀ + 1) ^ 2 * (z₀ * r ^ 2 - 33) := by ring
      _ = 0 := by rw [hz₀r2]; ring
  have hR : 251 * z₀ ^ 2 - 1208 * z₀ + 462 = 0 := by
    linear_combination hQ - (z₀ ^ 2 - 18 * z₀ + 18) * hP0
  have hBezout : (609842937 : ℝ) = 0 := by
    linear_combination (13858805 - 92031911 * z₀) * hP0 +
      (366661 * z₀ ^ 2 - 1223855 * z₀ + 2309921) * hR
  norm_num at hBezout

/-- **Refutation of Conjecture 5.4 at `n = 8`:**
No real ellipse in `ℂ ≅ ℝ²` contains all roots of `f_8(λ) = F_9`. -/
theorem refutes_gullerud_conjecture_5_4_eight :
    ¬ ∃ E : RealEllipse, ∀ z : ℂ, tridiagDet 8 z = (Nat.fib 9 : ℂ) → E.Mem z := by
  rintro ⟨E, hE⟩
  exact no_real_conic_contains_roots_eight E.toRealConic hE

/-- **Direct Negation of Gullerud–Johnson–Mbirika (`arXiv:2201.08490v3`, Conjecture 5.4 `conj:ellipse`):**
It is false that for every `n ≥ 1`, the roots of `det(A_n - λ I_n) = F_{n+1}` lie on an ellipse. -/
theorem not_gullerud_conjecture_5_4 :
    ¬ (∀ n : ℕ, 1 ≤ n → ∃ E : RealEllipse, ∀ z : ℂ, tridiagDet n z = (Nat.fib (n + 1) : ℂ) → E.Mem z) := by
  intro hall
  exact refutes_gullerud_conjecture_5_4_eight (hall 8 (by decide))

#print axioms tridiagDet_eq_fRec
#print axioms no_real_conic_contains_roots_eight
#print axioms refutes_gullerud_conjecture_5_4_eight
#print axioms not_gullerud_conjecture_5_4

end OpenMath.Gullerud220108490Conj54
