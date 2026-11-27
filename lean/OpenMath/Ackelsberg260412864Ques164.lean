import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Data.Finset.Prod
import Mathlib.Data.Nat.Log
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Order.LiminfLimsup
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Tactic

/-!
# Ackelsberg–Richter (`arXiv:2604.12864v1`, Section 16.1, Question 16.4): Disproof of Kneser in `ℕ²`

This file formalizes the refutation of Question 16.4 (*"Kneser's theorem in `ℕ²`"*) of
Ethan Ackelsberg and Florian K. Richter,
*"An inverse theorem for sumsets of sets of positive density in the integers"*
(`arXiv:2604.12864v1`, Section 16.1, lines 5759–5777):

> **Question 16.4 (Kneser's theorem in `ℕ²`).**
> With `ℕ = {1, 2, 3, ...}`, `[n] = {1, ..., n}`,
> `d̲(A) = liminf_{n,m→∞} |A ∩ ([n] × [m])| / (n m) = lim_{N→∞} inf_{n≥N, m≥N} |A ∩ ([n] × [m])| / (n m)`,
> and `H_{a,b,c} = {(a n + b m, c m) : m, n ∈ ℤ}` (`a, c ∈ ℕ`, `b ∈ {0, ..., a-1}`):
> If `A, B ⊆ ℕ²` are non-empty sets then either `d̲(A + B) ≥ d̲(A) + d̲(B)`, or there exists
> `H = H_{a,b,c} ∩ (ℕ × ℕ)` such that `A + B` equals, up to finitely many elements, a finite union
> of translates of `H` (and satisfies the density identity).

We refute Question 16.4 via the explicit nonempty witness `A = B ⊆ ℕ²`:
`A = (2ℕ × ℕ_{≥ 3}) ∪ {(2^j, 1) : j ∈ ℕ}` (where `ℕ = {1, 2, 3, ...}`):
1. `d̲(A) = d̲(B) = 1/2` and `d̲(A + B) = 1/2 < 1 = d̲(A) + d̲(B)` (exact limit of `inf_{n,m ≥ N}`).
2. For **every** `a ≥ 1`, `c ≥ 1`, `b < a`, and **every** finite set of translation vectors
   `V : Finset (ℤ × ℤ)`, the symmetric difference `(A + B) △ ⋃_{v ∈ V} (v + H)` is **infinite**:
   on the horizontal slice `y = 2`, `(A + B) ∩ (ℕ × {2}) = {(2^j + 2^{j'}, 2) : j, j' ≥ 1}` is
   infinite of zero linear density (`≤ K^2` elements up to `2^K`), whereas `⋃_{v ∈ V} (v + H)`
   intersects `y = 2` either in `∅` (leaving infinitely many points of `A + B` uncovered) or in
   a set containing an infinite arithmetic progression of step `a` (yielding `≥ ⌊(2^K - X₀)/a⌋ > K^2`
   points up to `2^K`, hence infinitely many points outside `A + B`).
-/

namespace OpenMath.Ackelsberg260412864Ques164

/-! ## Section 1: Primary-Source Definitions (`ℕ²` with `ℕ = {1, 2, ...}`, Lower Density, `H_{a,b,c}`) -/

/-- The positive integer grid `ℕ² = {(x, y) : 1 ≤ x ∧ 1 ≤ y}` (`arXiv:2604.12864v1`, Section 1 line 398). -/
def PosGrid : Set (ℕ × ℕ) := { p | 1 ≤ p.1 ∧ 1 ≤ p.2 }

/-- Pointwise sumset `A + B = {a + b | a ∈ A, b ∈ B}` in `ℕ × ℕ`. -/
def sumset2 (A B : Set (ℕ × ℕ)) : Set (ℕ × ℕ) :=
  { p | ∃ a ∈ A, ∃ b ∈ B, p = (a.1 + b.1, a.2 + b.2) }

/-- Box `[n] × [m] = {1, ..., n} × {1, ..., m}`. -/
def box (n m : ℕ) : Finset (ℕ × ℕ) :=
  Finset.Icc 1 n ×ˢ Finset.Icc 1 m

open Classical in
/-- Box density `|A ∩ ([n] × [m])| / (n * m)` (using classical decidability of `· ∈ A`). -/
noncomputable def boxDensity (A : Set (ℕ × ℕ)) (n m : ℕ) : ℝ :=
  (((box n m).filter (· ∈ A)).card : ℝ) / ((n * m : ℕ) : ℝ)

/-- Tail infimum `inf_{n ≥ N, m ≥ N} |A ∩ ([n] × [m])| / (n * m)` for `N ≥ 1`. -/
noncomputable def tailInf (A : Set (ℕ × ℕ)) (N : ℕ) : ℝ :=
  sInf { r : ℝ | ∃ n m : ℕ, N ≤ n ∧ N ≤ m ∧ r = boxDensity A n m }

/-- Lower density `d̲(A) = lim_{N → ∞} (inf_{n ≥ N, m ≥ N} |A ∩ ([n] × [m])| / (n * m))`,
defined via `iSup` of the monotone bounded sequence `tailInf A (N + 1)` (`N : ℕ`). -/
noncomputable def lowerDensity (A : Set (ℕ × ℕ)) : ℝ :=
  ⨆ N : ℕ, tailInf A (N + 1)

/-- Finite-index subgroup `H_{a,b,c} = {(a n + b m, c m) : m, n ∈ ℤ}` of `ℤ²`
(`arXiv:2604.12864v1`, Section 16.1 line 5768). -/
def H_abc (a b c : ℕ) : Set (ℤ × ℤ) :=
  { p | ∃ m n : ℤ, p = ((a : ℤ) * n + (b : ℤ) * m, (c : ℤ) * m) }

/-- Positive-quadrant restriction `H = H_{a,b,c} ∩ (ℕ × ℕ)`. -/
def Hpos (a b c : ℕ) : Set (ℕ × ℕ) :=
  { p | 1 ≤ p.1 ∧ 1 ≤ p.2 ∧ ((p.1 : ℤ), (p.2 : ℤ)) ∈ H_abc a b c }

/-- Translate `v + H` (allowing arbitrary integer shifts `v ∈ ℤ²`, intersected with `ℕ × ℕ`). -/
def translateH (v : ℤ × ℤ) (H : Set (ℕ × ℕ)) : Set (ℕ × ℕ) :=
  { p | ∃ h ∈ H, (p.1 : ℤ) = v.1 + (h.1 : ℤ) ∧ (p.2 : ℤ) = v.2 + (h.2 : ℤ) }

/-- Finite union of translates `⋃_{v ∈ V} (v + H)`. -/
def finiteUnionTranslates (V : Finset (ℤ × ℤ)) (H : Set (ℕ × ℕ)) : Set (ℕ × ℕ) :=
  { p | ∃ v ∈ V, p ∈ translateH v H }

/-! ## Section 2: Counterexample Witness `A = (2ℕ × ℕ_{≥ 3}) ∪ {(2^j, 1) : j ≥ 1}` -/

/-- Bulk piece `A₀ = 2ℕ × ℕ_{≥ 3}`. -/
def cexA0 : Set (ℕ × ℕ) :=
  { p | 1 ≤ p.1 ∧ p.1 % 2 = 0 ∧ 3 ≤ p.2 }

/-- Boundary power-of-2 ray `A₁ = {(2^j, 1) : j ≥ 1}`. -/
def cexA1 : Set (ℕ × ℕ) :=
  { p | ∃ j : ℕ, 1 ≤ j ∧ p = (2 ^ j, 1) }

/-- Counterexample set `A = B = A₀ ∪ A₁ ⊆ ℕ²`. -/
def cexA : Set (ℕ × ℕ) := cexA0 ∪ cexA1

lemma cexA_subset_posGrid : cexA ⊆ PosGrid := by
  rintro ⟨x, y⟩ (⟨hx1, _, hy3⟩ | ⟨j, hj, hEq⟩)
  · exact ⟨hx1, by omega⟩
  · rcases Prod.mk.inj hEq with ⟨rfl, rfl⟩
    exact ⟨Nat.one_le_pow j 2 (by decide), le_rfl⟩

lemma cexA_nonempty : cexA.Nonempty :=
  ⟨(2, 3), Or.inl ⟨by decide, by decide, by decide⟩⟩

/-- Exact characterization of `A + A` on horizontal slices. -/
theorem mem_sumset2_cexA (p : ℕ × ℕ) :
    p ∈ sumset2 cexA cexA ↔
      (4 ≤ p.1 ∧ p.1 % 2 = 0 ∧ 4 ≤ p.2) ∨
      (∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ p = (2 ^ j + 2 ^ j', 2)) := by
  constructor
  · rintro ⟨a, ha, b, hb, rfl⟩
    rcases ha with ⟨ha1, hae, ha3⟩ | ⟨j, hj, rfl⟩ <;>
    rcases hb with ⟨hb1, hbe, hb3⟩ | ⟨j', hj', rfl⟩
    · left; exact ⟨by omega, by omega, by omega⟩
    · left
      have h2j_ge : 2 ≤ 2 ^ j' := le_trans (by decide : 2 ≤ 2 ^ 1) (Nat.pow_le_pow_right (by decide) hj')
      have h2j_even : 2 ^ j' % 2 = 0 := by
        obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le' hj'
        simp [pow_succ]
      exact ⟨by omega, by omega, by omega⟩
    · left
      have h2j_ge : 2 ≤ 2 ^ j := le_trans (by decide : 2 ≤ 2 ^ 1) (Nat.pow_le_pow_right (by decide) hj)
      have h2j_even : 2 ^ j % 2 = 0 := by
        obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le' hj
        simp [pow_succ]
      exact ⟨by omega, by omega, by omega⟩
    · right
      exact ⟨j, j', hj, hj', rfl⟩
  · rintro (⟨hx4, hxe, hy4⟩ | ⟨j, j', hj, hj', rfl⟩)
    · refine ⟨(p.1 - 2, p.2 - 1), Or.inl ⟨by omega, by omega, by omega⟩,
        (2, 1), Or.inr ⟨1, le_rfl, rfl⟩, ?_⟩
      ext <;> dsimp <;> omega
    · exact ⟨(2 ^ j, 1), Or.inr ⟨j, hj, rfl⟩, (2 ^ j', 1), Or.inr ⟨j', hj', rfl⟩, rfl⟩

/-! ## Section 3: Exact Elementary Counting Bounds and `d̲(A) = d̲(A + A) = 1/2` -/

private lemma sq_le_two_pow (k : ℕ) (hk : 4 ≤ k) : k ^ 2 ≤ 2 ^ k := by
  induction k, hk using Nat.le_induction with
  | base => decide
  | succ m hm ih =>
    have hstep : (m + 1) ^ 2 ≤ 2 * m ^ 2 := by nlinarith
    have hpow : 2 ^ (m + 1) = 2 * 2 ^ m := by ring
    omega

private lemma cube_le_two_pow (k : ℕ) (hk : 10 ≤ k) : k ^ 3 ≤ 2 ^ k := by
  induction k, hk using Nat.le_induction with
  | base => decide
  | succ m hm ih =>
    have h1 : 10 * m ^ 2 ≤ m ^ 3 := by
      calc 10 * m ^ 2 ≤ m * m ^ 2 := Nat.mul_le_mul_right _ hm
        _ = m ^ 3 := by ring
    have hstep : (m + 1) ^ 3 ≤ 2 * m ^ 3 := by nlinarith
    have hpow : 2 ^ (m + 1) = 2 * 2 ^ m := by ring
    omega

private lemma card_even_Icc (n : ℕ) :
    ((Finset.Icc 1 n).filter (fun k => k % 2 = 0)).card = n / 2 := by
  induction n with
  | zero => simp
  | succ m ih =>
    have hsplit : Finset.Icc 1 (m + 1) = insert (m + 1) (Finset.Icc 1 m) := by
      ext x; simp only [Finset.mem_Icc, Finset.mem_insert]; omega
    have hnot : m + 1 ∉ Finset.Icc 1 m := by simp only [Finset.mem_Icc]; omega
    rw [hsplit, Finset.filter_insert]
    split_ifs with h
    · rw [Finset.card_insert_of_notMem (fun h' => hnot (Finset.mem_filter.mp h').1), ih]; omega
    · rw [ih]; omega

private lemma card_even_ge4_Icc {n : ℕ} (hn : 2 ≤ n) :
    ((Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0)).card = n / 2 - 1 := by
  have heq : (Finset.Icc 1 n).filter (fun k => k % 2 = 0) =
      insert 2 ((Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0)) := by
    ext x
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_insert]
    omega
  have hnot : 2 ∉ (Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0) := by
    simp only [Finset.mem_filter, Finset.mem_Icc]; omega
  have hcard := congrArg Finset.card heq
  rw [card_even_Icc, Finset.card_insert_of_notMem hnot] at hcard
  omega

open Classical in
private lemma card_pow2_slice_le (n : ℕ) :
    ((Finset.Icc 1 n).filter (fun x => ∃ j : ℕ, 1 ≤ j ∧ x = 2 ^ j)).card ≤ Nat.log 2 n := by
  have hsub : (Finset.Icc 1 n).filter (fun x => ∃ j : ℕ, 1 ≤ j ∧ x = 2 ^ j) ⊆
      (Finset.Icc 1 (Nat.log 2 n)).image (fun j => 2 ^ j) := by
    intro x hx
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_image] at hx ⊢
    rcases hx with ⟨⟨_, hxn⟩, j, hj1, rfl⟩
    refine ⟨j, ⟨hj1, ?_⟩, rfl⟩
    exact Nat.le_log_of_pow_le (by decide) hxn
  exact le_trans (Finset.card_le_card hsub)
    (le_trans Finset.card_image_le (by rw [Nat.card_Icc]; omega))

open Classical in
private lemma card_sum_pow2_slice_le (n : ℕ) :
    ((Finset.Icc 1 n).filter (fun x => ∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ x = 2 ^ j + 2 ^ j')).card ≤
      (Nat.log 2 n) ^ 2 := by
  have hsub : (Finset.Icc 1 n).filter
      (fun x => ∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ x = 2 ^ j + 2 ^ j') ⊆
      (Finset.Icc 1 (Nat.log 2 n) ×ˢ Finset.Icc 1 (Nat.log 2 n)).image
        (fun p => 2 ^ p.1 + 2 ^ p.2) := by
    intro x hx
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_image, Finset.mem_product] at hx ⊢
    rcases hx with ⟨⟨_, hxn⟩, j, j', hj1, hj'1, rfl⟩
    have h1 : 2 ^ j ≤ n := by have := Nat.one_le_pow j' 2 (by decide); omega
    have h2 : 2 ^ j' ≤ n := by have := Nat.one_le_pow j 2 (by decide); omega
    exact ⟨(j, j'), ⟨⟨hj1, Nat.le_log_of_pow_le (by decide) h1⟩,
      ⟨hj'1, Nat.le_log_of_pow_le (by decide) h2⟩⟩, rfl⟩
  exact le_trans (Finset.card_le_card hsub)
    (le_trans Finset.card_image_le (by rw [Finset.card_product, Nat.card_Icc, sq]; simp))

private lemma log_sq_le_n {n : ℕ} (hn : 16 ≤ n) : (Nat.log 2 n) ^ 2 ≤ n := by
  have hlog4 : 4 ≤ Nat.log 2 n := Nat.le_log_of_pow_le (by decide) (by omega : 2 ^ 4 ≤ n)
  exact le_trans (sq_le_two_pow _ hlog4) (Nat.pow_log_le_self 2 (by omega))

open Classical in
private lemma boxDensity_cexA_bounds {n m : ℕ} (hn : 16 ≤ n) (hm : 4 ≤ m) :
    1 / 2 - 2 / (m : ℝ) - 1 / (n : ℝ) ≤ boxDensity cexA n m ∧
    boxDensity cexA n m ≤ 1 / 2 + 1 / (m : ℝ) := by
  have hlo_sub : ((Finset.Icc 1 n).filter (fun k => k % 2 = 0)) ×ˢ Finset.Icc 3 m ⊆
      (box n m).filter (· ∈ cexA) := by
    intro p hp
    simp only [box, Finset.mem_filter, Finset.mem_product, Finset.mem_Icc] at hp ⊢
    exact ⟨⟨hp.1.1, by omega, hp.2.2⟩, Or.inl ⟨hp.1.1.1, hp.1.2, hp.2.1⟩⟩
  have hhi_sub : (box n m).filter (· ∈ cexA) ⊆
      (((Finset.Icc 1 n).filter (fun k => k % 2 = 0)) ×ˢ Finset.Icc 3 m) ∪
      (((Finset.Icc 1 n).filter (fun x => ∃ j : ℕ, 1 ≤ j ∧ x = 2 ^ j)) ×ˢ {1}) := by
    intro p hp
    simp only [box, cexA, cexA0, cexA1, Finset.mem_filter, Finset.mem_product, Finset.mem_union,
      Finset.mem_Icc, Finset.mem_singleton, Set.mem_union, Set.mem_ofPred_eq] at hp ⊢
    rcases hp with ⟨⟨⟨h1, h2⟩, ⟨h3, h4⟩⟩, ⟨_, hpe, hp3⟩ | ⟨j, hj, hEq⟩⟩
    · left; exact ⟨⟨⟨h1, h2⟩, hpe⟩, ⟨hp3, h4⟩⟩
    · right
      rcases Prod.mk.inj hEq with ⟨hx, hy⟩
      exact ⟨⟨⟨h1, h2⟩, ⟨j, hj, hx⟩⟩, hy⟩
  have hlo_card : (n / 2) * (m - 2) ≤ ((box n m).filter (· ∈ cexA)).card := by
    have h := Finset.card_le_card hlo_sub
    rw [Finset.card_product, card_even_Icc, Nat.card_Icc] at h
    simpa [show m + 1 - 3 = m - 2 by omega] using h
  have hhi_card : ((box n m).filter (· ∈ cexA)).card ≤ (n / 2) * (m - 2) + n := by
    have h1 := Finset.card_le_card hhi_sub
    have h2 := Finset.card_union_le
      (((Finset.Icc 1 n).filter (fun k => k % 2 = 0)) ×ˢ Finset.Icc 3 m)
      (((Finset.Icc 1 n).filter (fun x => ∃ j : ℕ, 1 ≤ j ∧ x = 2 ^ j)) ×ˢ {1})
    rw [Finset.card_product, Finset.card_product, card_even_Icc, Nat.card_Icc,
      Finset.card_singleton, mul_one] at h2
    have hlog_le : Nat.log 2 n ≤ n := le_trans (Nat.le_self_pow (by decide) _) (log_sq_le_n hn)
    have hpow_le := le_trans (card_pow2_slice_le n) hlog_le
    have hsubm : m + 1 - 3 = m - 2 := by omega
    rw [hsubm] at h2
    omega
  have hn_pos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (by omega)
  have hm_pos : (0 : ℝ) < (m : ℝ) := Nat.cast_pos.mpr (by omega)
  have hnm_pos : (0 : ℝ) < ((n * m : ℕ) : ℝ) := by push_cast; positivity
  unfold boxDensity
  have hcard_lo : (((n / 2) * (m - 2) : ℕ) : ℝ) ≤ (((box n m).filter (· ∈ cexA)).card : ℝ) :=
    Nat.cast_le.mpr hlo_card
  have hcard_hi : (((box n m).filter (· ∈ cexA)).card : ℝ) ≤ (((n / 2) * (m - 2) + n : ℕ) : ℝ) :=
    Nat.cast_le.mpr hhi_card
  have hdiv2_lo : (n : ℝ) / 2 - 1 ≤ ((n / 2 : ℕ) : ℝ) := by
    have : n ≤ 2 * (n / 2) + 1 := by omega
    have : (n : ℝ) ≤ 2 * ((n / 2 : ℕ) : ℝ) + 1 := by exact_mod_cast this
    linarith
  have hdiv2_hi : ((n / 2 : ℕ) : ℝ) ≤ (n : ℝ) / 2 := by
    have : 2 * (n / 2) ≤ n := by omega
    have : 2 * ((n / 2 : ℕ) : ℝ) ≤ (n : ℝ) := by exact_mod_cast this
    linarith
  have hm2 : ((m - 2 : ℕ) : ℝ) = (m : ℝ) - 2 := by
    rw [Nat.cast_sub (by omega)]; norm_num
  constructor
  · have h1 : (n : ℝ) * (m : ℝ) * (1 / 2 - 2 / (m : ℝ) - 1 / (n : ℝ)) ≤
        ((n / 2 : ℕ) : ℝ) * ((m - 2 : ℕ) : ℝ) := by
      have hlhs : (n : ℝ) * (m : ℝ) * (1 / 2 - 2 / (m : ℝ) - 1 / (n : ℝ)) =
          (n : ℝ) * (m : ℝ) / 2 - 2 * (n : ℝ) - (m : ℝ) := by
        field_simp [hn_pos.ne', hm_pos.ne']
      rw [hlhs, hm2]
      nlinarith [hdiv2_lo]
    rw [le_div_iff₀ hnm_pos]
    push_cast at hcard_lo ⊢
    linarith
  · have h1 : ((n / 2 : ℕ) : ℝ) * ((m - 2 : ℕ) : ℝ) + (n : ℝ) ≤
        (n : ℝ) * (m : ℝ) * (1 / 2 + 1 / (m : ℝ)) := by
      have hrhs : (n : ℝ) * (m : ℝ) * (1 / 2 + 1 / (m : ℝ)) =
          (n : ℝ) * (m : ℝ) / 2 + (n : ℝ) := by
        field_simp [hm_pos.ne']
      rw [hrhs, hm2]
      nlinarith [hdiv2_hi]
    rw [div_le_iff₀ hnm_pos]
    push_cast at hcard_hi ⊢
    linarith

open Classical in
private lemma boxDensity_sumset_bounds {n m : ℕ} (hn : 16 ≤ n) (hm : 4 ≤ m) :
    1 / 2 - 2 / (m : ℝ) - 2 / (n : ℝ) ≤ boxDensity (sumset2 cexA cexA) n m ∧
    boxDensity (sumset2 cexA cexA) n m ≤ 1 / 2 + 1 / (m : ℝ) := by
  have hlo_sub : ((Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0)) ×ˢ Finset.Icc 4 m ⊆
      (box n m).filter (· ∈ sumset2 cexA cexA) := by
    intro p hp
    simp only [box, Finset.mem_filter, Finset.mem_product, Finset.mem_Icc] at hp ⊢
    rw [mem_sumset2_cexA]
    exact ⟨⟨hp.1.1, by omega, hp.2.2⟩, Or.inl ⟨hp.1.2.1, hp.1.2.2, hp.2.1⟩⟩
  have hhi_sub : (box n m).filter (· ∈ sumset2 cexA cexA) ⊆
      (((Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0)) ×ˢ Finset.Icc 4 m) ∪
      (((Finset.Icc 1 n).filter (fun x => ∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ x = 2 ^ j + 2 ^ j')) ×ˢ {2}) := by
    intro p hp
    simp only [box, Finset.mem_filter, Finset.mem_product, Finset.mem_union,
      Finset.mem_Icc, Finset.mem_singleton] at hp ⊢
    rw [mem_sumset2_cexA] at hp
    rcases hp with ⟨⟨⟨h1, h2⟩, ⟨h3, h4⟩⟩, ⟨hp4, hpe, hpy4⟩ | ⟨j, j', hj, hj', hEq⟩⟩
    · left; exact ⟨⟨⟨h1, h2⟩, hp4, hpe⟩, ⟨hpy4, h4⟩⟩
    · right
      rcases Prod.mk.inj hEq with ⟨hx, hy⟩
      exact ⟨⟨⟨h1, h2⟩, ⟨j, j', hj, hj', hx⟩⟩, hy⟩
  have hlo_card : (n / 2 - 1) * (m - 3) ≤ ((box n m).filter (· ∈ sumset2 cexA cexA)).card := by
    have h := Finset.card_le_card hlo_sub
    rw [Finset.card_product, card_even_ge4_Icc (by omega), Nat.card_Icc] at h
    simpa [show m + 1 - 4 = m - 3 by omega] using h
  have hhi_card : ((box n m).filter (· ∈ sumset2 cexA cexA)).card ≤ (n / 2 - 1) * (m - 3) + n := by
    have h1 := Finset.card_le_card hhi_sub
    have h2 := Finset.card_union_le
      (((Finset.Icc 1 n).filter (fun k => 4 ≤ k ∧ k % 2 = 0)) ×ˢ Finset.Icc 4 m)
      (((Finset.Icc 1 n).filter (fun x => ∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ x = 2 ^ j + 2 ^ j')) ×ˢ {2})
    rw [Finset.card_product, Finset.card_product, card_even_ge4_Icc (by omega), Nat.card_Icc,
      Finset.card_singleton, mul_one] at h2
    have hsum_le := le_trans (card_sum_pow2_slice_le n) (log_sq_le_n hn)
    have hsubm : m + 1 - 4 = m - 3 := by omega
    rw [hsubm] at h2
    omega
  have hn_pos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (by omega)
  have hm_pos : (0 : ℝ) < (m : ℝ) := Nat.cast_pos.mpr (by omega)
  have hnm_pos : (0 : ℝ) < ((n * m : ℕ) : ℝ) := by push_cast; positivity
  unfold boxDensity
  have hcard_lo : (((n / 2 - 1) * (m - 3) : ℕ) : ℝ) ≤
      (((box n m).filter (· ∈ sumset2 cexA cexA)).card : ℝ) :=
    Nat.cast_le.mpr hlo_card
  have hcard_hi : (((box n m).filter (· ∈ sumset2 cexA cexA)).card : ℝ) ≤
      (((n / 2 - 1) * (m - 3) + n : ℕ) : ℝ) :=
    Nat.cast_le.mpr hhi_card
  have hdiv2_lo : (n : ℝ) / 2 - 2 ≤ ((n / 2 - 1 : ℕ) : ℝ) := by
    have : n ≤ 2 * (n / 2 - 1) + 3 := by omega
    have : (n : ℝ) ≤ 2 * ((n / 2 - 1 : ℕ) : ℝ) + 3 := by exact_mod_cast this
    linarith
  have hdiv2_hi : ((n / 2 - 1 : ℕ) : ℝ) ≤ (n : ℝ) / 2 := by
    have : 2 * (n / 2 - 1) ≤ n := by omega
    have : 2 * ((n / 2 - 1 : ℕ) : ℝ) ≤ (n : ℝ) := by exact_mod_cast this
    linarith
  have hm3 : ((m - 3 : ℕ) : ℝ) = (m : ℝ) - 3 := by
    rw [Nat.cast_sub (by omega)]; norm_num
  constructor
  · have h1 : (n : ℝ) * (m : ℝ) * (1 / 2 - 2 / (m : ℝ) - 2 / (n : ℝ)) ≤
        ((n / 2 - 1 : ℕ) : ℝ) * ((m - 3 : ℕ) : ℝ) := by
      have hlhs : (n : ℝ) * (m : ℝ) * (1 / 2 - 2 / (m : ℝ) - 2 / (n : ℝ)) =
          (n : ℝ) * (m : ℝ) / 2 - 2 * (n : ℝ) - 2 * (m : ℝ) := by
        field_simp [hn_pos.ne', hm_pos.ne']
      rw [hlhs, hm3]
      nlinarith [hdiv2_lo]
    rw [le_div_iff₀ hnm_pos]
    push_cast at hcard_lo ⊢
    linarith
  · have h1 : ((n / 2 - 1 : ℕ) : ℝ) * ((m - 3 : ℕ) : ℝ) + (n : ℝ) ≤
        (n : ℝ) * (m : ℝ) * (1 / 2 + 1 / (m : ℝ)) := by
      have hrhs : (n : ℝ) * (m : ℝ) * (1 / 2 + 1 / (m : ℝ)) =
          (n : ℝ) * (m : ℝ) / 2 + (n : ℝ) := by
        field_simp [hm_pos.ne']
      rw [hrhs, hm3]
      nlinarith [hdiv2_hi]
    rw [div_le_iff₀ hnm_pos]
    push_cast at hcard_hi ⊢
    linarith

private lemma boxDensity_nonneg (A : Set (ℕ × ℕ)) (n m : ℕ) : 0 ≤ boxDensity A n m := by
  unfold boxDensity
  positivity

open Classical in
private lemma boxDensity_le_one (A : Set (ℕ × ℕ)) (n m : ℕ) : boxDensity A n m ≤ 1 := by
  unfold boxDensity
  by_cases h0 : n * m = 0
  · rw [h0]; simp
  · have hpos : (0 : ℝ) < ((n * m : ℕ) : ℝ) := Nat.cast_pos.mpr (Nat.pos_of_ne_zero h0)
    rw [div_le_one hpos]
    have hcard : ((box n m).filter (· ∈ A)).card ≤ n * m := by
      have h1 := Finset.card_filter_le (box n m) (· ∈ A)
      have h2 : (box n m).card = n * m := by
        simp [box, Finset.card_product, Nat.card_Icc]
      omega
    exact_mod_cast hcard

private lemma tailInf_bddBelow (A : Set (ℕ × ℕ)) (N : ℕ) :
    BddBelow { r : ℝ | ∃ n m : ℕ, N ≤ n ∧ N ≤ m ∧ r = boxDensity A n m } :=
  ⟨0, by rintro r ⟨n, m, _, _, rfl⟩; exact boxDensity_nonneg A n m⟩

private lemma tailInf_nonempty (A : Set (ℕ × ℕ)) (N : ℕ) :
    { r : ℝ | ∃ n m : ℕ, N ≤ n ∧ N ≤ m ∧ r = boxDensity A n m }.Nonempty :=
  ⟨boxDensity A N N, N, N, le_rfl, le_rfl, rfl⟩

private lemma tailInf_le_one (A : Set (ℕ × ℕ)) (N : ℕ) : tailInf A N ≤ 1 :=
  le_trans (csInf_le (tailInf_bddBelow A N) ⟨N, N, le_rfl, le_rfl, rfl⟩) (boxDensity_le_one A N N)

private lemma tailInf_mono (A : Set (ℕ × ℕ)) : Monotone (tailInf A) := by
  intro N₁ N₂ hN
  apply csInf_le_csInf (tailInf_bddBelow A N₁) (tailInf_nonempty A N₂)
  rintro r ⟨n, m, hn, hm, rfl⟩
  exact ⟨n, m, le_trans hN hn, le_trans hN hm, rfl⟩

/-- Exact lower density `d̲(A) = 1/2` (and `tailInf A N → 1/2` as `N → ∞`). -/
theorem lowerDensity_cexA : lowerDensity cexA = 1 / 2 := by
  have hle : ∀ N : ℕ, tailInf cexA (N + 1) ≤ 1 / 2 := by
    intro N
    by_contra hgt
    push Not at hgt
    obtain ⟨M, hM⟩ := exists_nat_gt (1 / (tailInf cexA (N + 1) - 1 / 2))
    let K := max (max (N + 1) 16) M
    have hK_pos : (0 : ℝ) < (K : ℝ) := Nat.cast_pos.mpr (by omega)
    have h1 := (boxDensity_cexA_bounds (n := K) (m := K) (by omega) (by omega)).2
    have h2 : tailInf cexA (N + 1) ≤ boxDensity cexA K K :=
      csInf_le (tailInf_bddBelow cexA (N + 1)) ⟨K, K, by omega, by omega, rfl⟩
    have h3 : 1 / (K : ℝ) < tailInf cexA (N + 1) - 1 / 2 := by
      have hK_gt : 1 / (tailInf cexA (N + 1) - 1 / 2) < (K : ℝ) :=
        lt_of_lt_of_le hM (Nat.cast_le.mpr (le_max_right _ _))
      have hgap : 0 < tailInf cexA (N + 1) - 1 / 2 := by linarith
      rw [div_lt_iff₀ hK_pos]
      have := (div_lt_iff₀ hgap).mp hK_gt
      linarith
    linarith
  have hge : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, 1 / 2 - ε ≤ tailInf cexA (N + 1) := by
    intro ε hε
    obtain ⟨M, hM⟩ := exists_nat_gt (3 / ε)
    refine ⟨max M 16, ?_⟩
    apply le_csInf (tailInf_nonempty cexA _)
    rintro r ⟨n, m, hn, hm, rfl⟩
    have hlo := (boxDensity_cexA_bounds (n := n) (m := m) (by omega) (by omega)).1
    have hn_gt : 3 / ε < (n : ℝ) := lt_of_lt_of_le hM (Nat.cast_le.mpr (by omega))
    have hm_gt : 3 / ε < (m : ℝ) := lt_of_lt_of_le hM (Nat.cast_le.mpr (by omega))
    have hn_pos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (by omega)
    have hm_pos : (0 : ℝ) < (m : ℝ) := Nat.cast_pos.mpr (by omega)
    have h1n : 1 / (n : ℝ) < ε / 3 := by
      rw [div_lt_iff₀ hn_pos]; have := (div_lt_iff₀ hε).mp hn_gt; linarith
    have h2m : 2 / (m : ℝ) < 2 * ε / 3 := by
      rw [div_lt_iff₀ hm_pos]; have := (div_lt_iff₀ hε).mp hm_gt; linarith
    linarith
  apply le_antisymm
  · exact ciSup_le hle
  · by_contra hlt
    push Not at hlt
    obtain ⟨N, hN⟩ := hge ((1 / 2 - lowerDensity cexA) / 2) (by linarith)
    have hbdd : BddAbove (Set.range fun N : ℕ => tailInf cexA (N + 1)) := ⟨1 / 2, by rintro _ ⟨k, rfl⟩; exact hle k⟩
    have hsup : tailInf cexA (N + 1) ≤ lowerDensity cexA := le_ciSup hbdd N
    linarith

/-- Exact lower density `d̲(A + A) = 1/2` (strictly less than `d̲(A) + d̲(A) = 1`). -/
theorem lowerDensity_sumset_cexA : lowerDensity (sumset2 cexA cexA) = 1 / 2 := by
  have hle : ∀ N : ℕ, tailInf (sumset2 cexA cexA) (N + 1) ≤ 1 / 2 := by
    intro N
    by_contra hgt
    push Not at hgt
    obtain ⟨M, hM⟩ := exists_nat_gt (1 / (tailInf (sumset2 cexA cexA) (N + 1) - 1 / 2))
    let K := max (max (N + 1) 16) M
    have hK_pos : (0 : ℝ) < (K : ℝ) := Nat.cast_pos.mpr (by omega)
    have h1 := (boxDensity_sumset_bounds (n := K) (m := K) (by omega) (by omega)).2
    have h2 : tailInf (sumset2 cexA cexA) (N + 1) ≤ boxDensity (sumset2 cexA cexA) K K :=
      csInf_le (tailInf_bddBelow _ (N + 1)) ⟨K, K, by omega, by omega, rfl⟩
    have h3 : 1 / (K : ℝ) < tailInf (sumset2 cexA cexA) (N + 1) - 1 / 2 := by
      have hK_gt : 1 / (tailInf (sumset2 cexA cexA) (N + 1) - 1 / 2) < (K : ℝ) :=
        lt_of_lt_of_le hM (Nat.cast_le.mpr (le_max_right _ _))
      have hgap : 0 < tailInf (sumset2 cexA cexA) (N + 1) - 1 / 2 := by linarith
      rw [div_lt_iff₀ hK_pos]
      have := (div_lt_iff₀ hgap).mp hK_gt
      linarith
    linarith
  have hge : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, 1 / 2 - ε ≤ tailInf (sumset2 cexA cexA) (N + 1) := by
    intro ε hε
    obtain ⟨M, hM⟩ := exists_nat_gt (4 / ε)
    refine ⟨max M 16, ?_⟩
    apply le_csInf (tailInf_nonempty _ _)
    rintro r ⟨n, m, hn, hm, rfl⟩
    have hlo := (boxDensity_sumset_bounds (n := n) (m := m) (by omega) (by omega)).1
    have hn_gt : 4 / ε < (n : ℝ) := lt_of_lt_of_le hM (Nat.cast_le.mpr (by omega))
    have hm_gt : 4 / ε < (m : ℝ) := lt_of_lt_of_le hM (Nat.cast_le.mpr (by omega))
    have hn_pos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (by omega)
    have hm_pos : (0 : ℝ) < (m : ℝ) := Nat.cast_pos.mpr (by omega)
    have h2n : 2 / (n : ℝ) < ε / 2 := by
      rw [div_lt_iff₀ hn_pos]; have := (div_lt_iff₀ hε).mp hn_gt; linarith
    have h2m : 2 / (m : ℝ) < ε / 2 := by
      rw [div_lt_iff₀ hm_pos]; have := (div_lt_iff₀ hε).mp hm_gt; linarith
    linarith
  apply le_antisymm
  · exact ciSup_le hle
  · by_contra hlt
    push Not at hlt
    obtain ⟨N, hN⟩ := hge ((1 / 2 - lowerDensity (sumset2 cexA cexA)) / 2) (by linarith)
    have hbdd : BddAbove (Set.range fun N : ℕ => tailInf (sumset2 cexA cexA) (N + 1)) :=
      ⟨1 / 2, by rintro _ ⟨k, rfl⟩; exact hle k⟩
    have hsup : tailInf (sumset2 cexA cexA) (N + 1) ≤ lowerDensity (sumset2 cexA cexA) :=
      le_ciSup hbdd N
    linarith

/-- Also verify that `tailInf` converges literally to `lowerDensity` as `N → ∞` (`Filter.Tendsto`). -/
theorem tendsto_tailInf_cexA :
    Filter.Tendsto (fun N => tailInf cexA (N + 1)) Filter.atTop (nhds (1 / 2)) := by
  rw [← lowerDensity_cexA]
  exact tendsto_atTop_ciSup (fun i j hij => tailInf_mono cexA (by omega))
    ⟨1, by rintro _ ⟨k, rfl⟩; exact tailInf_le_one cexA (k + 1)⟩

theorem tendsto_tailInf_sumset_cexA :
    Filter.Tendsto (fun N => tailInf (sumset2 cexA cexA) (N + 1)) Filter.atTop (nhds (1 / 2)) := by
  rw [← lowerDensity_sumset_cexA]
  exact tendsto_atTop_ciSup (fun i j hij => tailInf_mono (sumset2 cexA cexA) (by omega))
    ⟨1, by rintro _ ⟨k, rfl⟩; exact tailInf_le_one (sumset2 cexA cexA) (k + 1)⟩

/-! ## Section 4: Refutation of the Finite-Union-of-Translates Alternative on Slice `y = 2` -/

open Classical in
/-- For every finite-index subgroup `H_{a,b,c}` (`a, c ≥ 1, b < a`) and every finite set of
translates `V : Finset (ℤ × ℤ)`, `(A + A) △ ⋃_{v ∈ V} (v + H)` is **infinite**. -/
theorem symmDiff_sumset_cexA_infinite (a b c : ℕ) (ha : 1 ≤ a) (_hc : 1 ≤ c)
    (V : Finset (ℤ × ℤ)) :
    (symmDiff (sumset2 cexA cexA) (finiteUnionTranslates V (Hpos a b c))).Infinite := by
  let U := finiteUnionTranslates V (Hpos a b c)
  by_cases hhit : ∃ v ∈ V, ∃ x : ℕ, (x, 2) ∈ translateH v (Hpos a b c)
  · -- Case 2: Some translate `v₀ + H` hits the line `y = 2` at `(x₀, 2)`.
    -- Then `(x₀ + t * a, 2) ∈ U` for ALL `t : ℕ`, giving an infinite AP of density `1 / a`,
    -- while `(A + A) ∩ ([2^K] × {2})` has at most `K^2` points (`≪ 2^K / a`).
    rcases hhit with ⟨v₀, hv₀V, x₀, ⟨h₀, ⟨hh₀1, hh₀2, m₀, n₀, hh₀_eq⟩, hx₀_eq, hy₀_eq⟩⟩
    have hAP : ∀ t : ℕ, (x₀ + t * a, 2) ∈ U := by
      intro t
      refine ⟨v₀, hv₀V, (h₀.1 + t * a, h₀.2), ⟨by omega, hh₀2, m₀, n₀ + (t : ℤ), ?_⟩, ?_, hy₀_eq⟩
      · rcases Prod.mk.inj hh₀_eq with ⟨h1, h2⟩
        ext
        · dsimp; linarith
        · exact h2
      · dsimp; linarith
    -- Show `U \ (A + A)` is infinite (hence `symmDiff (A + A) U` is infinite)
    intro hfin
    have hdiff_fin : (U \ sumset2 cexA cexA).Finite :=
      hfin.subset (fun p hp => Or.inr hp)
    let Sdiff := hdiff_fin.toFinset
    -- Pick `K` so large that `K ≥ 10`, `2^K ≥ x₀ + a * (Sdiff.card + K^2 + 2)`
    let K : ℕ := max 10 (max (x₀ + 1) (a * (Sdiff.card + 3) + 4 * a))
    have hK10 : 10 ≤ K := le_max_left _ _
    have hK_cube : K ^ 3 ≤ 2 ^ K := cube_le_two_pow K hK10
    -- Count `t ∈ [0, M]` where `M := Sdiff.card + K^2 + 1`:
    let M : ℕ := Sdiff.card + K ^ 2 + 1
    have hbound : x₀ + M * a ≤ 2 ^ K := by
      have hK_x0 : x₀ < K := lt_of_lt_of_le (Nat.lt_succ_self x₀)
        (le_trans (le_max_left _ _) (le_max_right _ _))
      have hK_a : a * (Sdiff.card + 3) + 4 * a ≤ K :=
        le_trans (le_max_right _ _) (le_max_right _ _)
      have h1 : x₀ + M * a ≤ K + (Sdiff.card + K ^ 2 + 1) * a := by
        dsimp [M]; omega
      have h2 : a ≤ K := by nlinarith
      have h3 : (Sdiff.card + 1) * a ≤ K := by nlinarith
      -- `K + K + K^2 * a ≤ 2K + a * K^2`; wait: what if `a` is close to `K`?
      -- Actually `K ≥ 4a` gives `a * K^2 ≤ K^3 / 4`!
      have h4a : 4 * a ≤ K := by omega
      have h4 : K + (Sdiff.card + K ^ 2 + 1) * a ≤ K ^ 3 := by
        nlinarith [hK10, h3, h4a]
      omega
    -- All `M + 1` points `(x₀ + t * a, 2)` (`t ∈ range (M + 1)`) lie in `U ∩ ([2^K] × {2})`,
    -- hence split between `Sdiff` (size `Sdiff.card`) and `(A + A) ∩ ([2^K] × {2})` (size `≤ K^2`)!
    let pts : Finset (ℕ × ℕ) := (Finset.range (M + 1)).image (fun t => (x₀ + t * a, 2))
    have hpts_card : pts.card = M + 1 := by
      rw [Finset.card_image_of_injOn, Finset.card_range]
      intro t₁ _ t₂ _ heq
      have hx : x₀ + t₁ * a = x₀ + t₂ * a := congrArg Prod.fst heq
      have hmul : t₁ * a = t₂ * a := by omega
      exact Nat.eq_of_mul_eq_mul_right (by omega) hmul
    let sliceA : Finset (ℕ × ℕ) :=
      ((Finset.Icc 1 (2 ^ K)).filter
        (fun x => ∃ j j' : ℕ, 1 ≤ j ∧ 1 ≤ j' ∧ x = 2 ^ j + 2 ^ j')) ×ˢ {2}
    have hpts_sub : pts ⊆ Sdiff ∪ sliceA := by
      intro p hp
      rcases Finset.mem_image.mp hp with ⟨t, ht, rfl⟩
      have ht_le : t ≤ M := Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)
      have hU_mem : (x₀ + t * a, 2) ∈ U := hAP t
      by_cases hA_mem : (x₀ + t * a, 2) ∈ sumset2 cexA cexA
      · apply Finset.mem_union_right
        rw [mem_sumset2_cexA] at hA_mem
        rcases hA_mem with ⟨_, _, hy4⟩ | ⟨j, j', hj, hj', hEq⟩
        · omega
        · simp only [sliceA, Finset.mem_product, Finset.mem_filter, Finset.mem_Icc,
            Finset.mem_singleton]
          refine ⟨⟨⟨?_, ?_⟩, j, j', hj, hj', (Prod.mk.inj hEq).1⟩, trivial⟩
          · rw [(Prod.mk.inj hEq).1]
            exact le_trans (Nat.one_le_pow j 2 (by decide)) (Nat.le_add_right _ _)
          · have hmul_le : t * a ≤ M * a := Nat.mul_le_mul_right a ht_le
            omega
      · apply Finset.mem_union_left
        exact hdiff_fin.mem_toFinset.mpr ⟨hU_mem, hA_mem⟩
    have hslice_card : sliceA.card ≤ K ^ 2 := by
      simp only [sliceA, Finset.card_product, Finset.card_singleton, mul_one]
      have h := card_sum_pow2_slice_le (2 ^ K)
      rwa [Nat.log_pow (by decide : 1 < 2) K] at h
    have hcard_le := le_trans (Finset.card_le_card hpts_sub) (Finset.card_union_le Sdiff sliceA)
    rw [hpts_card] at hcard_le
    dsimp [M] at hcard_le
    omega
  · -- Case 1: `U ∩ (ℕ × {2}) = ∅`, while `(A + A) ∩ (ℕ × {2})` contains `{(2^j + 2, 2) : j ≥ 1}`!
    push Not at hhit
    have hinj : Function.Injective (fun j : ℕ => (2 ^ (j + 1) + 2, 2)) := by
      intro j₁ j₂ h
      have h1 : 2 ^ (j₁ + 1) = 2 ^ (j₂ + 1) := by
        have := congrArg Prod.fst h; dsimp at this; omega
      have h2 := Nat.pow_right_injective (by decide : 2 ≤ 2) h1
      omega
    have hsub : Set.range (fun j : ℕ => (2 ^ (j + 1) + 2, 2)) ⊆ symmDiff (sumset2 cexA cexA) U := by
      rintro p ⟨j, rfl⟩
      left
      refine ⟨?_, ?_⟩
      · rw [mem_sumset2_cexA]
        exact Or.inr ⟨j + 1, 1, by omega, le_rfl, rfl⟩
      · rintro ⟨v, hvV, hmem⟩
        exact hhit v hvV (2 ^ (j + 1) + 2) hmem
    exact (Set.infinite_range_of_injective hinj).mono hsub

/-- **Main Refutation Witness for Question 16.4 (`arXiv:2604.12864v1`, Section 16.1):**
`A = B = cexA ⊆ ℕ²` is nonempty, satisfies `d̲(A + B) < d̲(A) + d̲(B)`, and `A + B` does not
equal any finite union of translates of `H_{a,b,c} ∩ (ℕ × ℕ)` up to finitely many elements. -/
theorem refutes_ackelsberg_question_16_4 :
    cexA ⊆ PosGrid ∧ cexA.Nonempty ∧
    lowerDensity (sumset2 cexA cexA) < lowerDensity cexA + lowerDensity cexA ∧
    ∀ (a b c : ℕ), 1 ≤ a → 1 ≤ c → b < a →
      ∀ (V : Finset (ℤ × ℤ)),
        (symmDiff (sumset2 cexA cexA) (finiteUnionTranslates V (Hpos a b c))).Infinite := by
  refine ⟨cexA_subset_posGrid, cexA_nonempty, ?_, fun a b c ha hc _ V =>
    symmDiff_sumset_cexA_infinite a b c ha hc V⟩
  rw [lowerDensity_sumset_cexA, lowerDensity_cexA]
  norm_num

/-- **Direct Negation of Ackelsberg–Richter (`arXiv:2604.12864v1`, Question 16.4):** -/
theorem not_ackelsberg_question_16_4 :
    ¬ (∀ A B : Set (ℕ × ℕ), A ⊆ PosGrid → B ⊆ PosGrid → A.Nonempty → B.Nonempty →
        lowerDensity (sumset2 A B) ≥ lowerDensity A + lowerDensity B ∨
        ∃ (a b c : ℕ) (V : Finset (ℤ × ℤ)),
          1 ≤ a ∧ 1 ≤ c ∧ b < a ∧
          (symmDiff (sumset2 A B) (finiteUnionTranslates V (Hpos a b c))).Finite) := by
  intro hall
  obtain ⟨hsub, hne, hlt, hinf⟩ := refutes_ackelsberg_question_16_4
  rcases hall cexA cexA hsub hsub hne hne with hge | ⟨a, b, c, V, ha, hc, hba, hfin⟩
  · linarith
  · exact hinf a b c ha hc hba V hfin

#print axioms lowerDensity_cexA
#print axioms lowerDensity_sumset_cexA
#print axioms symmDiff_sumset_cexA_infinite
#print axioms refutes_ackelsberg_question_16_4
#print axioms not_ackelsberg_question_16_4

end OpenMath.Ackelsberg260412864Ques164
