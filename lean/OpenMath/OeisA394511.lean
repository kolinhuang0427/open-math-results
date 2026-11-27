import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Data.Finset.Prod
import Mathlib.Data.Rat.Floor
import Mathlib.Tactic

/-!
# Refutation of Peter Exley's 2026 Enclosing Shell Conjecture (OEIS A394511)

Primary source:
OEIS **A394511** (author: Peter Exley, rev. 47, `2026-06-06`):
- **Name:** *"Minimum number of cells in a connected enclosing shell of an n-cell connected hole on
  the truncated-square (4.8.8) Archimedean tiling."*
- **Comment:** *"For a connected n-cell hole H, the corona C(H) is the set of cells edge-adjacent
  to H but not in H. An enclosing shell S is a connected superset of C(H), disjoint from H, with
  the cells outside H union S also connected. a(n) is the minimum |S|."*
- **Conjecture (`_Peter Exley_`, Jun 05 2026):**
  *"Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole,
    |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6, equivalently a(n) = a(n - 5) + 2 for
    n >= 11."*

This file formalizes the exact `4.8.8` tiling edge-adjacency graph `G488`, the corona `IsInCorona`,
valid enclosing shells `IsValidEnclosingShell`, and `a394511 n`, and proves (zero `sorry`, zero
`native_decide`, standard axioms only):
1. `isConnectedSet_iff_induce_connected`: equivalence between reachability inside `A` and
   Mathlib's `(G488.induce A).Connected`.
2. `a394511_rect_le`: for all `R, C ≥ 2`, `a394511 (2*R*C + R + C - 3) ≤ 2*R + 2*C + 4` (with
   `S_rect R C` equal to the exact corona of `H_rect R C`).
3. `a394511_35_le_20`: explicit counterexample at `n = 35` (`R = 3, C = 5`), giving
   `a394511 35 ≤ 20 < 22 = 2 * ⌈(35 + 17)/5⌉`.
4. `not_exley_conjecture_formula`: refutation of `∀ n ≥ 6, a(n) = 2 * ⌈(n + 17)/5⌉`.
5. `exley_infinite_family_refutation`: for all `k ≥ 4`, `n_k = 2k^2 + 2k - 3` satisfies
   `a394511 n_k ≤ 4k + 4 < 2 * ⌈(n_k + 17)/5⌉`.
-/

namespace OpenMath.OeisA394511

/-! ## Section 1: Exact Edge-Adjacency Graph of the Truncated-Square (`4.8.8`) Tiling -/

/-- Cells of the regular `4.8.8` (truncated-square) Archimedean tiling:
octagons `oct x y` and squares `sq i j` indexed by `ℤ × ℤ`. -/
inductive Tile : Type
  | oct (x y : ℤ)
  | sq (i j : ℤ)
  deriving DecidableEq, Repr

/-- Edge-adjacency relation of the `4.8.8` tiling:
- `oct x y` is adjacent to orthogonal octagons `oct (x ± 1) y`, `oct x (y ± 1)` and to the four
  diagonal squares `sq i j` with `x ∈ {i, i + 1}` and `y ∈ {j, j + 1}`;
- squares share edges exclusively with their four neighboring octagons. -/
def tileAdj : Tile → Tile → Prop
  | .oct x y, .oct x' y' =>
      ((x' = x + 1 ∨ x' = x - 1) ∧ y' = y) ∨ (x' = x ∧ (y' = y + 1 ∨ y' = y - 1))
  | .oct x y, .sq i j => (x = i ∨ x = i + 1) ∧ (y = j ∨ y = j + 1)
  | .sq i j, .oct x y => (x = i ∨ x = i + 1) ∧ (y = j ∨ y = j + 1)
  | .sq _ _, .sq _ _ => False

/-- The edge-adjacency simple graph `G_{4.8.8}`. -/
def G488 : SimpleGraph Tile where
  Adj := tileAdj
  symm := ⟨by
    intro u v h
    cases u <;> cases v <;> simp only [tileAdj] at h ⊢
    · rcases h with ⟨h1 | h1, h2⟩ | ⟨h1, h2 | h2⟩ <;> [left; left; right; right] <;>
        exact ⟨by omega, by omega⟩
    · exact h
    · exact h⟩
  loopless := ⟨by
    intro u h
    cases u <;> simp only [tileAdj] at h
    · rcases h with ⟨h1 | h1, _⟩ | ⟨_, h2 | h2⟩ <;> omega⟩

/-! ## Section 2: Connected Sets, Corona, Enclosing Shells, and `a(n)` -/

/-- Reachability inside a subset `A : Set Tile` via edges of `G488` staying within `A`. -/
def ReachIn (A : Set Tile) (u v : Tile) : Prop :=
  Relation.ReflTransGen (fun a b => a ∈ A ∧ b ∈ A ∧ G488.Adj a b) u v

/-- A subset `A : Set Tile` is connected if it is nonempty and any two vertices in `A` are
connected by a path in `G488` staying inside `A`. -/
def IsConnectedSet (A : Set Tile) : Prop :=
  A.Nonempty ∧ ∀ u ∈ A, ∀ v ∈ A, ReachIn A u v

lemma reachIn_symm {A : Set Tile} {u v : Tile} (h : ReachIn A u v) : ReachIn A v u := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih =>
    exact Relation.ReflTransGen.head ⟨hstep.2.1, hstep.1, hstep.2.2.symm⟩ ih

lemma reachIn_step {A : Set Tile} {u v : Tile} (hu : u ∈ A) (hv : v ∈ A) (hadj : G488.Adj u v) :
    ReachIn A u v :=
  Relation.ReflTransGen.single ⟨hu, hv, hadj⟩

private lemma reachIn_of_walk {A : Set Tile} {a b : A} (w : (G488.induce A).Walk a b) :
    ReachIn A a.1 b.1 := by
  induction w with
  | nil => exact Relation.ReflTransGen.refl
  | @cons x y z hadj _ ih =>
    exact Relation.ReflTransGen.head ⟨x.2, y.2, hadj⟩ ih

/-- Fidelity check: `IsConnectedSet A` is equivalent to Mathlib's `(G488.induce A).Connected`. -/
theorem isConnectedSet_iff_induce_connected (A : Set Tile) :
    IsConnectedSet A ↔ (G488.induce A).Connected := by
  constructor
  · rintro ⟨⟨v₀, hv₀⟩, hreach⟩
    have : Nonempty A := ⟨⟨v₀, hv₀⟩⟩
    refine SimpleGraph.Connected.mk fun ⟨u, hu⟩ ⟨v, hv⟩ => ?_
    have hr := hreach u hu v hv
    induction hr with
    | refl => exact SimpleGraph.Reachable.refl _
    | @tail b c _ hstep ih =>
      have hbc : (G488.induce A).Adj ⟨b, hstep.1⟩ ⟨c, hstep.2.1⟩ := hstep.2.2
      exact (ih hstep.1).trans hbc.reachable
  · intro hconn
    have ⟨⟨v₀, hv₀⟩⟩ := hconn.nonempty
    refine ⟨⟨v₀, hv₀⟩, fun u hu v hv => ?_⟩
    obtain ⟨w⟩ := hconn.preconnected ⟨u, hu⟩ ⟨v, hv⟩
    exact reachIn_of_walk w

/-- The corona `C(H)` of a hole `H`: cells outside `H` sharing an edge with at least one cell of `H`. -/
def IsInCorona (H : Finset Tile) (v : Tile) : Prop :=
  v ∉ H ∧ ∃ u ∈ H, G488.Adj u v

/-- A valid enclosing shell `S` of a hole `H` per OEIS `A394511`:
`H` is connected, `S` is connected, `H` and `S` are disjoint, `C(H) ⊆ S`, and `(H ∪ S)ᶜ` is
connected. -/
def IsValidEnclosingShell (H S : Finset Tile) : Prop :=
  IsConnectedSet (H : Set Tile) ∧
  IsConnectedSet (S : Set Tile) ∧
  Disjoint H S ∧
  (∀ v : Tile, IsInCorona H v → v ∈ S) ∧
  IsConnectedSet ((H ∪ S : Finset Tile) : Set Tile)ᶜ

/-- OEIS `A394511(n)`: minimum cardinality `|S|` of a valid enclosing shell `S` over all
connected `n`-cell holes `H` in the `4.8.8` tiling. -/
noncomputable def a394511 (n : ℕ) : ℕ :=
  sInf {k : ℕ | ∃ H S : Finset Tile, H.card = n ∧ IsValidEnclosingShell H S ∧ S.card = k}

lemma a394511_le_of_shell {H S : Finset Tile} (hvalid : IsValidEnclosingShell H S) :
    a394511 H.card ≤ S.card :=
  Nat.sInf_le ⟨H, S, rfl, hvalid, rfl⟩

/-! ## Section 3: Explicit Rectangular Family `H(R, C)` and Corona Shell `S(R, C)` -/

/-- The four corner square coordinates of the `R × C` octagon block. -/
def cornerCoords (R C : ℕ) : Finset (ℤ × ℤ) :=
  {(-1, -1), ((R : ℤ) - 1, -1), (-1, (C : ℤ) - 1), ((R : ℤ) - 1, (C : ℤ) - 1)}

/-- The octagon subgrid `O_{R,C} = {oct x y | 0 ≤ x < R, 0 ≤ y < C}`. -/
def octBlock (R C : ℕ) : Finset Tile :=
  ((Finset.Ico (0 : ℤ) R) ×ˢ (Finset.Ico (0 : ℤ) C)).image fun p => Tile.oct p.1 p.2

/-- The square cells of `H(R, C)`: all squares in `[-1, R-1] × [-1, C-1]` except the four corners. -/
def sqHoleBlock (R C : ℕ) : Finset Tile :=
  (((Finset.Icc (-1 : ℤ) ((R : ℤ) - 1)) ×ˢ (Finset.Icc (-1 : ℤ) ((C : ℤ) - 1))) \
      cornerCoords R C).image fun p => Tile.sq p.1 p.2

/-- The connected rectangular hole `H(R, C)` of size `2RC + R + C - 3`. -/
def HRect (R C : ℕ) : Finset Tile :=
  octBlock R C ∪ sqHoleBlock R C

/-- Side octagons in the corona `S(R, C)`. -/
def octShell (R C : ℕ) : Finset Tile :=
  ((Finset.Ico (0 : ℤ) R).image fun x => Tile.oct x (-1)) ∪
  ((Finset.Ico (0 : ℤ) R).image fun x => Tile.oct x (C : ℤ)) ∪
  ((Finset.Ico (0 : ℤ) C).image fun y => Tile.oct (-1) y) ∪
  ((Finset.Ico (0 : ℤ) C).image fun y => Tile.oct (R : ℤ) y)

/-- The four corner squares in the corona `S(R, C)`. -/
def sqCornerShell (R C : ℕ) : Finset Tile :=
  (cornerCoords R C).image fun p => Tile.sq p.1 p.2

/-- The enclosing shell `S(R, C) = C(H(R, C))` of size `2R + 2C + 4`. -/
def SRect (R C : ℕ) : Finset Tile :=
  octShell R C ∪ sqCornerShell R C

/-! ### Membership Characterizations -/

lemma mem_octBlock {R C : ℕ} {v : Tile} :
    v ∈ octBlock R C ↔ ∃ x y : ℤ, v = Tile.oct x y ∧ 0 ≤ x ∧ x < R ∧ 0 ≤ y ∧ y < C := by
  simp only [octBlock, Finset.mem_image, Finset.mem_product, Finset.mem_Ico, Prod.exists]
  constructor
  · rintro ⟨x, y, ⟨⟨hx1, hx2⟩, ⟨hy1, hy2⟩⟩, rfl⟩
    exact ⟨x, y, rfl, hx1, hx2, hy1, hy2⟩
  · rintro ⟨x, y, rfl, hx1, hx2, hy1, hy2⟩
    exact ⟨x, y, ⟨⟨hx1, hx2⟩, ⟨hy1, hy2⟩⟩, rfl⟩

lemma mem_cornerCoords {R C : ℕ} {p : ℤ × ℤ} :
    p ∈ cornerCoords R C ↔
      (p.1 = -1 ∨ p.1 = (R : ℤ) - 1) ∧ (p.2 = -1 ∨ p.2 = (C : ℤ) - 1) := by
  rcases p with ⟨i, j⟩
  simp only [cornerCoords, Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq]
  tauto

lemma mem_sqHoleBlock {R C : ℕ} {v : Tile} :
    v ∈ sqHoleBlock R C ↔
      ∃ i j : ℤ, v = Tile.sq i j ∧
        -1 ≤ i ∧ i ≤ (R : ℤ) - 1 ∧ -1 ≤ j ∧ j ≤ (C : ℤ) - 1 ∧
        ¬ ((i = -1 ∨ i = (R : ℤ) - 1) ∧ (j = -1 ∨ j = (C : ℤ) - 1)) := by
  simp only [sqHoleBlock, Finset.mem_image, Finset.mem_sdiff, Finset.mem_product, Finset.mem_Icc,
    mem_cornerCoords, Prod.exists]
  constructor
  · rintro ⟨i, j, ⟨⟨⟨hi1, hi2⟩, ⟨hj1, hj2⟩⟩, hnc⟩, rfl⟩
    exact ⟨i, j, rfl, hi1, hi2, hj1, hj2, hnc⟩
  · rintro ⟨i, j, rfl, hi1, hi2, hj1, hj2, hnc⟩
    exact ⟨i, j, ⟨⟨⟨hi1, hi2⟩, ⟨hj1, hj2⟩⟩, hnc⟩, rfl⟩

lemma mem_HRect_oct {R C : ℕ} {x y : ℤ} :
    Tile.oct x y ∈ HRect R C ↔ 0 ≤ x ∧ x < R ∧ 0 ≤ y ∧ y < C := by
  simp [HRect, mem_octBlock, mem_sqHoleBlock]

lemma mem_HRect_sq {R C : ℕ} {i j : ℤ} :
    Tile.sq i j ∈ HRect R C ↔
      -1 ≤ i ∧ i ≤ (R : ℤ) - 1 ∧ -1 ≤ j ∧ j ≤ (C : ℤ) - 1 ∧
        ¬ ((i = -1 ∨ i = (R : ℤ) - 1) ∧ (j = -1 ∨ j = (C : ℤ) - 1)) := by
  simp [HRect, mem_octBlock, mem_sqHoleBlock]

lemma mem_SRect_oct {R C : ℕ} {x y : ℤ} :
    Tile.oct x y ∈ SRect R C ↔
      (0 ≤ x ∧ x < R ∧ (y = -1 ∨ y = (C : ℤ))) ∨
      (0 ≤ y ∧ y < C ∧ (x = -1 ∨ x = (R : ℤ))) := by
  simp only [SRect, octShell, sqCornerShell, Finset.mem_union, Finset.mem_image, Finset.mem_Ico,
    Tile.oct.injEq, reduceCtorEq, and_false, exists_false, or_false]
  constructor
  · rintro (((⟨a, ⟨ha1, ha2⟩, rfl, rfl⟩ | ⟨a, ⟨ha1, ha2⟩, rfl, rfl⟩) |
        ⟨b, ⟨hb1, hb2⟩, rfl, rfl⟩) | ⟨b, ⟨hb1, hb2⟩, rfl, rfl⟩)
    · exact Or.inl ⟨ha1, ha2, Or.inl rfl⟩
    · exact Or.inl ⟨ha1, ha2, Or.inr rfl⟩
    · exact Or.inr ⟨hb1, hb2, Or.inl rfl⟩
    · exact Or.inr ⟨hb1, hb2, Or.inr rfl⟩
  · rintro (⟨hx1, hx2, rfl | rfl⟩ | ⟨hy1, hy2, rfl | rfl⟩)
    · exact Or.inl (Or.inl (Or.inl ⟨x, ⟨hx1, hx2⟩, rfl, rfl⟩))
    · exact Or.inl (Or.inl (Or.inr ⟨x, ⟨hx1, hx2⟩, rfl, rfl⟩))
    · exact Or.inl (Or.inr ⟨y, ⟨hy1, hy2⟩, rfl, rfl⟩)
    · exact Or.inr ⟨y, ⟨hy1, hy2⟩, rfl, rfl⟩

lemma mem_SRect_sq {R C : ℕ} {i j : ℤ} :
    Tile.sq i j ∈ SRect R C ↔
      (i = -1 ∨ i = (R : ℤ) - 1) ∧ (j = -1 ∨ j = (C : ℤ) - 1) := by
  simp only [SRect, octShell, sqCornerShell, Finset.mem_union, Finset.mem_image, Prod.exists,
    Tile.sq.injEq, reduceCtorEq, and_false, exists_false, or_false, false_or, mem_cornerCoords]
  constructor
  · rintro ⟨a, b, h, rfl, rfl⟩; exact h
  · intro h; exact ⟨i, j, h, rfl, rfl⟩

/-! ### Exact Cardinalities of `H(R, C)` and `S(R, C)` -/

lemma card_HRect {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    (HRect R C).card = 2 * R * C + R + C - 3 := by
  have hdisj : Disjoint (octBlock R C) (sqHoleBlock R C) := by
    rw [Finset.disjoint_left]
    intro v hv1 hv2
    rcases mem_octBlock.mp hv1 with ⟨_, _, rfl, _⟩
    rcases mem_sqHoleBlock.mp hv2 with ⟨_, _, h, _⟩
    exact absurd h (by simp)
  rw [HRect, Finset.card_union_of_disjoint hdisj]
  have hoct : (octBlock R C).card = R * C := by
    rw [octBlock, Finset.card_image_of_injective]
    · rw [Finset.card_product, Int.card_Ico, Int.card_Ico]
      simp
    · rintro ⟨a, b⟩ ⟨c, d⟩ h
      simp only [Tile.oct.injEq] at h
      exact Prod.ext h.1 h.2
  have hsub : cornerCoords R C ⊆
      (Finset.Icc (-1 : ℤ) ((R : ℤ) - 1)) ×ˢ (Finset.Icc (-1 : ℤ) ((C : ℤ) - 1)) := by
    intro p hp
    rw [mem_cornerCoords] at hp
    simp only [Finset.mem_product, Finset.mem_Icc]
    omega
  have hcorn : (cornerCoords R C).card = 4 := by
    unfold cornerCoords
    rw [Finset.card_insert_of_notMem, Finset.card_insert_of_notMem,
      Finset.card_insert_of_notMem, Finset.card_singleton]
    all_goals simp only [Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq]; omega
  have hsq : (sqHoleBlock R C).card = (R + 1) * (C + 1) - 4 := by
    rw [sqHoleBlock, Finset.card_image_of_injective]
    · rw [Finset.card_sdiff_of_subset hsub, Finset.card_product, Int.card_Icc, Int.card_Icc, hcorn]
      have h1 : (((R : ℤ) - 1 + 1 - (-1)).toNat) = R + 1 := by omega
      have h2 : (((C : ℤ) - 1 + 1 - (-1)).toNat) = C + 1 := by omega
      rw [h1, h2]
    · rintro ⟨a, b⟩ ⟨c, d⟩ h
      simp only [Tile.sq.injEq] at h
      exact Prod.ext h.1 h.2
  rw [hoct, hsq]
  have h1 : (R + 1) * (C + 1) = R * C + R + C + 1 := by ring
  have h2 : 2 * R * C = R * C + R * C := by ring
  have hge4 : 4 ≤ R * C + R + C + 1 := by nlinarith
  rw [h1, h2]
  omega

lemma card_SRect {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    (SRect R C).card = 2 * R + 2 * C + 4 := by
  have hdisj_os : Disjoint (octShell R C) (sqCornerShell R C) := by
    rw [Finset.disjoint_left]
    intro v hv1 hv2
    simp only [sqCornerShell, Finset.mem_image] at hv2
    rcases hv2 with ⟨_, _, rfl⟩
    simp only [octShell, Finset.mem_union, Finset.mem_image, reduceCtorEq, and_false,
      exists_false, or_self] at hv1
  rw [SRect, Finset.card_union_of_disjoint hdisj_os]
  have hcorn : (sqCornerShell R C).card = 4 := by
    rw [sqCornerShell, Finset.card_image_of_injective]
    · unfold cornerCoords
      rw [Finset.card_insert_of_notMem, Finset.card_insert_of_notMem,
        Finset.card_insert_of_notMem, Finset.card_singleton]
      all_goals simp only [Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq]; omega
    · rintro ⟨a, b⟩ ⟨c, d⟩ h
      simp only [Tile.sq.injEq] at h
      exact Prod.ext h.1 h.2
  let s1 := (Finset.Ico (0 : ℤ) R).image fun x => Tile.oct x (-1)
  let s2 := (Finset.Ico (0 : ℤ) R).image fun x => Tile.oct x (C : ℤ)
  let s3 := (Finset.Ico (0 : ℤ) C).image fun y => Tile.oct (-1) y
  let s4 := (Finset.Ico (0 : ℤ) C).image fun y => Tile.oct (R : ℤ) y
  have hd12 : Disjoint s1 s2 := by
    rw [Finset.disjoint_left]; intro v h1 h2
    simp only [s1, s2, Finset.mem_image, Finset.mem_Ico] at h1 h2
    rcases h1 with ⟨_, _, rfl⟩; rcases h2 with ⟨_, _, h⟩; simp only [Tile.oct.injEq] at h; omega
  have hd12_3 : Disjoint (s1 ∪ s2) s3 := by
    rw [Finset.disjoint_left]; intro v h1 h2
    simp only [s1, s2, s3, Finset.mem_union, Finset.mem_image, Finset.mem_Ico] at h1 h2
    rcases h2 with ⟨_, _, rfl⟩
    rcases h1 with ⟨_, ⟨_, _⟩, h⟩ | ⟨_, ⟨_, _⟩, h⟩ <;> (simp only [Tile.oct.injEq] at h; omega)
  have hd123_4 : Disjoint (s1 ∪ s2 ∪ s3) s4 := by
    rw [Finset.disjoint_left]; intro v h1 h2
    simp only [s1, s2, s3, s4, Finset.mem_union, Finset.mem_image, Finset.mem_Ico] at h1 h2
    rcases h2 with ⟨_, _, rfl⟩
    rcases h1 with (⟨_, ⟨_, _⟩, h⟩ | ⟨_, ⟨_, _⟩, h⟩) | ⟨_, ⟨_, _⟩, h⟩ <;>
      (simp only [Tile.oct.injEq] at h; omega)
  have hc1 : s1.card = R := by
    rw [Finset.card_image_of_injective _ (fun _ _ h => by simpa using h), Int.card_Ico]; simp
  have hc2 : s2.card = R := by
    rw [Finset.card_image_of_injective _ (fun _ _ h => by simpa using h), Int.card_Ico]; simp
  have hc3 : s3.card = C := by
    rw [Finset.card_image_of_injective _ (fun _ _ h => by simpa using h), Int.card_Ico]; simp
  have hc4 : s4.card = C := by
    rw [Finset.card_image_of_injective _ (fun _ _ h => by simpa using h), Int.card_Ico]; simp
  have hoct : (octShell R C).card = 2 * R + 2 * C := by
    change (s1 ∪ s2 ∪ s3 ∪ s4).card = 2 * R + 2 * C
    rw [Finset.card_union_of_disjoint hd123_4, Finset.card_union_of_disjoint hd12_3,
      Finset.card_union_of_disjoint hd12, hc1, hc2, hc3, hc4]
    omega
  rw [hoct, hcorn]

/-! ### Horizontal and Vertical Octagon Path Helpers -/

lemma reachIn_oct_horiz {A : Set Tile} {y x₁ x₂ : ℤ} (hx : x₁ ≤ x₂)
    (hmem : ∀ x : ℤ, x₁ ≤ x → x ≤ x₂ → Tile.oct x y ∈ A) :
    ReachIn A (Tile.oct x₁ y) (Tile.oct x₂ y) := by
  obtain ⟨k, hk⟩ := Int.eq_ofNat_of_zero_le (sub_nonneg.mpr hx)
  have hx₂ : x₂ = x₁ + (k : ℤ) := by omega
  subst hx₂
  clear hk hx
  induction k with
  | zero =>
    rw [Int.ofNat_zero, add_zero]
    exact Relation.ReflTransGen.refl
  | succ k ih =>
    have hprev : ReachIn A (Tile.oct x₁ y) (Tile.oct (x₁ + k) y) :=
      ih (fun x h1 h2 => hmem x h1 (by omega))
    refine Relation.ReflTransGen.tail hprev
      ⟨hmem (x₁ + k) (by omega) (by omega), hmem (x₁ + (k + 1 : ℕ)) (by omega) le_rfl, ?_⟩
    show tileAdj (Tile.oct (x₁ + k) y) (Tile.oct (x₁ + (k + 1 : ℕ)) y)
    dsimp only [tileAdj]
    left
    exact ⟨Or.inl (by push_cast; ring), rfl⟩

lemma reachIn_oct_vert {A : Set Tile} {x y₁ y₂ : ℤ} (hy : y₁ ≤ y₂)
    (hmem : ∀ y : ℤ, y₁ ≤ y → y ≤ y₂ → Tile.oct x y ∈ A) :
    ReachIn A (Tile.oct x y₁) (Tile.oct x y₂) := by
  obtain ⟨k, hk⟩ := Int.eq_ofNat_of_zero_le (sub_nonneg.mpr hy)
  have hy₂ : y₂ = y₁ + (k : ℤ) := by omega
  subst hy₂
  clear hk hy
  induction k with
  | zero =>
    rw [Int.ofNat_zero, add_zero]
    exact Relation.ReflTransGen.refl
  | succ k ih =>
    have hprev : ReachIn A (Tile.oct x y₁) (Tile.oct x (y₁ + k)) :=
      ih (fun y h1 h2 => hmem y h1 (by omega))
    refine Relation.ReflTransGen.tail hprev
      ⟨hmem (y₁ + k) (by omega) (by omega), hmem (y₁ + (k + 1 : ℕ)) (by omega) le_rfl, ?_⟩
    show tileAdj (Tile.oct x (y₁ + k)) (Tile.oct x (y₁ + (k + 1 : ℕ)))
    dsimp only [tileAdj]
    right
    exact ⟨rfl, Or.inl (by push_cast; ring)⟩

lemma isConnectedSet_of_star {A : Set Tile} {v₀ : Tile} (hv₀ : v₀ ∈ A)
    (hstar : ∀ u ∈ A, ReachIn A u v₀) : IsConnectedSet A :=
  ⟨⟨v₀, hv₀⟩, fun u hu v hv => (hstar u hu).trans (reachIn_symm (hstar v hv))⟩

/-! ### Validity of `S(R, C)` as an Enclosing Shell of `H(R, C)` -/

lemma HRect_connected {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    IsConnectedSet (HRect R C : Set Tile) := by
  have h00 : Tile.oct 0 0 ∈ (HRect R C : Set Tile) := by
    simp only [Finset.mem_coe, mem_HRect_oct]; omega
  refine isConnectedSet_of_star h00 fun u hu => ?_
  have hoct_reach : ∀ x y : ℤ, 0 ≤ x → x < R → 0 ≤ y → y < C →
      ReachIn (HRect R C : Set Tile) (Tile.oct x y) (Tile.oct 0 0) := by
    intro x y hx1 hx2 hy1 hy2
    have h1 : ReachIn (HRect R C : Set Tile) (Tile.oct 0 y) (Tile.oct x y) :=
      reachIn_oct_horiz hx1 fun a ha1 ha2 => by
        simp only [Finset.mem_coe, mem_HRect_oct]; omega
    have h2 : ReachIn (HRect R C : Set Tile) (Tile.oct 0 0) (Tile.oct 0 y) :=
      reachIn_oct_vert hy1 fun b hb1 hb2 => by
        simp only [Finset.mem_coe, mem_HRect_oct]; omega
    exact reachIn_symm (h2.trans h1)
  cases u with
  | oct x y =>
    simp only [Finset.mem_coe, mem_HRect_oct] at hu
    exact hoct_reach x y hu.1 hu.2.1 hu.2.2.1 hu.2.2.2
  | sq i j =>
    simp only [Finset.mem_coe, mem_HRect_sq] at hu
    let x' : ℤ := if i = -1 then 0 else i
    let y' : ℤ := if j = -1 then 0 else j
    have hx'1 : 0 ≤ x' := by dsimp [x']; split_ifs <;> omega
    have hx'2 : x' < R := by dsimp [x']; split_ifs <;> omega
    have hy'1 : 0 ≤ y' := by dsimp [y']; split_ifs <;> omega
    have hy'2 : y' < C := by dsimp [y']; split_ifs <;> omega
    have hmem' : Tile.oct x' y' ∈ (HRect R C : Set Tile) := by
      simp only [Finset.mem_coe, mem_HRect_oct]; omega
    have hadj : G488.Adj (Tile.sq i j) (Tile.oct x' y') := by
      show (x' = i ∨ x' = i + 1) ∧ (y' = j ∨ y' = j + 1)
      dsimp [x', y']
      constructor <;> split_ifs <;> omega
    exact (reachIn_step (by simp only [Finset.mem_coe, mem_HRect_sq]; exact hu) hmem' hadj).trans
      (hoct_reach x' y' hx'1 hx'2 hy'1 hy'2)

lemma SRect_connected {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    IsConnectedSet (SRect R C : Set Tile) := by
  let S : Set Tile := (SRect R C : Set Tile)
  have hmem_sq : ∀ i j : ℤ,
      (i = -1 ∨ i = (R : ℤ) - 1) → (j = -1 ∨ j = (C : ℤ) - 1) → Tile.sq i j ∈ S := by
    intro i j hi hj
    simp only [S, Finset.mem_coe, mem_SRect_sq]
    exact ⟨hi, hj⟩
  have hmem_oct : ∀ x y : ℤ,
      ((0 ≤ x ∧ x < R ∧ (y = -1 ∨ y = (C : ℤ))) ∨ (0 ≤ y ∧ y < C ∧ (x = -1 ∨ x = (R : ℤ)))) →
      Tile.oct x y ∈ S := by
    intro x y h
    simp only [S, Finset.mem_coe, mem_SRect_oct]
    exact h
  -- Basepoint: bottom-left corner square `sq (-1) (-1)`
  have hbase : Tile.sq (-1) (-1) ∈ S := hmem_sq (-1) (-1) (Or.inl rfl) (Or.inl rfl)
  -- Bottom side connects to basepoint
  have hbot : ∀ x : ℤ, 0 ≤ x → x < R → ReachIn S (Tile.oct x (-1)) (Tile.sq (-1) (-1)) := by
    intro x hx1 hx2
    have h1 := reachIn_symm (reachIn_oct_horiz hx1 fun a ha1 ha2 =>
      hmem_oct a (-1) (Or.inl ⟨ha1, by omega, Or.inl rfl⟩))
    have h2 : ReachIn S (Tile.oct 0 (-1)) (Tile.sq (-1) (-1)) :=
      reachIn_step (hmem_oct 0 (-1) (Or.inl ⟨le_rfl, by omega, Or.inl rfl⟩)) hbase
        (by show (0 = (-1 : ℤ) ∨ 0 = -1 + 1) ∧ (-1 = (-1 : ℤ) ∨ -1 = -1 + 1); omega)
    exact h1.trans h2
  -- Bottom-right corner square `sq (R-1) (-1)` connects via `oct (R-1) (-1)`
  have hbr : ReachIn S (Tile.sq ((R : ℤ) - 1) (-1)) (Tile.sq (-1) (-1)) := by
    have hstep : ReachIn S (Tile.sq ((R : ℤ) - 1) (-1)) (Tile.oct ((R : ℤ) - 1) (-1)) :=
      reachIn_step (hmem_sq _ _ (Or.inr rfl) (Or.inl rfl))
        (hmem_oct _ _ (Or.inl ⟨by omega, by omega, Or.inl rfl⟩))
        (by show ((R : ℤ) - 1 = (R : ℤ) - 1 ∨ _) ∧ (-1 = (-1 : ℤ) ∨ _); omega)
    exact hstep.trans (hbot ((R : ℤ) - 1) (by omega) (by omega))
  -- Right side connects to bottom-right corner square
  have hright : ∀ y : ℤ, 0 ≤ y → y < C → ReachIn S (Tile.oct (R : ℤ) y) (Tile.sq (-1) (-1)) := by
    intro y hy1 hy2
    have h1 := reachIn_symm (reachIn_oct_vert hy1 fun b hb1 hb2 =>
      hmem_oct (R : ℤ) b (Or.inr ⟨hb1, by omega, Or.inr rfl⟩))
    have h2 : ReachIn S (Tile.oct (R : ℤ) 0) (Tile.sq ((R : ℤ) - 1) (-1)) :=
      reachIn_step (hmem_oct (R : ℤ) 0 (Or.inr ⟨le_rfl, by omega, Or.inr rfl⟩))
        (hmem_sq _ _ (Or.inr rfl) (Or.inl rfl))
        (by show ((R : ℤ) = (R : ℤ) - 1 ∨ (R : ℤ) = (R : ℤ) - 1 + 1) ∧ (0 = (-1 : ℤ) ∨ 0 = -1 + 1); omega)
    exact (h1.trans h2).trans hbr
  -- Top-right corner square `sq (R-1) (C-1)` connects via `oct R (C-1)`
  have htr : ReachIn S (Tile.sq ((R : ℤ) - 1) ((C : ℤ) - 1)) (Tile.sq (-1) (-1)) := by
    have hstep : ReachIn S (Tile.sq ((R : ℤ) - 1) ((C : ℤ) - 1)) (Tile.oct (R : ℤ) ((C : ℤ) - 1)) :=
      reachIn_step (hmem_sq _ _ (Or.inr rfl) (Or.inr rfl))
        (hmem_oct _ _ (Or.inr ⟨by omega, by omega, Or.inr rfl⟩))
        (by show ((R : ℤ) = (R : ℤ) - 1 ∨ (R : ℤ) = (R : ℤ) - 1 + 1) ∧ _; omega)
    exact hstep.trans (hright ((C : ℤ) - 1) (by omega) (by omega))
  -- Top side connects to top-right corner square
  have htop : ∀ x : ℤ, 0 ≤ x → x < R → ReachIn S (Tile.oct x (C : ℤ)) (Tile.sq (-1) (-1)) := by
    intro x hx1 hx2
    have h1 := reachIn_oct_horiz (x₁ := x) (x₂ := (R : ℤ) - 1) (by omega) fun a ha1 ha2 =>
      hmem_oct a (C : ℤ) (Or.inl ⟨by omega, by omega, Or.inr rfl⟩)
    have h2 : ReachIn S (Tile.oct ((R : ℤ) - 1) (C : ℤ)) (Tile.sq ((R : ℤ) - 1) ((C : ℤ) - 1)) :=
      reachIn_step (hmem_oct _ _ (Or.inl ⟨by omega, by omega, Or.inr rfl⟩))
        (hmem_sq _ _ (Or.inr rfl) (Or.inr rfl))
        (by show ((R : ℤ) - 1 = (R : ℤ) - 1 ∨ _) ∧ ((C : ℤ) = (C : ℤ) - 1 ∨ (C : ℤ) = (C : ℤ) - 1 + 1); omega)
    exact (h1.trans h2).trans htr
  -- Left side connects to basepoint via `oct (-1) 0`
  have hleft : ∀ y : ℤ, 0 ≤ y → y < C → ReachIn S (Tile.oct (-1) y) (Tile.sq (-1) (-1)) := by
    intro y hy1 hy2
    have h1 := reachIn_symm (reachIn_oct_vert hy1 fun b hb1 hb2 =>
      hmem_oct (-1) b (Or.inr ⟨hb1, by omega, Or.inl rfl⟩))
    have h2 : ReachIn S (Tile.oct (-1) 0) (Tile.sq (-1) (-1)) :=
      reachIn_step (hmem_oct (-1) 0 (Or.inr ⟨le_rfl, by omega, Or.inl rfl⟩)) hbase
        (by show (-1 = (-1 : ℤ) ∨ _) ∧ (0 = (-1 : ℤ) ∨ 0 = -1 + 1); omega)
    exact h1.trans h2
  -- Top-left corner square `sq (-1) (C-1)` connects via `oct (-1) (C-1)`
  have htl : ReachIn S (Tile.sq (-1) ((C : ℤ) - 1)) (Tile.sq (-1) (-1)) := by
    have hstep : ReachIn S (Tile.sq (-1) ((C : ℤ) - 1)) (Tile.oct (-1) ((C : ℤ) - 1)) :=
      reachIn_step (hmem_sq _ _ (Or.inl rfl) (Or.inr rfl))
        (hmem_oct _ _ (Or.inr ⟨by omega, by omega, Or.inl rfl⟩))
        (by show (-1 = (-1 : ℤ) ∨ _) ∧ ((C : ℤ) - 1 = (C : ℤ) - 1 ∨ _); omega)
    exact hstep.trans (hleft ((C : ℤ) - 1) (by omega) (by omega))
  refine isConnectedSet_of_star hbase fun u hu => ?_
  cases u with
  | oct x y =>
    simp only [Finset.mem_coe, mem_SRect_oct] at hu
    rcases hu with ⟨hx1, hx2, rfl | rfl⟩ | ⟨hy1, hy2, rfl | rfl⟩
    · exact hbot x hx1 hx2
    · exact htop x hx1 hx2
    · exact hleft y hy1 hy2
    · exact hright y hy1 hy2
  | sq i j =>
    simp only [Finset.mem_coe, mem_SRect_sq] at hu
    rcases hu with ⟨rfl | rfl, rfl | rfl⟩
    · exact Relation.ReflTransGen.refl
    · exact htl
    · exact hbr
    · exact htr

lemma HRect_SRect_disjoint {R C : ℕ} : Disjoint (HRect R C) (SRect R C) := by
  rw [Finset.disjoint_left]
  intro v hvH hvS
  cases v with
  | oct x y =>
    rw [mem_HRect_oct] at hvH
    rw [mem_SRect_oct] at hvS
    omega
  | sq i j =>
    rw [mem_HRect_sq] at hvH
    rw [mem_SRect_sq] at hvS
    exact hvH.2.2.2.2 hvS

lemma SRect_contains_corona {R C : ℕ} :
    ∀ v : Tile, IsInCorona (HRect R C) v → v ∈ SRect R C := by
  intro v ⟨hv_notH, u, huH, hadj⟩
  cases v with
  | oct x y =>
    rw [mem_HRect_oct] at hv_notH
    rw [mem_SRect_oct]
    cases u with
    | oct x' y' =>
      rw [mem_HRect_oct] at huH
      simp only [G488, tileAdj] at hadj
      omega
    | sq i j =>
      rw [mem_HRect_sq] at huH
      simp only [G488, tileAdj] at hadj
      omega
  | sq i j =>
    rw [mem_HRect_sq] at hv_notH
    rw [mem_SRect_sq]
    cases u with
    | oct x' y' =>
      rw [mem_HRect_oct] at huH
      simp only [G488, tileAdj] at hadj
      have h1 : -1 ≤ i ∧ i ≤ (R : ℤ) - 1 ∧ -1 ≤ j ∧ j ≤ (C : ℤ) - 1 := by omega
      by_contra hnc
      exact hv_notH ⟨h1.1, h1.2.1, h1.2.2.1, h1.2.2.2, hnc⟩
    | sq _ _ =>
      exact False.elim hadj

lemma exterior_connected {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    IsConnectedSet ((HRect R C ∪ SRect R C : Finset Tile) : Set Tile)ᶜ := by
  let E : Set Tile := ((HRect R C ∪ SRect R C : Finset Tile) : Set Tile)ᶜ
  have hmem_oct : ∀ x y : ℤ, Tile.oct x y ∈ E ↔
      ¬ (0 ≤ x ∧ x < R ∧ 0 ≤ y ∧ y < C) ∧
      ¬ (0 ≤ x ∧ x < R ∧ (y = -1 ∨ y = (C : ℤ))) ∧
      ¬ (0 ≤ y ∧ y < C ∧ (x = -1 ∨ x = (R : ℤ))) := by
    intro x y
    simp only [E, Set.mem_compl_iff, Finset.mem_coe, Finset.mem_union, mem_HRect_oct, mem_SRect_oct]
    tauto
  have hmem_sq : ∀ i j : ℤ, Tile.sq i j ∈ E ↔
      ¬ (-1 ≤ i ∧ i ≤ (R : ℤ) - 1 ∧ -1 ≤ j ∧ j ≤ (C : ℤ) - 1) := by
    intro i j
    simp only [E, Set.mem_compl_iff, Finset.mem_coe, Finset.mem_union, mem_HRect_sq, mem_SRect_sq]
    omega
  have hbase : Tile.oct (-2) (-2) ∈ E := by rw [hmem_oct]; omega
  -- All `x ≤ -2` octagons reach `oct (-2) (-2)`
  have hleft_half : ∀ x y : ℤ, x ≤ -2 → ReachIn E (Tile.oct x y) (Tile.oct (-2) (-2)) := by
    intro x y hx
    have h1 := reachIn_oct_horiz (A := E) (y := y) hx fun a _ ha2 => by rw [hmem_oct]; omega
    have h2 : ReachIn E (Tile.oct (-2) y) (Tile.oct (-2) (-2)) := by
      rcases le_total y (-2) with hy | hy
      · exact reachIn_oct_vert (A := E) (x := -2) hy fun b _ _ => by rw [hmem_oct]; omega
      · exact reachIn_symm (reachIn_oct_vert (A := E) (x := -2) hy fun b _ _ => by rw [hmem_oct]; omega)
    exact h1.trans h2
  -- All `y ≤ -2` octagons reach `oct (-2) (-2)`
  have hbot_half : ∀ x y : ℤ, y ≤ -2 → ReachIn E (Tile.oct x y) (Tile.oct (-2) (-2)) := by
    intro x y hy
    rcases le_total x (-2) with hx | hx
    · exact hleft_half x y hx
    · have h1 := reachIn_symm (reachIn_oct_horiz (A := E) (y := y) hx fun a _ _ => by rw [hmem_oct]; omega)
      exact h1.trans (hleft_half (-2) y le_rfl)
  -- All `y ≥ C + 1` octagons reach `oct (-2) (-2)`
  have htop_half : ∀ x y : ℤ, (C : ℤ) + 1 ≤ y → ReachIn E (Tile.oct x y) (Tile.oct (-2) (-2)) := by
    intro x y hy
    rcases le_total x (-2) with hx | hx
    · exact hleft_half x y hx
    · have h1 := reachIn_symm (reachIn_oct_horiz (A := E) (y := y) hx fun a _ _ => by rw [hmem_oct]; omega)
      exact h1.trans (hleft_half (-2) y le_rfl)
  -- All `x ≥ R + 1` octagons reach `oct (-2) (-2)`
  have hright_half : ∀ x y : ℤ, (R : ℤ) + 1 ≤ x → ReachIn E (Tile.oct x y) (Tile.oct (-2) (-2)) := by
    intro x y hx
    rcases le_total y (-2) with hy | hy
    · exact hbot_half x y hy
    · have h1 := reachIn_symm (reachIn_oct_vert (A := E) (x := x) hy fun b _ _ => by rw [hmem_oct]; omega)
      exact h1.trans (hbot_half x (-2) le_rfl)
  -- Any exterior octagon reaches `oct (-2) (-2)`
  have hoct_reach : ∀ x y : ℤ, Tile.oct x y ∈ E → ReachIn E (Tile.oct x y) (Tile.oct (-2) (-2)) := by
    intro x y hxy
    have hcond := (hmem_oct x y).mp hxy
    by_cases h1 : x ≤ -2
    · exact hleft_half x y h1
    · by_cases h2 : (R : ℤ) + 1 ≤ x
      · exact hright_half x y h2
      · by_cases h3 : y ≤ -2
        · exact hbot_half x y h3
        · by_cases h4 : (C : ℤ) + 1 ≤ y
          · exact htop_half x y h4
          · -- Must be one of the 4 corner octagons `(-1, -1), (-1, C), (R, -1), (R, C)`
            have hcorn : (x = -1 ∧ (y = -1 ∨ y = (C : ℤ))) ∨ (x = (R : ℤ) ∧ (y = -1 ∨ y = (C : ℤ))) := by
              omega
            rcases hcorn with ⟨rfl, hyc⟩ | ⟨rfl, hyc⟩
            · have hstep : ReachIn E (Tile.oct (-1) y) (Tile.oct (-2) y) :=
                reachIn_step hxy (by rw [hmem_oct]; omega)
                  (by show ((_ ∨ _) ∧ _) ∨ _; left; exact ⟨Or.inr (by ring), rfl⟩)
              exact hstep.trans (hleft_half (-2) y le_rfl)
            · have hstep : ReachIn E (Tile.oct (R : ℤ) y) (Tile.oct ((R : ℤ) + 1) y) :=
                reachIn_step hxy (by rw [hmem_oct]; omega)
                  (by show ((_ ∨ _) ∧ _) ∨ _; left; exact ⟨Or.inl rfl, rfl⟩)
              exact hstep.trans (hright_half ((R : ℤ) + 1) y le_rfl)
  refine isConnectedSet_of_star hbase fun u hu => ?_
  cases u with
  | oct x y => exact hoct_reach x y hu
  | sq i j =>
    have hij := (hmem_sq i j).mp hu
    have hcases : i ≤ -2 ∨ (R : ℤ) ≤ i ∨ j ≤ -2 ∨ (C : ℤ) ≤ j := by omega
    rcases hcases with h1 | h2 | h3 | h4
    · have hm : Tile.oct i j ∈ E := by rw [hmem_oct]; omega
      exact (reachIn_step hu hm (by show (i = i ∨ _) ∧ (j = j ∨ _); exact ⟨Or.inl rfl, Or.inl rfl⟩)).trans
        (hoct_reach i j hm)
    · have hm : Tile.oct (i + 1) j ∈ E := by rw [hmem_oct]; omega
      exact (reachIn_step hu hm (by show (_ ∨ i + 1 = i + 1) ∧ (j = j ∨ _); exact ⟨Or.inr rfl, Or.inl rfl⟩)).trans
        (hoct_reach (i + 1) j hm)
    · have hm : Tile.oct i j ∈ E := by rw [hmem_oct]; omega
      exact (reachIn_step hu hm (by show (i = i ∨ _) ∧ (j = j ∨ _); exact ⟨Or.inl rfl, Or.inl rfl⟩)).trans
        (hoct_reach i j hm)
    · have hm : Tile.oct i (j + 1) ∈ E := by rw [hmem_oct]; omega
      exact (reachIn_step hu hm (by show (i = i ∨ _) ∧ (_ ∨ j + 1 = j + 1); exact ⟨Or.inl rfl, Or.inr rfl⟩)).trans
        (hoct_reach i (j + 1) hm)

/-- `S(R, C)` is a valid enclosing shell of `H(R, C)` for every `R, C ≥ 2`. -/
theorem SRect_isValidEnclosingShell {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    IsValidEnclosingShell (HRect R C) (SRect R C) :=
  ⟨HRect_connected hR hC, SRect_connected hR hC, HRect_SRect_disjoint,
    SRect_contains_corona, exterior_connected hR hC⟩

/-! ## Section 4: Main Refutation Theorems -/

/-- General rectangular upper bound: `a(2RC + R + C - 3) ≤ 2R + 2C + 4` for all `R, C ≥ 2`. -/
theorem a394511_rect_le {R C : ℕ} (hR : 2 ≤ R) (hC : 2 ≤ C) :
    a394511 (2 * R * C + R + C - 3) ≤ 2 * R + 2 * C + 4 := by
  have h := a394511_le_of_shell (SRect_isValidEnclosingShell hR hC)
  rwa [card_HRect hR hC, card_SRect hR hC] at h

/-- Explicit counterexample at `n = 35` (`R = 3, C = 5`): `a(35) ≤ 20 < 22 = 2 * ⌈(35 + 17) / 5⌉`. -/
theorem a394511_35_le_20 : a394511 35 ≤ 20 := by
  simpa using a394511_rect_le (R := 3) (C := 5) (by decide) (by decide)

/-- **Refutation of Exley's Formula Conjecture (OEIS `A394511`):**
It is false that `a(n) = 2 * ⌈(n + 17) / 5⌉` for all `n ≥ 6`. -/
theorem not_exley_conjecture_formula :
    ¬ (∀ n : ℕ, 6 ≤ n → a394511 n = 2 * Nat.ceil (((n : ℚ) + 17) / 5)) := by
  intro h
  have h35 := h 35 (by decide)
  have hceil : Nat.ceil ((((35 : ℕ) : ℚ) + 17) / 5) = 11 := by
    rw [Nat.ceil_eq_iff (by norm_num)]
    norm_num
  rw [hceil] at h35
  have hle := a394511_35_le_20
  omega

/-- **Infinite Family Refutation:** For every `k ≥ 4`, `n_k = 2k^2 + 2k - 3 ≥ 6` satisfies
`a(n_k) ≤ 4k + 4 < 2 * ⌈(n_k + 17) / 5⌉`. -/
theorem exley_infinite_family_refutation {k : ℕ} (hk : 4 ≤ k) :
    6 ≤ 2 * k ^ 2 + 2 * k - 3 ∧
    a394511 (2 * k ^ 2 + 2 * k - 3) <
      2 * Nat.ceil ((((2 * k ^ 2 + 2 * k - 3 : ℕ) : ℚ) + 17) / 5) := by
  have hle : a394511 (2 * k ^ 2 + 2 * k - 3) ≤ 4 * k + 4 := by
    have h := a394511_rect_le (R := k) (C := k) (by omega) (by omega)
    have hidx : 2 * k * k + k + k - 3 = 2 * k ^ 2 + 2 * k - 3 := by ring_nf
    have hval : 2 * k + 2 * k + 4 = 4 * k + 4 := by ring
    rwa [hidx, hval] at h
  have hge9 : 9 ≤ 2 * k ^ 2 + 2 * k := by nlinarith
  have hge3 : 3 ≤ 2 * k ^ 2 + 2 * k := by omega
  have hge6 : 6 ≤ 2 * k ^ 2 + 2 * k - 3 := by omega
  refine ⟨hge6, lt_of_le_of_lt hle ?_⟩
  have hq : ((2 * k + 2 : ℕ) : ℚ) < ((((2 * k ^ 2 + 2 * k - 3 : ℕ) : ℚ) + 17) / 5) := by
    rw [Nat.cast_sub hge3]
    push_cast
    have hkQ : (4 : ℚ) ≤ (k : ℚ) := by exact_mod_cast hk
    nlinarith
  have hceil_gt : 2 * k + 2 < Nat.ceil ((((2 * k ^ 2 + 2 * k - 3 : ℕ) : ℚ) + 17) / 5) :=
    Nat.lt_ceil.mpr hq
  omega

/-- **Unconditional Refutation of Exley's Recurrence Conjecture (`a(n) = a(n - 5) + 2` for `n ≥ 11`):**
Any recurrence `a(n) = a(n - 5) + 2` for all `n ≥ 11` forces `a(261) = a(11) + 100 ≥ 100`,
contradicting `a(261) ≤ 48` (from `R = C = 11`, `n = 2*11^2 + 2*11 - 3 = 261`). -/
theorem not_exley_conjecture_recurrence :
    ¬ (∀ n : ℕ, 11 ≤ n → a394511 n = a394511 (n - 5) + 2) := by
  intro hrec
  have hlin : ∀ m : ℕ, a394511 (11 + 5 * m) = a394511 11 + 2 * m := by
    intro m
    induction m with
    | zero => simp
    | succ m ih =>
      have hstep := hrec (11 + 5 * (m + 1)) (by omega)
      have hsub : 11 + 5 * (m + 1) - 5 = 11 + 5 * m := by omega
      rw [hsub, ih] at hstep
      omega
  have h261_lb : 100 ≤ a394511 261 := by
    have h50 : a394511 261 = a394511 11 + 100 := by simpa using hlin 50
    omega
  have h261_ub : a394511 261 ≤ 48 := by
    simpa using a394511_rect_le (R := 11) (C := 11) (by decide) (by decide)
  omega

#print axioms isConnectedSet_iff_induce_connected
#print axioms SRect_isValidEnclosingShell
#print axioms a394511_rect_le
#print axioms a394511_35_le_20
#print axioms not_exley_conjecture_formula
#print axioms exley_infinite_family_refutation
#print axioms not_exley_conjecture_recurrence

end OpenMath.OeisA394511
