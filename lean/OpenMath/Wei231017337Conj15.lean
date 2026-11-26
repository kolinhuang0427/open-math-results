import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Copy
import Mathlib.Combinatorics.SimpleGraph.CycleGraph
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Maps
import Mathlib.Data.Fintype.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Data.Rat.Init
import Mathlib.Tactic.NormNum

/-!
# Refutation of Conjecture 1.5 of Wei–Zhang–Zhao (`arXiv:2310.17337v1`)

We formalize the definitions from Section 1 of:
Xiaohua Wei, Gang Zhang, Biao Zhao, *"On the `C_4`-isolation number of a graph"*,
`arXiv:2310.17337v1` (2023):

- Closed neighborhood `N_G[v] = {v} ∪ N_G(v)` and `N_G[D] = ⋃_{v ∈ D} N_G[v]`.
- Induced subgraph `G - N_G[D]`.
- `F`-isolating set: `D ⊆ V(G)` such that `G - N_G[D]` does not contain `F` as a subgraph
  (`¬ (F ⊑ G.induce (closedNeighborhood G D)ᶜ)`).
- `F`-isolation number `ι(G, F)`: cardinality of a smallest `F`-isolating set of `G`.
- Conjecture 1.5 (`\label{conj1.5}`, lines 119–121 of `C_4-isolation.tex`):
  "If `G ≇ C_k` is a connected graph of size `m`, then `ι(G, C_k) ≤ (m + 1) / (k + 2)`."

We refute Conjecture 1.5 at `k = 8` via the 12-vertex, 18-edge truncated tetrahedral graph `G`,
proving `G.Connected`, `¬ Nonempty (G ≃g cycleGraph 8)`, `Nat.card G.edgeSet = 18`, and
`isolationNumber G (cycleGraph 8) = 2 > (18 + 1 : ℚ) / (8 + 2) = 19 / 10`.
-/

namespace OpenMath.Wei231017337Conj15

open SimpleGraph

/-! ## Section 1: Exact Primary-Source Definitions -/

/-- Closed neighborhood `N_G[v] = {v} ∪ N_G(v)` of a vertex `v` in `G`. -/
def closedNeighborSet {V : Type*} (G : SimpleGraph V) (v : V) : Set V :=
  insert v (G.neighborSet v)

/-- Closed neighborhood `N_G[D] = ⋃_{v ∈ D} N_G[v]` of a vertex subset `D` in `G`. -/
def closedNeighborhood {V : Type*} (G : SimpleGraph V) (D : Set V) : Set V :=
  ⋃ v ∈ D, closedNeighborSet G v

/-- `D ⊆ V(G)` is an `F`-isolating set of `G` if `G - N_G[D]` does not contain `F` as a subgraph
(Section 1, line 76 of `C_4-isolation.tex`). -/
def IsIsolatingSet {V W : Type*} (G : SimpleGraph V) (F : SimpleGraph W) (D : Finset V) : Prop :=
  ¬ (F ⊑ G.induce (closedNeighborhood G (D : Set V))ᶜ)

/-- The `F`-isolation number `ι(G, F)` is the cardinality of a smallest `F`-isolating set of `G`
(Section 1, line 76 of `C_4-isolation.tex`). -/
noncomputable def isolationNumber {V W : Type*} (G : SimpleGraph V) (F : SimpleGraph W) : ℕ :=
  sInf {d : ℕ | ∃ D : Finset V, IsIsolatingSet G F D ∧ D.card = d}

/-! ## Section 2: The Truncated Tetrahedral Graph on `Fin 12` -/

/-- The 6 matching edges between the four triangles `T_0 = {0,1,2}`, `T_1 = {3,4,5}`,
`T_2 = {6,7,8}`, `T_3 = {9,10,11}`: `{0,3}, {1,6}, {2,9}, {4,7}, {5,10}, {8,11}`. -/
def matchPartner : Fin 12 → Fin 12
  | 0 => 3
  | 1 => 6
  | 2 => 9
  | 3 => 0
  | 4 => 7
  | 5 => 10
  | 6 => 1
  | 7 => 4
  | 8 => 11
  | 9 => 2
  | 10 => 5
  | 11 => 8

/-- The 12-vertex, 18-edge 3-regular truncated tetrahedral graph. -/
def truncatedTetrahedron : SimpleGraph (Fin 12) where
  Adj u v := u ≠ v ∧ (u.val / 3 = v.val / 3 ∨ matchPartner u = v)
  symm := ⟨by decide⟩
  loopless := ⟨by decide⟩

instance : DecidableRel truncatedTetrahedron.Adj :=
  fun u v => inferInstanceAs (Decidable (u ≠ v ∧ (u.val / 3 = v.val / 3 ∨ matchPartner u = v)))

/-- `truncatedTetrahedron` is connected (every vertex is at distance ≤ 3 from `0`). -/
theorem truncatedTetrahedron_connected : truncatedTetrahedron.Connected := by
  have r1 : ∀ {a b : Fin 12}, truncatedTetrahedron.Adj a b → truncatedTetrahedron.Reachable a b :=
    fun h => h.reachable
  have r2 : ∀ {a b c : Fin 12}, truncatedTetrahedron.Adj a b → truncatedTetrahedron.Adj b c →
      truncatedTetrahedron.Reachable a c :=
    fun h1 h2 => h1.reachable.trans h2.reachable
  have r3 : ∀ {a b c d : Fin 12}, truncatedTetrahedron.Adj a b → truncatedTetrahedron.Adj b c →
      truncatedTetrahedron.Adj c d → truncatedTetrahedron.Reachable a d :=
    fun h1 h2 h3 => (h1.reachable.trans h2.reachable).trans h3.reachable
  rw [SimpleGraph.connected_iff_exists_forall_reachable]
  refine ⟨0, fun v => ?_⟩
  match v with
  | 0 => exact Reachable.rfl
  | 1 => exact r1 (by decide)
  | 2 => exact r1 (by decide)
  | 3 => exact r1 (by decide)
  | 4 => exact r2 (b := 3) (by decide) (by decide)
  | 5 => exact r2 (b := 3) (by decide) (by decide)
  | 6 => exact r2 (b := 1) (by decide) (by decide)
  | 7 => exact r3 (b := 1) (c := 6) (by decide) (by decide) (by decide)
  | 8 => exact r3 (b := 1) (c := 6) (by decide) (by decide) (by decide)
  | 9 => exact r2 (b := 2) (by decide) (by decide)
  | 10 => exact r3 (b := 2) (c := 9) (by decide) (by decide) (by decide)
  | 11 => exact r3 (b := 2) (c := 9) (by decide) (by decide) (by decide)

/-- `truncatedTetrahedron` has size `m = 18` edges. -/
theorem truncatedTetrahedron_edgeFinset_card :
    truncatedTetrahedron.edgeFinset.card = 18 := by
  decide

theorem truncatedTetrahedron_edgeSet_card :
    Nat.card truncatedTetrahedron.edgeSet = 18 := by
  rw [Nat.card_eq_fintype_card, ← SimpleGraph.edgeFinset_card]
  exact truncatedTetrahedron_edgeFinset_card

/-- `truncatedTetrahedron` is not isomorphic to `C_8` (12 vertices ≠ 8 vertices). -/
theorem truncatedTetrahedron_not_iso_c8 :
    ¬ Nonempty (truncatedTetrahedron ≃g cycleGraph 8) := by
  rintro ⟨e⟩
  have hcard : Fintype.card (Fin 12) = Fintype.card (Fin 8) :=
    Fintype.card_congr e.toEquiv
  simp at hcard

/-! ## Section 3: Exact Computation of `ι(truncatedTetrahedron, C_8) = 2` -/

/-- Explicit 8-cycle inside `truncatedTetrahedron - N_G[v]` for each `v : Fin 12`. -/
def avoidCycle (v : Fin 12) (i : Fin 8) : Fin 12 :=
  match v, i with
  | 0, 0 => 4  | 0, 1 => 5  | 0, 2 => 10 | 0, 3 => 9  | 0, 4 => 11 | 0, 5 => 8  | 0, 6 => 6  | 0, 7 => 7
  | 1, 0 => 7  | 1, 1 => 8  | 1, 2 => 11 | 1, 3 => 9  | 1, 4 => 10 | 1, 5 => 5  | 1, 6 => 3  | 1, 7 => 4
  | 2, 0 => 10 | 2, 1 => 11 | 2, 2 => 8  | 2, 3 => 6  | 2, 4 => 7  | 2, 5 => 4  | 2, 6 => 3  | 2, 7 => 5
  | 3, 0 => 1  | 3, 1 => 2  | 3, 2 => 9  | 3, 3 => 10 | 3, 4 => 11 | 3, 5 => 8  | 3, 6 => 7  | 3, 7 => 6
  | 4, 0 => 6  | 4, 1 => 8  | 4, 2 => 11 | 4, 3 => 10 | 4, 4 => 9  | 4, 5 => 2  | 4, 6 => 0  | 4, 7 => 1
  | 5, 0 => 9  | 5, 1 => 11 | 5, 2 => 8  | 5, 3 => 7  | 5, 4 => 6  | 5, 5 => 1  | 5, 6 => 0  | 5, 7 => 2
  | 6, 0 => 0  | 6, 1 => 2  | 6, 2 => 9  | 6, 3 => 11 | 6, 4 => 10 | 6, 5 => 5  | 6, 6 => 4  | 6, 7 => 3
  | 7, 0 => 3  | 7, 1 => 5  | 7, 2 => 10 | 7, 3 => 11 | 7, 4 => 9  | 7, 5 => 2  | 7, 6 => 1  | 7, 7 => 0
  | 8, 0 => 9  | 8, 1 => 10 | 8, 2 => 5  | 8, 3 => 4  | 8, 4 => 3  | 8, 5 => 0  | 8, 6 => 1  | 8, 7 => 2
  | 9, 0 => 0  | 9, 1 => 1  | 9, 2 => 6  | 9, 3 => 8  | 9, 4 => 7  | 9, 5 => 4  | 9, 6 => 5  | 9, 7 => 3
  | 10, 0 => 3 | 10, 1 => 4 | 10, 2 => 7 | 10, 3 => 8 | 10, 4 => 6 | 10, 5 => 1 | 10, 6 => 2 | 10, 7 => 0
  | 11, 0 => 6 | 11, 1 => 7 | 11, 2 => 4 | 11, 3 => 5 | 11, 4 => 3 | 11, 5 => 0 | 11, 6 => 2 | 11, 7 => 1

private lemma avoidCycle_injective :
    ∀ v : Fin 12, ∀ i j : Fin 8, avoidCycle v i = avoidCycle v j → i = j := by
  decide

private lemma avoidCycle_avoids :
    ∀ v : Fin 12, ∀ i : Fin 8,
      avoidCycle v i ≠ v ∧ ¬ truncatedTetrahedron.Adj v (avoidCycle v i) := by
  decide

private lemma avoidCycle_adj :
    ∀ v : Fin 12, ∀ i j : Fin 8,
      (cycleGraph 8).Adj i j → truncatedTetrahedron.Adj (avoidCycle v i) (avoidCycle v j) := by
  decide

/-- No vertex subset `D` of size `≤ 1` is a `C_8`-isolating set of `truncatedTetrahedron`. -/
lemma not_isIsolatingSet_of_card_le_one (D : Finset (Fin 12)) (hcard : D.card ≤ 1) :
    ¬ IsIsolatingSet truncatedTetrahedron (cycleGraph 8) D := by
  intro hiso
  have hex : ∃ v : Fin 12, ∀ u ∈ D, u = v := by
    rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hcard with h0 | h1
    · refine ⟨0, fun u hu => ?_⟩
      rw [Finset.card_eq_zero.mp h0] at hu
      simp at hu
    · obtain ⟨v, rfl⟩ := Finset.card_eq_one.mp h1
      exact ⟨v, fun u hu => Finset.mem_singleton.mp hu⟩
  obtain ⟨v, hv⟩ := hex
  have hmem : ∀ i : Fin 8, avoidCycle v i ∈ (closedNeighborhood truncatedTetrahedron (D : Set (Fin 12)))ᶜ := by
    intro i hbad
    simp only [closedNeighborhood, closedNeighborSet, Set.mem_iUnion, Set.mem_insert_iff,
      SimpleGraph.mem_neighborSet, Finset.mem_coe] at hbad
    obtain ⟨u, huD, h⟩ := hbad
    have huv : u = v := hv u huD
    subst huv
    rcases h with heq | hadj
    · exact (avoidCycle_avoids u i).1 heq
    · exact (avoidCycle_avoids u i).2 hadj
  let hom : cycleGraph 8 →g
      truncatedTetrahedron.induce (closedNeighborhood truncatedTetrahedron (D : Set (Fin 12)))ᶜ :=
    { toFun := fun i => ⟨avoidCycle v i, hmem i⟩
      map_rel' := fun hadj => avoidCycle_adj v _ _ hadj }
  have hinj : Function.Injective hom := by
    intro i j hij
    exact avoidCycle_injective v i j (congrArg Subtype.val hij)
  exact hiso ⟨hom.toCopy hinj⟩

/-- `{0, 4}` is a `C_8`-isolating set of `truncatedTetrahedron` because `|V \ N_G[{0, 4}]| = 5 < 8`. -/
lemma isIsolatingSet_pair :
    IsIsolatingSet truncatedTetrahedron (cycleGraph 8) ({0, 4} : Finset (Fin 12)) := by
  rintro ⟨c⟩
  let rem : Finset (Fin 12) := {6, 8, 9, 10, 11}
  have hrem_card : rem.card = 5 := by decide
  have hcover : ∀ u : Fin 12,
      u ∈ rem ∨
      (u = 0 ∨ truncatedTetrahedron.Adj 0 u) ∨
      (u = 4 ∨ truncatedTetrahedron.Adj 4 u) := by
    decide
  have hmaps : Set.MapsTo (fun i : Fin 8 => (c i).val) (Finset.univ : Finset (Fin 8)) rem := by
    intro i _
    have hnot : (c i).val ∉ closedNeighborhood truncatedTetrahedron (({0, 4} : Finset (Fin 12)) : Set (Fin 12)) :=
      (c i).property
    rcases hcover (c i).val with hmem | h0 | h4
    · exact hmem
    · exfalso; apply hnot
      simp only [closedNeighborhood, closedNeighborSet, Set.mem_iUnion, Set.mem_insert_iff,
        SimpleGraph.mem_neighborSet, Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton]
      exact ⟨0, Or.inl rfl, h0⟩
    · exfalso; apply hnot
      simp only [closedNeighborhood, closedNeighborSet, Set.mem_iUnion, Set.mem_insert_iff,
        SimpleGraph.mem_neighborSet, Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton]
      exact ⟨4, Or.inr rfl, h4⟩
  have hinj : Set.InjOn (fun i : Fin 8 => (c i).val) (Finset.univ : Finset (Fin 8)) := by
    intro i _ j _ hij
    exact c.injective (Subtype.ext hij)
  have hle : (Finset.univ : Finset (Fin 8)).card ≤ rem.card :=
    Finset.card_le_card_of_injOn (fun i => (c i).val) hmaps hinj
  rw [Finset.card_univ, Fintype.card_fin, hrem_card] at hle
  omega

/-- Exact `C_8`-isolation number: `ι(truncatedTetrahedron, C_8) = 2`. -/
theorem truncatedTetrahedron_isolationNumber_c8 :
    isolationNumber truncatedTetrahedron (cycleGraph 8) = 2 := by
  unfold isolationNumber
  have h2mem : 2 ∈ {d : ℕ | ∃ D : Finset (Fin 12),
      IsIsolatingSet truncatedTetrahedron (cycleGraph 8) D ∧ D.card = d} :=
    ⟨{0, 4}, isIsolatingSet_pair, by decide⟩
  apply le_antisymm
  · exact Nat.sInf_le h2mem
  · refine le_csInf ⟨2, h2mem⟩ ?_
    rintro d ⟨D, hiso, rfl⟩
    by_contra hlt
    exact not_isIsolatingSet_of_card_le_one D (by omega) hiso

/-! ## Section 4: Refutation of Conjecture 1.5 of `arXiv:2310.17337v1` -/

/-- Main witness theorem: the truncated tetrahedral graph `G` is connected, non-isomorphic to `C_8`,
has size `m = 18`, and satisfies `ι(G, C_8) = 2 > (18 + 1) / (8 + 2) = 19 / 10`. -/
theorem refutes_wei_conjecture_1_5_witness :
    truncatedTetrahedron.Connected ∧
    ¬ Nonempty (truncatedTetrahedron ≃g cycleGraph 8) ∧
    Nat.card truncatedTetrahedron.edgeSet = 18 ∧
    isolationNumber truncatedTetrahedron (cycleGraph 8) = 2 ∧
    ((Nat.card truncatedTetrahedron.edgeSet : ℚ) + 1) / ((8 : ℚ) + 2) <
      (isolationNumber truncatedTetrahedron (cycleGraph 8) : ℚ) := by
  refine ⟨truncatedTetrahedron_connected,
          truncatedTetrahedron_not_iso_c8,
          truncatedTetrahedron_edgeSet_card,
          truncatedTetrahedron_isolationNumber_c8,
          ?_⟩
  rw [truncatedTetrahedron_edgeSet_card, truncatedTetrahedron_isolationNumber_c8]
  norm_num

/-- Direct negation of the universal statement of Conjecture 1.5 of `arXiv:2310.17337v1`. -/
theorem not_wei_conjecture_1_5 :
    ¬ (∀ (k : ℕ), 3 ≤ k → ∀ (n : ℕ) (G : SimpleGraph (Fin n)),
      G.Connected → ¬ Nonempty (G ≃g cycleGraph k) →
      (isolationNumber G (cycleGraph k) : ℚ) ≤
        ((Nat.card G.edgeSet : ℚ) + 1) / ((k : ℚ) + 2)) := by
  intro hconj
  have hle := hconj 8 (by omega) 12 truncatedTetrahedron
    truncatedTetrahedron_connected truncatedTetrahedron_not_iso_c8
  rw [truncatedTetrahedron_edgeSet_card, truncatedTetrahedron_isolationNumber_c8] at hle
  norm_num at hle

#print axioms refutes_wei_conjecture_1_5_witness
#print axioms not_wei_conjecture_1_5

end OpenMath.Wei231017337Conj15
