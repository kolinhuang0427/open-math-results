import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.DegreeSum
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

/-!
# Lau–Shiu–Premalatha–Zhang–Nalliah (2022/2023) — Refutation of Conjecture 2.2 (`arXiv:2208.14707v1`)

This file formalizes the refutation of **Conjecture 2.2** from Gee-Choon Lau, Wai-Chee Shiu,
K. Premalatha, Xiao-Min Zhang, and M. Nalliah, *"A note on local antimagic chromatic number
of lexicographic product graphs"*, `arXiv:2208.14707v1` (Section 2, p. 8, line 819; also
*Discrete Math. Lett.* 11 (2023), pp. 76–83, `DOI:10.47443/dml.2022.149`, p. 82):

> **Conjecture 2.2.** For `k ≥ 1` and graph `G` and `H`, `χ_la(G[H]) = χ(G) χ(H)` if and only if
> `χ(G) χ(H) = 2 χ(H) + ⌈χ(H) / k⌉`, where `2k + 1` is the length of a shortest odd cycle in `G`.

## Main Results

* `OpenMath.Lau220814707Conj22.refutes_lau_conjecture_2_2_K4_K2`:
  For the connected non-null simple graphs `G = K_4` and `H = K_2`:
  - the shortest odd cycle in `K_4` has length `3 = 2·1 + 1` (`k = 1`),
  - `χ(K_4) = 4` and `χ(K_2) = 2`,
  - `χ_la(K_4[K_2]) = 8 = χ(K_4) · χ(K_2)`,
  - yet `2 · χ(K_2) + ⌈χ(K_2) / 1⌉ = 6 ≠ 8 = χ(K_4) · χ(K_2)`.
* `OpenMath.Lau220814707Conj22.lexLabelK8_vertexSums`:
  Explicit verification of the `1..28` edge labeling of `K_8 ≅ K_4[K_2]` and its eight distinct
  vertex sums `(28, 64, 90, 108, 120, 128, 134, 140)`.
* `OpenMath.Lau220814707Conj22.refutes_lau_conjecture_2_2_infinite_family`:
  For every `m ≥ 4` and `n ≥ 2`, `(G, H) = (K_m, K_n)` refutes Conjecture 2.2
  (`k = 1`, `χ_la(K_m[K_n]) = m n = χ(K_m) χ(K_n)`, while `2 χ(K_n) + ⌈χ(K_n) / 1⌉ = 3 n ≠ m n`).
* `OpenMath.Lau220814707Conj22.not_lau_conjecture_2_2`:
  Direct negation of the universally quantified Conjecture 2.2 over connected non-null simple graphs.
-/

namespace OpenMath.Lau220814707Conj22

open scoped BigOperators

/-! ## Section 1: Primary-Source Definitions -/

/-- Proper vertex coloring of a simple graph `G`. -/
def IsProperColoring {V α : Type*} (G : SimpleGraph V) (c : V → α) : Prop :=
  ∀ u v : V, G.Adj u v → c u ≠ c v

/-- `G` admits a proper `t`-coloring. -/
def HasProperColoring {V : Type*} (G : SimpleGraph V) (t : ℕ) : Prop :=
  ∃ c : V → Fin t, IsProperColoring G c

/-- Chromatic number `χ(G) = min { t | G has a proper t-coloring }`. -/
noncomputable def chromaticNumber {V : Type*} (G : SimpleGraph V) : ℕ :=
  sInf { t : ℕ | HasProperColoring G t }

/-- Simple cycle of length `L ≥ 3` in `G`. -/
def HasCycleOfLen {V : Type*} (G : SimpleGraph V) (L : ℕ) : Prop :=
  ∃ hL : 3 ≤ L, ∃ v : Fin L → V, Function.Injective v ∧
    ∀ i : Fin L, G.Adj (v i) (v ⟨(i.val + 1) % L, Nat.mod_lt _ (by omega)⟩)

/-- `2k + 1` (`k ≥ 1`) is the length of a shortest odd cycle in `G`. -/
def IsShortestOddCycleLen {V : Type*} (G : SimpleGraph V) (k : ℕ) : Prop :=
  1 ≤ k ∧ HasCycleOfLen G (2 * k + 1) ∧
    ∀ j : ℕ, 1 ≤ j → HasCycleOfLen G (2 * j + 1) → k ≤ j

/-- Lexicographic product `G[H]` of simple graphs `G` and `H`:
`(u, u') ~ (v, v')` iff `u ~_G v`, or `u = v` and `u' ~_H v'`. -/
def lexProd {V W : Type*} (G : SimpleGraph V) (H : SimpleGraph W) : SimpleGraph (V × W) where
  Adj p q := G.Adj p.1 q.1 ∨ (p.1 = q.1 ∧ H.Adj p.2 q.2)
  symm := ⟨fun _ _ h => by
    rcases h with h | ⟨heq, h⟩
    · exact Or.inl h.symm
    · exact Or.inr ⟨heq.symm, h.symm⟩⟩
  loopless := ⟨fun p h => by
    rcases h with h | ⟨_, h⟩
    · exact G.loopless.irrefl p.1 h
    · exact H.loopless.irrefl p.2 h⟩

instance instDecidableRelLexProd {V W : Type*} [DecidableEq V]
    (G : SimpleGraph V) (H : SimpleGraph W)
    [DecidableRel G.Adj] [DecidableRel H.Adj] :
    DecidableRel (lexProd G H).Adj :=
  fun p q =>
    show Decidable (G.Adj p.1 q.1 ∨ (p.1 = q.1 ∧ H.Adj p.2 q.2)) from inferInstance

/-- Induced vertex sum `f^+(u) = ∑_{e ∈ E(u)} f(e)` for an edge labeling `f : E(G) → ℕ`. -/
def vertexSum {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : G.edgeFinset → ℕ) (u : V) : ℕ :=
  ∑ e : G.edgeFinset, if u ∈ (e : Sym2 V) then f e else 0

/-- A *local antimagic labeling* of `G` is a bijection `f : E(G) → {1, ..., |E(G)|}` such that
`f^+(u) ≠ f^+(v)` for every pair of adjacent vertices `u ~ v`. -/
def IsLocalAntimagicLabeling {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : G.edgeFinset → ℕ) : Prop :=
  Set.BijOn f Set.univ (Set.Icc 1 G.edgeFinset.card) ∧
  ∀ u v : V, G.Adj u v → vertexSum G f u ≠ vertexSum G f v

/-- Number of distinct vertex colors `c(f) = |{f^+(u) : u ∈ V}|` induced by `f`. -/
def numColors {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (f : G.edgeFinset → ℕ) : ℕ :=
  (Finset.univ.image (vertexSum G f)).card

/-- `G` admits a local antimagic `t`-coloring. -/
def HasLocalAntimagicColoring {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (t : ℕ) : Prop :=
  ∃ f : G.edgeFinset → ℕ, IsLocalAntimagicLabeling G f ∧ numColors G f = t

/-- Local antimagic chromatic number `χ_la(G) = min { c(f) | f is a local antimagic labeling }`. -/
noncomputable def localAntimagicChromaticNumber {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] : ℕ :=
  sInf { t : ℕ | HasLocalAntimagicColoring G t }

/-- Exact ceiling of rational division `⌈a / b⌉` for natural numbers (`b > 0`). -/
def natCeilDiv (a b : ℕ) : ℕ :=
  Nat.ceil ((a : ℚ) / (b : ℚ))

/-! ## Section 2: General Graph-Theoretic Lemmas -/

/-- Every local antimagic `t`-coloring induces a proper `t`-coloring of `G`. -/
lemma hasProperColoring_of_hasLocalAntimagicColoring {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] {t : ℕ}
    (h : HasLocalAntimagicColoring G t) : HasProperColoring G t := by
  rcases h with ⟨f, hf, hcard⟩
  let S : Finset ℕ := Finset.univ.image (vertexSum G f)
  have hScard : S.card = t := hcard
  let e : S ≃ Fin t := S.equivFin.trans (Fin.castOrderIso hScard).toEquiv
  refine ⟨fun u => e ⟨vertexSum G f u, Finset.mem_image.mpr ⟨u, Finset.mem_univ u, rfl⟩⟩, ?_⟩
  intro u v huv heq
  have hsub := e.injective heq
  have hval : vertexSum G f u = vertexSum G f v := congrArg Subtype.val hsub
  exact hf.2 u v huv hval

/-- If `G` admits a local antimagic labeling, then `χ(G) ≤ χ_la(G)`. -/
lemma chromaticNumber_le_localAntimagic {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (hne : ∃ t, HasLocalAntimagicColoring G t) :
    chromaticNumber G ≤ localAntimagicChromaticNumber G := by
  refine le_csInf hne ?_
  intro t ht
  exact Nat.sInf_le (hasProperColoring_of_hasLocalAntimagicColoring G ht)

/-- For any finite graph `G` with `χ(G) = N` and a local antimagic `N`-coloring, `χ_la(G) = N`. -/
lemma localAntimagicChromaticNumber_eq_of_witness {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] {N : ℕ}
    (hchi : chromaticNumber G = N) (hw : HasLocalAntimagicColoring G N) :
    localAntimagicChromaticNumber G = N := by
  apply le_antisymm
  · exact Nat.sInf_le hw
  · rw [← hchi]
    exact chromaticNumber_le_localAntimagic G ⟨N, hw⟩

/-- Chromatic number of the complete graph `K_N = ⊤` on `Fin N` is `N`. -/
theorem chromaticNumber_complete (N : ℕ) :
    chromaticNumber (⊤ : SimpleGraph (Fin N)) = N := by
  apply le_antisymm
  · refine Nat.sInf_le ⟨id, fun u v huv => huv⟩
  · refine le_csInf ⟨N, ⟨id, fun u v huv => huv⟩⟩ ?_
    rintro t ⟨c, hc⟩
    have hinj : Function.Injective c := by
      intro u v huv
      by_contra hne
      exact hc u v hne huv
    simpa [Fintype.card_fin] using Fintype.card_le_of_injective c hinj

/-- Connectedness of the complete graph `K_N = ⊤` on `Fin N` for `N ≥ 1`. -/
lemma complete_connected {N : ℕ} (hN : 1 ≤ N) :
    (⊤ : SimpleGraph (Fin N)).Connected := by
  have : Nonempty (Fin N) := ⟨⟨0, by omega⟩⟩
  refine ⟨fun u v => ?_⟩
  by_cases huv : u = v
  · subst huv; exact SimpleGraph.Reachable.refl u
  · exact SimpleGraph.Adj.reachable huv

/-- The shortest odd cycle in `K_m` (`m ≥ 3`) has length `3 = 2·1 + 1` (i.e., `k = 1`). -/
lemma complete_shortestOddCycleLen {m : ℕ} (hm : 3 ≤ m) :
    IsShortestOddCycleLen (⊤ : SimpleGraph (Fin m)) 1 := by
  refine ⟨le_rfl, ⟨le_rfl, ?_⟩, fun j hj _ => hj⟩
  refine ⟨fun i : Fin 3 => ⟨i.val, by omega⟩, ?_, ?_⟩
  · intro a b hab
    exact Fin.ext (congrArg (Fin.val : Fin m → ℕ) hab)
  · intro i
    show (⟨i.val, by omega⟩ : Fin m) ≠ ⟨(i.val + 1) % 3, by omega⟩
    intro heq
    have hv := congrArg Fin.val heq
    dsimp at hv
    omega

/-- `K_m[K_n]` is literally the complete graph `⊤` on `Fin m × Fin n`. -/
lemma lexProd_complete_eq_top (m n : ℕ) :
    lexProd (⊤ : SimpleGraph (Fin m)) (⊤ : SimpleGraph (Fin n)) = ⊤ := by
  ext p q
  simp only [lexProd, SimpleGraph.top_adj, ne_eq, Prod.ext_iff, not_and]
  constructor
  · rintro (h | ⟨_, h⟩) h1 h2
    · exact h h1
    · exact h h2
  · intro h
    by_cases h1 : p.1 = q.1
    · exact Or.inr ⟨h1, h h1⟩
    · exact Or.inl h1

/-- Transfer `HasLocalAntimagicColoring` along a graph isomorphism `G ≃g G'`. -/
lemma hasLocalAntimagicColoring_of_iso {V W : Type*} [Fintype V] [DecidableEq V]
    [Fintype W] [DecidableEq W]
    {G : SimpleGraph V} {G' : SimpleGraph W}
    [DecidableRel G.Adj] [DecidableRel G'.Adj]
    (e : G ≃g G') {t : ℕ} (h : HasLocalAntimagicColoring G t) :
    HasLocalAntimagicColoring G' t := by
  rcases h with ⟨f, ⟨hbij, hadj⟩, hcard⟩
  let mapEdge : G'.edgeFinset ≃ G.edgeFinset :=
    { toFun := fun x =>
        ⟨Sym2.map e.symm x.1, by
          rw [SimpleGraph.mem_edgeFinset]
          exact e.symm.map_mem_edgeSet_iff.mpr (SimpleGraph.mem_edgeFinset.mp x.2)⟩
      invFun := fun y =>
        ⟨Sym2.map e y.1, by
          rw [SimpleGraph.mem_edgeFinset]
          exact e.map_mem_edgeSet_iff.mpr (SimpleGraph.mem_edgeFinset.mp y.2)⟩
      left_inv := fun x => by
        apply Subtype.ext
        simp [Sym2.map_map]
      right_inv := fun y => by
        apply Subtype.ext
        simp [Sym2.map_map] }
  let f' : G'.edgeFinset → ℕ := fun x => f (mapEdge x)
  have hcardE : G'.edgeFinset.card = G.edgeFinset.card := by
    simpa only [Fintype.card_coe] using Fintype.card_congr mapEdge
  have hsum : ∀ w : W, vertexSum G' f' w = vertexSum G f (e.symm w) := by
    intro w
    unfold vertexSum
    refine Fintype.sum_equiv mapEdge _ _ fun x => ?_
    have hmem : w ∈ (x : Sym2 W) ↔ e.symm w ∈ (mapEdge x : Sym2 V) := by
      dsimp [mapEdge]
      constructor
      · intro hw; exact Sym2.mem_map.mpr ⟨w, hw, rfl⟩
      · intro hw
        rcases Sym2.mem_map.mp hw with ⟨z, hz, hzw⟩
        have : z = w := e.symm.injective hzw
        rwa [← this]
    simp only [f', hmem]
  refine ⟨f', ⟨?_, ?_⟩, ?_⟩
  · rw [hcardE]
    refine ⟨fun x _ => hbij.mapsTo (Set.mem_univ _), ?_, ?_⟩
    · intro x₁ _ x₂ _ hx
      exact mapEdge.injective (hbij.injOn (Set.mem_univ _) (Set.mem_univ _) hx)
    · intro y hy
      rcases hbij.surjOn hy with ⟨z, _, rfl⟩
      exact ⟨mapEdge.symm z, Set.mem_univ _, by simp [f']⟩
  · intro u v huv
    rw [hsum u, hsum v]
    exact hadj (e.symm u) (e.symm v) (e.symm.map_rel_iff.mpr huv)
  · unfold numColors at hcard ⊢
    have himg : Finset.univ.image (vertexSum G' f') = Finset.univ.image (vertexSum G f) := by
      ext c
      simp only [Finset.mem_image, Finset.mem_univ, true_and, hsum]
      constructor
      · rintro ⟨w, hw⟩; exact ⟨e.symm w, hw⟩
      · rintro ⟨v, hv⟩; exact ⟨e v, by simpa using hv⟩
    rw [himg, hcard]

/-! ## Section 3: Explicit Lexicographic Local Antimagic Labeling of `K_N` (`N ≥ 3`) -/

/-- Row start offset `∑_{a=0}^{i-1} (N - 1 - a)` for lexicographic ordering of edges of `K_N`. -/
def rowStart (N i : ℕ) : ℕ :=
  ∑ a ∈ Finset.range i, (N - 1 - a)

lemma rowStart_zero (N : ℕ) : rowStart N 0 = 0 := by
  simp [rowStart]

lemma rowStart_succ (N i : ℕ) : rowStart N (i + 1) = rowStart N i + (N - 1 - i) := by
  simp [rowStart, Finset.sum_range_succ]

lemma rowStart_mono {N i j : ℕ} (hij : i ≤ j) : rowStart N i ≤ rowStart N j := by
  induction hij with
  | refl => exact le_rfl
  | @step k _ ih =>
    rw [rowStart_succ]
    omega

/-- Lexicographic edge label `f({i, j}) = 1 + rowStart(N, i) + (j - i - 1)` for `i < j < N`. -/
def lexPair (N i j : ℕ) : ℕ :=
  if i < j then 1 + rowStart N i + (j - i - 1)
  else if j < i then 1 + rowStart N j + (i - j - 1)
  else 0

lemma lexPair_symm (N i j : ℕ) : lexPair N i j = lexPair N j i := by
  unfold lexPair
  by_cases h1 : i < j
  · have h2 : ¬ j < i := by omega
    simp [h1, h2]
  · by_cases h2 : j < i
    · simp [h1, h2]
    · simp [h1, h2]

lemma lexPair_lt {N i j : ℕ} (h : i < j) :
    lexPair N i j = 1 + rowStart N i + (j - i - 1) := by
  unfold lexPair
  rw [ite_eq_left h]

/-- Induced labeling on `Sym2 (Fin N)` via `Sym2.lift`. -/
def lexSym2 (N : ℕ) : Sym2 (Fin N) → ℕ :=
  Sym2.lift ⟨fun i j => lexPair N i.val j.val, fun i j => lexPair_symm N i.val j.val⟩

lemma lexSym2_mk (N : ℕ) (i j : Fin N) : lexSym2 N s(i, j) = lexPair N i.val j.val :=
  rfl

/-- Edge labeling of `K_N = ⊤` on `Fin N`. -/
def lexLabel (N : ℕ) (e : (⊤ : SimpleGraph (Fin N)).edgeFinset) : ℕ :=
  lexSym2 N e.1

lemma rowStart_total (N : ℕ) : 2 * rowStart N N = N * (N - 1) := by
  induction N with
  | zero => simp [rowStart]
  | succ m ih =>
    have hstep : rowStart (m + 1) (m + 1) = rowStart m m + m := by
      unfold rowStart
      rw [Finset.sum_range_succ, Nat.add_sub_cancel, Nat.sub_self, add_zero]
      have hdiff : ∀ a ∈ Finset.range m, m - a = (m - 1 - a) + 1 := by
        intro a ha
        have ham : a < m := Finset.mem_range.mp ha
        omega
      rw [Finset.sum_congr rfl hdiff, Finset.sum_add_distrib, Finset.sum_const,
        Finset.card_range, smul_eq_mul, mul_one]
    rw [hstep, Nat.add_sub_cancel]
    have hm : m = 0 ∨ 1 ≤ m := by omega
    rcases hm with rfl | hm
    · simp [rowStart]
    · zify [hm] at ih ⊢
      linarith

lemma card_edgeFinset_complete (N : ℕ) :
    (⊤ : SimpleGraph (Fin N)).edgeFinset.card = rowStart N N := by
  have h2 : 2 * (⊤ : SimpleGraph (Fin N)).edgeFinset.card = N * (N - 1) := by
    have hdeg := SimpleGraph.sum_degrees_eq_twice_card_edges (⊤ : SimpleGraph (Fin N))
    have hconst : ∀ v : Fin N, (⊤ : SimpleGraph (Fin N)).degree v = N - 1 := by
      intro v
      rw [SimpleGraph.degree, SimpleGraph.neighborFinset_eq_filter]
      have hfilt : Finset.univ.filter (fun w : Fin N => (⊤ : SimpleGraph (Fin N)).Adj v w) =
          Finset.univ.erase v := by
        ext w
        simp [ne_comm]
      rw [hfilt, Finset.card_erase_of_mem (Finset.mem_univ v), Finset.card_fin]
    simp only [hconst, Finset.sum_const, Finset.card_univ, Fintype.card_fin, smul_eq_mul] at hdeg
    exact hdeg.symm
  have hr := rowStart_total N
  omega

lemma lexPair_strict_order {N i₁ j₁ i₂ j₂ : ℕ}
    (h1 : i₁ < j₁) (hj1 : j₁ < N) (h2 : i₂ < j₂)
    (hlt : i₁ < i₂ ∨ (i₁ = i₂ ∧ j₁ < j₂)) :
    lexPair N i₁ j₁ < lexPair N i₂ j₂ := by
  rw [lexPair_lt h1, lexPair_lt h2]
  rcases hlt with hi | ⟨rfl, hj⟩
  · have hstep : rowStart N (i₁ + 1) ≤ rowStart N i₂ := rowStart_mono (by omega)
    rw [rowStart_succ] at hstep
    omega
  · omega

/-- `lexLabel N` is a bijection from `E(K_N)` onto `{1, ..., |E(K_N)|}`. -/
lemma lexLabel_bijOn (N : ℕ) :
    Set.BijOn (lexLabel N) Set.univ (Set.Icc 1 (⊤ : SimpleGraph (Fin N)).edgeFinset.card) := by
  rw [card_edgeFinset_complete]
  have hmaps : ∀ e : (⊤ : SimpleGraph (Fin N)).edgeFinset,
      lexLabel N e ∈ Finset.Icc 1 (rowStart N N) := by
    intro ⟨x, hx⟩
    rw [SimpleGraph.mem_edgeFinset] at hx
    induction x using Sym2.ind with
    | _ a b =>
      have hne : a ≠ b := by simpa [SimpleGraph.mem_edgeSet] using hx
      have hne' : a.val ≠ b.val := fun h => hne (Fin.ext h)
      rw [Finset.mem_Icc, lexLabel, lexSym2_mk]
      rcases lt_or_gt_of_ne hne' with hlt | hlt
      · rw [lexPair_lt hlt]
        have hle : rowStart N (a.val + 1) ≤ rowStart N N := rowStart_mono (by omega)
        rw [rowStart_succ] at hle
        exact ⟨by omega, by omega⟩
      · rw [lexPair_symm, lexPair_lt hlt]
        have hle : rowStart N (b.val + 1) ≤ rowStart N N := rowStart_mono (by omega)
        rw [rowStart_succ] at hle
        exact ⟨by omega, by omega⟩
  have hinj : Function.Injective (lexLabel N) := by
    intro ⟨x₁, hx₁⟩ ⟨x₂, hx₂⟩ heq
    apply Subtype.ext
    rw [SimpleGraph.mem_edgeFinset] at hx₁ hx₂
    induction x₁ using Sym2.ind with
    | _ a₁ b₁ =>
      induction x₂ using Sym2.ind with
      | _ a₂ b₂ =>
        have hne₁ : a₁.val ≠ b₁.val := fun h => (by simpa using hx₁ : a₁ ≠ b₁) (Fin.ext h)
        have hne₂ : a₂.val ≠ b₂.val := fun h => (by simpa using hx₂ : a₂ ≠ b₂) (Fin.ext h)
        -- Normalize both pairs to `(u₁ < v₁)` and `(u₂ < v₂)`
        dsimp only
        suffices ∀ u₁ v₁ u₂ v₂ : Fin N, u₁.val < v₁.val → u₂.val < v₂.val →
            lexPair N u₁.val v₁.val = lexPair N u₂.val v₂.val → s(u₁, v₁) = s(u₂, v₂) by
          rcases lt_or_gt_of_ne hne₁ with h1 | h1 <;> rcases lt_or_gt_of_ne hne₂ with h2 | h2
          · exact this a₁ b₁ a₂ b₂ h1 h2 heq
          · rw [Sym2.eq_swap (a := a₂) (b := b₂)]
            exact this a₁ b₁ b₂ a₂ h1 h2 (by simpa [lexLabel, lexSym2_mk, lexPair_symm] using heq)
          · rw [Sym2.eq_swap (a := a₁) (b := b₁)]
            exact this b₁ a₁ a₂ b₂ h1 h2 (by simpa [lexLabel, lexSym2_mk, lexPair_symm] using heq)
          · rw [Sym2.eq_swap (a := a₁) (b := b₁), Sym2.eq_swap (a := a₂) (b := b₂)]
            exact this b₁ a₁ b₂ a₂ h1 h2 (by simpa [lexLabel, lexSym2_mk, lexPair_symm] using heq)
        intro u₁ v₁ u₂ v₂ h1 h2 hpair
        have hu : u₁ = u₂ := by
          apply Fin.ext
          by_contra hne
          rcases lt_or_gt_of_ne hne with hlt | hlt
          · exact absurd hpair (ne_of_lt (lexPair_strict_order h1 v₁.isLt h2 (Or.inl hlt)))
          · exact absurd hpair.symm (ne_of_lt (lexPair_strict_order h2 v₂.isLt h1 (Or.inl hlt)))
        subst hu
        have hv : v₁ = v₂ := by
          apply Fin.ext
          by_contra hne
          rcases lt_or_gt_of_ne hne with hlt | hlt
          · exact absurd hpair (ne_of_lt (lexPair_strict_order h1 v₁.isLt h2 (Or.inr ⟨rfl, hlt⟩)))
          · exact absurd hpair.symm (ne_of_lt (lexPair_strict_order h2 v₂.isLt h1 (Or.inr ⟨rfl, hlt⟩)))
        subst hv
        rfl
  -- Injectivity into a Finset of the same cardinality gives surjectivity onto `Set.Icc 1 (rowStart N N)`
  have himg_eq : Finset.univ.image (lexLabel N) = Finset.Icc 1 (rowStart N N) := by
    apply Finset.eq_of_subset_of_card_le
    · intro y hy
      rcases Finset.mem_image.mp hy with ⟨e, _, rfl⟩
      exact hmaps e
    · rw [Finset.card_image_of_injective _ hinj, Finset.card_univ, Fintype.card_coe,
        card_edgeFinset_complete, Nat.card_Icc]
      omega
  refine ⟨fun e _ => by simpa [Finset.mem_Icc] using hmaps e, fun e₁ _ e₂ _ h => hinj h, ?_⟩
  intro y hy
  have hy' : y ∈ Finset.Icc 1 (rowStart N N) := Finset.mem_Icc.mpr hy
  rw [← himg_eq] at hy'
  rcases Finset.mem_image.mp hy' with ⟨e, _, rfl⟩
  exact ⟨e, Set.mem_univ _, rfl⟩

/-- Explicit vertex sum formula for `lexLabel N` on `K_N`:
`f^+(k) = ∑_{j ≠ k} lexPair N k j`. -/
lemma vertexSum_lexLabel_eq (N : ℕ) (k : Fin N) :
    vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N) k =
      ∑ j ∈ Finset.univ.erase k, lexPair N k.val j.val := by
  unfold vertexSum
  rw [← Finset.sum_filter]
  symm
  refine Finset.sum_bij
    (fun j hj =>
      ⟨s(k, j), by
        rw [SimpleGraph.mem_edgeFinset]
        exact (Finset.mem_erase.mp hj).1.symm⟩)
    ?_ ?_ ?_ ?_
  · intro j hj
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    exact Sym2.mem_mk_left k j
  · intro j₁ hj₁ j₂ hj₂ heq
    have hs : s(k, j₁) = s(k, j₂) := congrArg Subtype.val heq
    rcases Sym2.eq_iff.mp hs with ⟨_, h⟩ | ⟨h, _⟩
    · exact h
    · exact absurd h.symm (Finset.mem_erase.mp hj₂).1
  · intro ⟨x, hx⟩ hmem
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hmem
    rcases Sym2.mem_iff_exists.mp hmem with ⟨j, rfl⟩
    have hne : j ≠ k := by
      rw [SimpleGraph.mem_edgeFinset] at hx
      exact (by simpa [SimpleGraph.mem_edgeSet] using hx : k ≠ j).symm
    exact ⟨j, Finset.mem_erase.mpr ⟨hne, Finset.mem_univ j⟩, rfl⟩
  · intro j hj
    rfl

/-- Strict monotonicity of vertex sums `f^+(0) < f^+(1) < ... < f^+(N-1)` for `lexLabel N` (`N ≥ 3`). -/
lemma vertexSum_lexLabel_step_lt {N : ℕ} (hN : 3 ≤ N) (k : ℕ) (hk : k + 1 < N) :
    vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N) ⟨k, by omega⟩ <
      vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N) ⟨k + 1, hk⟩ := by
  let k₁ : Fin N := ⟨k, by omega⟩
  let k₂ : Fin N := ⟨k + 1, hk⟩
  have hne : k₁ ≠ k₂ := fun h => by have := congrArg Fin.val h; dsimp [k₁, k₂] at this; omega
  rw [vertexSum_lexLabel_eq, vertexSum_lexLabel_eq]
  have hk2_mem : k₂ ∈ Finset.univ.erase k₁ := Finset.mem_erase.mpr ⟨hne.symm, Finset.mem_univ k₂⟩
  have hk1_mem : k₁ ∈ Finset.univ.erase k₂ := Finset.mem_erase.mpr ⟨hne, Finset.mem_univ k₁⟩
  rw [← Finset.add_sum_erase _ _ hk2_mem, ← Finset.add_sum_erase _ _ hk1_mem]
  have hS : (Finset.univ.erase k₂).erase k₁ = (Finset.univ.erase k₁).erase k₂ :=
    Finset.erase_right_comm
  rw [hS, lexPair_symm N k₂.val k₁.val]
  refine Nat.add_lt_add_left ?_ _
  let S : Finset (Fin N) := (Finset.univ.erase k₁).erase k₂
  have hSnonempty : S.Nonempty := by
    by_cases hk0 : k = 0
    · refine ⟨⟨2, by omega⟩, ?_⟩
      simp only [S, Finset.mem_erase, Finset.mem_univ, and_true]
      refine ⟨fun h => ?_, fun h => ?_⟩ <;>
        (have := congrArg Fin.val h; dsimp [k₁, k₂] at this; omega)
    · refine ⟨⟨0, by omega⟩, ?_⟩
      simp only [S, Finset.mem_erase, Finset.mem_univ, and_true]
      refine ⟨fun h => ?_, fun h => ?_⟩ <;>
        (have := congrArg Fin.val h; dsimp [k₁, k₂] at this; omega)
  refine Finset.sum_lt_sum_of_nonempty hSnonempty ?_
  intro j hj
  simp only [Finset.mem_erase, Finset.mem_univ, and_true] at hj
  have hj1 : j.val ≠ k := fun h => hj.2 (Fin.ext h)
  have hj2 : j.val ≠ k + 1 := fun h => hj.1 (Fin.ext h)
  dsimp [k₁, k₂]
  by_cases hlt : j.val < k
  · rw [lexPair_symm N k j.val, lexPair_symm N (k + 1) j.val,
      lexPair_lt hlt, lexPair_lt (by omega : j.val < k + 1)]
    omega
  · have hgt : k + 1 < j.val := by omega
    rw [lexPair_lt (by omega : k < j.val), lexPair_lt hgt, rowStart_succ]
    have hjN : j.val < N := j.isLt
    omega

lemma vertexSum_lexLabel_strictMono {N : ℕ} (hN : 3 ≤ N) :
    StrictMono (vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N)) := by
  intro a b hab
  suffices ∀ d : ℕ, ∀ (b : Fin N), b.val = a.val + (d + 1) →
      vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N) a <
        vertexSum (⊤ : SimpleGraph (Fin N)) (lexLabel N) b by
    exact this (b.val - a.val - 1) b (by have : a.val < b.val := hab; omega)
  intro d
  induction d with
  | zero =>
    intro b hb
    have hstep := vertexSum_lexLabel_step_lt hN a.val (by omega)
    have hbeq : (⟨a.val + 1, by omega⟩ : Fin N) = b := Fin.ext (by dsimp; omega)
    have haeq : (⟨a.val, by omega⟩ : Fin N) = a := rfl
    rwa [haeq, hbeq] at hstep
  | succ d ih =>
    intro b hb
    let m : Fin N := ⟨a.val + (d + 1), by omega⟩
    have hm_lt := ih m rfl
    have hstep := vertexSum_lexLabel_step_lt hN m.val (by dsimp [m]; omega)
    have hbeq : (⟨m.val + 1, by dsimp [m]; omega⟩ : Fin N) = b := Fin.ext (by dsimp [m]; omega)
    have hmeq : (⟨m.val, by omega⟩ : Fin N) = m := rfl
    rw [hmeq, hbeq] at hstep
    exact lt_trans hm_lt hstep

/-- `K_N` (`N ≥ 3`) admits a local antimagic `N`-coloring via `lexLabel N`. -/
theorem complete_hasLocalAntimagicColoring {N : ℕ} (hN : 3 ≤ N) :
    HasLocalAntimagicColoring (⊤ : SimpleGraph (Fin N)) N := by
  refine ⟨lexLabel N, ⟨lexLabel_bijOn N, ?_⟩, ?_⟩
  · intro u v huv
    exact (vertexSum_lexLabel_strictMono hN).injective.ne huv
  · unfold numColors
    rw [Finset.card_image_of_injective _ (vertexSum_lexLabel_strictMono hN).injective,
      Finset.card_univ, Fintype.card_fin]

/-- For every `N ≥ 3`, `χ_la(K_N) = N`. -/
theorem localAntimagicChromaticNumber_complete {N : ℕ} (hN : 3 ≤ N) :
    localAntimagicChromaticNumber (⊤ : SimpleGraph (Fin N)) = N :=
  localAntimagicChromaticNumber_eq_of_witness (⊤ : SimpleGraph (Fin N))
    (chromaticNumber_complete N) (complete_hasLocalAntimagicColoring hN)

/-- Graph isomorphism `K_{m*n} ≃g K_m[K_n]`. -/
def isoCompleteLexProd (m n : ℕ) :
    (⊤ : SimpleGraph (Fin (m * n))) ≃g
      lexProd (⊤ : SimpleGraph (Fin m)) (⊤ : SimpleGraph (Fin n)) where
  toEquiv := finProdFinEquiv.symm
  map_rel_iff' := by
    intro a b
    rw [lexProd_complete_eq_top]
    exact finProdFinEquiv.symm.injective.ne_iff

/-- Chromatic number of `K_m[K_n]` equals `m * n`. -/
lemma chromaticNumber_lexProd_complete (m n : ℕ) :
    chromaticNumber (lexProd (⊤ : SimpleGraph (Fin m)) (⊤ : SimpleGraph (Fin n))) = m * n := by
  have htop := lexProd_complete_eq_top m n
  rw [htop]
  apply le_antisymm
  · refine Nat.sInf_le ⟨finProdFinEquiv, fun u v huv => finProdFinEquiv.injective.ne huv⟩
  · refine le_csInf ⟨m * n, ⟨finProdFinEquiv, fun u v huv => finProdFinEquiv.injective.ne huv⟩⟩ ?_
    rintro t ⟨c, hc⟩
    have hinj : Function.Injective c := by
      intro u v huv
      by_contra hne
      exact hc u v hne huv
    simpa [Fintype.card_prod, Fintype.card_fin] using Fintype.card_le_of_injective c hinj

/-- For `m * n ≥ 3`, `χ_la(K_m[K_n]) = m * n`. -/
theorem localAntimagicChromaticNumber_lexProd_complete {m n : ℕ} (hmn : 3 ≤ m * n) :
    localAntimagicChromaticNumber
      (lexProd (⊤ : SimpleGraph (Fin m)) (⊤ : SimpleGraph (Fin n))) = m * n :=
  localAntimagicChromaticNumber_eq_of_witness _
    (chromaticNumber_lexProd_complete m n)
    (hasLocalAntimagicColoring_of_iso (isoCompleteLexProd m n)
      (complete_hasLocalAntimagicColoring hmn))

/-! ## Section 4: Explicit `K_4[K_2] ≅ K_8` Witness Sums and Main Refutations -/

/-- Explicit verification of the `8` vertex sums `(28, 64, 90, 108, 120, 128, 134, 140)`
for the lexicographic `1..28` edge labeling of `K_8 ≅ K_4[K_2]`. -/
theorem lexLabelK8_vertexSums :
    (vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 0,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 1,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 2,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 3,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 4,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 5,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 6,
     vertexSum (⊤ : SimpleGraph (Fin 8)) (lexLabel 8) 7) =
      (28, 64, 90, 108, 120, 128, 134, 140) := by
  have hsum8 : ∀ k : Fin 8,
      ∑ j ∈ Finset.univ.erase k, lexPair 8 k.val j.val =
      ∑ j : Fin 8, if j = k then 0 else lexPair 8 k.val j.val := by
    intro k
    rw [Finset.sum_ite, Finset.sum_const_zero, zero_add]
    congr 1
    ext j
    simp [Finset.mem_erase]
  simp only [vertexSum_lexLabel_eq, hsum8, Fin.sum_univ_eight]
  norm_num [lexPair, rowStart, Finset.sum_range_succ]

lemma natCeilDiv_div_one (a : ℕ) : natCeilDiv a 1 = a := by
  unfold natCeilDiv
  simp

/-- **Explicit Counterexample `(G, H) = (K_4, K_2)` to Conjecture 2.2 of `arXiv:2208.14707v1`:**
Both graphs are connected and non-null, `G = K_4` has shortest odd cycle length `3 = 2·1 + 1`
(`k = 1`), `χ_la(K_4[K_2]) = 8 = χ(K_4) χ(K_2)`, yet
`2 χ(K_2) + ⌈χ(K_2) / 1⌉ = 6 ≠ 8 = χ(K_4) χ(K_2)`. -/
theorem refutes_lau_conjecture_2_2_K4_K2 :
    let G : SimpleGraph (Fin 4) := ⊤
    let H : SimpleGraph (Fin 2) := ⊤
    G.Connected ∧ H.Connected ∧
    0 < G.edgeFinset.card ∧ 0 < H.edgeFinset.card ∧
    IsShortestOddCycleLen G 1 ∧
    chromaticNumber G = 4 ∧
    chromaticNumber H = 2 ∧
    localAntimagicChromaticNumber (lexProd G H) = chromaticNumber G * chromaticNumber H ∧
    chromaticNumber G * chromaticNumber H ≠
      2 * chromaticNumber H + natCeilDiv (chromaticNumber H) 1 := by
  refine ⟨complete_connected (by omega), complete_connected (by omega), ?_, ?_,
    complete_shortestOddCycleLen (by omega),
    chromaticNumber_complete 4, chromaticNumber_complete 2, ?_, ?_⟩
  · rw [card_edgeFinset_complete]; decide
  · rw [card_edgeFinset_complete]; decide
  · rw [chromaticNumber_complete 4, chromaticNumber_complete 2,
      localAntimagicChromaticNumber_lexProd_complete (by omega)]
  · rw [chromaticNumber_complete 4, chromaticNumber_complete 2, natCeilDiv_div_one]
    omega

/-- **Infinite Family of Counterexamples `(K_m, K_n)` (`m ≥ 4, n ≥ 2`) to Conjecture 2.2:**
For all `m ≥ 4, n ≥ 2`, `G = K_m` and `H = K_n` are connected non-null simple graphs with
`k = 1`, `χ_la(K_m[K_n]) = m n = χ(K_m) χ(K_n)`, yet `2 χ(K_n) + ⌈χ(K_n)/1⌉ = 3n ≠ mn`. -/
theorem refutes_lau_conjecture_2_2_infinite_family {m n : ℕ} (hm : 4 ≤ m) (hn : 2 ≤ n) :
    let G : SimpleGraph (Fin m) := ⊤
    let H : SimpleGraph (Fin n) := ⊤
    G.Connected ∧ H.Connected ∧
    0 < G.edgeFinset.card ∧ 0 < H.edgeFinset.card ∧
    IsShortestOddCycleLen G 1 ∧
    localAntimagicChromaticNumber (lexProd G H) = chromaticNumber G * chromaticNumber H ∧
    chromaticNumber G * chromaticNumber H ≠
      2 * chromaticNumber H + natCeilDiv (chromaticNumber H) 1 := by
  have hmn : 3 ≤ m * n := by nlinarith
  refine ⟨complete_connected (by omega), complete_connected (by omega), ?_, ?_,
    complete_shortestOddCycleLen (by omega), ?_, ?_⟩
  · rw [card_edgeFinset_complete]
    have ht := rowStart_total m
    have hm1 : 3 ≤ m - 1 := by omega
    nlinarith
  · rw [card_edgeFinset_complete]
    have ht := rowStart_total n
    have hn1 : 1 ≤ n - 1 := by omega
    nlinarith
  · rw [chromaticNumber_complete m, chromaticNumber_complete n,
      localAntimagicChromaticNumber_lexProd_complete hmn]
  · rw [chromaticNumber_complete m, chromaticNumber_complete n, natCeilDiv_div_one]
    nlinarith

/-- **Direct Negation of Conjecture 2.2 (`arXiv:2208.14707v1`, Section 2, p. 8):**
It is false that for all connected non-null finite simple graphs `G, H` and all `k ≥ 1` where
`2k + 1` is the length of a shortest odd cycle in `G`,
`χ_la(G[H]) = χ(G) χ(H) ↔ χ(G) χ(H) = 2 χ(H) + ⌈χ(H) / k⌉`. -/
theorem not_lau_conjecture_2_2 :
    ¬ (∀ (p q : ℕ) (G : SimpleGraph (Fin p)) (H : SimpleGraph (Fin q))
        [DecidableRel G.Adj] [DecidableRel H.Adj] (k : ℕ),
        G.Connected → H.Connected →
        0 < G.edgeFinset.card → 0 < H.edgeFinset.card →
        IsShortestOddCycleLen G k →
        (localAntimagicChromaticNumber (lexProd G H) = chromaticNumber G * chromaticNumber H ↔
          chromaticNumber G * chromaticNumber H =
            2 * chromaticNumber H + natCeilDiv (chromaticNumber H) k)) := by
  intro hconj
  obtain ⟨hGc, hHc, hGe, hHe, hk, _, _, heq, hne⟩ := refutes_lau_conjecture_2_2_K4_K2
  have hiff := hconj 4 2 (⊤ : SimpleGraph (Fin 4)) (⊤ : SimpleGraph (Fin 2)) 1
    hGc hHc hGe hHe hk
  exact hne (hiff.mp heq)

#print axioms lexLabelK8_vertexSums
#print axioms refutes_lau_conjecture_2_2_K4_K2
#print axioms refutes_lau_conjecture_2_2_infinite_family
#print axioms not_lau_conjecture_2_2

end OpenMath.Lau220814707Conj22
