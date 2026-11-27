import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Fin

/-!
# Refutation of Conjecture 7 (`conj:ore`) of Li–Lu–Luo (`arXiv:2505.12035v1`)

Primary source:
Yupei Li, Linyuan Lu, Ruth Luo, *"An Ore-type theorem for `[3]`-graphs"*,
`arXiv:2505.12035v1` (2025-05-17), Section 1, Conjecture 7 (`\label{conj:ore}`):

> Let `n ≥ 6`, and let `H` be a `[3]`-graph on `n` vertices such that every pair `u, v ∈ V(H)`
> of non-adjacent vertices satisfies `d_{∂H}(u) + d_{∂H}(v) ≥ n + 1`.
> Then `H` contains a Hamiltonian Berge cycle.

We formalize the exact definitions from Section 1 (`[3]`-graph, `2`-shadow `∂H`, shadow degree
`d_{∂H}`, Hamiltonian Berge cycle) and prove two explicit counterexamples:
1. **Witness 1 (`n = 6`):** Connected `3`-uniform hypergraph with `5` edges whose shadow is
   `K_{2,2,2}` (`4`-regular, so every non-adjacent pair has degree sum `8 = n + 2 > n + 1`),
   having no Hamiltonian Berge cycle (`|E| = 5 < 6`).
2. **Witness 2 (`n = 7`):** Connected, **linear** `3`-uniform hypergraph (Fano plane minus one
   line, `6` edges) with every non-adjacent pair having degree sum `8 = n + 1`, having no
   Hamiltonian Berge cycle (`|E| = 6 < 7`).
-/

namespace OpenMath.Li250512035Conj7

/-- A simple `[3]`-graph on vertex set `Fin n`: a finite set of hyperedges, each containing
between `1` and `3` vertices (Section 1 of `arXiv:2505.12035v1`). -/
structure Hypergraph3 (n : ℕ) where
  edges : Finset (Finset (Fin n))
  edge_card : ∀ e ∈ edges, 1 ≤ e.card ∧ e.card ≤ 3

/-- A `[3]`-graph is `3`-uniform if every hyperedge has cardinality `3`. -/
def Hypergraph3.IsUniform3 {n : ℕ} (H : Hypergraph3 n) : Prop :=
  ∀ e ∈ H.edges, e.card = 3

/-- A `[3]`-graph is linear if any two distinct hyperedges intersect in at most one vertex. -/
def Hypergraph3.IsLinear {n : ℕ} (H : Hypergraph3 n) : Prop :=
  ∀ e₁ ∈ H.edges, ∀ e₂ ∈ H.edges, e₁ ≠ e₂ → (e₁ ∩ e₂).card ≤ 1

/-- Adjacency in the `2`-shadow graph `∂H`: distinct vertices `u, v` contained in a common
hyperedge `e ∈ E(H)`. -/
def Hypergraph3.shadowAdj {n : ℕ} (H : Hypergraph3 n) (u v : Fin n) : Prop :=
  u ≠ v ∧ ∃ e ∈ H.edges, u ∈ e ∧ v ∈ e

instance {n : ℕ} (H : Hypergraph3 n) (u v : Fin n) : Decidable (H.shadowAdj u v) := by
  unfold Hypergraph3.shadowAdj
  infer_instance

/-- Shadow degree `d_{∂H}(u) = |N_H(u)|`: number of vertices adjacent to `u` in `∂H`. -/
def Hypergraph3.shadowDeg {n : ℕ} (H : Hypergraph3 n) (u : Fin n) : ℕ :=
  (Finset.univ.filter (fun v => H.shadowAdj u v)).card

/-- Ore-type shadow degree condition with parameter `d₀`:
every pair of distinct non-adjacent vertices `u, v` satisfies `d_{∂H}(u) + d_{∂H}(v) ≥ n + d₀`. -/
def Hypergraph3.SatisfiesOre {n : ℕ} (H : Hypergraph3 n) (d₀ : ℕ) : Prop :=
  ∀ u v : Fin n, u ≠ v → ¬ H.shadowAdj u v → n + d₀ ≤ H.shadowDeg u + H.shadowDeg v

instance {n : ℕ} (H : Hypergraph3 n) (d₀ : ℕ) : Decidable (H.SatisfiesOre d₀) := by
  unfold Hypergraph3.SatisfiesOre
  infer_instance

/-- Diameter `≤ 2` in the `2`-shadow graph (in particular, `H` is connected). -/
def Hypergraph3.ShadowDiamLeTwo {n : ℕ} (H : Hypergraph3 n) : Prop :=
  ∀ u v : Fin n, u = v ∨ H.shadowAdj u v ∨ ∃ w : Fin n, H.shadowAdj u w ∧ H.shadowAdj w v

instance {n : ℕ} (H : Hypergraph3 n) : Decidable H.ShadowDiamLeTwo := by
  unfold Hypergraph3.ShadowDiamLeTwo
  infer_instance

/-- A Hamiltonian Berge cycle in `H` (`n ≥ 1`): `n` distinct vertices `v_0, ..., v_{n-1}` and
`n` distinct hyperedges `e_0, ..., e_{n-1} ∈ E(H)` such that `{v_i, v_{i+1}} ⊆ e_i` cyclically
for all `i ∈ Fin n`. -/
def Hypergraph3.HasHamiltonianBergeCycle {n : ℕ} [NeZero n] (H : Hypergraph3 n) : Prop :=
  ∃ (v : Fin n → Fin n) (e : Fin n → Finset (Fin n)),
    Function.Injective v ∧
    Function.Injective e ∧
    (∀ i : Fin n, e i ∈ H.edges) ∧
    (∀ i : Fin n, v i ∈ e i ∧ v (i + 1) ∈ e i)

/-- Any `[3]`-graph on `n ≥ 1` vertices with fewer than `n` hyperedges has no Hamiltonian Berge
cycle (by pigeonhole on the `n` distinct hyperedges required). -/
theorem no_hamiltonian_berge_cycle_of_card_lt {n : ℕ} [NeZero n]
    (H : Hypergraph3 n) (hlt : H.edges.card < n) :
    ¬ H.HasHamiltonianBergeCycle := by
  rintro ⟨_, e, _, he_inj, he_mem, _⟩
  have hsub : Finset.univ.image e ⊆ H.edges := by
    intro x hx
    rcases Finset.mem_image.mp hx with ⟨i, _, rfl⟩
    exact he_mem i
  have hcard : n ≤ H.edges.card := by
    calc
      n = (Finset.univ : Finset (Fin n)).card := (Finset.card_fin n).symm
      _ = (Finset.univ.image e).card := (Finset.card_image_of_injective _ he_inj).symm
      _ ≤ H.edges.card := Finset.card_le_card hsub
  omega

/-! ## Witness 1: `n = 6`, `5` triples, `d_{∂H}(u) + d_{∂H}(v) = 8 = n + 2 > n + 1` -/

/-- Explicit `3`-uniform counterexample on `6` vertices with `5` hyperedges. -/
def witness1 : Hypergraph3 6 where
  edges :=
    { ({0, 1, 2} : Finset (Fin 6)),
      ({0, 1, 3} : Finset (Fin 6)),
      ({0, 2, 4} : Finset (Fin 6)),
      ({1, 2, 5} : Finset (Fin 6)),
      ({3, 4, 5} : Finset (Fin 6)) }
  edge_card := by decide

theorem witness1_isUniform3 : witness1.IsUniform3 := by
  intro e he
  simp only [witness1, Finset.mem_insert, Finset.mem_singleton] at he
  rcases he with rfl | rfl | rfl | rfl | rfl <;> decide
theorem witness1_connected : witness1.ShadowDiamLeTwo := by decide
theorem witness1_edges_card : witness1.edges.card = 5 := by decide
theorem witness1_shadowDeg_eq_four : ∀ u : Fin 6, witness1.shadowDeg u = 4 := by decide
theorem witness1_satisfiesOre_two : witness1.SatisfiesOre 2 := by decide
theorem witness1_satisfiesOre_one : witness1.SatisfiesOre 1 := by decide

theorem witness1_no_hamiltonian_berge_cycle : ¬ witness1.HasHamiltonianBergeCycle :=
  no_hamiltonian_berge_cycle_of_card_lt witness1 (by rw [witness1_edges_card]; omega)

/-! ## Witness 2: `n = 7`, `6` triples (Fano plane minus a line), linear `3`-uniform -/

/-- Explicit linear `3`-uniform counterexample on `7` vertices with `6` hyperedges
(Fano plane `STS(7)` minus `{0, 1, 2}`). -/
def witness2 : Hypergraph3 7 where
  edges :=
    { ({0, 3, 4} : Finset (Fin 7)),
      ({0, 5, 6} : Finset (Fin 7)),
      ({1, 3, 5} : Finset (Fin 7)),
      ({1, 4, 6} : Finset (Fin 7)),
      ({2, 3, 6} : Finset (Fin 7)),
      ({2, 4, 5} : Finset (Fin 7)) }
  edge_card := by
    intro e he
    simp only [Finset.mem_insert, Finset.mem_singleton] at he
    rcases he with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

theorem witness2_isUniform3 : witness2.IsUniform3 := by
  intro e he
  simp only [witness2, Finset.mem_insert, Finset.mem_singleton] at he
  rcases he with rfl | rfl | rfl | rfl | rfl | rfl <;> decide

theorem witness2_isLinear : witness2.IsLinear := by
  intro e₁ he₁ e₂ he₂ hne
  simp only [witness2, Finset.mem_insert, Finset.mem_singleton] at he₁ he₂
  rcases he₁ with rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases he₂ with rfl | rfl | rfl | rfl | rfl | rfl <;>
    first | exact absurd rfl hne | decide

theorem witness2_connected : witness2.ShadowDiamLeTwo := by decide
theorem witness2_edges_card : witness2.edges.card = 6 := by decide
theorem witness2_satisfiesOre_one : witness2.SatisfiesOre 1 := by decide

theorem witness2_no_hamiltonian_berge_cycle : ¬ witness2.HasHamiltonianBergeCycle :=
  no_hamiltonian_berge_cycle_of_card_lt witness2 (by rw [witness2_edges_card]; omega)

/-! ## Direct Refutation of Conjecture 7 (`conj:ore`) -/

/-- **Refutation of Li–Lu–Luo Conjecture 7 (`arXiv:2505.12035v1`):**
Even restricted to connected `3`-uniform hypergraphs satisfying the stronger Ore bound
`d_{∂H}(u) + d_{∂H}(v) ≥ n + 2`, Conjecture 7 fails at `n = 6`. -/
theorem not_li_lu_luo_conjecture_7 :
    ¬ (∀ (n : ℕ) [NeZero n], 6 ≤ n →
        ∀ H : Hypergraph3 n, H.SatisfiesOre 1 → H.HasHamiltonianBergeCycle) := by
  intro hconj
  exact witness1_no_hamiltonian_berge_cycle (hconj 6 (by omega) witness1 witness1_satisfiesOre_one)

/-- **Linear `3`-Uniform Refutation at `n = 7`:**
Conjecture 7 also fails when restricted to connected **linear** `3`-uniform hypergraphs. -/
theorem not_li_lu_luo_conjecture_7_linear_uniform :
    ¬ (∀ (n : ℕ) [NeZero n], 6 ≤ n →
        ∀ H : Hypergraph3 n,
          H.IsUniform3 → H.IsLinear → H.ShadowDiamLeTwo → H.SatisfiesOre 1 →
            H.HasHamiltonianBergeCycle) := by
  intro hconj
  exact witness2_no_hamiltonian_berge_cycle
    (hconj 7 (by omega) witness2 witness2_isUniform3 witness2_isLinear
      witness2_connected witness2_satisfiesOre_one)

#print axioms witness1_no_hamiltonian_berge_cycle
#print axioms witness2_no_hamiltonian_berge_cycle
#print axioms not_li_lu_luo_conjecture_7
#print axioms not_li_lu_luo_conjecture_7_linear_uniform

end OpenMath.Li250512035Conj7
