import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Perm
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Relation
import Mathlib.Tactic

/-!
# Hong Duc Bui (2025) — Acyclicity of Triangle-Matching Flip Graph (`arXiv:2508.04602v1`, §8.2)

This file formalizes the proof of Hong Duc Bui's Section 8.2 acyclicity conjecture
from *"On existence of a compatible triangulation with the double circle order type"*
(`arXiv:2508.04602v1`, lines 1188–1217):

Let `Q ⊂ ℝ²` be a planar point set in general position with `|Q| = 2n` and
`|CH(Q)| = n` (`n ≥ 3`), with convex hull vertices `Q_0, ..., Q_{n-1}` in
counterclockwise cyclic order (indices modulo `n`) and interior points
`B_0, ..., B_{n-1}`.

For each permutation `π : Equiv.Perm (Fin n)`, form the `n` triangles
`T_k(π) = △ Q_k Q_{k+1} B_{π(k)}`. The directed state graph `G` has vertex set
`Equiv.Perm (Fin n)` and a directed edge `π → ρ` iff there exist `i ≠ j` such that
`ρ i = π j`, `ρ j = π i`, `ρ k = π k` for `k ∉ {i, j}`, and `T_i(π)` and `T_j(π)`
intersect nontrivially (beyond a shared convex-hull vertex).

## Main Results

* `OpenMath.Bui250804602Conj81.trianglesIntersect_iff_open`:
  Lemma 1 — nontrivial intersection of `T_i(a)` and `T_j(b)` (`i ≠ j`, `a ≠ b`)
  is equivalent to nonempty intersection of their open interiors.
* `OpenMath.Bui250804602Conj81.area_product_strict_decrease`:
  Lemma 3 — every directed edge `π → ρ` swapping `i, j` strictly decreases the
  oriented area product `ℓ_i(B_{π(i)}) * ℓ_j(B_{π(j)})`, and the swapped
  triangles `T_i(ρ)` and `T_j(ρ)` do not intersect nontrivially.
* `OpenMath.Bui250804602Conj81.potential_strict_decrease`:
  The positive potential `Φ(π) = ∏ k, ℓ_k(B_{π(k)})` strictly decreases along
  every directed edge `π → ρ`.
* `OpenMath.Bui250804602Conj81.bui_conjecture_8_2_acyclic`:
  The directed state graph `G` has no directed cycles (`¬ TransGen (StateEdge cfg) π π`).
* `OpenMath.Bui250804602Conj81.bui_conjecture_8_2_terminates`:
  Every directed walk in `G` has length at most `n! - 1`.
-/

namespace OpenMath.Bui250804602Conj81

open scoped BigOperators

/-! ## Section 1: 2D Planar Geometry and Barycentric Coordinates -/

/-- A point in the Euclidean plane `ℝ²`. -/
abbrev Pt := ℝ × ℝ

/-- 2D determinant (cross product) `u.1 * v.2 - u.2 * v.1`. -/
def det2 (u v : Pt) : ℝ :=
  u.1 * v.2 - u.2 * v.1

/-- Signed twice-area `det(B - A, C - A)` of triangle `(A, B, C)`. -/
def orient (A B C : Pt) : ℝ :=
  det2 (B.1 - A.1, B.2 - A.2) (C.1 - A.1, C.2 - A.2)

/-- Affine combination `a • A + b • B + c • C` in `ℝ²`. -/
def comb3 (a b c : ℝ) (A B C : Pt) : Pt :=
  (a * A.1 + b * B.1 + c * C.1, a * A.2 + b * B.2 + c * C.2)

/-- Closed triangle `△ A B C` as convex combinations of its three vertices. -/
def InClosedTri (A B C X : Pt) : Prop :=
  ∃ a b c : ℝ, 0 ≤ a ∧ 0 ≤ b ∧ 0 ≤ c ∧ a + b + c = 1 ∧ X = comb3 a b c A B C

/-- Open interior `int(△ A B C)` as strictly positive barycentric combinations. -/
def InOpenTri (A B C X : Pt) : Prop :=
  ∃ a b c : ℝ, 0 < a ∧ 0 < b ∧ 0 < c ∧ a + b + c = 1 ∧ X = comb3 a b c A B C

lemma orient_self_left (A B : Pt) : orient A B A = 0 := by
  unfold orient det2; ring

lemma orient_self_right (A B : Pt) : orient A B B = 0 := by
  unfold orient det2; ring

lemma orient_cyc (A B C : Pt) : orient B C A = orient A B C := by
  unfold orient det2; ring

lemma orient_cyc' (A B C : Pt) : orient C A B = orient A B C := by
  unfold orient det2; ring

lemma orient_swap_fst (A B C : Pt) : orient B A C = -orient A B C := by
  unfold orient det2; ring

lemma orient_swap_snd (A B C : Pt) : orient A C B = -orient A B C := by
  unfold orient det2; ring

lemma orient_comb3 {a b c : ℝ} (hsum : a + b + c = 1) (U V A B C : Pt) :
    orient U V (comb3 a b c A B C) =
      a * orient U V A + b * orient U V B + c * orient U V C := by
  have hc : c = 1 - a - b := by linarith
  subst hc
  unfold orient det2 comb3
  ring

lemma orient_sum_eq (A B C X : Pt) :
    orient B C X + orient C A X + orient A B X = orient A B C := by
  unfold orient det2; ring

lemma cramer_fst (A B C X : Pt) :
    orient B C X * A.1 + orient C A X * B.1 + orient A B X * C.1 = orient A B C * X.1 := by
  unfold orient det2; ring

lemma cramer_snd (A B C X : Pt) :
    orient B C X * A.2 + orient C A X * B.2 + orient A B X * C.2 = orient A B C * X.2 := by
  unfold orient det2; ring

/-- Exact half-plane characterization of a closed positively-oriented triangle. -/
lemma inClosedTri_iff {A B C X : Pt} (hD : 0 < orient A B C) :
    InClosedTri A B C X ↔
      0 ≤ orient B C X ∧ 0 ≤ orient C A X ∧ 0 ≤ orient A B X := by
  constructor
  · rintro ⟨a, b, c, ha, hb, hc, hsum, rfl⟩
    rw [orient_comb3 hsum, orient_comb3 hsum, orient_comb3 hsum]
    simp only [orient_self_left, orient_self_right, orient_cyc,
      mul_zero, add_zero, zero_add]
    exact ⟨mul_nonneg ha hD.le, mul_nonneg hb hD.le, mul_nonneg hc hD.le⟩
  · rintro ⟨h1, h2, h3⟩
    set D := orient A B C
    have hDne : D ≠ 0 := ne_of_gt hD
    refine ⟨orient B C X / D, orient C A X / D, orient A B X / D,
      div_nonneg h1 hD.le, div_nonneg h2 hD.le, div_nonneg h3 hD.le, ?_, ?_⟩
    · rw [← add_div, ← add_div, orient_sum_eq, div_self hDne]
    · ext
      · dsimp [comb3]
        have h := cramer_fst A B C X
        field_simp
        linarith
      · dsimp [comb3]
        have h := cramer_snd A B C X
        field_simp
        linarith

/-- Exact half-plane characterization of an open positively-oriented triangle. -/
lemma inOpenTri_iff {A B C X : Pt} (hD : 0 < orient A B C) :
    InOpenTri A B C X ↔
      0 < orient B C X ∧ 0 < orient C A X ∧ 0 < orient A B X := by
  constructor
  · rintro ⟨a, b, c, ha, hb, hc, hsum, rfl⟩
    rw [orient_comb3 hsum, orient_comb3 hsum, orient_comb3 hsum]
    simp only [orient_self_left, orient_self_right, orient_cyc,
      mul_zero, add_zero, zero_add]
    exact ⟨mul_pos ha hD, mul_pos hb hD, mul_pos hc hD⟩
  · rintro ⟨h1, h2, h3⟩
    set D := orient A B C
    have hDne : D ≠ 0 := ne_of_gt hD
    refine ⟨orient B C X / D, orient C A X / D, orient A B X / D,
      div_pos h1 hD, div_pos h2 hD, div_pos h3 hD, ?_, ?_⟩
    · rw [← add_div, ← add_div, orient_sum_eq, div_self hDne]
    · ext
      · dsimp [comb3]
        have h := cramer_fst A B C X
        field_simp
        linarith
      · dsimp [comb3]
        have h := cramer_snd A B C X
        field_simp
        linarith

lemma orient_shift (P Q X w : Pt) (t : ℝ) :
    orient P Q (X.1 + t * w.1, X.2 + t * w.2) =
      orient P Q X + t * det2 (Q.1 - P.1, Q.2 - P.2) w := by
  unfold orient det2; ring

private lemma exists_pos_pair (c d : ℝ) (h : 0 < c ∨ (c = 0 ∧ 0 < d)) :
    ∃ t₀ : ℝ, 0 < t₀ ∧ ∀ t : ℝ, 0 < t → t ≤ t₀ → 0 < c + t * d := by
  rcases h with hc | ⟨rfl, hd⟩
  · by_cases hd : 0 ≤ d
    · exact ⟨1, one_pos, fun t ht _ => by nlinarith⟩
    · refine ⟨c / (2 * (-d)), div_pos hc (by linarith), fun t ht htle => ?_⟩
      have hneg : 0 < -d := by linarith
      have hmul : t * (2 * (-d)) ≤ c := (le_div_iff₀ (by linarith)).mp htle
      linarith
  · exact ⟨1, one_pos, fun t ht _ => by nlinarith⟩

private lemma exists_pos_six {c₁ d₁ c₂ d₂ c₃ d₃ c₄ d₄ c₅ d₅ c₆ d₆ : ℝ}
    (h₁ : 0 < c₁ ∨ (c₁ = 0 ∧ 0 < d₁)) (h₂ : 0 < c₂ ∨ (c₂ = 0 ∧ 0 < d₂))
    (h₃ : 0 < c₃ ∨ (c₃ = 0 ∧ 0 < d₃)) (h₄ : 0 < c₄ ∨ (c₄ = 0 ∧ 0 < d₄))
    (h₅ : 0 < c₅ ∨ (c₅ = 0 ∧ 0 < d₅)) (h₆ : 0 < c₆ ∨ (c₆ = 0 ∧ 0 < d₆)) :
    ∃ t : ℝ, 0 < t ∧
      0 < c₁ + t * d₁ ∧ 0 < c₂ + t * d₂ ∧ 0 < c₃ + t * d₃ ∧
      0 < c₄ + t * d₄ ∧ 0 < c₅ + t * d₅ ∧ 0 < c₆ + t * d₆ := by
  obtain ⟨t₁, ht₁, H₁⟩ := exists_pos_pair c₁ d₁ h₁
  obtain ⟨t₂, ht₂, H₂⟩ := exists_pos_pair c₂ d₂ h₂
  obtain ⟨t₃, ht₃, H₃⟩ := exists_pos_pair c₃ d₃ h₃
  obtain ⟨t₄, ht₄, H₄⟩ := exists_pos_pair c₄ d₄ h₄
  obtain ⟨t₅, ht₅, H₅⟩ := exists_pos_pair c₅ d₅ h₅
  obtain ⟨t₆, ht₆, H₆⟩ := exists_pos_pair c₆ d₆ h₆
  let t := min (min (min t₁ t₂) (min t₃ t₄)) (min t₅ t₆)
  have ht : 0 < t := lt_min (lt_min (lt_min ht₁ ht₂) (lt_min ht₃ ht₄)) (lt_min ht₅ ht₆)
  refine ⟨t, ht,
    H₁ t ht (le_trans (le_trans (min_le_left _ _) (min_le_left _ _)) (min_le_left _ _)),
    H₂ t ht (le_trans (le_trans (min_le_left _ _) (min_le_left _ _)) (min_le_right _ _)),
    H₃ t ht (le_trans (le_trans (min_le_left _ _) (min_le_right _ _)) (min_le_left _ _)),
    H₄ t ht (le_trans (le_trans (min_le_left _ _) (min_le_right _ _)) (min_le_right _ _)),
    H₅ t ht (le_trans (min_le_right _ _) (min_le_left _ _)),
    H₆ t ht (le_trans (min_le_right _ _) (min_le_right _ _))⟩

/-! ## Section 2: General-Position Convex-Hull Point Configuration and State Graph -/

/-- A planar point set `Q` of size `2n` in general position (`n ≥ 3`) with `n` convex-hull
vertices `Q 0, ..., Q (n - 1)` in counterclockwise cyclic order (indices modulo `n`) and
`n` interior points `B 0, ..., B (n - 1)`. -/
structure PointConfig (n : ℕ) [NeZero n] where
  hn : 3 ≤ n
  Q : Fin n → Pt
  B : Fin n → Pt
  inj : Function.Injective (Sum.elim Q B)
  general_position : ∀ p q r : Fin n ⊕ Fin n,
    p ≠ q → q ≠ r → p ≠ r →
      orient (Sum.elim Q B p) (Sum.elim Q B q) (Sum.elim Q B r) ≠ 0
  hull_ccw : ∀ k m : Fin n, m ≠ k → m ≠ k + 1 →
    0 < orient (Q k) (Q (k + 1)) (Q m)
  interior_pos : ∀ k r : Fin n, 0 < orient (Q k) (Q (k + 1)) (B r)

namespace PointConfig

variable {n : ℕ} [NeZero n] (cfg : PointConfig n)

/-- Oriented edge-height function `ℓ_k(X) = det(Q_{k+1} - Q_k, X - Q_k)`. -/
def edgeHeight (k : Fin n) (X : Pt) : ℝ :=
  orient (cfg.Q k) (cfg.Q (k + 1)) X

lemma edgeHeight_Q_left (k : Fin n) : cfg.edgeHeight k (cfg.Q k) = 0 :=
  orient_self_left _ _

lemma edgeHeight_Q_right (k : Fin n) : cfg.edgeHeight k (cfg.Q (k + 1)) = 0 :=
  orient_self_right _ _

lemma edgeHeight_B_pos (k r : Fin n) : 0 < cfg.edgeHeight k (cfg.B r) :=
  cfg.interior_pos k r

lemma edgeHeight_Q_nonneg (k m : Fin n) : 0 ≤ cfg.edgeHeight k (cfg.Q m) := by
  by_cases h1 : m = k
  · subst h1; exact (cfg.edgeHeight_Q_left m).ge
  · by_cases h2 : m = k + 1
    · subst h2; exact (cfg.edgeHeight_Q_right k).ge
    · exact (cfg.hull_ccw k m h1 h2).le

include cfg in
lemma fin_succ_ne_self (k : Fin n) : k + 1 ≠ k := by
  intro h
  have h1 : (1 : Fin n) = 0 := by
    have := congrArg (· - k) h
    simpa using this
  have hv := congrArg Fin.val h1
  have hlt : 1 < n := by have := cfg.hn; omega
  simp [Nat.mod_eq_of_lt hlt] at hv

include cfg in
lemma fin_edges_distinct {i j : Fin n} (hij : i ≠ j) :
    ¬ ((i = j ∨ i = j + 1) ∧ (i + 1 = j ∨ i + 1 = j + 1)) := by
  rintro ⟨hi1 | hi2, hi3 | hi4⟩
  · exact hij hi1
  · exact hij (add_right_cancel hi4)
  · have h2 : (1 : Fin n) + 1 = 0 := by
      have : j + (1 + 1) = j + 0 := by rw [← add_assoc, ← hi2, hi3, add_zero]
      exact add_left_cancel this
    have hv := congrArg Fin.val h2
    have hlt : 2 < n := by have := cfg.hn; omega
    have hv1 : ((1 : Fin n) : ℕ) = 1 := by
      rw [Fin.val_one']
      exact Nat.mod_eq_of_lt (by omega)
    rw [Fin.val_add, hv1, Fin.val_zero, Nat.mod_eq_of_lt (by omega)] at hv
    omega
  · exact hij (add_right_cancel hi4)

/-- Lemma 2(4): for `i ≠ j`, `ℓ_j(Q_i) ≥ 0`, `ℓ_j(Q_{i+1}) ≥ 0`, and `ℓ_j(Q_i) + ℓ_j(Q_{i+1}) > 0`. -/
lemma edgeHeight_pair_pos {i j : Fin n} (hij : i ≠ j) :
    0 ≤ cfg.edgeHeight j (cfg.Q i) ∧
    0 ≤ cfg.edgeHeight j (cfg.Q (i + 1)) ∧
    0 < cfg.edgeHeight j (cfg.Q i) + cfg.edgeHeight j (cfg.Q (i + 1)) := by
  refine ⟨cfg.edgeHeight_Q_nonneg j i, cfg.edgeHeight_Q_nonneg j (i + 1), ?_⟩
  by_cases hi : i = j ∨ i = j + 1
  · have hi1 : i + 1 ≠ j ∧ i + 1 ≠ j + 1 := by
      have hne := cfg.fin_edges_distinct hij
      tauto
    have hpos : 0 < cfg.edgeHeight j (cfg.Q (i + 1)) := cfg.hull_ccw j (i + 1) hi1.1 hi1.2
    linarith [cfg.edgeHeight_Q_nonneg j i]
  · push Not at hi
    have hpos : 0 < cfg.edgeHeight j (cfg.Q i) := cfg.hull_ccw j i hi.1 hi.2
    linarith [cfg.edgeHeight_Q_nonneg j (i + 1)]

/-- Closed triangle `T_k(r) = △ Q_k Q_{k+1} B_r`. -/
def Tri (k r : Fin n) (X : Pt) : Prop :=
  InClosedTri (cfg.Q k) (cfg.Q (k + 1)) (cfg.B r) X

/-- Open interior `int(T_k(r))`. -/
def OpenTri (k r : Fin n) (X : Pt) : Prop :=
  InOpenTri (cfg.Q k) (cfg.Q (k + 1)) (cfg.B r) X

/-- Nontrivial intersection of `T_i(a)` and `T_j(b)`: they share a point `X` that is not
a common convex-hull vertex in `{Q_i, Q_{i+1}} ∩ {Q_j, Q_{j+1}}`. -/
def TrianglesIntersect (i j a b : Fin n) : Prop :=
  ∃ X : Pt, cfg.Tri i a X ∧ cfg.Tri j b X ∧
    ¬ ((X = cfg.Q i ∨ X = cfg.Q (i + 1)) ∧ (X = cfg.Q j ∨ X = cfg.Q (j + 1)))

/-- Directed edge `π → ρ` in Bui's Section 8.2 state graph `G`:
swapping two indices `i ≠ j` whose matched triangles `T_i(π)` and `T_j(π)` intersect. -/
def StateEdge (π ρ : Equiv.Perm (Fin n)) : Prop :=
  ∃ i j : Fin n, i ≠ j ∧
    ρ i = π j ∧ ρ j = π i ∧ (∀ k : Fin n, k ≠ i → k ≠ j → ρ k = π k) ∧
    cfg.TrianglesIntersect i j (π i) (π j)

/-! ## Section 3: Lemma 1 (General-Position Intersection Equivalence) -/

private lemma transverse_edges {p₁ q₁ p₂ q₂ : Fin n ⊕ Fin n} {X : Pt}
    (hpq₁ : p₁ ≠ q₁) (hpq₂ : p₂ ≠ q₂)
    (hdiff : ¬ ((p₁ = p₂ ∧ q₁ = q₂) ∨ (p₁ = q₂ ∧ q₁ = p₂)))
    (h1 : orient (Sum.elim cfg.Q cfg.B p₁) (Sum.elim cfg.Q cfg.B q₁) X = 0)
    (h2 : orient (Sum.elim cfg.Q cfg.B p₂) (Sum.elim cfg.Q cfg.B q₂) X = 0) :
    det2
      ((Sum.elim cfg.Q cfg.B q₁).1 - (Sum.elim cfg.Q cfg.B p₁).1,
       (Sum.elim cfg.Q cfg.B q₁).2 - (Sum.elim cfg.Q cfg.B p₁).2)
      ((Sum.elim cfg.Q cfg.B q₂).1 - (Sum.elim cfg.Q cfg.B p₂).1,
       (Sum.elim cfg.Q cfg.B q₂).2 - (Sum.elim cfg.Q cfg.B p₂).2) ≠ 0 := by
  intro hdet
  set P₁ := Sum.elim cfg.Q cfg.B p₁
  set Q₁ := Sum.elim cfg.Q cfg.B q₁
  set P₂ := Sum.elim cfg.Q cfg.B p₂
  set Q₂ := Sum.elim cfg.Q cfg.B q₂
  have hQ₁P₁ : Q₁.1 - P₁.1 ≠ 0 ∨ Q₁.2 - P₁.2 ≠ 0 := by
    by_contra h
    push Not at h
    have hEq : Q₁ = P₁ := Prod.ext (sub_eq_zero.mp h.1) (sub_eq_zero.mp h.2)
    exact hpq₁ (cfg.inj hEq).symm
  have hQ₂P₂ : Q₂.1 - P₂.1 ≠ 0 ∨ Q₂.2 - P₂.2 ≠ 0 := by
    by_contra h
    push Not at h
    have hEq : Q₂ = P₂ := Prod.ext (sub_eq_zero.mp h.1) (sub_eq_zero.mp h.2)
    exact hpq₂ (cfg.inj hEq).symm
  -- Algebraically, collinearity of `X` on both lines plus parallel directions forces `P₂` and `Q₂` onto line `P₁ Q₁`.
  have hcol : orient P₁ Q₁ P₂ = 0 ∧ orient P₁ Q₁ Q₂ = 0 := by
    have hmul_x : (Q₂.1 - P₂.1) * orient P₁ Q₁ P₂ = 0 := by
      have hid : (Q₂.1 - P₂.1) * orient P₁ Q₁ P₂ =
          (Q₂.1 - P₂.1) * orient P₁ Q₁ X -
          (Q₁.1 - P₁.1) * orient P₂ Q₂ X -
          (X.1 - P₂.1) * det2 (Q₁.1 - P₁.1, Q₁.2 - P₁.2) (Q₂.1 - P₂.1, Q₂.2 - P₂.2) := by
        unfold orient det2; ring
      rw [hid, h1, h2, hdet]; ring
    have hmul_y : (Q₂.2 - P₂.2) * orient P₁ Q₁ P₂ = 0 := by
      have hid : (Q₂.2 - P₂.2) * orient P₁ Q₁ P₂ =
          (Q₂.2 - P₂.2) * orient P₁ Q₁ X -
          (Q₁.2 - P₁.2) * orient P₂ Q₂ X -
          (X.2 - P₂.2) * det2 (Q₁.1 - P₁.1, Q₁.2 - P₁.2) (Q₂.1 - P₂.1, Q₂.2 - P₂.2) := by
        unfold orient det2; ring
      rw [hid, h1, h2, hdet]; ring
    have hP₂ : orient P₁ Q₁ P₂ = 0 := by
      rcases hQ₂P₂ with hx | hy
      · exact (mul_eq_zero.mp hmul_x).resolve_left hx
      · exact (mul_eq_zero.mp hmul_y).resolve_left hy
    have hQ₂ : orient P₁ Q₁ Q₂ = 0 := by
      have hid : orient P₁ Q₁ Q₂ = orient P₁ Q₁ P₂ +
          det2 (Q₁.1 - P₁.1, Q₁.2 - P₁.2) (Q₂.1 - P₂.1, Q₂.2 - P₂.2) := by
        unfold orient det2; ring
      rw [hid, hP₂, hdet, add_zero]
    exact ⟨hP₂, hQ₂⟩
  by_cases hp₂ : p₂ ≠ p₁ ∧ p₂ ≠ q₁
  · exact cfg.general_position p₁ q₁ p₂ hpq₁ hp₂.2.symm hp₂.1.symm hcol.1
  · by_cases hq₂ : q₂ ≠ p₁ ∧ q₂ ≠ q₁
    · exact cfg.general_position p₁ q₁ q₂ hpq₁ hq₂.2.symm hq₂.1.symm hcol.2
    · push Not at hp₂ hq₂
      by_cases h1p : p₂ = p₁
      · have h1q : q₂ = q₁ := by
          by_cases hq : q₂ = p₁
          · exact absurd (h1p.trans hq.symm) hpq₂
          · exact hq₂ hq
        exact hdiff (Or.inl ⟨h1p.symm, h1q.symm⟩)
      · have h1p' : p₂ = q₁ := hp₂ h1p
        have h1q' : q₂ = p₁ := by
          by_contra hq
          have : q₂ = q₁ := hq₂ hq
          exact hpq₂ (h1p'.trans this.symm)
        exact hdiff (Or.inr ⟨h1q'.symm, h1p'.symm⟩)

private lemma open_inter_of_edge_cross
    {A₁ B₁ C₁ A₂ B₂ C₂ X : Pt}
    (hD₁ : 0 < orient A₁ B₁ C₁) (hD₂ : 0 < orient A₂ B₂ C₂)
    (u₁ u₂ u₃ v₁ v₂ v₃ : ℝ)
    (hu₁ : u₁ = orient B₁ C₁ X) (hu₂ : u₂ = orient C₁ A₁ X) (hu₃ : u₃ = orient A₁ B₁ X)
    (hv₁ : v₁ = orient B₂ C₂ X) (hv₂ : v₂ = orient C₂ A₂ X) (hv₃ : v₃ = orient A₂ B₂ X)
    (hpos₁ : 0 < u₁) (hpos₂ : 0 < u₂) (hzero₃ : u₃ = 0)
    (hpos₄ : 0 < v₁) (hpos₅ : 0 < v₂) (hzero₆ : v₃ = 0)
    (hdet : det2 (B₁.1 - A₁.1, B₁.2 - A₁.2) (B₂.1 - A₂.1, B₂.2 - A₂.2) ≠ 0) :
    ∃ Z : Pt, InOpenTri A₁ B₁ C₁ Z ∧ InOpenTri A₂ B₂ C₂ Z := by
  let r₁ : Pt := (B₁.1 - A₁.1, B₁.2 - A₁.2)
  let r₂ : Pt := (B₂.1 - A₂.1, B₂.2 - A₂.2)
  let Δ : ℝ := det2 r₁ r₂
  let w : Pt := ((r₂.1 - r₁.1) / Δ, (r₂.2 - r₁.2) / Δ)
  have hdw₁ : det2 r₁ w = 1 := by
    have hnum : det2 r₁ (r₂.1 - r₁.1, r₂.2 - r₁.2) = Δ := by dsimp [Δ, det2]; ring
    have hdiv : det2 r₁ w = det2 r₁ (r₂.1 - r₁.1, r₂.2 - r₁.2) / Δ := by dsimp [w, det2]; ring
    rw [hdiv, hnum, div_self hdet]
  have hdw₂ : det2 r₂ w = 1 := by
    have hnum : det2 r₂ (r₂.1 - r₁.1, r₂.2 - r₁.2) = Δ := by dsimp [Δ, det2]; ring
    have hdiv : det2 r₂ w = det2 r₂ (r₂.1 - r₁.1, r₂.2 - r₁.2) / Δ := by dsimp [w, det2]; ring
    rw [hdiv, hnum, div_self hdet]
  obtain ⟨t, ht, h1, h2, h3, h4, h5, h6⟩ := exists_pos_six
    (d₁ := det2 (C₁.1 - B₁.1, C₁.2 - B₁.2) w)
    (d₂ := det2 (A₁.1 - C₁.1, A₁.2 - C₁.2) w)
    (d₃ := det2 r₁ w)
    (d₄ := det2 (C₂.1 - B₂.1, C₂.2 - B₂.2) w)
    (d₅ := det2 (A₂.1 - C₂.1, A₂.2 - C₂.2) w)
    (d₆ := det2 r₂ w)
    (Or.inl hpos₁) (Or.inl hpos₂) (Or.inr ⟨hzero₃, by rw [hdw₁]; exact one_pos⟩)
    (Or.inl hpos₄) (Or.inl hpos₅) (Or.inr ⟨hzero₆, by rw [hdw₂]; exact one_pos⟩)
  refine ⟨(X.1 + t * w.1, X.2 + t * w.2), ?_, ?_⟩
  · rw [inOpenTri_iff hD₁, orient_shift, orient_shift, orient_shift, ← hu₁, ← hu₂, ← hu₃]
    exact ⟨h1, h2, h3⟩
  · rw [inOpenTri_iff hD₂, orient_shift, orient_shift, orient_shift, ← hv₁, ← hv₂, ← hv₃]
    exact ⟨h4, h5, h6⟩

/-- **Lemma 1 (General-Position Intersection Equivalence):**
For any `i ≠ j` and `a ≠ b`, the closed triangles `T_i(a)` and `T_j(b)` intersect nontrivially
if and only if their open interiors intersect. -/
theorem trianglesIntersect_iff_open {i j a b : Fin n} (hij : i ≠ j) (hab : a ≠ b) :
    cfg.TrianglesIntersect i j a b ↔ ∃ Z : Pt, cfg.OpenTri i a Z ∧ cfg.OpenTri j b Z := by
  have hD₁ : 0 < orient (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) := cfg.interior_pos i a
  have hD₂ : 0 < orient (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) := cfg.interior_pos j b
  constructor
  · rintro ⟨X, hXi, hXj, hnotshared⟩
    have hi_le := (inClosedTri_iff hD₁).mp hXi
    have hj_le := (inClosedTri_iff hD₂).mp hXj
    -- Case A: `X` is already in `OpenTri i a`
    by_cases hopen_i : 0 < orient (cfg.Q (i + 1)) (cfg.B a) X ∧
        0 < orient (cfg.B a) (cfg.Q i) X ∧ 0 < orient (cfg.Q i) (cfg.Q (i + 1)) X
    · let Cj : Pt := comb3 (1 / 3) (1 / 3) (1 / 3) (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b)
      let w : Pt := (Cj.1 - X.1, Cj.2 - X.2)
      have hCj : orient (cfg.Q (j + 1)) (cfg.B b) Cj =
            orient (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) / 3 ∧
          orient (cfg.B b) (cfg.Q j) Cj =
            orient (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) / 3 ∧
          orient (cfg.Q j) (cfg.Q (j + 1)) Cj =
            orient (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) / 3 := by
        dsimp [Cj]
        refine ⟨?_, ?_, ?_⟩
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right, orient_cyc]; ring
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right, orient_cyc']; ring
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right]; ring
      have hdiff_o : ∀ P Q : Pt, det2 (Q.1 - P.1, Q.2 - P.2) w = orient P Q Cj - orient P Q X := by
        intro P Q; dsimp [w]; unfold orient det2; ring
      have hcond : ∀ P Q : Pt, 0 ≤ orient P Q X → 0 < orient P Q Cj →
          0 < orient P Q X ∨ (orient P Q X = 0 ∧ 0 < det2 (Q.1 - P.1, Q.2 - P.2) w) := by
        intro P Q hle hpos
        rcases lt_or_eq_of_le hle with hlt | heq
        · exact Or.inl hlt
        · exact Or.inr ⟨heq.symm, by rw [hdiff_o, ← heq, sub_zero]; exact hpos⟩
      obtain ⟨t, _, h1, h2, h3, h4, h5, h6⟩ := exists_pos_six
        (Or.inl hopen_i.1) (Or.inl hopen_i.2.1) (Or.inl hopen_i.2.2)
        (hcond _ _ hj_le.1 (by rw [hCj.1]; linarith))
        (hcond _ _ hj_le.2.1 (by rw [hCj.2.1]; linarith))
        (hcond _ _ hj_le.2.2 (by rw [hCj.2.2]; linarith))
      refine ⟨(X.1 + t * w.1, X.2 + t * w.2), ?_, ?_⟩
      · rw [OpenTri, inOpenTri_iff hD₁, orient_shift, orient_shift, orient_shift]
        exact ⟨h1, h2, h3⟩
      · rw [OpenTri, inOpenTri_iff hD₂, orient_shift, orient_shift, orient_shift]
        exact ⟨h4, h5, h6⟩
    -- Case B: `X` is already in `OpenTri j b`
    by_cases hopen_j : 0 < orient (cfg.Q (j + 1)) (cfg.B b) X ∧
        0 < orient (cfg.B b) (cfg.Q j) X ∧ 0 < orient (cfg.Q j) (cfg.Q (j + 1)) X
    · let Ci : Pt := comb3 (1 / 3) (1 / 3) (1 / 3) (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a)
      let w : Pt := (Ci.1 - X.1, Ci.2 - X.2)
      have hCi : orient (cfg.Q (i + 1)) (cfg.B a) Ci =
            orient (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) / 3 ∧
          orient (cfg.B a) (cfg.Q i) Ci =
            orient (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) / 3 ∧
          orient (cfg.Q i) (cfg.Q (i + 1)) Ci =
            orient (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) / 3 := by
        dsimp [Ci]
        refine ⟨?_, ?_, ?_⟩
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right, orient_cyc]; ring
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right, orient_cyc']; ring
        · rw [orient_comb3 (by norm_num), orient_self_left, orient_self_right]; ring
      have hdiff_o : ∀ P Q : Pt, det2 (Q.1 - P.1, Q.2 - P.2) w = orient P Q Ci - orient P Q X := by
        intro P Q; dsimp [w]; unfold orient det2; ring
      have hcond : ∀ P Q : Pt, 0 ≤ orient P Q X → 0 < orient P Q Ci →
          0 < orient P Q X ∨ (orient P Q X = 0 ∧ 0 < det2 (Q.1 - P.1, Q.2 - P.2) w) := by
        intro P Q hle hpos
        rcases lt_or_eq_of_le hle with hlt | heq
        · exact Or.inl hlt
        · exact Or.inr ⟨heq.symm, by rw [hdiff_o, ← heq, sub_zero]; exact hpos⟩
      obtain ⟨t, _, h1, h2, h3, h4, h5, h6⟩ := exists_pos_six
        (hcond _ _ hi_le.1 (by rw [hCi.1]; linarith))
        (hcond _ _ hi_le.2.1 (by rw [hCi.2.1]; linarith))
        (hcond _ _ hi_le.2.2 (by rw [hCi.2.2]; linarith))
        (Or.inl hopen_j.1) (Or.inl hopen_j.2.1) (Or.inl hopen_j.2.2)
      refine ⟨(X.1 + t * w.1, X.2 + t * w.2), ?_, ?_⟩
      · rw [OpenTri, inOpenTri_iff hD₁, orient_shift, orient_shift, orient_shift]
        exact ⟨h1, h2, h3⟩
      · rw [OpenTri, inOpenTri_iff hD₂, orient_shift, orient_shift, orient_shift]
        exact ⟨h4, h5, h6⟩
    -- Case C: `X ∈ ∂T_i ∩ ∂T_j`. Show `X` is neither a vertex of `T_i` nor of `T_j`.
    have hvtx_rule : ∀ (p q r s : Fin n ⊕ Fin n),
        p ≠ q → p ≠ r → p ≠ s → q ≠ r → q ≠ s → r ≠ s →
        X = Sum.elim cfg.Q cfg.B p →
        orient (Sum.elim cfg.Q cfg.B q) (Sum.elim cfg.Q cfg.B r) X = 0 ∨
        orient (Sum.elim cfg.Q cfg.B r) (Sum.elim cfg.Q cfg.B s) X = 0 ∨
        orient (Sum.elim cfg.Q cfg.B s) (Sum.elim cfg.Q cfg.B q) X = 0 → False := by
      intro p q r s hpq hpr hps hqr hqs hrs hXp hor
      rw [hXp] at hor
      rcases hor with h | h | h
      · exact cfg.general_position q r p hqr hpr.symm hpq.symm h
      · exact cfg.general_position r s p hrs hps.symm hpr.symm h
      · exact cfg.general_position s q p hqs.symm hpq.symm hps.symm h
    -- Helper: if two orientations vanish on a non-degenerate triangle, `X` equals the opposite vertex.
    have htwo_zero : ∀ (A B C : Pt), 0 < orient A B C →
        orient B C X = 0 → orient C A X = 0 → X = C := by
      intro A B C hD h1 h2
      have h3 : orient A B X = orient A B C := by
        have := orient_sum_eq A B C X; linarith
      have hx := cramer_fst A B C X
      have hy := cramer_snd A B C X
      rw [h1, h2, h3] at hx hy
      have hDne : orient A B C ≠ 0 := ne_of_gt hD
      ext
      · exact mul_left_cancel₀ hDne (by linarith)
      · exact mul_left_cancel₀ hDne (by linarith)
    have hj_zero : orient (cfg.Q (j + 1)) (cfg.B b) X = 0 ∨
        orient (cfg.B b) (cfg.Q j) X = 0 ∨ orient (cfg.Q j) (cfg.Q (j + 1)) X = 0 := by
      by_contra h
      push Not at h
      exact hopen_j ⟨lt_of_le_of_ne hj_le.1 (Ne.symm h.1),
        lt_of_le_of_ne hj_le.2.1 (Ne.symm h.2.1),
        lt_of_le_of_ne hj_le.2.2 (Ne.symm h.2.2)⟩
    have hi_zero : orient (cfg.Q (i + 1)) (cfg.B a) X = 0 ∨
        orient (cfg.B a) (cfg.Q i) X = 0 ∨ orient (cfg.Q i) (cfg.Q (i + 1)) X = 0 := by
      by_contra h
      push Not at h
      exact hopen_i ⟨lt_of_le_of_ne hi_le.1 (Ne.symm h.1),
        lt_of_le_of_ne hi_le.2.1 (Ne.symm h.2.1),
        lt_of_le_of_ne hi_le.2.2 (Ne.symm h.2.2)⟩
    -- Rule out `X` being any vertex of `T_i` or `T_j`.
    have hX_ne_Ba : X ≠ cfg.B a := by
      intro hX
      exact hvtx_rule (Sum.inr a) (Sum.inl (j + 1)) (Sum.inr b) (Sum.inl j)
        (by simp) (by simp [hab]) (by simp) (by simp) (by simp [cfg.fin_succ_ne_self j]) (by simp)
        hX (by simpa [Sum.elim] using hj_zero)
    have hX_ne_Bb : X ≠ cfg.B b := by
      intro hX
      exact hvtx_rule (Sum.inr b) (Sum.inl (i + 1)) (Sum.inr a) (Sum.inl i)
        (by simp) (by simp [hab.symm]) (by simp) (by simp) (by simp [cfg.fin_succ_ne_self i]) (by simp)
        hX (by simpa [Sum.elim] using hi_zero)
    have hX_ne_Qi : X ≠ cfg.Q i := by
      intro hX
      have hnotj : i ≠ j ∧ i ≠ j + 1 := by
        constructor
        · exact hij
        · intro heq; exact hnotshared ⟨Or.inl hX, Or.inr (by rw [hX, heq])⟩
      exact hvtx_rule (Sum.inl i) (Sum.inl (j + 1)) (Sum.inr b) (Sum.inl j)
        (by simp [hnotj.2]) (by simp) (by simp [hnotj.1]) (by simp)
        (by simp [cfg.fin_succ_ne_self j]) (by simp)
        hX (by simpa [Sum.elim] using hj_zero)
    have hX_ne_Qi1 : X ≠ cfg.Q (i + 1) := by
      intro hX
      have hnotj : i + 1 ≠ j ∧ i + 1 ≠ j + 1 := by
        constructor
        · intro heq; exact hnotshared ⟨Or.inr hX, Or.inl (by rw [hX, heq])⟩
        · intro heq; exact hij (add_right_cancel heq)
      exact hvtx_rule (Sum.inl (i + 1)) (Sum.inl (j + 1)) (Sum.inr b) (Sum.inl j)
        (by simp [hnotj.2]) (by simp) (by simp [hnotj.1]) (by simp)
        (by simp [cfg.fin_succ_ne_self j]) (by simp)
        hX (by simpa [Sum.elim] using hj_zero)
    have hX_ne_Qj : X ≠ cfg.Q j := by
      intro hX
      have hnoti : j ≠ i ∧ j ≠ i + 1 := by
        constructor
        · exact hij.symm
        · intro heq; exact hnotshared ⟨Or.inr (by rw [hX, heq]), Or.inl hX⟩
      exact hvtx_rule (Sum.inl j) (Sum.inl (i + 1)) (Sum.inr a) (Sum.inl i)
        (by simp [hnoti.2]) (by simp) (by simp [hnoti.1]) (by simp)
        (by simp [cfg.fin_succ_ne_self i]) (by simp)
        hX (by simpa [Sum.elim] using hi_zero)
    have hX_ne_Qj1 : X ≠ cfg.Q (j + 1) := by
      intro hX
      have hnoti : j + 1 ≠ i ∧ j + 1 ≠ i + 1 := by
        constructor
        · intro heq; exact hnotshared ⟨Or.inl (by rw [hX, heq]), Or.inr hX⟩
        · intro heq; exact hij (add_right_cancel heq).symm
      exact hvtx_rule (Sum.inl (j + 1)) (Sum.inl (i + 1)) (Sum.inr a) (Sum.inl i)
        (by simp [hnoti.2]) (by simp) (by simp [hnoti.1]) (by simp)
        (by simp [cfg.fin_succ_ne_self i]) (by simp)
        hX (by simpa [Sum.elim] using hi_zero)
    -- Therefore exactly one edge of `T_i` and one edge of `T_j` vanish at `X`.
    -- Package each triangle by rotating the vanishing edge to the third position `(A, B)`.
    have hrot_i : ∃ p₁ q₁ r₁ : Fin n ⊕ Fin n,
        p₁ ≠ q₁ ∧ p₁ ≠ r₁ ∧ q₁ ≠ r₁ ∧
        (p₁, q₁, r₁) ∈
          [(Sum.inl i, Sum.inl (i + 1), Sum.inr a),
           (Sum.inl (i + 1), Sum.inr a, Sum.inl i),
           (Sum.inr a, Sum.inl i, Sum.inl (i + 1))] ∧
        0 < orient (Sum.elim cfg.Q cfg.B p₁) (Sum.elim cfg.Q cfg.B q₁) (Sum.elim cfg.Q cfg.B r₁) ∧
        0 < orient (Sum.elim cfg.Q cfg.B q₁) (Sum.elim cfg.Q cfg.B r₁) X ∧
        0 < orient (Sum.elim cfg.Q cfg.B r₁) (Sum.elim cfg.Q cfg.B p₁) X ∧
        orient (Sum.elim cfg.Q cfg.B p₁) (Sum.elim cfg.Q cfg.B q₁) X = 0 := by
      have hne_i : i ≠ i + 1 := (cfg.fin_succ_ne_self i).symm
      rcases hi_zero with hz1 | hz2 | hz3
      · refine ⟨Sum.inl (i + 1), Sum.inr a, Sum.inl i, by simp, by simp [hne_i.symm], by simp,
          by simp, by simpa [Sum.elim, orient_cyc] using hD₁, ?_, ?_, hz1⟩
        · exact lt_of_le_of_ne hi_le.2.1 fun heq =>
            hX_ne_Ba (htwo_zero (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) hD₁ hz1 heq.symm)
        · exact lt_of_le_of_ne hi_le.2.2 fun heq =>
            hX_ne_Qi1 (htwo_zero (cfg.B a) (cfg.Q i) (cfg.Q (i + 1))
              (by rwa [orient_cyc']) heq.symm hz1)
      · refine ⟨Sum.inr a, Sum.inl i, Sum.inl (i + 1), by simp, by simp, by simp [hne_i],
          by simp, by simpa [Sum.elim, orient_cyc'] using hD₁, ?_, ?_, hz2⟩
        · exact lt_of_le_of_ne hi_le.2.2 fun heq =>
            hX_ne_Qi (htwo_zero (cfg.Q (i + 1)) (cfg.B a) (cfg.Q i)
              (by rwa [orient_cyc]) hz2 (by simpa using heq.symm))
        · exact lt_of_le_of_ne hi_le.1 fun heq =>
            hX_ne_Ba (htwo_zero (cfg.Q i) (cfg.Q (i + 1)) (cfg.B a) hD₁ heq.symm hz2)
      · refine ⟨Sum.inl i, Sum.inl (i + 1), Sum.inr a, by simp [hne_i], by simp, by simp,
          by simp, hD₁, ?_, ?_, hz3⟩
        · exact lt_of_le_of_ne hi_le.1 fun heq =>
            hX_ne_Qi1 (htwo_zero (cfg.B a) (cfg.Q i) (cfg.Q (i + 1))
              (by rwa [orient_cyc']) hz3 heq.symm)
        · exact lt_of_le_of_ne hi_le.2.1 fun heq =>
            hX_ne_Qi (htwo_zero (cfg.Q (i + 1)) (cfg.B a) (cfg.Q i)
              (by rwa [orient_cyc]) heq.symm hz3)
    have hrot_j : ∃ p₂ q₂ r₂ : Fin n ⊕ Fin n,
        p₂ ≠ q₂ ∧ p₂ ≠ r₂ ∧ q₂ ≠ r₂ ∧
        (p₂, q₂, r₂) ∈
          [(Sum.inl j, Sum.inl (j + 1), Sum.inr b),
           (Sum.inl (j + 1), Sum.inr b, Sum.inl j),
           (Sum.inr b, Sum.inl j, Sum.inl (j + 1))] ∧
        0 < orient (Sum.elim cfg.Q cfg.B p₂) (Sum.elim cfg.Q cfg.B q₂) (Sum.elim cfg.Q cfg.B r₂) ∧
        0 < orient (Sum.elim cfg.Q cfg.B q₂) (Sum.elim cfg.Q cfg.B r₂) X ∧
        0 < orient (Sum.elim cfg.Q cfg.B r₂) (Sum.elim cfg.Q cfg.B p₂) X ∧
        orient (Sum.elim cfg.Q cfg.B p₂) (Sum.elim cfg.Q cfg.B q₂) X = 0 := by
      have hne_j : j ≠ j + 1 := (cfg.fin_succ_ne_self j).symm
      rcases hj_zero with hz1 | hz2 | hz3
      · refine ⟨Sum.inl (j + 1), Sum.inr b, Sum.inl j, by simp, by simp [hne_j.symm], by simp,
          by simp, by simpa [Sum.elim, orient_cyc] using hD₂, ?_, ?_, hz1⟩
        · exact lt_of_le_of_ne hj_le.2.1 fun heq =>
            hX_ne_Bb (htwo_zero (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) hD₂ hz1 heq.symm)
        · exact lt_of_le_of_ne hj_le.2.2 fun heq =>
            hX_ne_Qj1 (htwo_zero (cfg.B b) (cfg.Q j) (cfg.Q (j + 1))
              (by rwa [orient_cyc']) heq.symm hz1)
      · refine ⟨Sum.inr b, Sum.inl j, Sum.inl (j + 1), by simp, by simp, by simp [hne_j],
          by simp, by simpa [Sum.elim, orient_cyc'] using hD₂, ?_, ?_, hz2⟩
        · exact lt_of_le_of_ne hj_le.2.2 fun heq =>
            hX_ne_Qj (htwo_zero (cfg.Q (j + 1)) (cfg.B b) (cfg.Q j)
              (by rwa [orient_cyc]) hz2 (by simpa using heq.symm))
        · exact lt_of_le_of_ne hj_le.1 fun heq =>
            hX_ne_Bb (htwo_zero (cfg.Q j) (cfg.Q (j + 1)) (cfg.B b) hD₂ heq.symm hz2)
      · refine ⟨Sum.inl j, Sum.inl (j + 1), Sum.inr b, by simp [hne_j], by simp, by simp,
          by simp, hD₂, ?_, ?_, hz3⟩
        · exact lt_of_le_of_ne hj_le.1 fun heq =>
            hX_ne_Qj1 (htwo_zero (cfg.B b) (cfg.Q j) (cfg.Q (j + 1))
              (by rwa [orient_cyc']) hz3 heq.symm)
        · exact lt_of_le_of_ne hj_le.2.1 fun heq =>
            hX_ne_Qj (htwo_zero (cfg.Q (j + 1)) (cfg.B b) (cfg.Q j)
              (by rwa [orient_cyc]) heq.symm hz3)
    obtain ⟨p₁, q₁, r₁, hpq₁, _, _, hmem₁, hDp₁, hp1, hp2, hz1⟩ := hrot_i
    obtain ⟨p₂, q₂, r₂, hpq₂, _, _, hmem₂, hDp₂, hq1, hq2, hz2⟩ := hrot_j
    -- Show the two vanishing edges `(p₁, q₁)` and `(p₂, q₂)` cannot have the same pair of endpoints.
    have hdiff_edges : ¬ ((p₁ = p₂ ∧ q₁ = q₂) ∨ (p₁ = q₂ ∧ q₁ = p₂)) := by
      have hed := cfg.fin_edges_distinct hij
      simp only [List.mem_cons, List.not_mem_nil, or_false, Prod.mk.injEq] at hmem₁ hmem₂
      rcases hmem₁ with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ <;>
        rcases hmem₂ with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ <;>
        simp [hab, hij]
      exact fun h1 h2 => hed ⟨Or.inr h1, Or.inl h2⟩
    have hdet := cfg.transverse_edges hpq₁ hpq₂ hdiff_edges hz1 hz2
    obtain ⟨Z, hZ₁, hZ₂⟩ := open_inter_of_edge_cross hDp₁ hDp₂ _ _ _ _ _ _
      rfl rfl rfl rfl rfl rfl hp1 hp2 hz1 hq1 hq2 hz2 hdet
    -- Un-rotate `InOpenTri` back to the canonical vertex order of `T_i(a)` and `T_j(b)`.
    refine ⟨Z, ?_, ?_⟩
    · rw [inOpenTri_iff hDp₁] at hZ₁
      rw [OpenTri, inOpenTri_iff hD₁]
      simp only [List.mem_cons, List.not_mem_nil, or_false, Prod.mk.injEq] at hmem₁
      rcases hmem₁ with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
      · exact hZ₁
      · exact ⟨hZ₁.2.2, hZ₁.1, hZ₁.2.1⟩
      · exact ⟨hZ₁.2.1, hZ₁.2.2, hZ₁.1⟩
    · rw [inOpenTri_iff hDp₂] at hZ₂
      rw [OpenTri, inOpenTri_iff hD₂]
      simp only [List.mem_cons, List.not_mem_nil, or_false, Prod.mk.injEq] at hmem₂
      rcases hmem₂ with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
      · exact hZ₂
      · exact ⟨hZ₂.2.2, hZ₂.1, hZ₂.2.1⟩
      · exact ⟨hZ₂.2.1, hZ₂.2.2, hZ₂.1⟩
  · rintro ⟨Z, hZi, hZj⟩
    have hZi_pos := (inOpenTri_iff hD₁).mp hZi
    have hZj_pos := (inOpenTri_iff hD₂).mp hZj
    refine ⟨Z, (inClosedTri_iff hD₁).mpr ⟨hZi_pos.1.le, hZi_pos.2.1.le, hZi_pos.2.2.le⟩,
      (inClosedTri_iff hD₂).mpr ⟨hZj_pos.1.le, hZj_pos.2.1.le, hZj_pos.2.2.le⟩, ?_⟩
    rintro ⟨hQi | hQi1, _⟩
    · rw [hQi, orient_self_left] at hZi_pos
      exact lt_irrefl 0 hZi_pos.2.2
    · rw [hQi1, orient_self_right] at hZi_pos
      exact lt_irrefl 0 hZi_pos.2.2

/-! ## Section 4: Lemma 3 (Strict Area-Product Decrease) and Potential Function -/

/-- **Lemma 3 (Strict Area-Product Decrease on Every Swap):**
If `i ≠ j`, `a ≠ b`, and `T_i(a)` and `T_j(b)` intersect nontrivially, then
`ℓ_i(B_b) * ℓ_j(B_a) < ℓ_i(B_a) * ℓ_j(B_b)`. -/
theorem area_product_strict_decrease {i j a b : Fin n} (hij : i ≠ j) (hab : a ≠ b)
    (hint : cfg.TrianglesIntersect i j a b) :
    cfg.edgeHeight i (cfg.B b) * cfg.edgeHeight j (cfg.B a) <
      cfg.edgeHeight i (cfg.B a) * cfg.edgeHeight j (cfg.B b) := by
  obtain ⟨Z, hZi, hZj⟩ := (cfg.trianglesIntersect_iff_open hij hab).mp hint
  rcases hZi with ⟨α₁, β₁, γ₁, hα₁, hβ₁, hγ₁, hsum₁, hZ₁⟩
  rcases hZj with ⟨α₂, β₂, γ₂, hα₂, hβ₂, hγ₂, hsum₂, hZ₂⟩
  -- Apply `ℓ_i` and `ℓ_j` to `Z ∈ int(T_i(a))`:
  have hli₁ : cfg.edgeHeight i Z = γ₁ * cfg.edgeHeight i (cfg.B a) := by
    simp only [edgeHeight]
    rw [hZ₁, orient_comb3 hsum₁, orient_self_left, orient_self_right]
    ring
  have hlj₁ : γ₁ * cfg.edgeHeight j (cfg.B a) < cfg.edgeHeight j Z := by
    obtain ⟨h1, h2, h3⟩ := cfg.edgeHeight_pair_pos hij
    have hpos : 0 < α₁ * cfg.edgeHeight j (cfg.Q i) + β₁ * cfg.edgeHeight j (cfg.Q (i + 1)) := by
      by_cases hq : 0 < cfg.edgeHeight j (cfg.Q i)
      · nlinarith
      · have hq2 : 0 < cfg.edgeHeight j (cfg.Q (i + 1)) := by linarith
        nlinarith
    simp only [edgeHeight] at hpos ⊢
    rw [hZ₁, orient_comb3 hsum₁]
    linarith
  -- Apply `ℓ_j` and `ℓ_i` to `Z ∈ int(T_j(b))`:
  have hlj₂ : cfg.edgeHeight j Z = γ₂ * cfg.edgeHeight j (cfg.B b) := by
    simp only [edgeHeight]
    rw [hZ₂, orient_comb3 hsum₂, orient_self_left, orient_self_right]
    ring
  have hli₂ : γ₂ * cfg.edgeHeight i (cfg.B b) < cfg.edgeHeight i Z := by
    obtain ⟨h1, h2, h3⟩ := cfg.edgeHeight_pair_pos hij.symm
    have hpos : 0 < α₂ * cfg.edgeHeight i (cfg.Q j) + β₂ * cfg.edgeHeight i (cfg.Q (j + 1)) := by
      by_cases hq : 0 < cfg.edgeHeight i (cfg.Q j)
      · nlinarith
      · have hq2 : 0 < cfg.edgeHeight i (cfg.Q (j + 1)) := by linarith
        nlinarith
    simp only [edgeHeight] at hpos ⊢
    rw [hZ₂, orient_comb3 hsum₂]
    linarith
  have h1 : γ₂ * cfg.edgeHeight i (cfg.B b) < γ₁ * cfg.edgeHeight i (cfg.B a) := by linarith
  have h2 : γ₁ * cfg.edgeHeight j (cfg.B a) < γ₂ * cfg.edgeHeight j (cfg.B b) := by linarith
  have hpos_a : 0 < γ₁ * cfg.edgeHeight j (cfg.B a) := mul_pos hγ₁ (cfg.edgeHeight_B_pos j a)
  have hpos_b : 0 < γ₂ * cfg.edgeHeight i (cfg.B b) := mul_pos hγ₂ (cfg.edgeHeight_B_pos i b)
  have hprod : (γ₂ * cfg.edgeHeight i (cfg.B b)) * (γ₁ * cfg.edgeHeight j (cfg.B a)) <
      (γ₁ * cfg.edgeHeight i (cfg.B a)) * (γ₂ * cfg.edgeHeight j (cfg.B b)) :=
    mul_lt_mul'' h1 h2 hpos_b.le hpos_a.le
  have hγγ : 0 < γ₁ * γ₂ := mul_pos hγ₁ hγ₂
  nlinarith

/-- Swapping two intersecting triangles produces two triangles that do not intersect nontrivially. -/
theorem swapped_triangles_disjoint {i j a b : Fin n} (hij : i ≠ j) (hab : a ≠ b)
    (hint : cfg.TrianglesIntersect i j a b) :
    ¬ cfg.TrianglesIntersect i j b a := by
  intro hint'
  have h1 := cfg.area_product_strict_decrease hij hab hint
  have h2 := cfg.area_product_strict_decrease hij hab.symm hint'
  linarith

/-- Positive area-product potential `Φ(π) = ∏_{k : Fin n} ℓ_k(B_{π(k)})`. -/
def potential (π : Equiv.Perm (Fin n)) : ℝ :=
  ∏ k : Fin n, cfg.edgeHeight k (cfg.B (π k))

lemma potential_pos (π : Equiv.Perm (Fin n)) : 0 < cfg.potential π :=
  Finset.prod_pos fun k _ => cfg.edgeHeight_B_pos k (π k)

/-- Every directed edge `π → ρ` of Bui's state graph strictly decreases `Φ`. -/
theorem potential_strict_decrease {π ρ : Equiv.Perm (Fin n)} (hedge : cfg.StateEdge π ρ) :
    cfg.potential ρ < cfg.potential π := by
  rcases hedge with ⟨i, j, hij, hρi, hρj, hρother, hint⟩
  have hab : π i ≠ π j := fun h => hij (π.injective h)
  have hlt := cfg.area_product_strict_decrease hij hab hint
  let S : Finset (Fin n) := Finset.univ.erase i |>.erase j
  have hsplit : ∀ σ : Equiv.Perm (Fin n),
      cfg.potential σ =
        (cfg.edgeHeight i (cfg.B (σ i)) * cfg.edgeHeight j (cfg.B (σ j))) *
        ∏ k ∈ S, cfg.edgeHeight k (cfg.B (σ k)) := by
    intro σ
    unfold potential
    have hi : i ∈ (Finset.univ : Finset (Fin n)) := Finset.mem_univ i
    have hj : j ∈ (Finset.univ : Finset (Fin n)).erase i :=
      Finset.mem_erase.mpr ⟨hij.symm, Finset.mem_univ j⟩
    rw [← Finset.mul_prod_erase Finset.univ _ hi,
      ← Finset.mul_prod_erase (Finset.univ.erase i) _ hj]
    ring
  rw [hsplit ρ, hsplit π, hρi, hρj]
  have hrest_eq : ∏ k ∈ S, cfg.edgeHeight k (cfg.B (ρ k)) =
      ∏ k ∈ S, cfg.edgeHeight k (cfg.B (π k)) := by
    refine Finset.prod_congr rfl fun k hk => ?_
    have hkj : k ≠ j := (Finset.mem_erase.mp hk).1
    have hki : k ≠ i := (Finset.mem_erase.mp (Finset.mem_erase.mp hk).2).1
    rw [hρother k hki hkj]
  rw [hrest_eq]
  have hrest_pos : 0 < ∏ k ∈ S, cfg.edgeHeight k (cfg.B (π k)) :=
    Finset.prod_pos fun k _ => cfg.edgeHeight_B_pos k (π k)
  exact mul_lt_mul_of_pos_right hlt hrest_pos

lemma potential_strict_decrease_trans {π ρ : Equiv.Perm (Fin n)}
    (hpath : Relation.TransGen cfg.StateEdge π ρ) :
    cfg.potential ρ < cfg.potential π := by
  induction hpath with
  | single h => exact cfg.potential_strict_decrease h
  | tail _ h ih => exact lt_trans (cfg.potential_strict_decrease h) ih

/-! ## Section 5: Main Theorems (Acyclicity and Termination) -/

/-- **Main Theorem (Hong Duc Bui, `arXiv:2508.04602v1`, Section 8.2 Conjecture):**
For every `n ≥ 3` and every general-position planar point set `Q` of size `2n` with
`|CH(Q)| = n`, the directed triangle-matching state graph `G` is acyclic (contains no
directed cycle). -/
theorem bui_conjecture_8_2_acyclic (π : Equiv.Perm (Fin n)) :
    ¬ Relation.TransGen cfg.StateEdge π π := by
  intro hcyc
  exact lt_irrefl (cfg.potential π) (cfg.potential_strict_decrease_trans hcyc)

/-- Every directed path `π₀ → π₁ → ... → π_L` in `G` has length `L ≤ n! - 1`,
so the iterative swap algorithm always terminates in at most `n! - 1` steps. -/
theorem bui_conjecture_8_2_terminates (L : ℕ) (path : Fin (L + 1) → Equiv.Perm (Fin n))
    (hstep : ∀ t : Fin L, cfg.StateEdge (path t.castSucc) (path t.succ)) :
    L ≤ n.factorial - 1 := by
  have hdec : ∀ a b : Fin (L + 1), a < b → cfg.potential (path b) < cfg.potential (path a) := by
    intro a b hab
    obtain ⟨d, hd⟩ : ∃ d : ℕ, b.1 = a.1 + (d + 1) := ⟨b.1 - a.1 - 1, by omega⟩
    induction d generalizing b with
    | zero =>
      have haL : a.1 < L := by omega
      have h1 : path (⟨a.1, haL⟩ : Fin L).castSucc = path a := rfl
      have h2 : path (⟨a.1, haL⟩ : Fin L).succ = path b := by
        congr 1; exact Fin.ext (by dsimp [Fin.succ]; omega)
      rw [← h2, ← h1]
      exact cfg.potential_strict_decrease (hstep ⟨a.1, haL⟩)
    | succ d ih =>
      let m : Fin (L + 1) := ⟨a.1 + (d + 1), by omega⟩
      have hm_val : m.1 = a.1 + (d + 1) := rfl
      have hm_lt : cfg.potential (path m) < cfg.potential (path a) :=
        ih m (by show a.1 < m.1; omega) hm_val
      have hmL : m.1 < L := by omega
      have hm1 : path (⟨m.1, hmL⟩ : Fin L).castSucc = path m := rfl
      have hb_eq : path (⟨m.1, hmL⟩ : Fin L).succ = path b := by
        congr 1; exact Fin.ext (by dsimp [Fin.succ]; omega)
      have hmb : cfg.potential (path b) < cfg.potential (path m) := by
        rw [← hb_eq, ← hm1]
        exact cfg.potential_strict_decrease (hstep ⟨m.1, hmL⟩)
      exact lt_trans hmb hm_lt
  have hinj : Function.Injective path := by
    intro a b hab
    rcases lt_trichotomy a b with hlt | rfl | hgt
    · exact absurd (by rw [hab] : cfg.potential (path b) = cfg.potential (path a))
        (ne_of_lt (hdec a b hlt))
    · rfl
    · exact absurd (by rw [hab] : cfg.potential (path a) = cfg.potential (path b))
        (ne_of_lt (hdec b a hgt))
  have hcard : L + 1 ≤ Fintype.card (Equiv.Perm (Fin n)) := by
    simpa [Fintype.card_fin] using Fintype.card_le_of_injective path hinj
  rw [Fintype.card_perm, Fintype.card_fin] at hcard
  omega

end PointConfig

#print axioms PointConfig.trianglesIntersect_iff_open
#print axioms PointConfig.area_product_strict_decrease
#print axioms PointConfig.swapped_triangles_disjoint
#print axioms PointConfig.potential_strict_decrease
#print axioms PointConfig.bui_conjecture_8_2_acyclic
#print axioms PointConfig.bui_conjecture_8_2_terminates

end OpenMath.Bui250804602Conj81
