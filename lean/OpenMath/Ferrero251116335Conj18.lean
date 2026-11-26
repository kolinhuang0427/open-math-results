import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.CycleGraph
import Mathlib.Combinatorics.SimpleGraph.Maps
import Mathlib.Data.Fintype.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Data.Set.Finite.Basic

/-!
# Refutation of Conjecture 1.8 of Ferrero–Hall–Hogben–Hunnell–Small (`arXiv:2511.16335v1`)

We formalize the definitions from Section 1 of:
Daniela Ferrero, H. Tracy Hall, Leslie Hogben, Mark Hunnell, Ben Small,
*"Zero forcing propagation time intervals and graphs with fixed propagation time"*,
`arXiv:2511.16335v1` (2025):

- Color change rule CCR-`Z` (standard zero forcing), rounds `B^{[i]}` and `B^{(i)}`,
  standard zero forcing sets, minimal forcing sets, propagation time `pt(G, B)`,
  and upper/lower standard propagation times `PT̄(G)`, `PT_(G)` (Definition 1.2).
- Disjoint union, graph join, and *standard fast join* (Definition 1.5).
- Conjecture 1.8 (`\label{c:std}`): "Let `G` be a connected graph. If `PT̄(G) = 1`,
  then `G` is a standard fast join."

We refute Conjecture 1.8 for the entire infinite family of lexicographic blowups
`C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`), and specialize to the explicit 12-vertex
witness `C_6[2K_1] ≅ Circ(12, {1, 5})`.
-/

namespace OpenMath.Ferrero251116335Conj18

open SimpleGraph

/-! ## Section 1: Exact Primary-Source Definitions -/

/-- One simultaneous round of standard zero forcing (CCR-`Z`): a vertex `w` is forced given
currently blue set `S` iff some blue vertex `u ∈ S` has `w` as its unique white neighbor. -/
def forceStep {V : Type*} (G : SimpleGraph V) (S : Set V) : Set V :=
  {w | ∃ u ∈ S, {w' | G.Adj u w' ∧ w' ∉ S} = {w}}

/-- `B^{[i]}`: the set of vertices that are blue after round `i` of standard zero forcing. -/
def roundBlue {V : Type*} (G : SimpleGraph V) (B : Set V) : ℕ → Set V
  | 0 => B
  | i + 1 => roundBlue G B i ∪ forceStep G (roundBlue G B i)

/-- `B^{(i)}`: the set of vertices forced in round `i` (`B^{(0)} = B`). -/
def roundNew {V : Type*} (G : SimpleGraph V) (B : Set V) : ℕ → Set V
  | 0 => B
  | i + 1 => forceStep G (roundBlue G B i)

/-- The propagation time `pt(G, B)` for a forcing set `B`: the greatest integer `p` such that
`B^{(p)} ≠ ∅` (Section 1, lines 321 & 326 of `NewFixedPropTime.tex`). -/
noncomputable def propTime {V : Type*} (G : SimpleGraph V) (B : Set V) : ℕ :=
  sSup {p : ℕ | (roundNew G B p).Nonempty}

/-- `B` is a standard zero forcing set of `G`: letting `p` be the greatest integer such that
`B^{(p)} ≠ ∅`, we have `B^{[p]} = V(G)` (Section 1, line 321). -/
def IsZeroForcingSet {V : Type*} (G : SimpleGraph V) (B : Set V) : Prop :=
  roundBlue G B (propTime G B) = Set.univ

/-- `B` is a minimal standard zero forcing set of `G` (Section 1, line 323). -/
def IsMinimalZeroForcingSet {V : Type*} (G : SimpleGraph V) (B : Set V) : Prop :=
  IsZeroForcingSet G B ∧ ∀ B', B' ⊂ B → ¬ IsZeroForcingSet G B'

/-- The upper standard propagation time `PT̄(G)` (Definition 1.2): maximum propagation time
over all minimal standard zero forcing sets of `G`. -/
noncomputable def upperPropTime {V : Type*} (G : SimpleGraph V) : ℕ :=
  sSup {p : ℕ | ∃ B, IsMinimalZeroForcingSet G B ∧ propTime G B = p}

/-- The lower standard propagation time `PT_(G)` (Definition 1.2): minimum propagation time
over all minimal standard zero forcing sets of `G`. -/
noncomputable def lowerPropTime {V : Type*} (G : SimpleGraph V) : ℕ :=
  sInf {p : ℕ | ∃ B, IsMinimalZeroForcingSet G B ∧ propTime G B = p}

/-- Disjoint union `G₁ ⊔ G₂` of two vertex-disjoint graphs on `V₁ ⊕ V₂`. -/
def disjointUnion {V₁ V₂ : Type*} (G₁ : SimpleGraph V₁) (G₂ : SimpleGraph V₂) :
    SimpleGraph (V₁ ⊕ V₂) where
  Adj
    | Sum.inl u, Sum.inl v => G₁.Adj u v
    | Sum.inr u, Sum.inr v => G₂.Adj u v
    | _, _ => False
  symm := ⟨by
    rintro (u | u) (v | v) h
    · exact G₁.symm.symm u v h
    · exact h
    · exact h
    · exact G₂.symm.symm u v h⟩
  loopless := ⟨by
    rintro (u | u) h
    · exact G₁.loopless.irrefl u h
    · exact G₂.loopless.irrefl u h⟩

/-- Graph join `⋁_{i} H i` of a family of graphs on `Σ i, W i`. -/
def graphJoin {ι : Type*} (W : ι → Type*) (H : ∀ i, SimpleGraph (W i)) :
    SimpleGraph (Σ i, W i) where
  Adj x y := x.1 ≠ y.1 ∨ ∃ h : x.1 = y.1, (H y.1).Adj (h ▸ x.2) y.2
  symm := ⟨by
    rintro ⟨i, u⟩ ⟨j, v⟩ (hne | ⟨h, hadj⟩)
    · exact Or.inl hne.symm
    · dsimp only at h hadj
      subst h
      exact Or.inr ⟨rfl, (H i).symm.symm u v hadj⟩⟩
  loopless := ⟨by
    rintro ⟨i, u⟩ (hne | ⟨_, hadj⟩)
    · exact hne rfl
    · exact (H i).loopless.irrefl u hadj⟩

/-- A factor `G_i` allowed in a standard fast join (Definition 1.5):
either `n_i K₁` (`n_i ≥ 1`) or `K_{n_i} ⊔ K_{m_i}` (`n_i, m_i ≥ 2`). -/
inductive FastJoinFactor where
  | edgeless (n : ℕ) (hn : 1 ≤ n)
  | twoCliques (n m : ℕ) (hn : 2 ≤ n) (hm : 2 ≤ m)

def FastJoinFactor.Vertex : FastJoinFactor → Type
  | .edgeless n _ => Fin n
  | .twoCliques n m _ _ => Fin n ⊕ Fin m

def FastJoinFactor.graph : (f : FastJoinFactor) → SimpleGraph f.Vertex
  | .edgeless _ _ => ⊥
  | .twoCliques _ _ _ _ => disjointUnion ⊤ ⊤

lemma FastJoinFactor.nonempty_vertex (f : FastJoinFactor) : Nonempty f.Vertex := by
  cases f with
  | edgeless n hn => exact ⟨⟨0, by omega⟩⟩
  | twoCliques n m hn _ => exact ⟨Sum.inl ⟨0, by omega⟩⟩

/-- Definition 1.5 of `arXiv:2511.16335v1`:
A graph `G` of order `n ≥ 2` is a *standard fast join* if `G ≅ K_n` or
`G ≅ ⋁_{i=1}^t G_i` where `t ≥ 2` and each `G_i` is `n_i K₁` (`n_i ≥ 1`) or
`K_{n_i} ⊔ K_{m_i}` (`n_i, m_i ≥ 2`). -/
def IsStandardFastJoin {V : Type*} [Fintype V] (G : SimpleGraph V) : Prop :=
  2 ≤ Fintype.card V ∧
    (Nonempty (G ≃g (⊤ : SimpleGraph (Fin (Fintype.card V)))) ∨
      ∃ (t : ℕ) (_ : 2 ≤ t) (factors : Fin t → FastJoinFactor),
        Nonempty (G ≃g graphJoin (fun i => (factors i).Vertex) (fun i => (factors i).graph)))

/-! ## Section 2: General Lemmas on Zero Forcing, Complements, and Standard Fast Joins -/

section GeneralLemmas

variable {V W : Type*}

lemma forceStep_subset_compl (G : SimpleGraph V) (S : Set V) :
    forceStep G S ⊆ Sᶜ := by
  intro w ⟨u, _, huniq⟩
  have hw : w ∈ {w' | G.Adj u w' ∧ w' ∉ S} := by rw [huniq]; exact Set.mem_singleton w
  exact hw.2

lemma forceStep_univ (G : SimpleGraph V) : forceStep G Set.univ = ∅ := by
  ext w
  simp only [Set.mem_empty_iff_false, iff_false]
  intro hw
  exact forceStep_subset_compl G Set.univ hw trivial

lemma roundBlue_subset_succ (G : SimpleGraph V) (B : Set V) (i : ℕ) :
    roundBlue G B i ⊆ roundBlue G B (i + 1) :=
  Set.subset_union_left

lemma roundBlue_mono (G : SimpleGraph V) (B : Set V) {i j : ℕ} (h : i ≤ j) :
    roundBlue G B i ⊆ roundBlue G B j := by
  induction h with
  | refl => exact Set.Subset.rfl
  | step _ ih => exact ih.trans (roundBlue_subset_succ G B _)

lemma roundBlue_eq_univ_of_le (G : SimpleGraph V) (B : Set V) {i j : ℕ}
    (h : i ≤ j) (hi : roundBlue G B i = Set.univ) : roundBlue G B j = Set.univ :=
  Set.eq_univ_of_univ_subset (hi ▸ roundBlue_mono G B h)

lemma roundNew_eq_empty_of_roundBlue_univ (G : SimpleGraph V) (B : Set V) {i j : ℕ}
    (h : i < j) (hi : roundBlue G B i = Set.univ) : roundNew G B j = ∅ := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  have hk : roundBlue G B (i + k) = Set.univ :=
    roundBlue_eq_univ_of_le G B (Nat.le_add_right i k) hi
  rw [Nat.succ_add]
  change forceStep G (roundBlue G B (i + k)) = ∅
  rw [hk, forceStep_univ]

lemma propTime_eq_one_of_roundBlue_one_eq_univ (G : SimpleGraph V) (B : Set V)
    (h1 : roundBlue G B 1 = Set.univ) (hne : B ≠ Set.univ) :
    propTime G B = 1 := by
  have h1_nonempty : (roundNew G B 1).Nonempty := by
    by_contra hemp
    rw [Set.not_nonempty_iff_eq_empty] at hemp
    have : roundBlue G B 1 = B := by
      change B ∪ roundNew G B 1 = B
      rw [hemp, Set.union_empty]
    exact hne (this ▸ h1)
  have hle : ∀ p ∈ {p : ℕ | (roundNew G B p).Nonempty}, p ≤ 1 := by
    intro p hp
    by_contra hgt
    have h1lt : 1 < p := by omega
    have hemp := roundNew_eq_empty_of_roundBlue_univ G B h1lt h1
    change (roundNew G B p).Nonempty at hp
    rw [hemp] at hp
    exact Set.not_nonempty_empty hp
  unfold propTime
  apply le_antisymm
  · exact csSup_le ⟨1, h1_nonempty⟩ hle
  · exact le_csSup ⟨1, fun p hp => hle p hp⟩ h1_nonempty

lemma isZeroForcingSet_of_roundBlue_one_eq_univ (G : SimpleGraph V) (B : Set V)
    (h1 : roundBlue G B 1 = Set.univ) : IsZeroForcingSet G B := by
  by_cases hne : B = Set.univ
  · have h0 : ∀ p ∈ {p : ℕ | (roundNew G B p).Nonempty}, p ≤ 0 := by
      intro p hp
      cases p with
      | zero => exact le_rfl
      | succ k =>
        have hemp := roundNew_eq_empty_of_roundBlue_univ G B (Nat.zero_lt_succ k) hne
        change (roundNew G B (k + 1)).Nonempty at hp
        rw [hemp] at hp
        exact (Set.not_nonempty_empty hp).elim
    have hpt : propTime G B = 0 := by
      unfold propTime
      by_cases hE : ({p : ℕ | (roundNew G B p).Nonempty}).Nonempty
      · exact Nat.le_zero.mp (csSup_le hE h0)
      · rw [Set.not_nonempty_iff_eq_empty.mp hE, csSup_empty]; rfl
    unfold IsZeroForcingSet
    rw [hpt]
    exact hne
  · unfold IsZeroForcingSet
    rw [propTime_eq_one_of_roundBlue_one_eq_univ G B h1 hne]
    exact h1

/-- Graph isomorphism induces an isomorphism of complements. -/
def isoCompl {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) : Gᶜ ≃g Hᶜ where
  toEquiv := e.toEquiv
  map_rel_iff' := by
    intro a b
    simp [SimpleGraph.compl_adj, e.map_rel_iff]

/-- In the complement of a graph join, every walk stays within a single join part. -/
lemma walk_compl_graphJoin_fst_eq {ι : Type*} {U : ι → Type*} {H : ∀ i, SimpleGraph (U i)}
    {x y : Σ i, U i} (p : (graphJoin U H)ᶜ.Walk x y) : x.1 = y.1 := by
  induction p with
  | nil => rfl
  | @cons u v w hadj _ ih =>
    have huv : u.1 = v.1 := by
      by_contra hne
      exact hadj.2 (Or.inl hne)
    exact huv.trans ih

/-- A join of `t ≥ 2` nonempty graphs cannot have a connected complement. -/
lemma not_connected_compl_graphJoin {t : ℕ} (ht : 2 ≤ t)
    (U : Fin t → Type*) (hU : ∀ i, Nonempty (U i)) (H : ∀ i, SimpleGraph (U i)) :
    ¬ (graphJoin U H)ᶜ.Connected := by
  intro hconn
  let i₀ : Fin t := ⟨0, by omega⟩
  let i₁ : Fin t := ⟨1, by omega⟩
  obtain ⟨u₀⟩ := hU i₀
  obtain ⟨u₁⟩ := hU i₁
  obtain ⟨w⟩ := hconn ⟨i₀, u₀⟩ ⟨i₁, u₁⟩
  have heq : i₀ = i₁ := walk_compl_graphJoin_fst_eq w
  have : (0 : ℕ) = 1 := congrArg Fin.val heq
  omega

/-- Any non-complete graph with a connected complement is not a standard fast join. -/
lemma not_isStandardFastJoin_of_not_top_of_compl_connected [Fintype V]
    (G : SimpleGraph V) (hnotTop : ∃ u v : V, u ≠ v ∧ ¬ G.Adj u v)
    (hcompl : Gᶜ.Connected) : ¬ IsStandardFastJoin G := by
  intro hsfj
  rcases hsfj.2 with hK | ⟨t, ht, factors, ⟨e⟩⟩
  · obtain ⟨e⟩ := hK
    obtain ⟨u, v, huv, hnadj⟩ := hnotTop
    have hene : e u ≠ e v := e.injective.ne huv
    have hadjTop : (⊤ : SimpleGraph (Fin (Fintype.card V))).Adj (e u) (e v) := hene
    exact hnadj ((e.map_rel_iff).mp hadjTop)
  · have hconnJoin : (graphJoin (fun i => (factors i).Vertex)
        (fun i => (factors i).graph))ᶜ.Connected :=
      (isoCompl e).connected_iff.mp hcompl
    exact not_connected_compl_graphJoin ht
      (fun i => (factors i).Vertex)
      (fun i => (factors i).nonempty_vertex)
      (fun i => (factors i).graph)
      hconnJoin

/-! ### Isomorphism invariance of zero forcing and `IsStandardFastJoin` -/

lemma forceStep_image {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) (S : Set V) :
    forceStep H (e '' S) = e '' forceStep G S := by
  ext y
  constructor
  · rintro ⟨u', ⟨u, huS, rfl⟩, huniq⟩
    refine ⟨e.symm y, ⟨u, huS, ?_⟩, e.apply_symm_apply y⟩
    ext w'
    constructor
    · intro ⟨hadj, hw'⟩
      have hmem : e w' ∈ {z | H.Adj (e u) z ∧ z ∉ e '' S} :=
        ⟨(e.map_rel_iff).mpr hadj, fun ⟨v, hvS, hveq⟩ => hw' (e.injective hveq ▸ hvS)⟩
      rw [huniq] at hmem
      change w' = e.symm y
      rw [← e.symm_apply_apply w', hmem]
    · rintro rfl
      have hy : y ∈ {z | H.Adj (e u) z ∧ z ∉ e '' S} := by
        rw [huniq]; exact Set.mem_singleton y
      refine ⟨?_, ?_⟩
      · exact (e.map_rel_iff).mp (by simpa using hy.1)
      · intro hmem
        exact hy.2 ⟨e.symm y, hmem, e.apply_symm_apply y⟩
  · rintro ⟨w, ⟨u, huS, huniq⟩, rfl⟩
    refine ⟨e u, ⟨u, huS, rfl⟩, ?_⟩
    ext z
    constructor
    · intro ⟨hadj, hz⟩
      have hmem : e.symm z ∈ {w' | G.Adj u w' ∧ w' ∉ S} := by
        refine ⟨(e.map_rel_iff).mp (by simpa using hadj), ?_⟩
        intro hmem
        exact hz ⟨e.symm z, hmem, e.apply_symm_apply z⟩
      rw [huniq] at hmem
      change z = e w
      rw [← e.apply_symm_apply z, hmem]
    · rintro rfl
      have hw : w ∈ {w' | G.Adj u w' ∧ w' ∉ S} := by
        rw [huniq]; exact Set.mem_singleton w
      exact ⟨(e.map_rel_iff).mpr hw.1, fun ⟨v, hvS, hveq⟩ => hw.2 (e.injective hveq ▸ hvS)⟩

lemma roundBlue_image {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) (B : Set V) (i : ℕ) :
    roundBlue H (e '' B) i = e '' roundBlue G B i := by
  induction i with
  | zero => rfl
  | succ i ih =>
    simp only [roundBlue, ih, forceStep_image, Set.image_union]

lemma roundNew_image {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) (B : Set V) (i : ℕ) :
    roundNew H (e '' B) i = e '' roundNew G B i := by
  cases i with
  | zero => rfl
  | succ i =>
    simp only [roundNew, roundBlue_image, forceStep_image]

lemma propTime_image {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) (B : Set V) :
    propTime H (e '' B) = propTime G B := by
  unfold propTime
  congr 1
  ext p
  simp [roundNew_image]

lemma isZeroForcingSet_image_iff {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) (B : Set V) :
    IsZeroForcingSet H (e '' B) ↔ IsZeroForcingSet G B := by
  unfold IsZeroForcingSet
  rw [propTime_image, roundBlue_image]
  constructor
  · intro h
    ext v
    simp only [Set.mem_univ, iff_true]
    have : e v ∈ e '' roundBlue G B (propTime G B) := h ▸ Set.mem_univ (e v)
    obtain ⟨u, hu, huv⟩ := this
    exact e.injective huv ▸ hu
  · intro h
    rw [h, Set.image_univ, e.surjective.range_eq]

lemma isMinimalZeroForcingSet_image_iff {G : SimpleGraph V} {H : SimpleGraph W}
    (e : G ≃g H) (B : Set V) :
    IsMinimalZeroForcingSet H (e '' B) ↔ IsMinimalZeroForcingSet G B := by
  constructor
  · rintro ⟨hzfs, hmin⟩
    refine ⟨(isZeroForcingSet_image_iff e B).mp hzfs, ?_⟩
    intro B' hss hzfs'
    have hssImg : e '' B' ⊂ e '' B := by
      refine ⟨Set.image_mono hss.1, fun hsub => hss.2 ?_⟩
      intro x hx
      obtain ⟨y, hy, hyx⟩ := hsub ⟨x, hx, rfl⟩
      exact e.injective hyx ▸ hy
    exact hmin (e '' B') hssImg ((isZeroForcingSet_image_iff e B').mpr hzfs')
  · rintro ⟨hzfs, hmin⟩
    refine ⟨(isZeroForcingSet_image_iff e B).mpr hzfs, ?_⟩
    intro C hss hzfsC
    have hCeq : e '' (e.symm '' C) = C := by
      ext y
      simp only [Set.mem_image]
      constructor
      · rintro ⟨_, ⟨z, hz, rfl⟩, rfl⟩; simpa using hz
      · intro hy; exact ⟨e.symm y, ⟨y, hy, rfl⟩, e.apply_symm_apply y⟩
    have hss' : e.symm '' C ⊂ B := by
      have hsub : e.symm '' C ⊆ B := by
        rintro _ ⟨y, hyC, rfl⟩
        obtain ⟨u, huB, rfl⟩ := hss.1 hyC
        simpa using huB
      refine ⟨hsub, fun hBsub => hss.2 ?_⟩
      intro y hy
      obtain ⟨u, huB, rfl⟩ := hy
      have : u ∈ e.symm '' C := hBsub huB
      obtain ⟨z, hzC, hzeq⟩ := this
      have : e u = z := by rw [← hzeq, e.apply_symm_apply]
      exact this ▸ hzC
    have hzfs' : IsZeroForcingSet G (e.symm '' C) :=
      (isZeroForcingSet_image_iff e (e.symm '' C)).mp (hCeq.symm ▸ hzfsC)
    exact hmin (e.symm '' C) hss' hzfs'

lemma upperPropTime_congr {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) :
    upperPropTime G = upperPropTime H := by
  unfold upperPropTime
  congr 1
  ext p
  constructor
  · rintro ⟨B, hmin, rfl⟩
    exact ⟨e '' B, (isMinimalZeroForcingSet_image_iff e B).mpr hmin, propTime_image e B⟩
  · rintro ⟨C, hmin, rfl⟩
    have hCeq : e '' (e.symm '' C) = C := by
      ext y
      simp only [Set.mem_image]
      constructor
      · rintro ⟨_, ⟨z, hz, rfl⟩, rfl⟩; simpa using hz
      · intro hy; exact ⟨e.symm y, ⟨y, hy, rfl⟩, e.apply_symm_apply y⟩
    refine ⟨e.symm '' C, (isMinimalZeroForcingSet_image_iff e (e.symm '' C)).mp (hCeq.symm ▸ hmin),
      ?_⟩
    rw [← propTime_image e (e.symm '' C), hCeq]

lemma lowerPropTime_congr {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) :
    lowerPropTime G = lowerPropTime H := by
  unfold lowerPropTime
  congr 1
  ext p
  constructor
  · rintro ⟨B, hmin, rfl⟩
    exact ⟨e '' B, (isMinimalZeroForcingSet_image_iff e B).mpr hmin, propTime_image e B⟩
  · rintro ⟨C, hmin, rfl⟩
    have hCeq : e '' (e.symm '' C) = C := by
      ext y
      simp only [Set.mem_image]
      constructor
      · rintro ⟨_, ⟨z, hz, rfl⟩, rfl⟩; simpa using hz
      · intro hy; exact ⟨e.symm y, ⟨y, hy, rfl⟩, e.apply_symm_apply y⟩
    refine ⟨e.symm '' C, (isMinimalZeroForcingSet_image_iff e (e.symm '' C)).mp (hCeq.symm ▸ hmin),
      ?_⟩
    rw [← propTime_image e (e.symm '' C), hCeq]

lemma isStandardFastJoin_congr [Fintype V] [Fintype W] {G : SimpleGraph V} {H : SimpleGraph W}
    (e : G ≃g H) : IsStandardFastJoin G ↔ IsStandardFastJoin H := by
  have hcard : Fintype.card V = Fintype.card W := Fintype.card_congr e.toEquiv
  unfold IsStandardFastJoin
  rw [hcard]
  constructor
  · intro h
    rcases h.2 with hK | ⟨t, ht, f, ⟨eJ⟩⟩
    · obtain ⟨eK⟩ := hK
      exact ⟨h.1, Or.inl ⟨e.symm.trans eK⟩⟩
    · exact ⟨h.1, Or.inr ⟨t, ht, f, ⟨e.symm.trans eJ⟩⟩⟩
  · intro h
    rcases h.2 with hK | ⟨t, ht, f, ⟨eJ⟩⟩
    · obtain ⟨eK⟩ := hK
      exact ⟨h.1, Or.inl ⟨e.trans eK⟩⟩
    · exact ⟨h.1, Or.inr ⟨t, ht, f, ⟨e.trans eJ⟩⟩⟩

end GeneralLemmas

/-! ## Section 3: The Infinite Counterexample Family `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`) -/

/-- The blowup `C_6[r_0 K_1, ..., r_5 K_1]`: vertex set `(i : Fin 6) × Fin (r i)`,
with edges between every vertex in part `i` and every vertex in part `j` iff `i ~ j` in `C_6`. -/
def c6Blowup (r : Fin 6 → ℕ) : SimpleGraph ((i : Fin 6) × Fin (r i)) where
  Adj x y := (cycleGraph 6).Adj x.1 y.1
  symm := ⟨fun _ _ h => (cycleGraph 6).symm.symm _ _ h⟩
  loopless := ⟨fun x h => (cycleGraph 6).loopless.irrefl x.1 h⟩

section C6Combinatorics

private lemma c6_other_neighbor_same_parity :
    ∀ u i : Fin 6, (cycleGraph 6).Adj u i →
      ∃ j : Fin 6, j ≠ i ∧ j.val % 2 = i.val % 2 ∧ (cycleGraph 6).Adj u j := by
  decide

private lemma c6_exists_common_neighbor :
    ∀ j m : Fin 6, m.val % 2 = j.val % 2 → m ≠ j →
      ∃ u : Fin 6, (cycleGraph 6).Adj u j ∧
        ∀ v : Fin 6, (cycleGraph 6).Adj u v → v = j ∨ v = m := by
  decide

private lemma c6_adj_succ (i : Fin 6) : (cycleGraph 6).Adj i (i + 1) := by
  revert i; decide

private lemma c6_compl_path_from_zero :
    ∀ i : Fin 6, i = 0 ∨
      (i ≠ 0 ∧ ¬ (cycleGraph 6).Adj 0 i) ∨
      (i ≠ 3 ∧ ¬ (cycleGraph 6).Adj 0 3 ∧ ¬ (cycleGraph 6).Adj 3 i) := by
  decide

end C6Combinatorics

section InfiniteFamilyProof

/-- Every blowup `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`) is connected. -/
theorem c6Blowup_connected (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    (c6Blowup r).Connected := by
  have hpos : ∀ i : Fin 6, 0 < r i := fun i => by have := hr i; omega
  let pt (i : Fin 6) : (k : Fin 6) × Fin (r k) := ⟨i, ⟨0, hpos i⟩⟩
  let emb : cycleGraph 6 →g c6Blowup r := ⟨pt, fun h => h⟩
  rw [SimpleGraph.connected_iff_exists_forall_reachable]
  refine ⟨pt 0, fun ⟨i, a⟩ => ?_⟩
  have h1 : (c6Blowup r).Reachable (pt 0) (pt (i + 1)) :=
    (SimpleGraph.preconnected_cycleGraph (0 : Fin 6) (i + 1)).map emb
  have h2 : (c6Blowup r).Adj (pt (i + 1)) ⟨i, a⟩ :=
    (cycleGraph 6).symm.symm _ _ (c6_adj_succ i)
  exact h1.trans h2.reachable

/-- `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`) is not a complete graph. -/
lemma c6Blowup_not_top (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    ∃ u v : (i : Fin 6) × Fin (r i), u ≠ v ∧ ¬ (c6Blowup r).Adj u v := by
  have h0 : 2 ≤ r 0 := hr 0
  refine ⟨⟨0, ⟨0, by omega⟩⟩, ⟨0, ⟨1, by omega⟩⟩, ?_, ?_⟩
  · intro heq
    have := congrArg (fun x : (i : Fin 6) × Fin (r i) => x.2.val) heq
    simp at this
  · exact (cycleGraph 6).loopless.irrefl 0

/-- The complement of `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`) is connected (diameter 2). -/
lemma c6Blowup_compl_connected (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    (c6Blowup r)ᶜ.Connected := by
  have hpos : ∀ i : Fin 6, 0 < r i := fun i => by have := hr i; omega
  let base : (i : Fin 6) × Fin (r i) := ⟨0, ⟨0, hpos 0⟩⟩
  let mid : (i : Fin 6) × Fin (r i) := ⟨3, ⟨0, hpos 3⟩⟩
  rw [SimpleGraph.connected_iff_exists_forall_reachable]
  refine ⟨base, fun ⟨i, a⟩ => ?_⟩
  rcases c6_compl_path_from_zero i with rfl | ⟨hi0, hnadj⟩ | ⟨hi3, h03, h3i⟩
  · by_cases ha : a = ⟨0, hpos 0⟩
    · subst ha; exact Reachable.rfl
    · refine SimpleGraph.Adj.reachable ⟨?_, (cycleGraph 6).loopless.irrefl 0⟩
      intro heq
      apply ha
      have : a.val = 0 := by
        have := congrArg (fun x : (k : Fin 6) × Fin (r k) => x.2.val) heq.symm
        simpa using this
      exact Fin.ext this
  · refine SimpleGraph.Adj.reachable ⟨?_, hnadj⟩
    intro heq
    exact hi0 (congrArg Sigma.fst heq).symm
  · have h1 : (c6Blowup r)ᶜ.Adj base mid :=
      ⟨fun heq => by
        have h03eq : (0 : Fin 6) = 3 := congrArg Sigma.fst heq
        exact absurd h03eq (by decide), h03⟩
    have h2 : (c6Blowup r)ᶜ.Adj mid ⟨i, a⟩ :=
      ⟨fun heq => hi3 (congrArg Sigma.fst heq).symm, h3i⟩
    exact h1.reachable.trans h2.reachable

/-- `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`) is not a standard fast join. -/
theorem c6Blowup_not_isStandardFastJoin (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    ¬ IsStandardFastJoin (c6Blowup r) :=
  not_isStandardFastJoin_of_not_top_of_compl_connected (c6Blowup r)
    (c6Blowup_not_top r hr) (c6Blowup_compl_connected r hr)

/-- Twin fort obstruction: two distinct white vertices in the same part `A_i` can never be forced. -/
lemma c6Blowup_twin_fort (r : Fin 6 → ℕ) (B : Set ((i : Fin 6) × Fin (r i)))
    (i : Fin 6) (a b : Fin (r i)) (hab : a ≠ b)
    (ha : ⟨i, a⟩ ∉ B) (hb : ⟨i, b⟩ ∉ B) :
    ∀ k : ℕ, ⟨i, a⟩ ∉ roundBlue (c6Blowup r) B k ∧ ⟨i, b⟩ ∉ roundBlue (c6Blowup r) B k := by
  intro k
  induction k with
  | zero => exact ⟨ha, hb⟩
  | succ k ih =>
    constructor
    · rintro (hmem | ⟨u, _, huniq⟩)
      · exact ih.1 hmem
      · have hia : (c6Blowup r).Adj u ⟨i, a⟩ := by
          have : ⟨i, a⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} := by
            rw [huniq]; exact Set.mem_singleton _
          exact this.1
        have hib : ⟨i, b⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} :=
          ⟨hia, ih.2⟩
        rw [huniq, Set.mem_singleton_iff] at hib
        exact hab (eq_of_heq (Sigma.mk.inj hib).2).symm
    · rintro (hmem | ⟨u, _, huniq⟩)
      · exact ih.2 hmem
      · have hib : (c6Blowup r).Adj u ⟨i, b⟩ := by
          have : ⟨i, b⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} := by
            rw [huniq]; exact Set.mem_singleton _
          exact this.1
        have hia : ⟨i, a⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} :=
          ⟨hib, ih.1⟩
        rw [huniq, Set.mem_singleton_iff] at hia
        exact hab (eq_of_heq (Sigma.mk.inj hia).2)

/-- Parity fort obstruction: if every part of a fixed parity (`E = {0,2,4}` or `O = {1,3,5}`)
contains a white vertex `w i`, then none of those white vertices is ever forced. -/
lemma c6Blowup_parity_fort (r : Fin 6 → ℕ) (B : Set ((i : Fin 6) × Fin (r i))) (p : Fin 2)
    (w : ∀ i : Fin 6, i.val % 2 = p.val → Fin (r i))
    (hw : ∀ i (hi : i.val % 2 = p.val), ⟨i, w i hi⟩ ∉ B) :
    ∀ k : ℕ, ∀ i (hi : i.val % 2 = p.val), ⟨i, w i hi⟩ ∉ roundBlue (c6Blowup r) B k := by
  intro k
  induction k with
  | zero => exact hw
  | succ k ih =>
    intro i hi
    rintro (hmem | ⟨u, _, huniq⟩)
    · exact ih i hi hmem
    · have hui : (cycleGraph 6).Adj u.1 i := by
        have : ⟨i, w i hi⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} := by
          rw [huniq]; exact Set.mem_singleton _
        exact this.1
      obtain ⟨j, hji, hjp, huj⟩ := c6_other_neighbor_same_parity u.1 i hui
      have hj : j.val % 2 = p.val := hjp.trans hi
      have hjmem : ⟨j, w j hj⟩ ∈ {w' | (c6Blowup r).Adj u w' ∧ w' ∉ roundBlue (c6Blowup r) B k} :=
        ⟨huj, ih j hj⟩
      rw [huniq, Set.mem_singleton_iff] at hjmem
      exact hji (congrArg Sigma.fst hjmem)

/-- Characterization of sets whose complement avoids both twin forts and parity forts. -/
def IsGoodSet (r : Fin 6 → ℕ) (B : Set ((i : Fin 6) × Fin (r i))) : Prop :=
  (∀ i : Fin 6, ∀ a b : Fin (r i), ⟨i, a⟩ ∉ B → ⟨i, b⟩ ∉ B → a = b) ∧
  (∃ i : Fin 6, i.val % 2 = 0 ∧ ∀ a : Fin (r i), ⟨i, a⟩ ∈ B) ∧
  (∃ i : Fin 6, i.val % 2 = 1 ∧ ∀ a : Fin (r i), ⟨i, a⟩ ∈ B)

/-- Every standard zero forcing set of `C_6[r_0 K_1, ..., r_5 K_1]` satisfies `IsGoodSet`. -/
lemma c6Blowup_isGood_of_zfs (r : Fin 6 → ℕ) (B : Set ((i : Fin 6) × Fin (r i)))
    (hzfs : IsZeroForcingSet (c6Blowup r) B) : IsGoodSet r B := by
  refine ⟨?_, ?_, ?_⟩
  · intro i a b ha hb
    by_contra hab
    have hnot := (c6Blowup_twin_fort r B i a b hab ha hb (propTime (c6Blowup r) B)).1
    exact hnot (hzfs ▸ Set.mem_univ _)
  · by_contra hno
    push Not at hno
    have hex : ∀ i : Fin 6, i.val % 2 = 0 → ∃ a : Fin (r i), ⟨i, a⟩ ∉ B := hno
    choose w hw using hex
    have hnot := c6Blowup_parity_fort r B 0 w hw (propTime (c6Blowup r) B) 0 (by decide)
    exact hnot (hzfs ▸ Set.mem_univ _)
  · by_contra hno
    push Not at hno
    have hex : ∀ i : Fin 6, i.val % 2 = 1 → ∃ a : Fin (r i), ⟨i, a⟩ ∉ B := hno
    choose w hw using hex
    have hnot := c6Blowup_parity_fort r B 1 w hw (propTime (c6Blowup r) B) 1 (by decide)
    exact hnot (hzfs ▸ Set.mem_univ _)

/-- Every `IsGoodSet` forces all remaining white vertices in round 1 (`B^{[1]} = V`). -/
lemma c6Blowup_roundBlue_one_eq_univ_of_isGood (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i)
    (B : Set ((i : Fin 6) × Fin (r i))) (hgood : IsGoodSet r B) :
    roundBlue (c6Blowup r) B 1 = Set.univ := by
  obtain ⟨hatmost, ⟨m0, hm0p, hm0B⟩, ⟨m1, hm1p, hm1B⟩⟩ := hgood
  have hblue : ∀ k : Fin 6, ∃ b : Fin (r k), ⟨k, b⟩ ∈ B := by
    intro k
    have hk : 2 ≤ r k := hr k
    let a0 : Fin (r k) := ⟨0, by omega⟩
    let a1 : Fin (r k) := ⟨1, by omega⟩
    by_cases h0 : ⟨k, a0⟩ ∈ B
    · exact ⟨a0, h0⟩
    · by_cases h1 : ⟨k, a1⟩ ∈ B
      · exact ⟨a1, h1⟩
      · have heq : a0 = a1 := hatmost k a0 a1 h0 h1
        have : (0 : ℕ) = 1 := congrArg Fin.val heq
        omega
  ext ⟨j, a⟩
  simp only [Set.mem_univ, iff_true]
  by_cases hjB : ⟨j, a⟩ ∈ B
  · exact Or.inl hjB
  · right
    have hm_ex : ∃ m : Fin 6, m.val % 2 = j.val % 2 ∧ m ≠ j ∧ ∀ c : Fin (r m), ⟨m, c⟩ ∈ B := by
      have hpar : j.val % 2 = 0 ∨ j.val % 2 = 1 := Nat.mod_two_eq_zero_or_one j.val
      rcases hpar with hj0 | hj1
      · refine ⟨m0, hm0p.trans hj0.symm, ?_, hm0B⟩
        rintro rfl
        exact hjB (hm0B a)
      · refine ⟨m1, hm1p.trans hj1.symm, ?_, hm1B⟩
        rintro rfl
        exact hjB (hm1B a)
    obtain ⟨m, hmp, hmj, hmB⟩ := hm_ex
    obtain ⟨u_idx, huj, hunbrs⟩ := c6_exists_common_neighbor j m hmp hmj
    obtain ⟨b, hbB⟩ := hblue u_idx
    refine ⟨⟨u_idx, b⟩, hbB, ?_⟩
    ext ⟨k, c⟩
    simp only [Set.mem_ofPred_eq, Set.mem_singleton_iff]
    constructor
    · rintro ⟨hadj, hcW⟩
      rcases hunbrs k hadj with rfl | rfl
      · have hca : c = a := hatmost k c a hcW hjB
        cases hca
        rfl
      · exact (hcW (hmB c)).elim
    · intro heq
      rw [heq]
      exact ⟨huj, hjB⟩

/-- Explicit minimal zero forcing set `B₀` omitting one vertex from each of parts `0, 1, 2, 3`. -/
def witnessZFS (r : Fin 6 → ℕ) : Set ((i : Fin 6) × Fin (r i)) :=
  {x | ¬ (x.1.val < 4 ∧ x.2.val = 0)}

lemma c6Blowup_witnessZFS_minimal (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    IsMinimalZeroForcingSet (c6Blowup r) (witnessZFS r) := by
  have hpos : ∀ i : Fin 6, 0 < r i := fun i => by have := hr i; omega
  have hgood : IsGoodSet r (witnessZFS r) := by
    refine ⟨?_, ?_, ?_⟩
    · intro i a b ha hb
      simp only [witnessZFS, Set.mem_ofPred_eq, not_not] at ha hb
      exact Fin.ext (ha.2.trans hb.2.symm)
    · refine ⟨4, by decide, fun a => ?_⟩
      simp [witnessZFS]
    · refine ⟨5, by decide, fun a => ?_⟩
      simp [witnessZFS]
  refine ⟨isZeroForcingSet_of_roundBlue_one_eq_univ (c6Blowup r) (witnessZFS r)
    (c6Blowup_roundBlue_one_eq_univ_of_isGood r hr (witnessZFS r) hgood), ?_⟩
  intro B' hss hzfs'
  obtain ⟨⟨k, c⟩, hkcB0, hkcNotB'⟩ := Set.exists_of_ssubset hss
  have hgood' := c6Blowup_isGood_of_zfs r B' hzfs'
  have hsub : B' ⊆ witnessZFS r := hss.1
  by_cases hk4 : k.val < 4
  · have hc0 : c.val ≠ 0 := fun h0 => hkcB0 ⟨hk4, h0⟩
    have h0NotB' : ⟨k, ⟨0, hpos k⟩⟩ ∉ B' := fun h => hsub h ⟨hk4, rfl⟩
    have heq := hgood'.1 k ⟨0, hpos k⟩ c h0NotB' hkcNotB'
    exact hc0 (congrArg Fin.val heq).symm
  · have hk45 : k = 4 ∨ k = 5 := by omega
    rcases hk45 with rfl | rfl
    · obtain ⟨m, hmp, hmB'⟩ := hgood'.2.1
      have hm_cases : m = 0 ∨ m = 2 ∨ m = 4 := by omega
      rcases hm_cases with rfl | rfl | rfl
      · exact hsub (hmB' ⟨0, hpos 0⟩) ⟨by simp, rfl⟩
      · exact hsub (hmB' ⟨0, hpos 2⟩) ⟨by simp, rfl⟩
      · exact hkcNotB' (hmB' c)
    · obtain ⟨m, hmp, hmB'⟩ := hgood'.2.2
      have hm_cases : m = 1 ∨ m = 3 ∨ m = 5 := by omega
      rcases hm_cases with rfl | rfl | rfl
      · exact hsub (hmB' ⟨0, hpos 1⟩) ⟨by simp, rfl⟩
      · exact hsub (hmB' ⟨0, hpos 3⟩) ⟨by simp, rfl⟩
      · exact hkcNotB' (hmB' c)

/-- Every minimal standard zero forcing set of `C_6[r_0 K_1, ..., r_5 K_1]` (`r_i ≥ 2`)
has propagation time `1`. -/
lemma c6Blowup_propTime_eq_one_of_minimal (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i)
    (B : Set ((i : Fin 6) × Fin (r i)))
    (hmin : IsMinimalZeroForcingSet (c6Blowup r) B) :
    propTime (c6Blowup r) B = 1 := by
  have h1 := c6Blowup_roundBlue_one_eq_univ_of_isGood r hr B
    (c6Blowup_isGood_of_zfs r B hmin.1)
  have hne : B ≠ Set.univ := by
    rintro rfl
    have hpos0 : 0 < r 0 := by have := hr 0; omega
    have hss : witnessZFS r ⊂ Set.univ := by
      refine ⟨Set.subset_univ _, fun h => ?_⟩
      have : ⟨(0 : Fin 6), ⟨0, hpos0⟩⟩ ∈ witnessZFS r := h (Set.mem_univ _)
      exact this ⟨by simp, rfl⟩
    exact hmin.2 (witnessZFS r) hss (c6Blowup_witnessZFS_minimal r hr).1
  exact propTime_eq_one_of_roundBlue_one_eq_univ (c6Blowup r) B h1 hne

/-- The set of propagation times of minimal standard zero forcing sets of `C_6[r_0 K_1, ..., r_5 K_1]`
is `{1}`. -/
lemma c6Blowup_minimalPropTimeSet (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    {p : ℕ | ∃ B, IsMinimalZeroForcingSet (c6Blowup r) B ∧ propTime (c6Blowup r) B = p} = {1} := by
  ext p
  simp only [Set.mem_ofPred_eq, Set.mem_singleton_iff]
  constructor
  · rintro ⟨B, hmin, rfl⟩
    exact c6Blowup_propTime_eq_one_of_minimal r hr B hmin
  · rintro rfl
    exact ⟨witnessZFS r, c6Blowup_witnessZFS_minimal r hr,
      c6Blowup_propTime_eq_one_of_minimal r hr (witnessZFS r) (c6Blowup_witnessZFS_minimal r hr)⟩

/-- `PT̄(C_6[r_0 K_1, ..., r_5 K_1]) = 1` for all `r_i ≥ 2`. -/
theorem c6Blowup_upperPropTime (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    upperPropTime (c6Blowup r) = 1 := by
  unfold upperPropTime
  rw [c6Blowup_minimalPropTimeSet r hr, csSup_singleton]

/-- `PT_(C_6[r_0 K_1, ..., r_5 K_1]) = 1` for all `r_i ≥ 2`. -/
theorem c6Blowup_lowerPropTime (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    lowerPropTime (c6Blowup r) = 1 := by
  unfold lowerPropTime
  rw [c6Blowup_minimalPropTimeSet r hr, csInf_singleton]

/-- Main theorem (infinite family): for every `r : Fin 6 → ℕ` with `∀ i, 2 ≤ r i`,
the graph `G = C_6[r_0 K_1, ..., r_5 K_1]` is connected, has `PT̄(G) = 1` (and `PT_(G) = 1`),
and is not a standard fast join — refuting Conjecture 1.8 of `arXiv:2511.16335v1`. -/
theorem refutes_conjecture_1_8_infinite_family (r : Fin 6 → ℕ) (hr : ∀ i : Fin 6, 2 ≤ r i) :
    (c6Blowup r).Connected ∧
    upperPropTime (c6Blowup r) = 1 ∧
    lowerPropTime (c6Blowup r) = 1 ∧
    ¬ IsStandardFastJoin (c6Blowup r) :=
  ⟨c6Blowup_connected r hr,
   c6Blowup_upperPropTime r hr,
   c6Blowup_lowerPropTime r hr,
   c6Blowup_not_isStandardFastJoin r hr⟩

end InfiniteFamilyProof

/-! ## Section 4: Explicit 12-Vertex Witness `Circ(12, {1, 5}) ≅ C_6[2K_1]` -/

/-- The 12-vertex circulant graph `Circ(12, {1, 5})` on `Fin 12`. -/
def circ12 : SimpleGraph (Fin 12) where
  Adj u v := u - v = 1 ∨ v - u = 1 ∨ u - v = 5 ∨ v - u = 5
  symm := ⟨fun _ _ h => by tauto⟩
  loopless := ⟨fun u => by revert u; decide⟩

/-- Explicit isomorphism `Circ(12, {1, 5}) ≃g C_6[2K_1]`. -/
def circ12IsoC6Blowup2 : circ12 ≃g c6Blowup (fun _ => 2) where
  toFun k := ⟨⟨k.val % 6, Nat.mod_lt _ (by omega)⟩, ⟨k.val / 6, by omega⟩⟩
  invFun x := ⟨x.1.val + 6 * x.2.val, by omega⟩
  left_inv k := by
    apply Fin.ext
    change k.val % 6 + 6 * (k.val / 6) = k.val
    omega
  right_inv x := by
    rcases x with ⟨⟨i, hi⟩, ⟨a, ha⟩⟩
    apply Sigma.ext
    · apply Fin.ext; change (i + 6 * a) % 6 = i; omega
    · apply heq_of_eq
      apply Fin.ext; change (i + 6 * a) / 6 = a; omega
  map_rel_iff' := by
    intro u v
    change (cycleGraph 6).Adj ⟨u.val % 6, _⟩ ⟨v.val % 6, _⟩ ↔ circ12.Adj u v
    dsimp only [circ12]
    revert u v
    decide

/-- Explicit 12-vertex counterexample to Conjecture 1.8 of `arXiv:2511.16335v1`:
`G = Circ(12, {1, 5}) ≅ C_6[2K_1]` is connected, has `PT̄(G) = PT_(G) = 1`,
and is not a standard fast join. -/
theorem refutes_conjecture_1_8_circ12 :
    circ12.Connected ∧
    upperPropTime circ12 = 1 ∧
    lowerPropTime circ12 = 1 ∧
    ¬ IsStandardFastJoin circ12 := by
  have hr : ∀ i : Fin 6, 2 ≤ (fun _ : Fin 6 => 2) i := fun _ => le_rfl
  obtain ⟨hconn, hup, hlo, hnot⟩ := refutes_conjecture_1_8_infinite_family (fun _ => 2) hr
  refine ⟨(circ12IsoC6Blowup2.connected_iff).mpr hconn, ?_, ?_, ?_⟩
  · rw [upperPropTime_congr circ12IsoC6Blowup2]; exact hup
  · rw [lowerPropTime_congr circ12IsoC6Blowup2]; exact hlo
  · rw [isStandardFastJoin_congr circ12IsoC6Blowup2]; exact hnot

/-- Direct negation of the universal statement of Conjecture 1.8 of `arXiv:2511.16335v1`. -/
theorem not_ferrero_conjecture_1_8 :
    ¬ (∀ (n : ℕ) (G : SimpleGraph (Fin n)),
      G.Connected → upperPropTime G = 1 → IsStandardFastJoin G) := by
  intro hconj
  obtain ⟨hconn, hup, _, hnot⟩ := refutes_conjecture_1_8_circ12
  exact hnot (hconj 12 circ12 hconn hup)

#print axioms refutes_conjecture_1_8_infinite_family
#print axioms refutes_conjecture_1_8_circ12
#print axioms not_ferrero_conjecture_1_8

end OpenMath.Ferrero251116335Conj18
