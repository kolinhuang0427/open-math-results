import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Maps
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.CardEmbedding
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# Refutation of Questions 2 & 3 of Kaul–Maxfield–Mudrock–Thomason (`arXiv:2112.05316v2`)

This module formalizes the refutation of BOTH **Question 2** (`\label{ques: classify}`) and
**Question 3** (`\label{ques: easier}`) from Section 1.3–1.4 of
Hemanshu Kaul, Michael Maxfield, Jeffrey A. Mudrock, and Seth Thomason,
*"The DP Color Function of Clique-Gluings of Graphs"*, `arXiv:2112.05316v2`
(published in *Enumerative Combinatorics and Applications* 4, 2024), for **every** $p \ge 4$
and **every** $d_G(v) = p \ge 4$ (in fact for every $p \ge 3$).

## Main results

- `kaul_question_3_false`: For every $p \ge 4$ (and indeed every $p \ge 3$), there exist a
  nonempty finite simple graph $G$, a simplicial vertex $v$ of $G$ with $\deg_G(v) = p$, and
  $m = p + 1 \ge \deg_G(v)$ such that
  $$P_{DP}(G, m) > (m - \deg_G(v)) \cdot P_{DP}(G - \{v\}, m).$$
- `kaul_question_2_false`: For every $p \ge 4$ (and indeed every $p \ge 3$), there exist nonempty
  finite simple graphs $G_1, G_2, G$ with $G \in G_1 \oplus_p G_2$ (a $K_p$-gluing of $G_1$ and
  $G_2$) and $m = p + 1 \ge p$ such that
  $$P_{DP}(G, m) > \frac{P_{DP}(G_1, m) \cdot P_{DP}(G_2, m)}{\prod_{i=0}^{p-1} (m - i)}.$$

## Construction

For every $p \ge 3$, let $G_0^{(p)} := K_{p-2} \vee K_{2,p}$ and form $G_0, G_1, \dots, G_{2p}$
by iteratively attaching a simplicial vertex $d_k$ of degree $p$ to each of the $2p$ copies of
$K_p$ in $G_0^{(p)}$. We prove:
1. `dpColorFun_top_eq_factorial` (Lemma 1): $P_{DP}(K_{p+1}, p+1) = (p+1)!$.
2. `dpColorFun_G0_lt_chromPoly` (Lemma 2): Using a single transposed edge in a full $(p+1)$-fold
   cover, $P_{DP}(G_0^{(p)}, p+1) + (p-1)!(2^p - 2p + 2) \le P(G_0^{(p)}, p+1)$, so
   $P_{DP}(G_0^{(p)}, p+1) < P(G_0^{(p)}, p+1)$.
3. `precoloring_extension_G0` (Lemma 3): Every $\mathcal{H}_{K_r}$-coloring of any $p$-clique
   $K_r$ in $G_0^{(p)}$ extends to an $\mathcal{H}$-coloring of $G_0^{(p)}$.
4. `exists_counterexample_step` (Main Theorem): $P_{DP}(G_{2p}, p+1) > P_{DP}(G_0^{(p)}, p+1)$,
   hence some step $k \in \{0, \dots, 2p - 1\}$ satisfies $P_{DP}(G_{k+1}, p+1) > P_{DP}(G_k, p+1)$.
-/

namespace OpenMath.Kaul211205316Ques3

open SimpleGraph Finset

/-! ## Section 1: Covers, DP Color Function, Simplicial Vertices, and $K_p$-Gluings -/

/-- An $m$-fold cover $\mathcal{H} = (L, H)$ of a simple graph $G$ on vertex type $V$, represented
with $V(H) = V \times \mathrm{Fin}\,m$ and $L(u) = \{u\} \times \mathrm{Fin}\,m$:
- Each part $L(u)$ is a clique in $H$.
- Every cross-edge in $H$ projects to an edge of $G$.
- Cross-edges between $L(u)$ and $L(v)$ ($u \ne v$) form a matching. -/
structure FoldCover {V : Type*} (G : SimpleGraph V) (m : ℕ) where
  H : SimpleGraph (V × Fin m)
  clique_part : ∀ u c₁ c₂, c₁ ≠ c₂ → H.Adj (u, c₁) (u, c₂)
  adj_subset : ∀ u v c₁ c₂, H.Adj (u, c₁) (v, c₂) → u = v ∨ G.Adj u v
  matching_right : ∀ u v c c₁ c₂, u ≠ v → H.Adj (u, c) (v, c₁) → H.Adj (u, c) (v, c₂) → c₁ = c₂

namespace FoldCover

variable {V : Type*} {G : SimpleGraph V} {m : ℕ}

lemma matching_left (C : FoldCover G m) {u v : V} {c₁ c₂ c : Fin m} (huv : u ≠ v)
    (h1 : C.H.Adj (u, c₁) (v, c)) (h2 : C.H.Adj (u, c₂) (v, c)) : c₁ = c₂ :=
  C.matching_right v u c c₁ c₂ huv.symm h1.symm h2.symm

/-- A cover $\mathcal{H} = (L, H)$ is *full* if $E_H(L(u), L(v))$ is a perfect matching for every
edge $uv \in E(G)$. (Because $E_H(L(u), L(v))$ is already a matching on equal-size finite parts,
left-totality is equivalent to being a perfect matching.) -/
def IsFull (C : FoldCover G m) : Prop :=
  ∀ u v, G.Adj u v → ∀ c₁ : Fin m, ∃ c₂ : Fin m, C.H.Adj (u, c₁) (v, c₂)

/-- An $\mathcal{H}$-coloring of $G$ as an independent set of size $|V(G)|$ in $H$
(exact primary-source definition from `paper.tex`, Section 1.1). -/
def IsIndepColoring [Fintype V] (C : FoldCover G m) (I : Finset (V × Fin m)) : Prop :=
  I.card = Fintype.card V ∧ ∀ x ∈ I, ∀ y ∈ I, ¬ C.H.Adj x y

/-- Functional form of an $\mathcal{H}$-coloring: a choice $f : V \to \mathrm{Fin}\,m$ with
no adjacent chosen pairs across edges of $G$. -/
def IsHColoring (C : FoldCover G m) (f : V → Fin m) : Prop :=
  ∀ u v, G.Adj u v → ¬ C.H.Adj (u, f u) (v, f v)

/-- The canonical bijection between independent sets of size $|V(G)|$ in $H$ and functional
$\mathcal{H}$-colorings $f : V \to \mathrm{Fin}\,m$. -/
noncomputable def indepColoringEquiv [Fintype V] [DecidableEq V] (C : FoldCover G m) :
    { I : Finset (V × Fin m) // C.IsIndepColoring I } ≃ { f : V → Fin m // C.IsHColoring f } := by
  classical
  refine
    { toFun := fun ⟨I, hcard, hind⟩ =>
        ⟨fun u =>
            have hsurj : I.image Prod.fst = Finset.univ := by
              apply Finset.eq_univ_of_card
              rw [Finset.card_image_of_injOn]
              · exact hcard
              · intro x hx y hy hxy
                rcases x with ⟨u₁, c₁⟩; rcases y with ⟨u₂, c₂⟩
                dsimp at hxy; subst hxy
                by_contra hne
                have hc : c₁ ≠ c₂ := fun h => hne (by subst h; rfl)
                exact hind _ hx _ hy (C.clique_part u₁ c₁ c₂ hc)
            have hex : ∃ c : Fin m, (u, c) ∈ I := by
              have hu : u ∈ I.image Prod.fst := by rw [hsurj]; exact Finset.mem_univ u
              rcases Finset.mem_image.mp hu with ⟨⟨u', c⟩, hmem, heq⟩
              dsimp at heq; subst heq
              exact ⟨c, hmem⟩
            Classical.choose hex,
          by
            intro u v huv hadj
            have hsurj : I.image Prod.fst = Finset.univ := by
              apply Finset.eq_univ_of_card
              rw [Finset.card_image_of_injOn]
              · exact hcard
              · intro x hx y hy hxy
                rcases x with ⟨u₁, c₁⟩; rcases y with ⟨u₂, c₂⟩
                dsimp at hxy; subst hxy
                by_contra hne
                have hc : c₁ ≠ c₂ := fun h => hne (by subst h; rfl)
                exact hind _ hx _ hy (C.clique_part u₁ c₁ c₂ hc)
            have hex : ∀ w, ∃ c : Fin m, (w, c) ∈ I := fun w => by
              have hw : w ∈ I.image Prod.fst := by rw [hsurj]; exact Finset.mem_univ w
              rcases Finset.mem_image.mp hw with ⟨⟨w', c⟩, hmem, heq⟩
              dsimp at heq; subst heq
              exact ⟨c, hmem⟩
            exact hind _ (Classical.choose_spec (hex u)) _ (Classical.choose_spec (hex v)) hadj⟩
      invFun := fun ⟨f, hf⟩ =>
        ⟨Finset.univ.image (fun u => (u, f u)),
          by
            rw [Finset.card_image_of_injective _ (fun a b h => (Prod.mk.inj h).1), Finset.card_univ],
          by
            intro x hx y hy hadj
            rcases Finset.mem_image.mp hx with ⟨u, _, rfl⟩
            rcases Finset.mem_image.mp hy with ⟨v, _, rfl⟩
            rcases C.adj_subset u v (f u) (f v) hadj with rfl | huv
            · exact C.H.loopless.irrefl _ hadj
            · exact hf u v huv hadj⟩
      left_inv := by
        rintro ⟨I, hcard, hind⟩
        apply Subtype.ext
        dsimp
        ext ⟨u, c⟩
        simp only [Finset.mem_image, Finset.mem_univ, true_and]
        have hsurj : I.image Prod.fst = Finset.univ := by
          apply Finset.eq_univ_of_card
          rw [Finset.card_image_of_injOn]
          · exact hcard
          · intro x hx y hy hxy
            rcases x with ⟨u₁, c₁⟩; rcases y with ⟨u₂, c₂⟩
            dsimp at hxy; subst hxy
            by_contra hne
            have hc : c₁ ≠ c₂ := fun h => hne (by subst h; rfl)
            exact hind _ hx _ hy (C.clique_part u₁ c₁ c₂ hc)
        have hex : ∀ w, ∃ c' : Fin m, (w, c') ∈ I := fun w => by
          have hw : w ∈ I.image Prod.fst := by rw [hsurj]; exact Finset.mem_univ w
          rcases Finset.mem_image.mp hw with ⟨⟨w', c'⟩, hmem, heq⟩
          dsimp at heq; subst heq
          exact ⟨c', hmem⟩
        constructor
        · rintro ⟨u', hpair⟩
          rcases Prod.mk.inj hpair with ⟨rfl, rfl⟩
          exact Classical.choose_spec (hex u')
        · intro hmem
          refine ⟨u, Prod.ext rfl ?_⟩
          by_contra hne
          exact hind _ (Classical.choose_spec (hex u)) _ hmem (C.clique_part u _ _ hne)
      right_inv := by
        rintro ⟨f, hf⟩
        apply Subtype.ext
        funext u
        dsimp
        have hex : ∃ c : Fin m, (u, c) ∈ Finset.univ.image (fun w => (w, f w)) :=
          ⟨f u, Finset.mem_image.mpr ⟨u, Finset.mem_univ u, rfl⟩⟩
        have hmem := Classical.choose_spec hex
        rcases Finset.mem_image.mp hmem with ⟨w, _, hpair⟩
        rcases Prod.mk.inj hpair with ⟨rfl, hc⟩
        exact hc.symm }

/-- Number of $\mathcal{H}$-colorings $P_{DP}(G, \mathcal{H})$: count of independent sets of size
$|V(G)|$ in $H$. -/
noncomputable def dpColorCount [Fintype V] (C : FoldCover G m) : ℕ := by
  classical exact Fintype.card { I : Finset (V × Fin m) // C.IsIndepColoring I }

lemma dpColorCount_eq_card_hColoring [Fintype V] (C : FoldCover G m)
    [Fintype { f : V → Fin m // C.IsHColoring f }] :
    C.dpColorCount = Fintype.card { f : V → Fin m // C.IsHColoring f } := by
  classical
  unfold dpColorCount
  convert Fintype.card_congr (C.indepColoringEquiv)

/-- Canonical $m$-fold cover of $G$: cross-edges connect $(u, c)$ and $(v, c)$ whenever
$uv \in E(G)$. -/
def canonical (G : SimpleGraph V) (m : ℕ) : FoldCover G m where
  H :=
    { Adj := fun x y => (x.1 = y.1 ∧ x.2 ≠ y.2) ∨ (G.Adj x.1 y.1 ∧ x.2 = y.2)
      symm := ⟨by
        rintro ⟨u, c₁⟩ ⟨v, c₂⟩ (⟨rfl, hne⟩ | ⟨hadj, rfl⟩)
        · exact Or.inl ⟨rfl, hne.symm⟩
        · exact Or.inr ⟨hadj.symm, rfl⟩⟩
      loopless := ⟨by
        rintro ⟨u, c⟩ (⟨_, hne⟩ | ⟨hadj, _⟩)
        · exact hne rfl
        · exact G.loopless.irrefl u hadj⟩ }
  clique_part := fun u c₁ c₂ hne => Or.inl ⟨rfl, hne⟩
  adj_subset := by
    rintro u v c₁ c₂ (⟨h, _⟩ | ⟨h, _⟩)
    · exact Or.inl h
    · exact Or.inr h
  matching_right := by
    rintro u v c c₁ c₂ huv (⟨heq, _⟩ | ⟨_, rfl⟩) (⟨heq', _⟩ | ⟨_, h2⟩)
    · exact (huv heq).elim
    · exact (huv heq).elim
    · exact (huv heq').elim
    · exact h2

/-- A cover $\mathcal{H}$ has a *canonical labeling* if there exist permutations
$\sigma_u \in S_m$ such that $(u, c_1)(v, c_2) \in E(H) \iff \sigma_u(c_1) = \sigma_v(c_2)$
for all edges $uv \in E(G)$. -/
def HasCanonicalLabeling (C : FoldCover G m) : Prop :=
  ∃ σ : V → Equiv.Perm (Fin m),
    ∀ u v, G.Adj u v → ∀ c₁ c₂, C.H.Adj (u, c₁) (v, c₂) ↔ σ u c₁ = σ v c₂

/-- Proper $m$-colorings of $G$. -/
def IsProperColoring (G : SimpleGraph V) {m : ℕ} (f : V → Fin m) : Prop :=
  ∀ u v, G.Adj u v → f u ≠ f v

/-- The chromatic polynomial $P(G, m)$ evaluated at $m \in \mathbb{N}$. -/
noncomputable def chromPoly [Fintype V] (G : SimpleGraph V) (m : ℕ) : ℕ := by
  classical exact Fintype.card { f : V → Fin m // IsProperColoring G f }

lemma chromPoly_eq_card [Fintype V] (G : SimpleGraph V) (m : ℕ)
    [Fintype { f : V → Fin m // IsProperColoring G f }] :
    chromPoly G m = Fintype.card { f : V → Fin m // IsProperColoring G f } := by
  classical
  unfold chromPoly
  convert rfl

lemma dpColorCount_canonical [Fintype V] (G : SimpleGraph V) (m : ℕ) :
    (FoldCover.canonical G m).dpColorCount = chromPoly G m := by
  classical
  rw [dpColorCount_eq_card_hColoring, chromPoly_eq_card]
  refine Fintype.card_congr (Equiv.subtypeEquivRight fun f => ?_)
  constructor
  · intro hf u v huv hEq
    exact hf u v huv (Or.inr ⟨huv, hEq⟩)
  · rintro hf u v huv (⟨heq, _⟩ | ⟨_, hEq⟩)
    · exact G.ne_of_adj huv heq
    · exact hf u v huv hEq

lemma dpColorCount_of_hasCanonicalLabeling [Fintype V] {C : FoldCover G m}
    (hcan : C.HasCanonicalLabeling) : C.dpColorCount = chromPoly G m := by
  classical
  rcases hcan with ⟨σ, hσ⟩
  rw [dpColorCount_eq_card_hColoring, chromPoly_eq_card]
  refine Fintype.card_congr
    { toFun := fun ⟨f, hf⟩ =>
        ⟨fun u => σ u (f u), fun u v huv hEq => hf u v huv ((hσ u v huv _ _).mpr hEq)⟩
      invFun := fun ⟨g, hg⟩ =>
        ⟨fun u => (σ u).symm (g u), fun u v huv hadj =>
          hg u v huv (by simpa using (hσ u v huv _ _).mp hadj)⟩
      left_inv := fun ⟨f, _⟩ => by apply Subtype.ext; funext u; simp
      right_inv := fun ⟨g, _⟩ => by apply Subtype.ext; funext u; simp }

/-- Transport a cover along a graph isomorphism. -/
def transport {V' : Type*} {G' : SimpleGraph V'} (e : G ≃g G') (C : FoldCover G' m) :
    FoldCover G m where
  H :=
    { Adj := fun x y => C.H.Adj (e x.1, x.2) (e y.1, y.2)
      symm := ⟨fun _ _ h => h.symm⟩
      loopless := ⟨fun _ h => C.H.loopless.irrefl _ h⟩ }
  clique_part := fun u c₁ c₂ hne => C.clique_part (e u) c₁ c₂ hne
  adj_subset := fun u v c₁ c₂ hadj => by
    rcases C.adj_subset (e u) (e v) c₁ c₂ hadj with h | h
    · exact Or.inl (e.injective h)
    · exact Or.inr (e.map_rel_iff.mp h)
  matching_right := fun u v c c₁ c₂ huv h1 h2 =>
    C.matching_right (e u) (e v) c c₁ c₂ (fun h => huv (e.injective h)) h1 h2

lemma dpColorCount_transport [Fintype V] {V' : Type*} [Fintype V'] {G' : SimpleGraph V'}
    (e : G ≃g G') (C : FoldCover G' m) :
    (C.transport e).dpColorCount = C.dpColorCount := by
  classical
  rw [dpColorCount_eq_card_hColoring, dpColorCount_eq_card_hColoring]
  refine Fintype.card_congr
    { toFun := fun ⟨f, hf⟩ =>
        ⟨fun v' => f (e.symm v'), fun u' v' huv' hadj =>
          hf (e.symm u') (e.symm v') (e.symm.map_rel_iff.mpr huv') (by simpa [transport] using hadj)⟩
      invFun := fun ⟨g, hg⟩ =>
        ⟨fun u => g (e u), fun u v huv hadj =>
          hg (e u) (e v) (e.map_rel_iff.mpr huv) hadj⟩
      left_inv := fun ⟨f, _⟩ => by apply Subtype.ext; funext u; simp
      right_inv := fun ⟨g, _⟩ => by apply Subtype.ext; funext v'; simp }

/-- Extend any partial matching on `Fin m × Fin m` to a permutation of `Fin m`. -/
private lemma exists_perm_extending_matching {m : ℕ} (R : Fin m → Fin m → Prop)
    (hR : ∀ a b₁ b₂, R a b₁ → R a b₂ → b₁ = b₂)
    (hL : ∀ a₁ a₂ b, R a₁ b → R a₂ b → a₁ = a₂) :
    ∃ π : Equiv.Perm (Fin m), ∀ a b, R a b → π a = b := by
  classical
  let A : Finset (Fin m) := Finset.univ.filter (fun a => ∃ b, R a b)
  let B : Finset (Fin m) := Finset.univ.filter (fun b => ∃ a, R a b)
  let fA : {a // a ∈ A} → {b // b ∈ B} := fun ⟨a, ha⟩ =>
    have hex : ∃ b, R a b := (Finset.mem_filter.mp ha).2
    ⟨Classical.choose hex, Finset.mem_filter.mpr ⟨Finset.mem_univ _, a, Classical.choose_spec hex⟩⟩
  have hfA_bij : Function.Bijective fA := by
    constructor
    · rintro ⟨a₁, ha₁⟩ ⟨a₂, ha₂⟩ hEq
      have hval : (fA ⟨a₁, ha₁⟩).1 = (fA ⟨a₂, ha₂⟩).1 := congrArg Subtype.val hEq
      have h1 : R a₁ (fA ⟨a₁, ha₁⟩).1 := Classical.choose_spec (Finset.mem_filter.mp ha₁).2
      have h2 : R a₂ (fA ⟨a₁, ha₁⟩).1 := hval ▸ Classical.choose_spec (Finset.mem_filter.mp ha₂).2
      exact Subtype.ext (hL a₁ a₂ _ h1 h2)
    · rintro ⟨b, hb⟩
      rcases (Finset.mem_filter.mp hb).2 with ⟨a, hab⟩
      have ha : a ∈ A := Finset.mem_filter.mpr ⟨Finset.mem_univ _, b, hab⟩
      refine ⟨⟨a, ha⟩, Subtype.ext ?_⟩
      exact hR a _ b (Classical.choose_spec (Finset.mem_filter.mp ha).2) hab
  let eAB : {a // a ∈ A} ≃ {b // b ∈ B} := Equiv.ofBijective fA hfA_bij
  have hcardAB : A.card = B.card := by
    simpa [Fintype.card_coe] using Fintype.card_congr eAB
  have hcardC : (Finset.univ \ A).card = (Finset.univ \ B).card := by
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ A),
      Finset.card_sdiff_of_subset (Finset.subset_univ B), hcardAB]
  let eC : {a // a ∈ Finset.univ \ A} ≃ {b // b ∈ Finset.univ \ B} :=
    Fintype.equivOfCardEq (by rw [Fintype.card_coe, Fintype.card_coe, hcardC])
  let g : Fin m → Fin m := fun a =>
    if ha : a ∈ A then (eAB ⟨a, ha⟩).1
    else (eC ⟨a, Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, ha⟩⟩).1
  have hg_inj : Function.Injective g := by
    intro a₁ a₂ hEq
    dsimp [g] at hEq
    split_ifs at hEq with h1 h2 h2
    · have : eAB ⟨a₁, h1⟩ = eAB ⟨a₂, h2⟩ := Subtype.ext hEq
      exact congrArg Subtype.val (eAB.injective this)
    · have hb1 : (eAB ⟨a₁, h1⟩).1 ∈ B := (eAB ⟨a₁, h1⟩).2
      have hb2 : (eC ⟨a₂, Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, h2⟩⟩).1 ∉ B :=
        (Finset.mem_sdiff.mp (eC _).2).2
      exact (hb2 (hEq ▸ hb1)).elim
    · have hb2 : (eAB ⟨a₂, h2⟩).1 ∈ B := (eAB ⟨a₂, h2⟩).2
      have hb1 : (eC ⟨a₁, Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, h1⟩⟩).1 ∉ B :=
        (Finset.mem_sdiff.mp (eC _).2).2
      exact (hb1 (hEq.symm ▸ hb2)).elim
    · have : eC ⟨a₁, Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, h1⟩⟩ =
          eC ⟨a₂, Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, h2⟩⟩ := Subtype.ext hEq
      exact congrArg Subtype.val (eC.injective this)
  refine ⟨Equiv.ofBijective g (Finite.injective_iff_bijective.mp hg_inj), ?_⟩
  intro a b hab
  have ha : a ∈ A := Finset.mem_filter.mpr ⟨Finset.mem_univ _, b, hab⟩
  change g a = b
  simp only [g, ha, ↓reduceDIte]
  exact hR a _ b (Classical.choose_spec (Finset.mem_filter.mp ha).2) hab

/-- Every $m$-fold cover can be completed to a *full* $m$-fold cover with no more colorings
(adding cross-edges cannot create independent sets). -/
lemma exists_full_le [Fintype V] (C : FoldCover G m) :
    ∃ C' : FoldCover G m, C'.IsFull ∧ C'.dpColorCount ≤ C.dpColorCount := by
  classical
  let permEdge : ∀ e : Sym2 V, Equiv.Perm (Fin m) := fun e =>
    if hne : (Quot.out e).1 ≠ (Quot.out e).2 then
      Classical.choose (exists_perm_extending_matching
        (fun c₁ c₂ => C.H.Adj ((Quot.out e).1, c₁) ((Quot.out e).2, c₂))
        (fun c c₁ c₂ => C.matching_right (Quot.out e).1 (Quot.out e).2 c c₁ c₂ hne)
        (fun c₁ c₂ c => C.matching_left hne))
    else Equiv.refl (Fin m)
  let adj' : (V × Fin m) → (V × Fin m) → Prop := fun x y =>
    (x.1 = y.1 ∧ x.2 ≠ y.2) ∨
    (G.Adj x.1 y.1 ∧
      if x.1 = (Quot.out (s(x.1, y.1))).1 ∧ y.1 = (Quot.out (s(x.1, y.1))).2
      then permEdge (s(x.1, y.1)) x.2 = y.2
      else permEdge (s(x.1, y.1)) y.2 = x.2)
  have hpair_cases : ∀ {u v : V}, G.Adj u v →
      (u = (Quot.out s(u, v)).1 ∧ v = (Quot.out s(u, v)).2) ∨
      (u = (Quot.out s(u, v)).2 ∧ v = (Quot.out s(u, v)).1) := by
    intro u v _huv
    have hq : s((Quot.out s(u, v)).1, (Quot.out s(u, v)).2) = s(u, v) := Quot.out_eq s(u, v)
    rcases Sym2.eq_iff.mp hq with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · exact Or.inl ⟨h1.symm, h2.symm⟩
    · exact Or.inr ⟨h2.symm, h1.symm⟩
  let hC' : FoldCover G m :=
    { H :=
        { Adj := adj'
          symm := ⟨by
            rintro ⟨u, c₁⟩ ⟨v, c₂⟩ (⟨rfl, hne⟩ | ⟨huv, hmatch⟩)
            · exact Or.inl ⟨rfl, hne.symm⟩
            · right
              refine ⟨huv.symm, ?_⟩
              have hsym : s(v, u) = s(u, v) := Sym2.eq_swap
              have hne : u ≠ v := G.ne_of_adj huv
              dsimp only at hmatch ⊢
              rw [hsym]
              split_ifs at hmatch ⊢ with h1 h2 h2
              · exact (hne (h2.1.trans h1.1.symm)).elim
              · exact hmatch
              · exact hmatch
              · rcases hpair_cases huv with hc | hc
                · exact (h2 hc).elim
                · exact (h1 ⟨hc.2, hc.1⟩).elim⟩
          loopless := ⟨by
            rintro ⟨u, c⟩ (⟨_, hne⟩ | ⟨huu, _⟩)
            · exact hne rfl
            · exact G.loopless.irrefl u huu⟩ }
      clique_part := fun u c₁ c₂ hne => Or.inl ⟨rfl, hne⟩
      adj_subset := by
        rintro u v c₁ c₂ (⟨h, _⟩ | ⟨h, _⟩)
        · exact Or.inl h
        · exact Or.inr h
      matching_right := by
        rintro u v c c₁ c₂ huv (⟨heq, _⟩ | ⟨hadj, hm1⟩) (⟨heq', _⟩ | ⟨_, hm2⟩)
        · exact (huv heq).elim
        · exact (huv heq).elim
        · exact (huv heq').elim
        · dsimp only at hm1 hm2
          split_ifs at hm1 hm2
          · exact hm1.symm.trans hm2
          · exact (permEdge s(u, v)).injective (hm1.trans hm2.symm) }
  refine ⟨hC', ?_, ?_⟩
  · intro u v huv c₁
    rcases hpair_cases huv with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · refine ⟨permEdge s(u, v) c₁, Or.inr ⟨huv, ?_⟩⟩
      dsimp only
      split_ifs with hc
      · rfl
      · exact (hc ⟨h1, h2⟩).elim
    · refine ⟨(permEdge s(u, v)).symm c₁, Or.inr ⟨huv, ?_⟩⟩
      have hne : u ≠ v := G.ne_of_adj huv
      dsimp only
      split_ifs with hc
      · exact (hne (hc.1.trans h2.symm)).elim
      · exact Equiv.apply_symm_apply _ _
  · rw [dpColorCount_eq_card_hColoring, dpColorCount_eq_card_hColoring]
    have hsub : ∀ f, hC'.IsHColoring f → C.IsHColoring f := by
      intro f hf u v huv hadj
      apply hf u v huv
      right
      refine ⟨huv, ?_⟩
      dsimp only
      have hne : u ≠ v := G.ne_of_adj huv
      split_ifs with hc
      · have hpne : (Quot.out s(u, v)).1 ≠ (Quot.out s(u, v)).2 := by rw [← hc.1, ← hc.2]; exact hne
        have hspec := Classical.choose_spec (exists_perm_extending_matching
          (fun c₁ c₂ => C.H.Adj ((Quot.out s(u, v)).1, c₁) ((Quot.out s(u, v)).2, c₂))
          (fun c c₁ c₂ => C.matching_right _ _ c c₁ c₂ hpne)
          (fun c₁ c₂ c => C.matching_left hpne))
        dsimp only [permEdge]
        split_ifs
        exact hspec (f u) (f v) (by rw [← hc.1, ← hc.2]; exact hadj)
      · rcases hpair_cases huv with ⟨h1, h2⟩ | ⟨h1, h2⟩
        · exact (hc ⟨h1, h2⟩).elim
        · have hpne : (Quot.out s(u, v)).1 ≠ (Quot.out s(u, v)).2 := by rw [← h1, ← h2]; exact hne.symm
          have hspec := Classical.choose_spec (exists_perm_extending_matching
            (fun c₁ c₂ => C.H.Adj ((Quot.out s(u, v)).1, c₁) ((Quot.out s(u, v)).2, c₂))
            (fun c c₁ c₂ => C.matching_right _ _ c c₁ c₂ hpne)
            (fun c₁ c₂ c => C.matching_left hpne))
          dsimp only [permEdge]
          split_ifs
          exact hspec (f v) (f u) (by rw [← h1, ← h2]; exact hadj.symm)
    exact Fintype.card_le_of_injective
      (fun x => ⟨x.1, hsub x.1 x.2⟩)
      (fun a b h => Subtype.ext (congrArg (fun z : { f : V → Fin m // C.IsHColoring f } => z.1) h))

end FoldCover

/-- The DP color function $P_{DP}(G, m) = \min_{\mathcal{H}} P_{DP}(G, \mathcal{H})$ over all
$m$-fold covers $\mathcal{H}$ of $G$. -/
noncomputable def dpColorFun {V : Type*} [Fintype V] (G : SimpleGraph V) (m : ℕ) : ℕ :=
  sInf { k : ℕ | ∃ C : FoldCover G m, C.dpColorCount = k }

lemma dpColorFun_le {V : Type*} [Fintype V] (G : SimpleGraph V) (m : ℕ) (C : FoldCover G m) :
    dpColorFun G m ≤ C.dpColorCount :=
  Nat.sInf_le ⟨C, rfl⟩

lemma dpColorFun_le_chromPoly {V : Type*} [Fintype V] (G : SimpleGraph V) (m : ℕ) :
    dpColorFun G m ≤ FoldCover.chromPoly G m := by
  rw [← FoldCover.dpColorCount_canonical]
  exact dpColorFun_le G m (FoldCover.canonical G m)

lemma exists_min_full_foldCover {V : Type*} [Fintype V] (G : SimpleGraph V) (m : ℕ) :
    ∃ C : FoldCover G m, C.IsFull ∧ C.dpColorCount = dpColorFun G m := by
  have hne : { k : ℕ | ∃ C : FoldCover G m, C.dpColorCount = k }.Nonempty :=
    ⟨(FoldCover.canonical G m).dpColorCount, FoldCover.canonical G m, rfl⟩
  rcases Nat.sInf_mem hne with ⟨C, hC⟩
  rcases C.exists_full_le with ⟨C', hfull, hle⟩
  exact ⟨C', hfull, le_antisymm (by unfold dpColorFun; rw [← hC]; exact hle) (dpColorFun_le G m C')⟩

lemma dpColorFun_congr {V V' : Type*} [Fintype V] [Fintype V']
    {G : SimpleGraph V} {G' : SimpleGraph V'} (e : G ≃g G') (m : ℕ) :
    dpColorFun G m = dpColorFun G' m := by
  apply le_antisymm
  · rcases exists_min_full_foldCover G' m with ⟨C', _, hC'⟩
    rw [← hC', ← C'.dpColorCount_transport e]
    exact dpColorFun_le G m (C'.transport e)
  · rcases exists_min_full_foldCover G m with ⟨C, _, hC⟩
    rw [← hC, ← C.dpColorCount_transport e.symm]
    exact dpColorFun_le G' m (C.transport e.symm)

/-- A vertex $v \in V(G)$ is *simplicial* if its neighborhood induces a clique in $G$
(vacuously true when $d_G(v) = 0$). -/
def IsSimplicial {V : Type*} (G : SimpleGraph V) (v : V) : Prop :=
  ∀ x y, G.Adj v x → G.Adj v y → x ≠ y → G.Adj x y

/-- Degree of a vertex $v$ in a finite simple graph $G$. -/
noncomputable def vertexDeg {V : Type*} [Fintype V] (G : SimpleGraph V) (v : V) : ℕ := by
  classical exact (Finset.univ.filter (fun u => G.Adj v u)).card

/-- $G \in G_1 \oplus_p G_2$: $G$ is a $K_p$-gluing of $G_1$ and $G_2$ along a shared $p$-clique
$S_1 \cap S_2$ with no edges between $S_1 \setminus S_2$ and $S_2 \setminus S_1$. -/
def IsCliqueGluing2 (p : ℕ) {V₁ V₂ V : Type*} [Fintype V] [DecidableEq V]
    (G₁ : SimpleGraph V₁) (G₂ : SimpleGraph V₂) (G : SimpleGraph V) : Prop :=
  ∃ S₁ S₂ : Finset V,
    S₁ ∪ S₂ = Finset.univ ∧
    (S₁ ∩ S₂).card = p ∧
    (∀ x ∈ S₁ ∩ S₂, ∀ y ∈ S₁ ∩ S₂, x ≠ y → G.Adj x y) ∧
    (∀ x ∈ S₁, ∀ y ∈ S₂, G.Adj x y → x ∈ S₁ ∩ S₂ ∨ y ∈ S₁ ∩ S₂) ∧
    Nonempty (G.induce (S₁ : Set V) ≃g G₁) ∧
    Nonempty (G.induce (S₂ : Set V) ≃g G₂)

/-! ## Section 2: Lemma 1 — DP Color Function of Complete Graphs $K_{p+1}$ -/

open Classical in
/-- Helper: in any $m$-fold cover of $G$, a finite set $S$ of vertices with chosen colors forbids
at most $|S|$ colors at any vertex $v \notin S$. -/
private lemma card_forbidden_le {V : Type*} [DecidableEq V] {G : SimpleGraph V} {m : ℕ}
    (C : FoldCover G m) (S : Finset V) (v : V) (hv : v ∉ S) (f : V → Fin m) :
    (Finset.univ.filter (fun c : Fin m => ∃ x ∈ S, C.H.Adj (x, f x) (v, c))).card ≤ S.card := by
  classical
  have hsub : Finset.univ.filter (fun c : Fin m => ∃ x ∈ S, C.H.Adj (x, f x) (v, c)) ⊆
      S.biUnion (fun x => Finset.univ.filter (fun c : Fin m => C.H.Adj (x, f x) (v, c))) := by
    intro c hc
    rcases (Finset.mem_filter.mp hc).2 with ⟨x, hx, hadj⟩
    exact Finset.mem_biUnion.mpr ⟨x, hx, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hadj⟩⟩
  calc
    (Finset.univ.filter (fun c : Fin m => ∃ x ∈ S, C.H.Adj (x, f x) (v, c))).card
        ≤ (S.biUnion (fun x => Finset.univ.filter (fun c : Fin m => C.H.Adj (x, f x) (v, c)))).card :=
      Finset.card_le_card hsub
    _ ≤ ∑ x ∈ S, (Finset.univ.filter (fun c : Fin m => C.H.Adj (x, f x) (v, c))).card :=
      Finset.card_biUnion_le
    _ ≤ ∑ _x ∈ S, 1 := by
      refine Finset.sum_le_sum fun x hx => Finset.card_le_one.mpr ?_
      intro c₁ hc₁ c₂ hc₂
      have hne : x ≠ v := fun h => hv (h ▸ hx)
      exact C.matching_right x v (f x) c₁ c₂ hne
        (Finset.mem_filter.mp hc₁).2 (Finset.mem_filter.mp hc₂).2
    _ = S.card := by simp

private lemma descFactorial_le_dpColorCount_top :
    ∀ (n m : ℕ) (C : FoldCover (⊤ : SimpleGraph (Fin n)) m),
      m.descFactorial n ≤ C.dpColorCount := by
  intro n
  induction n with
  | zero =>
    intro m C
    classical
    rw [FoldCover.dpColorCount_eq_card_hColoring, Nat.descFactorial_zero]
    have : Nonempty { f : Fin 0 → Fin m // C.IsHColoring f } :=
      ⟨⟨Fin.elim0, fun u => Fin.elim0 u⟩⟩
    exact Fintype.card_pos
  | succ n ih =>
    intro m C
    classical
    rw [FoldCover.dpColorCount_eq_card_hColoring]
    -- Restrict cover `C` to `Fin n` via `Fin.castSucc`
    let C' : FoldCover (⊤ : SimpleGraph (Fin n)) m :=
      { H :=
          { Adj := fun x y => C.H.Adj (x.1.castSucc, x.2) (y.1.castSucc, y.2)
            symm := ⟨fun _ _ h => h.symm⟩
            loopless := ⟨fun _ h => C.H.loopless.irrefl _ h⟩ }
        clique_part := fun u c₁ c₂ hne => C.clique_part u.castSucc c₁ c₂ hne
        adj_subset := fun u v c₁ c₂ hadj => by
          rcases C.adj_subset u.castSucc v.castSucc c₁ c₂ hadj with h | h
          · exact Or.inl (Fin.castSucc_injective n h)
          · exact Or.inr (fun heq => h (congrArg Fin.castSucc heq))
        matching_right := fun u v c c₁ c₂ huv h1 h2 =>
          C.matching_right u.castSucc v.castSucc c c₁ c₂
            (fun h => huv (Fin.castSucc_injective n h)) h1 h2 }
    let avail : { f : Fin n → Fin m // C'.IsHColoring f } → Finset (Fin m) := fun f =>
      Finset.univ.filter (fun c => ∀ i : Fin n, ¬ C.H.Adj (i.castSucc, f.1 i) (Fin.last n, c))
    let e : { g : Fin (n + 1) → Fin m // C.IsHColoring g } ≃
        Σ f : { f : Fin n → Fin m // C'.IsHColoring f }, { c : Fin m // c ∈ avail f } :=
      { toFun := fun ⟨g, hg⟩ =>
          ⟨⟨fun i => g i.castSucc, fun u v huv hadj =>
              hg u.castSucc v.castSucc (fun h => huv (Fin.castSucc_injective n h)) hadj⟩,
            ⟨g (Fin.last n), Finset.mem_filter.mpr ⟨Finset.mem_univ _, fun i =>
              hg i.castSucc (Fin.last n) (Fin.castSucc_lt_last i).ne⟩⟩⟩
        invFun := fun ⟨⟨f, hf⟩, ⟨c, hc⟩⟩ =>
          ⟨Fin.snoc f c, by
            intro u
            refine Fin.lastCases ?_ (fun i => ?_) u
            · intro v
              refine Fin.lastCases ?_ (fun j => ?_) v
              · intro huv _; exact huv rfl
              · intro _ hadj
                simp only [Fin.snoc_last, Fin.snoc_castSucc] at hadj
                exact (Finset.mem_filter.mp hc).2 j hadj.symm
            · intro v
              refine Fin.lastCases ?_ (fun j => ?_) v
              · intro _ hadj
                simp only [Fin.snoc_last, Fin.snoc_castSucc] at hadj
                exact (Finset.mem_filter.mp hc).2 i hadj
              · intro huv hadj
                simp only [Fin.snoc_castSucc] at hadj
                exact hf i j (fun h => huv (congrArg Fin.castSucc h)) hadj⟩
        left_inv := fun ⟨g, _⟩ => by
          apply Subtype.ext
          funext u
          refine Fin.lastCases ?_ (fun i => ?_) u <;> simp
        right_inv := fun ⟨⟨f, hf⟩, ⟨c, hc⟩⟩ => by
          have hf_eq : (⟨fun i => Fin.snoc (α := fun _ => Fin m) f c i.castSucc, by
              intro u v huv hadj
              simp only [Fin.snoc_castSucc] at hadj
              exact hf u v huv hadj⟩ : { f : Fin n → Fin m // C'.IsHColoring f }) = ⟨f, hf⟩ := by
            apply Subtype.ext; funext i; simp [Fin.snoc_castSucc]
          refine Sigma.ext hf_eq ?_
          refine (Subtype.heq_iff_coe_eq (fun x => ?_)).mpr (by simp [Fin.snoc_last])
          simp [avail] }
    have hcard_eq : Fintype.card { g : Fin (n + 1) → Fin m // C.IsHColoring g } =
        ∑ f : { f : Fin n → Fin m // C'.IsHColoring f }, (avail f).card := by
      rw [Fintype.card_congr e, Fintype.card_sigma]
      simp [Fintype.card_coe]
    have havail_ge : ∀ f, m - n ≤ (avail f).card := by
      intro f
      let S : Finset (Fin (n + 1)) := Finset.univ.image Fin.castSucc
      have hv_not : Fin.last n ∉ S := by
        simp only [S, Finset.mem_image, Finset.mem_univ, true_and, not_exists]
        exact fun i => (Fin.castSucc_lt_last i).ne
      have hScard : S.card = n := by
        rw [Finset.card_image_of_injective _ (Fin.castSucc_injective n), Finset.card_univ, Fintype.card_fin]
      by_cases hm : n < m
      · have hpos : 0 < m := by omega
        let fExt' : Fin (n + 1) → Fin m := Fin.snoc f.1 ⟨0, hpos⟩
        let forb : Finset (Fin m) :=
          Finset.univ.filter (fun c => ∃ x ∈ S, C.H.Adj (x, fExt' x) (Fin.last n, c))
        have hforb_le : forb.card ≤ n := by
          convert le_trans (card_forbidden_le C S (Fin.last n) hv_not fExt') hScard.le
        have hsub : Finset.univ \ forb ⊆ avail f := by
          intro c hc
          have hnot : c ∉ forb := (Finset.mem_sdiff.mp hc).2
          refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, fun i hadj => hnot ?_⟩
          refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, i.castSucc,
            Finset.mem_image.mpr ⟨i, Finset.mem_univ _, rfl⟩, ?_⟩
          simpa [fExt'] using hadj
        have hsdiff : (Finset.univ \ forb).card = m - forb.card := by
          rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ, Fintype.card_fin]
        have hle := Finset.card_le_card hsub
        omega
      · omega
    have hih := ih m C'
    rw [FoldCover.dpColorCount_eq_card_hColoring] at hih
    calc
      m.descFactorial (n + 1) = (m - n) * m.descFactorial n := Nat.descFactorial_succ m n
      _ ≤ (m - n) * Fintype.card { f : Fin n → Fin m // C'.IsHColoring f } :=
        Nat.mul_le_mul_left _ hih
      _ = ∑ _f : { f : Fin n → Fin m // C'.IsHColoring f }, (m - n) := by
        rw [Finset.sum_const, Finset.card_univ, smul_eq_mul, mul_comm]
      _ ≤ ∑ f : { f : Fin n → Fin m // C'.IsHColoring f }, (avail f).card :=
        Finset.sum_le_sum fun f _ => havail_ge f
      _ = Fintype.card { g : Fin (n + 1) → Fin m // C.IsHColoring g } := hcard_eq.symm

/-- **Lemma 1:** For every $n \in \mathbb{N}$, $P_{DP}(K_n, n) = n!$. -/
theorem dpColorFun_top_eq_factorial (n : ℕ) :
    dpColorFun (⊤ : SimpleGraph (Fin n)) n = n.factorial := by
  apply le_antisymm
  · refine le_trans (dpColorFun_le_chromPoly _ _) ?_
    classical
    rw [FoldCover.chromPoly_eq_card]
    have e : { f : Fin n → Fin n // FoldCover.IsProperColoring (⊤ : SimpleGraph (Fin n)) f } ≃
        (Fin n ↪ Fin n) :=
      { toFun := fun ⟨f, hf⟩ =>
          ⟨f, fun a b hEq => by
            by_contra hne
            exact hf a b hne hEq⟩
        invFun := fun g => ⟨g, fun a b hne hEq => hne (g.injective hEq)⟩
        left_inv := fun _ => rfl
        right_inv := fun _ => rfl }
    rw [Fintype.card_congr e, Fintype.card_embedding_eq, Fintype.card_fin, Nat.descFactorial_self]
  · rcases exists_min_full_foldCover (⊤ : SimpleGraph (Fin n)) n with ⟨C, _, hC⟩
    rw [← hC, ← Nat.descFactorial_self]
    exact descFactorial_le_dpColorCount_top n n C

/-! ## Section 3: Base Graph $G_0^{(p)} = K_{p-2} \vee K_{2,p}$ and Iterated Clique-Gluings $G_k^{(p)}$ -/

/-- Vertex set of $G_0^{(p)} = K_{p-2} \vee K_{2,p}$:
- `Sum.inl w`: vertex $w \in W$ ($|W| = p - 2$),
- `Sum.inr (Sum.inl i)`: vertex $v_i \in V$ ($|V| = 2$),
- `Sum.inr (Sum.inr j)`: vertex $u_j \in U$ ($|U| = p$). -/
abbrev V0 (p : ℕ) : Type := Fin (p - 2) ⊕ (Fin 2 ⊕ Fin p)

/-- Adjacency relation of $G_0^{(p)} = K_{p-2} \vee K_{2,p}$. -/
def G0Adj (p : ℕ) : V0 p → V0 p → Prop
  | Sum.inl w₁, Sum.inl w₂ => w₁ ≠ w₂
  | Sum.inl _, Sum.inr _ => True
  | Sum.inr _, Sum.inl _ => True
  | Sum.inr (Sum.inl _), Sum.inr (Sum.inr _) => True
  | Sum.inr (Sum.inr _), Sum.inr (Sum.inl _) => True
  | _, _ => False

/-- The base graph $G_0^{(p)} = K_{p-2} \vee K_{2,p}$. -/
def G0 (p : ℕ) : SimpleGraph (V0 p) where
  Adj := G0Adj p
  symm := ⟨by
    rintro (w₁ | (i₁ | j₁)) (w₂ | (i₂ | j₂)) h <;> simp [G0Adj] at h ⊢
    exact Ne.symm h⟩
  loopless := ⟨by
    rintro (w | (i | j)) h <;> simp [G0Adj] at h⟩

/-- Membership in the $r$-th $p$-clique $K_r = W \cup \{v_{r/p}, u_{r \bmod p}\}$ of $G_0^{(p)}$
($0 \le r < 2p$). -/
def inKp (p r : ℕ) : V0 p → Prop
  | Sum.inl _ => True
  | Sum.inr (Sum.inl i) => i.val = r / p
  | Sum.inr (Sum.inr j) => j.val = r % p

instance instDecidableInKp (p r : ℕ) : DecidablePred (inKp p r) := fun x => by
  cases x with
  | inl _ => exact isTrue trivial
  | inr y => cases y with
    | inl i => exact inferInstanceAs (Decidable (i.val = r / p))
    | inr j => exact inferInstanceAs (Decidable (j.val = r % p))

/-- The $k$-th graph $G_k^{(p)}$ ($0 \le k \le 2p$), obtained from $G_0^{(p)}$ by attaching
simplicial vertices $d_0, \dots, d_{k-1}$ adjacent to $K_0, \dots, K_{k-1}$ respectively. -/
def Gk (p k : ℕ) : SimpleGraph (V0 p ⊕ Fin k) where
  Adj := fun x y =>
    match x, y with
    | Sum.inl a, Sum.inl b => (G0 p).Adj a b
    | Sum.inl a, Sum.inr r => inKp p r.val a
    | Sum.inr r, Sum.inl a => inKp p r.val a
    | Sum.inr _, Sum.inr _ => False
  symm := ⟨by
    rintro (a | r) (b | s) h
    · exact h.symm
    · exact h
    · exact h
    · exact h⟩
  loopless := ⟨by
    rintro (a | r) h
    · exact (G0 p).loopless.irrefl a h
    · exact h⟩

private lemma inKp_clique {p r : ℕ} {x y : V0 p} (hx : inKp p r x) (hy : inKp p r y)
    (hne : x ≠ y) : (G0 p).Adj x y := by
  rcases x with w₁ | (i₁ | j₁) <;> rcases y with w₂ | (i₂ | j₂)
  · exact fun h => hne (congrArg Sum.inl h)
  · trivial
  · trivial
  · trivial
  · exact (hne (by simp [inKp] at hx hy; exact congrArg (Sum.inr ∘ Sum.inl) (Fin.ext (hx.trans hy.symm)))).elim
  · trivial
  · trivial
  · trivial
  · exact (hne (by simp [inKp] at hx hy; exact congrArg (Sum.inr ∘ Sum.inr) (Fin.ext (hx.trans hy.symm)))).elim

private lemma card_inKp {p r : ℕ} (hp : 3 ≤ p) (hr : r < 2 * p) :
    (Finset.univ.filter (fun x : V0 p => inKp p r x)).card = p := by
  classical
  have hi : r / p < 2 := Nat.div_lt_of_lt_mul (by omega)
  have hj : r % p < p := Nat.mod_lt r (by omega)
  let e : { x : V0 p // inKp p r x } ≃ Fin (p - 2) ⊕ (Unit ⊕ Unit) :=
    { toFun := fun ⟨x, hx⟩ =>
        match x with
        | Sum.inl w => Sum.inl w
        | Sum.inr (Sum.inl _) => Sum.inr (Sum.inl ())
        | Sum.inr (Sum.inr _) => Sum.inr (Sum.inr ())
      invFun := fun y =>
        match y with
        | Sum.inl w => ⟨Sum.inl w, trivial⟩
        | Sum.inr (Sum.inl ()) => ⟨Sum.inr (Sum.inl ⟨r / p, hi⟩), rfl⟩
        | Sum.inr (Sum.inr ()) => ⟨Sum.inr (Sum.inr ⟨r % p, hj⟩), rfl⟩
      left_inv := by
        rintro ⟨w | (i | j), hx⟩
        · rfl
        · apply Subtype.ext; dsimp [inKp] at hx; exact congrArg (Sum.inr ∘ Sum.inl) (Fin.ext hx.symm)
        · apply Subtype.ext; dsimp [inKp] at hx; exact congrArg (Sum.inr ∘ Sum.inr) (Fin.ext hx.symm)
      right_inv := by rintro (w | (⟨⟩ | ⟨⟩)) <;> rfl }
  have h1 : (Finset.univ.filter (fun x : V0 p => inKp p r x)).card =
      Fintype.card { x : V0 p // inKp p r x } := by
    rw [Fintype.card_subtype]
  rw [h1, Fintype.card_congr e]
  simp only [Fintype.card_sum, Fintype.card_fin, Fintype.card_unit]
  omega

private lemma exists_clique_containing_edge {p : ℕ} (hp : 3 ≤ p) {x y : V0 p}
    (hadj : (G0 p).Adj x y) : ∃ r : Fin (2 * p), inKp p r.val x ∧ inKp p r.val y := by
  have hp0 : 0 < p := by omega
  rcases x with w₁ | (i₁ | j₁) <;> rcases y with w₂ | (i₂ | j₂)
  · exact ⟨⟨0, by omega⟩, trivial, trivial⟩
  · refine ⟨⟨i₂.val * p, by have := i₂.isLt; nlinarith⟩, trivial, ?_⟩
    simp [inKp, Nat.mul_div_cancel _ hp0]
  · refine ⟨⟨j₂.val, by have := j₂.isLt; omega⟩, trivial, ?_⟩
    simp [inKp, Nat.mod_eq_of_lt j₂.isLt]
  · refine ⟨⟨i₁.val * p, by have := i₁.isLt; nlinarith⟩, ?_, trivial⟩
    simp [inKp, Nat.mul_div_cancel _ hp0]
  · exact hadj.elim
  · refine ⟨⟨i₁.val * p + j₂.val, by have := i₁.isLt; have := j₂.isLt; nlinarith⟩, ?_, ?_⟩
    · simp only [inKp]
      rw [Nat.add_comm, Nat.add_mul_div_right _ _ hp0, Nat.div_eq_of_lt j₂.isLt, zero_add]
    · simp only [inKp]
      rw [Nat.add_comm, Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt j₂.isLt]
  · refine ⟨⟨j₁.val, by have := j₁.isLt; omega⟩, ?_, trivial⟩
    simp [inKp, Nat.mod_eq_of_lt j₁.isLt]
  · refine ⟨⟨i₂.val * p + j₁.val, by have := i₂.isLt; have := j₁.isLt; nlinarith⟩, ?_, ?_⟩
    · simp only [inKp]
      rw [Nat.add_comm, Nat.add_mul_mod_self_right, Nat.mod_eq_of_lt j₁.isLt]
    · simp only [inKp]
      rw [Nat.add_comm, Nat.add_mul_div_right _ _ hp0, Nat.div_eq_of_lt j₁.isLt, zero_add]
  · exact hadj.elim

private def GkZeroIso (p : ℕ) : Gk p 0 ≃g G0 p where
  toEquiv :=
    { toFun := fun x => match x with | Sum.inl a => a | Sum.inr r => Fin.elim0 r
      invFun := Sum.inl
      left_inv := fun x => match x with | Sum.inl _ => rfl | Sum.inr r => Fin.elim0 r
      right_inv := fun _ => rfl }
  map_rel_iff' := by
    rintro (a | r) (b | s)
    · rfl
    · exact Fin.elim0 s
    · exact Fin.elim0 r
    · exact Fin.elim0 r

private lemma last_isSimplicial {p k : ℕ} :
    IsSimplicial (Gk p (k + 1)) (Sum.inr (Fin.last k)) := by
  rintro (a | r) (b | s) ha hb hne
  · exact inKp_clique ha hb (fun h => hne (congrArg Sum.inl h))
  · exact hb.elim
  · exact ha.elim
  · exact ha.elim

private lemma vertexDeg_last {p k : ℕ} (hp : 3 ≤ p) (hk : k < 2 * p) :
    vertexDeg (Gk p (k + 1)) (Sum.inr (Fin.last k)) = p := by
  classical
  unfold vertexDeg
  have hEq : Finset.univ.filter (fun u : V0 p ⊕ Fin (k + 1) => (Gk p (k + 1)).Adj (Sum.inr (Fin.last k)) u) =
      (Finset.univ.filter (fun x : V0 p => inKp p k x)).image Sum.inl := by
    ext (a | r)
    · simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image,
        Sum.inl.injEq, exists_eq_right]
      rfl
    · simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image,
        reduceCtorEq, and_false, exists_false]
      rfl
  rw [hEq, Finset.card_image_of_injective _ Sum.inl_injective]
  exact card_inKp hp hk

private def GkSuccDeleteIso (p k : ℕ) :
    (Gk p (k + 1)).induce { u : V0 p ⊕ Fin (k + 1) | u ≠ Sum.inr (Fin.last k) } ≃g Gk p k where
  toEquiv :=
    { toFun := fun ⟨u, hu⟩ =>
        match u with
        | Sum.inl a => Sum.inl a
        | Sum.inr r =>
          Sum.inr ⟨r.val, by
            have hlt := r.isLt
            have hne : r ≠ Fin.last k := fun h => hu (congrArg Sum.inr h)
            have hval : r.val ≠ k := fun h => hne (Fin.ext h)
            omega⟩
      invFun := fun u =>
        match u with
        | Sum.inl a => ⟨Sum.inl a, by simp⟩
        | Sum.inr r => ⟨Sum.inr r.castSucc, fun h =>
            (Fin.castSucc_lt_last r).ne (Sum.inr.inj h)⟩
      left_inv := by
        rintro ⟨a | r, hu⟩
        · rfl
        · apply Subtype.ext; apply congrArg Sum.inr; exact Fin.ext rfl
      right_inv := by
        rintro (a | r)
        · rfl
        · apply congrArg Sum.inr; exact Fin.ext rfl }
  map_rel_iff' := by
    rintro ⟨a | r, ha⟩ ⟨b | s, hb⟩ <;> rfl

private lemma Gk_isCliqueGluing2 {p k : ℕ} (hp : 3 ≤ p) (hk : k < 2 * p) :
    IsCliqueGluing2 p (Gk p k) (⊤ : SimpleGraph (Fin (p + 1))) (Gk p (k + 1)) := by
  classical
  let d : V0 p ⊕ Fin (k + 1) := Sum.inr (Fin.last k)
  let K : Finset (V0 p ⊕ Fin (k + 1)) :=
    (Finset.univ.filter (fun x : V0 p => inKp p k x)).image Sum.inl
  let S₁ : Finset (V0 p ⊕ Fin (k + 1)) := Finset.univ.erase d
  let S₂ : Finset (V0 p ⊕ Fin (k + 1)) := insert d K
  have hd_not_K : d ∉ K := by simp [d, K]
  have hK_sub_S₁ : K ⊆ S₁ := by
    intro u hu
    refine Finset.mem_erase.mpr ⟨fun h => hd_not_K (h ▸ hu), Finset.mem_univ _⟩
  have hInter : S₁ ∩ S₂ = K := by
    ext u
    simp only [Finset.mem_inter, S₁, S₂, Finset.mem_erase, Finset.mem_univ, and_true,
      Finset.mem_insert]
    constructor
    · rintro ⟨hne, rfl | hu⟩
      · exact (hne rfl).elim
      · exact hu
    · intro hu
      exact ⟨fun h => hd_not_K (h ▸ hu), Or.inr hu⟩
  have hKcard : K.card = p := by
    rw [Finset.card_image_of_injective _ Sum.inl_injective]
    exact card_inKp hp hk
  refine ⟨S₁, S₂, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext u
    simp only [Finset.mem_union, S₁, S₂, Finset.mem_erase, Finset.mem_univ, and_true,
      Finset.mem_insert, iff_true]
    by_cases h : u = d
    · exact Or.inr (Or.inl h)
    · exact Or.inl h
  · rw [hInter]; exact hKcard
  · rw [hInter]
    intro x hx y hy hne
    rcases Finset.mem_image.mp hx with ⟨a, ha, rfl⟩
    rcases Finset.mem_image.mp hy with ⟨b, hb, rfl⟩
    exact inKp_clique (Finset.mem_filter.mp ha).2 (Finset.mem_filter.mp hb).2
      (fun h => hne (congrArg Sum.inl h))
  · intro x hx y hy hadj
    rw [hInter]
    rcases Finset.mem_insert.mp hy with rfl | hyK
    · left
      rcases x with a | r
      · exact Finset.mem_image.mpr ⟨a, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hadj⟩, rfl⟩
      · exact hadj.elim
    · exact Or.inr hyK
  · have hset : (S₁ : Set (V0 p ⊕ Fin (k + 1))) = { u | u ≠ d } := by
      ext u; simp [S₁]
    rw [hset]
    exact ⟨GkSuccDeleteIso p k⟩
  · have hS₂card : S₂.card = p + 1 := by
      rw [Finset.card_insert_of_notMem hd_not_K, hKcard]
    let e : { u : V0 p ⊕ Fin (k + 1) // u ∈ (S₂ : Set (V0 p ⊕ Fin (k + 1))) } ≃ Fin (p + 1) :=
      Fintype.equivOfCardEq (by simpa [Fintype.card_coe] using hS₂card)
    refine ⟨{ toEquiv := e, map_rel_iff' := ?_ }⟩
    rintro ⟨x, hx⟩ ⟨y, hy⟩
    change e ⟨x, hx⟩ ≠ e ⟨y, hy⟩ ↔ (Gk p (k + 1)).Adj x y
    rw [ne_eq, e.injective.eq_iff, Subtype.mk.injEq]
    constructor
    · intro hne
      rcases Finset.mem_insert.mp hx with rfl | hxK <;>
      rcases Finset.mem_insert.mp hy with rfl | hyK
      · exact (hne rfl).elim
      · rcases Finset.mem_image.mp hyK with ⟨b, hb, rfl⟩
        exact (Finset.mem_filter.mp hb).2
      · rcases Finset.mem_image.mp hxK with ⟨a, ha, rfl⟩
        exact (Finset.mem_filter.mp ha).2
      · rcases Finset.mem_image.mp hxK with ⟨a, ha, rfl⟩
        rcases Finset.mem_image.mp hyK with ⟨b, hb, rfl⟩
        exact inKp_clique (Finset.mem_filter.mp ha).2 (Finset.mem_filter.mp hb).2
          (fun h => hne (congrArg Sum.inl h))
    · intro hadj hEq
      exact (Gk p (k + 1)).loopless.irrefl x (hEq ▸ hadj)

/-! ## Section 4: Lemma 2 — $P_{DP}(G_0^{(p)}, p+1) < P(G_0^{(p)}, p+1)$ via a Single Twisted Edge -/

/-- The transposition $\tau = (0\,1) \in S_{p+1}$ (for $p \ge 3$). -/
private def swap01 (p : ℕ) (hp : 3 ≤ p) : Equiv.Perm (Fin (p + 1)) :=
  Equiv.swap ⟨0, by omega⟩ ⟨1, by omega⟩

private lemma swap01_apply_zero {p : ℕ} (hp : 3 ≤ p) :
    swap01 p hp ⟨0, by omega⟩ = ⟨1, by omega⟩ :=
  Equiv.swap_apply_left _ _

private lemma swap01_apply_one {p : ℕ} (hp : 3 ≤ p) :
    swap01 p hp ⟨1, by omega⟩ = ⟨0, by omega⟩ :=
  Equiv.swap_apply_right _ _

private lemma swap01_apply_of_ne {p : ℕ} (hp : 3 ≤ p) {c : Fin (p + 1)}
    (h0 : c ≠ ⟨0, by omega⟩) (h1 : c ≠ ⟨1, by omega⟩) :
    swap01 p hp c = c :=
  Equiv.swap_apply_of_ne_of_ne h0 h1

/-- The distinguished edge $v_0 u_0$ of $G_0^{(p)}$. -/
private def isTwistedEdge (p : ℕ) (hp : 3 ≤ p) (x y : V0 p) : Prop :=
  (x = Sum.inr (Sum.inl 0) ∧ y = Sum.inr (Sum.inr ⟨0, by omega⟩)) ∨
  (y = Sum.inr (Sum.inl 0) ∧ x = Sum.inr (Sum.inr ⟨0, by omega⟩))

open Classical in
/-- The full $(p+1)$-fold cover $\mathcal{H}_{\mathrm{twist}}$ of $G_0^{(p)}$ obtained from the
canonical cover by transposing colors $0$ and $1$ across the single edge $v_0 u_0$. -/
private noncomputable def twistedCover (p : ℕ) (hp : 3 ≤ p) : FoldCover (G0 p) (p + 1) where
  H :=
    { Adj := fun x y =>
        (x.1 = y.1 ∧ x.2 ≠ y.2) ∨
        ((G0 p).Adj x.1 y.1 ∧
          if isTwistedEdge p hp x.1 y.1 then swap01 p hp x.2 = y.2 else x.2 = y.2)
      symm := ⟨by
        rintro ⟨u, c₁⟩ ⟨v, c₂⟩ (⟨rfl, hne⟩ | ⟨huv, hmatch⟩)
        · exact Or.inl ⟨rfl, hne.symm⟩
        · right
          refine ⟨huv.symm, ?_⟩
          have hsym : isTwistedEdge p hp v u ↔ isTwistedEdge p hp u v := by
            unfold isTwistedEdge; tauto
          by_cases ht : isTwistedEdge p hp u v
          · have htv : isTwistedEdge p hp v u := hsym.mpr ht
            simp only [ht, ↓reduceIte] at hmatch
            simp only [htv, ↓reduceIte]
            rw [← hmatch]
            exact Equiv.swap_apply_self _ _ _
          · have htv : ¬ isTwistedEdge p hp v u := fun h => ht (hsym.mp h)
            simp only [ht, ↓reduceIte] at hmatch
            simp only [htv, ↓reduceIte]
            exact hmatch.symm⟩
      loopless := ⟨by
        rintro ⟨u, c⟩ (⟨_, hne⟩ | ⟨huu, _⟩)
        · exact hne rfl
        · exact (G0 p).loopless.irrefl u huu⟩ }
  clique_part := fun u c₁ c₂ hne => Or.inl ⟨rfl, hne⟩
  adj_subset := by
    rintro u v c₁ c₂ (⟨h, _⟩ | ⟨h, _⟩)
    · exact Or.inl h
    · exact Or.inr h
  matching_right := by
    rintro u v c c₁ c₂ huv (⟨heq, _⟩ | ⟨_, hm1⟩) (⟨heq', _⟩ | ⟨_, hm2⟩)
    · exact (huv heq).elim
    · exact (huv heq).elim
    · exact (huv heq').elim
    · split_ifs at hm1 hm2
      · exact hm1.symm.trans hm2
      · exact hm1.symm.trans hm2

/-- Canonical count of $K_{2,p}$-colorings using colors from a subset $S \subseteq \mathrm{Fin}(p+1)$. -/
private def countCanon (p : ℕ) (S : Finset (Fin (p + 1))) : ℕ :=
  ∑ c₀ ∈ S, ∑ c₁ ∈ S, ((S.erase c₀).erase c₁).card ^ p

/-- Twisted count of $K_{2,p}$-colorings using colors from $S \subseteq \mathrm{Fin}(p+1)$ under
$\mathcal{H}_{\mathrm{twist}}$. -/
private def countTwist (p : ℕ) (hp : 3 ≤ p) (S : Finset (Fin (p + 1))) : ℕ :=
  ∑ c₀ ∈ S, ∑ c₁ ∈ S,
    ((S.erase c₀).erase c₁).card ^ (p - 1) * ((S.erase (swap01 p hp c₀)).erase c₁).card

/-- Remaining 3-element color set after coloring the $(p-2)$-clique $W$. -/
private def availSet {p : ℕ} (fW : Fin (p - 2) ↪ Fin (p + 1)) : Finset (Fin (p + 1)) :=
  Finset.univ \ Finset.univ.image fW

private lemma card_availSet {p : ℕ} (hp : 3 ≤ p) (fW : Fin (p - 2) ↪ Fin (p + 1)) :
    (availSet fW).card = 3 := by
  unfold availSet
  rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ, Fintype.card_fin,
    Finset.card_image_of_injective _ fW.injective, Finset.card_univ, Fintype.card_fin]
  omega

private lemma chromPoly_G0_eq_sum {p : ℕ} (_hp : 3 ≤ p) :
    FoldCover.chromPoly (G0 p) (p + 1) =
      ∑ fW : Fin (p - 2) ↪ Fin (p + 1), countCanon p (availSet fW) := by
  classical
  rw [FoldCover.chromPoly_eq_card]
  let e : { f : V0 p → Fin (p + 1) // FoldCover.IsProperColoring (G0 p) f } ≃
      Σ (fW : Fin (p - 2) ↪ Fin (p + 1)) (c₀ : availSet fW) (c₁ : availSet fW),
        (Fin p → { c : Fin (p + 1) // c ∈ ((availSet fW).erase c₀.1).erase c₁.1 }) :=
    { toFun := fun ⟨f, hf⟩ =>
        let fW : Fin (p - 2) ↪ Fin (p + 1) :=
          ⟨fun w => f (Sum.inl w), fun w₁ w₂ hEq => by
            by_contra hne
            exact hf (Sum.inl w₁) (Sum.inl w₂) hne hEq⟩
        have hmem : ∀ y : Fin 2 ⊕ Fin p, f (Sum.inr y) ∈ availSet fW := fun y => by
          simp only [availSet, Finset.mem_sdiff, Finset.mem_univ, true_and, Finset.mem_image,
            not_exists]
          intro w hEq
          exact hf (Sum.inl w) (Sum.inr y) trivial hEq
        ⟨fW, ⟨f (Sum.inr (Sum.inl 0)), hmem (Sum.inl 0)⟩,
          ⟨f (Sum.inr (Sum.inl 1)), hmem (Sum.inl 1)⟩,
          fun j => ⟨f (Sum.inr (Sum.inr j)), by
            refine Finset.mem_erase.mpr ⟨?_, Finset.mem_erase.mpr ⟨?_, hmem (Sum.inr j)⟩⟩
            · exact (hf (Sum.inr (Sum.inl 1)) (Sum.inr (Sum.inr j)) trivial).symm
            · exact (hf (Sum.inr (Sum.inl 0)) (Sum.inr (Sum.inr j)) trivial).symm⟩⟩
      invFun := fun ⟨fW, c₀, c₁, fU⟩ =>
        ⟨fun x => match x with
          | Sum.inl w => fW w
          | Sum.inr (Sum.inl i) => if i = 0 then c₀.1 else c₁.1
          | Sum.inr (Sum.inr j) => (fU j).1,
        by
          rintro (w₁ | (i₁ | j₁)) (w₂ | (i₂ | j₂)) hadj hEq
          · exact hadj (fW.injective hEq)
          · have hm : (if i₂ = 0 then c₀.1 else c₁.1) ∈ availSet fW := by
              split_ifs <;> [exact c₀.2; exact c₁.2]
            exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₁, Finset.mem_univ _, hEq⟩)
          · have hm : (fU j₂).1 ∈ availSet fW :=
              Finset.mem_of_mem_erase (Finset.mem_of_mem_erase (fU j₂).2)
            exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₁, Finset.mem_univ _, hEq⟩)
          · have hm : (if i₁ = 0 then c₀.1 else c₁.1) ∈ availSet fW := by
              split_ifs <;> [exact c₀.2; exact c₁.2]
            exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₂, Finset.mem_univ _, hEq.symm⟩)
          · exact hadj.elim
          · fin_cases i₁
            · exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase (fU j₂).2)).1 hEq.symm
            · exact (Finset.mem_erase.mp (fU j₂).2).1 hEq.symm
          · have hm : (fU j₁).1 ∈ availSet fW :=
              Finset.mem_of_mem_erase (Finset.mem_of_mem_erase (fU j₁).2)
            exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₂, Finset.mem_univ _, hEq.symm⟩)
          · fin_cases i₂
            · exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase (fU j₁).2)).1 hEq
            · exact (Finset.mem_erase.mp (fU j₁).2).1 hEq
          · exact hadj.elim⟩
      left_inv := fun ⟨f, _⟩ => by
        apply Subtype.ext
        funext x
        rcases x with w | (i | j)
        · rfl
        · fin_cases i <;> rfl
        · rfl
      right_inv := fun ⟨fW, c₀, c₁, fU⟩ => by
        dsimp
        rfl }
  rw [Fintype.card_congr e]
  simp only [Fintype.card_sigma, Fintype.card_pi, Fintype.card_coe, Finset.prod_const,
    Finset.card_univ, Fintype.card_fin]
  refine Finset.sum_congr rfl fun fW _ => ?_
  unfold countCanon
  rw [← Finset.sum_coe_sort (availSet fW)]
  refine Finset.sum_congr rfl fun c₀ _ => ?_
  rw [← Finset.sum_coe_sort (availSet fW)]

private lemma dpColorCount_twistedCover_eq_sum {p : ℕ} (hp : 3 ≤ p) :
    (twistedCover p hp).dpColorCount =
      ∑ fW : Fin (p - 2) ↪ Fin (p + 1), countTwist p hp (availSet fW) := by
  classical
  rw [FoldCover.dpColorCount_eq_card_hColoring]
  let e : { f : V0 p → Fin (p + 1) // (twistedCover p hp).IsHColoring f } ≃
      Σ (fW : Fin (p - 2) ↪ Fin (p + 1)) (c₀ : availSet fW) (c₁ : availSet fW),
        ({ c : Fin (p + 1) // c ∈ ((availSet fW).erase (swap01 p hp c₀.1)).erase c₁.1 } ×
         ({ j : Fin p // j ≠ ⟨0, by omega⟩ } →
           { c : Fin (p + 1) // c ∈ ((availSet fW).erase c₀.1).erase c₁.1 })) :=
    { toFun := fun ⟨f, hf⟩ =>
        let fW : Fin (p - 2) ↪ Fin (p + 1) :=
          ⟨fun w => f (Sum.inl w), fun w₁ w₂ hEq => by
            by_contra hne
            apply hf (Sum.inl w₁) (Sum.inl w₂) hne
            right; refine ⟨hne, ?_⟩
            have hnt : ¬ isTwistedEdge p hp (Sum.inl w₁) (Sum.inl w₂) := by simp [isTwistedEdge]
            simp only [hnt, ↓reduceIte]; exact hEq⟩
        have hmem : ∀ y : Fin 2 ⊕ Fin p, f (Sum.inr y) ∈ availSet fW := fun y => by
          simp only [availSet, Finset.mem_sdiff, Finset.mem_univ, true_and, Finset.mem_image,
            not_exists]
          intro w hEq
          apply hf (Sum.inl w) (Sum.inr y) trivial
          right; refine ⟨trivial, ?_⟩
          have hnt : ¬ isTwistedEdge p hp (Sum.inl w) (Sum.inr y) := by simp [isTwistedEdge]
          simp only [hnt, ↓reduceIte]; exact hEq
        ⟨fW, ⟨f (Sum.inr (Sum.inl 0)), hmem (Sum.inl 0)⟩,
          ⟨f (Sum.inr (Sum.inl 1)), hmem (Sum.inl 1)⟩,
          ⟨⟨f (Sum.inr (Sum.inr ⟨0, by omega⟩)), by
            refine Finset.mem_erase.mpr ⟨?_, Finset.mem_erase.mpr ⟨?_, hmem (Sum.inr _)⟩⟩
            · intro hEq
              apply hf (Sum.inr (Sum.inl 1)) (Sum.inr (Sum.inr ⟨0, by omega⟩)) trivial
              right; refine ⟨trivial, ?_⟩
              have hnt : ¬ isTwistedEdge p hp (Sum.inr (Sum.inl 1)) (Sum.inr (Sum.inr ⟨0, by omega⟩)) := by
                simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte]; exact hEq.symm
            · intro hEq
              apply hf (Sum.inr (Sum.inl 0)) (Sum.inr (Sum.inr ⟨0, by omega⟩)) trivial
              right; refine ⟨trivial, ?_⟩
              have ht : isTwistedEdge p hp (Sum.inr (Sum.inl 0)) (Sum.inr (Sum.inr ⟨0, by omega⟩)) :=
                Or.inl ⟨rfl, rfl⟩
              simp only [ht, ↓reduceIte]; exact hEq.symm⟩,
          fun ⟨j, hj⟩ => ⟨f (Sum.inr (Sum.inr j)), by
            refine Finset.mem_erase.mpr ⟨?_, Finset.mem_erase.mpr ⟨?_, hmem (Sum.inr j)⟩⟩
            · intro hEq
              apply hf (Sum.inr (Sum.inl 1)) (Sum.inr (Sum.inr j)) trivial
              right; refine ⟨trivial, ?_⟩
              have hnt : ¬ isTwistedEdge p hp (Sum.inr (Sum.inl 1)) (Sum.inr (Sum.inr j)) := by
                simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte]; exact hEq.symm
            · intro hEq
              apply hf (Sum.inr (Sum.inl 0)) (Sum.inr (Sum.inr j)) trivial
              right; refine ⟨trivial, ?_⟩
              have hnt : ¬ isTwistedEdge p hp (Sum.inr (Sum.inl 0)) (Sum.inr (Sum.inr j)) := by
                simp [isTwistedEdge, hj]
              simp only [hnt, ↓reduceIte]; exact hEq.symm⟩⟩⟩
      invFun := fun ⟨fW, c₀, c₁, u₀, fU⟩ =>
        ⟨fun x => match x with
          | Sum.inl w => fW w
          | Sum.inr (Sum.inl i) => if i = 0 then c₀.1 else c₁.1
          | Sum.inr (Sum.inr j) => if hj : j = ⟨0, by omega⟩ then u₀.1 else (fU ⟨j, hj⟩).1,
        by
          intro x y hadj hCadj
          rcases hCadj with ⟨hxy, _⟩ | ⟨_, hmatch⟩
          · dsimp only at hxy
            exact (G0 p).loopless.irrefl x (hxy ▸ hadj)
          · rcases x with w₁ | (i₁ | j₁) <;> rcases y with w₂ | (i₂ | j₂)
            · have hnt : ¬ isTwistedEdge p hp (Sum.inl w₁) (Sum.inl w₂) := by simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte] at hmatch
              exact hadj (fW.injective hmatch)
            · have hnt : ¬ isTwistedEdge p hp (Sum.inl w₁) (Sum.inr (Sum.inl i₂)) := by simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte] at hmatch
              have hm : (if i₂ = 0 then c₀.1 else c₁.1) ∈ availSet fW := by
                split_ifs <;> [exact c₀.2; exact c₁.2]
              exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₁, Finset.mem_univ _, hmatch⟩)
            · have hnt : ¬ isTwistedEdge p hp (Sum.inl w₁) (Sum.inr (Sum.inr j₂)) := by simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte] at hmatch
              have hm : (if hj : j₂ = ⟨0, by omega⟩ then u₀.1 else (fU ⟨j₂, hj⟩).1) ∈ availSet fW := by
                split_ifs with hj
                · exact Finset.mem_of_mem_erase (Finset.mem_of_mem_erase u₀.2)
                · exact Finset.mem_of_mem_erase (Finset.mem_of_mem_erase (fU ⟨j₂, hj⟩).2)
              exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₁, Finset.mem_univ _, hmatch⟩)
            · have hnt : ¬ isTwistedEdge p hp (Sum.inr (Sum.inl i₁)) (Sum.inl w₂) := by simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte] at hmatch
              have hm : (if i₁ = 0 then c₀.1 else c₁.1) ∈ availSet fW := by
                split_ifs <;> [exact c₀.2; exact c₁.2]
              exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₂, Finset.mem_univ _, hmatch.symm⟩)
            · exact hadj.elim
            · rcases (show i₁ = 0 ∨ i₁ = 1 by fin_cases i₁ <;> [left; right] <;> rfl) with rfl | rfl
              · by_cases hj : j₂ = ⟨0, by omega⟩
                · subst hj
                  dsimp only at hmatch
                  simp only [↓reduceIte, ↓reduceDIte] at hmatch
                  split_ifs at hmatch with ht
                  · exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase u₀.2)).1 hmatch.symm
                  · exact ht (Or.inl ⟨rfl, rfl⟩)
                · dsimp only at hmatch
                  simp only [hj, ↓reduceIte, ↓reduceDIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge, hj] at ht
                  · exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase (fU ⟨j₂, hj⟩).2)).1 hmatch.symm
              · by_cases hj : j₂ = ⟨0, by omega⟩
                · subst hj
                  dsimp only at hmatch
                  simp only [↓reduceDIte] at hmatch
                  have h10 : (1 : Fin 2) ≠ 0 := by decide
                  simp only [h10, ↓reduceIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge] at ht
                  · exact (Finset.mem_erase.mp u₀.2).1 hmatch.symm
                · dsimp only at hmatch
                  simp only [hj, ↓reduceDIte] at hmatch
                  have h10 : (1 : Fin 2) ≠ 0 := by decide
                  simp only [h10, ↓reduceIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge] at ht
                  · exact (Finset.mem_erase.mp (fU ⟨j₂, hj⟩).2).1 hmatch.symm
            · have hnt : ¬ isTwistedEdge p hp (Sum.inr (Sum.inr j₁)) (Sum.inl w₂) := by simp [isTwistedEdge]
              simp only [hnt, ↓reduceIte] at hmatch
              have hm : (if hj : j₁ = ⟨0, by omega⟩ then u₀.1 else (fU ⟨j₁, hj⟩).1) ∈ availSet fW := by
                split_ifs with hj
                · exact Finset.mem_of_mem_erase (Finset.mem_of_mem_erase u₀.2)
                · exact Finset.mem_of_mem_erase (Finset.mem_of_mem_erase (fU ⟨j₁, hj⟩).2)
              exact (Finset.mem_sdiff.mp hm).2 (Finset.mem_image.mpr ⟨w₂, Finset.mem_univ _, hmatch.symm⟩)
            · rcases (show i₂ = 0 ∨ i₂ = 1 by fin_cases i₂ <;> [left; right] <;> rfl) with rfl | rfl
              · by_cases hj : j₁ = ⟨0, by omega⟩
                · subst hj
                  dsimp only at hmatch
                  simp only [↓reduceIte, ↓reduceDIte] at hmatch
                  split_ifs at hmatch with ht
                  · have h2 : u₀.1 = swap01 p hp c₀.1 := by
                      calc u₀.1 = swap01 p hp (swap01 p hp u₀.1) := (Equiv.swap_apply_self _ _ _).symm
                        _ = swap01 p hp c₀.1 := congrArg (swap01 p hp) hmatch
                    exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase u₀.2)).1 h2
                  · exact ht (Or.inr ⟨rfl, rfl⟩)
                · dsimp only at hmatch
                  simp only [hj, ↓reduceIte, ↓reduceDIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge, hj] at ht
                  · exact (Finset.mem_erase.mp (Finset.mem_of_mem_erase (fU ⟨j₁, hj⟩).2)).1 hmatch
              · by_cases hj : j₁ = ⟨0, by omega⟩
                · subst hj
                  dsimp only at hmatch
                  simp only [↓reduceDIte] at hmatch
                  have h10 : (1 : Fin 2) ≠ 0 := by decide
                  simp only [h10, ↓reduceIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge] at ht
                  · exact (Finset.mem_erase.mp u₀.2).1 hmatch
                · dsimp only at hmatch
                  simp only [hj, ↓reduceDIte] at hmatch
                  have h10 : (1 : Fin 2) ≠ 0 := by decide
                  simp only [h10, ↓reduceIte] at hmatch
                  split_ifs at hmatch with ht
                  · simp [isTwistedEdge] at ht
                  · exact (Finset.mem_erase.mp (fU ⟨j₁, hj⟩).2).1 hmatch
            · exact hadj.elim⟩
      left_inv := fun ⟨f, _⟩ => by
        apply Subtype.ext
        funext x
        rcases x with w | (i | j)
        · rfl
        · fin_cases i <;> rfl
        · by_cases hj : j = ⟨0, by omega⟩
          · subst hj; simp
          · simp [hj]
      right_inv := fun ⟨fW, c₀, c₁, u₀, fU⟩ => by
        refine Sigma.ext rfl (heq_of_eq ?_)
        refine Sigma.ext rfl (heq_of_eq ?_)
        refine Sigma.ext rfl (heq_of_eq ?_)
        refine Prod.ext (Subtype.ext (by simp)) (funext fun ⟨j, hj⟩ => Subtype.ext (by simp [hj])) }
  rw [Fintype.card_congr e]
  have hcard_j : Fintype.card { j : Fin p // j ≠ ⟨0, by omega⟩ } = p - 1 := by
    rw [Fintype.card_subtype_compl, Fintype.card_fin, Fintype.card_unique]
  simp only [Fintype.card_sigma, Fintype.card_prod, Fintype.card_pi, Fintype.card_coe,
    Finset.prod_const, Finset.card_univ, hcard_j]
  refine Finset.sum_congr rfl fun fW _ => ?_
  unfold countTwist
  rw [← Finset.sum_coe_sort (availSet fW)]
  refine Finset.sum_congr rfl fun c₀ _ => ?_
  rw [← Finset.sum_coe_sort (availSet fW)]
  refine Finset.sum_congr rfl fun c₁ _ => mul_comm _ _

/-- Pointwise comparison of `countTwist` vs `countCanon` on a 3-element subset $S \subseteq \mathrm{Fin}(p+1)$. -/
private lemma countTwist_case_disjoint {p : ℕ} (hp : 3 ≤ p) {S : Finset (Fin (p + 1))}
    (h0 : ⟨0, by omega⟩ ∉ S) (h1 : ⟨1, by omega⟩ ∉ S) :
    countTwist p hp S = countCanon p S := by
  unfold countTwist countCanon
  refine Finset.sum_congr rfl fun c₀ hc₀ => Finset.sum_congr rfl fun c₁ _ => ?_
  have hne0 : c₀ ≠ ⟨0, by omega⟩ := fun h => h0 (h ▸ hc₀)
  have hne1 : c₀ ≠ ⟨1, by omega⟩ := fun h => h1 (h ▸ hc₀)
  rw [swap01_apply_of_ne hp hne0 hne1, ← pow_succ, Nat.sub_add_cancel (by omega)]

private lemma countTwist_case_one {p : ℕ} (hp : 3 ≤ p) {S : Finset (Fin (p + 1))} (hcard : S.card = 3)
    {a : Fin (p + 1)} (ha_mem : a ∈ S) (htau_not : swap01 p hp a ∉ S)
    (hother : ∀ c ∈ S, c ≠ a → swap01 p hp c = c) :
    countTwist p hp S = countCanon p S + 2 := by
  unfold countTwist countCanon
  conv_lhs => rw [← Finset.add_sum_erase _ _ ha_mem]
  conv_rhs => rw [← Finset.add_sum_erase _ _ ha_mem]
  have hrest : ∑ c₀ ∈ S.erase a, ∑ c₁ ∈ S,
      ((S.erase c₀).erase c₁).card ^ (p - 1) * ((S.erase (swap01 p hp c₀)).erase c₁).card =
      ∑ c₀ ∈ S.erase a, ∑ c₁ ∈ S, ((S.erase c₀).erase c₁).card ^ p := by
    refine Finset.sum_congr rfl fun c₀ hc₀ => Finset.sum_congr rfl fun c₁ _ => ?_
    rw [hother c₀ (Finset.mem_of_mem_erase hc₀) (Finset.ne_of_mem_erase hc₀),
      ← pow_succ, Nat.sub_add_cancel (by omega)]
  rw [hrest]
  suffices hmain : ∑ c₁ ∈ S,
      ((S.erase a).erase c₁).card ^ (p - 1) * ((S.erase (swap01 p hp a)).erase c₁).card =
      (∑ c₁ ∈ S, ((S.erase a).erase c₁).card ^ p) + 2 by rw [hmain]; ring
  rw [← Finset.add_sum_erase _ _ ha_mem, ← Finset.add_sum_erase _ _ ha_mem]
  have hta_eq : S.erase (swap01 p hp a) = S := Finset.erase_eq_of_notMem htau_not
  have hdiag : ((S.erase a).erase a).card ^ (p - 1) * ((S.erase (swap01 p hp a)).erase a).card =
      ((S.erase a).erase a).card ^ p := by
    rw [hta_eq, Finset.erase_idem, ← pow_succ, Nat.sub_add_cancel (by omega)]
  rw [hdiag]
  have hoff_t : ∑ c₁ ∈ S.erase a,
      ((S.erase a).erase c₁).card ^ (p - 1) * ((S.erase (swap01 p hp a)).erase c₁).card = 4 := by
    have hterm : ∀ c₁ ∈ S.erase a,
        ((S.erase a).erase c₁).card ^ (p - 1) * ((S.erase (swap01 p hp a)).erase c₁).card = 2 := by
      intro c₁ hc₁
      have h1 : ((S.erase a).erase c₁).card = 1 := by
        rw [Finset.card_erase_of_mem hc₁, Finset.card_erase_of_mem ha_mem, hcard]
      have h2 : ((S.erase (swap01 p hp a)).erase c₁).card = 2 := by
        rw [hta_eq, Finset.card_erase_of_mem (Finset.mem_of_mem_erase hc₁), hcard]
      rw [h1, h2, one_pow, one_mul]
    rw [Finset.sum_congr rfl hterm, Finset.sum_const, Finset.card_erase_of_mem ha_mem, hcard]
    decide
  have hoff_c : ∑ c₁ ∈ S.erase a, ((S.erase a).erase c₁).card ^ p = 2 := by
    have hterm : ∀ c₁ ∈ S.erase a, ((S.erase a).erase c₁).card ^ p = 1 := by
      intro c₁ hc₁
      have h1 : ((S.erase a).erase c₁).card = 1 := by
        rw [Finset.card_erase_of_mem hc₁, Finset.card_erase_of_mem ha_mem, hcard]
      rw [h1, one_pow]
    rw [Finset.sum_congr rfl hterm, Finset.sum_const, Finset.card_erase_of_mem ha_mem, hcard]
    decide
  rw [hoff_t, hoff_c]

private lemma countTwist_case_both {p : ℕ} (hp : 3 ≤ p) {S : Finset (Fin (p + 1))} (hcard : S.card = 3)
    (h0 : ⟨0, by omega⟩ ∈ S) (h1 : ⟨1, by omega⟩ ∈ S) :
    countTwist p hp S + 2 ^ p = countCanon p S + 2 := by
  let z0 : Fin (p + 1) := ⟨0, by omega⟩
  let z1 : Fin (p + 1) := ⟨1, by omega⟩
  have hz01 : z0 ≠ z1 := by intro h; have := congrArg Fin.val h; dsimp [z0, z1] at this; omega
  have h1' : z1 ∈ S.erase z0 := Finset.mem_erase.mpr ⟨hz01.symm, h1⟩
  have hcard1 : ((S.erase z0).erase z1).card = 1 := by
    rw [Finset.card_erase_of_mem h1', Finset.card_erase_of_mem h0, hcard]
  rcases Finset.card_eq_one.mp hcard1 with ⟨s, hs⟩
  have hs_mem : s ∈ (S.erase z0).erase z1 := by rw [hs]; exact Finset.mem_singleton_self s
  have hsz1 : s ≠ z1 := Finset.ne_of_mem_erase hs_mem
  have hsz0 : s ≠ z0 := Finset.ne_of_mem_erase (Finset.mem_of_mem_erase hs_mem)
  have hs_S : s ∈ S := Finset.mem_of_mem_erase (Finset.mem_of_mem_erase hs_mem)
  have hS_eq : S = {z0, z1, s} := by
    ext x
    simp only [Finset.mem_insert, Finset.mem_singleton]
    constructor
    · intro hx
      by_cases hx0 : x = z0
      · exact Or.inl hx0
      · by_cases hx1 : x = z1
        · exact Or.inr (Or.inl hx1)
        · have : x ∈ (S.erase z0).erase z1 :=
            Finset.mem_erase.mpr ⟨hx1, Finset.mem_erase.mpr ⟨hx0, hx⟩⟩
          rw [hs] at this
          exact Or.inr (Or.inr (Finset.mem_singleton.mp this))
    · rintro (rfl | rfl | rfl)
      · exact h0
      · exact h1
      · exact hs_S
  have hnot0 : z0 ∉ ({z1, s} : Finset (Fin (p + 1))) := by simp [hz01, hsz0.symm]
  have hnot1 : z1 ∉ ({s} : Finset (Fin (p + 1))) := by simp [hsz1.symm]
  have hcard_er : ∀ a ∈ S, ∀ b ∈ S, ((S.erase a).erase b).card = if a = b then 2 else 1 := by
    intro a ha b hb
    split_ifs with hab
    · subst hab; rw [Finset.erase_idem, Finset.card_erase_of_mem ha, hcard]
    · rw [Finset.card_erase_of_mem (Finset.mem_erase.mpr ⟨Ne.symm hab, hb⟩),
        Finset.card_erase_of_mem ha, hcard]
  have hs0 : swap01 p hp z0 = z1 := swap01_apply_zero hp
  have hs1 : swap01 p hp z1 = z0 := swap01_apply_one hp
  have hss : swap01 p hp s = s := swap01_apply_of_ne hp hsz0 hsz1
  -- Expand both sums over `{z0, z1, s} × {z0, z1, s}` explicitly!
  have hCanon : countCanon p S = 3 * 2 ^ p + 6 := by
    unfold countCanon
    have expand : ∀ f : Fin (p + 1) → ℕ, ∑ x ∈ S, f x = f z0 + f z1 + f s := fun f => by
      rw [hS_eq, Finset.sum_insert hnot0, Finset.sum_insert hnot1, Finset.sum_singleton]; omega
    rw [expand]
    simp only [expand]
    rw [hcard_er z0 h0 z0 h0, hcard_er z0 h0 z1 h1, hcard_er z0 h0 s hs_S,
      hcard_er z1 h1 z0 h0, hcard_er z1 h1 z1 h1, hcard_er z1 h1 s hs_S,
      hcard_er s hs_S z0 h0, hcard_er s hs_S z1 h1, hcard_er s hs_S s hs_S]
    simp [hz01, hz01.symm, hsz0, hsz0.symm, hsz1, hsz1.symm]
    ring
  have hTwist : countTwist p hp S = 2 * 2 ^ (p - 1) + 2 ^ p + 8 := by
    unfold countTwist
    have expand : ∀ f : Fin (p + 1) → ℕ, ∑ x ∈ S, f x = f z0 + f z1 + f s := fun f => by
      rw [hS_eq, Finset.sum_insert hnot0, Finset.sum_insert hnot1, Finset.sum_singleton]; omega
    rw [expand]
    simp only [expand, hs0, hs1, hss]
    rw [hcard_er z0 h0 z0 h0, hcard_er z0 h0 z1 h1, hcard_er z0 h0 s hs_S,
      hcard_er z1 h1 z0 h0, hcard_er z1 h1 z1 h1, hcard_er z1 h1 s hs_S,
      hcard_er s hs_S z0 h0, hcard_er s hs_S z1 h1, hcard_er s hs_S s hs_S]
    simp [hz01, hz01.symm, hsz0, hsz0.symm, hsz1, hsz1.symm]
    have hpow : 2 ^ (p - 1) * 2 = 2 ^ p := by
      rw [← pow_succ, Nat.sub_add_cancel (by omega)]
    linarith
  have hpow : 2 * 2 ^ (p - 1) = 2 ^ p := by
    rw [mul_comm, ← pow_succ, Nat.sub_add_cancel (by omega)]
  rw [hCanon, hTwist, hpow]
  omega

/-- **Lemma 2:** For every $p \ge 3$, $P_{DP}(G_0^{(p)}, p+1) < P(G_0^{(p)}, p+1)$. -/
theorem dpColorFun_G0_lt_chromPoly {p : ℕ} (hp : 3 ≤ p) :
    dpColorFun (G0 p) (p + 1) < FoldCover.chromPoly (G0 p) (p + 1) := by
  classical
  refine lt_of_le_of_lt (dpColorFun_le (G0 p) (p + 1) (twistedCover p hp)) ?_
  rw [dpColorCount_twistedCover_eq_sum hp, chromPoly_G0_eq_sum hp]
  let z0 : Fin (p + 1) := ⟨0, by omega⟩
  let z1 : Fin (p + 1) := ⟨1, by omega⟩
  have hz01 : z0 ≠ z1 := by intro h; have := congrArg Fin.val h; dsimp [z0, z1] at this; omega
  let inB : (Fin (p - 2) ↪ Fin (p + 1)) → Prop := fun fW =>
    (z0 ∈ availSet fW ∧ z1 ∉ availSet fW) ∨ (z0 ∉ availSet fW ∧ z1 ∈ availSet fW)
  let inC : (Fin (p - 2) ↪ Fin (p + 1)) → Prop := fun fW =>
    z0 ∈ availSet fW ∧ z1 ∈ availSet fW
  have hpt : ∀ fW : Fin (p - 2) ↪ Fin (p + 1),
      countTwist p hp (availSet fW) + (if inC fW then 2 ^ p else 0) =
      countCanon p (availSet fW) + (if inB fW ∨ inC fW then 2 else 0) := by
    intro fW
    have hcard := card_availSet hp fW
    by_cases h0 : z0 ∈ availSet fW <;> by_cases h1 : z1 ∈ availSet fW
    · have hC : inC fW := ⟨h0, h1⟩
      have h1_eq : (if inC fW then 2 ^ p else 0) = 2 ^ p := by simp [hC]
      have h2_eq : (if inB fW ∨ inC fW then 2 else 0) = 2 := by simp [hC]
      rw [h1_eq, h2_eq]
      exact countTwist_case_both hp hcard h0 h1
    · have hB : inB fW := Or.inl ⟨h0, h1⟩
      have hnC : ¬ inC fW := fun h => h1 h.2
      have h1_eq : (if inC fW then 2 ^ p else 0) = 0 := by simp [hnC]
      have h2_eq : (if inB fW ∨ inC fW then 2 else 0) = 2 := by simp [hB]
      rw [h1_eq, h2_eq, add_zero]
      exact countTwist_case_one hp hcard h0 (by rw [swap01_apply_zero hp]; exact h1)
        (fun c hc hne => swap01_apply_of_ne hp hne (fun h => h1 (by change (⟨1, by omega⟩ : Fin (p + 1)) ∈ _; rw [← h]; exact hc)))
    · have hB : inB fW := Or.inr ⟨h0, h1⟩
      have hnC : ¬ inC fW := fun h => h0 h.1
      have h1_eq : (if inC fW then 2 ^ p else 0) = 0 := by simp [hnC]
      have h2_eq : (if inB fW ∨ inC fW then 2 else 0) = 2 := by simp [hB]
      rw [h1_eq, h2_eq, add_zero]
      exact countTwist_case_one hp hcard h1 (by rw [swap01_apply_one hp]; exact h0)
        (fun c hc hne => swap01_apply_of_ne hp (fun h => h0 (by change (⟨0, by omega⟩ : Fin (p + 1)) ∈ _; rw [← h]; exact hc)) hne)
    · have hnB : ¬ inB fW := by rintro (⟨h, _⟩ | ⟨_, h⟩) <;> [exact h0 h; exact h1 h]
      have hnC : ¬ inC fW := fun h => h0 h.1
      have h1_eq : (if inC fW then 2 ^ p else 0) = 0 := by simp [hnC]
      have h2_eq : (if inB fW ∨ inC fW then 2 else 0) = 0 := by simp [hnB, hnC]
      rw [h1_eq, h2_eq, add_zero, add_zero]
      exact countTwist_case_disjoint hp h0 h1
  have hsum : (∑ fW : Fin (p - 2) ↪ Fin (p + 1), countTwist p hp (availSet fW)) +
      (Finset.univ.filter inC).card * 2 ^ p =
      (∑ fW : Fin (p - 2) ↪ Fin (p + 1), countCanon p (availSet fW)) +
      (Finset.univ.filter (fun fW => inB fW ∨ inC fW)).card * 2 := by
    have h1 := Finset.sum_congr rfl fun fW (_ : fW ∈ Finset.univ) => hpt fW
    simp only [Finset.sum_add_distrib, Finset.sum_ite, Finset.sum_const, smul_eq_mul] at h1
    simpa using h1
  -- Count `inC` and `inB ∨ inC` using `Fintype.card_embedding_eq`
  have hcard_C : (Finset.univ.filter inC).card = (p - 1).descFactorial (p - 2) := by
    have e : { fW : Fin (p - 2) ↪ Fin (p + 1) // inC fW } ≃
        (Fin (p - 2) ↪ { c : Fin (p + 1) // c ≠ z0 ∧ c ≠ z1 }) :=
      { toFun := fun ⟨fW, h0, h1⟩ =>
          ⟨fun w => ⟨fW w,
            fun h => (Finset.mem_sdiff.mp h0).2 (Finset.mem_image.mpr ⟨w, Finset.mem_univ _, h⟩),
            fun h => (Finset.mem_sdiff.mp h1).2 (Finset.mem_image.mpr ⟨w, Finset.mem_univ _, h⟩)⟩,
          fun w₁ w₂ h => fW.injective (congrArg Subtype.val h)⟩
        invFun := fun g =>
          ⟨⟨fun w => (g w).1, fun w₁ w₂ h => g.injective (Subtype.ext h)⟩,
            Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, by
              simp only [Finset.mem_image, Finset.mem_univ, true_and, not_exists]
              exact fun w => (g w).2.1⟩,
            Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, by
              simp only [Finset.mem_image, Finset.mem_univ, true_and, not_exists]
              exact fun w => (g w).2.2⟩⟩
        left_inv := fun _ => rfl
        right_inv := fun _ => rfl }
    have htarget : Fintype.card { c : Fin (p + 1) // c ≠ z0 ∧ c ≠ z1 } = p - 1 := by
      have hsub : Finset.univ.filter (fun c : Fin (p + 1) => c ≠ z0 ∧ c ≠ z1) =
          (Finset.univ.erase z0).erase z1 := by
        ext c; simp [and_comm]
      rw [Fintype.card_subtype, hsub, Finset.card_erase_of_mem (Finset.mem_erase.mpr ⟨hz01.symm, Finset.mem_univ _⟩),
        Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, Fintype.card_fin]
      omega
    rw [← Fintype.card_subtype, Fintype.card_congr e, Fintype.card_embedding_eq, Fintype.card_fin,
      htarget]
  have hcard_mem : ∀ z : Fin (p + 1),
      (Finset.univ.filter (fun fW : Fin (p - 2) ↪ Fin (p + 1) => z ∈ availSet fW)).card =
        p.descFactorial (p - 2) := by
    intro z
    have e : { fW : Fin (p - 2) ↪ Fin (p + 1) // z ∈ availSet fW } ≃
        (Fin (p - 2) ↪ { c : Fin (p + 1) // c ≠ z }) :=
      { toFun := fun ⟨fW, hz⟩ =>
          ⟨fun w => ⟨fW w,
            fun h => (Finset.mem_sdiff.mp hz).2 (Finset.mem_image.mpr ⟨w, Finset.mem_univ _, h⟩)⟩,
          fun w₁ w₂ h => fW.injective (congrArg Subtype.val h)⟩
        invFun := fun g =>
          ⟨⟨fun w => (g w).1, fun w₁ w₂ h => g.injective (Subtype.ext h)⟩,
            Finset.mem_sdiff.mpr ⟨Finset.mem_univ _, by
              simp only [Finset.mem_image, Finset.mem_univ, true_and, not_exists]
              exact fun w => (g w).2⟩⟩
        left_inv := fun _ => rfl
        right_inv := fun _ => rfl }
    have htarget : Fintype.card { c : Fin (p + 1) // c ≠ z } = p := by
      rw [Fintype.card_subtype_compl, Fintype.card_fin, Fintype.card_unique]; omega
    rw [← Fintype.card_subtype, Fintype.card_congr e, Fintype.card_embedding_eq, Fintype.card_fin,
      htarget]
  -- Inclusion-exclusion: `|inB ∨ inC| + |inC| = |z0 ∈ avail| + |z1 ∈ avail|`
  have hBC_union : Finset.univ.filter (fun fW => inB fW ∨ inC fW) =
      (Finset.univ.filter (fun fW => z0 ∈ availSet fW)) ∪
      (Finset.univ.filter (fun fW => z1 ∈ availSet fW)) := by
    ext fW
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_union, inB, inC]
    tauto
  have hBC_inter : (Finset.univ.filter (fun fW => z0 ∈ availSet fW)) ∩
      (Finset.univ.filter (fun fW => z1 ∈ availSet fW)) =
      Finset.univ.filter inC := by
    ext fW; simp [inC]
  have hcard_BC_add : (Finset.univ.filter (fun fW => inB fW ∨ inC fW)).card +
      (Finset.univ.filter inC).card = 2 * p.descFactorial (p - 2) := by
    rw [hBC_union, ← hBC_inter, Finset.card_union_add_card_inter, hcard_mem z0, hcard_mem z1]
    omega
  -- Key factorial identity: `2 * p.descFactorial (p - 2) = p * (p - 1).descFactorial (p - 2)`
  have hdesc_id : 2 * p.descFactorial (p - 2) = p * (p - 1).descFactorial (p - 2) := by
    have h1 : p.descFactorial (p - 1) = 2 * p.descFactorial (p - 2) := by
      have hp1 : p - 1 = (p - 2) + 1 := by omega
      rw [hp1, Nat.descFactorial_succ]
      have : p - (p - 2) = 2 := by omega
      rw [this]
    have h2 : p.descFactorial (p - 1) = p * (p - 1).descFactorial (p - 2) := by
      obtain ⟨q, rfl⟩ : ∃ q, p = q + 2 := ⟨p - 2, by omega⟩
      exact Nat.succ_descFactorial_succ (q + 1) q
    omega
  have hcard_BC : (Finset.univ.filter (fun fW => inB fW ∨ inC fW)).card =
      (p - 1) * (Finset.univ.filter inC).card := by
    rw [hcard_C] at hcard_BC_add ⊢
    have hmul : (p - 1) * (p - 1).descFactorial (p - 2) + (p - 1).descFactorial (p - 2) =
        p * (p - 1).descFactorial (p - 2) := by
      have hp0 : (p - 1) + 1 = p := by omega
      calc (p - 1) * (p - 1).descFactorial (p - 2) + (p - 1).descFactorial (p - 2)
          = ((p - 1) + 1) * (p - 1).descFactorial (p - 2) := by ring
        _ = p * (p - 1).descFactorial (p - 2) := by rw [hp0]
    omega
  have hC_pos : 0 < (Finset.univ.filter inC).card := by
    rw [hcard_C]
    exact Nat.descFactorial_pos.mpr (by omega)
  have hpow_gt : 2 * (p - 1) < 2 ^ p := by
    have hgen : ∀ n, 3 ≤ n → 2 * (n - 1) < 2 ^ n := by
      intro n hn
      induction n, hn using Nat.le_induction with
      | base => decide
      | succ k hk ih =>
        rw [pow_succ]
        omega
    exact hgen p hp
  have hstrict : (Finset.univ.filter (fun fW => inB fW ∨ inC fW)).card * 2 <
      (Finset.univ.filter inC).card * 2 ^ p := by
    rw [hcard_BC]
    calc (p - 1) * (Finset.univ.filter inC).card * 2
        = (Finset.univ.filter inC).card * (2 * (p - 1)) := by ring
      _ < (Finset.univ.filter inC).card * 2 ^ p := Nat.mul_lt_mul_of_pos_left hpow_gt hC_pos
  omega

/-! ## Section 5: Lemma 3 — Precoloring Extension on $G_0^{(p)}$ -/

/-- **Lemma 3:** For any $(p+1)$-fold cover $\mathcal{H}$ of $G_0^{(p)}$ and any $p$-clique $K_r$,
every partial $\mathcal{H}$-coloring on $K_r$ extends to a full $\mathcal{H}$-coloring of $G_0^{(p)}$. -/
private lemma precoloring_extension_G0 {p r : ℕ} (hp : 3 ≤ p) (hr : r < 2 * p)
    (C : FoldCover (G0 p) (p + 1)) (fK : V0 p → Fin (p + 1))
    (hfK : ∀ x y, inKp p r x → inKp p r y → (G0 p).Adj x y → ¬ C.H.Adj (x, fK x) (y, fK y)) :
    ∃ D : V0 p → Fin (p + 1), C.IsHColoring D ∧ ∀ x, inKp p r x → D x = fK x := by
  classical
  have hi0_lt : r / p < 2 := Nat.div_lt_of_lt_mul (by omega)
  let i₀ : Fin 2 := ⟨r / p, hi0_lt⟩
  let j₀ : Fin p := ⟨r % p, Nat.mod_lt r (by omega)⟩
  let i₁ : Fin 2 := ⟨1 - r / p, Nat.lt_of_le_of_lt (Nat.sub_le 1 (r / p)) (by decide)⟩
  have hi_ne : i₁ ≠ i₀ := by
    intro h
    have hv : 1 - r / p = r / p := congrArg Fin.val h
    omega
  -- Step 1: color `v_{i₁}`, whose neighbors in `K_r` are `W ∪ {u_{j₀}}` (size `p - 1`)
  let S_v : Finset (V0 p) :=
    insert (Sum.inr (Sum.inr j₀)) (Finset.univ.image Sum.inl)
  have hv_not : Sum.inr (Sum.inl i₁) ∉ S_v := by simp [S_v]
  have hSv_card : S_v.card = p - 1 := by
    rw [Finset.card_insert_of_notMem (by simp),
      Finset.card_image_of_injective _ Sum.inl_injective, Finset.card_univ, Fintype.card_fin]
    omega
  have hforb_v := card_forbidden_le C S_v (Sum.inr (Sum.inl i₁)) hv_not fK
  have hex_v : ∃ cv : Fin (p + 1), ∀ x ∈ S_v, ¬ C.H.Adj (x, fK x) (Sum.inr (Sum.inl i₁), cv) := by
    have hlt : (Finset.univ.filter (fun c : Fin (p + 1) =>
        ∃ x ∈ S_v, C.H.Adj (x, fK x) (Sum.inr (Sum.inl i₁), c))).card <
        (Finset.univ : Finset (Fin (p + 1))).card := by
      rw [Finset.card_univ, Fintype.card_fin]; omega
    rcases Finset.exists_mem_notMem_of_card_lt_card hlt with ⟨cv, _, hnot⟩
    refine ⟨cv, fun x hx hadj => hnot (Finset.mem_filter.mpr ⟨Finset.mem_univ _, x, hx, hadj⟩)⟩
  rcases hex_v with ⟨cv, hcv⟩
  -- Intermediate coloring `f1` agreeing with `fK` on `K_r` and equal to `cv` on `v_{i₁}`
  let f1 : V0 p → Fin (p + 1) := fun x =>
    if x = Sum.inr (Sum.inl i₁) then cv else fK x
  -- Step 2: for each `j ≠ j₀`, `u_j` has neighbors `W ∪ {v₀, v₁}` (size `p`), leaving `≥ 1` choice
  let S_u : Finset (V0 p) :=
    insert (Sum.inr (Sum.inl i₀)) (insert (Sum.inr (Sum.inl i₁)) (Finset.univ.image Sum.inl))
  have hSu_card : S_u.card = p := by
    rw [Finset.card_insert_of_notMem (by simp [hi_ne.symm]),
      Finset.card_insert_of_notMem (by simp),
      Finset.card_image_of_injective _ Sum.inl_injective, Finset.card_univ, Fintype.card_fin]
    omega
  have hex_u : ∀ j : Fin p, ∃ cu : Fin (p + 1),
      ∀ x ∈ S_u, ¬ C.H.Adj (x, f1 x) (Sum.inr (Sum.inr j), cu) := by
    intro j
    have hu_not : Sum.inr (Sum.inr j) ∉ S_u := by simp [S_u]
    have hforb_u := card_forbidden_le C S_u (Sum.inr (Sum.inr j)) hu_not f1
    have hlt : (Finset.univ.filter (fun c : Fin (p + 1) =>
        ∃ x ∈ S_u, C.H.Adj (x, f1 x) (Sum.inr (Sum.inr j), c))).card <
        (Finset.univ : Finset (Fin (p + 1))).card := by
      rw [Finset.card_univ, Fintype.card_fin]; omega
    rcases Finset.exists_mem_notMem_of_card_lt_card hlt with ⟨cu, _, hnot⟩
    exact ⟨cu, fun x hx hadj => hnot (Finset.mem_filter.mpr ⟨Finset.mem_univ _, x, hx, hadj⟩)⟩
  let D : V0 p → Fin (p + 1) := fun x =>
    match x with
    | Sum.inl w => fK (Sum.inl w)
    | Sum.inr (Sum.inl i) => if i = i₁ then cv else fK (Sum.inr (Sum.inl i))
    | Sum.inr (Sum.inr j) => if j = j₀ then fK (Sum.inr (Sum.inr j₀)) else Classical.choose (hex_u j)
  have hD_K : ∀ x, inKp p r x → D x = fK x := by
    rintro (w | (i | j)) hx
    · rfl
    · have hi : i = i₀ := Fin.ext hx
      simp [D, hi, hi_ne.symm]
    · have hj : j = j₀ := Fin.ext hx
      simp [D, hj]
  have hD_f1 : ∀ x ∈ S_u, D x = f1 x := by
    intro x hx
    simp only [S_u, Finset.mem_insert, Finset.mem_image, Finset.mem_univ, true_and] at hx
    rcases hx with rfl | rfl | ⟨w, rfl⟩
    · simp [D, f1, hi_ne.symm]
    · simp [D, f1]
    · simp [D, f1]
  refine ⟨D, ?_, hD_K⟩
  have hfin2 : ∀ i : Fin 2, i ≠ i₁ → i = i₀ := by
    intro i hi
    have h1 : i.val < 2 := i.isLt
    have hi0_val : i₀.val = r / p := rfl
    have hi1_val : i₁.val = 1 - r / p := rfl
    have h3 : i.val ≠ i₁.val := fun h => hi (Fin.ext h)
    exact Fin.ext (by omega)
  -- Verify `C.IsHColoring D`
  have hcheck : ∀ x y, (G0 p).Adj x y → ¬ C.H.Adj (x, D x) (y, D y) := by
    rintro (w₁ | (i | j)) (w₂ | (i' | j')) hadj
    · exact hfK (Sum.inl w₁) (Sum.inl w₂) trivial trivial hadj
    · by_cases hi : i' = i₁
      · subst hi
        simpa [D] using hcv (Sum.inl w₁) (by simp [S_v])
      · have hi0 : i' = i₀ := hfin2 i' hi
        subst hi0
        simpa [D, hi] using hfK (Sum.inl w₁) (Sum.inr (Sum.inl i₀)) trivial rfl hadj
    · by_cases hj : j' = j₀
      · subst hj
        simpa [D] using hfK (Sum.inl w₁) (Sum.inr (Sum.inr j₀)) trivial rfl hadj
      · have hmem : Sum.inl w₁ ∈ S_u := by simp [S_u]
        have hspec := Classical.choose_spec (hex_u j') (Sum.inl w₁) hmem
        simpa [D, hj, hD_f1 _ hmem] using hspec
    · by_cases hi : i = i₁
      · subst hi
        intro h
        simp only [D, ↓reduceIte] at h
        exact hcv (Sum.inl w₂) (by simp [S_v]) h.symm
      · have hi0 : i = i₀ := hfin2 i hi
        subst hi0
        simpa [D, hi] using hfK (Sum.inr (Sum.inl i₀)) (Sum.inl w₂) rfl trivial hadj
    · exact hadj.elim
    · by_cases hj : j' = j₀
      · subst hj
        by_cases hi : i = i₁
        · subst hi
          intro h
          simp only [D, ↓reduceIte] at h
          exact hcv (Sum.inr (Sum.inr j₀)) (by simp [S_v]) h.symm
        · have hi0 : i = i₀ := hfin2 i hi
          subst hi0
          simpa [D, hi] using hfK (Sum.inr (Sum.inl i₀)) (Sum.inr (Sum.inr j₀)) rfl rfl hadj
      · have hmem : Sum.inr (Sum.inl i) ∈ S_u := by
          by_cases hi : i = i₁
          · subst hi; simp [S_u]
          · have hi0 : i = i₀ := hfin2 i hi
            subst hi0; simp [S_u]
        have hspec := Classical.choose_spec (hex_u j') (Sum.inr (Sum.inl i)) hmem
        simpa [D, hj, hD_f1 _ hmem] using hspec
    · by_cases hj : j = j₀
      · subst hj
        simpa [D] using hfK (Sum.inr (Sum.inr j₀)) (Sum.inl w₂) rfl trivial hadj
      · have hmem : Sum.inl w₂ ∈ S_u := by simp [S_u]
        have hspec := Classical.choose_spec (hex_u j) (Sum.inl w₂) hmem
        intro h; exact hspec (by simpa [D, hj, hD_f1 _ hmem] using h.symm)
    · by_cases hj : j = j₀
      · subst hj
        by_cases hi : i' = i₁
        · subst hi
          simpa [D] using hcv (Sum.inr (Sum.inr j₀)) (by simp [S_v])
        · have hi0 : i' = i₀ := hfin2 i' hi
          subst hi0
          simpa [D, hi] using hfK (Sum.inr (Sum.inr j₀)) (Sum.inr (Sum.inl i₀)) rfl rfl hadj
      · have hmem : Sum.inr (Sum.inl i') ∈ S_u := by
          by_cases hi : i' = i₁
          · subst hi; simp [S_u]
          · have hi0 : i' = i₀ := hfin2 i' hi
            subst hi0; simp [S_u]
        have hspec := Classical.choose_spec (hex_u j) (Sum.inr (Sum.inl i')) hmem
        intro h; exact hspec (by simpa [D, hj, hD_f1 _ hmem] using h.symm)
    · exact hadj.elim
  exact hcheck

/-! ## Section 6: Main Theorem — Contradiction on $G^* = G_{2p}^{(p)}$ and Refutations -/

/-- Helper: given a full cover $C$ of $G$ and an edge $uv \in E(G)$, extract the matching
permutation $\pi_{u,v} \in S_m$ such that $C.H.\mathrm{Adj}(u, c_1)(v, c_2) \iff \pi_{u,v}(c_1) = c_2$. -/
private noncomputable def fullEdgePerm {V : Type*} {G : SimpleGraph V} {m : ℕ}
    (C : FoldCover G m) (hfull : C.IsFull) {u v : V} (huv : G.Adj u v) : Equiv.Perm (Fin m) := by
  classical
  let g : Fin m → Fin m := fun c₁ => Classical.choose (hfull u v huv c₁)
  have hg_adj : ∀ c₁, C.H.Adj (u, c₁) (v, g c₁) := fun c₁ => Classical.choose_spec (hfull u v huv c₁)
  have hg_inj : Function.Injective g := fun c₁ c₂ hEq =>
    C.matching_left (G.ne_of_adj huv) (hg_adj c₁) (hEq ▸ hg_adj c₂)
  exact Equiv.ofBijective g (Finite.injective_iff_bijective.mp hg_inj)

private lemma fullEdgePerm_iff {V : Type*} {G : SimpleGraph V} {m : ℕ}
    (C : FoldCover G m) (hfull : C.IsFull) {u v : V} (huv : G.Adj u v) (c₁ c₂ : Fin m) :
    C.H.Adj (u, c₁) (v, c₂) ↔ fullEdgePerm C hfull huv c₁ = c₂ := by
  classical
  have hadj : C.H.Adj (u, c₁) (v, fullEdgePerm C hfull huv c₁) :=
    Classical.choose_spec (hfull u v huv c₁)
  constructor
  · intro h
    exact C.matching_right u v c₁ _ c₂ (G.ne_of_adj huv) hadj h
  · rintro rfl
    exact hadj

/-- Greedy extension of a valid partial coloring on a subset $S \subseteq K$ of a clique $K$ of
size $p$ to all of $K$ in any $(p+1)$-fold cover. -/
private lemma greedy_extend_on_clique {V : Type*} [DecidableEq V] {G : SimpleGraph V} {p : ℕ}
    (C : FoldCover G (p + 1)) (K : Finset V) (hKcard : K.card = p) :
    ∀ n : ℕ, ∀ S : Finset V, S ⊆ K → (K \ S).card = n →
      ∀ f : V → Fin (p + 1),
        (∀ x ∈ S, ∀ y ∈ S, G.Adj x y → ¬ C.H.Adj (x, f x) (y, f y)) →
        ∃ f' : V → Fin (p + 1),
          (∀ x ∈ S, f' x = f x) ∧
          (∀ x ∈ K, ∀ y ∈ K, G.Adj x y → ¬ C.H.Adj (x, f' x) (y, f' y)) := by
  intro n
  induction n with
  | zero =>
    intro S hSK hcard0 f hf
    have hEq : S = K := by
      have : K \ S = ∅ := Finset.card_eq_zero.mp hcard0
      exact Finset.Subset.antisymm hSK (Finset.sdiff_eq_empty_iff_subset.mp this)
    subst hEq
    exact ⟨f, fun _ _ => rfl, hf⟩
  | succ n ih =>
    classical
    intro S hSK hcard f hf
    have hne : (K \ S).Nonempty := Finset.card_pos.mp (by omega)
    rcases hne with ⟨v, hv⟩
    have hvK : v ∈ K := (Finset.mem_sdiff.mp hv).1
    have hvS : v ∉ S := (Finset.mem_sdiff.mp hv).2
    have hSlt : S.card < p := by
      have h1 := Finset.card_sdiff_add_card_eq_card hSK
      omega
    have hforb := card_forbidden_le C S v hvS f
    have hlt : (Finset.univ.filter (fun c : Fin (p + 1) =>
        ∃ x ∈ S, C.H.Adj (x, f x) (v, c))).card < (Finset.univ : Finset (Fin (p + 1))).card := by
      rw [Finset.card_univ, Fintype.card_fin]; omega
    rcases Finset.exists_mem_notMem_of_card_lt_card hlt with ⟨cv, _, hnot⟩
    have hcv : ∀ x ∈ S, ¬ C.H.Adj (x, f x) (v, cv) := fun x hx hadj =>
      hnot (Finset.mem_filter.mpr ⟨Finset.mem_univ _, x, hx, hadj⟩)
    let f1 : V → Fin (p + 1) := fun x => if x = v then cv else f x
    have hf1 : ∀ x ∈ insert v S, ∀ y ∈ insert v S, G.Adj x y → ¬ C.H.Adj (x, f1 x) (y, f1 y) := by
      intro x hx y hy hadj
      rcases Finset.mem_insert.mp hx with hxv | hxS <;>
      rcases Finset.mem_insert.mp hy with hyv | hyS
      · subst hxv; subst hyv; exact (G.loopless.irrefl _ hadj).elim
      · have hne : y ≠ v := fun h => hvS (h ▸ hyS)
        subst hxv
        simp only [f1, ↓reduceIte, hne]
        intro h; exact hcv y hyS h.symm
      · have hne : x ≠ v := fun h => hvS (h ▸ hxS)
        subst hyv
        simp only [f1, ↓reduceIte, hne]
        exact hcv x hxS
      · have hxne : x ≠ v := fun h => hvS (h ▸ hxS)
        have hyne : y ≠ v := fun h => hvS (h ▸ hyS)
        simp only [f1, hxne, hyne, ↓reduceIte]
        exact hf x hxS y hyS hadj
    have hsub1 : insert v S ⊆ K := Finset.insert_subset_iff.mpr ⟨hvK, hSK⟩
    have hcard1 : (K \ insert v S).card = n := by
      have h1 := Finset.card_sdiff_add_card_eq_card hSK
      have h2 := Finset.card_sdiff_add_card_eq_card hsub1
      rw [Finset.card_insert_of_notMem hvS] at h2
      omega
    rcases ih (insert v S) hsub1 hcard1 f1 hf1 with ⟨f', hf'eq, hf'valid⟩
    refine ⟨f', ?_, hf'valid⟩
    intro x hxS
    have hne : x ≠ v := fun h => hvS (h ▸ hxS)
    rw [hf'eq x (Finset.mem_insert_of_mem hxS)]
    simp [f1, hne]

/-- **Main Structural Theorem:** For every $p \ge 3$,
$P_{DP}(G_0^{(p)}, p+1) < P_{DP}(G_{2p}^{(p)}, p+1)$. -/
theorem dpColorFun_G0_lt_Gstar {p : ℕ} (hp : 3 ≤ p) :
    dpColorFun (G0 p) (p + 1) < dpColorFun (Gk p (2 * p)) (p + 1) := by
  classical
  rcases exists_min_full_foldCover (Gk p (2 * p)) (p + 1) with ⟨Cstar, hfullStar, hCstar⟩
  rw [← hCstar]
  -- Induced subcover `C0` on `G0 p`
  let C0 : FoldCover (G0 p) (p + 1) :=
    { H :=
        { Adj := fun x y => Cstar.H.Adj (Sum.inl x.1, x.2) (Sum.inl y.1, y.2)
          symm := ⟨fun _ _ h => h.symm⟩
          loopless := ⟨fun _ h => Cstar.H.loopless.irrefl _ h⟩ }
      clique_part := fun u c₁ c₂ hne => Cstar.clique_part (Sum.inl u) c₁ c₂ hne
      adj_subset := fun u v c₁ c₂ hadj => by
        rcases Cstar.adj_subset (Sum.inl u) (Sum.inl v) c₁ c₂ hadj with h | h
        · exact Or.inl (Sum.inl.inj h)
        · exact Or.inr h
      matching_right := fun u v c c₁ c₂ huv h1 h2 =>
        Cstar.matching_right (Sum.inl u) (Sum.inl v) c c₁ c₂
          (fun h => huv (Sum.inl.inj h)) h1 h2 }
  have hfull0 : C0.IsFull := fun u v huv c₁ => hfullStar (Sum.inl u) (Sum.inl v) huv c₁
  -- Express `Cstar.dpColorCount` as sum of extension counts over `C0`-colorings
  let availD : (V0 p → Fin (p + 1)) → Fin (2 * p) → Finset (Fin (p + 1)) := fun f r =>
    Finset.univ.filter (fun c =>
      ∀ x : V0 p, inKp p r.val x → ¬ Cstar.H.Adj (Sum.inl x, f x) (Sum.inr r, c))
  let extCount : (V0 p → Fin (p + 1)) → ℕ := fun f =>
    ∏ r : Fin (2 * p), (availD f r).card
  have hstar_sum : Cstar.dpColorCount =
      ∑ f : { f : V0 p → Fin (p + 1) // C0.IsHColoring f }, extCount f.1 := by
    rw [FoldCover.dpColorCount_eq_card_hColoring]
    let e : { g : V0 p ⊕ Fin (2 * p) → Fin (p + 1) // Cstar.IsHColoring g } ≃
        Σ f : { f : V0 p → Fin (p + 1) // C0.IsHColoring f },
          ∀ r : Fin (2 * p), { c : Fin (p + 1) // c ∈ availD f.1 r } :=
      { toFun := fun ⟨g, hg⟩ =>
          ⟨⟨fun x => g (Sum.inl x), fun u v huv hadj => hg (Sum.inl u) (Sum.inl v) huv hadj⟩,
            fun r => ⟨g (Sum.inr r), Finset.mem_filter.mpr ⟨Finset.mem_univ _, fun x hx =>
              hg (Sum.inl x) (Sum.inr r) hx⟩⟩⟩
        invFun := fun ⟨⟨f, hf⟩, d⟩ =>
          ⟨fun u => match u with | Sum.inl x => f x | Sum.inr r => (d r).1,
            by
              rintro (x | r) (y | s) huv hadj
              · exact hf x y huv hadj
              · exact (Finset.mem_filter.mp (d s).2).2 x huv hadj
              · exact (Finset.mem_filter.mp (d r).2).2 y huv hadj.symm
              · exact huv.elim⟩
        left_inv := fun ⟨g, _⟩ => by
          apply Subtype.ext; funext u; cases u <;> rfl
        right_inv := fun ⟨⟨f, _⟩, d⟩ => rfl }
    rw [Fintype.card_congr e, Fintype.card_sigma]
    refine Finset.sum_congr rfl fun f _ => ?_
    rw [Fintype.card_pi]
    simp [extCount, Fintype.card_coe]
  -- Every `C0`-coloring has `≥ 1` choice at every `d_r`, hence `extCount f ≥ 1`
  have havailD_ge1 : ∀ (f : V0 p → Fin (p + 1)) (r : Fin (2 * p)), 1 ≤ (availD f r).card := by
    intro f r
    let Kr : Finset (V0 p ⊕ Fin (2 * p)) :=
      (Finset.univ.filter (fun x : V0 p => inKp p r.val x)).image Sum.inl
    have hv_not : Sum.inr r ∉ Kr := by simp [Kr]
    have hKcard : Kr.card = p := by
      rw [Finset.card_image_of_injective _ Sum.inl_injective]
      exact card_inKp hp r.isLt
    let fExt : V0 p ⊕ Fin (2 * p) → Fin (p + 1) := fun u =>
      match u with | Sum.inl x => f x | Sum.inr _ => ⟨0, by omega⟩
    let forb := Finset.univ.filter (fun c : Fin (p + 1) =>
      ∃ u ∈ Kr, Cstar.H.Adj (u, fExt u) (Sum.inr r, c))
    have hforb_le : forb.card ≤ p :=
      le_trans (card_forbidden_le Cstar Kr (Sum.inr r) hv_not fExt) hKcard.le
    have hsub : Finset.univ \ forb ⊆ availD f r := by
      intro c hc
      have hnot := (Finset.mem_sdiff.mp hc).2
      refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, fun x hx hadj => hnot ?_⟩
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, Sum.inl x,
        Finset.mem_image.mpr ⟨x, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx⟩, rfl⟩, hadj⟩
    have hsdiff : (Finset.univ \ forb).card = (p + 1) - forb.card := by
      rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ, Fintype.card_fin]
    have hle := Finset.card_le_card hsub
    omega
  have hext_ge1 : ∀ f : V0 p → Fin (p + 1), 1 ≤ extCount f := fun f =>
    Finset.one_le_prod fun r _ => havailD_ge1 f r
  -- Split into Case 1 (`C0.HasCanonicalLabeling`) and Case 2 (`¬ C0.HasCanonicalLabeling`)
  by_cases hcan : C0.HasCanonicalLabeling
  · -- Case 1: `C0` has a canonical labeling, so `Cstar.dpColorCount ≥ C0.dpColorCount = P(G0, p+1) > P_DP(G0, p+1)`
    have hge : C0.dpColorCount ≤ Cstar.dpColorCount := by
      rw [hstar_sum, FoldCover.dpColorCount_eq_card_hColoring]
      calc Fintype.card { f : V0 p → Fin (p + 1) // C0.IsHColoring f }
          = ∑ _f : { f : V0 p → Fin (p + 1) // C0.IsHColoring f }, 1 := by simp
        _ ≤ ∑ f : { f : V0 p → Fin (p + 1) // C0.IsHColoring f }, extCount f.1 :=
          Finset.sum_le_sum fun f _ => hext_ge1 f.1
    rw [FoldCover.dpColorCount_of_hasCanonicalLabeling hcan] at hge
    exact lt_of_lt_of_le (dpColorFun_G0_lt_chromPoly hp) hge
  · -- Case 2: `C0` has no canonical labeling; find `D` with `extCount D ≥ 2`
    let w₀ : V0 p := Sum.inl ⟨0, by omega⟩
    have hw₀_adj : ∀ x : V0 p, x ≠ w₀ → (G0 p).Adj w₀ x := by
      rintro (w | (i | j)) hne
      · exact fun h => hne (congrArg Sum.inl h.symm)
      · trivial
      · trivial
    -- Define `σ x` normalizing all edges incident to `w₀`
    let σ : V0 p → Equiv.Perm (Fin (p + 1)) := fun x =>
      if h : x = w₀ then Equiv.refl (Fin (p + 1))
      else (fullEdgePerm C0 hfull0 (hw₀_adj x h)).symm
    have hσ_w₀ : ∀ x : V0 p, x ≠ w₀ → ∀ c₁ c₂,
        C0.H.Adj (w₀, c₁) (x, c₂) ↔ σ w₀ c₁ = σ x c₂ := by
      intro x hx c₁ c₂
      simp only [σ, hx, ↓reduceDIte, Equiv.refl_apply]
      rw [fullEdgePerm_iff C0 hfull0 (hw₀_adj x hx) c₁ c₂]
      exact (Equiv.eq_symm_apply _).symm
    -- Since `¬ C0.HasCanonicalLabeling`, `σ` fails on some edge `y z` (with `y ≠ w₀, z ≠ w₀`)
    have hbad_edge : ∃ y z : V0 p, (G0 p).Adj y z ∧
        ∃ c₁ c₂ : Fin (p + 1), ¬ (C0.H.Adj (y, c₁) (z, c₂) ↔ σ y c₁ = σ z c₂) := by
      by_contra hall
      push Not at hall
      exact hcan ⟨σ, hall⟩
    rcases hbad_edge with ⟨y, z, hyz, cy, cz, hbad_yz⟩
    have hy_ne : y ≠ w₀ := by
      rintro rfl
      exact hbad_yz (hσ_w₀ z ((G0 p).ne_of_adj hyz).symm cy cz)
    have hz_ne : z ≠ w₀ := by
      rintro rfl
      have h := hσ_w₀ y ((G0 p).ne_of_adj hyz) cz cy
      exact hbad_yz ⟨fun h1 => (h.mp h1.symm).symm, fun h2 => (h.mpr h2.symm).symm⟩
    -- Pick a `p`-clique `K_r` containing `y` and `z` (and automatically `w₀`)
    rcases exists_clique_containing_edge hp hyz with ⟨r, hyK, hzK⟩
    -- Define `τ x` for `x ∈ K_r` as the matching from `x` to `d_r`
    let τ : ∀ x : V0 p, inKp p r.val x → Equiv.Perm (Fin (p + 1)) := fun x hx =>
      fullEdgePerm Cstar hfullStar (u := Sum.inl x) (v := Sum.inr r) hx
    -- Some edge `a b` inside `K_r` fails to match `τ a c₁ = τ b c₂`
    have hbad_ab : ∃ a b : V0 p, ∃ ha : inKp p r.val a, ∃ hb : inKp p r.val b,
        (G0 p).Adj a b ∧ ∃ c₀ : Fin (p + 1),
        ¬ C0.H.Adj (a, (τ a ha).symm c₀) (b, (τ b hb).symm c₀) := by
      by_contra hall
      push Not at hall
      -- Then for ALL `a, b ∈ K_r` with `(G0 p).Adj a b`, `C0.H.Adj (a, c₁) (b, c₂) ↔ τ a c₁ = τ b c₂`
      have hall_iff : ∀ a b : V0 p, ∀ ha : inKp p r.val a, ∀ hb : inKp p r.val b,
          (G0 p).Adj a b → ∀ c₁ c₂, C0.H.Adj (a, c₁) (b, c₂) ↔ τ a ha c₁ = τ b hb c₂ := by
        intro a b ha hb hab c₁ c₂
        constructor
        · intro hadj
          have h1 := hall a b ha hb hab (τ a ha c₁)
          rw [Equiv.symm_apply_apply] at h1
          have hEq := C0.matching_right a b c₁ _ c₂ ((G0 p).ne_of_adj hab) h1 hadj
          rw [← hEq, Equiv.apply_symm_apply]
        · intro hEq
          have h1 := hall a b ha hb hab (τ a ha c₁)
          rw [Equiv.symm_apply_apply, hEq, Equiv.symm_apply_apply] at h1
          exact h1
      -- Relate `τ x` to `τ w₀ ∘ σ x` for `x ∈ {y, z}`
      have hτ_rel : ∀ x : V0 p, ∀ hx : inKp p r.val x, x ≠ w₀ → ∀ c,
          τ x hx c = τ w₀ trivial (σ x c) := by
        intro x hx hne c
        have hadj_w : C0.H.Adj (w₀, σ x c) (x, c) := (hσ_w₀ x hne (σ x c) c).mpr (by simp [σ])
        exact ((hall_iff w₀ x trivial hx (hw₀_adj x hne) (σ x c) c).mp hadj_w).symm
      apply hbad_yz
      rw [hall_iff y z hyK hzK hyz cy cz, hτ_rel y hyK hy_ne cy, hτ_rel z hzK hz_ne cz]
      exact (τ w₀ trivial).injective.eq_iff
    rcases hbad_ab with ⟨a, b, haK, hbK, hab, c₀, hnot_adj⟩
    have hab_ne : a ≠ b := (G0 p).ne_of_adj hab
    -- Start partial coloring on `{a, b}` with `f_init a = (τ a).symm c₀`, `f_init b = (τ b).symm c₀`
    let Kr_fin : Finset (V0 p) := Finset.univ.filter (fun x : V0 p => inKp p r.val x)
    have hKr_card : Kr_fin.card = p := card_inKp hp r.isLt
    let f_init : V0 p → Fin (p + 1) := fun x =>
      if x = a then (τ a haK).symm c₀ else (τ b hbK).symm c₀
    have hSsub : ({a, b} : Finset (V0 p)) ⊆ Kr_fin := by
      intro x hx
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl <;> exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, ‹_›⟩
    have hf_init : ∀ x ∈ ({a, b} : Finset (V0 p)), ∀ y ∈ ({a, b} : Finset (V0 p)),
        (G0 p).Adj x y → ¬ C0.H.Adj (x, f_init x) (y, f_init y) := by
      intro x hx y hy hadj
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx hy
      rcases hx with rfl | rfl <;> rcases hy with rfl | rfl
      · exact ((G0 p).loopless.irrefl _ hadj).elim
      · simp only [f_init, hab_ne.symm, ↓reduceIte]; exact hnot_adj
      · simp only [f_init, hab_ne.symm, ↓reduceIte]; intro h; exact hnot_adj h.symm
      · exact ((G0 p).loopless.irrefl _ hadj).elim
    -- Greedily extend `f_init` to all of `Kr_fin`, then by Lemma 3 to all of `G0 p`
    rcases greedy_extend_on_clique C0 Kr_fin hKr_card (Kr_fin \ {a, b}).card {a, b} hSsub rfl f_init hf_init with
      ⟨fK, hfK_eq, hfK_valid⟩
    rcases precoloring_extension_G0 hp r.isLt C0 fK (fun x y hx hy hadj =>
        hfK_valid x (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx⟩)
          y (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hy⟩) hadj) with
      ⟨D, hD_valid, hD_eq⟩
    -- Prove `(availD D r).card ≥ 2`: colors forbidden at `d_r` are `{τ x (D x) | x ∈ K_r}`,
    -- which has card `≤ p - 1` because `a ≠ b` collide at `c₀`!
    have hDa : D a = (τ a haK).symm c₀ := by
      rw [hD_eq a haK, hfK_eq a (Finset.mem_insert_self a {b})]; simp [f_init]
    have hDb : D b = (τ b hbK).symm c₀ := by
      rw [hD_eq b hbK, hfK_eq b (Finset.mem_insert_of_mem (Finset.mem_singleton_self b))]
      simp [f_init, hab_ne.symm]
    let g_forb : V0 p → Fin (p + 1) := fun x =>
      if hx : inKp p r.val x then τ x hx (D x) else c₀
    have hga : g_forb a = c₀ := by simp [g_forb, haK, hDa]
    have hgb : g_forb b = c₀ := by simp [g_forb, hbK, hDb]
    have himg_eq : Kr_fin.image g_forb = (Kr_fin.erase a).image g_forb := by
      ext c
      simp only [Finset.mem_image, Finset.mem_erase]
      constructor
      · rintro ⟨x, hx, rfl⟩
        by_cases hxa : x = a
        · subst hxa
          refine ⟨b, ⟨hab_ne.symm, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hbK⟩⟩, ?_⟩
          rw [hga, hgb]
        · exact ⟨x, ⟨hxa, hx⟩, rfl⟩
      · rintro ⟨x, ⟨_, hx⟩, rfl⟩
        exact ⟨x, hx, rfl⟩
    have himg_card : (Kr_fin.image g_forb).card ≤ p - 1 := by
      rw [himg_eq]
      calc ((Kr_fin.erase a).image g_forb).card
          ≤ (Kr_fin.erase a).card := Finset.card_image_le
        _ = p - 1 := by
          rw [Finset.card_erase_of_mem (Finset.mem_filter.mpr ⟨Finset.mem_univ _, haK⟩), hKr_card]
    have hsub_avail : Finset.univ \ (Kr_fin.image g_forb) ⊆ availD D r := by
      intro c hc
      have hnot := (Finset.mem_sdiff.mp hc).2
      refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, fun x hx hadj => hnot ?_⟩
      have hEq : τ x hx (D x) = c :=
        (fullEdgePerm_iff Cstar hfullStar (u := Sum.inl x) (v := Sum.inr r) hx (D x) c).mp hadj
      refine Finset.mem_image.mpr ⟨x, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx⟩, ?_⟩
      simp [g_forb, hx, hEq]
    have hD_r_ge2 : 2 ≤ (availD D r).card := by
      have hsdiff : (Finset.univ \ (Kr_fin.image g_forb)).card = (p + 1) - (Kr_fin.image g_forb).card := by
        rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ, Fintype.card_fin]
      have hle := Finset.card_le_card hsub_avail
      omega
    have hD_ext_ge2 : 2 ≤ extCount D := by
      unfold extCount
      rw [← Finset.mul_prod_erase _ _ (Finset.mem_univ r)]
      have hprod_ge1 : 1 ≤ ∏ r' ∈ Finset.univ.erase r, (availD D r').card :=
        Finset.one_le_prod fun r' _ => havailD_ge1 D r'
      nlinarith
    -- Hence `Cstar.dpColorCount ≥ C0.dpColorCount + 1 ≥ dpColorFun (G0 p) (p + 1) + 1`
    let Dsub : { f : V0 p → Fin (p + 1) // C0.IsHColoring f } := ⟨D, hD_valid⟩
    have hge_plus1 : C0.dpColorCount + 1 ≤ Cstar.dpColorCount := by
      rw [hstar_sum, FoldCover.dpColorCount_eq_card_hColoring]
      rw [← Finset.add_sum_erase _ _ (Finset.mem_univ Dsub)]
      have hrest : (Finset.univ.erase Dsub).card ≤
          ∑ f ∈ Finset.univ.erase Dsub, extCount f.1 := by
        calc (Finset.univ.erase Dsub).card
            = ∑ _f ∈ Finset.univ.erase Dsub, 1 := by simp
          _ ≤ ∑ f ∈ Finset.univ.erase Dsub, extCount f.1 :=
            Finset.sum_le_sum fun f _ => hext_ge1 f.1
      have hcard_er : (Finset.univ.erase Dsub).card + 1 =
          Fintype.card { f : V0 p → Fin (p + 1) // C0.IsHColoring f } := by
        rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ]
        have hpos : 0 < Fintype.card { f : V0 p → Fin (p + 1) // C0.IsHColoring f } :=
          Fintype.card_pos_iff.mpr ⟨Dsub⟩
        omega
      have hDsub_ext : 2 ≤ extCount Dsub.1 := hD_ext_ge2
      omega
    have hle0 : dpColorFun (G0 p) (p + 1) ≤ C0.dpColorCount := dpColorFun_le (G0 p) (p + 1) C0
    omega

/-- There exists an explicit step $k \in \{0, \dots, 2p - 1\}$ at which attaching the simplicial
vertex $d_k$ of degree $p$ strictly increases $P_{DP}(\cdot, p+1)$. -/
theorem exists_counterexample_step {p : ℕ} (hp : 3 ≤ p) :
    ∃ k : Fin (2 * p),
      dpColorFun (Gk p k.val) (p + 1) < dpColorFun (Gk p (k.val + 1)) (p + 1) := by
  by_contra hall
  push Not at hall
  have hmono : ∀ n : ℕ, n ≤ 2 * p → dpColorFun (Gk p n) (p + 1) ≤ dpColorFun (Gk p 0) (p + 1) := by
    intro n hn
    induction n with
    | zero => exact le_rfl
    | succ k ih =>
      exact le_trans (hall ⟨k, by omega⟩) (ih (by omega))
  have hle : dpColorFun (Gk p (2 * p)) (p + 1) ≤ dpColorFun (G0 p) (p + 1) := by
    simpa [dpColorFun_congr (GkZeroIso p) (p + 1)] using hmono (2 * p) le_rfl
  exact absurd (dpColorFun_G0_lt_Gstar hp) (not_lt.mpr hle)

/-- Helper product identity: $\prod_{i=0}^{p-1} (p + 1 - i) = (p + 1)!$. -/
private lemma prod_range_sub_eq_factorial (p : ℕ) :
    (∏ i ∈ Finset.range p, ((p + 1) - i)) = (p + 1).factorial := by
  have hgen : ∀ k : ℕ, k ≤ p + 1 →
      (∏ i ∈ Finset.range k, ((p + 1) - i)) = (p + 1).descFactorial k := by
    intro k hk
    induction k with
    | zero => simp
    | succ k ih =>
      rw [Finset.prod_range_succ, ih (by omega), Nat.descFactorial_succ, mul_comm]
  rw [hgen p (by omega)]
  have h1 : (p + 1).descFactorial (p + 1) = (p + 1).descFactorial p := by
    rw [Nat.descFactorial_succ]
    simp
  rw [← h1, Nat.descFactorial_self]

open Classical in
/-- **Refutation of Question 3 (`ques: easier`) of `arXiv:2112.05316v2` for every $p \ge 4$
(in fact every $p \ge 3$):**
There exist a nonempty finite simple graph $G$, a simplicial vertex $v$ of $G$ of degree $p$,
and a positive integer $m = p + 1 \ge d_G(v)$ such that
$$P_{DP}(G, m) > (m - d_G(v)) \cdot P_{DP}(G - \{v\}, m).$$ -/
theorem kaul_question_3_false (p : ℕ) (hp : 3 ≤ p) :
    ∃ (V : Type) (_ : Fintype V) (_ : Nonempty V) (G : SimpleGraph V) (v : V) (m : ℕ),
      IsSimplicial G v ∧
      vertexDeg G v = p ∧
      vertexDeg G v ≤ m ∧
      (m - vertexDeg G v) * dpColorFun (G.induce { u : V | u ≠ v }) m < dpColorFun G m := by
  rcases exists_counterexample_step hp with ⟨k, hlt⟩
  let V := V0 p ⊕ Fin (k.val + 1)
  have hne : Nonempty V := ⟨Sum.inr (Fin.last k.val)⟩
  let G := Gk p (k.val + 1)
  let v : V := Sum.inr (Fin.last k.val)
  refine ⟨V, inferInstance, hne, G, v, p + 1, last_isSimplicial, vertexDeg_last hp k.isLt, ?_, ?_⟩
  · rw [vertexDeg_last hp k.isLt]; omega
  · rw [vertexDeg_last hp k.isLt, show p + 1 - p = 1 by omega, one_mul]
    have hcongr : ∀ {V₁ V₂ : Type} {inst₁ : Fintype V₁} {inst₂ : Fintype V₂}
        {G₁ : SimpleGraph V₁} {G₂ : SimpleGraph V₂} (e : G₁ ≃g G₂),
        @dpColorFun V₁ inst₁ G₁ (p + 1) = @dpColorFun V₂ inst₂ G₂ (p + 1) :=
      fun {V₁ V₂} {inst₁ inst₂} {G₁ G₂} e => @dpColorFun_congr V₁ V₂ inst₁ inst₂ G₁ G₂ e (p + 1)
    refine lt_of_eq_of_lt ?_ hlt
    exact hcongr (GkSuccDeleteIso p k.val)

/-- **Refutation of Question 2 (`ques: classify`) of `arXiv:2112.05316v2` for every $p \ge 4$
(in fact every $p \ge 3$):**
There exist nonempty finite simple graphs $G_1, G_2, G$ with $G \in G_1 \oplus_p G_2$ (a
$K_p$-gluing of $G_1$ and $G_2$) and $m = p + 1 \ge p$ such that
$$P_{DP}(G, m) > \frac{P_{DP}(G_1, m) \cdot P_{DP}(G_2, m)}{\prod_{i=0}^{p-1} (m - i)}.$$ -/
theorem kaul_question_2_false (p : ℕ) (hp : 3 ≤ p) :
    ∃ (V₁ V₂ V : Type) (_ : Fintype V₁) (_ : Nonempty V₁) (_ : Fintype V₂) (_ : Nonempty V₂)
      (_ : Fintype V) (_ : DecidableEq V) (_ : Nonempty V)
      (G₁ : SimpleGraph V₁) (G₂ : SimpleGraph V₂) (G : SimpleGraph V) (m : ℕ),
      p ≤ m ∧
      IsCliqueGluing2 p G₁ G₂ G ∧
      ((dpColorFun G₁ m : ℚ) * (dpColorFun G₂ m : ℚ)) /
        (∏ i ∈ Finset.range p, ((m - i : ℕ) : ℚ)) < (dpColorFun G m : ℚ) := by
  rcases exists_counterexample_step hp with ⟨k, hlt⟩
  let V₁ := V0 p ⊕ Fin k.val
  let V₂ := Fin (p + 1)
  let V := V0 p ⊕ Fin (k.val + 1)
  have hne₁ : Nonempty V₁ := ⟨Sum.inl (Sum.inl ⟨0, by omega⟩)⟩
  have hne₂ : Nonempty V₂ := ⟨⟨0, by omega⟩⟩
  have hne : Nonempty V := ⟨Sum.inr (Fin.last k.val)⟩
  refine ⟨V₁, V₂, V, inferInstance, hne₁, inferInstance, hne₂, inferInstance, inferInstance, hne,
    Gk p k.val, (⊤ : SimpleGraph (Fin (p + 1))), Gk p (k.val + 1), p + 1, by omega,
    Gk_isCliqueGluing2 hp k.isLt, ?_⟩
  rw [dpColorFun_top_eq_factorial (p + 1)]
  have hprod_nat : (∏ i ∈ Finset.range p, ((p + 1) - i)) = (p + 1).factorial :=
    prod_range_sub_eq_factorial p
  have hprod_rat : (∏ i ∈ Finset.range p, (((p + 1) - i : ℕ) : ℚ)) = ((p + 1).factorial : ℚ) := by
    rw [← Nat.cast_prod, hprod_nat]
  rw [hprod_rat]
  have hfac_ne : (((p + 1).factorial : ℕ) : ℚ) ≠ 0 := by
    exact Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero (p + 1))
  rw [mul_div_cancel_right₀ _ hfac_ne]
  exact_mod_cast hlt

end OpenMath.Kaul211205316Ques3

#print axioms OpenMath.Kaul211205316Ques3.kaul_question_3_false
#print axioms OpenMath.Kaul211205316Ques3.kaul_question_2_false
