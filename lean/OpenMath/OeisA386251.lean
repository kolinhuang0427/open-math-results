import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Data.Int.GCD
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

/-!
# Refutation of the OEIS A386251 3-Segment Closed Walk Conjecture

Primary source:
OEIS **A386251** (Charles L. Hohn, rev. 22, 2025-08-06):
- Name: *"Consider the graph whose vertices are the points of the n-dimensional cubic lattice with
  points connected by all integer-length diagonals that traverse all n dimensions and do not
  intersect intermediate points. a(n) is the total length of the shortest possible closed walk in
  this graph via noncongruent diagonals."*
- Conjecture (Comment): *"It is provable that all such walks must be even in total length. It is
  also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n)
  for all n >= 6 are produced by 3-segment walks."*

We refute this conjecture for the entire infinite family `n = m^2 - 30` (`m ≥ 92`, smallest
instance `m = 92`, `n = 8434`):
1. We construct an explicit valid 4-segment closed walk (in fact a simple 4-cycle) of total
   Euclidean length `4 * m` (`368` at `n = 8434`).
2. We prove every valid 3-segment closed walk has total length `≥ 4 * m + 2` (`≥ 370` at `n = 8434`).
3. We prove `a(m^2 - 30) = 4 * m` for all `m ≥ 92`, so `a(n)` is never achieved by a 3-segment walk.
-/

namespace OpenMath.OeisA386251

open scoped BigOperators

/-! ## Section 1: Exact Primary-Source Definitions -/

/-- A lattice vector `v : Fin n → ℤ` is a valid diagonal of Euclidean length `L` if:
1. It traverses all `n` dimensions (`∀ i, v i ≠ 0`),
2. It does not intersect intermediate lattice points (primitive: no `d ≥ 2` divides all coordinates),
3. Its squared Euclidean norm equals `L^2` (`L > 0`). -/
def ValidDiagonal {n : ℕ} (v : Fin n → ℤ) (L : ℕ) : Prop :=
  0 < L ∧
  (∀ i : Fin n, v i ≠ 0) ∧
  (∀ d : ℕ, (∀ i : Fin n, d ∣ (v i).natAbs) → d = 1) ∧
  ∑ i : Fin n, (v i) ^ 2 = (L : ℤ) ^ 2

/-- Two diagonals `u, v : Fin n → ℤ` are congruent under the cubic lattice symmetry group `B_n`
iff one is a signed coordinate permutation of the other (equivalently, equal coordinate-magnitude
multisets). -/
def AreCongruent {n : ℕ} (u v : Fin n → ℤ) : Prop :=
  ∃ σ : Equiv.Perm (Fin n), ∀ i : Fin n, (v i).natAbs = (u (σ i)).natAbs

/-- A valid `k`-segment closed walk via pairwise noncongruent diagonals in `ℤ^n`. -/
structure ClosedWalk (n k : ℕ) where
  steps : Fin k → Fin n → ℤ
  lengths : Fin k → ℕ
  hk : 0 < k
  closed : ∀ i : Fin n, ∑ j : Fin k, steps j i = 0
  valid : ∀ j : Fin k, ValidDiagonal (steps j) (lengths j)
  noncongruent : ∀ j₁ j₂ : Fin k, j₁ ≠ j₂ → ¬ AreCongruent (steps j₁) (steps j₂)

/-- Total Euclidean length of a closed walk. -/
def ClosedWalk.totalLength {n k : ℕ} (W : ClosedWalk n k) : ℕ :=
  ∑ j : Fin k, W.lengths j

/-- `a(n)`: minimum total length over all valid closed walks in `ℤ^n`. -/
noncomputable def a386251 (n : ℕ) : ℕ :=
  sInf {L : ℕ | ∃ (k : ℕ) (W : ClosedWalk n k), W.totalLength = L}

/-! ## Section 2: Explicit 4-Segment Witness (Simple 4-Cycle) for `n = m^2 - 30` (`m ≥ 92`) -/

/-- Coordinate function `witnessStepVal j v` for `j : Fin 4`, `v : ℕ`. -/
def witnessStepVal (j : Fin 4) (v : ℕ) : ℤ :=
  match j, v with
  | 0, 0 => -2
  | 0, 1 | 0, 2 | 0, 3 => -2
  | 0, 4 | 0, 5 | 0, 6 | 0, 7 | 0, 8 | 0, 9 => 2
  | 0, _ => 1
  | 1, 0 => -4
  | 1, 1 | 1, 2 | 1, 3 | 1, 4 | 1, 5 => -2
  | 1, 6 | 1, 7 | 1, 8 | 1, 9 => -1
  | 1, _ => 1
  | 2, 0 => 1
  | 2, 1 | 2, 2 | 2, 3 => 3
  | 2, 4 | 2, 5 => -1
  | 2, 6 | 2, 7 => -2
  | 2, 8 | 2, 9 => 1
  | 2, _ => -1
  | 3, 0 => 5
  | 3, 1 | 3, 2 | 3, 3 | 3, 4 | 3, 5 | 3, 6 | 3, 7 => 1
  | 3, 8 | 3, 9 => -2
  | 3, _ => -1

/-- The four step vectors `v^{(1)}, v^{(2)}, v^{(3)}, v^{(4)} ∈ ℤ^n` (`n ≥ 11`). -/
def witnessStep {n : ℕ} (j : Fin 4) (i : Fin n) : ℤ :=
  witnessStepVal j i.val

lemma witnessStepVal_closed_lt10 : ∀ k : Fin 10, ∑ j : Fin 4, witnessStepVal j k.val = 0 := by
  decide

lemma witnessStep_closed {n : ℕ} (i : Fin n) :
    ∑ j : Fin 4, witnessStep j i = 0 := by
  change ∑ j : Fin 4, witnessStepVal j i.val = 0
  by_cases h10 : i.val < 10
  · exact witnessStepVal_closed_lt10 ⟨i.val, h10⟩
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le' (by omega : 10 ≤ i.val)
    rw [hk, Fin.sum_univ_four]
    simp [witnessStepVal]

lemma witnessStepVal_ne_zero_lt10 : ∀ (j : Fin 4) (k : Fin 10), witnessStepVal j k.val ≠ 0 := by
  decide

lemma witnessStep_ne_zero {n : ℕ} (j : Fin 4) (i : Fin n) : witnessStep j i ≠ 0 := by
  change witnessStepVal j i.val ≠ 0
  by_cases h10 : i.val < 10
  · exact witnessStepVal_ne_zero_lt10 j ⟨i.val, h10⟩
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le' (by omega : 10 ≤ i.val)
    rw [hk]
    match j with
    | 0 | 1 | 2 | 3 => simp [witnessStepVal]

lemma witnessStep_primitive {n : ℕ} (hn : 11 ≤ n) (j : Fin 4) :
    ∀ d : ℕ, (∀ i : Fin n, d ∣ (witnessStep j i).natAbs) → d = 1 := by
  intro d hd
  have h10 := hd ⟨10, by omega⟩
  have habs : ∀ j' : Fin 4, (witnessStepVal j' 10).natAbs = 1 := by decide
  change d ∣ (witnessStepVal j 10).natAbs at h10
  rw [habs j] at h10
  exact Nat.eq_one_of_dvd_one h10

lemma witnessStepVal_head_sum :
    ∀ j : Fin 4, ∑ k : Fin 10, ((witnessStepVal j k.val) ^ 2 - 1) = 30 := by
  decide

lemma witnessStep_norm_sq {n : ℕ} (hn : 10 ≤ n) (j : Fin 4) :
    ∑ i : Fin n, (witnessStep j i) ^ 2 = (n : ℤ) + 30 := by
  have htail : ∀ i : Fin n, 10 ≤ i.val → (witnessStep j i) ^ 2 = 1 := by
    intro ⟨v, hv⟩ h10
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le' h10
    change (witnessStepVal j (k + 10)) ^ 2 = 1
    match j with
    | 0 | 1 | 2 | 3 => simp [witnessStepVal]
  have hdiff : ∑ i : Fin n, ((witnessStep j i) ^ 2 - 1) = 30 := by
    let head : Finset (Fin n) := Finset.univ.filter (fun i => i.val < 10)
    have hzero : ∀ i ∈ Finset.univ, i ∉ head → (witnessStep j i) ^ 2 - 1 = 0 := by
      intro i _ hi
      simp only [head, Finset.mem_filter, Finset.mem_univ, true_and, not_lt] at hi
      rw [htail i hi, sub_self]
    rw [← Finset.sum_subset (Finset.subset_univ head) hzero]
    have hbij : ∑ i ∈ head, ((witnessStep j i) ^ 2 - 1) =
        ∑ k : Fin 10, ((witnessStepVal j k.val) ^ 2 - 1) := by
      refine Finset.sum_bij (fun i hi => (⟨i.val, (Finset.mem_filter.mp hi).2⟩ : Fin 10))
        (fun _ _ => Finset.mem_univ _)
        (fun i₁ _ i₂ _ h => Fin.ext (Fin.mk.inj h))
        (fun k _ => ⟨⟨k.val, by omega⟩, Finset.mem_filter.mpr ⟨Finset.mem_univ _, k.isLt⟩, rfl⟩)
        (fun _ _ => rfl)
    rw [hbij]
    exact witnessStepVal_head_sum j
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    nsmul_eq_mul, mul_one] at hdiff
  linarith

lemma witnessStepVal_no4_lt10 :
    ∀ (j : Fin 4) (k : Fin 10), j ≠ 1 → (witnessStepVal j k.val).natAbs ≠ 4 := by
  decide

lemma witnessStepVal_no3_lt10 :
    ∀ (j : Fin 4) (k : Fin 10), j ≠ 2 → (witnessStepVal j k.val).natAbs ≠ 3 := by
  decide

lemma witnessStepVal_no5_lt10 :
    ∀ (j : Fin 4) (k : Fin 10), j ≠ 3 → (witnessStepVal j k.val).natAbs ≠ 5 := by
  decide

lemma witnessStep_noncongruent {n : ℕ} (hn : 10 ≤ n) (j₁ j₂ : Fin 4) (hne : j₁ ≠ j₂) :
    ¬ AreCongruent (witnessStep (n := n) j₁) (witnessStep (n := n) j₂) := by
  have hno4 : ∀ (j : Fin 4), j ≠ 1 → ∀ i : Fin n, (witnessStep j i).natAbs ≠ 4 := by
    intro j hj i
    change (witnessStepVal j i.val).natAbs ≠ 4
    by_cases h10 : i.val < 10
    · exact witnessStepVal_no4_lt10 j ⟨i.val, h10⟩ hj
    · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le' (by omega : 10 ≤ i.val)
      rw [hk]
      match j with
      | 0 | 2 | 3 => simp [witnessStepVal]
      | 1 => exact absurd rfl hj
  have hno3 : ∀ (j : Fin 4), j ≠ 2 → ∀ i : Fin n, (witnessStep j i).natAbs ≠ 3 := by
    intro j hj i
    change (witnessStepVal j i.val).natAbs ≠ 3
    by_cases h10 : i.val < 10
    · exact witnessStepVal_no3_lt10 j ⟨i.val, h10⟩ hj
    · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le' (by omega : 10 ≤ i.val)
      rw [hk]
      match j with
      | 0 | 1 | 3 => simp [witnessStepVal]
      | 2 => exact absurd rfl hj
  have hno5 : ∀ (j : Fin 4), j ≠ 3 → ∀ i : Fin n, (witnessStep j i).natAbs ≠ 5 := by
    intro j hj i
    change (witnessStepVal j i.val).natAbs ≠ 5
    by_cases h10 : i.val < 10
    · exact witnessStepVal_no5_lt10 j ⟨i.val, h10⟩ hj
    · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le' (by omega : 10 ≤ i.val)
      rw [hk]
      match j with
      | 0 | 1 | 2 => simp [witnessStepVal]
      | 3 => exact absurd rfl hj
  rintro ⟨σ, hσ⟩
  have hv1 : (witnessStep (n := n) 1 ⟨0, by omega⟩).natAbs = 4 := rfl
  have hv2 : (witnessStep (n := n) 2 ⟨1, by omega⟩).natAbs = 3 := rfl
  have hv3 : (witnessStep (n := n) 3 ⟨0, by omega⟩).natAbs = 5 := rfl
  match j₁, j₂ with
  | 0, 1 => exact hno4 0 (by decide) (σ ⟨0, by omega⟩) ((hσ ⟨0, by omega⟩).symm.trans hv1)
  | 1, 0 =>
    have h := hσ (σ.symm ⟨0, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno4 0 (by decide) (σ.symm ⟨0, by omega⟩) (h.trans hv1)
  | 0, 2 => exact hno3 0 (by decide) (σ ⟨1, by omega⟩) ((hσ ⟨1, by omega⟩).symm.trans hv2)
  | 2, 0 =>
    have h := hσ (σ.symm ⟨1, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno3 0 (by decide) (σ.symm ⟨1, by omega⟩) (h.trans hv2)
  | 0, 3 => exact hno5 0 (by decide) (σ ⟨0, by omega⟩) ((hσ ⟨0, by omega⟩).symm.trans hv3)
  | 3, 0 =>
    have h := hσ (σ.symm ⟨0, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno5 0 (by decide) (σ.symm ⟨0, by omega⟩) (h.trans hv3)
  | 1, 2 =>
    have h := hσ (σ.symm ⟨0, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno4 2 (by decide) (σ.symm ⟨0, by omega⟩) (h.trans hv1)
  | 2, 1 => exact hno4 2 (by decide) (σ ⟨0, by omega⟩) ((hσ ⟨0, by omega⟩).symm.trans hv1)
  | 1, 3 =>
    have h := hσ (σ.symm ⟨0, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno4 3 (by decide) (σ.symm ⟨0, by omega⟩) (h.trans hv1)
  | 3, 1 => exact hno4 3 (by decide) (σ ⟨0, by omega⟩) ((hσ ⟨0, by omega⟩).symm.trans hv1)
  | 2, 3 =>
    have h := hσ (σ.symm ⟨1, by omega⟩); rw [Equiv.apply_symm_apply] at h
    exact hno3 3 (by decide) (σ.symm ⟨1, by omega⟩) (h.trans hv2)
  | 3, 2 => exact hno3 3 (by decide) (σ ⟨1, by omega⟩) ((hσ ⟨1, by omega⟩).symm.trans hv2)
  | 0, 0 | 1, 1 | 2, 2 | 3, 3 => exact hne rfl

lemma sq_sub_thirty_ge {m : ℕ} (hm : 92 ≤ m) : 8434 ≤ m ^ 2 - 30 := by
  have hsq : 8464 ≤ m ^ 2 := by nlinarith
  omega

/-- Explicit 4-segment closed walk of total length `4 * m` for `n = m^2 - 30` (`m ≥ 92`). -/
def witnessWalk4 (m : ℕ) (hm : 92 ≤ m) : ClosedWalk (m ^ 2 - 30) 4 where
  steps := witnessStep
  lengths := fun _ => m
  hk := by omega
  closed := witnessStep_closed
  valid j := by
    have hn_ge := sq_sub_thirty_ge hm
    refine ⟨by omega, witnessStep_ne_zero j, witnessStep_primitive (by omega) j, ?_⟩
    rw [witnessStep_norm_sq (by omega) j]
    have h30 : 30 ≤ m ^ 2 := by nlinarith
    rw [Nat.cast_sub h30]
    push_cast
    ring
  noncongruent := witnessStep_noncongruent (by have := sq_sub_thirty_ge hm; omega)

lemma witnessWalk4_totalLength (m : ℕ) (hm : 92 ≤ m) :
    (witnessWalk4 m hm).totalLength = 4 * m := by
  unfold ClosedWalk.totalLength witnessWalk4
  simp only [Fin.sum_univ_four]
  omega

/-- The 4-segment witness is a simple 4-cycle (its 4 partial sums have distinct 0th coordinates
`0, -2, -6, -5`). -/
lemma witnessWalk4_simple_cycle (m : ℕ) (hm : 92 ≤ m) :
    let v := (witnessWalk4 m hm).steps
    let p : Fin 4 → Fin (m ^ 2 - 30) → ℤ
      | 0 => fun _ => 0
      | 1 => v 0
      | 2 => fun i => v 0 i + v 1 i
      | 3 => fun i => v 0 i + v 1 i + v 2 i
    Function.Injective p := by
  intro v p a b hab
  have h0lt : 0 < m ^ 2 - 30 := by have := sq_sub_thirty_ge hm; omega
  have hcoord := congrFun hab ⟨0, h0lt⟩
  have hp0 : p 0 ⟨0, h0lt⟩ = 0 := rfl
  have hp1 : p 1 ⟨0, h0lt⟩ = -2 := rfl
  have hp2 : p 2 ⟨0, h0lt⟩ = -6 := rfl
  have hp3 : p 3 ⟨0, h0lt⟩ = -5 := rfl
  match a, b with
  | 0, 0 | 1, 1 | 2, 2 | 3, 3 => rfl
  | 0, 1 | 0, 2 | 0, 3 | 1, 0 | 1, 2 | 1, 3 | 2, 0 | 2, 1 | 2, 3 | 3, 0 | 3, 1 | 3, 2 =>
    simp only [hp0, hp1, hp2, hp3] at hcoord
    omega

/-! ## Section 3: Proof That Every 3-Segment Walk Has Length `≥ 4 * m + 2` (`m ≥ 92`) -/

/-- Step 1: Every valid diagonal in `ℤ^{m² - 30}` (`m ≥ 16`) has length `L ≥ m`. -/
lemma length_ge_of_valid {m L : ℕ} (hm : 16 ≤ m) {v : Fin (m ^ 2 - 30) → ℤ}
    (hv : ValidDiagonal v L) : m ≤ L := by
  have hge : (m ^ 2 - 30 : ℤ) ≤ ∑ i : Fin (m ^ 2 - 30), (v i) ^ 2 := by
    have h1 : ∀ i : Fin (m ^ 2 - 30), (1 : ℤ) ≤ (v i) ^ 2 := by
      intro i
      have hne : v i ≤ -1 ∨ 1 ≤ v i := by have := hv.2.1 i; omega
      rcases hne with h | h <;> nlinarith
    calc
      (m ^ 2 - 30 : ℤ) = ∑ _i : Fin (m ^ 2 - 30), (1 : ℤ) := by
        rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
        have h30 : 30 ≤ m ^ 2 := by nlinarith
        rw [Nat.cast_sub h30]; push_cast; ring
      _ ≤ ∑ i : Fin (m ^ 2 - 30), (v i) ^ 2 := Finset.sum_le_sum fun i _ => h1 i
  rw [hv.2.2.2] at hge
  by_contra hlt
  have hL : (L : ℤ) ≤ (m : ℤ) - 1 := by omega
  nlinarith

/-- Step 3 (coordinatewise): three nonzero integers summing to `0` have sum of squares `≥ 6`. -/
lemma sum_sq_ge_six {a b c : ℤ} (ha : a ≠ 0) (hb : b ≠ 0) (hc : c ≠ 0) (hsum : a + b + c = 0) :
    6 ≤ a ^ 2 + b ^ 2 + c ^ 2 := by
  by_cases h1 : a = 1 ∨ a = -1
  · by_cases h2 : b = 1 ∨ b = -1
    · rcases h1 with rfl | rfl <;> rcases h2 with rfl | rfl <;> (try omega) <;> nlinarith
    · have : 4 ≤ b ^ 2 := by
        have : b ≤ -2 ∨ 2 ≤ b := by omega
        rcases this with h | h <;> nlinarith
      nlinarith [sq_nonneg (a - 1), sq_nonneg (a + 1), sq_nonneg (c - 1), sq_nonneg (c + 1)]
  · have : 4 ≤ a ^ 2 := by
      have : a ≤ -2 ∨ 2 ≤ a := by omega
      rcases this with h | h <;> nlinarith
    have hb2 : 1 ≤ b ^ 2 := by
      have : b ≤ -1 ∨ 1 ≤ b := by omega
      rcases this with h | h <;> nlinarith
    have hc2 : 1 ≤ c ^ 2 := by
      have : c ≤ -1 ∨ 1 ≤ c := by omega
      rcases this with h | h <;> nlinarith
    linarith

/-- Step 4: Strict triangle inequality for noncongruent primitive diagonals `u + v + w = 0`:
`L₃ < L₁ + L₂`. -/
lemma strict_triangle_of_noncongruent {n : ℕ} (hn : 1 ≤ n)
    {u v w : Fin n → ℤ} {L₁ L₂ L₃ : ℕ}
    (hu : ValidDiagonal u L₁) (hv : ValidDiagonal v L₂) (hw : ValidDiagonal w L₃)
    (hsum : ∀ i, u i + v i + w i = 0) (hnc : ¬ AreCongruent u v) :
    L₃ < L₁ + L₂ := by
  by_contra hge
  have hge' : (L₁ : ℤ) + (L₂ : ℤ) ≤ (L₃ : ℤ) := by omega
  have hsq_le : ((L₁ : ℤ) + (L₂ : ℤ)) ^ 2 ≤ (L₃ : ℤ) ^ 2 := by nlinarith
  have hw_eq : ∀ i, w i = -(u i + v i) := fun i => by linarith [hsum i]
  have hL3_sq : (L₃ : ℤ) ^ 2 = (L₁ : ℤ) ^ 2 + (L₂ : ℤ) ^ 2 + 2 * ∑ i : Fin n, u i * v i := by
    rw [← hw.2.2.2, ← hu.2.2.2, ← hv.2.2.2]
    rw [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [hw_eq i]; ring
  have hdot_ge : (L₁ : ℤ) * (L₂ : ℤ) ≤ ∑ i : Fin n, u i * v i := by linarith
  -- Lagrange identity in `ℤ`: `∑_i ∑_j (u_i v_j - u_j v_i)^2 = 2 * (L₁² L₂² - (∑ u_i v_i)²)`.
  have hlagrange :
      ∑ i : Fin n, ∑ j : Fin n, (u i * v j - u j * v i) ^ 2 =
        2 * ((L₁ : ℤ) ^ 2 * (L₂ : ℤ) ^ 2 - (∑ i : Fin n, u i * v i) ^ 2) := by
    have h1 : ∀ i j : Fin n,
        (u i * v j - u j * v i) ^ 2 =
          (u i) ^ 2 * (v j) ^ 2 + (u j) ^ 2 * (v i) ^ 2 - 2 * ((u i * v i) * (u j * v j)) := by
      intro i j; ring
    simp_rw [h1, Finset.sum_sub_distrib, Finset.sum_add_distrib]
    have hA : ∑ i : Fin n, ∑ j : Fin n, (u i) ^ 2 * (v j) ^ 2 = (L₁ : ℤ) ^ 2 * (L₂ : ℤ) ^ 2 := by
      rw [← Finset.sum_mul_sum, hu.2.2.2, hv.2.2.2]
    have hB : ∑ i : Fin n, ∑ j : Fin n, (u j) ^ 2 * (v i) ^ 2 = (L₁ : ℤ) ^ 2 * (L₂ : ℤ) ^ 2 := by
      rw [Finset.sum_comm]
      have : ∀ j : Fin n, ∑ i : Fin n, (u j) ^ 2 * (v i) ^ 2 = (u j) ^ 2 * (L₂ : ℤ) ^ 2 := fun j => by
        rw [← Finset.mul_sum, hv.2.2.2]
      simp_rw [this, ← Finset.sum_mul, hu.2.2.2]
    have hC : ∑ i : Fin n, ∑ j : Fin n, (u i * v i) * (u j * v j) = (∑ i : Fin n, u i * v i) ^ 2 := by
      rw [sq, Finset.sum_mul_sum]
    have h2C : ∑ i : Fin n, ∑ j : Fin n, 2 * ((u i * v i) * (u j * v j)) =
        2 * (∑ i : Fin n, u i * v i) ^ 2 := by
      rw [← hC, Finset.mul_sum]
      refine Finset.sum_congr rfl fun i _ => (Finset.mul_sum ..).symm
    rw [hA, hB, h2C]; ring
  have hsq_nonpos : ∑ i : Fin n, ∑ j : Fin n, (u i * v j - u j * v i) ^ 2 ≤ 0 := by
    rw [hlagrange]
    have hpos : 0 ≤ (L₁ : ℤ) * (L₂ : ℤ) := by positivity
    nlinarith
  have hcollinear : ∀ i j : Fin n, u i * v j = u j * v i := by
    intro i j
    have hterm_le : (u i * v j - u j * v i) ^ 2 ≤ 0 := by
      have hinner : (u i * v j - u j * v i) ^ 2 ≤ ∑ j' : Fin n, (u i * v j' - u j' * v i) ^ 2 :=
        Finset.single_le_sum (f := fun j' => (u i * v j' - u j' * v i) ^ 2)
          (fun _ _ => sq_nonneg _) (Finset.mem_univ j)
      have houter : ∑ j' : Fin n, (u i * v j' - u j' * v i) ^ 2 ≤
          ∑ i' : Fin n, ∑ j' : Fin n, (u i' * v j' - u j' * v i') ^ 2 :=
        Finset.single_le_sum (f := fun i' => ∑ j' : Fin n, (u i' * v j' - u j' * v i') ^ 2)
          (fun _ _ => Finset.sum_nonneg fun _ _ => sq_nonneg _) (Finset.mem_univ i)
      linarith
    have : u i * v j - u j * v i = 0 := by nlinarith [sq_nonneg (u i * v j - u j * v i)]
    linarith
  -- From primitivity of `u` and `v`, collinearity forces `|u i| = |v i|` for all `i`, contradicting `hnc`.
  let i₀ : Fin n := ⟨0, by omega⟩
  let g : ℕ := Nat.gcd (u i₀).natAbs (v i₀).natAbs
  have hu0_pos : 0 < (u i₀).natAbs := Int.natAbs_pos.mpr (hu.2.1 i₀)
  have hv0_pos : 0 < (v i₀).natAbs := Int.natAbs_pos.mpr (hv.2.1 i₀)
  have hg_pos : 0 < g := Nat.gcd_pos_of_pos_left _ hu0_pos
  let p : ℕ := (u i₀).natAbs / g
  let q : ℕ := (v i₀).natAbs / g
  have hcop : p.Coprime q := Nat.coprime_div_gcd_div_gcd hg_pos
  have hp_eq : g * p = (u i₀).natAbs := Nat.mul_div_cancel' (Nat.gcd_dvd_left _ _)
  have hq_eq : g * q = (v i₀).natAbs := Nat.mul_div_cancel' (Nat.gcd_dvd_right _ _)
  have hratio : ∀ i : Fin n, (u i).natAbs * q = p * (v i).natAbs := by
    intro i
    have hmul : (u i).natAbs * (v i₀).natAbs = (u i₀).natAbs * (v i).natAbs := by
      have := congrArg Int.natAbs (hcollinear i i₀)
      simpa [Int.natAbs_mul] using this
    rw [← hp_eq, ← hq_eq] at hmul
    have : g * ((u i).natAbs * q) = g * (p * (v i).natAbs) := by linarith
    exact Nat.eq_of_mul_eq_mul_left hg_pos this
  have hp1 : p = 1 := hu.2.2.1 p fun i =>
    hcop.dvd_of_dvd_mul_right ⟨(v i).natAbs, hratio i⟩
  have hq1 : q = 1 := hv.2.2.1 q fun i =>
    hcop.symm.dvd_of_dvd_mul_left ⟨(u i).natAbs, (hratio i).symm.trans (mul_comm _ _)⟩
  apply hnc
  refine ⟨Equiv.refl _, fun i => ?_⟩
  have := hratio i
  rw [hp1, hq1, mul_one, one_mul] at this
  exact this.symm

/-- Step 5 algebraic inequality for sorted triple `m ≤ x ≤ y ≤ z` with `x + y + z ≤ 4m`
and strict triangle inequality `z < x + y` (`m ≥ 92`). -/
lemma three_sq_lt_of_sorted {m x y z : ℕ} (hm : 92 ≤ m)
    (hmx : m ≤ x) (hxy : x ≤ y) (hyz : y ≤ z)
    (hsum4 : x + y + z ≤ 4 * m) (htri : z < x + y) :
    (x : ℤ) ^ 2 + (y : ℤ) ^ 2 + (z : ℤ) ^ 2 < 6 * ((m : ℤ) ^ 2 - 30) := by
  let a : ℤ := (x : ℤ) - m
  let b : ℤ := (y : ℤ) - m
  let d : ℤ := 2 * (m : ℤ) - z
  have hmZ : (92 : ℤ) ≤ m := by exact_mod_cast hm
  have ha : 0 ≤ a := by omega
  have hb : a ≤ b := by omega
  have hd_ge : a + b ≤ d := by omega
  have hd_pos : 1 ≤ d := by omega
  have hd_le : d ≤ m := by omega
  have hx : (x : ℤ) = m + a := by omega
  have hy : (y : ℤ) = m + b := by omega
  have hz : (z : ℤ) = 2 * m - d := by omega
  by_cases hdm : d = m
  · have ha0 : a = 0 := by omega
    have hb0 : b = 0 := by omega
    rw [hx, hy, hz, hdm, ha0, hb0]
    nlinarith
  · have hd_lt : d ≤ (m : ℤ) - 1 := by omega
    have hprod : (m : ℤ) - 1 ≤ d * ((m : ℤ) - d) := by
      have : (d - 1) * ((m : ℤ) - 1 - d) ≥ 0 := mul_nonneg (by omega) (by omega)
      linarith
    have hsq_bound :
        (x : ℤ) ^ 2 + (y : ℤ) ^ 2 + (z : ℤ) ^ 2 ≤
          6 * (m : ℤ) ^ 2 - 2 * d * ((m : ℤ) - d) := by
      rw [hx, hy, hz]
      have hab_prod : 0 ≤ 2 * a * b := by nlinarith
      have hdiff_sq : 0 ≤ (d - a - b) * (d + a + b) := mul_nonneg (by omega) (by omega)
      have hd_m : 0 ≤ 2 * (m : ℤ) * (d - a - b) := mul_nonneg (by omega) (by omega)
      linarith
    linarith

/-- **Main Lower Bound:** Every valid 3-segment closed walk in `ℤ^{m² - 30}` (`m ≥ 92`) has
total length `≥ 4 * m + 2`. -/
theorem three_segment_length_ge (m : ℕ) (hm : 92 ≤ m) (W : ClosedWalk (m ^ 2 - 30) 3) :
    4 * m + 2 ≤ W.totalLength := by
  have hn : 1 ≤ m ^ 2 - 30 := by have := sq_sub_thirty_ge hm; omega
  have hm16 : 16 ≤ m := by omega
  let L0 := W.lengths 0
  let L1 := W.lengths 1
  let L2 := W.lengths 2
  have htot : W.totalLength = L0 + L1 + L2 := by
    unfold ClosedWalk.totalLength
    rw [Fin.sum_univ_three]
  -- Step 1: all three lengths `≥ m`.
  have hL0 : m ≤ L0 := length_ge_of_valid hm16 (W.valid 0)
  have hL1 : m ≤ L1 := length_ge_of_valid hm16 (W.valid 1)
  have hL2 : m ≤ L2 := length_ge_of_valid hm16 (W.valid 2)
  -- Step 2: parity (`L0 + L1 + L2` is even).
  have hsum_step : ∀ i, W.steps 0 i + W.steps 1 i + W.steps 2 i = 0 := fun i => by
    have := W.closed i
    rw [Fin.sum_univ_three] at this
    exact this
  have heven_sq : Even ((L0 : ℤ) ^ 2 + (L1 : ℤ) ^ 2 + (L2 : ℤ) ^ 2) := by
    rw [← (W.valid 0).2.2.2, ← (W.valid 1).2.2.2, ← (W.valid 2).2.2.2,
      ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    refine ⟨∑ i : Fin (m ^ 2 - 30),
        ((W.steps 0 i) ^ 2 + W.steps 0 i * W.steps 1 i + (W.steps 1 i) ^ 2), ?_⟩
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    have h2 : W.steps 2 i = -(W.steps 0 i + W.steps 1 i) := by linarith [hsum_step i]
    rw [h2]; ring
  have heven : Even (L0 + L1 + L2) := by
    obtain ⟨t, ht⟩ := heven_sq
    have hmod : ((L0 + L1 + L2 : ℕ) : ℤ) % 2 = 0 := by
      have : ((L0 : ℤ) ^ 2 + (L1 : ℤ) ^ 2 + (L2 : ℤ) ^ 2) % 2 = 0 := by omega
      have hsq : ∀ x : ℤ, x ^ 2 % 2 = x % 2 := fun x => by
        rcases Int.emod_two_eq_zero_or_one x with h | h <;> simp [sq, Int.mul_emod, h]
      have h0 := hsq (L0 : ℤ)
      have h1 := hsq (L1 : ℤ)
      have h2 := hsq (L2 : ℤ)
      push_cast
      omega
    have hmod_nat : (L0 + L1 + L2) % 2 = 0 := by exact_mod_cast hmod
    exact Nat.even_iff.mpr hmod_nat
  -- Step 3: `L0² + L1² + L2² ≥ 6 * (m² - 30)`.
  have hsum_sq : (6 * ((m : ℤ) ^ 2 - 30)) ≤ (L0 : ℤ) ^ 2 + (L1 : ℤ) ^ 2 + (L2 : ℤ) ^ 2 := by
    rw [← (W.valid 0).2.2.2, ← (W.valid 1).2.2.2, ← (W.valid 2).2.2.2,
      ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    calc
      6 * ((m : ℤ) ^ 2 - 30) = ∑ _i : Fin (m ^ 2 - 30), (6 : ℤ) := by
        rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
        have h30 : 30 ≤ m ^ 2 := by nlinarith
        rw [Nat.cast_sub h30]; push_cast; ring
      _ ≤ ∑ i : Fin (m ^ 2 - 30), ((W.steps 0 i) ^ 2 + (W.steps 1 i) ^ 2 + (W.steps 2 i) ^ 2) :=
        Finset.sum_le_sum fun i _ =>
          sum_sq_ge_six ((W.valid 0).2.1 i) ((W.valid 1).2.1 i) ((W.valid 2).2.1 i) (hsum_step i)
  -- Step 4: strict triangle inequalities in all three directions.
  have htri2 : L2 < L0 + L1 :=
    strict_triangle_of_noncongruent hn (W.valid 0) (W.valid 1) (W.valid 2)
      hsum_step (W.noncongruent 0 1 (by decide))
  have htri1 : L1 < L0 + L2 :=
    strict_triangle_of_noncongruent hn (W.valid 0) (W.valid 2) (W.valid 1)
      (fun i => by linarith [hsum_step i]) (W.noncongruent 0 2 (by decide))
  have htri0 : L0 < L1 + L2 :=
    strict_triangle_of_noncongruent hn (W.valid 1) (W.valid 2) (W.valid 0)
      (fun i => by linarith [hsum_step i]) (W.noncongruent 1 2 (by decide))
  -- Step 5: Symmetric contradiction for `L0 + L1 + L2 ≤ 4 * m`.
  have hnot_le : ¬ (L0 + L1 + L2 ≤ 4 * m) := by
    intro hle
    rcases le_total L0 L1 with h01 | h10
    · rcases le_total L1 L2 with h12 | h21
      · linarith [three_sq_lt_of_sorted hm hL0 h01 h12 hle htri2]
      · rcases le_total L0 L2 with h02 | h20
        · linarith [three_sq_lt_of_sorted hm hL0 h02 h21 (by omega) htri1]
        · linarith [three_sq_lt_of_sorted hm hL2 h20 h01 (by omega) (by omega)]
    · rcases le_total L0 L2 with h02 | h20
      · linarith [three_sq_lt_of_sorted hm hL1 h10 h02 (by omega) (by omega)]
      · rcases le_total L1 L2 with h12 | h21
        · linarith [three_sq_lt_of_sorted hm hL1 h12 h20 (by omega) htri0]
        · linarith [three_sq_lt_of_sorted hm hL2 h21 h10 (by omega) (by omega)]
  obtain ⟨r, hr⟩ := heven
  omega

/-! ## Section 4: Exact Value `a(m^2 - 30) = 4 * m` and Refutation of Conjecture -/

/-- No valid 1-segment or 2-segment closed walk exists for `n ≥ 1`. -/
lemma no_walk_one_or_two {n k : ℕ} (hn : 1 ≤ n) (hk : k ≤ 2) (W : ClosedWalk n k) : False := by
  have hk12 : k = 1 ∨ k = 2 := by have := W.hk; omega
  rcases hk12 with rfl | rfl
  · have h0 := W.closed ⟨0, by omega⟩
    rw [Fin.sum_univ_one] at h0
    exact (W.valid 0).2.1 ⟨0, by omega⟩ h0
  · apply W.noncongruent 0 1 (by decide)
    refine ⟨Equiv.refl _, fun i => ?_⟩
    have h0 := W.closed i
    rw [Fin.sum_univ_two] at h0
    have hneg : W.steps 1 i = -W.steps 0 i := by linarith
    rw [hneg, Int.natAbs_neg]
    rfl

/-- Every valid closed walk in `ℤ^{m² - 30}` (`m ≥ 92`) has total length `≥ 4 * m`. -/
theorem any_walk_length_ge (m : ℕ) (hm : 92 ≤ m) {k : ℕ} (W : ClosedWalk (m ^ 2 - 30) k) :
    4 * m ≤ W.totalLength := by
  have hn : 1 ≤ m ^ 2 - 30 := by have := sq_sub_thirty_ge hm; omega
  by_cases hk2 : k ≤ 2
  · exact (no_walk_one_or_two hn hk2 W).elim
  · by_cases hk3 : k = 3
    · subst hk3
      have := three_segment_length_ge m hm W
      omega
    · have hk4 : 4 ≤ k := by omega
      calc
        4 * m ≤ k * m := Nat.mul_le_mul_right m hk4
        _ = ∑ _j : Fin k, m := by simp [Finset.sum_const, smul_eq_mul]
        _ ≤ ∑ j : Fin k, W.lengths j :=
          Finset.sum_le_sum fun j _ => length_ge_of_valid (by omega) (W.valid j)

/-- Exact value `a386251 (m^2 - 30) = 4 * m` for all `m ≥ 92`. -/
theorem a386251_eq_four_mul (m : ℕ) (hm : 92 ≤ m) :
    a386251 (m ^ 2 - 30) = 4 * m := by
  unfold a386251
  have hmem : 4 * m ∈ {L : ℕ | ∃ (k : ℕ) (W : ClosedWalk (m ^ 2 - 30) k), W.totalLength = L} :=
    ⟨4, witnessWalk4 m hm, witnessWalk4_totalLength m hm⟩
  apply le_antisymm
  · exact Nat.sInf_le hmem
  · refine le_csInf ⟨4 * m, hmem⟩ ?_
    rintro L ⟨k, W, rfl⟩
    exact any_walk_length_ge m hm W

/-- **Infinite Family Refutation:** For every `m ≥ 92`, setting `n = m^2 - 30 ≥ 8434 ≥ 6`,
`a386251 n = 4 * m` is strictly less than the length of EVERY valid 3-segment closed walk
(so `a(n)` is NOT produced by any 3-segment walk). -/
theorem refutes_a386251_conjecture_infinite_family (m : ℕ) (hm : 92 ≤ m) :
    6 ≤ m ^ 2 - 30 ∧
    a386251 (m ^ 2 - 30) = 4 * m ∧
    ∀ W : ClosedWalk (m ^ 2 - 30) 3, a386251 (m ^ 2 - 30) < W.totalLength := by
  refine ⟨by have := sq_sub_thirty_ge hm; omega, a386251_eq_four_mul m hm, fun W => ?_⟩
  rw [a386251_eq_four_mul m hm]
  have := three_segment_length_ge m hm W
  omega

/-- Smallest counterexample in the family (`m = 92`, `n = 8434`, `a(8434) = 368 < 370`). -/
theorem refutes_a386251_at_8434 :
    a386251 8434 = 368 ∧ ∀ W : ClosedWalk 8434 3, 370 ≤ W.totalLength := by
  have h := a386251_eq_four_mul 92 le_rfl
  have h3 := three_segment_length_ge 92 le_rfl
  norm_num at h h3
  exact ⟨h, h3⟩

/-- Direct negation of Hohn's 2025 conjecture on OEIS `A386251`. -/
theorem not_a386251_conjecture :
    ¬ (∀ n : ℕ, 6 ≤ n → ∃ W : ClosedWalk n 3, W.totalLength = a386251 n) := by
  intro hconj
  obtain ⟨W, hW⟩ := hconj 8434 (by omega)
  obtain ⟨ha, hge⟩ := refutes_a386251_at_8434
  have := hge W
  omega

#print axioms witnessWalk4_simple_cycle
#print axioms a386251_eq_four_mul
#print axioms refutes_a386251_conjecture_infinite_family
#print axioms refutes_a386251_at_8434
#print axioms not_a386251_conjecture

end OpenMath.OeisA386251
