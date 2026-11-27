import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Data.Finset.Prod
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
# Ackelsberg–Richter (`arXiv:2604.12864v1`, Section 16.1, Question 16.3): Disproof of Finitary Kneser

This file formalizes the refutation of Question 16.3 (*"Finitary form of Kneser's theorem"*) of
Ethan Ackelsberg and Florian K. Richter,
*"An inverse theorem for sumsets of sets of positive density in the integers"*
(`arXiv:2604.12864v1`, Section 16.1, lines 5747–5757):

> **Question 16.3 (Finitary form of Kneser's theorem).** Is it true that for every `ε > 0` and
> `N_0 ∈ ℕ` (`ℕ = {1, 2, 3, ...}`) there exist `D = D(ε, N_0) > 0` and `N_1 = N_1(ε, N_0) ∈ ℕ`
> such that the following holds: For any `α, β > 0`, any `N ≥ N_1`, and any sets
> `A, B ⊂ [N]` (`[N] = {1, ..., N}`) such that
> `min_{N_0 < n ≤ N} |A ∩ [n]| / n ≥ α` and `min_{N_0 < n ≤ N} |B ∩ [n]| / n ≥ β`,
> and `B` intersects every residue class mod `D`, we have
> `|(A + B) ∩ [N]| / N ≥ α + β - ε`?

We refute Question 16.3 **even under the strictly stronger non-trivial hypothesis `α + β < 1`**
(and for **every** `0 < ε < 1/2` and **every** `N_0 ≥ 1`, as well as the concrete parameters
`ε = 1/10`, `α = β = 4/9`) via:
- `A = {1, 3, 5, ...} ∩ [N]` (all odd integers in `[N]`),
- `B = A ∪ {N - D + 1, ..., N}` (which meets every residue class mod `D`),
showing `|A ∩ [n]| / n ≥ 1/2` and `|B ∩ [n]| / n ≥ 1/2` for all `1 ≤ n ≤ N`, while
`|(A + B) ∩ [N]| ≤ N / 2 + D / 2`, violating `|(A + B) ∩ [N]| / N ≥ α + β - ε`.
-/

namespace OpenMath.Ackelsberg260412864Ques163

/-- `[n] = {1, ..., n}` (`arXiv:2604.12864v1`, Section 1 line 405). -/
def intervalOne (n : ℕ) : Finset ℕ := Finset.Icc 1 n

/-- Finite sumset `A + B = {a + b | a ∈ A, b ∈ B}`. -/
def finSumset (A B : Finset ℕ) : Finset ℕ :=
  (A ×ˢ B).image (fun p => p.1 + p.2)

/-- `B` intersects every residue class modulo `D` (`D ≥ 1`). -/
def MeetsAllResidues (B : Finset ℕ) (D : ℕ) : Prop :=
  ∀ r : ℕ, r < D → ∃ b ∈ B, b % D = r

/-- Equivalent `ZMod D` formulation of intersecting every residue class modulo `D`. -/
lemma meetsAllResidues_iff_zmod {B : Finset ℕ} {D : ℕ} (hD : 1 ≤ D) :
    MeetsAllResidues B D ↔ ∀ r : ZMod D, ∃ b ∈ B, (b : ZMod D) = r := by
  have : NeZero D := ⟨by omega⟩
  constructor
  · intro h r
    obtain ⟨b, hb, hmod⟩ := h r.val r.val_lt
    refine ⟨b, hb, ?_⟩
    rw [← ZMod.natCast_mod, hmod, ZMod.natCast_zmod_val]
  · intro h r hr
    obtain ⟨b, hb, hcast⟩ := h (r : ZMod D)
    refine ⟨b, hb, ?_⟩
    have hval := congrArg ZMod.val hcast
    rw [ZMod.val_natCast, ZMod.val_natCast, Nat.mod_eq_of_lt hr] at hval
    exact hval

/-! ## Section 1: Exact Cardinality Bounds for Odd/Even Subsets of Intervals -/

/-- Exact count of odd integers in `[1, n]`: `|{k ∈ [1, n] | Odd k}| = (n + 1) / 2`. -/
lemma card_odd_Icc (n : ℕ) :
    ((intervalOne n).filter (fun k => k % 2 = 1)).card = (n + 1) / 2 := by
  induction n with
  | zero => simp [intervalOne]
  | succ m ih =>
    have hsplit : intervalOne (m + 1) = insert (m + 1) (intervalOne m) := by
      ext x
      simp only [intervalOne, Finset.mem_Icc, Finset.mem_insert]
      omega
    have hnotmem : m + 1 ∉ intervalOne m := by
      simp only [intervalOne, Finset.mem_Icc]
      omega
    rw [hsplit, Finset.filter_insert]
    split_ifs with hodd
    · rw [Finset.card_insert_of_notMem (fun h => hnotmem (Finset.mem_filter.mp h).1), ih]
      omega
    · rw [ih]
      omega

/-- Exact count of even integers in `[1, n]`: `|{k ∈ [1, n] | Even k}| = n / 2`. -/
lemma card_even_Icc (n : ℕ) :
    ((intervalOne n).filter (fun k => k % 2 = 0)).card = n / 2 := by
  induction n with
  | zero => simp [intervalOne]
  | succ m ih =>
    have hsplit : intervalOne (m + 1) = insert (m + 1) (intervalOne m) := by
      ext x
      simp only [intervalOne, Finset.mem_Icc, Finset.mem_insert]
      omega
    have hnotmem : m + 1 ∉ intervalOne m := by
      simp only [intervalOne, Finset.mem_Icc]
      omega
    rw [hsplit, Finset.filter_insert]
    split_ifs with heven
    · rw [Finset.card_insert_of_notMem (fun h => hnotmem (Finset.mem_filter.mp h).1), ih]
      omega
    · rw [ih]
      omega

/-- Upper bound on odd integers in any interval `[a, b]` of length `b + 1 - a`:
if `a ≤ b + 1`, then `|{k ∈ [a, b] | Odd k}| ≤ (b + 2 - a) / 2`. -/
lemma card_odd_Icc_le (a b : ℕ) :
    ((Finset.Icc a b).filter (fun k => k % 2 = 1)).card ≤ (b + 2 - a) / 2 := by
  -- Map `k ↦ k / 2` injectively into `Finset.Icc (a / 2) (b / 2)` (or direct induction on `b`)
  induction b with
  | zero =>
    have hempty : ((Finset.Icc a 0).filter (fun k => k % 2 = 1)) = ∅ := by
      ext x
      simp only [Finset.mem_filter, Finset.mem_Icc, Finset.notMem_empty, iff_false, not_and]
      omega
    rw [hempty, Finset.card_empty]
    exact Nat.zero_le _
  | succ m ih =>
    by_cases hlt : m + 1 < a
    · have hempty : Finset.Icc a (m + 1) = ∅ := Finset.Icc_eq_empty (by omega)
      rw [hempty, Finset.filter_empty, Finset.card_empty]
      exact Nat.zero_le _
    · have hsplit : Finset.Icc a (m + 1) = insert (m + 1) (Finset.Icc a m) := by
        ext x
        simp only [Finset.mem_Icc, Finset.mem_insert]
        omega
      have hnotmem : m + 1 ∉ Finset.Icc a m := by
        simp only [Finset.mem_Icc]
        omega
      rw [hsplit, Finset.filter_insert]
      split_ifs with hodd
      · rw [Finset.card_insert_of_notMem (fun h => hnotmem (Finset.mem_filter.mp h).1)]
        -- If `m + 1` is odd, `m` is even so `m` wasn't counted in `Finset.Icc a m`!
        by_cases ha : a ≤ m
        · have hsub : (Finset.Icc a m).filter (fun k => k % 2 = 1) ⊆
              (Finset.Icc a (m - 1)).filter (fun k => k % 2 = 1) := by
            intro x hx
            simp only [Finset.mem_filter, Finset.mem_Icc] at hx ⊢
            exact ⟨⟨hx.1.1, by omega⟩, hx.2⟩
          -- Direct exact count via `card_odd_Icc`:
          -- `|(Icc a (m+1)).filter odd| = |(Icc 1 (m+1)).filter odd| - |(Icc 1 (a-1)).filter odd|`
          have hdisj : Disjoint ((intervalOne (a - 1)).filter (fun k => k % 2 = 1))
              ((Finset.Icc a m).filter (fun k => k % 2 = 1)) := by
            rw [Finset.disjoint_left]
            intro x hx1 hx2
            simp only [intervalOne, Finset.mem_filter, Finset.mem_Icc] at hx1 hx2
            omega
          have hunion : ((intervalOne (a - 1)).filter (fun k => k % 2 = 1)) ∪
              ((Finset.Icc a m).filter (fun k => k % 2 = 1)) ⊆
              (intervalOne m).filter (fun k => k % 2 = 1) := by
            intro x hx
            simp only [intervalOne, Finset.mem_union, Finset.mem_filter, Finset.mem_Icc] at hx ⊢
            rcases hx with ⟨⟨h1, h2⟩, h3⟩ | ⟨⟨h1, h2⟩, h3⟩
            · exact ⟨⟨h1, by omega⟩, h3⟩
            · exact ⟨⟨by omega, h2⟩, h3⟩
          have hle := Finset.card_le_card hunion
          rw [Finset.card_union_of_disjoint hdisj, card_odd_Icc, card_odd_Icc] at hle
          omega
        · have hempty : (Finset.Icc a m) = ∅ := Finset.Icc_eq_empty (by omega)
          rw [hempty, Finset.filter_empty, Finset.card_empty]
          omega
      · exact le_trans ih (by omega)

/-- Any interval of `D` consecutive integers `{N - D + 1, ..., N}` (with `D ≤ N`) meets every
residue class modulo `D`. -/
lemma Icc_consecutive_meetsAllResidues {N D : ℕ} (hD : 1 ≤ D) (hDN : D ≤ N) :
    MeetsAllResidues (Finset.Icc (N - D + 1) N) D := by
  intro r hr
  let start := N - D + 1
  let offset := (r + D - start % D) % D
  have hoff : offset < D := Nat.mod_lt _ (by omega)
  refine ⟨start + offset, ?_, ?_⟩
  · simp only [Finset.mem_Icc, start]
    omega
  · have hlt : start % D < D := Nat.mod_lt _ (by omega)
    calc (start + offset) % D
        = (start % D + offset % D) % D := Nat.add_mod _ _ _
      _ = (start % D + (r + D - start % D) % D) % D := by rw [Nat.mod_eq_of_lt hoff]
      _ = (start % D % D + (r + D - start % D) % D) % D := by rw [Nat.mod_mod]
      _ = (start % D + (r + D - start % D)) % D := (Nat.add_mod _ _ _).symm
      _ = (r + D) % D := by rw [show start % D + (r + D - start % D) = r + D by omega]
      _ = r := by rw [Nat.add_mod_right, Nat.mod_eq_of_lt hr]

/-! ## Section 2: Counterexample Construction & Exact Bounds -/

/-- Counterexample set `A = (2ℕ - 1) ∩ [N] = {1, 3, 5, ...} ∩ [N]`. -/
def cexA (N : ℕ) : Finset ℕ :=
  (intervalOne N).filter (fun k => k % 2 = 1)

/-- Counterexample set `B = A ∪ {N - D + 1, ..., N}`. -/
def cexB (N D : ℕ) : Finset ℕ :=
  cexA N ∪ Finset.Icc (N - D + 1) N

lemma cexA_subset_interval (N : ℕ) : cexA N ⊆ intervalOne N :=
  Finset.filter_subset _ _

lemma cexB_subset_interval (N D : ℕ) : cexB N D ⊆ intervalOne N := by
  intro x hx
  simp only [cexB, cexA, intervalOne, Finset.mem_union, Finset.mem_filter, Finset.mem_Icc] at hx ⊢
  rcases hx with ⟨h, _⟩ | ⟨h1, h2⟩
  · exact h
  · exact ⟨by omega, h2⟩

lemma cexA_prefix_density {N n : ℕ} (hn1 : 1 ≤ n) (hnN : n ≤ N) :
    ((cexA N ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ 1 / 2 := by
  have heq : cexA N ∩ intervalOne n = (intervalOne n).filter (fun k => k % 2 = 1) := by
    ext x
    simp only [cexA, intervalOne, Finset.mem_inter, Finset.mem_filter, Finset.mem_Icc]
    omega
  rw [heq, card_odd_Icc]
  have hn_pos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr (by omega)
  rw [ge_iff_le, div_le_div_iff₀ (by norm_num) hn_pos]
  have hnat : n ≤ 2 * ((n + 1) / 2) := by omega
  have hcast : (n : ℝ) ≤ 2 * (((n + 1) / 2 : ℕ) : ℝ) := by exact_mod_cast hnat
  linarith

lemma cexB_prefix_density {N D n : ℕ} (hn1 : 1 ≤ n) (hnN : n ≤ N) :
    ((cexB N D ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ 1 / 2 := by
  have hsub : cexA N ∩ intervalOne n ⊆ cexB N D ∩ intervalOne n := by
    intro x hx
    simp only [cexB, Finset.mem_inter, Finset.mem_union] at hx ⊢
    exact ⟨Or.inl hx.1, hx.2⟩
  have hcard : ((cexA N ∩ intervalOne n).card : ℝ) ≤ ((cexB N D ∩ intervalOne n).card : ℝ) :=
    Nat.cast_le.mpr (Finset.card_le_card hsub)
  have hA := cexA_prefix_density hn1 hnN
  have hn_nonneg : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  exact le_trans hA (div_le_div_of_nonneg_right hcard hn_nonneg)

lemma cexB_meetsAllResidues {N D : ℕ} (hD : 1 ≤ D) (hDN : D ≤ N) :
    MeetsAllResidues (cexB N D) D := by
  intro r hr
  obtain ⟨b, hb, hmod⟩ := Icc_consecutive_meetsAllResidues hD hDN r hr
  exact ⟨b, Finset.mem_union_right _ hb, hmod⟩

/-- Exact structural upper bound `|(A + B) ∩ [N]| ≤ N / 2 + D / 2` for `1 ≤ D ≤ N`. -/
theorem cex_sumset_card_le {N D : ℕ} (hD : 1 ≤ D) (hDN : D ≤ N) :
    (finSumset (cexA N) (cexB N D) ∩ intervalOne N).card ≤ N / 2 + D / 2 := by
  have hsub : finSumset (cexA N) (cexB N D) ∩ intervalOne N ⊆
      ((intervalOne N).filter (fun k => k % 2 = 0)) ∪
      ((Finset.Icc (N - D + 2) N).filter (fun k => k % 2 = 1)) := by
    intro x hx
    simp only [finSumset, Finset.mem_inter, Finset.mem_image, Finset.mem_product,
      Finset.mem_union, Finset.mem_filter, intervalOne, Finset.mem_Icc] at hx ⊢
    rcases hx with ⟨⟨⟨a, b⟩, ⟨ha, hb⟩, rfl⟩, hx1, hxN⟩
    simp only [cexA, intervalOne, Finset.mem_filter, Finset.mem_Icc] at ha
    simp only [cexB, cexA, intervalOne, Finset.mem_union, Finset.mem_filter, Finset.mem_Icc] at hb
    rcases hb with ⟨⟨_, _⟩, hb_odd⟩ | ⟨hb1, _⟩
    · left
      exact ⟨⟨hx1, hxN⟩, by omega⟩
    · by_cases hbe : b % 2 = 1
      · left
        exact ⟨⟨hx1, hxN⟩, by omega⟩
      · right
        exact ⟨⟨by omega, hxN⟩, by omega⟩
  have h1 := Finset.card_le_card hsub
  have h2 := Finset.card_union_le ((intervalOne N).filter (fun k => k % 2 = 0))
    ((Finset.Icc (N - D + 2) N).filter (fun k => k % 2 = 1))
  have h3 := card_even_Icc N
  have h4 := card_odd_Icc_le (N - D + 2) N
  have h5 : (N + 2 - (N - D + 2)) / 2 = D / 2 := by congr 1; omega
  omega

/-! ## Section 3: Main Refutations (General `0 < ε < 1/2` and Concrete `ε = 1/10`) -/

/-- **General Refutation (for EVERY `0 < ε < 1/2` and EVERY `N_0 ≥ 1`, even with `α + β < 1`):**
No `(D, N_1)` can satisfy the finitary Kneser inequality of Question 16.3. -/
theorem refutes_ackelsberg_question_16_3_general
    {ε : ℝ} (hε0 : 0 < ε) (hε_lt : ε < 1 / 2)
    (N₀ : ℕ) (hN₀ : 1 ≤ N₀) (D : ℕ) (hD : 1 ≤ D) (N₁ : ℕ) :
    ∃ (α β : ℝ) (N : ℕ) (A B : Finset ℕ),
      0 < α ∧ 0 < β ∧ α + β < 1 ∧ N₁ ≤ N ∧ N₀ < N ∧
      A ⊆ intervalOne N ∧ B ⊆ intervalOne N ∧
      (∀ n : ℕ, N₀ < n → n ≤ N → ((A ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ α) ∧
      (∀ n : ℕ, N₀ < n → n ≤ N → ((B ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ β) ∧
      MeetsAllResidues B D ∧
      ((finSumset A B ∩ intervalOne N).card : ℝ) / (N : ℝ) < α + β - ε := by
  let η : ℝ := (1 / 2 - ε) / 4
  have hη_pos : 0 < η := by dsimp [η]; linarith
  have hη_lt : η < 1 / 2 := by dsimp [η]; linarith
  let α : ℝ := 1 / 2 - η
  have hα_pos : 0 < α := by dsimp [α]; linarith
  have hgap_pos : 0 < 1 / 2 - ε - 2 * η := by dsimp [η]; linarith
  obtain ⟨M, hM⟩ := exists_nat_gt ((D : ℝ) / (1 / 2 - ε - 2 * η))
  let N : ℕ := max (max N₁ (N₀ + 1)) (max D M)
  have hN1 : N₁ ≤ N := le_trans (le_max_left _ _) (le_max_left _ _)
  have hN0 : N₀ < N := lt_of_lt_of_le (Nat.lt_succ_self N₀)
    (le_trans (le_max_right _ _) (le_max_left _ _))
  have hDN : D ≤ N := le_trans (le_max_left _ _) (le_max_right _ _)
  have hMN : M ≤ N := le_trans (le_max_right _ _) (le_max_right _ _)
  have hN_pos : (0 : ℝ) < (N : ℝ) := Nat.cast_pos.mpr (by omega)
  refine ⟨α, α, N, cexA N, cexB N D, hα_pos, hα_pos, by dsimp [α]; linarith,
    hN1, hN0, cexA_subset_interval N, cexB_subset_interval N D, ?_, ?_,
    cexB_meetsAllResidues hD hDN, ?_⟩
  · intro n hn0 hnN
    exact le_trans (by dsimp [α]; linarith) (cexA_prefix_density (by omega) hnN)
  · intro n hn0 hnN
    exact le_trans (by dsimp [α]; linarith) (cexB_prefix_density (by omega) hnN)
  · have hcard : ((finSumset (cexA N) (cexB N D) ∩ intervalOne N).card : ℝ) ≤
        (N : ℝ) / 2 + (D : ℝ) / 2 := by
      have hnat := cex_sumset_card_le hD hDN
      have h1 : (N / 2 : ℕ) * 2 ≤ N := Nat.div_mul_le_self N 2
      have h2 : (D / 2 : ℕ) * 2 ≤ D := Nat.div_mul_le_self D 2
      have hc1 : ((N / 2 : ℕ) : ℝ) ≤ (N : ℝ) / 2 := by
        have : ((N / 2 : ℕ) : ℝ) * 2 ≤ (N : ℝ) := by exact_mod_cast h1
        linarith
      have hc2 : ((D / 2 : ℕ) : ℝ) ≤ (D : ℝ) / 2 := by
        have : ((D / 2 : ℕ) : ℝ) * 2 ≤ (D : ℝ) := by exact_mod_cast h2
        linarith
      have hnatR : ((finSumset (cexA N) (cexB N D) ∩ intervalOne N).card : ℝ) ≤
          ((N / 2 : ℕ) : ℝ) + ((D / 2 : ℕ) : ℝ) := by exact_mod_cast hnat
      linarith
    have hdiv : ((finSumset (cexA N) (cexB N D) ∩ intervalOne N).card : ℝ) / (N : ℝ) ≤
        1 / 2 + (D : ℝ) / (2 * (N : ℝ)) := by
      have h := div_le_div_of_nonneg_right hcard hN_pos.le
      have hsimp : ((N : ℝ) / 2 + (D : ℝ) / 2) / (N : ℝ) = 1 / 2 + (D : ℝ) / (2 * (N : ℝ)) := by
        field_simp [hN_pos.ne']
      linarith
    have hDN_small : (D : ℝ) / (2 * (N : ℝ)) < 1 / 2 - ε - 2 * η := by
      have hN_gt : (D : ℝ) / (1 / 2 - ε - 2 * η) < (N : ℝ) :=
        lt_of_lt_of_le hM (Nat.cast_le.mpr hMN)
      have hmul : (D : ℝ) < (N : ℝ) * (1 / 2 - ε - 2 * η) :=
        (div_lt_iff₀ hgap_pos).mp hN_gt
      rw [div_lt_iff₀ (by positivity : (0 : ℝ) < 2 * (N : ℝ))]
      nlinarith
    dsimp [α]
    linarith

/-- **Direct Negation of Ackelsberg–Richter (`arXiv:2604.12864v1`, Section 16.1, Question 16.3):**
Even restricting to `α + β < 1`, Question 16.3 is false (taking `ε = 1/10`, `N_0 = 1`). -/
theorem not_ackelsberg_question_16_3 :
    ¬ (∀ ε : ℝ, 0 < ε → ∀ N₀ : ℕ, 1 ≤ N₀ →
        ∃ (D N₁ : ℕ), 1 ≤ D ∧ 1 ≤ N₁ ∧
          ∀ (α β : ℝ) (N : ℕ) (A B : Finset ℕ),
            0 < α → 0 < β → α + β < 1 → N₁ ≤ N →
            A ⊆ intervalOne N → B ⊆ intervalOne N →
            (∀ n : ℕ, N₀ < n → n ≤ N → ((A ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ α) →
            (∀ n : ℕ, N₀ < n → n ≤ N → ((B ∩ intervalOne n).card : ℝ) / (n : ℝ) ≥ β) →
            MeetsAllResidues B D →
            ((finSumset A B ∩ intervalOne N).card : ℝ) / (N : ℝ) ≥ α + β - ε) := by
  intro hall
  obtain ⟨D, N₁, hD, _, hspec⟩ := hall (1 / 10) (by norm_num) 1 le_rfl
  obtain ⟨α, β, N, A, B, hα, hβ, hsum, hN1, _, hAsub, hBsub, hAdens, hBdens, hres, hfail⟩ :=
    refutes_ackelsberg_question_16_3_general (ε := 1 / 10) (by norm_num) (by norm_num) 1 le_rfl D hD N₁
  have hge := hspec α β N A B hα hβ hsum hN1 hAsub hBsub hAdens hBdens hres
  linarith

#print axioms cex_sumset_card_le
#print axioms refutes_ackelsberg_question_16_3_general
#print axioms not_ackelsberg_question_16_3

end OpenMath.Ackelsberg260412864Ques163
