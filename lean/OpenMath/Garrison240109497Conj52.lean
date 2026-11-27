import Mathlib.Data.Nat.ChineseRemainder
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.Factorization.LCM
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

/-!
# Garrison–Seiler–Knowles (2024) — Proof of Conjecture 5.2 (`arXiv:2401.09497v1`, `conj:1 at end`)

This file formalizes the complete proof of **Conjecture 5.2** (`\label{conj:1 at end}`) from
Thomas Garrison, Chris Seiler, and Andrew Knowles, *"Weakly Consecutive Sequences"*,
`arXiv:2401.09497v1` (Section 1, Definition 1.1; Section 5, lines 718–720):

* **Definition 1.1:** A permutation `σ : [k] → [k]` is *weakly consecutive* (a WCS) if for all
  `i, j ∈ [k]` and integers `m`, `m ∣ σ(i)` and `m ∣ (i - j)` implies `m ∣ σ(j)`.
* **Conjecture 5.2 (`conj:1 at end`):** Any WCS either begins or ends with the term `1`
  (i.e., `σ(1) = 1` or `σ(k) = 1`).

## Main Results

* `OpenMath.Garrison240109497Conj52.wcs_residue_class`:
  Lemma 2 — for every `m ∈ [1, k]`, `{i ∈ [1, k] | m ∣ σ i} = {i ∈ [1, k] | i ≡ c_m (mod m)}`
  with `c_m ∈ [1, m]` and `c_m > k % m`.
* `OpenMath.Garrison240109497Conj52.wcs_gcd_repr`:
  Lemma 3 — there exists `a : ℕ` such that `σ i = Nat.gcd (a + i) (lcm(1..k))` for all `i ∈ [1, k]`.
* `OpenMath.Garrison240109497Conj52.garrison_conjecture_5_2`:
  For every `k ≥ 1` and every weakly consecutive permutation `σ` of `{1, ..., k}`,
  `σ 1 = 1 ∨ σ k = 1`.
* `OpenMath.Garrison240109497Conj52.garrison_conjecture_5_2_perm`:
  Equivalent formulation directly for `σ : Equiv.Perm (Fin k)`.
-/

namespace OpenMath.Garrison240109497Conj52

open scoped BigOperators

/-! ## Section 1: Primary-Source Definitions and Reversal Lemma -/

/-- Definition 1.1 (`arXiv:2401.09497v1`): `σ` is a weakly consecutive permutation of `[k] = {1..k}`. -/
def IsWeaklyConsecutive (k : ℕ) (σ : ℕ → ℕ) : Prop :=
  Set.BijOn σ (Set.Icc 1 k) (Set.Icc 1 k) ∧
  ∀ i ∈ Set.Icc 1 k, ∀ j ∈ Set.Icc 1 k, ∀ m : ℤ,
    m ∣ (σ i : ℤ) → m ∣ ((i : ℤ) - (j : ℤ)) → m ∣ (σ j : ℤ)

/-- Weakly consecutive condition stated directly on `Equiv.Perm (Fin k)` (1-based values `val + 1`). -/
def IsWeaklyConsecutivePerm {k : ℕ} (σ : Equiv.Perm (Fin k)) : Prop :=
  ∀ i j : Fin k, ∀ m : ℤ,
    m ∣ ((σ i).val + 1 : ℤ) → m ∣ (((i.val + 1 : ℕ) : ℤ) - ((j.val + 1 : ℕ) : ℤ)) →
      m ∣ ((σ j).val + 1 : ℤ)

/-- Lemma 1 (Reversal): `i ↦ σ (k + 1 - i)` is also weakly consecutive. -/
lemma wcs_rev {k : ℕ} {σ : ℕ → ℕ} (hσ : IsWeaklyConsecutive k σ) :
    IsWeaklyConsecutive k (fun i => σ (k + 1 - i)) := by
  have hflip_mem : ∀ i ∈ Set.Icc 1 k, k + 1 - i ∈ Set.Icc 1 k := by
    intro i hi; simp only [Set.mem_Icc] at hi ⊢; omega
  refine ⟨⟨?_, ?_, ?_⟩, ?_⟩
  · intro i hi; exact hσ.1.mapsTo (hflip_mem i hi)
  · intro i hi j hj heq
    have h1 := hσ.1.injOn (hflip_mem i hi) (hflip_mem j hj) heq
    simp only [Set.mem_Icc] at hi hj
    omega
  · intro y hy
    rcases hσ.1.surjOn hy with ⟨x, hx, rfl⟩
    refine ⟨k + 1 - x, hflip_mem x hx, ?_⟩
    simp only [Set.mem_Icc] at hx
    dsimp only
    rw [show k + 1 - (k + 1 - x) = x by omega]
  · intro i hi j hj m hdiv hsub
    have hsub' : m ∣ (((k + 1 - i : ℕ) : ℤ) - ((k + 1 - j : ℕ) : ℤ)) := by
      simp only [Set.mem_Icc] at hi hj
      have heq : (((k + 1 - i : ℕ) : ℤ) - ((k + 1 - j : ℕ) : ℤ)) = -((i : ℤ) - (j : ℤ)) := by
        omega
      rw [heq]
      exact dvd_neg.mpr hsub
    exact hσ.2 (k + 1 - i) (hflip_mem i hi) (k + 1 - j) (hflip_mem j hj) m hdiv hsub'

/-! ## Section 2: Lemma 2 (Residue-Class Characterization) -/

/-- Lemma 2: For every `m ∈ [1, k]`, let `i₀ ∈ [1, k]` be the unique preimage `σ i₀ = m` and
`c = ((i₀ - 1) % m) + 1 ∈ [1, m]`. Then `c > k % m`, and for every `i ∈ [1, k]`,
`m ∣ σ i ↔ (m : ℤ) ∣ (i : ℤ) - (c : ℤ)` (equivalently `i % m = c % m`). -/
lemma wcs_residue_class {k m : ℕ} {σ : ℕ → ℕ} (hσ : IsWeaklyConsecutive k σ)
    (hm1 : 1 ≤ m) (hmk : m ≤ k) :
    ∃ c : ℕ, 1 ≤ c ∧ c ≤ m ∧ k % m < c ∧
      (∀ i ∈ Set.Icc 1 k, m ∣ σ i ↔ (m : ℤ) ∣ (i : ℤ) - (c : ℤ)) ∧
      (∀ i₀ ∈ Set.Icc 1 k, σ i₀ = m → (m : ℤ) ∣ (i₀ : ℤ) - (c : ℤ)) := by
  classical
  rcases hσ.1.surjOn (show m ∈ Set.Icc 1 k from ⟨hm1, hmk⟩) with ⟨i₀, hi₀_mem, hσi₀⟩
  have hi₀_1 : 1 ≤ i₀ := hi₀_mem.1
  let c : ℕ := ((i₀ - 1) % m) + 1
  have hc1 : 1 ≤ c := by dsimp [c]; omega
  have hcm : c ≤ m := by
    dsimp [c]
    have := Nat.mod_lt (i₀ - 1) (by omega : 0 < m)
    omega
  have hi₀_cong : (m : ℤ) ∣ (i₀ : ℤ) - (c : ℤ) := by
    dsimp [c]
    have hdiv := Nat.div_add_mod (i₀ - 1) m
    refine ⟨((i₀ - 1) / m : ℕ), ?_⟩
    omega
  let S : Finset ℕ := (Finset.Icc 1 k).filter (fun i => (m : ℤ) ∣ (i : ℤ) - (c : ℤ))
  let T : Finset ℕ := (Finset.Icc 1 k).filter (fun i => m ∣ σ i)
  -- `S ⊆ T` by weak consecutiveness from `i₀`
  have hST : S ⊆ T := by
    intro i hi
    simp only [S, T, Finset.mem_filter, Finset.mem_Icc] at hi ⊢
    refine ⟨hi.1, ?_⟩
    have hdiff : (m : ℤ) ∣ (i₀ : ℤ) - (i : ℤ) := by
      have : (i₀ : ℤ) - (i : ℤ) = ((i₀ : ℤ) - (c : ℤ)) - ((i : ℤ) - (c : ℤ)) := by ring
      rw [this]
      exact dvd_sub hi₀_cong hi.2
    have hdivZ : (m : ℤ) ∣ (σ i : ℤ) :=
      hσ.2 i₀ hi₀_mem i hi.1 (m : ℤ) (by rw [hσi₀]) hdiff
    exact Int.ofNat_dvd.mp hdivZ
  -- `|T| = k / m` because `σ` maps `T` bijectively onto `{m, 2m, ..., (k/m)*m}`
  have hTcard : T.card = k / m := by
    have hbij : T.card = ((Finset.Icc 1 (k / m)).image (fun t => t * m)).card := by
      refine Finset.card_bij (fun i _ => σ i) ?_ ?_ ?_
      · intro i hi
        simp only [T, Finset.mem_filter, Finset.mem_Icc] at hi
        rcases hi.2 with ⟨t, ht⟩
        have hσmem := hσ.1.mapsTo hi.1
        simp only [Set.mem_Icc] at hσmem
        have ht1 : 1 ≤ t := by nlinarith
        have htk : t ≤ k / m := (Nat.le_div_iff_mul_le (by omega)).mpr (by nlinarith)
        exact Finset.mem_image.mpr ⟨t, Finset.mem_Icc.mpr ⟨ht1, htk⟩, by linarith⟩
      · intro i₁ hi₁ i₂ hi₂ heq
        simp only [T, Finset.mem_filter, Finset.mem_Icc] at hi₁ hi₂
        exact hσ.1.injOn hi₁.1 hi₂.1 heq
      · intro y hy
        rcases Finset.mem_image.mp hy with ⟨t, ht, rfl⟩
        simp only [Finset.mem_Icc] at ht
        have htm_le : t * m ≤ k := (Nat.le_div_iff_mul_le (by omega)).mp ht.2
        have htm_ge : 1 ≤ t * m := by nlinarith
        rcases hσ.1.surjOn ⟨htm_ge, htm_le⟩ with ⟨i, hi, hσi⟩
        refine ⟨i, Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr hi, ?_⟩, hσi⟩
        rw [hσi]; exact ⟨t, by ring⟩
    have hinj : Set.InjOn (fun t => t * m) (Finset.Icc 1 (k / m)) := by
      intro a _ b _ h; exact Nat.eq_of_mul_eq_mul_right (by omega) h
    rw [hbij, Finset.card_image_of_injOn hinj, Nat.card_Icc, Nat.add_sub_cancel]
  -- Embed `{c + t * m | 0 ≤ t < k / m}` into `S`
  set q := k / m
  set r := k % m
  have hqr : q * m + r = k := by
    simpa [q, r, mul_comm] using Nat.div_add_mod k m
  have hbase_sub : (Finset.range q).image (fun t => c + t * m) ⊆ S := by
    intro x hx
    rcases Finset.mem_image.mp hx with ⟨t, ht, rfl⟩
    have htq : t < q := Finset.mem_range.mp ht
    have hle : c + t * m ≤ k := by nlinarith
    simp only [S, Finset.mem_filter, Finset.mem_Icc]
    refine ⟨⟨by omega, hle⟩, ⟨(t : ℤ), by push_cast; ring⟩⟩
  -- Deduce `r < c`
  have hrc : r < c := by
    by_contra hle
    have hcr : c ≤ r := by omega
    have hextra : c + q * m ∈ S := by
      simp only [S, Finset.mem_filter, Finset.mem_Icc]
      refine ⟨⟨by omega, by omega⟩, ⟨(q : ℤ), by push_cast; ring⟩⟩
    have hsub' : (Finset.range (q + 1)).image (fun t => c + t * m) ⊆ S := by
      intro x hx
      rcases Finset.mem_image.mp hx with ⟨t, ht, rfl⟩
      have htq : t ≤ q := Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)
      rcases eq_or_lt_of_le htq with rfl | hlt
      · exact hextra
      · exact hbase_sub (Finset.mem_image.mpr ⟨t, Finset.mem_range.mpr hlt, rfl⟩)
    have hcard_lo : q + 1 ≤ S.card := by
      have hc := Finset.card_le_card hsub'
      rw [Finset.card_image_of_injOn, Finset.card_range] at hc
      · exact hc
      · intro a _ b _ h; dsimp at h
        have : a * m = b * m := by omega
        exact Nat.eq_of_mul_eq_mul_right (by omega) this
    have hcard_hi : S.card ≤ T.card := Finset.card_le_card hST
    omega
  -- Now `|S| ≥ q = |T|` and `S ⊆ T`, so `S = T`!
  have hScard_ge : q ≤ S.card := by
    have hc := Finset.card_le_card hbase_sub
    rw [Finset.card_image_of_injOn, Finset.card_range] at hc
    · exact hc
    · intro a _ b _ h; dsimp at h
      have : a * m = b * m := by omega
      exact Nat.eq_of_mul_eq_mul_right (by omega) this
  have hS_eq_T : S = T := Finset.eq_of_subset_of_card_le hST (by omega)
  refine ⟨c, hc1, hcm, hrc, ?_, ?_⟩
  · intro i hi
    have hmem : i ∈ T ↔ i ∈ S := by rw [hS_eq_T]
    simp only [S, T, Finset.mem_filter, Finset.mem_Icc] at hmem
    have hi' : 1 ≤ i ∧ i ≤ k := hi
    tauto
  · intro j hj hσj
    have hj_eq : j = i₀ := hσ.1.injOn hj hi₀_mem (hσj.trans hσi₀.symm)
    rwa [hj_eq]

/-- Corollary of Lemma 2: `σ 1 ∣ k` and `σ k ∣ k`. -/
lemma wcs_first_dvd {k : ℕ} {σ : ℕ → ℕ} (hk : 1 ≤ k) (hσ : IsWeaklyConsecutive k σ) :
    σ 1 ∣ k := by
  have h1mem : 1 ∈ Set.Icc 1 k := ⟨le_rfl, hk⟩
  have hσ1 := hσ.1.mapsTo h1mem
  obtain ⟨c, hc1, hcm, hrc, hiff, _⟩ := wcs_residue_class hσ hσ1.1 hσ1.2
  have hdiv : (σ 1 : ℤ) ∣ (1 : ℤ) - (c : ℤ) := (hiff 1 h1mem).mp (dvd_refl _)
  have hc_eq : c = 1 := by
    rcases hdiv with ⟨t, ht⟩
    have h1 : (1 : ℤ) ≤ c := by exact_mod_cast hc1
    have h2 : (c : ℤ) ≤ σ 1 := by exact_mod_cast hcm
    have ht0 : t = 0 := by nlinarith
    rw [ht0, mul_zero] at ht
    omega
  rw [hc_eq] at hrc
  exact Nat.dvd_of_mod_eq_zero (by omega)

lemma wcs_last_dvd {k : ℕ} {σ : ℕ → ℕ} (hk : 1 ≤ k) (hσ : IsWeaklyConsecutive k σ) :
    σ k ∣ k := by
  have h := wcs_first_dvd hk (wcs_rev hσ)
  simpa [show k + 1 - 1 = k by omega] using h

/-- Corollary of Lemma 2 for `k / 2 < m ≤ k`: the unique `j` with `σ j = m` satisfies
`k - m + 1 ≤ j ≤ m`. -/
lemma wcs_mid_preimage_bounds {k m j : ℕ} {σ : ℕ → ℕ} (hσ : IsWeaklyConsecutive k σ)
    (hm_lo : k / 2 < m) (hm_hi : m ≤ k) (hj : j ∈ Set.Icc 1 k) (hσj : σ j = m) :
    k - m + 1 ≤ j ∧ j ≤ m := by
  have hm1 : 1 ≤ m := by omega
  obtain ⟨c, hc1, hcm, hrc, _, hcong⟩ := wcs_residue_class hσ hm1 hm_hi
  have hmod : k % m = k - m := by
    have hdiv : k / m = 1 := by
      apply Nat.div_eq_of_lt_le
      · omega
      · omega
    have h := Nat.div_add_mod k m
    rw [hdiv, mul_one] at h
    omega
  have hc_lo : k - m + 1 ≤ c := by omega
  have hdiv := hcong j hj hσj
  have hj_eq : j = c := by
    rcases hdiv with ⟨t, ht⟩
    have h1 : 1 ≤ j := hj.1
    have h2 : j ≤ k := hj.2
    have h2m : k < 2 * m := by omega
    zify [hm_hi] at h1 h2 hc1 hcm hc_lo h2m
    have ht0 : t = 0 := by nlinarith
    rw [ht0, mul_zero] at ht
    omega
  subst hj_eq
  exact ⟨hc_lo, hcm⟩

/-! ## Section 3: Lemma 3 (GCD Representation `σ(i) = gcd(a + i, L_k)`) -/

/-- `L_k = lcm(1, 2, ..., k)`. -/
def lcmIcc (k : ℕ) : ℕ :=
  (Finset.Icc 1 k).lcm id

lemma lcmIcc_pos {k : ℕ} (_hk : 1 ≤ k) : 0 < lcmIcc k := by
  apply Nat.pos_of_ne_zero
  unfold lcmIcc
  intro h0
  rw [Finset.lcm_eq_zero_iff] at h0
  rcases h0 with ⟨x, hx, hx0⟩
  simp only [Finset.mem_Icc, id_eq] at hx hx0
  omega

lemma dvd_lcmIcc {k m : ℕ} (hm1 : 1 ≤ m) (hmk : m ≤ k) : m ∣ lcmIcc k :=
  Finset.dvd_lcm (Finset.mem_Icc.mpr ⟨hm1, hmk⟩)

lemma prime_pow_dvd_lcmIcc_iff {k p e : ℕ} (hk : 1 ≤ k) (hp : p.Prime) (he : 1 ≤ e) :
    p ^ e ∣ lcmIcc k ↔ p ^ e ≤ k := by
  constructor
  · intro hdvd
    have hle : e ≤ (lcmIcc k).factorization p := by
      have h1 := Nat.factorization_le_iff_dvd (pow_ne_zero e hp.ne_zero) (ne_of_gt (lcmIcc_pos hk)) |>.mpr hdvd p
      rwa [Nat.Prime.factorization_pow hp, Finsupp.single_eq_same] at h1
    -- Since `lcmIcc k = (Finset.Icc 1 k).lcm id`, some `x ∈ [1, k]` achieves `e ≤ x.factorization p`
    have hex : ∃ x ∈ Finset.Icc 1 k, p ^ e ∣ x := by
      by_contra hnone
      push Not at hnone
      have hlt : ∀ x ∈ Finset.Icc 1 k, x.factorization p < e := by
        intro x hx
        by_contra hge
        have hpe : p ^ e ∣ x := by
          have hx0 : x ≠ 0 := by have := (Finset.mem_Icc.mp hx).1; omega
          exact (hp.pow_dvd_iff_le_factorization hx0).mpr (by omega)
        exact hnone x hx hpe
      -- Wait: `lcmIcc k` divides `∏`? Even simpler: show `lcmIcc k ∣ (lcmIcc k) / p`? No:
      -- Prove directly by induction on any `Finset ℕ` `S`: if `∀ x ∈ S, ¬ p^e ∣ x`, then `¬ p^e ∣ S.lcm id`!
      have hnot : ∀ S : Finset ℕ, (∀ x ∈ S, x ≠ 0 ∧ ¬ p ^ e ∣ x) → ¬ p ^ e ∣ S.lcm id := by
        intro S
        induction S using Finset.induction with
        | empty =>
          intro _ hd
          simp only [Finset.lcm_empty] at hd
          have := Nat.le_of_dvd one_pos hd
          have hp2 : 2 ≤ p := hp.two_le
          have : 2 ≤ p ^ e := le_trans hp2 (Nat.le_self_pow (by omega) p)
          omega
        | @insert a s has ih =>
          intro hS hd
          rw [Finset.lcm_insert] at hd
          have ha := hS a (Finset.mem_insert_self a s)
          have hs := ih (fun x hx => hS x (Finset.mem_insert_of_mem hx))
          have hs0 : s.lcm id ≠ 0 := by
            intro h0
            rw [Finset.lcm_eq_zero_iff] at h0
            rcases h0 with ⟨x, hx, hx0⟩
            exact (hS x (Finset.mem_insert_of_mem hx)).1 hx0
          have hfac := Nat.factorization_lcm ha.1 hs0
          have hle_lcm : e ≤ (Nat.lcm a (s.lcm id)).factorization p :=
            (hp.pow_dvd_iff_le_factorization (Nat.lcm_ne_zero ha.1 hs0)).mp hd
          rw [hfac, Finsupp.sup_apply] at hle_lcm
          rcases le_sup_iff.mp hle_lcm with h1 | h2
          · exact ha.2 ((hp.pow_dvd_iff_le_factorization ha.1).mpr h1)
          · exact hs ((hp.pow_dvd_iff_le_factorization hs0).mpr h2)
      exact hnot (Finset.Icc 1 k) (fun x hx => ⟨by have := (Finset.mem_Icc.mp hx).1; omega, hnone x hx⟩) hdvd
    rcases hex with ⟨x, hx, hpe⟩
    have hx1 : 1 ≤ x := (Finset.mem_Icc.mp hx).1
    have hxk : x ≤ k := (Finset.mem_Icc.mp hx).2
    exact le_trans (Nat.le_of_dvd (by omega) hpe) hxk
  · intro hle
    exact dvd_lcmIcc (by have := hp.one_lt; exact Nat.one_le_pow e p (by omega)) hle

/-- Helper CRT over a finite set of pairwise coprime moduli. -/
private lemma exists_crt_finset (S : Finset ℕ) (m : ℕ → ℕ) (r : ℕ → ℕ)
    (hcop : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → Nat.Coprime (m x) (m y)) :
    ∃ a : ℕ, ∀ x ∈ S, a ≡ r x [MOD m x] := by
  classical
  induction S using Finset.induction with
  | empty => exact ⟨0, by simp⟩
  | @insert x s hxs ih =>
    obtain ⟨a₀, ha₀⟩ := ih (fun u hu v hv => hcop u (Finset.mem_insert_of_mem hu) v (Finset.mem_insert_of_mem hv))
    have hcop_prod : Nat.Coprime (m x) (∏ y ∈ s, m y) := by
      refine Nat.Coprime.prod_right fun y hy => ?_
      exact hcop x (Finset.mem_insert_self x s) y (Finset.mem_insert_of_mem hy) (fun h => hxs (h ▸ hy))
    let sol := Nat.chineseRemainder hcop_prod (r x) a₀
    refine ⟨sol.val, ?_⟩
    intro y hy
    rcases Finset.mem_insert.mp hy with rfl | hys
    · exact sol.property.1
    · have hmod_prod : sol.val ≡ a₀ [MOD ∏ z ∈ s, m z] := sol.property.2
      have hdvd : m y ∣ ∏ z ∈ s, m z := Finset.dvd_prod_of_mem m hys
      exact (hmod_prod.of_dvd hdvd).trans (ha₀ y hys)

/-- Lemma 3 (GCD representation): for any WCS `σ` on `[k]`, there exists `a : ℕ` such that
`σ i = Nat.gcd (a + i) (lcmIcc k)` for all `i ∈ [1, k]`, and for all `m ∈ [1, k]`,
`m ∣ σ i ↔ m ∣ a + i`. -/
lemma wcs_gcd_repr {k : ℕ} {σ : ℕ → ℕ} (hk : 1 ≤ k) (hσ : IsWeaklyConsecutive k σ) :
    ∃ a : ℕ, (∀ i ∈ Set.Icc 1 k, σ i = Nat.gcd (a + i) (lcmIcc k)) ∧
      (∀ i ∈ Set.Icc 1 k, ∀ m ∈ Set.Icc 1 k, m ∣ σ i ↔ m ∣ a + i) := by
  classical
  let P : Finset ℕ := (Finset.Icc 1 k).filter Nat.Prime
  let ep : ℕ → ℕ := fun p => (lcmIcc k).factorization p
  let modP : ℕ → ℕ := fun p => p ^ ep p
  -- For each prime `p ∈ P`, `1 ≤ ep p` and `p ^ ep p ≤ k`, so Lemma 2 gives `c_{p^{ep p}}`
  have hep_pos : ∀ p ∈ P, 1 ≤ ep p := by
    intro p hp
    simp only [P, Finset.mem_filter, Finset.mem_Icc] at hp
    have hdvd : p ^ 1 ∣ lcmIcc k := by rw [pow_one]; exact dvd_lcmIcc hp.1.1 hp.1.2
    exact (hp.2.pow_dvd_iff_le_factorization (ne_of_gt (lcmIcc_pos hk))).mp hdvd
  have hmod_le : ∀ p ∈ P, modP p ≤ k := by
    intro p hp
    have hp' := (Finset.mem_filter.mp hp).2
    have he1 := hep_pos p hp
    have hdvd : p ^ ep p ∣ lcmIcc k := Nat.ordProj_dvd (lcmIcc k) p
    exact (prime_pow_dvd_lcmIcc_iff hk hp' he1).mp hdvd
  have hmod_pos : ∀ p ∈ P, 1 ≤ modP p := by
    intro p hp
    have hp' := (Finset.mem_filter.mp hp).2
    exact Nat.one_le_pow _ _ hp'.pos
  -- Choose residue `c_p` for each `p ∈ P` via Lemma 2 at `m = modP p`
  have hex_c : ∀ p ∈ P, ∃ c : ℕ, 1 ≤ c ∧ c ≤ modP p ∧
      (∀ i ∈ Set.Icc 1 k, modP p ∣ σ i ↔ (modP p : ℤ) ∣ (i : ℤ) - (c : ℤ)) ∧
      (∀ i₀ ∈ Set.Icc 1 k, σ i₀ = modP p → (modP p : ℤ) ∣ (i₀ : ℤ) - (c : ℤ)) := by
    intro p hp
    obtain ⟨c, hc1, hcm, _, hiff, hcong⟩ := wcs_residue_class hσ (hmod_pos p hp) (hmod_le p hp)
    exact ⟨c, hc1, hcm, hiff, hcong⟩
  let remP : ℕ → ℕ := fun p =>
    if hp : p ∈ P then modP p - (Classical.choose (hex_c p hp)) % modP p else 0
  have hcop : ∀ p ∈ P, ∀ q ∈ P, p ≠ q → Nat.Coprime (modP p) (modP q) := by
    intro p hp q hq hpq
    have hp' := (Finset.mem_filter.mp hp).2
    have hq' := (Finset.mem_filter.mp hq).2
    exact (hp'.coprime_iff_not_dvd.mpr fun h => hpq ((Nat.prime_dvd_prime_iff_eq hp' hq').mp h)).pow _ _
  obtain ⟨a, ha⟩ := exists_crt_finset P modP remP hcop
  -- Show: for every prime `p` and `e ≥ 1` with `p^e ≤ k`, `p^e ∣ σ i ↔ p^e ∣ a + i`
  have hpp : ∀ p e : ℕ, p.Prime → 1 ≤ e → p ^ e ≤ k →
      ∀ i ∈ Set.Icc 1 k, p ^ e ∣ σ i ↔ p ^ e ∣ a + i := by
    intro p e hp he hpek i hi
    have hpP : p ∈ P := Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨hp.one_lt.le,
      le_trans (Nat.le_self_pow (by omega) p) hpek⟩, hp⟩
    have he_le : e ≤ ep p := by
      have hdvd : p ^ e ∣ lcmIcc k := (prime_pow_dvd_lcmIcc_iff hk hp he).mpr hpek
      exact (hp.pow_dvd_iff_le_factorization (ne_of_gt (lcmIcc_pos hk))).mp hdvd
    have hpe_dvd_mod : p ^ e ∣ modP p := pow_dvd_pow p he_le
    -- Pick `i₀ ∈ [1, k]` with `σ i₀ = modP p`
    rcases hσ.1.surjOn ⟨hmod_pos p hpP, hmod_le p hpP⟩ with ⟨i₀, hi₀_mem, hσi₀⟩
    have hspec := Classical.choose_spec (hex_c p hpP)
    set cP := Classical.choose (hex_c p hpP)
    have ha_mod : a ≡ modP p - cP % modP p [MOD modP p] := by
      have h := ha p hpP
      simp only [remP, dite_eq_left hpP] at h
      exact h
    have hmod_dvd_ac : modP p ∣ a + cP := by
      have h1 : (a + cP) % modP p = ((a % modP p) + (cP % modP p)) % modP p := Nat.add_mod _ _ _
      have hlt : cP % modP p < modP p := Nat.mod_lt cP (hmod_pos p hpP)
      have h2 : a % modP p = (modP p - cP % modP p) % modP p := ha_mod
      rw [Nat.dvd_iff_mod_eq_zero, h1, h2]
      by_cases h0 : cP % modP p = 0
      · rw [h0, Nat.sub_zero, Nat.mod_self, add_zero, Nat.zero_mod]
      · have hsub_lt : modP p - cP % modP p < modP p := by omega
        rw [Nat.mod_eq_of_lt hsub_lt, Nat.sub_add_cancel (le_of_lt hlt), Nat.mod_self]
    have hpe_dvd_ai₀ : p ^ e ∣ a + i₀ := by
      have hZ1 : (modP p : ℤ) ∣ (a : ℤ) + (cP : ℤ) := by exact_mod_cast hmod_dvd_ac
      have hZ2 : (modP p : ℤ) ∣ (i₀ : ℤ) - (cP : ℤ) := hspec.2.2.2 i₀ hi₀_mem hσi₀
      have hZ3 : (modP p : ℤ) ∣ (a : ℤ) + (i₀ : ℤ) := by
        have : (a : ℤ) + (i₀ : ℤ) = ((a : ℤ) + (cP : ℤ)) + ((i₀ : ℤ) - (cP : ℤ)) := by ring
        rw [this]; exact dvd_add hZ1 hZ2
      exact hpe_dvd_mod.trans (Int.ofNat_dvd.mp hZ3)
    -- Apply Lemma 2 at `m = p ^ e`
    obtain ⟨c, _, _, _, hiff_pe, _⟩ := wcs_residue_class hσ (Nat.one_le_pow e p hp.pos) hpek
    have hi₀_div : p ^ e ∣ σ i₀ := by rw [hσi₀]; exact hpe_dvd_mod
    have hi₀_c : (p ^ e : ℤ) ∣ (i₀ : ℤ) - (c : ℤ) := (hiff_pe i₀ hi₀_mem).mp hi₀_div
    rw [hiff_pe i hi]
    constructor
    · intro hic
      have hZ : (p ^ e : ℤ) ∣ (a : ℤ) + (i : ℤ) := by
        have h1 : (p ^ e : ℤ) ∣ (a : ℤ) + (i₀ : ℤ) := by exact_mod_cast hpe_dvd_ai₀
        have : (a : ℤ) + (i : ℤ) = ((a : ℤ) + (i₀ : ℤ)) - ((i₀ : ℤ) - (c : ℤ)) + ((i : ℤ) - (c : ℤ)) := by
          ring
        rw [this]; exact dvd_add (dvd_sub h1 hi₀_c) hic
      exact Int.ofNat_dvd.mp hZ
    · intro hai
      have h1 : (p ^ e : ℤ) ∣ (a : ℤ) + (i : ℤ) := by exact_mod_cast hai
      have h2 : (p ^ e : ℤ) ∣ (a : ℤ) + (i₀ : ℤ) := by exact_mod_cast hpe_dvd_ai₀
      have : (i : ℤ) - (c : ℤ) = ((a : ℤ) + (i : ℤ)) - ((a : ℤ) + (i₀ : ℤ)) + ((i₀ : ℤ) - (c : ℤ)) := by
        ring
      rw [this]; exact dvd_add (dvd_sub h1 h2) hi₀_c
  -- Conclude `σ i = Nat.gcd (a + i) (lcmIcc k)` by comparing prime-power factorizations
  have hgcd : ∀ i ∈ Set.Icc 1 k, σ i = Nat.gcd (a + i) (lcmIcc k) := by
    intro i hi
    have hσi_mem := hσ.1.mapsTo hi
    have hσi_ne : σ i ≠ 0 := by have := hσi_mem.1; omega
    have hg_ne : Nat.gcd (a + i) (lcmIcc k) ≠ 0 :=
      Nat.ne_of_gt (Nat.gcd_pos_of_pos_right (a + i) (lcmIcc_pos hk))
    refine Nat.eq_of_factorization_eq hσi_ne hg_ne fun p => ?_
    by_cases hp : p.Prime
    · apply le_antisymm
      · set e := (σ i).factorization p
        by_cases he0 : e = 0
        · rw [he0]; exact Nat.zero_le _
        · have he1 : 1 ≤ e := by omega
          have hpe_σ : p ^ e ∣ σ i := Nat.ordProj_dvd (σ i) p
          have hpe_k : p ^ e ≤ k := le_trans (Nat.le_of_dvd (by omega) hpe_σ) hσi_mem.2
          have hpe_ai : p ^ e ∣ a + i := (hpp p e hp he1 hpe_k i hi).mp hpe_σ
          have hpe_L : p ^ e ∣ lcmIcc k := (prime_pow_dvd_lcmIcc_iff hk hp he1).mpr hpe_k
          exact (hp.pow_dvd_iff_le_factorization hg_ne).mp (Nat.dvd_gcd hpe_ai hpe_L)
      · set e := (Nat.gcd (a + i) (lcmIcc k)).factorization p
        by_cases he0 : e = 0
        · rw [he0]; exact Nat.zero_le _
        · have he1 : 1 ≤ e := by omega
          have hpe_g : p ^ e ∣ Nat.gcd (a + i) (lcmIcc k) := Nat.ordProj_dvd _ p
          have hpe_ai : p ^ e ∣ a + i := hpe_g.trans (Nat.gcd_dvd_left _ _)
          have hpe_L : p ^ e ∣ lcmIcc k := hpe_g.trans (Nat.gcd_dvd_right _ _)
          have hpe_k : p ^ e ≤ k := (prime_pow_dvd_lcmIcc_iff hk hp he1).mp hpe_L
          have hpe_σ : p ^ e ∣ σ i := (hpp p e hp he1 hpe_k i hi).mpr hpe_ai
          exact (hp.pow_dvd_iff_le_factorization hσi_ne).mp hpe_σ
    · rw [Nat.factorization_eq_zero_of_not_prime _ hp, Nat.factorization_eq_zero_of_not_prime _ hp]
  refine ⟨a, hgcd, ?_⟩
  intro i hi m hm
  rw [hgcd i hi, Nat.dvd_gcd_iff]
  have hmL : m ∣ lcmIcc k := dvd_lcmIcc hm.1 hm.2
  tauto

/-! ## Section 4: Case 1 (`k ≥ 4` even) and Case 2 (`k ≥ 3` odd) -/

/-- Case 1: Conjecture 5.2 for all even `k ≥ 4`. -/
lemma wcs_even {k : ℕ} {σ : ℕ → ℕ} (hk4 : 4 ≤ k) (heven : Even k)
    (hσ : IsWeaklyConsecutive k σ) : σ 1 = 1 ∨ σ k = 1 := by
  -- Helper assuming `2 ∣ σ i ↔ 2 ∣ i` on `[1, k]`, proving `σ 1 = 1`
  have hnorm : ∀ τ : ℕ → ℕ, IsWeaklyConsecutive k τ →
      (∀ i ∈ Set.Icc 1 k, 2 ∣ τ i ↔ 2 ∣ i) → τ 1 = 1 := by
    intro τ hτ hpar
    rcases heven with ⟨h, hk_eq⟩
    have hh2 : 2 ≤ h := by omega
    set m := h + 1
    have hm_lo : k / 2 < m := by omega
    have hm_hi : m ≤ k := by omega
    rcases hτ.1.surjOn ⟨by omega, hm_hi⟩ with ⟨j, hj_mem, hτj⟩
    have hj_b := wcs_mid_preimage_bounds hτ hm_lo hm_hi hj_mem hτj
    have hj_cases : j = h ∨ j = h + 1 := by omega
    have hj_eq : j = h + 1 := by
      rcases hj_cases with hjh | hjh1
      · exfalso
        have hp := hpar j hj_mem
        rw [hτj, hjh] at hp
        omega
      · exact hjh1
    have hτm : τ (h + 1) = h + 1 := by rw [← hj_eq, hτj]; exact hj_eq.symm
    set A := τ 1
    have hA_mem := hτ.1.mapsTo (show 1 ∈ Set.Icc 1 k from ⟨le_rfl, by omega⟩)
    by_contra hAne1
    have hA_gt : 1 < A := by have := hA_mem.1; omega
    have hA_dvd_k : A ∣ k := wcs_first_dvd (by omega) hτ
    have hA_odd : ¬ (2 ∣ A) := by
      intro h2A
      have := (hpar 1 ⟨le_rfl, by omega⟩).mp h2A
      omega
    have hA_cop2 : Nat.Coprime A 2 :=
      (Nat.coprime_comm.mp (Nat.prime_two.coprime_iff_not_dvd.mpr hA_odd))
    have hA_dvd_h : A ∣ h := hA_cop2.dvd_of_dvd_mul_left (by rw [two_mul, ← hk_eq]; exact hA_dvd_k)
    have hA_dvd_diff : (A : ℤ) ∣ (1 : ℤ) - ((h + 1 : ℕ) : ℤ) := by
      rcases hA_dvd_h with ⟨t, ht⟩
      refine ⟨-(t : ℤ), ?_⟩
      push_cast [ht]
      ring
    have hA_dvd_τm : (A : ℤ) ∣ (τ (h + 1) : ℤ) :=
      hτ.2 1 ⟨le_rfl, by omega⟩ (h + 1) ⟨by omega, by omega⟩ (A : ℤ) (dvd_refl _) hA_dvd_diff
    rw [hτm] at hA_dvd_τm
    have hA_dvd_h1 : A ∣ h + 1 := Int.ofNat_dvd.mp hA_dvd_τm
    have hA_dvd_1 : A ∣ 1 := by
      have := (Nat.dvd_add_right hA_dvd_h).mp hA_dvd_h1
      exact this
    have := Nat.le_of_dvd one_pos hA_dvd_1
    omega
  obtain ⟨c, hc1, hc2, _, hiff2, _⟩ := wcs_residue_class hσ (by omega : 1 ≤ 2) (by omega : 2 ≤ k)
  have hc_cases : c = 1 ∨ c = 2 := by omega
  rcases hc_cases with rfl | rfl
  · -- `c = 1`: reverse `σ` so that `c_2` flips to `2`
    right
    have hrev := wcs_rev hσ
    have hpar : ∀ i ∈ Set.Icc 1 k, 2 ∣ σ (k + 1 - i) ↔ 2 ∣ i := by
      intro i hi
      have hflip : k + 1 - i ∈ Set.Icc 1 k := ⟨by have := hi.2; omega, by have := hi.1; omega⟩
      rw [hiff2 (k + 1 - i) hflip]
      rcases heven with ⟨h, rfl⟩
      have hi1 := hi.1
      have hi2 := hi.2
      rw [← Int.ofNat_dvd, Nat.cast_ofNat, Nat.cast_one,
        show (((h + h + 1 - i : ℕ) : ℤ) - 1) = 2 * (h : ℤ) - (i : ℤ) by omega]
      constructor
      · rintro ⟨t, ht⟩; exact ⟨(h : ℤ) - t, by linarith⟩
      · rintro ⟨t, ht⟩; exact ⟨(h : ℤ) - t, by linarith⟩
    have h1 := hnorm (fun i => σ (k + 1 - i)) hrev hpar
    simpa [show k + 1 - 1 = k by omega] using h1
  · -- `c = 2`: already normalized
    left
    have hpar : ∀ i ∈ Set.Icc 1 k, 2 ∣ σ i ↔ 2 ∣ i := by
      intro i hi
      rw [hiff2 i hi, ← Int.ofNat_dvd]
      constructor
      · rintro ⟨t, ht⟩; exact ⟨t + 1, by linarith⟩
      · rintro ⟨t, ht⟩; exact ⟨t - 1, by linarith⟩
    exact hnorm σ hσ hpar

/-- Case 2: Conjecture 5.2 for all odd `k ≥ 3`. -/
lemma wcs_odd {k : ℕ} {σ : ℕ → ℕ} (hk3 : 3 ≤ k) (hodd : Odd k)
    (hσ : IsWeaklyConsecutive k σ) : σ 1 = 1 ∨ σ k = 1 := by
  by_contra hneither
  push Not at hneither
  -- Core contradiction assuming `3 ≤ σ 1 < σ k`
  have hcontra : ∀ τ : ℕ → ℕ, IsWeaklyConsecutive k τ → 1 < τ 1 → τ 1 < τ k → False := by
    intro τ hτ hA1 hAB
    obtain ⟨a, hgcd, hdiv_iff⟩ := wcs_gcd_repr (by omega : 1 ≤ k) hτ
    -- Step 1: Parity (`2 ∣ a`), `A ∣ k`, `B ∣ k`, `A ∣ a + 1`, `B ∣ a`, `Coprime A B`
    set A := τ 1
    set B := τ k
    have h1mem : 1 ∈ Set.Icc 1 k := ⟨le_rfl, by omega⟩
    have hkmem : k ∈ Set.Icc 1 k := ⟨by omega, le_rfl⟩
    have hAmem := hτ.1.mapsTo h1mem
    have hBmem := hτ.1.mapsTo hkmem
    have hA_dvd_k : A ∣ k := wcs_first_dvd (by omega) hτ
    have hB_dvd_k : B ∣ k := wcs_last_dvd (by omega) hτ
    have hA_odd : Odd A := hodd.of_dvd_nat hA_dvd_k
    have hB_odd : Odd B := hodd.of_dvd_nat hB_dvd_k
    have hA3 : 3 ≤ A := by rcases hA_odd with ⟨r, hr⟩; omega
    have hB5 : 5 ≤ B := by rcases hB_odd with ⟨r, hr⟩; omega
    have hA_dvd_a1 : A ∣ a + 1 := (hdiv_iff 1 h1mem A hAmem).mp (dvd_refl A)
    have hB_dvd_ak : B ∣ a + k := (hdiv_iff k hkmem B hBmem).mp (dvd_refl B)
    have hB_dvd_a : B ∣ a := (Nat.dvd_add_left hB_dvd_k).mp hB_dvd_ak
    have hcopAB : Nat.Coprime A B := by
      rw [Nat.coprime_iff_gcd_eq_one]
      have hd1 : Nat.gcd A B ∣ a + 1 := (Nat.gcd_dvd_left A B).trans hA_dvd_a1
      have hd2 : Nat.gcd A B ∣ a := (Nat.gcd_dvd_right A B).trans hB_dvd_a
      have hd : Nat.gcd A B ∣ 1 := (Nat.dvd_add_right hd2).mp hd1
      exact Nat.eq_one_of_dvd_one hd
    have hAB_dvd_k : A * B ∣ k := hcopAB.mul_dvd_of_dvd_of_dvd hA_dvd_k hB_dvd_k
    rcases hAB_dvd_k with ⟨R, hR⟩
    have hR_pos : 1 ≤ R := by
      by_contra h0
      have hR0 : R = 0 := by omega
      rw [hR0, mul_zero] at hR
      omega
    have hR_odd : Odd R := hodd.of_dvd_nat ⟨A * B, by linarith⟩
    have hBR_odd : Odd (B * R) := hB_odd.mul hR_odd
    have hBR5 : 5 ≤ B * R := by nlinarith
    have h2a : 2 ∣ a := by
      obtain ⟨c, hc1, hc2, hrc, hiff2, _⟩ := wcs_residue_class hτ (by omega : 1 ≤ 2) (by omega : 2 ≤ k)
      have hkmod2 : k % 2 = 1 := by rcases hodd with ⟨r, rfl⟩; omega
      have hc_eq : c = 2 := by omega
      have h2_div : 2 ∣ τ 2 := (hiff2 2 ⟨by omega, by omega⟩).mpr (by rw [hc_eq]; simp)
      have h2_a2 : 2 ∣ a + 2 := (hdiv_iff 2 ⟨by omega, by omega⟩ 2 ⟨by omega, by omega⟩).mp h2_div
      exact (Nat.dvd_add_left (dvd_refl 2)).mp h2_a2
    -- Step 2: Mid-range fixed congruence for `m = (k + A) / 2`
    set Q := (B * R + 1) / 2
    have h2Q : 2 * Q = B * R + 1 := by rcases hBR_odd with ⟨r, hr⟩; omega
    set m := A * Q
    have h2m : 2 * m = k + A := by
      dsimp [m]
      calc 2 * (A * Q) = A * (2 * Q) := by ring
        _ = A * (B * R + 1) := by rw [h2Q]
        _ = A * B * R + A := by ring
        _ = k + A := by rw [← hR]
    have hm_lo : k / 2 < m := by omega
    have hm_hi : m ≤ k := by nlinarith
    rcases hτ.1.surjOn ⟨by omega, hm_hi⟩ with ⟨j, hj_mem, hτj⟩
    have hj_b := wcs_mid_preimage_bounds hτ hm_lo hm_hi hj_mem hτj
    have hA_dvd_j1 : (A : ℤ) ∣ (j : ℤ) - 1 := by
      have hAj : A ∣ a + j := (hdiv_iff j hj_mem A hAmem).mp (by rw [hτj]; exact dvd_mul_right A Q)
      have h1 : (A : ℤ) ∣ (a : ℤ) + (j : ℤ) := by exact_mod_cast hAj
      have h2 : (A : ℤ) ∣ (a : ℤ) + 1 := by exact_mod_cast hA_dvd_a1
      have : (j : ℤ) - 1 = ((a : ℤ) + (j : ℤ)) - ((a : ℤ) + 1) := by ring
      rw [this]; exact dvd_sub h1 h2
    have hj_eq : j = k - m + 1 := by
      have hleft : k - m + 1 = A * (Q - 1) + 1 := by
        have hQ1 : 1 ≤ Q := by omega
        have hkm : k - m = A * (Q - 1) := by
          zify [hm_hi, hQ1]
          have hmZ : (m : ℤ) = (A : ℤ) * (Q : ℤ) := by exact_mod_cast rfl
          have h2mZ : 2 * (m : ℤ) = (k : ℤ) + (A : ℤ) := by exact_mod_cast h2m
          linarith
        omega
      have hdiff : (A : ℤ) ∣ (j : ℤ) - ((k - m + 1 : ℕ) : ℤ) := by
        have : (j : ℤ) - ((k - m + 1 : ℕ) : ℤ) = ((j : ℤ) - 1) - (A : ℤ) * ((Q - 1 : ℕ) : ℤ) := by
          rw [hleft]; push_cast; ring
        rw [this]
        exact dvd_sub hA_dvd_j1 (dvd_mul_right _ _)
      rcases hdiff with ⟨t, ht⟩
      have hgap : m - (k - m + 1) = A - 1 := by omega
      have hj1Z : ((k - m + 1 : ℕ) : ℤ) ≤ (j : ℤ) := by exact_mod_cast hj_b.1
      have hj2Z : (j : ℤ) ≤ (m : ℤ) := by exact_mod_cast hj_b.2
      have hgapZ : (m : ℤ) - ((k - m + 1 : ℕ) : ℤ) = (A : ℤ) - 1 := by omega
      have hAZ : (3 : ℤ) ≤ (A : ℤ) := by exact_mod_cast hA3
      have ht0 : t = 0 := by nlinarith
      rw [ht0, mul_zero] at ht
      omega
    have hm_dvd_aj : m ∣ a + j := (hdiv_iff j hj_mem m ⟨by omega, hm_hi⟩).mp (by rw [hτj])
    -- Equation (1): `Q ∣ (a + 1 - A)` in `ℤ`
    have hQ_dvd : (Q : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ) := by
      have hm_sub : (m : ℤ) ∣ (a : ℤ) + (j : ℤ) - (m : ℤ) :=
        dvd_sub (by exact_mod_cast hm_dvd_aj) (dvd_refl _)
      have heq_sub : (a : ℤ) + (j : ℤ) - (m : ℤ) = (a : ℤ) + 1 - (A : ℤ) := by omega
      rw [heq_sub] at hm_sub
      exact (dvd_mul_left (Q : ℤ) (A : ℤ)).trans (by simpa [m] using hm_sub)
    -- Step 3: Write `B * R + 1 = 2^s * u` with `u` odd, `s ≥ 1`, and pin `a` mod `2^s`
    set s := (B * R + 1).factorization 2
    set u := (B * R + 1) / 2 ^ s
    have h2s_dvd : 2 ^ s ∣ B * R + 1 := Nat.ordProj_dvd (B * R + 1) 2
    have hBR1_eq : 2 ^ s * u = B * R + 1 := Nat.mul_div_cancel' h2s_dvd
    have hs1 : 1 ≤ s := by
      have h2_dvd : 2 ^ 1 ∣ B * R + 1 := by rw [pow_one]; rcases hBR_odd with ⟨r, hr⟩; exact ⟨r + 1, by omega⟩
      exact (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp h2_dvd
    have hu_odd : Odd u := by
      by_contra hnot
      rcases Nat.even_or_odd u with heven_u | hodd_u
      · rcases heven_u.two_dvd with ⟨v, hv⟩
        have hpow : 2 ^ (s + 1) ∣ B * R + 1 := ⟨v, by
          calc B * R + 1 = 2 ^ s * u := hBR1_eq.symm
            _ = 2 ^ s * (2 * v) := by rw [hv]
            _ = 2 ^ (s + 1) * v := by rw [pow_succ]; ring⟩
        have hle : s + 1 ≤ s := (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp hpow
        omega
      · exact hnot hodd_u
    have hu1 : 1 ≤ u := by rcases hu_odd with ⟨r, hr⟩; omega
    have hQ_eq : Q = 2 ^ (s - 1) * u := by
      have h2s : 2 ^ s = 2 * 2 ^ (s - 1) := by
        rw [← pow_succ', Nat.sub_add_cancel hs1]
      have h2Q' : 2 * Q = 2 * (2 ^ (s - 1) * u) := by
        rw [h2Q, ← hBR1_eq, h2s]; ring
      omega
    -- Index `i₁ = (A - 1) * B * R`
    set i₁ := (A - 1) * (B * R)
    have hi₁_mem : i₁ ∈ Set.Icc 1 k := by
      refine ⟨Nat.mul_pos (by omega) (by omega), ?_⟩
      calc (A - 1) * (B * R) ≤ A * (B * R) := Nat.mul_le_mul_right _ (Nat.sub_le A 1)
        _ = A * B * R := by ring
        _ = k := hR.symm
    -- Equation (2) in `ℤ`: `a + i₁ = (a + 1 - A) + (A - 1) * (B * R + 1)`
    have hi₁_id : (a : ℤ) + (i₁ : ℤ) = ((a : ℤ) + 1 - (A : ℤ)) + ((A - 1 : ℕ) : ℤ) * ((B * R + 1 : ℕ) : ℤ) := by
      dsimp [i₁]
      have hA1' : 1 ≤ A := by omega
      zify [hA1']
      ring
    have hu_dvd_ai₁ : u ∣ a + i₁ := by
      have h1 : (u : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ) :=
        (by rw [hQ_eq]; exact_mod_cast dvd_mul_left u (2 ^ (s - 1)) : (u : ℤ) ∣ (Q : ℤ)).trans hQ_dvd
      have h2 : (u : ℤ) ∣ ((A - 1 : ℕ) : ℤ) * ((B * R + 1 : ℕ) : ℤ) := by
        have : (u : ℤ) ∣ ((B * R + 1 : ℕ) : ℤ) := by rw [← hBR1_eq]; exact_mod_cast dvd_mul_left u (2 ^ s)
        exact dvd_mul_of_dvd_right this _
      exact Int.ofNat_dvd.mp (by rw [Nat.cast_add, hi₁_id]; exact dvd_add h1 h2)
    have hB_dvd_ai₁ : B ∣ a + i₁ :=
      dvd_add hB_dvd_a ⟨(A - 1) * R, by dsimp [i₁]; ring⟩
    -- Prove `¬ (2 ^ s ∣ a + i₁)`
    have h2s_not_dvd : ¬ (2 ^ s ∣ a + i₁) := by
      intro h2s_ai₁
      have hcop_2u : Nat.Coprime (2 ^ s) u :=
        (Nat.prime_two.coprime_iff_not_dvd.mpr
          (fun h => by rcases hu_odd with ⟨r, hr⟩; rcases h with ⟨t, ht⟩; omega)).pow_left s
      have hBR1_dvd_ai₁ : B * R + 1 ∣ a + i₁ := by
        rw [← hBR1_eq]
        exact hcop_2u.mul_dvd_of_dvd_of_dvd h2s_ai₁ hu_dvd_ai₁
      have hcop_B : Nat.Coprime B (B * R + 1) := by
        rw [Nat.coprime_iff_gcd_eq_one]
        have hd1 : Nat.gcd B (B * R + 1) ∣ B * R := (Nat.gcd_dvd_left _ _).trans (dvd_mul_right B R)
        have hd2 : Nat.gcd B (B * R + 1) ∣ B * R + 1 := Nat.gcd_dvd_right _ _
        exact Nat.eq_one_of_dvd_one ((Nat.dvd_add_right hd1).mp hd2)
      have hprod_ai₁ : B * (B * R + 1) ∣ a + i₁ :=
        hcop_B.mul_dvd_of_dvd_of_dvd hB_dvd_ai₁ hBR1_dvd_ai₁
      have hBR1_le_k : B * R + 1 ≤ k := by
        have h3 : 3 * (B * R) ≤ k := by rw [hR, mul_assoc]; exact Nat.mul_le_mul_right _ hA3
        omega
      have hprod_L : B * (B * R + 1) ∣ lcmIcc k :=
        hcop_B.mul_dvd_of_dvd_of_dvd (dvd_lcmIcc (by omega) hBmem.2) (dvd_lcmIcc (by omega) hBR1_le_k)
      have hprod_σ : B * (B * R + 1) ∣ τ i₁ := by
        rw [hgcd i₁ hi₁_mem]; exact Nat.dvd_gcd hprod_ai₁ hprod_L
      have hτi₁_mem := hτ.1.mapsTo hi₁_mem
      have hle_k : B * (B * R + 1) ≤ k :=
        le_trans (Nat.le_of_dvd (by have := hτi₁_mem.1; omega) hprod_σ) hτi₁_mem.2
      have hgt : k < B * (B * R + 1) := by
        calc k = A * (B * R) := by rw [hR]; ring
          _ < B * (B * R) := Nat.mul_lt_mul_of_pos_right hAB (by omega)
          _ < B * (B * R + 1) := Nat.mul_lt_mul_of_pos_left (by omega) (by omega)
      omega
    -- Deduce `s ≥ 2` and Equation (3): `(2^s : ℤ) ∣ (a + 1 - A) - 2^(s - 1)`
    have hs2 : 2 ≤ s := by
      by_contra hs1'
      have hs_eq : s = 1 := by omega
      have h2_a1A : (2 : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ) := by
        rcases h2a with ⟨c, hc⟩
        rcases hA_odd with ⟨r, hr⟩
        refine ⟨(c : ℤ) - (r : ℤ), ?_⟩
        omega
      have h2_prod : (2 : ℤ) ∣ ((A - 1 : ℕ) : ℤ) * ((B * R + 1 : ℕ) : ℤ) := by
        have : (2 : ℤ) ∣ ((B * R + 1 : ℕ) : ℤ) := by
          rw [← hBR1_eq, hs_eq, pow_one]; exact_mod_cast dvd_mul_right 2 u
        exact dvd_mul_of_dvd_right this _
      have h2_ai₁ : 2 ∣ a + i₁ := Int.ofNat_dvd.mp (by rw [Nat.cast_add, hi₁_id]; exact dvd_add h2_a1A h2_prod)
      exact h2s_not_dvd (by rw [hs_eq, pow_one]; exact h2_ai₁)
    have h2sm1_dvd : (2 ^ (s - 1) : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ) :=
      (by rw [hQ_eq]; exact_mod_cast dvd_mul_right (2 ^ (s - 1)) u : (2 ^ (s - 1) : ℤ) ∣ (Q : ℤ)).trans hQ_dvd
    have h2s_not_a1A : ¬ ((2 ^ s : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ)) := by
      intro hd
      have h2s_prod : (2 ^ s : ℤ) ∣ ((A - 1 : ℕ) : ℤ) * ((B * R + 1 : ℕ) : ℤ) := by
        have : (2 ^ s : ℤ) ∣ ((B * R + 1 : ℕ) : ℤ) := by
          rw [← hBR1_eq]; exact_mod_cast dvd_mul_right (2 ^ s) u
        exact dvd_mul_of_dvd_right this _
      exact h2s_not_dvd (Int.ofNat_dvd.mp (by rw [Nat.cast_add, hi₁_id]; exact dvd_add hd h2s_prod))
    -- Equation (3): `(2^s : ℤ) ∣ (a + 1 - A) + 2^(s - 1)`
    have hEq3 : (2 ^ s : ℤ) ∣ (a : ℤ) + 1 - (A : ℤ) + (2 ^ (s - 1) : ℤ) := by
      rcases h2sm1_dvd with ⟨w, hw⟩
      have hw_odd : Odd w := by
        rcases Int.even_or_odd w with ⟨v, hv⟩ | ho
        · exfalso
          have h2s_eq : (2 ^ s : ℤ) = (2 ^ (s - 1) : ℤ) * 2 := by
            rw [← pow_succ, Nat.sub_add_cancel hs1]
          exact h2s_not_a1A ⟨v, by rw [hw, hv, h2s_eq]; ring⟩
        · exact ho
      rcases hw_odd with ⟨v, hv⟩
      have h2s_eq : (2 ^ s : ℤ) = (2 ^ (s - 1) : ℤ) * 2 := by
        rw [← pow_succ, Nat.sub_add_cancel hs1]
      refine ⟨v + 1, ?_⟩
      rw [hw, hv, h2s_eq]
      ring
    -- Step 4: Construct `u` distinct indices `i_t ∈ [1, k]` with `2^s * A ∣ τ (i_t)`
    have h2s_le_k : 2 ^ s ≤ k := by
      have h1 : 2 ^ s ≤ B * R + 1 := by rw [← hBR1_eq]; exact Nat.le_mul_of_pos_right _ (by omega)
      have h2 : 3 * (B * R) ≤ k := by rw [hR, mul_assoc]; exact Nat.mul_le_mul_right _ hA3
      omega
    have hcop_2sA : Nat.Coprime (2 ^ s) A :=
      (Nat.prime_two.coprime_iff_not_dvd.mpr
        (fun h => by rcases hA_odd with ⟨r, hr⟩; rcases h with ⟨t, ht⟩; omega)).pow_left s
    have h2sA_dvd_L : 2 ^ s * A ∣ lcmIcc k :=
      hcop_2sA.mul_dvd_of_dvd_of_dvd (dvd_lcmIcc (Nat.one_le_pow s 2 (by omega)) h2s_le_k)
        (dvd_lcmIcc (by omega) hAmem.2)
    have h2sm1_ge2 : 2 ≤ 2 ^ (s - 1) :=
      le_trans le_rfl (Nat.le_self_pow (by omega : s - 1 ≠ 0) 2)
    have h2s_eq_nat : 2 ^ s = 2 * 2 ^ (s - 1) := by rw [← pow_succ', Nat.sub_add_cancel hs1]
    let idx : ℕ → ℕ := fun t => (2 ^ (s - 1) - 1) * A + 1 + t * (2 ^ s * A)
    have hidx_mem : ∀ t ∈ Finset.range u, idx t ∈ Set.Icc 1 k := by
      intro t ht
      have htu : t ≤ u - 1 := by have := Finset.mem_range.mp ht; omega
      refine ⟨by dsimp [idx]; omega, ?_⟩
      dsimp [idx]
      have hstep : (2 ^ (s - 1) - 1) * A + 1 + t * (2 ^ s * A) ≤
          (2 ^ (s - 1) - 1) * A + 1 + (u - 1) * (2 ^ s * A) := by
        gcongr
      have htop : (2 ^ (s - 1) - 1) * A + 1 + (u - 1) * (2 ^ s * A) + 2 ^ (s - 1) * A = k + 1 := by
        have h1 : (2 ^ (s - 1) - 1) * A + 2 ^ (s - 1) * A = (2 ^ s - 1) * A := by
          have h2sZ : (2 : ℤ) ^ s = 2 * (2 : ℤ) ^ (s - 1) := by exact_mod_cast h2s_eq_nat
          zify [show 1 ≤ 2 ^ (s - 1) by omega, show 1 ≤ 2 ^ s by omega]
          rw [h2sZ]; ring
        have h2 : (2 ^ s - 1) * A + (u - 1) * (2 ^ s * A) = (2 ^ s * u - 1) * A := by
          zify [show 1 ≤ 2 ^ s by omega, show 1 ≤ u by omega,
            Nat.mul_pos (Nat.one_le_pow s 2 (by omega)) hu1]
          ring
        have h3 : (2 ^ s * u - 1) * A = k := by
          rw [hBR1_eq, Nat.add_sub_cancel]; rw [hR]; ring
        linarith
      have hbig : 2 ≤ 2 ^ (s - 1) * A :=
        le_trans h2sm1_ge2 (Nat.le_mul_of_pos_right _ (by omega))
      omega
    have hidx_div : ∀ t ∈ Finset.range u, 2 ^ s * A ∣ τ (idx t) := by
      intro t ht
      have hmem := hidx_mem t ht
      rw [hgcd (idx t) hmem]
      refine Nat.dvd_gcd ?_ h2sA_dvd_L
      -- Show `2^s ∣ a + idx t` and `A ∣ a + idx t`
      have hA_div : A ∣ a + idx t := by
        have : a + idx t = (a + 1) + ((2 ^ (s - 1) - 1) + t * 2 ^ s) * A := by
          dsimp [idx]; ring
        rw [this]
        exact dvd_add hA_dvd_a1 (dvd_mul_left A _)
      have h2s_div : 2 ^ s ∣ a + idx t := by
        apply Int.ofNat_dvd.mp
        rcases hA_odd with ⟨r, hr⟩
        have hdecomp : (a : ℤ) + (idx t : ℤ) =
            ((a : ℤ) + 1 - (A : ℤ) + (2 ^ (s - 1) : ℤ)) +
            (2 ^ s : ℤ) * ((r : ℤ) + (t : ℤ) * (A : ℤ)) := by
          dsimp [idx]
          have h2sZ : (2 : ℤ) ^ s = 2 * (2 : ℤ) ^ (s - 1) := by exact_mod_cast h2s_eq_nat
          have hA_Z : (A : ℤ) = 2 * (r : ℤ) + 1 := by exact_mod_cast hr
          zify [show 1 ≤ 2 ^ (s - 1) by omega]
          rw [h2sZ, hA_Z]; ring
        rw [Nat.cast_add, hdecomp]
        exact dvd_add hEq3 (dvd_mul_right _ _)
      exact hcop_2sA.mul_dvd_of_dvd_of_dvd h2s_div hA_div
    -- Count: `u` distinct positive multiples of `2^s * A` in `[1, k]`, impossible since `k < u * (2^s * A)`!
    let M : Finset ℕ := (Finset.range u).image (fun t => τ (idx t))
    have hM_card : M.card = u := by
      rw [Finset.card_image_of_injOn, Finset.card_range]
      intro t₁ ht₁ t₂ ht₂ heq
      have hidx_eq : idx t₁ = idx t₂ :=
        hτ.1.injOn (hidx_mem t₁ ht₁) (hidx_mem t₂ ht₂) heq
      dsimp [idx] at hidx_eq
      have hmul : t₁ * (2 ^ s * A) = t₂ * (2 ^ s * A) := by omega
      exact Nat.eq_of_mul_eq_mul_right (Nat.mul_pos (Nat.pow_pos (by decide)) (by omega)) hmul
    have hM_sub : M ⊆ (Finset.Icc 1 (u - 1)).image (fun q => q * (2 ^ s * A)) := by
      intro y hy
      rcases Finset.mem_image.mp hy with ⟨t, ht, rfl⟩
      rcases hidx_div t ht with ⟨q, hq⟩
      have hτmem := hτ.1.mapsTo (hidx_mem t ht)
      have hq1 : 1 ≤ q := by
        by_contra h0
        have hq0 : q = 0 := by omega
        rw [hq0, mul_zero] at hq
        have := hτmem.1; omega
      have hk_lt : k < u * (2 ^ s * A) := by
        have hsum : k + A = u * (2 ^ s * A) := by
          calc k + A = A * (B * R + 1) := by rw [hR]; ring
            _ = A * (2 ^ s * u) := by rw [hBR1_eq]
            _ = u * (2 ^ s * A) := by ring
        omega
      have hqu : q ≤ u - 1 := by
        have hle : q * (2 ^ s * A) ≤ k := by have := hτmem.2; linarith
        have hq_lt_u : q < u := by
          by_contra hge
          have : u * (2 ^ s * A) ≤ q * (2 ^ s * A) := Nat.mul_le_mul_right _ (by omega)
          omega
        omega
      exact Finset.mem_image.mpr ⟨q, Finset.mem_Icc.mpr ⟨hq1, hqu⟩, by linarith⟩
    have hle_card : M.card ≤ ((Finset.Icc 1 (u - 1)).image (fun q => q * (2 ^ s * A))).card :=
      Finset.card_le_card hM_sub
    have hcard_rhs : ((Finset.Icc 1 (u - 1)).image (fun q => q * (2 ^ s * A))).card ≤ u - 1 := by
      calc ((Finset.Icc 1 (u - 1)).image (fun q => q * (2 ^ s * A))).card
          ≤ (Finset.Icc 1 (u - 1)).card := Finset.card_image_le
        _ = u - 1 := by rw [Nat.card_Icc]; omega
    omega
  -- Split on `σ 1 < σ k` vs `σ k < σ 1` (`σ 1 ≠ σ k` since `σ` is injective and `1 ≠ k`)
  have h1mem : 1 ∈ Set.Icc 1 k := ⟨le_rfl, by omega⟩
  have hkmem : k ∈ Set.Icc 1 k := ⟨by omega, le_rfl⟩
  have h1_gt : 1 < σ 1 := by have := (hσ.1.mapsTo h1mem).1; omega
  have hk_gt : 1 < σ k := by have := (hσ.1.mapsTo hkmem).1; omega
  have hne : σ 1 ≠ σ k := fun h => by
    have := hσ.1.injOn h1mem hkmem h; omega
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · exact hcontra σ hσ h1_gt hlt
  · have hrev := wcs_rev hσ
    exact hcontra (fun i => σ (k + 1 - i)) hrev
      (by simpa [show k + 1 - 1 = k by omega] using hk_gt)
      (by simpa [show k + 1 - 1 = k by omega, show k + 1 - k = 1 by omega] using hgt)

/-! ## Section 5: Main Theorems -/

/-- **Main Theorem (Garrison–Seiler–Knowles `arXiv:2401.09497v1`, Conjecture 5.2):**
For every integer `k ≥ 1`, every weakly consecutive permutation `σ` of `{1, ..., k}` satisfies
`σ(1) = 1` or `σ(k) = 1`. -/
theorem garrison_conjecture_5_2 {k : ℕ} (hk : 1 ≤ k) {σ : ℕ → ℕ}
    (hσ : IsWeaklyConsecutive k σ) : σ 1 = 1 ∨ σ k = 1 := by
  by_cases hk1 : k = 1
  · subst hk1
    left
    have h := hσ.1.mapsTo (show 1 ∈ Set.Icc 1 1 from ⟨le_rfl, le_rfl⟩)
    simp only [Set.mem_Icc] at h
    omega
  by_cases hk2 : k = 2
  · subst hk2
    rcases hσ.1.surjOn (show 1 ∈ Set.Icc 1 2 from ⟨le_rfl, by omega⟩) with ⟨i, hi, hσi⟩
    simp only [Set.mem_Icc] at hi
    have hi_cases : i = 1 ∨ i = 2 := by omega
    rcases hi_cases with rfl | rfl
    · exact Or.inl hσi
    · exact Or.inr hσi
  have hk3 : 3 ≤ k := by omega
  rcases Nat.even_or_odd k with heven | hodd
  · have hk4 : 4 ≤ k := by rcases heven with ⟨r, hr⟩; omega
    exact wcs_even hk4 heven hσ
  · exact wcs_odd hk3 hodd hσ

/-- Equivalent formulation directly for `σ : Equiv.Perm (Fin k)` (`k ≥ 1`):
`(σ ⟨0, _⟩).val + 1 = 1 ∨ (σ ⟨k - 1, _⟩).val + 1 = 1`. -/
theorem garrison_conjecture_5_2_perm {k : ℕ} (hk : 1 ≤ k) (σ : Equiv.Perm (Fin k))
    (hσ : IsWeaklyConsecutivePerm σ) :
    (σ ⟨0, by omega⟩).val = 0 ∨ (σ ⟨k - 1, by omega⟩).val = 0 := by
  let f : ℕ → ℕ := fun i =>
    if h : 1 ≤ i ∧ i ≤ k then (σ ⟨i - 1, by omega⟩).val + 1 else 0
  have hf : IsWeaklyConsecutive k f := by
    refine ⟨⟨?_, ?_, ?_⟩, ?_⟩
    · intro i hi
      simp only [Set.mem_Icc] at hi ⊢
      simp only [f, dite_eq_left hi]
      exact ⟨by omega, (σ ⟨i - 1, by omega⟩).isLt⟩
    · intro i hi j hj heq
      simp only [Set.mem_Icc] at hi hj
      simp only [f, dite_eq_left hi, dite_eq_left hj] at heq
      have hfin : σ ⟨i - 1, by omega⟩ = σ ⟨j - 1, by omega⟩ := Fin.ext (by omega)
      have harg := σ.injective hfin
      have hval := congrArg Fin.val harg
      dsimp at hval
      omega
    · intro y hy
      simp only [Set.mem_Icc] at hy
      let x : Fin k := σ.symm ⟨y - 1, by omega⟩
      refine ⟨x.val + 1, ⟨by omega, x.isLt⟩, ?_⟩
      simp only [f, dite_eq_left (show 1 ≤ x.val + 1 ∧ x.val + 1 ≤ k from ⟨by omega, x.isLt⟩)]
      have hx : (⟨x.val + 1 - 1, by omega⟩ : Fin k) = x := Fin.ext (by simp)
      rw [hx]
      dsimp [x]
      rw [Equiv.apply_symm_apply]
      dsimp
      omega
    · intro i hi j hj m hdiv hsub
      simp only [Set.mem_Icc] at hi hj
      simp only [f, dite_eq_left hi, dite_eq_left hj] at hdiv ⊢
      have h1 : (((⟨i - 1, by omega⟩ : Fin k).val + 1 : ℕ) : ℤ) = (i : ℤ) := by
        dsimp; omega
      have h2 : (((⟨j - 1, by omega⟩ : Fin k).val + 1 : ℕ) : ℤ) = (j : ℤ) := by
        dsimp; omega
      exact hσ ⟨i - 1, by omega⟩ ⟨j - 1, by omega⟩ m
        (by exact_mod_cast hdiv) (by rw [h1, h2]; exact hsub)
  have hres := garrison_conjecture_5_2 hk hf
  rcases hres with h1 | hk'
  · left
    simp only [f, dite_eq_left (show 1 ≤ 1 ∧ 1 ≤ k from ⟨le_rfl, hk⟩)] at h1
    change (σ ⟨0, by omega⟩).val + 1 = 1 at h1
    omega
  · right
    simp only [f, dite_eq_left (show 1 ≤ k ∧ k ≤ k from ⟨hk, le_rfl⟩)] at hk'
    omega

#print axioms wcs_residue_class
#print axioms wcs_gcd_repr
#print axioms garrison_conjecture_5_2
#print axioms garrison_conjecture_5_2_perm

end OpenMath.Garrison240109497Conj52
