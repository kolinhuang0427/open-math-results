import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Analysis.Real.Sqrt
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic

/-!
# Reyes–Dalfó–Fiol (`arXiv:2310.16929v1`, Section 3, Conjecture 3.2): Counterexample `G = C_6`

This file formalizes the refutation of Conjecture 3.2 (`\label{conjec-creix-alfa}`) of
M. A. Reyes, C. Dalfó, and M. A. Fiol, *"On the spectra and spectral radii of token graphs"*
(`arXiv:2310.16929v1`, Section 1 lines 182–184, Section 2.1 lines 255–267, Section 3
Definition 3.1 lines 502–505 & Conjecture 3.2 lines 542–548; also *Bol. Soc. Mat. Mex.*
30 (2024), Art. 11, `DOI:10.1007/s40590-023-00583-3`):

> **Conjecture 3.2.** For any graph `G`,
> `α₁(G) ≤ α₂(G) ≤ ⋯ ≤ α_{⌊n/2⌋}(G)`.

where `α_k(G)` is the `k`-algebraic connectivity of `G`, defined as the minimum eigenvalue
in the multiset difference `sp F_k(G) \ sp F_{k-1}(G)` of Laplacian spectra of the `k`-token
graphs `F_k(G)`.

For the connected simple 6-cycle `G = C_6` (`n = 6`, `⌊n/2⌋ = 3`), we prove from the literal
`k`-token graph and Laplacian `L = D - A` definitions via exact orthogonal integer
block-diagonalizations (avoiding any brute-force `20 × 20` determinant expansion or
`native_decide`):
- `P₀(x) = x`
- `P₁(x) = x (x - 1)² (x - 3)² (x - 4)`
- `P₂(x) = P₁(x) (x - 2) (x - 5)² (x² - 10x + 20) (x² - 7x + 8)²`
- `P₃(x) = P₂(x) (x - 4)² (x - 6) (x² - 10x + 12)`
- `α₁(C_6) = 1`, `α₂(C_6) = (7 - √17) / 2`, `α₃(C_6) = 5 - √13`
- `α₃(C_6) < α₂(C_6)` (via `9 * 17 = 153 < 169 = 13²`), refuting Conjecture 3.2.

## Main Results

* `OpenMath.Reyes231016929Conj32.charpoly_C6_token0` .. `charpoly_C6_token3`:
  Exact Laplacian characteristic polynomials of `F_0(C_6), F_1(C_6), F_2(C_6), F_3(C_6)`.
* `OpenMath.Reyes231016929Conj32.algConnK_C6_one`, `algConnK_C6_two`, `algConnK_C6_three`:
  Exact values `α₁(C_6) = 1`, `α₂(C_6) = (7 - √17)/2`, `α₃(C_6) = 5 - √13`.
* `OpenMath.Reyes231016929Conj32.refutes_reyes_conjecture_3_2_C6`:
  `C_6` is connected and `α₃(C_6) < α₂(C_6)`.
* `OpenMath.Reyes231016929Conj32.not_reyes_conjecture_3_2`:
  Direct negation of Conjecture 3.2.
-/

namespace OpenMath.Reyes231016929Conj32

open Polynomial Matrix

/-! ## Section 1: Primary-Source Definitions (`k`-Token Graph, Laplacian, `α_k(G)`) -/

/-- The `k`-token graph `F_k(G)` of a simple graph `G` on `V`: vertices are `k`-element
subsets of `V`, and two `k`-subsets `A, B` are adjacent iff their symmetric difference
`A △ B = {a, b}` is an edge `{a, b} ∈ E(G)`. -/
def tokenGraph {V : Type*} [DecidableEq V] (G : SimpleGraph V) (k : ℕ) :
    SimpleGraph { S : Finset V // S.card = k } where
  Adj A B := ∃ a b : V, G.Adj a b ∧ symmDiff A.1 B.1 = {a, b}
  symm := ⟨by
    rintro A B ⟨a, b, hab, hdiff⟩
    exact ⟨a, b, hab, by rw [symmDiff_comm]; exact hdiff⟩⟩
  loopless := ⟨by
    rintro A ⟨a, b, _, hdiff⟩
    rw [symmDiff_self, Finset.bot_eq_empty] at hdiff
    have : a ∈ (∅ : Finset V) := by rw [hdiff]; simp
    exact Finset.notMem_empty a this⟩

/-- Decidable adjacency instance for `tokenGraph G k` when `V` is finite. -/
instance tokenGraphDecidableAdj {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (k : ℕ) :
    DecidableRel (tokenGraph G k).Adj := fun A B =>
  decidable_of_iff (∃ a : V, ∃ b : V, G.Adj a b ∧ symmDiff A.1 B.1 = {a, b}) Iff.rfl

/-- Combinatorial Laplacian matrix `L(H) = D(H) - A(H)` over a ring `R`. -/
def laplacianMatrix (R : Type*) [Ring R] {W : Type*} [Fintype W] [DecidableEq W]
    (H : SimpleGraph W) [DecidableRel H.Adj] : Matrix W W R :=
  fun u v =>
    if u = v then ((H.degree u : ℕ) : R)
    else if H.Adj u v then -1 else 0

/-- The multiset of real Laplacian eigenvalues `sp(H)` of a finite simple graph `H`. -/
noncomputable def laplacianSpec {W : Type*} [Fintype W] [DecidableEq W]
    (H : SimpleGraph W) [DecidableRel H.Adj] : Multiset ℝ :=
  (laplacianMatrix ℝ H).charpoly.roots

/-- The new Laplacian eigenvalue multiset `sp(F_k(G)) \ sp(F_{k-1}(G))`. -/
noncomputable def newLayerSpec {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (k : ℕ) : Multiset ℝ :=
  laplacianSpec (tokenGraph G k) - laplacianSpec (tokenGraph G (k - 1))

/-- **Definition 3.1 (`arXiv:2310.16929v1`):** The `k`-algebraic connectivity `α_k(G)` is
the minimum eigenvalue in the multiset difference `sp F_k(G) \ sp F_{k-1}(G)` (with `0`
fallback if the multiset difference were empty). -/
noncomputable def algConnK {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (k : ℕ) : ℝ :=
  let S := (newLayerSpec G k).toFinset
  if h : S.Nonempty then S.min' h else 0

/-! ## Section 2: Generic Orthogonal Block-Diagonalization Charpoly Engine -/

/-- A `1 × 1` or `2 × 2` integer diagonal block (representing `1/scale` times the block). -/
inductive IBlock
  | b1 (a : ℤ)
  | b2 (a b c d : ℤ)

def blockSize : List IBlock → ℕ
  | [] => 0
  | .b1 _ :: rest => 1 + blockSize rest
  | .b2 _ _ _ _ :: rest => 2 + blockSize rest

/-- Block-diagonal rational matrix built recursively from scaled integer blocks `(1/scale) * B`. -/
def blockMat (scale : ℤ) : (bs : List IBlock) → Matrix (Fin (blockSize bs)) (Fin (blockSize bs)) ℚ
  | [] => Matrix.of fun i => Fin.elim0 i
  | .b1 a :: rest =>
    (Matrix.fromBlocks (!![(a : ℚ) / (scale : ℚ)] : Matrix (Fin 1) (Fin 1) ℚ) 0 0
      (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv
  | .b2 a b c d :: rest =>
    (Matrix.fromBlocks
      (!![(a : ℚ) / (scale : ℚ), (b : ℚ) / (scale : ℚ);
          (c : ℚ) / (scale : ℚ), (d : ℚ) / (scale : ℚ)] : Matrix (Fin 2) (Fin 2) ℚ) 0 0
      (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv

/-- Characteristic polynomial product of a list of scaled `1 × 1` and `2 × 2` blocks. -/
noncomputable def blockPoly (scale : ℤ) : List IBlock → Polynomial ℚ
  | [] => 1
  | .b1 a :: rest => (X - C ((a : ℚ) / (scale : ℚ))) * blockPoly scale rest
  | .b2 a b c d :: rest =>
    (X ^ 2 - C (((a + d : ℤ) : ℚ) / (scale : ℚ)) * X +
      C (((a * d - b * c : ℤ) : ℚ) / ((scale * scale : ℤ) : ℚ))) * blockPoly scale rest

private lemma charpoly_fromBlocks_zero₁₂_aux {m n : ℕ}
    (A : Matrix (Fin m) (Fin m) ℚ) (D : Matrix (Fin n) (Fin n) ℚ) :
    (Matrix.fromBlocks A (0 : Matrix (Fin m) (Fin n) ℚ) (0 : Matrix (Fin n) (Fin m) ℚ) D).charpoly =
      A.charpoly * D.charpoly := by
  unfold Matrix.charpoly
  have hcm : Matrix.charmatrix (Matrix.fromBlocks A 0 0 D) =
      Matrix.fromBlocks (Matrix.charmatrix A) 0 0 (Matrix.charmatrix D) := by
    ext i j
    cases i <;> cases j <;>
      simp [Matrix.charmatrix, Matrix.fromBlocks, Matrix.scalar_apply, Matrix.diagonal]
  rw [hcm, Matrix.det_fromBlocks_zero₁₂]

private lemma charpoly_fin1 (a : ℚ) :
    (!![a] : Matrix (Fin 1) (Fin 1) ℚ).charpoly = X - C a := by
  unfold Matrix.charpoly
  rw [Matrix.det_fin_one]
  simp [Matrix.charmatrix, Matrix.scalar_apply]

/-- Pure-integer entry lookup for the unscaled block matrix `scale * blockMat scale bs`. -/
def blockEntry : List IBlock → ℕ → ℕ → ℤ
  | [], _, _ => 0
  | .b1 a :: rest, i, j =>
    if i = 0 ∧ j = 0 then a
    else if 1 ≤ i ∧ 1 ≤ j then blockEntry rest (i - 1) (j - 1)
    else 0
  | .b2 a b c d :: rest, i, j =>
    if i = 0 ∧ j = 0 then a
    else if i = 0 ∧ j = 1 then b
    else if i = 1 ∧ j = 0 then c
    else if i = 1 ∧ j = 1 then d
    else if 2 ≤ i ∧ 2 ≤ j then blockEntry rest (i - 2) (j - 2)
    else 0

private lemma blockMat_apply (scale : ℤ) (bs : List IBlock) (i j : Fin (blockSize bs)) :
    blockMat scale bs i j = (blockEntry bs i.1 j.1 : ℚ) / (scale : ℚ) := by
  induction bs with
  | nil => exact Fin.elim0 i
  | cons hd rest ih =>
    cases hd with
    | b1 a =>
      dsimp only [blockSize] at i j
      change ((Matrix.fromBlocks (!![(a : ℚ) / (scale : ℚ)] : Matrix (Fin 1) (Fin 1) ℚ) 0 0
        (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv) i j =
        (blockEntry (.b1 a :: rest) i.1 j.1 : ℚ) / (scale : ℚ)
      obtain ⟨si, rfl⟩ := finSumFinEquiv.surjective i
      obtain ⟨sj, rfl⟩ := finSumFinEquiv.surjective j
      rw [Matrix.reindex_apply, Matrix.submatrix_apply,
        finSumFinEquiv.symm_apply_apply, finSumFinEquiv.symm_apply_apply]
      dsimp only [blockEntry]
      cases si with
      | inl i0 =>
        have hi0 : i0 = 0 := Fin.eq_zero i0; subst hi0
        cases sj with
        | inl j0 =>
          have hj0 : j0 = 0 := Fin.eq_zero j0; subst hj0
          simp [Matrix.fromBlocks, finSumFinEquiv]
        | inr j1 =>
          simp [Matrix.fromBlocks, finSumFinEquiv]
      | inr i1 =>
        cases sj with
        | inl j0 =>
          have hj0 : j0 = 0 := Fin.eq_zero j0; subst hj0
          simp [Matrix.fromBlocks, finSumFinEquiv]
        | inr j1 =>
          simp only [Matrix.fromBlocks_apply₂₂, finSumFinEquiv_apply_right, Fin.val_natAdd,
            show ¬ (1 + i1.1 = 0 ∧ 1 + j1.1 = 0) by omega,
            show 1 ≤ 1 + i1.1 ∧ 1 ≤ 1 + j1.1 by omega,
            ↓reduceIte, Nat.add_sub_cancel_left]
          exact ih i1 j1
    | b2 a b c d =>
      dsimp only [blockSize] at i j
      change ((Matrix.fromBlocks
        (!![(a : ℚ) / (scale : ℚ), (b : ℚ) / (scale : ℚ);
            (c : ℚ) / (scale : ℚ), (d : ℚ) / (scale : ℚ)] : Matrix (Fin 2) (Fin 2) ℚ) 0 0
        (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv) i j =
        (blockEntry (.b2 a b c d :: rest) i.1 j.1 : ℚ) / (scale : ℚ)
      obtain ⟨si, rfl⟩ := finSumFinEquiv.surjective i
      obtain ⟨sj, rfl⟩ := finSumFinEquiv.surjective j
      rw [Matrix.reindex_apply, Matrix.submatrix_apply,
        finSumFinEquiv.symm_apply_apply, finSumFinEquiv.symm_apply_apply]
      dsimp only [blockEntry]
      cases si with
      | inl i0 =>
        cases sj with
        | inl j0 =>
          fin_cases i0 <;> fin_cases j0 <;> simp [Matrix.fromBlocks, finSumFinEquiv]
        | inr j1 =>
          fin_cases i0 <;> simp [Matrix.fromBlocks, finSumFinEquiv, show 2 + j1.1 ≠ 1 by omega]
      | inr i1 =>
        cases sj with
        | inl j0 =>
          fin_cases j0 <;> simp [Matrix.fromBlocks, finSumFinEquiv, show 2 + i1.1 ≠ 1 by omega]
        | inr j1 =>
          simp only [Matrix.fromBlocks_apply₂₂, finSumFinEquiv_apply_right, Fin.val_natAdd,
            show ¬ (2 + i1.1 = 0 ∧ 2 + j1.1 = 0) by omega,
            show ¬ (2 + i1.1 = 0 ∧ 2 + j1.1 = 1) by omega,
            show ¬ (2 + i1.1 = 1 ∧ 2 + j1.1 = 0) by omega,
            show ¬ (2 + i1.1 = 1 ∧ 2 + j1.1 = 1) by omega,
            show 2 ≤ 2 + i1.1 ∧ 2 ≤ 2 + j1.1 by omega,
            ↓reduceIte, Nat.add_sub_cancel_left]
          exact ih i1 j1

private lemma charpoly_fin2 (a b c d : ℚ) :
    (!![a, b; c, d] : Matrix (Fin 2) (Fin 2) ℚ).charpoly =
      X ^ 2 - C (a + d) * X + C (a * d - b * c) := by
  unfold Matrix.charpoly
  rw [Matrix.det_fin_two]
  simp [Matrix.charmatrix, Matrix.scalar_apply]
  ring

/-- Exact characteristic polynomial of `blockMat scale bs` with zero large-determinant expansion! -/
lemma charpoly_blockMat (scale : ℤ) (bs : List IBlock) :
    (blockMat scale bs).charpoly = blockPoly scale bs := by
  induction bs with
  | nil =>
    change (Matrix.of (fun i : Fin 0 => Fin.elim0 i) : Matrix (Fin 0) (Fin 0) ℚ).charpoly = 1
    unfold Matrix.charpoly
    exact Matrix.det_isEmpty
  | cons hd rest ih =>
    cases hd with
    | b1 a =>
      change ((Matrix.fromBlocks (!![(a : ℚ) / (scale : ℚ)] : Matrix (Fin 1) (Fin 1) ℚ) 0 0
        (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv).charpoly =
        (X - C ((a : ℚ) / (scale : ℚ))) * blockPoly scale rest
      rw [Matrix.charpoly_reindex, charpoly_fromBlocks_zero₁₂_aux, charpoly_fin1, ih]
    | b2 a b c d =>
      change ((Matrix.fromBlocks
        (!![(a : ℚ) / (scale : ℚ), (b : ℚ) / (scale : ℚ);
            (c : ℚ) / (scale : ℚ), (d : ℚ) / (scale : ℚ)] : Matrix (Fin 2) (Fin 2) ℚ) 0 0
        (blockMat scale rest)).reindex finSumFinEquiv finSumFinEquiv).charpoly =
        (X ^ 2 - C (((a + d : ℤ) : ℚ) / (scale : ℚ)) * X +
          C (((a * d - b * c : ℤ) : ℚ) / ((scale * scale : ℤ) : ℚ))) * blockPoly scale rest
      rw [Matrix.charpoly_reindex, charpoly_fromBlocks_zero₁₂_aux, charpoly_fin2, ih]
      congr 1
      have h1 : (a : ℚ) / (scale : ℚ) + (d : ℚ) / (scale : ℚ) =
          (((a + d : ℤ) : ℚ) / (scale : ℚ)) := by push_cast; ring
      have h2 : (a : ℚ) / (scale : ℚ) * ((d : ℚ) / (scale : ℚ)) -
          (b : ℚ) / (scale : ℚ) * ((c : ℚ) / (scale : ℚ)) =
          (((a * d - b * c : ℤ) : ℚ) / ((scale * scale : ℤ) : ℚ)) := by push_cast; ring
      rw [h1, h2]

/-- Similarity invariance via an orthogonal integer matrix `P` (`Pᵀ * P = diag d`, `d i ≠ 0`)
and scaled integer relation `scale • (L * P) = P * Bint`. -/
lemma charpoly_eq_of_orth_block {n : ℕ}
    (L P : Matrix (Fin n) (Fin n) ℤ) (d : Fin n → ℤ)
    (bs : List IBlock) (hsz : blockSize bs = n)
    (scale : ℤ) (hscale : scale ≠ 0)
    (hd_pos : ∀ i : Fin n, d i ≠ 0)
    (horth : ∀ i j : Fin n, (∑ k : Fin n, P k i * P k j) = if i = j then d i else 0)
    (Bint : Matrix (Fin n) (Fin n) ℤ)
    (hBint : ∀ i j : Fin n, Bint i j - blockEntry bs i.1 j.1 = 0)
    (hinter : ∀ i j : Fin n,
      scale * (∑ k : Fin n, L i k * P k j) = ∑ k : Fin n, P i k * Bint k j) :
    (L.map (Int.castRingHom ℚ)).charpoly = blockPoly scale bs := by
  let Lq : Matrix (Fin n) (Fin n) ℚ := L.map (Int.castRingHom ℚ)
  let Pq : Matrix (Fin n) (Fin n) ℚ := P.map (Int.castRingHom ℚ)
  let Bq : Matrix (Fin n) (Fin n) ℚ :=
    (blockMat scale bs).reindex (Fin.castOrderIso hsz).toEquiv (Fin.castOrderIso hsz).toEquiv
  let Pinv : Matrix (Fin n) (Fin n) ℚ := Matrix.diagonal (fun i => (d i : ℚ)⁻¹) * Pqᵀ
  have hPinvP : Pinv * Pq = 1 := by
    dsimp only [Pinv]
    rw [Matrix.mul_assoc]
    ext i j
    rw [Matrix.diagonal_mul]
    simp only [Matrix.mul_apply, Matrix.transpose_apply,
      Matrix.one_apply, Pq, Matrix.map_apply, Int.coe_castRingHom]
    have hsum : (∑ k : Fin n, (P k i : ℚ) * (P k j : ℚ)) =
        ((∑ k : Fin n, P k i * P k j : ℤ) : ℚ) := by push_cast; rfl
    rw [hsum, horth i j]
    split_ifs with hij
    · subst hij
      have hne : (d i : ℚ) ≠ 0 := Int.cast_ne_zero.mpr (hd_pos i)
      exact inv_mul_cancel₀ hne
    · simp
  have hPPinv : Pq * Pinv = 1 := by
    have hdet : Pq.det ≠ 0 := by
      intro h0
      have h1 : (Pinv * Pq).det = 1 := by rw [hPinvP, Matrix.det_one]
      rw [Matrix.det_mul, h0, mul_zero] at h1
      exact zero_ne_one h1
    have hinv : Pq * Pq⁻¹ = 1 := Matrix.mul_nonsing_inv Pq (isUnit_iff_ne_zero.mpr hdet)
    have heq : Pinv = Pq⁻¹ := by
      calc Pinv = Pinv * 1 := (Matrix.mul_one Pinv).symm
        _ = Pinv * (Pq * Pq⁻¹) := by rw [hinv]
        _ = (Pinv * Pq) * Pq⁻¹ := (Matrix.mul_assoc _ _ _).symm
        _ = 1 * Pq⁻¹ := by rw [hPinvP]
        _ = Pq⁻¹ := Matrix.one_mul _
    rw [heq, hinv]
  have hLP : Lq * Pq = Pq * Bq := by
    ext i j
    have hsne : (scale : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hscale
    apply mul_left_cancel₀ hsne
    simp only [Lq, Pq, Bq, Matrix.mul_apply, Matrix.map_apply, Int.coe_castRingHom,
      Matrix.reindex_apply, Matrix.submatrix_apply]
    have hlhs : (scale : ℚ) * ∑ k : Fin n, (L i k : ℚ) * (P k j : ℚ) =
        ((scale * ∑ k : Fin n, L i k * P k j : ℤ) : ℚ) := by push_cast; rfl
    have hrhs : (scale : ℚ) * ∑ k : Fin n, (P i k : ℚ) *
        blockMat scale bs ((Fin.castOrderIso hsz).toEquiv.symm k) ((Fin.castOrderIso hsz).toEquiv.symm j) =
        ((∑ k : Fin n, P i k * Bint k j : ℤ) : ℚ) := by
      rw [Finset.mul_sum]
      push_cast
      refine Finset.sum_congr rfl fun k _ => ?_
      rw [blockMat_apply]
      have hk1 : ((Fin.castOrderIso hsz).toEquiv.symm k).1 = k.1 := rfl
      have hj1 : ((Fin.castOrderIso hsz).toEquiv.symm j).1 = j.1 := rfl
      have hbij : Bint k j = blockEntry bs k.1 j.1 := sub_eq_zero.mp (hBint k j)
      rw [hk1, hj1, ← hbij]
      field_simp [hsne]
    rw [hlhs, hrhs, hinter i j]
  have hsim : Bq.charpoly = Lq.charpoly := by
    calc Bq.charpoly = (1 * Bq).charpoly := by rw [Matrix.one_mul]
      _ = ((Pinv * Pq) * Bq).charpoly := by rw [hPinvP]
      _ = (Pinv * (Pq * Bq)).charpoly := by rw [Matrix.mul_assoc]
      _ = (Pinv * (Lq * Pq)).charpoly := by rw [← hLP]
      _ = ((Pinv * Lq) * Pq).charpoly := by rw [← Matrix.mul_assoc]
      _ = (Pq * (Pinv * Lq)).charpoly := Matrix.charpoly_mul_comm _ _
      _ = ((Pq * Pinv) * Lq).charpoly := by rw [← Matrix.mul_assoc]
      _ = Lq.charpoly := by rw [hPPinv, Matrix.one_mul]
  rw [← hsim]
  dsimp only [Bq]
  rw [Matrix.charpoly_reindex, charpoly_blockMat]

/-! ## Section 3: The 6-Cycle `C_6` and Its Token Graphs `F_0(C_6), F_1(C_6), F_2(C_6), F_3(C_6)` -/

/-- The 6-cycle graph `C_6` on `Fin 6` with edges `{i, i + 1 mod 6}`. -/
def C6 : SimpleGraph (Fin 6) where
  Adj u v := (u + 1 = v) ∨ (v + 1 = u)
  symm := ⟨fun _ _ h => h.symm⟩
  loopless := ⟨fun u h => by fin_cases u <;> simp at h⟩

instance : DecidableRel C6.Adj := fun u v =>
  decidable_of_iff ((u + 1 = v) ∨ (v + 1 = u)) Iff.rfl

lemma C6_connected : C6.Connected := by
  refine ⟨fun u v => ?_⟩
  have hreach0 : ∀ w : Fin 6, C6.Reachable 0 w := by
    intro w
    fin_cases w
    · exact SimpleGraph.Reachable.refl 0
    · exact SimpleGraph.Adj.reachable (Or.inl rfl)
    · exact (SimpleGraph.Adj.reachable (Or.inl rfl)).trans
        (SimpleGraph.Adj.reachable (Or.inl rfl : C6.Adj 1 2))
    · exact (SimpleGraph.Adj.reachable (Or.inl rfl : C6.Adj 0 1)).trans
        ((SimpleGraph.Adj.reachable (Or.inl rfl : C6.Adj 1 2)).trans
          (SimpleGraph.Adj.reachable (Or.inl rfl : C6.Adj 2 3)))
    · exact (SimpleGraph.Adj.reachable (Or.inr rfl : C6.Adj 0 5)).trans
        (SimpleGraph.Adj.reachable (Or.inr rfl : C6.Adj 5 4))
    · exact SimpleGraph.Adj.reachable (Or.inr rfl : C6.Adj 0 5)
  exact (hreach0 u).symm.trans (hreach0 v)

/-- Helper to read entries of an `n × n` integer table stored as a `List (List ℤ)`. -/
def matOfRows {n : ℕ} (rows : List (List ℤ)) : Matrix (Fin n) (Fin n) ℤ :=
  fun i j => (rows.getD i.1 []).getD j.1 0

/-- Helper to build a `Fin n → {S : Finset (Fin 6) // S.card = k}` bijection from an explicit list. -/
private noncomputable def mkSubEquiv {n k : ℕ} (L : List (Finset (Fin 6)))
    (_hlen : L.length = n)
    (hcard : ∀ i : Fin n, (L.getD i.1 ∅).card = k)
    (hinj : Function.Injective (fun i : Fin n => L.getD i.1 ∅))
    (hsurj : ∀ S : Finset (Fin 6), S.card = k → ∃ i : Fin n, L.getD i.1 ∅ = S) :
    Fin n ≃ { S : Finset (Fin 6) // S.card = k } :=
  Equiv.ofBijective (fun i => ⟨L.getD i.1 ∅, hcard i⟩)
    ⟨fun i j h => hinj (congrArg Subtype.val h), fun ⟨S, hS⟩ => by
      obtain ⟨i, hi⟩ := hsurj S hS
      exact ⟨i, Subtype.ext hi⟩⟩

/-- Direct fast integer Laplacian of a token graph indexed by `e : Fin n ≃ {S // S.card = k}`. -/
private noncomputable def tokenLapInt {n k : ℕ} (e : Fin n ≃ { S : Finset (Fin 6) // S.card = k }) :
    Matrix (Fin n) (Fin n) ℤ :=
  (laplacianMatrix ℤ (tokenGraph C6 k)).reindex e.symm e.symm

lemma laplacian_charpoly_rat_eq_map {n k : ℕ}
    (e : Fin n ≃ { S : Finset (Fin 6) // S.card = k }) :
    (laplacianMatrix ℝ (tokenGraph C6 k)).charpoly =
      ((tokenLapInt e).map (Int.castRingHom ℚ)).charpoly.map (Rat.castHom ℝ) := by
  have h1 : (laplacianMatrix ℝ (tokenGraph C6 k)).charpoly =
      ((laplacianMatrix ℝ (tokenGraph C6 k)).reindex e.symm e.symm).charpoly :=
    (Matrix.charpoly_reindex e.symm _).symm
  rw [h1]
  have hmap : (laplacianMatrix ℝ (tokenGraph C6 k)).reindex e.symm e.symm =
      ((tokenLapInt e).map (Int.castRingHom ℚ)).map (Rat.castHom ℝ) := by
    ext i j
    simp only [tokenLapInt, laplacianMatrix, Matrix.reindex_apply, Matrix.submatrix_apply,
      Matrix.map_apply, Int.coe_castRingHom, Rat.coe_castHom]
    split_ifs <;> simp
  rw [hmap]
  exact (Matrix.charpoly_map _ (Rat.castHom ℝ))

/-! ### `k = 0`: `F_0(C_6) ≅ K_1` (`1` vertex) -/

theorem charpoly_C6_token0 :
    (laplacianMatrix ℝ (tokenGraph C6 0)).charpoly = X := by
  let e0 : Fin 1 ≃ { S : Finset (Fin 6) // S.card = 0 } :=
    { toFun := fun _ => ⟨∅, rfl⟩
      invFun := fun _ => 0
      left_inv := fun i => (Fin.eq_zero i).symm
      right_inv := fun ⟨S, hS⟩ => Subtype.ext (Finset.card_eq_zero.mp hS).symm }
  rw [← Matrix.charpoly_reindex e0.symm]
  unfold Matrix.charpoly
  rw [Matrix.det_fin_one]
  have hdeg : (tokenGraph C6 0).degree ⟨∅, rfl⟩ = 0 := by
    rw [SimpleGraph.degree, Finset.card_eq_zero, Finset.eq_empty_iff_forall_notMem]
    intro v hv
    rw [SimpleGraph.mem_neighborFinset] at hv
    exact (tokenGraph C6 0).loopless.irrefl ⟨∅, rfl⟩
      (by rwa [show v = ⟨∅, rfl⟩ from Subtype.ext (Finset.card_eq_zero.mp v.2)] at hv)
  simp [Matrix.charmatrix, Matrix.scalar_apply, laplacianMatrix, e0, hdeg]

/-! ### `k = 1`: `F_1(C_6) ≅ C_6` (`6` vertices) -/

private def verts1 : List (Finset (Fin 6)) :=
  [{0}, {1}, {2}, {3}, {4}, {5}]

private noncomputable def e1 : Fin 6 ≃ { S : Finset (Fin 6) // S.card = 1 } :=
  mkSubEquiv verts1 rfl
    (by intro i; fin_cases i <;> decide)
    (by intro i j; fin_cases i <;> fin_cases j <;> decide)
    (by
      intro S hS
      obtain ⟨a, rfl⟩ := Finset.card_eq_one.mp hS
      fin_cases a
      · exact ⟨0, rfl⟩
      · exact ⟨1, rfl⟩
      · exact ⟨2, rfl⟩
      · exact ⟨3, rfl⟩
      · exact ⟨4, rfl⟩
      · exact ⟨5, rfl⟩)

private def L1_int : Matrix (Fin 6) (Fin 6) ℤ :=
  matOfRows
    [[ 2,-1, 0, 0, 0,-1],
     [-1, 2,-1, 0, 0, 0],
     [ 0,-1, 2,-1, 0, 0],
     [ 0, 0,-1, 2,-1, 0],
     [ 0, 0, 0,-1, 2,-1],
     [-1, 0, 0, 0,-1, 2]]

private def P1_int : Matrix (Fin 6) (Fin 6) ℤ :=
  matOfRows
    [[-1, 1,-1,-1,-1, 1],
     [ 1, 1, 1,-1,-1,-1],
     [-1, 1, 0, 2, 0,-2],
     [ 1, 1,-1,-1, 1,-1],
     [-1, 1, 1,-1, 1, 1],
     [ 1, 1, 0, 2, 0, 2]]

private def d1_vec : Fin 6 → ℤ := ![6, 6, 4, 12, 4, 12]

private def blocks1 : List IBlock :=
  [.b1 4, .b1 0, .b1 3, .b1 3, .b1 1, .b1 1]

private def B1_int : Matrix (Fin 6) (Fin 6) ℤ :=
  Matrix.diagonal ![4, 0, 3, 3, 1, 1]

private def adj1Bool (i j : Fin 6) : Bool :=
  let s1 := verts1.getD i.1 ∅
  let s2 := verts1.getD j.1 ∅
  let d := symmDiff s1 s2
  d.card == 2 &&
    (d == {0, 1} || d == {1, 2} || d == {2, 3} || d == {3, 4} || d == {4, 5} || d == {5, 0})

private lemma adj1Bool_iff (i j : Fin 6) :
    adj1Bool i j = true ↔ (tokenGraph C6 1).Adj (e1 i) (e1 j) := by
  change adj1Bool i j = true ↔
    ∃ a b : Fin 6, C6.Adj a b ∧ symmDiff (verts1.getD i.1 ∅) (verts1.getD j.1 ∅) = {a, b}
  revert i j; decide

private lemma tokenLapInt_e1_eq : tokenLapInt e1 = L1_int := by
  have hL1 : L1_int = fun i j =>
      if i = j then ((Finset.univ.filter (fun k : Fin 6 => adj1Bool i k)).card : ℤ)
      else if adj1Bool i j then -1 else 0 := by
    ext i j; fin_cases i <;> fin_cases j <;> decide
  rw [hL1]
  ext i j
  simp only [tokenLapInt, laplacianMatrix, Matrix.reindex_apply, Matrix.submatrix_apply,
    Equiv.symm_symm]
  by_cases hij : i = j
  · subst hij
    simp only [↓reduceIte]
    congr 1
    rw [SimpleGraph.degree]
    refine Finset.card_bij (fun x _ => e1.symm x) ?_ (fun _ _ _ _ h => e1.symm.injective h) ?_
    · intro x hx
      rw [SimpleGraph.mem_neighborFinset] at hx
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      exact (adj1Bool_iff i (e1.symm x)).mpr (by simpa using hx)
    · intro k hk
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hk
      exact ⟨e1 k, by rw [SimpleGraph.mem_neighborFinset]; exact (adj1Bool_iff i k).mp hk, e1.symm_apply_apply k⟩
  · have hene : e1 i ≠ e1 j := e1.injective.ne hij
    simp only [hij, hene, ↓reduceIte]
    by_cases hadj : adj1Bool i j = true
    · simp only [hadj, (adj1Bool_iff i j).mp hadj, ↓reduceIte]
    · have hnot : ¬ (tokenGraph C6 1).Adj (e1 i) (e1 j) := fun h => hadj ((adj1Bool_iff i j).mpr h)
      simp only [hadj, hnot, Bool.false_eq_true, ↓reduceIte]

theorem charpoly_C6_token1_rat :
    ((tokenLapInt e1).map (Int.castRingHom ℚ)).charpoly =
      X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) := by
  rw [tokenLapInt_e1_eq]
  have h := charpoly_eq_of_orth_block L1_int P1_int d1_vec blocks1 rfl 1 (by decide)
    (by decide)
    (by decide)
    B1_int
    (by decide)
    (by decide)
  rw [h]
  simp only [blockPoly, blocks1]
  norm_num
  simp only [map_ofNat]
  ring

theorem charpoly_C6_token1 :
    (laplacianMatrix ℝ (tokenGraph C6 1)).charpoly =
      X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) := by
  rw [laplacian_charpoly_rat_eq_map e1, charpoly_C6_token1_rat]
  simp [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_sub]

/-! ### `k = 2`: `F_2(C_6)` (`15` vertices) -/

private def verts2 : List (Finset (Fin 6)) :=
  [{0,1}, {0,2}, {0,3}, {0,4}, {0,5}, {1,2}, {1,3}, {1,4}, {1,5}, {2,3}, {2,4}, {2,5}, {3,4}, {3,5}, {4,5}]

private noncomputable def e2 : Fin 15 ≃ { S : Finset (Fin 6) // S.card = 2 } :=
  mkSubEquiv verts2 rfl
    (by intro i; fin_cases i <;> decide)
    (by intro i j; fin_cases i <;> fin_cases j <;> decide)
    (by
      intro S hS
      obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp hS
      fin_cases a <;> fin_cases b <;>
        first
        | exact absurd rfl hab
        | exact ⟨0, by decide⟩ | exact ⟨1, by decide⟩ | exact ⟨2, by decide⟩
        | exact ⟨3, by decide⟩ | exact ⟨4, by decide⟩ | exact ⟨5, by decide⟩
        | exact ⟨6, by decide⟩ | exact ⟨7, by decide⟩ | exact ⟨8, by decide⟩
        | exact ⟨9, by decide⟩ | exact ⟨10, by decide⟩ | exact ⟨11, by decide⟩
        | exact ⟨12, by decide⟩ | exact ⟨13, by decide⟩ | exact ⟨14, by decide⟩)

private def P2_int : Matrix (Fin 15) (Fin 15) ℤ :=
  matOfRows
    [[ 0, 1, 1, 1,-1,-1,-1,-3,-1, 0,-3, 0, 3, 1,-1],
     [-1, 0, 1,-1, 3, 1,-1,-1,-1, 1, 2, 0, 0, 0,-6],
     [ 0, 0, 1, 0, 0, 0,-4, 0, 0,-2, 2,-1,-2, 1, 2],
     [-1, 0, 1,-1,-3,-1,-1,-1, 1, 1, 2, 1,-1, 0, 3],
     [ 0,-1, 1, 1, 1, 1,-1,-3, 1, 0,-3, 0, 0,-2, 2],
     [ 0,-1, 1, 0,-2, 0, 2, 0,-2, 0,-3, 0,-3, 1,-1],
     [ 1, 0, 1, 1, 3,-1,-1, 1,-1, 1, 2, 1,-1, 0, 3],
     [ 0, 0, 1, 0, 0,-2, 2, 0, 0,-2, 2, 0, 0,-2,-4],
     [ 1, 0, 1,-2, 0, 0, 2,-2, 0, 1, 2,-1, 1, 0, 3],
     [ 0, 1, 1,-1,-1, 1,-1, 3,-1, 0,-3, 0, 0,-2, 2],
     [-1, 0, 1, 2, 0, 0, 2, 2, 0, 1, 2,-1, 1, 0, 3],
     [ 0, 0, 1, 0, 0, 2, 2, 0, 0,-2, 2, 1, 2, 1, 2],
     [ 0,-1, 1,-1, 1,-1,-1, 3, 1, 0,-3, 0, 3, 1,-1],
     [ 1, 0, 1, 1,-3, 1,-1, 1, 1, 1, 2, 0, 0, 0,-6],
     [ 0, 1, 1, 0, 2, 0, 2, 0, 2, 0,-3, 0,-3, 1,-1]]

private def d2_vec : Fin 15 → ℤ :=
  ![6, 6, 15, 16, 48, 16, 48, 48, 16, 18, 90, 6, 48, 18, 144]

private def blocks2 : List IBlock :=
  [.b1 12, .b1 6, .b1 0, .b1 15, .b1 15, .b1 9, .b1 9, .b1 3, .b1 3,
   .b2 20 10 2 10,
   .b2 16 8 1 5,
   .b2 8 16 2 13]

/-- `3 * blockMat blocks2` as an explicit integer `15 × 15` matrix. -/
private def B2_int : Matrix (Fin 15) (Fin 15) ℤ :=
  fun i j =>
    match i.1, j.1 with
    | 0, 0 => 12 | 1, 1 => 6  | 2, 2 => 0  | 3, 3 => 15 | 4, 4 => 15
    | 5, 5 => 9  | 6, 6 => 9  | 7, 7 => 3  | 8, 8 => 3
    | 9, 9 => 20 | 9, 10 => 10 | 10, 9 => 2 | 10, 10 => 10
    | 11, 11 => 16 | 11, 12 => 8 | 12, 11 => 1 | 12, 12 => 5
    | 13, 13 => 8 | 13, 14 => 16 | 14, 13 => 2 | 14, 14 => 13
    | _, _ => 0

/-- Direct fast-evaluating `15 × 15` integer adjacency/Laplacian matrix for `F_2(C_6)`. -/
private def adj2Bool (i j : Fin 15) : Bool :=
  let s1 := verts2.getD i.1 ∅
  let s2 := verts2.getD j.1 ∅
  let d := symmDiff s1 s2
  d.card == 2 &&
    (d == {0, 1} || d == {1, 2} || d == {2, 3} || d == {3, 4} || d == {4, 5} || d == {5, 0})

private def L2_int : Matrix (Fin 15) (Fin 15) ℤ :=
  fun i j =>
    if i = j then ((Finset.univ.filter (fun k : Fin 15 => adj2Bool i k)).card : ℤ)
    else if adj2Bool i j then -1 else 0

private lemma adj2Bool_iff (i j : Fin 15) :
    adj2Bool i j = true ↔ (tokenGraph C6 2).Adj (e2 i) (e2 j) := by
  change adj2Bool i j = true ↔
    ∃ a b : Fin 6, C6.Adj a b ∧ symmDiff (verts2.getD i.1 ∅) (verts2.getD j.1 ∅) = {a, b}
  revert i j; decide

private lemma tokenLapInt_e2_eq : tokenLapInt e2 = L2_int := by
  ext i j
  simp only [tokenLapInt, laplacianMatrix, Matrix.reindex_apply, Matrix.submatrix_apply,
    Equiv.symm_symm, L2_int]
  by_cases hij : i = j
  · subst hij
    simp only [↓reduceIte]
    congr 1
    rw [SimpleGraph.degree]
    refine Finset.card_bij (fun x _ => e2.symm x) ?_ (fun _ _ _ _ h => e2.symm.injective h) ?_
    · intro x hx
      rw [SimpleGraph.mem_neighborFinset] at hx
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      exact (adj2Bool_iff i (e2.symm x)).mpr (by simpa using hx)
    · intro k hk
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hk
      exact ⟨e2 k, by rw [SimpleGraph.mem_neighborFinset]; exact (adj2Bool_iff i k).mp hk, e2.symm_apply_apply k⟩
  · have hene : e2 i ≠ e2 j := e2.injective.ne hij
    simp only [hij, hene, ↓reduceIte]
    by_cases hadj : adj2Bool i j = true
    · simp only [hadj, (adj2Bool_iff i j).mp hadj, ↓reduceIte]
    · have hnot : ¬ (tokenGraph C6 2).Adj (e2 i) (e2 j) := fun h => hadj ((adj2Bool_iff i j).mpr h)
      simp only [hadj, hnot, Bool.false_eq_true, ↓reduceIte]

theorem charpoly_C6_token2_rat :
    ((tokenLapInt e2).map (Int.castRingHom ℚ)).charpoly =
      X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) *
      ((X - 2) * (X - 5) ^ 2 * (X ^ 2 - 10 * X + 20) * (X ^ 2 - 7 * X + 8) ^ 2) := by
  rw [tokenLapInt_e2_eq]
  have h := charpoly_eq_of_orth_block L2_int P2_int d2_vec blocks2 rfl 3 (by decide)
    (by decide)
    (by decide)
    B2_int
    (by decide)
    (by decide)
  rw [h]
  simp only [blockPoly, blocks2]
  norm_num
  simp only [map_ofNat]
  ring

theorem charpoly_C6_token2 :
    (laplacianMatrix ℝ (tokenGraph C6 2)).charpoly =
      (laplacianMatrix ℝ (tokenGraph C6 1)).charpoly *
      ((X - 2) * (X - 5) ^ 2 * (X ^ 2 - 10 * X + 20) * (X ^ 2 - 7 * X + 8) ^ 2) := by
  rw [charpoly_C6_token1, laplacian_charpoly_rat_eq_map e2, charpoly_C6_token2_rat]
  simp [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_add]

/-! ### `k = 3`: `F_3(C_6)` (`20` vertices) -/

private def verts3 : List (Finset (Fin 6)) :=
  [{0,1,2}, {0,1,3}, {0,1,4}, {0,1,5}, {0,2,3}, {0,2,4}, {0,2,5}, {0,3,4}, {0,3,5}, {0,4,5},
   {1,2,3}, {1,2,4}, {1,2,5}, {1,3,4}, {1,3,5}, {1,4,5}, {2,3,4}, {2,3,5}, {2,4,5}, {3,4,5}]

private noncomputable def e3 : Fin 20 ≃ { S : Finset (Fin 6) // S.card = 3 } :=
  mkSubEquiv verts3 rfl
    (by intro i; fin_cases i <;> decide)
    (by intro i j; fin_cases i <;> fin_cases j <;> decide)
    (by
      intro S hS
      obtain ⟨a, b, c, hab, hac, hbc, rfl⟩ := Finset.card_eq_three.mp hS
      fin_cases a <;> fin_cases b <;> fin_cases c <;>
        first
        | exact absurd rfl hab | exact absurd rfl hac | exact absurd rfl hbc
        | exact ⟨0, by decide⟩ | exact ⟨1, by decide⟩ | exact ⟨2, by decide⟩ | exact ⟨3, by decide⟩
        | exact ⟨4, by decide⟩ | exact ⟨5, by decide⟩ | exact ⟨6, by decide⟩ | exact ⟨7, by decide⟩
        | exact ⟨8, by decide⟩ | exact ⟨9, by decide⟩ | exact ⟨10, by decide⟩ | exact ⟨11, by decide⟩
        | exact ⟨12, by decide⟩ | exact ⟨13, by decide⟩ | exact ⟨14, by decide⟩ | exact ⟨15, by decide⟩
        | exact ⟨16, by decide⟩ | exact ⟨17, by decide⟩ | exact ⟨18, by decide⟩ | exact ⟨19, by decide⟩)

private def P3_int : Matrix (Fin 20) (Fin 20) ℤ :=
  matOfRows
    [[ 0, 0, 1, 0, 0, 0, 0, 0,-4, 0, 0,-5, 0, 5, 0,-7, 0, 0, 0,-2],
     [-1, 1, 1, 0, 2, 0,-2, 0,-2, 0, 0, 5,-1, 1, 1, 3, 0, 0, 2, 0],
     [ 1, 1, 1, 1,-1,-1,-1,-1,-1, 0,-4, 1, 1,-1, 1, 3, 0,-1,-1, 0],
     [ 0, 0, 1, 0, 0, 0, 0,-2,-2, 0, 4,-1, 0,-5, 0,-7, 1, 0, 0, 1],
     [ 1, 1, 1,-1,-1, 1,-1, 1,-1,-1, 1, 1, 1,-1, 1, 3, 0, 1,-1, 0],
     [ 0, 0, 1, 0, 0, 0, 0, 0, 0,-1,-3,-3,-2,-3,-6, 3, 0, 0, 0, 0],
     [-1,-1, 1,-1, 1, 1, 1,-1,-1, 0,-4, 1, 1,-1, 1, 3, 0,-1,-1, 0],
     [-1,-1, 1, 0,-2, 0,-2, 0, 2, 0, 0,-5, 1,-1, 1, 3, 0, 0, 2, 0],
     [ 1,-1, 1, 1, 1, 1,-1,-1, 1, 1,-1,-1,-1, 1, 1, 3, 0, 1,-1, 0],
     [ 0, 0, 1, 0, 0, 0, 0,-2, 2,-1, 1, 1, 0, 5, 0,-7,-1, 0, 0, 1],
     [ 0, 0, 1, 0, 0, 0, 0, 2,-2, 1,-1,-1, 0,-5, 0,-7,-1, 0, 0, 1],
     [-1,-1, 1, 1, 1,-1, 1, 1,-1,-1, 1, 1, 1,-1, 1, 3, 0, 1,-1, 0],
     [ 1,-1, 1, 0,-2, 0, 2, 0,-2, 0, 0, 5,-1, 1, 1, 3, 0, 0, 2, 0],
     [ 1,-1, 1,-1, 1,-1,-1, 1, 1, 0, 4,-1,-1, 1, 1, 3, 0,-1,-1, 0],
     [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3, 3, 2, 3,-6, 3, 0, 0, 0, 0],
     [-1, 1, 1,-1,-1,-1, 1,-1, 1, 1,-1,-1,-1, 1, 1, 3, 0, 1,-1, 0],
     [ 0, 0, 1, 0, 0, 0, 0, 2, 2, 0,-4, 1, 0, 5, 0,-7, 1, 0, 0, 1],
     [-1, 1, 1, 1,-1, 1, 1, 1, 1, 0, 4,-1,-1, 1, 1, 3, 0,-1,-1, 0],
     [ 1, 1, 1, 0, 2, 0, 2, 0, 2, 0, 0,-5, 1,-1, 1, 3, 0, 0, 2, 0],
     [ 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0,-5, 0,-7, 0, 0, 0,-2]]

private def d3_vec : Fin 20 → ℤ :=
  ![12, 12, 20, 8, 24, 8, 24, 24, 72, 8, 120, 180, 20, 180, 84, 420, 4, 8, 24, 12]

private def blocks3 : List IBlock :=
  [.b1 210, .b1 70, .b1 0, .b1 175, .b1 175, .b1 105, .b1 105, .b1 35, .b1 35, .b1 140, .b1 140, .b1 140,
   .b2 294 126 14 56,
   .b2 250 50 10 100,
   .b2 70 70 35 175,
   .b2 175 35 70 70]

/-- `35 * blockMat blocks3` as an explicit integer `20 × 20` matrix. -/
private def B3_int : Matrix (Fin 20) (Fin 20) ℤ :=
  fun i j =>
    match i.1, j.1 with
    | 0, 0 => 210 | 1, 1 => 70  | 2, 2 => 0   | 3, 3 => 175 | 4, 4 => 175
    | 5, 5 => 105 | 6, 6 => 105 | 7, 7 => 35  | 8, 8 => 35  | 9, 9 => 140
    | 10, 10 => 140 | 11, 11 => 140
    | 12, 12 => 294 | 12, 13 => 126 | 13, 12 => 14 | 13, 13 => 56
    | 14, 14 => 250 | 14, 15 => 50  | 15, 14 => 10 | 15, 15 => 100
    | 16, 16 => 70  | 16, 17 => 70  | 17, 16 => 35 | 17, 17 => 175
    | 18, 18 => 175 | 18, 19 => 35  | 19, 18 => 70 | 19, 19 => 70
    | _, _ => 0

private def adj3Bool (i j : Fin 20) : Bool :=
  let s1 := verts3.getD i.1 ∅
  let s2 := verts3.getD j.1 ∅
  let d := symmDiff s1 s2
  d.card == 2 &&
    (d == {0, 1} || d == {1, 2} || d == {2, 3} || d == {3, 4} || d == {4, 5} || d == {5, 0})

private def L3_int : Matrix (Fin 20) (Fin 20) ℤ :=
  fun i j =>
    if i = j then ((Finset.univ.filter (fun k : Fin 20 => adj3Bool i k)).card : ℤ)
    else if adj3Bool i j then -1 else 0

private lemma adj3Bool_iff (i j : Fin 20) :
    adj3Bool i j = true ↔ (tokenGraph C6 3).Adj (e3 i) (e3 j) := by
  change adj3Bool i j = true ↔
    ∃ a b : Fin 6, C6.Adj a b ∧ symmDiff (verts3.getD i.1 ∅) (verts3.getD j.1 ∅) = {a, b}
  revert i j; decide

private lemma tokenLapInt_e3_eq : tokenLapInt e3 = L3_int := by
  ext i j
  simp only [tokenLapInt, laplacianMatrix, Matrix.reindex_apply, Matrix.submatrix_apply,
    Equiv.symm_symm, L3_int]
  by_cases hij : i = j
  · subst hij
    simp only [↓reduceIte]
    congr 1
    rw [SimpleGraph.degree]
    refine Finset.card_bij (fun x _ => e3.symm x) ?_ (fun _ _ _ _ h => e3.symm.injective h) ?_
    · intro x hx
      rw [SimpleGraph.mem_neighborFinset] at hx
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      exact (adj3Bool_iff i (e3.symm x)).mpr (by simpa using hx)
    · intro k hk
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hk
      exact ⟨e3 k, by rw [SimpleGraph.mem_neighborFinset]; exact (adj3Bool_iff i k).mp hk, e3.symm_apply_apply k⟩
  · have hene : e3 i ≠ e3 j := e3.injective.ne hij
    simp only [hij, hene, ↓reduceIte]
    by_cases hadj : adj3Bool i j = true
    · simp only [hadj, (adj3Bool_iff i j).mp hadj, ↓reduceIte]
    · have hnot : ¬ (tokenGraph C6 3).Adj (e3 i) (e3 j) := fun h => hadj ((adj3Bool_iff i j).mpr h)
      simp only [hadj, hnot, Bool.false_eq_true, ↓reduceIte]

theorem charpoly_C6_token3_rat :
    ((tokenLapInt e3).map (Int.castRingHom ℚ)).charpoly =
      (X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) *
       ((X - 2) * (X - 5) ^ 2 * (X ^ 2 - 10 * X + 20) * (X ^ 2 - 7 * X + 8) ^ 2)) *
      ((X - 4) ^ 2 * (X - 6) * (X ^ 2 - 10 * X + 12)) := by
  rw [tokenLapInt_e3_eq]
  have h := charpoly_eq_of_orth_block L3_int P3_int d3_vec blocks3 rfl 35 (by decide)
    (by decide)
    (by decide)
    B3_int
    (by decide)
    (by decide)
  rw [h]
  simp only [blockPoly, blocks3]
  norm_num
  simp only [map_ofNat]
  ring

theorem charpoly_C6_token3 :
    (laplacianMatrix ℝ (tokenGraph C6 3)).charpoly =
      (laplacianMatrix ℝ (tokenGraph C6 2)).charpoly *
      ((X - 4) ^ 2 * (X - 6) * (X ^ 2 - 10 * X + 12)) := by
  rw [laplacian_charpoly_rat_eq_map e2, charpoly_C6_token2_rat,
      laplacian_charpoly_rat_eq_map e3, charpoly_C6_token3_rat]
  simp [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_add]

/-! ## Section 4: Exact Real Roots, `α₁(C_6), α₂(C_6), α₃(C_6)`, and Refutation of Conjecture 3.2 -/

private lemma roots_X_sub_C_real (a : ℝ) : (X - C a : Polynomial ℝ).roots = {a} :=
  Polynomial.roots_X_sub_C a

private lemma roots_quad_real (a b r₁ r₂ : ℝ) (hsum : r₁ + r₂ = a) (hprod : r₁ * r₂ = b) :
    (X ^ 2 - C a * X + C b : Polynomial ℝ).roots = {r₁, r₂} := by
  have hfac : (X ^ 2 - C a * X + C b : Polynomial ℝ) = (X - C r₁) * (X - C r₂) := by
    rw [← hsum, ← hprod, map_add, map_mul]
    ring
  rw [hfac, Polynomial.roots_mul (mul_ne_zero (Polynomial.X_sub_C_ne_zero r₁)
    (Polynomial.X_sub_C_ne_zero r₂)), Polynomial.roots_X_sub_C, Polynomial.roots_X_sub_C]
  rfl

private lemma roots_Q2 :
    ((X - 2) * (X - 5) ^ 2 * (X ^ 2 - 10 * X + 20) * (X ^ 2 - 7 * X + 8) ^ 2 : Polynomial ℝ).roots =
      {2, 5, 5, 5 - Real.sqrt 5, 5 + Real.sqrt 5,
       (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2,
       (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2} := by
  have hq1 : (X ^ 2 - 10 * X + 20 : Polynomial ℝ) = (X - C (5 - Real.sqrt 5)) * (X - C (5 + Real.sqrt 5)) := by
    have hsq : Real.sqrt 5 * Real.sqrt 5 = 5 := Real.mul_self_sqrt (by norm_num)
    have hprod : (5 - Real.sqrt 5) * (5 + Real.sqrt 5) = 20 := by nlinarith
    have hsum : (5 - Real.sqrt 5) + (5 + Real.sqrt 5) = 10 := by ring
    have hCp : C (5 - Real.sqrt 5) * C (5 + Real.sqrt 5) = C 20 := by rw [← map_mul, hprod]
    have hCs : C (5 - Real.sqrt 5) + C (5 + Real.sqrt 5) = C 10 := by rw [← map_add, hsum]
    have h10 : (10 : Polynomial ℝ) = C 10 := rfl
    have h20 : (20 : Polynomial ℝ) = C 20 := rfl
    rw [h10, h20, ← hCs, ← hCp]
    ring
  have hq2 : (X ^ 2 - 7 * X + 8 : Polynomial ℝ) =
      (X - C ((7 - Real.sqrt 17) / 2)) * (X - C ((7 + Real.sqrt 17) / 2)) := by
    have hsq : Real.sqrt 17 * Real.sqrt 17 = 17 := Real.mul_self_sqrt (by norm_num)
    have hprod : ((7 - Real.sqrt 17) / 2) * ((7 + Real.sqrt 17) / 2) = 8 := by nlinarith
    have hsum : ((7 - Real.sqrt 17) / 2) + ((7 + Real.sqrt 17) / 2) = 7 := by ring
    have hCp : C ((7 - Real.sqrt 17) / 2) * C ((7 + Real.sqrt 17) / 2) = C 8 := by rw [← map_mul, hprod]
    have hCs : C ((7 - Real.sqrt 17) / 2) + C ((7 + Real.sqrt 17) / 2) = C 7 := by rw [← map_add, hsum]
    have h7 : (7 : Polynomial ℝ) = C 7 := rfl
    have h8 : (8 : Polynomial ℝ) = C 8 := rfl
    rw [h7, h8, ← hCs, ← hCp]
    ring
  have h2 : (X - 2 : Polynomial ℝ) = X - C 2 := rfl
  have h5 : (X - 5 : Polynomial ℝ) = X - C 5 := rfl
  rw [h2, h5, hq1, hq2]
  have hne : ∀ a : ℝ, (X - C a : Polynomial ℝ) ≠ 0 := Polynomial.X_sub_C_ne_zero
  have hA : (X - C 2 : Polynomial ℝ) * (X - C 5) ^ 2 ≠ 0 :=
    mul_ne_zero (hne _) (pow_ne_zero 2 (hne _))
  have hB : (X - C (5 - Real.sqrt 5) : Polynomial ℝ) * (X - C (5 + Real.sqrt 5)) ≠ 0 :=
    mul_ne_zero (hne _) (hne _)
  have hC : ((X - C ((7 - Real.sqrt 17) / 2) : Polynomial ℝ) * (X - C ((7 + Real.sqrt 17) / 2))) ^ 2 ≠ 0 :=
    pow_ne_zero 2 (mul_ne_zero (hne _) (hne _))
  rw [Polynomial.roots_mul (mul_ne_zero (mul_ne_zero hA hB) hC),
      Polynomial.roots_mul (mul_ne_zero hA hB),
      Polynomial.roots_mul hA,
      Polynomial.roots_mul hB,
      Polynomial.roots_pow, Polynomial.roots_pow,
      Polynomial.roots_mul (mul_ne_zero (hne _) (hne _))]
  simp only [Polynomial.roots_X_sub_C, two_nsmul, Multiset.insert_eq_cons, ← Multiset.singleton_add]
  abel

private lemma roots_Q3 :
    ((X - 4) ^ 2 * (X - 6) * (X ^ 2 - 10 * X + 12) : Polynomial ℝ).roots =
      {4, 4, 6, 5 - Real.sqrt 13, 5 + Real.sqrt 13} := by
  have hq : (X ^ 2 - 10 * X + 12 : Polynomial ℝ) =
      (X - C (5 - Real.sqrt 13)) * (X - C (5 + Real.sqrt 13)) := by
    have hsq : Real.sqrt 13 * Real.sqrt 13 = 13 := Real.mul_self_sqrt (by norm_num)
    have hprod : (5 - Real.sqrt 13) * (5 + Real.sqrt 13) = 12 := by nlinarith
    have hsum : (5 - Real.sqrt 13) + (5 + Real.sqrt 13) = 10 := by ring
    have hCp : C (5 - Real.sqrt 13) * C (5 + Real.sqrt 13) = C 12 := by rw [← map_mul, hprod]
    have hCs : C (5 - Real.sqrt 13) + C (5 + Real.sqrt 13) = C 10 := by rw [← map_add, hsum]
    have h10 : (10 : Polynomial ℝ) = C 10 := rfl
    have h12 : (12 : Polynomial ℝ) = C 12 := rfl
    rw [h10, h12, ← hCs, ← hCp]
    ring
  have h4 : (X - 4 : Polynomial ℝ) = X - C 4 := rfl
  have h6 : (X - 6 : Polynomial ℝ) = X - C 6 := rfl
  rw [h4, h6, hq]
  have hne : ∀ a : ℝ, (X - C a : Polynomial ℝ) ≠ 0 := Polynomial.X_sub_C_ne_zero
  rw [Polynomial.roots_mul (mul_ne_zero (mul_ne_zero (pow_ne_zero 2 (hne _)) (hne _))
    (mul_ne_zero (hne _) (hne _))),
    Polynomial.roots_mul (mul_ne_zero (pow_ne_zero 2 (hne _)) (hne _)),
    Polynomial.roots_pow,
    Polynomial.roots_mul (mul_ne_zero (hne _) (hne _))]
  simp only [Polynomial.roots_X_sub_C, two_nsmul, Multiset.insert_eq_cons, ← Multiset.singleton_add]
  abel

private lemma charpoly_ne_zero_of_monic {W : Type*} [Fintype W] [DecidableEq W]
    (M : Matrix W W ℝ) : M.charpoly ≠ 0 :=
  M.charpoly_monic.ne_zero

theorem newLayerSpec_C6_one :
    newLayerSpec C6 1 = {1, 1, 3, 3, 4} := by
  unfold newLayerSpec laplacianSpec
  rw [charpoly_C6_token1, charpoly_C6_token0]
  have h1 : (X - 1 : Polynomial ℝ) = X - C 1 := rfl
  have h3 : (X - 3 : Polynomial ℝ) = X - C 3 := rfl
  have h4 : (X - 4 : Polynomial ℝ) = X - C 4 := rfl
  have hne : ∀ a : ℝ, (X - C a : Polynomial ℝ) ≠ 0 := Polynomial.X_sub_C_ne_zero
  have hmul : (X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) : Polynomial ℝ).roots =
      (X : Polynomial ℝ).roots + ((X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) : Polynomial ℝ).roots := by
    have hassoc : (X * (X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4) : Polynomial ℝ) =
        X * ((X - 1) ^ 2 * (X - 3) ^ 2 * (X - 4)) := by ring
    rw [hassoc, Polynomial.roots_mul]
    rw [h1, h3, h4]
    exact mul_ne_zero Polynomial.X_ne_zero
      (mul_ne_zero (mul_ne_zero (pow_ne_zero 2 (hne 1)) (pow_ne_zero 2 (hne 3))) (hne 4))
  rw [hmul, add_tsub_cancel_left, h1, h3, h4]
  rw [Polynomial.roots_mul (mul_ne_zero (mul_ne_zero (pow_ne_zero 2 (hne 1)) (pow_ne_zero 2 (hne 3))) (hne 4)),
      Polynomial.roots_mul (mul_ne_zero (pow_ne_zero 2 (hne 1)) (pow_ne_zero 2 (hne 3))),
      Polynomial.roots_pow, Polynomial.roots_pow]
  simp only [Polynomial.roots_X_sub_C, two_nsmul, Multiset.insert_eq_cons, ← Multiset.singleton_add]
  abel

theorem newLayerSpec_C6_two :
    newLayerSpec C6 2 =
      {2, 5, 5, 5 - Real.sqrt 5, 5 + Real.sqrt 5,
       (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2,
       (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2} := by
  unfold newLayerSpec laplacianSpec
  have hne1 := charpoly_ne_zero_of_monic (laplacianMatrix ℝ (tokenGraph C6 1))
  have hneQ : ((X - 2) * (X - 5) ^ 2 * (X ^ 2 - 10 * X + 20) * (X ^ 2 - 7 * X + 8) ^ 2 : Polynomial ℝ) ≠ 0 := by
    intro h0
    have := congrArg Polynomial.roots h0
    rw [roots_Q2, Polynomial.roots_zero] at this
    exact Multiset.cons_ne_zero this
  rw [charpoly_C6_token2, Polynomial.roots_mul (mul_ne_zero hne1 hneQ), add_tsub_cancel_left, roots_Q2]

theorem newLayerSpec_C6_three :
    newLayerSpec C6 3 = {4, 4, 6, 5 - Real.sqrt 13, 5 + Real.sqrt 13} := by
  unfold newLayerSpec laplacianSpec
  have hne2 := charpoly_ne_zero_of_monic (laplacianMatrix ℝ (tokenGraph C6 2))
  have hneQ : ((X - 4) ^ 2 * (X - 6) * (X ^ 2 - 10 * X + 12) : Polynomial ℝ) ≠ 0 := by
    intro h0
    have := congrArg Polynomial.roots h0
    rw [roots_Q3, Polynomial.roots_zero] at this
    exact Multiset.cons_ne_zero this
  rw [charpoly_C6_token3, Polynomial.roots_mul (mul_ne_zero hne2 hneQ), add_tsub_cancel_left, roots_Q3]

/-- `α₁(C_6) = 1`. -/
theorem algConnK_C6_one : algConnK C6 1 = 1 := by
  unfold algConnK
  rw [newLayerSpec_C6_one]
  have hne : ({1, 1, 3, 3, 4} : Multiset ℝ).toFinset.Nonempty := ⟨1, by simp⟩
  rw [dite_eq_left hne]
  apply le_antisymm
  · exact Finset.min'_le _ 1 (by simp)
  · apply Finset.le_min'
    intro y hy
    simp only [Multiset.mem_toFinset, Multiset.insert_eq_cons, Multiset.mem_cons,
      Multiset.mem_singleton] at hy
    rcases hy with rfl | rfl | rfl | rfl | rfl <;> norm_num

/-- `α₂(C_6) = (7 - √17) / 2`. -/
theorem algConnK_C6_two : algConnK C6 2 = (7 - Real.sqrt 17) / 2 := by
  unfold algConnK
  rw [newLayerSpec_C6_two]
  have hne : ({2, 5, 5, 5 - Real.sqrt 5, 5 + Real.sqrt 5,
      (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2,
      (7 - Real.sqrt 17) / 2, (7 + Real.sqrt 17) / 2} : Multiset ℝ).toFinset.Nonempty :=
    ⟨2, by simp⟩
  rw [dite_eq_left hne]
  have h17_gt_3 : (3 : ℝ) < Real.sqrt 17 := by
    rw [← Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 3)]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have h5_lt_3 : Real.sqrt 5 < (3 : ℝ) := by
    rw [← Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 3)]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have h5_nonneg : (0 : ℝ) ≤ Real.sqrt 5 := Real.sqrt_nonneg 5
  have h17_nonneg : (0 : ℝ) ≤ Real.sqrt 17 := Real.sqrt_nonneg 17
  apply le_antisymm
  · exact Finset.min'_le _ ((7 - Real.sqrt 17) / 2) (by simp)
  · apply Finset.le_min'
    intro y hy
    simp only [Multiset.mem_toFinset, Multiset.insert_eq_cons, Multiset.mem_cons,
      Multiset.mem_singleton] at hy
    rcases hy with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> linarith

/-- `α₃(C_6) = 5 - √13`. -/
theorem algConnK_C6_three : algConnK C6 3 = 5 - Real.sqrt 13 := by
  unfold algConnK
  rw [newLayerSpec_C6_three]
  have hne : ({4, 4, 6, 5 - Real.sqrt 13, 5 + Real.sqrt 13} : Multiset ℝ).toFinset.Nonempty :=
    ⟨4, by simp⟩
  rw [dite_eq_left hne]
  have h13_gt_1 : (1 : ℝ) < Real.sqrt 13 := by
    rw [← Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 1)]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have h13_nonneg : (0 : ℝ) ≤ Real.sqrt 13 := Real.sqrt_nonneg 13
  apply le_antisymm
  · exact Finset.min'_le _ (5 - Real.sqrt 13) (by simp)
  · apply Finset.le_min'
    intro y hy
    simp only [Multiset.mem_toFinset, Multiset.insert_eq_cons, Multiset.mem_cons,
      Multiset.mem_singleton] at hy
    rcases hy with rfl | rfl | rfl | rfl | rfl <;> linarith

/-- Pure algebraic proof that `5 - √13 < (7 - √17) / 2` (from `9 * 17 = 153 < 169 = 13²`). -/
theorem alpha3_lt_alpha2_C6 : algConnK C6 3 < algConnK C6 2 := by
  rw [algConnK_C6_three, algConnK_C6_two]
  have h17_sq : Real.sqrt 17 ^ 2 = 17 := Real.sq_sqrt (by norm_num)
  have h13_sq : Real.sqrt 13 ^ 2 = 13 := Real.sq_sqrt (by norm_num)
  have h17_pos : 0 < Real.sqrt 17 := Real.sqrt_pos.mpr (by norm_num)
  have h13_pos : 0 < Real.sqrt 13 := Real.sqrt_pos.mpr (by norm_num)
  have hstep1 : 3 * Real.sqrt 17 < 13 := by nlinarith
  have hstep2 : (3 + Real.sqrt 17) ^ 2 < (2 * Real.sqrt 13) ^ 2 := by nlinarith
  have hstep3 : 3 + Real.sqrt 17 < 2 * Real.sqrt 13 := by nlinarith
  linarith

/-- **Explicit Counterexample Witness:** `G = C_6` is a connected simple graph on `6` vertices
with `α₃(C_6) < α₂(C_6)`, refuting Conjecture 3.2. -/
theorem refutes_reyes_conjecture_3_2_C6 :
    C6.Connected ∧ algConnK C6 3 < algConnK C6 2 :=
  ⟨C6_connected, alpha3_lt_alpha2_C6⟩

/-- **Refutation of Reyes–Dalfó–Fiol (`arXiv:2310.16929v1`, Section 3, Conjecture 3.2):**
It is false that every connected simple graph `G` on `n` vertices satisfies
`α_{k₁}(G) ≤ α_{k₂}(G)` for all `1 ≤ k₁ ≤ k₂ ≤ ⌊n / 2⌋`. -/
theorem not_reyes_conjecture_3_2 :
    ¬ (∀ (n : ℕ) (G : SimpleGraph (Fin n)) [DecidableRel G.Adj], G.Connected →
        ∀ k₁ k₂ : ℕ, 1 ≤ k₁ → k₁ ≤ k₂ → k₂ ≤ n / 2 → algConnK G k₁ ≤ algConnK G k₂) := by
  intro hconj
  have hle : algConnK C6 2 ≤ algConnK C6 3 :=
    hconj 6 C6 C6_connected 2 3 (by decide) (by decide) (by decide)
  exact not_lt.mpr hle alpha3_lt_alpha2_C6

#print axioms charpoly_C6_token0
#print axioms charpoly_C6_token1
#print axioms charpoly_C6_token2
#print axioms charpoly_C6_token3
#print axioms algConnK_C6_one
#print axioms algConnK_C6_two
#print axioms algConnK_C6_three
#print axioms refutes_reyes_conjecture_3_2_C6
#print axioms not_reyes_conjecture_3_2

end OpenMath.Reyes231016929Conj32
