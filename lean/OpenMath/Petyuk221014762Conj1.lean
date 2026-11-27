import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Finset.Card
import Mathlib.Data.List.Nodup
import Mathlib.Tactic

/-!
# Refutation of Petyuk's Conjecture 1 (`arXiv:2210.14762v2`)

Primary source:
Anthony V. Petyuk, *"On word-representability of simplified de Bruijn graphs"*,
`arXiv:2210.14762v2` (`2023-07-12`), Section 1.1–1.2 & Section 4, Conjecture 1:
- **Definition (§1.2):** For alphabet `A = {0, ..., k - 1}` and word length `n`, the de Bruijn
  digraph `B(n, k)` has vertex set `A^n` and directed edges `x₁ x₂ ⋯ xₙ → x₂ ⋯ xₙ xₙ₊₁`.
  The simplified de Bruijn graph `S(n, k)` is the simple undirected graph obtained from `B(n, k)`
  by removing orientations and loops and replacing multiple edges by a single edge.
- **Definition (§1.1):** A simple graph `G` is word-representable if there exists a finite word `w`
  over `V(G)` (containing every vertex of `G`) such that for all distinct `u, v ∈ V(G)`, `u` and
  `v` are adjacent in `G` if and only if `u` and `v` alternate in `w`.
- **Conjecture 1 (§4):** *"$S(n, k)$ is non-word-rerpesentable for $n \ge 4$ and $k \ge 3$."*

This file proves completely (zero `sorry`, zero `native_decide`, standard axioms only):
1. **Halldórsson–Kitaev–Pyatkin (2016) Theorem (`threeColorable_isWordRepresentable`):**
   Every finite `3`-colorable simple graph is word-representable (via an explicit representing word
   constructed from the three color classes).
2. **Explicit `ℤ/3ℤ`-shift-equivariant proper `3`-coloring of `S(4, 3)` (`s43_coloring_proper`):**
   Verifies `c(x₁, x₂, x₃, x₄) = x₁ + f(x₂ - x₁, x₃ - x₂, x₄ - x₃)` in `Fin 3`, and records
   the triangle `0010–0100–1001` (`s43_has_triangle`).
3. **Refutation (`s43_wordRepresentable`, `not_petyuk_conjecture_1`):**
   `S(4, 3)` is word-representable, refuting Petyuk's Conjecture 1 at `(n, k) = (4, 3)`.
-/

namespace OpenMath.Petyuk221014762Conj1

/-! ## Section 1: Word-Representable Graphs (Primary-Source Definition) -/

/-- A list has no two consecutive equal elements. -/
def IsAlternating {α : Type*} : List α → Prop
  | [] => True
  | [_] => True
  | a :: b :: t => a ≠ b ∧ IsAlternating (b :: t)

/-- Index characterization of `IsAlternating`: every adjacent pair of entries is distinct. -/
theorem isAlternating_iff_forall_ne {α : Type*} :
    ∀ l : List α, IsAlternating l ↔ ∀ (i : ℕ) (hi : i + 1 < l.length), l[i] ≠ l[i + 1]
  | [] => by simp [IsAlternating]
  | [_] => by simp [IsAlternating]
  | a :: b :: t => by
    constructor
    · rintro ⟨hab, hbt⟩ i hi
      cases i with
      | zero => exact hab
      | succ j =>
        exact (isAlternating_iff_forall_ne (b :: t)).mp hbt j (by simpa using hi)
    · intro h
      refine ⟨h 0 (by simp), (isAlternating_iff_forall_ne (b :: t)).mpr fun j hj => ?_⟩
      exact h (j + 1) (by simpa using hj)

lemma isAlternating_of_append_left {α : Type*} :
    ∀ {l₁ l₂ : List α}, IsAlternating (l₁ ++ l₂) → IsAlternating l₂
  | [], _, h => h
  | [_], [], _ => trivial
  | [_], _ :: _, h => h.2
  | _ :: b :: t, l₂, h => isAlternating_of_append_left (l₁ := b :: t) (l₂ := l₂) h.2

lemma isAlternating_of_append_right {α : Type*} :
    ∀ {l₁ l₂ : List α}, IsAlternating (l₁ ++ l₂) → IsAlternating l₁
  | [], _, _ => trivial
  | [_], _, _ => trivial
  | _ :: b :: t, l₂, h => ⟨h.1, isAlternating_of_append_right (l₁ := b :: t) (l₂ := l₂) h.2⟩

/-- Restricting a word `w` to occurrences of `u` and `v`. -/
def restrictPair {V : Type*} [DecidableEq V] (w : List V) (u v : V) : List V :=
  w.filter fun x => decide (x = u ∨ x = v)

lemma restrictPair_comm {V : Type*} [DecidableEq V] (w : List V) (u v : V) :
    restrictPair w u v = restrictPair w v u := by
  unfold restrictPair
  congr 1
  funext x
  simp [or_comm]

/-- Two vertices `u, v` alternate in a word `w` if their restriction in `w` has no two
consecutive equal occurrences. -/
def Alternates {V : Type*} [DecidableEq V] (w : List V) (u v : V) : Prop :=
  IsAlternating (restrictPair w u v)

lemma alternates_comm {V : Type*} [DecidableEq V] (w : List V) (u v : V) :
    Alternates w u v ↔ Alternates w v u := by
  rw [Alternates, Alternates, restrictPair_comm]

/-- A word `w` represents a simple graph `G` if every vertex appears in `w` and for all distinct
vertices `u ≠ v`, `u` and `v` are adjacent in `G` iff they alternate in `w`. -/
def Represents {V : Type*} [DecidableEq V] (G : SimpleGraph V) (w : List V) : Prop :=
  (∀ v : V, v ∈ w) ∧ ∀ u v : V, u ≠ v → (G.Adj u v ↔ Alternates w u v)

/-- A simple graph `G` is word-representable if some finite word over `V` represents `G`. -/
def IsWordRepresentable {V : Type*} [DecidableEq V] (G : SimpleGraph V) : Prop :=
  ∃ w : List V, Represents G w

/-! ## Section 2: List Restriction Helpers for the 3-Coloring Construction -/

lemma restrictPair_append {V : Type*} [DecidableEq V] (l₁ l₂ : List V) (u v : V) :
    restrictPair (l₁ ++ l₂) u v = restrictPair l₁ u v ++ restrictPair l₂ u v := by
  simp [restrictPair, List.filter_append]

lemma restrictPair_flatMap {α V : Type*} [DecidableEq V] (L : List α) (f : α → List V) (u v : V) :
    restrictPair (L.flatMap f) u v = L.flatMap (fun a => restrictPair (f a) u v) := by
  induction L with
  | nil => simp [restrictPair]
  | cons a t ih =>
    simp only [List.flatMap_cons, restrictPair_append, ih]

lemma restrictPair_reverse {V : Type*} [DecidableEq V] (l : List V) (u v : V) :
    restrictPair l.reverse u v = (restrictPair l u v).reverse :=
  List.filter_reverse

lemma restrictPair_eq_nil {V : Type*} [DecidableEq V] {l : List V} {u v : V}
    (hu : u ∉ l) (hv : v ∉ l) : restrictPair l u v = [] := by
  unfold restrictPair
  rw [List.filter_eq_nil_iff]
  intro x hx
  simp only [decide_eq_true_eq, not_or]
  exact ⟨fun h => hu (h ▸ hx), fun h => hv (h ▸ hx)⟩

lemma restrictPair_eq_singleton_left {V : Type*} [DecidableEq V] {l : List V} {u v : V}
    (hnd : l.Nodup) (hu : u ∈ l) (hv : v ∉ l) : restrictPair l u v = [u] := by
  induction l with
  | nil => cases hu
  | cons x t ih =>
    rw [List.nodup_cons] at hnd
    have hvx : v ≠ x := fun h => hv (h ▸ List.mem_cons_self)
    have hvt : v ∉ t := fun h => hv (List.mem_cons_of_mem x h)
    unfold restrictPair
    rw [List.filter_cons]
    by_cases hux : x = u
    · subst hux
      simp only [true_or, decide_true, ↓reduceIte]
      congr 1
      exact restrictPair_eq_nil hnd.1 hvt
    · have hcond : decide (x = u ∨ x = v) = false := by
        simp [hux, Ne.symm hvx]
      rw [hcond]
      have hut : u ∈ t := by
        rcases List.mem_cons.mp hu with rfl | ht
        · exact (hux rfl).elim
        · exact ht
      exact ih hnd.2 hut hvt

lemma restrictPair_eq_singleton_right {V : Type*} [DecidableEq V] {l : List V} {u v : V}
    (hnd : l.Nodup) (hu : u ∉ l) (hv : v ∈ l) : restrictPair l u v = [v] := by
  rw [restrictPair_comm]
  exact restrictPair_eq_singleton_left hnd hv hu

lemma restrictPair_both_mem_nodup {V : Type*} [DecidableEq V] {l : List V} {u v : V}
    (hnd : l.Nodup) (huv : u ≠ v) (hu : u ∈ l) (hv : v ∈ l) :
    restrictPair l u v = [u, v] ∨ restrictPair l u v = [v, u] := by
  induction l with
  | nil => cases hu
  | cons x t ih =>
    rw [List.nodup_cons] at hnd
    unfold restrictPair
    rw [List.filter_cons]
    by_cases hxu : x = u
    · subst hxu
      simp only [true_or, decide_true, ↓reduceIte]
      have hvt : v ∈ t := by
        rcases List.mem_cons.mp hv with rfl | ht
        · exact (huv rfl).elim
        · exact ht
      left
      congr 1
      exact restrictPair_eq_singleton_right hnd.2 hnd.1 hvt
    · by_cases hxv : x = v
      · subst hxv
        simp only [or_true, decide_true, ↓reduceIte]
        have hut : u ∈ t := by
          rcases List.mem_cons.mp hu with rfl | ht
          · exact (hxu rfl).elim
          · exact ht
        right
        congr 1
        exact restrictPair_eq_singleton_left hnd.2 hut hnd.1
      · have hcond : decide (x = u ∨ x = v) = false := by simp [hxu, hxv]
        rw [hcond]
        have hut : u ∈ t := by
          rcases List.mem_cons.mp hu with rfl | ht
          · exact (hxu rfl).elim
          · exact ht
        have hvt : v ∈ t := by
          rcases List.mem_cons.mp hv with rfl | ht
          · exact (hxv rfl).elim
          · exact ht
        exact ih hnd.2 hut hvt

lemma isAlternating_flatMap_quad {α V : Type*} {x y : V} (hxy : x ≠ y)
    (L : List α) (f : α → List V) (hf : ∀ a ∈ L, f a = [x, y, x, y]) :
    IsAlternating (L.flatMap f) ∧
      ((L.flatMap f).head? = none ∨ (L.flatMap f).head? = some x) := by
  induction L with
  | nil => simp [IsAlternating]
  | cons a t ih =>
    have ha : f a = [x, y, x, y] := hf a List.mem_cons_self
    have ⟨halt, hhead⟩ := ih fun b hb => hf b (List.mem_cons_of_mem a hb)
    rw [List.flatMap_cons, ha]
    refine ⟨?_, Or.inr rfl⟩
    show IsAlternating (x :: y :: x :: y :: t.flatMap f)
    refine ⟨hxy, hxy.symm, hxy, ?_⟩
    cases htf : t.flatMap f with
    | nil => trivial
    | cons z rest =>
      rw [htf] at hhead halt
      rcases hhead with hnone | hsome
      · simp at hnone
      · simp only [List.head?_cons, Option.some.injEq] at hsome
        subst hsome
        exact ⟨hxy.symm, halt⟩

lemma not_isAlternating_flatMap_of_mem {α V : Type*} {L : List α} {f : α → List V}
    {a : α} (ha : a ∈ L) (hbad : ¬ IsAlternating (f a)) :
    ¬ IsAlternating (L.flatMap f) := by
  obtain ⟨l₁, l₂, rfl⟩ := List.append_of_mem ha
  rw [List.flatMap_append, List.flatMap_cons]
  intro h
  have h1 := isAlternating_of_append_left h
  have h2 := isAlternating_of_append_right h1
  exact hbad h2

/-! ## Section 3: Halldórsson–Kitaev–Pyatkin Theorem (Every 3-Colorable Graph is Word-Representable) -/

section ThreeColorable

variable {V : Type*} [DecidableEq V]
variable (G : SimpleGraph V) [DecidableRel G.Adj]

/-- Single permutation block `P_y(X, Y) = N_X(y) ++ [y] ++ (X \ N_X(y)) ++ (Y \ {y})`. -/
def permBlock (X Y : List V) (y : V) : List V :=
  (X.filter fun x => decide (G.Adj x y)) ++ [y] ++
    (X.filter fun x => decide (¬ G.Adj x y)) ++ (Y.filter fun z => decide (z ≠ y))

lemma restrictPair_permBlock_across {X Y : List V} {y u v : V}
    (hXnd : X.Nodup) (hYnd : Y.Nodup) (hdisj : ∀ z, z ∈ X → z ∉ Y)
    (hyY : y ∈ Y) (huX : u ∈ X) (hvY : v ∈ Y) :
    restrictPair (permBlock G X Y y) u v =
      if v = y ∧ ¬ G.Adj u v then [v, u] else [u, v] := by
  have huY : u ∉ Y := hdisj u huX
  have hvX : v ∉ X := fun h => hdisj v h hvY
  have huy : u ≠ y := fun h => huY (h ▸ hyY)
  have hX1nd : (X.filter fun x => decide (G.Adj x y)).Nodup := hXnd.filter _
  have hX2nd : (X.filter fun x => decide (¬ G.Adj x y)).Nodup := hXnd.filter _
  have hY1nd : (Y.filter fun z => decide (z ≠ y)).Nodup := hYnd.filter _
  have hvX1 : v ∉ X.filter fun x => decide (G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have hvX2 : v ∉ X.filter fun x => decide (¬ G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have huY1 : u ∉ Y.filter fun z => decide (z ≠ y) := fun h => huY (List.mem_of_mem_filter h)
  unfold permBlock
  simp only [restrictPair_append]
  by_cases hvy : v = y
  · subst hvy
    have hvY1 : v ∉ Y.filter fun z => decide (z ≠ v) := by simp
    have hsing : restrictPair [v] u v = [v] := by
      simp [restrictPair]
    have hnilY : restrictPair (Y.filter fun z => decide (z ≠ v)) u v = [] :=
      restrictPair_eq_nil huY1 hvY1
    by_cases hadj : G.Adj u v
    · have huX1 : u ∈ X.filter fun x => decide (G.Adj x v) := by
        simp [List.mem_filter, huX, hadj]
      have huX2 : u ∉ X.filter fun x => decide (¬ G.Adj x v) := by
        simp [List.mem_filter, hadj]
      rw [restrictPair_eq_singleton_left hX1nd huX1 hvX1, hsing,
        restrictPair_eq_nil huX2 hvX2, hnilY]
      simp [hadj]
    · have huX1 : u ∉ X.filter fun x => decide (G.Adj x v) := by
        simp [List.mem_filter, hadj]
      have huX2 : u ∈ X.filter fun x => decide (¬ G.Adj x v) := by
        simp [List.mem_filter, huX, hadj]
      rw [restrictPair_eq_nil huX1 hvX1, hsing,
        restrictPair_eq_singleton_left hX2nd huX2 hvX2, hnilY]
      simp [hadj]
  · have hvy_ne : ¬ (v = y ∧ ¬ G.Adj u v) := fun h => hvy h.1
    rw [ite_eq_right hvy_ne]
    have hsing : restrictPair [y] u v = [] := by
      simp [restrictPair, huy.symm, Ne.symm hvy]
    have hvY1 : v ∈ Y.filter fun z => decide (z ≠ y) := by
      simp [List.mem_filter, hvY, hvy]
    have hYpart : restrictPair (Y.filter fun z => decide (z ≠ y)) u v = [v] :=
      restrictPair_eq_singleton_right hY1nd huY1 hvY1
    by_cases hadj : G.Adj u y
    · have huX1 : u ∈ X.filter fun x => decide (G.Adj x y) := by
        simp [List.mem_filter, huX, hadj]
      have huX2 : u ∉ X.filter fun x => decide (¬ G.Adj x y) := by
        simp [List.mem_filter, hadj]
      rw [restrictPair_eq_singleton_left hX1nd huX1 hvX1, hsing,
        restrictPair_eq_nil huX2 hvX2, hYpart]
      simp
    · have huX1 : u ∉ X.filter fun x => decide (G.Adj x y) := by
        simp [List.mem_filter, hadj]
      have huX2 : u ∈ X.filter fun x => decide (¬ G.Adj x y) := by
        simp [List.mem_filter, huX, hadj]
      rw [restrictPair_eq_nil huX1 hvX1, hsing,
        restrictPair_eq_singleton_left hX2nd huX2 hvX2, hYpart]
      simp

lemma restrictPair_permBlock_only_X {X Y : List V} {y u v : V}
    (hXnd : X.Nodup) (hdisj : ∀ z, z ∈ X → z ∉ Y)
    (hyY : y ∈ Y) (huX : u ∈ X) (hvX : v ∉ X) (hvY : v ∉ Y) :
    restrictPair (permBlock G X Y y) u v = [u] := by
  have huY : u ∉ Y := hdisj u huX
  have huy : u ≠ y := fun h => huY (h ▸ hyY)
  have hvy : v ≠ y := fun h => hvY (h ▸ hyY)
  have hX1nd : (X.filter fun x => decide (G.Adj x y)).Nodup := hXnd.filter _
  have hX2nd : (X.filter fun x => decide (¬ G.Adj x y)).Nodup := hXnd.filter _
  have hvX1 : v ∉ X.filter fun x => decide (G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have hvX2 : v ∉ X.filter fun x => decide (¬ G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have huY1 : u ∉ Y.filter fun z => decide (z ≠ y) := fun h => huY (List.mem_of_mem_filter h)
  have hvY1 : v ∉ Y.filter fun z => decide (z ≠ y) := fun h => hvY (List.mem_of_mem_filter h)
  unfold permBlock
  simp only [restrictPair_append]
  have hsing : restrictPair [y] u v = [] := by
    simp [restrictPair, huy.symm, hvy.symm]
  have hnilY : restrictPair (Y.filter fun z => decide (z ≠ y)) u v = [] :=
    restrictPair_eq_nil huY1 hvY1
  by_cases hadj : G.Adj u y
  · have huX1 : u ∈ X.filter fun x => decide (G.Adj x y) := by simp [List.mem_filter, huX, hadj]
    have huX2 : u ∉ X.filter fun x => decide (¬ G.Adj x y) := by simp [List.mem_filter, hadj]
    rw [restrictPair_eq_singleton_left hX1nd huX1 hvX1, hsing,
      restrictPair_eq_nil huX2 hvX2, hnilY]
    simp
  · have huX1 : u ∉ X.filter fun x => decide (G.Adj x y) := by simp [List.mem_filter, hadj]
    have huX2 : u ∈ X.filter fun x => decide (¬ G.Adj x y) := by simp [List.mem_filter, huX, hadj]
    rw [restrictPair_eq_nil huX1 hvX1, hsing,
      restrictPair_eq_singleton_left hX2nd huX2 hvX2, hnilY]
    simp

lemma restrictPair_permBlock_only_Y {X Y : List V} {y u v : V}
    (hYnd : Y.Nodup) (hdisj : ∀ z, z ∈ X → z ∉ Y)
    (hyY : y ∈ Y) (huX : u ∉ X) (huY : u ∉ Y) (hvY : v ∈ Y) :
    restrictPair (permBlock G X Y y) u v = [v] := by
  have hvX : v ∉ X := fun h => hdisj v h hvY
  have huy : u ≠ y := fun h => huY (h ▸ hyY)
  have hY1nd : (Y.filter fun z => decide (z ≠ y)).Nodup := hYnd.filter _
  have huX1 : u ∉ X.filter fun x => decide (G.Adj x y) := fun h => huX (List.mem_of_mem_filter h)
  have hvX1 : v ∉ X.filter fun x => decide (G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have huX2 : u ∉ X.filter fun x => decide (¬ G.Adj x y) := fun h => huX (List.mem_of_mem_filter h)
  have hvX2 : v ∉ X.filter fun x => decide (¬ G.Adj x y) := fun h => hvX (List.mem_of_mem_filter h)
  have huY1 : u ∉ Y.filter fun z => decide (z ≠ y) := fun h => huY (List.mem_of_mem_filter h)
  unfold permBlock
  simp only [restrictPair_append]
  rw [restrictPair_eq_nil huX1 hvX1, restrictPair_eq_nil huX2 hvX2]
  by_cases hvy : v = y
  · subst hvy
    have hvY1 : v ∉ Y.filter fun z => decide (z ≠ v) := by simp
    have hsing : restrictPair [v] u v = [v] := by simp [restrictPair]
    rw [hsing, restrictPair_eq_nil huY1 hvY1]
    simp
  · have hsing : restrictPair [y] u v = [] := by simp [restrictPair, huy.symm, Ne.symm hvy]
    have hvY1 : v ∈ Y.filter fun z => decide (z ≠ y) := by simp [List.mem_filter, hvY, hvy]
    rw [hsing, restrictPair_eq_singleton_right hY1nd huY1 hvY1]
    simp

/-- **Halldórsson–Kitaev–Pyatkin (2016), Theorem 2:**
Every finite `3`-colorable simple graph is word-representable. -/
theorem threeColorable_isWordRepresentable [Fintype V]
    (c : V → Fin 3) (hc : ∀ u v : V, G.Adj u v → c u ≠ c v) :
    IsWordRepresentable G := by
  let A0 : List V := (Finset.univ.filter fun v : V => c v = 0).toList
  let A1 : List V := (Finset.univ.filter fun v : V => c v = 1).toList
  let A2 : List V := (Finset.univ.filter fun v : V => c v = 2).toList
  have hnd0 : A0.Nodup := Finset.nodup_toList _
  have hnd1 : A1.Nodup := Finset.nodup_toList _
  have hnd2 : A2.Nodup := Finset.nodup_toList _
  have hmem0 : ∀ v : V, v ∈ A0 ↔ c v = 0 := by intro v; simp [A0]
  have hmem1 : ∀ v : V, v ∈ A1 ↔ c v = 1 := by intro v; simp [A1]
  have hmem2 : ∀ v : V, v ∈ A2 ↔ c v = 2 := by intro v; simp [A2]
  have hdisj01 : ∀ z, z ∈ A0 → z ∉ A1 := by
    intro z h0 h1; rw [hmem0] at h0; rw [hmem1] at h1; rw [h0] at h1; exact absurd h1 (by decide)
  have hdisj20 : ∀ z, z ∈ A2 → z ∉ A0 := by
    intro z h2 h0; rw [hmem2] at h2; rw [hmem0] at h0; rw [h2] at h0; exact absurd h0 (by decide)
  have hdisj12 : ∀ z, z ∈ A1 → z ∉ A2 := by
    intro z h1 h2; rw [hmem1] at h1; rw [hmem2] at h2; rw [h1] at h2; exact absurd h2 (by decide)
  let M : ℕ := 1 + max A0.length (max A1.length A2.length)
  let block01 : ℕ → List V := fun t =>
    if h : 1 ≤ t ∧ t - 1 < A1.length then permBlock G A0 A1 (A1[t - 1]'h.2) else A0 ++ A1
  let block20 : ℕ → List V := fun t =>
    if h : 1 ≤ t ∧ t - 1 < A0.length then permBlock G A2 A0 (A0[t - 1]'h.2) else A2 ++ A0.reverse
  let block12 : ℕ → List V := fun t =>
    if h : 1 ≤ t ∧ t - 1 < A2.length then permBlock G A1 A2 (A2[t - 1]'h.2)
    else A1.reverse ++ A2.reverse
  let round : ℕ → List V := fun t => block01 t ++ block20 t ++ block12 t
  let w : List V := (List.range M).flatMap round
  have h0_mem : 0 ∈ List.range M := List.mem_range.mpr (by omega)
  have hround0 : round 0 = (A0 ++ A1) ++ (A2 ++ A0.reverse) ++ (A1.reverse ++ A2.reverse) := by
    simp [round, block01, block20, block12]
  refine ⟨w, ?_, ?_⟩
  · intro v
    refine List.mem_flatMap.mpr ⟨0, h0_mem, ?_⟩
    rw [hround0]
    have hcv : c v = 0 ∨ c v = 1 ∨ c v = 2 := by
      generalize h : c v = x
      fin_cases x <;> simp
    rcases hcv with h0 | h1 | h2
    · have hv : v ∈ A0 := (hmem0 v).mpr h0
      simp [hv]
    · have hv : v ∈ A1 := (hmem1 v).mpr h1
      simp [hv]
    · have hv : v ∈ A2 := (hmem2 v).mpr h2
      simp [hv]
  · -- Helper for pairs `(u, v)` with `(c u, c v) = (0, 1)`
    have hcase01 : ∀ u v : V, c u = 0 → c v = 1 → (G.Adj u v ↔ Alternates w u v) := by
      intro u v hu0 hv1
      have huA0 : u ∈ A0 := (hmem0 u).mpr hu0
      have hvA1 : v ∈ A1 := (hmem1 v).mpr hv1
      have huA1 : u ∉ A1 := hdisj01 u huA0
      have hvA0 : v ∉ A0 := fun h => hdisj01 v h hvA1
      have huA2 : u ∉ A2 := fun h => hdisj20 u h huA0
      have hvA2 : v ∉ A2 := hdisj12 v hvA1
      have huv : u ≠ v := fun h => huA1 (h ▸ hvA1)
      have hb20 : ∀ t, restrictPair (block20 t) u v = [u] := by
        intro t
        dsimp only [block20]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_Y G hnd0 hdisj20 (List.getElem_mem h.2) hvA2 hvA0 huA0
        · rw [restrictPair_append, restrictPair_eq_nil huA2 hvA2, restrictPair_reverse,
            restrictPair_eq_singleton_left hnd0 huA0 hvA0]
          simp
      have hb12 : ∀ t, restrictPair (block12 t) u v = [v] := by
        intro t
        dsimp only [block12]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_X G hnd1 hdisj12 (List.getElem_mem h.2) hvA1 huA1 huA2
        · rw [restrictPair_append, restrictPair_reverse, restrictPair_reverse,
            restrictPair_eq_singleton_right hnd1 huA1 hvA1, restrictPair_eq_nil huA2 hvA2]
          simp
      have hb01 : ∀ t, restrictPair (block01 t) u v =
          if h : 1 ≤ t ∧ t - 1 < A1.length then
            if v = A1[t - 1]'h.2 ∧ ¬ G.Adj u v then [v, u] else [u, v]
          else [u, v] := by
        intro t
        dsimp only [block01]
        by_cases h : 1 ≤ t ∧ t - 1 < A1.length
        · rw [dite_eq_left h, dite_eq_left h]
          exact restrictPair_permBlock_across G hnd0 hnd1 hdisj01 (List.getElem_mem h.2) huA0 hvA1
        · rw [dite_eq_right h, dite_eq_right h, restrictPair_append,
            restrictPair_eq_singleton_left hnd0 huA0 hvA0,
            restrictPair_eq_singleton_right hnd1 huA1 hvA1]
          rfl
      constructor
      · intro hadj
        unfold Alternates
        rw [restrictPair_flatMap]
        refine (isAlternating_flatMap_quad huv (List.range M) _ fun t _ => ?_).1
        simp only [round, restrictPair_append, hb01 t, hb20 t, hb12 t]
        split_ifs with h h2
        · exact (h2.2 hadj).elim
        · rfl
        · rfl
      · intro halt
        by_contra hnadj
        obtain ⟨k, hk, hkv⟩ := List.getElem_of_mem hvA1
        have ht_mem : k + 1 ∈ List.range M := List.mem_range.mpr (by omega)
        have hbad : ¬ IsAlternating (restrictPair (round (k + 1)) u v) := by
          simp only [round, restrictPair_append, hb01 (k + 1), hb20 (k + 1), hb12 (k + 1)]
          have hcond : 1 ≤ k + 1 ∧ k + 1 - 1 < A1.length := ⟨by omega, by omega⟩
          rw [dite_eq_left hcond]
          have hcond2 : v = A1[k + 1 - 1]'hcond.2 ∧ ¬ G.Adj u v := ⟨hkv.symm, hnadj⟩
          rw [ite_eq_left hcond2]
          show ¬ IsAlternating [v, u, u, v]
          intro h
          exact h.2.1 rfl
        unfold Alternates at halt
        rw [restrictPair_flatMap] at halt
        exact not_isAlternating_flatMap_of_mem ht_mem hbad halt
    -- Helper for pairs `(u, v)` with `(c u, c v) = (1, 2)`
    have hcase12 : ∀ u v : V, c u = 1 → c v = 2 → (G.Adj u v ↔ Alternates w u v) := by
      intro u v hu1 hv2
      have huA1 : u ∈ A1 := (hmem1 u).mpr hu1
      have hvA2 : v ∈ A2 := (hmem2 v).mpr hv2
      have huA2 : u ∉ A2 := hdisj12 u huA1
      have hvA1 : v ∉ A1 := fun h => hdisj12 v h hvA2
      have huA0 : u ∉ A0 := fun h => hdisj01 u h huA1
      have hvA0 : v ∉ A0 := hdisj20 v hvA2
      have huv : u ≠ v := fun h => huA2 (h ▸ hvA2)
      have hb01 : ∀ t, restrictPair (block01 t) u v = [u] := by
        intro t
        dsimp only [block01]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_Y G hnd1 hdisj01 (List.getElem_mem h.2) hvA0 hvA1 huA1
        · rw [restrictPair_append, restrictPair_eq_nil huA0 hvA0,
            restrictPair_eq_singleton_left hnd1 huA1 hvA1]
          simp
      have hb20 : ∀ t, restrictPair (block20 t) u v = [v] := by
        intro t
        dsimp only [block20]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_X G hnd2 hdisj20 (List.getElem_mem h.2) hvA2 huA2 huA0
        · rw [restrictPair_append, restrictPair_eq_singleton_right hnd2 huA2 hvA2,
            restrictPair_reverse, restrictPair_eq_nil huA0 hvA0]
          simp
      have hb12 : ∀ t, restrictPair (block12 t) u v =
          if h : 1 ≤ t ∧ t - 1 < A2.length then
            if v = A2[t - 1]'h.2 ∧ ¬ G.Adj u v then [v, u] else [u, v]
          else [u, v] := by
        intro t
        dsimp only [block12]
        by_cases h : 1 ≤ t ∧ t - 1 < A2.length
        · rw [dite_eq_left h, dite_eq_left h]
          exact restrictPair_permBlock_across G hnd1 hnd2 hdisj12 (List.getElem_mem h.2) huA1 hvA2
        · rw [dite_eq_right h, dite_eq_right h, restrictPair_append, restrictPair_reverse,
            restrictPair_reverse, restrictPair_eq_singleton_left hnd1 huA1 hvA1,
            restrictPair_eq_singleton_right hnd2 huA2 hvA2]
          rfl
      constructor
      · intro hadj
        unfold Alternates
        rw [restrictPair_flatMap]
        refine (isAlternating_flatMap_quad huv (List.range M) _ fun t _ => ?_).1
        simp only [round, restrictPair_append, hb01 t, hb20 t, hb12 t]
        split_ifs with h h2
        · exact (h2.2 hadj).elim
        · rfl
        · rfl
      · intro halt
        by_contra hnadj
        obtain ⟨k, hk, hkv⟩ := List.getElem_of_mem hvA2
        have ht_mem : k + 1 ∈ List.range M := List.mem_range.mpr (by omega)
        have hbad : ¬ IsAlternating (restrictPair (round (k + 1)) u v) := by
          simp only [round, restrictPair_append, hb01 (k + 1), hb20 (k + 1), hb12 (k + 1)]
          have hcond : 1 ≤ k + 1 ∧ k + 1 - 1 < A2.length := ⟨by omega, by omega⟩
          rw [dite_eq_left hcond]
          have hcond2 : v = A2[k + 1 - 1]'hcond.2 ∧ ¬ G.Adj u v := ⟨hkv.symm, hnadj⟩
          rw [ite_eq_left hcond2]
          show ¬ IsAlternating [u, v, v, u]
          intro h
          exact h.2.1 rfl
        unfold Alternates at halt
        rw [restrictPair_flatMap] at halt
        exact not_isAlternating_flatMap_of_mem ht_mem hbad halt
    -- Helper for pairs `(u, v)` with `(c u, c v) = (2, 0)`
    have hcase20 : ∀ u v : V, c u = 2 → c v = 0 → (G.Adj u v ↔ Alternates w u v) := by
      intro u v hu2 hv0
      have huA2 : u ∈ A2 := (hmem2 u).mpr hu2
      have hvA0 : v ∈ A0 := (hmem0 v).mpr hv0
      have huA0 : u ∉ A0 := hdisj20 u huA2
      have hvA2 : v ∉ A2 := fun h => hdisj20 v h hvA0
      have huA1 : u ∉ A1 := fun h => hdisj12 u h huA2
      have hvA1 : v ∉ A1 := hdisj01 v hvA0
      have huv : u ≠ v := fun h => huA0 (h ▸ hvA0)
      have hb01 : ∀ t, restrictPair (block01 t) u v = [v] := by
        intro t
        dsimp only [block01]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_X G hnd0 hdisj01 (List.getElem_mem h.2) hvA0 huA0 huA1
        · rw [restrictPair_append, restrictPair_eq_singleton_right hnd0 huA0 hvA0,
            restrictPair_eq_nil huA1 hvA1]
          simp
      have hb12 : ∀ t, restrictPair (block12 t) u v = [u] := by
        intro t
        dsimp only [block12]
        split_ifs with h
        · rw [restrictPair_comm]
          exact restrictPair_permBlock_only_Y G hnd2 hdisj12 (List.getElem_mem h.2) hvA1 hvA2 huA2
        · rw [restrictPair_append, restrictPair_reverse, restrictPair_reverse,
            restrictPair_eq_nil huA1 hvA1, restrictPair_eq_singleton_left hnd2 huA2 hvA2]
          simp
      have hb20 : ∀ t, restrictPair (block20 t) u v =
          if h : 1 ≤ t ∧ t - 1 < A0.length then
            if v = A0[t - 1]'h.2 ∧ ¬ G.Adj u v then [v, u] else [u, v]
          else [u, v] := by
        intro t
        dsimp only [block20]
        by_cases h : 1 ≤ t ∧ t - 1 < A0.length
        · rw [dite_eq_left h, dite_eq_left h]
          exact restrictPair_permBlock_across G hnd2 hnd0 hdisj20 (List.getElem_mem h.2) huA2 hvA0
        · rw [dite_eq_right h, dite_eq_right h, restrictPair_append,
            restrictPair_eq_singleton_left hnd2 huA2 hvA2,
            restrictPair_reverse, restrictPair_eq_singleton_right hnd0 huA0 hvA0]
          rfl
      constructor
      · intro hadj
        unfold Alternates
        rw [restrictPair_flatMap]
        refine (isAlternating_flatMap_quad huv.symm (List.range M) _ fun t _ => ?_).1
        simp only [round, restrictPair_append, hb01 t, hb20 t, hb12 t]
        split_ifs with h h2
        · exact (h2.2 hadj).elim
        · rfl
        · rfl
      · intro halt
        by_contra hnadj
        obtain ⟨k, hk, hkv⟩ := List.getElem_of_mem hvA0
        have ht_mem : k + 1 ∈ List.range M := List.mem_range.mpr (by omega)
        have hbad : ¬ IsAlternating (restrictPair (round (k + 1)) u v) := by
          simp only [round, restrictPair_append, hb01 (k + 1), hb20 (k + 1), hb12 (k + 1)]
          have hcond : 1 ≤ k + 1 ∧ k + 1 - 1 < A0.length := ⟨by omega, by omega⟩
          rw [dite_eq_left hcond]
          have hcond2 : v = A0[k + 1 - 1]'hcond.2 ∧ ¬ G.Adj u v := ⟨hkv.symm, hnadj⟩
          rw [ite_eq_left hcond2]
          show ¬ IsAlternating [v, v, u, u]
          intro h
          exact h.1 rfl
        unfold Alternates at halt
        rw [restrictPair_flatMap] at halt
        exact not_isAlternating_flatMap_of_mem ht_mem hbad halt
    -- Helper for same-color pairs `c u = c v`
    have hcaseSame : ∀ {A : List V} (hnd : A.Nodup) {u v : V},
        u ≠ v → u ∈ A → v ∈ A →
        restrictPair (round 0) u v = restrictPair A u v ++ (restrictPair A u v).reverse →
        ¬ Alternates w u v := by
      intro A hnd u v huv huA hvA hr0 halt
      have hbad : ¬ IsAlternating (restrictPair (round 0) u v) := by
        rw [hr0]
        rcases restrictPair_both_mem_nodup hnd huv huA hvA with hp | hp <;> rw [hp]
        · show ¬ IsAlternating [u, v, v, u]
          intro h; exact h.2.1 rfl
        · show ¬ IsAlternating [v, u, u, v]
          intro h; exact h.2.1 rfl
      unfold Alternates at halt
      rw [restrictPair_flatMap] at halt
      exact not_isAlternating_flatMap_of_mem h0_mem hbad halt
    -- Dispatch all 9 color pairs `(c u, c v) ∈ Fin 3 × Fin 3`
    intro u v huv
    generalize hcu : c u = cu
    generalize hcv : c v = cv
    fin_cases cu <;> fin_cases cv
    · -- (0, 0)
      have hna : ¬ G.Adj u v := fun h => hc u v h (hcu.trans hcv.symm)
      have huA0 : u ∈ A0 := (hmem0 u).mpr hcu
      have hvA0 : v ∈ A0 := (hmem0 v).mpr hcv
      have hr0 : restrictPair (round 0) u v = restrictPair A0 u v ++ (restrictPair A0 u v).reverse := by
        rw [hround0]
        simp only [restrictPair_append, restrictPair_reverse]
        rw [restrictPair_eq_nil (hdisj01 u huA0) (hdisj01 v hvA0),
          restrictPair_eq_nil (fun h => hdisj20 u h huA0) (fun h => hdisj20 v h hvA0)]
        simp
      exact iff_of_false hna (hcaseSame hnd0 huv huA0 hvA0 hr0)
    · exact hcase01 u v hcu hcv
    · rw [G.adj_comm, alternates_comm]
      exact hcase20 v u hcv hcu
    · rw [G.adj_comm, alternates_comm]
      exact hcase01 v u hcv hcu
    · -- (1, 1)
      have hna : ¬ G.Adj u v := fun h => hc u v h (hcu.trans hcv.symm)
      have huA1 : u ∈ A1 := (hmem1 u).mpr hcu
      have hvA1 : v ∈ A1 := (hmem1 v).mpr hcv
      have hr0 : restrictPair (round 0) u v = restrictPair A1 u v ++ (restrictPair A1 u v).reverse := by
        rw [hround0]
        simp only [restrictPair_append, restrictPair_reverse]
        rw [restrictPair_eq_nil (fun h => hdisj01 u h huA1) (fun h => hdisj01 v h hvA1),
          restrictPair_eq_nil (hdisj12 u huA1) (hdisj12 v hvA1)]
        simp
      exact iff_of_false hna (hcaseSame hnd1 huv huA1 hvA1 hr0)
    · exact hcase12 u v hcu hcv
    · exact hcase20 u v hcu hcv
    · rw [G.adj_comm, alternates_comm]
      exact hcase12 v u hcv hcu
    · -- (2, 2)
      have hna : ¬ G.Adj u v := fun h => hc u v h (hcu.trans hcv.symm)
      have huA2 : u ∈ A2 := (hmem2 u).mpr hcu
      have hvA2 : v ∈ A2 := (hmem2 v).mpr hcv
      have hr0 : restrictPair (round 0) u v = restrictPair A2 u v ++ (restrictPair A2 u v).reverse := by
        rw [hround0]
        simp only [restrictPair_append, restrictPair_reverse]
        rw [restrictPair_eq_nil (hdisj20 u huA2) (hdisj20 v hvA2),
          restrictPair_eq_nil (fun h => hdisj12 u h huA2) (fun h => hdisj12 v h hvA2)]
        simp
      exact iff_of_false hna (hcaseSame hnd2 huv huA2 hvA2 hr0)

end ThreeColorable

/-! ## Section 4: Simplified de Bruijn Graph `S(n, k)` -/

/-- Directed edge in the de Bruijn graph `B(n, k)`: `x₁ x₂ ⋯ xₙ → x₂ ⋯ xₙ xₙ₊₁`. -/
def DeBruijnArc {n k : ℕ} (u v : Fin n → Fin k) : Prop :=
  ∀ (i : ℕ) (hi : i + 1 < n), u ⟨i + 1, hi⟩ = v ⟨i, by omega⟩

instance {n k : ℕ} (u v : Fin n → Fin k) : Decidable (DeBruijnArc u v) :=
  decidable_of_iff (∀ i : Fin n, ∀ h : i.val + 1 < n, u ⟨i.val + 1, h⟩ = v i)
    ⟨fun h i hi => h ⟨i, by omega⟩ hi, fun h i hi => h i.val hi⟩

/-- The simplified de Bruijn graph `S(n, k)` (Petyuk `arXiv:2210.14762v2`, §1.2):
simple undirected graph on `(Fin n → Fin k)` obtained from `B(n, k)` by removing orientations,
removing self-loops, and merging parallel edges. -/
def simplifiedDeBruijn (n k : ℕ) : SimpleGraph (Fin n → Fin k) where
  Adj u v := u ≠ v ∧ (DeBruijnArc u v ∨ DeBruijnArc v u)
  symm := ⟨fun _ _ h => ⟨h.1.symm, h.2.symm⟩⟩
  loopless := ⟨fun _ h => h.1 rfl⟩

instance {n k : ℕ} : DecidableRel (simplifiedDeBruijn n k).Adj :=
  fun u v => inferInstanceAs (Decidable (u ≠ v ∧ (DeBruijnArc u v ∨ DeBruijnArc v u)))

/-! ## Section 5: Explicit Proper 3-Coloring of `S(4, 3)` and Refutation of Petyuk Conjecture 1 -/

/-- The `9`-row table `f : Fin 3 → Fin 3 → Fin 3 → Fin 3` from `COUNTEREXAMPLE.md`. -/
def tableF : Fin 3 → Fin 3 → Fin 3 → Fin 3
  | 0, 0, 0 => 1
  | 0, 0, 1 => 2
  | 0, 0, 2 => 2
  | 0, 1, 0 => 0
  | 0, 1, 1 => 0
  | 0, 1, 2 => 0
  | 0, 2, 0 => 1
  | 0, 2, 1 => 1
  | 0, 2, 2 => 1
  | 1, 0, 0 => 1
  | 1, 0, 1 => 2
  | 1, 0, 2 => 1
  | 1, 1, 0 => 1
  | 1, 1, 1 => 1
  | 1, 1, 2 => 1
  | 1, 2, 0 => 2
  | 1, 2, 1 => 1
  | 1, 2, 2 => 2
  | 2, 0, 0 => 2
  | 2, 0, 1 => 0
  | 2, 0, 2 => 2
  | 2, 1, 0 => 2
  | 2, 1, 1 => 2
  | 2, 1, 2 => 2
  | 2, 2, 0 => 0
  | 2, 2, 1 => 2
  | 2, 2, 2 => 0

/-- The `ℤ/3ℤ`-shift-equivariant `3`-coloring of `S(4, 3)`. -/
def s43Color (x : Fin 4 → Fin 3) : Fin 3 :=
  x 0 + tableF (x 1 - x 0) (x 2 - x 1) (x 3 - x 2)

/-- All `80` nonzero difference tuples `(d₁, d₂, d₃, d₄) ∈ (Fin 3)⁴ \ {0}` satisfy
`f(d₁, d₂, d₃) ≠ d₁ + f(d₂, d₃, d₄)` in `Fin 3`. -/
lemma tableF_diff_ne :
    ∀ d₁ d₂ d₃ d₄ : Fin 3,
      (d₁ ≠ 0 ∨ d₂ ≠ 0 ∨ d₃ ≠ 0 ∨ d₄ ≠ 0) →
        tableF d₁ d₂ d₃ ≠ d₁ + tableF d₂ d₃ d₄ := by
  decide

/-- Properness of `s43Color` on every edge of `S(4, 3)`. -/
theorem s43_coloring_proper :
    ∀ u v : Fin 4 → Fin 3, (simplifiedDeBruijn 4 3).Adj u v → s43Color u ≠ s43Color v := by
  have harc : ∀ u v : Fin 4 → Fin 3, u ≠ v → DeBruijnArc u v → s43Color u ≠ s43Color v := by
    intro u v huv ha
    have h0 : u 1 = v 0 := ha 0 (by omega)
    have h1 : u 2 = v 1 := ha 1 (by omega)
    have h2 : u 3 = v 2 := ha 2 (by omega)
    have hnz : u 1 - u 0 ≠ 0 ∨ u 2 - u 1 ≠ 0 ∨ u 3 - u 2 ≠ 0 ∨ v 3 - v 2 ≠ 0 := by
      by_contra hall
      push Not at hall
      rcases hall with ⟨e1, e2, e3, e4⟩
      have hu1 : u 1 = u 0 := sub_eq_zero.mp e1
      have hu2 : u 2 = u 1 := sub_eq_zero.mp e2
      have hu3 : u 3 = u 2 := sub_eq_zero.mp e3
      have hv3 : v 3 = v 2 := sub_eq_zero.mp e4
      apply huv
      funext i
      fin_cases i
      · exact (h0.symm.trans hu1).symm
      · exact (h1.symm.trans hu2).symm
      · exact (h2.symm.trans hu3).symm
      · exact (hv3.trans h2.symm).symm
    have hne := tableF_diff_ne (u 1 - u 0) (u 2 - u 1) (u 3 - u 2) (v 3 - v 2) hnz
    intro heq
    unfold s43Color at heq
    rw [← h0, ← h1, ← h2] at heq
    apply hne
    have hsum : u 0 + tableF (u 1 - u 0) (u 2 - u 1) (u 3 - u 2) =
        u 0 + ((u 1 - u 0) + tableF (u 2 - u 1) (u 3 - u 2) (v 3 - u 3)) := by
      calc
        u 0 + tableF (u 1 - u 0) (u 2 - u 1) (u 3 - u 2)
            = u 1 + tableF (u 2 - u 1) (u 3 - u 2) (v 3 - u 3) := heq
        _ = u 0 + ((u 1 - u 0) + tableF (u 2 - u 1) (u 3 - u 2) (v 3 - u 3)) := by abel
    rw [← h2]
    exact add_left_cancel hsum
  rintro u v ⟨huv, h | h⟩
  · exact harc u v huv h
  · exact (harc v u huv.symm h).symm

/-- `S(4, 3)` contains the triangle `0010–0100–1001` (so `χ(S(4, 3)) = 3`). -/
theorem s43_has_triangle :
    let v₁ : Fin 4 → Fin 3 := ![0, 0, 1, 0]
    let v₂ : Fin 4 → Fin 3 := ![0, 1, 0, 0]
    let v₃ : Fin 4 → Fin 3 := ![1, 0, 0, 1]
    (simplifiedDeBruijn 4 3).Adj v₁ v₂ ∧
    (simplifiedDeBruijn 4 3).Adj v₂ v₃ ∧
    (simplifiedDeBruijn 4 3).Adj v₃ v₁ := by
  decide

/-- **Counterexample Witness:** The simplified de Bruijn graph `S(4, 3)` is word-representable. -/
theorem s43_wordRepresentable : IsWordRepresentable (simplifiedDeBruijn 4 3) :=
  threeColorable_isWordRepresentable (simplifiedDeBruijn 4 3) s43Color s43_coloring_proper

/-- **Refutation of Petyuk's Conjecture 1 (`arXiv:2210.14762v2`, §4):**
It is false that `S(n, k)` is non-word-representable for all `n ≥ 4` and `k ≥ 3`. -/
theorem not_petyuk_conjecture_1 :
    ¬ (∀ n k : ℕ, 4 ≤ n → 3 ≤ k → ¬ IsWordRepresentable (simplifiedDeBruijn n k)) := by
  intro h
  exact h 4 3 (by decide) (by decide) s43_wordRepresentable

#print axioms isAlternating_iff_forall_ne
#print axioms threeColorable_isWordRepresentable
#print axioms s43_coloring_proper
#print axioms s43_has_triangle
#print axioms s43_wordRepresentable
#print axioms not_petyuk_conjecture_1

end OpenMath.Petyuk221014762Conj1
