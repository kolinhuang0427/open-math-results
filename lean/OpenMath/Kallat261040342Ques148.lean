import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.CardEmbedding
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.Perm.Cycle.Basic
import Mathlib.Tactic

/-!
# Refutation of Question 14.8 (`\label{prob:composite}`) of Kallat (`arXiv:2610.40342v1`)

This module formalizes the refutation of **Question 14.8** (`\label{prob:composite}`, Section 14)
of Ahaan Kallat, *"A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths"*,
`arXiv:2610.40342v1`, across **all three non-constant regimes** (odd $p$ with sign $+$, odd $p$
with sign $-$, and $p = 2$ with sign $+$), directly from the permutation-counting definition
$$a_A(n) = \#\{\sigma \in S_n : \text{every cycle length of } \sigma \text{ lies in } A\}.$$

## Main results

- `aPerm_succ_rec`: Exact combinatorial proof of Kallat's cycle-of-$n$ recurrence (equation `(1.2)`,
  `\label{eq:last0}`):
  $$a_A(n + 1) = \sum_{\substack{1 \le m \le n + 1 \\ m \in A}} (n)_{m-1} \, a_A(n + 1 - m).$$
- `kallat_counterexample_odd_plus`: For $A = \{1, 7\}$, $p = 3$, $e = 3$ (type II, sign $+$,
  predicted period $3^3 = 27$), $a_A(n) \bmod 27$ is non-constant with exact least period
  $9 < 27$.
- `kallat_counterexample_odd_minus`: For $A = \{5\}$, $p = 5$, $e = 2$ (type II, sign $-$,
  predicted period $2 \cdot 5^2 = 50$), $a_A(n) \bmod 25$ is non-constant with exact least period
  $10 < 50$.
- `kallat_counterexample_even`: For $A = \{2, 4\}$, $p = 2$, $e = 2$ (type II, sign $+$,
  predicted period $2^2 = 4$), $a_A(n) \bmod 4$ is non-constant with exact least period
  $2 < 4$.
- `not_kallat_question_14_8`: Direct negation of the universal statement of Question 14.8
  (even restricted to non-constant sequences mod $p^e$).
-/

namespace OpenMath.Kallat261040342Ques148

open Finset

/-! ## Section 1: Permutations with Restricted Cycle Lengths and Kallat's Definitions -/

/-- A permutation $\sigma \in S_n$ has all cycle lengths in $A \subseteq \mathbb{N}$ if the orbit
(cycle) of every element $x \in \mathrm{Fin}\,n$ under $\sigma$ has cardinality in $A$. -/
def AllCyclesIn (A : Set ℕ) {n : ℕ} (σ : Equiv.Perm (Fin n)) : Prop := by
  classical exact ∀ x : Fin n, (Finset.univ.filter (fun y : Fin n => σ.SameCycle x y)).card ∈ A

/-- $a_A(n)$: number of permutations of $\mathrm{Fin}\,n$ all of whose cycle lengths lie in $A$. -/
noncomputable def aPerm (A : Set ℕ) (n : ℕ) : ℕ := by
  classical exact Fintype.card { σ : Equiv.Perm (Fin n) // AllCyclesIn A σ }

/-- Definition 13.1 (`\label{def:types}`): a prime $p$ is of **type II** for $A$ if
$[1 \in A] \neq [p \in A]$. -/
def IsTypeII (A : Set ℕ) (p : ℕ) : Prop :=
  Nat.Prime p ∧ ((1 ∈ A) ↔ (p ∉ A))

/-- Lemma 13.2(a) (`\label{lem:typeB}`): the condition under which the sign in
$a_A(n + p^e) \equiv \pm a_A(n) \pmod{p^e}$ is $-$.
For odd $p$, the sign is $-$ iff $1 \notin A \wedge p \in A$.
For $p = 2$, the sign is $+$ except when $e = 2$, where it is $(-1)^{[2 \in A] + [4 \in A]}$
(i.e. $-$ iff $[2 \in A] \neq [4 \in A]$). -/
def typeIINegSign (A : Set ℕ) (p e : ℕ) : Prop :=
  (p ≠ 2 ∧ 1 ∉ A ∧ p ∈ A) ∨ (p = 2 ∧ e = 2 ∧ ((2 ∈ A) ↔ (4 ∉ A)))

/-- The least period predicted by Question 14.8: $2 p^e$ when the Lemma 13.2(a) sign is $-$,
and $p^e$ otherwise. -/
noncomputable def predictedPeriod (A : Set ℕ) (p e : ℕ) : ℕ := by
  classical exact if typeIINegSign A p e then 2 * p ^ e else p ^ e

/-- $T > 0$ is a period of $f(n) \bmod M$. -/
def IsPeriodMod (f : ℕ → ℕ) (M T : ℕ) : Prop :=
  0 < T ∧ ∀ n : ℕ, f (n + T) ≡ f n [MOD M]

/-- $T$ is the least period of $f(n) \bmod M$. -/
def IsLeastPeriodMod (f : ℕ → ℕ) (M T : ℕ) : Prop :=
  IsPeriodMod f M T ∧ ∀ T' : ℕ, IsPeriodMod f M T' → T ≤ T'

/-- $f(n) \bmod M$ is non-constant. -/
def NonConstantMod (f : ℕ → ℕ) (M : ℕ) : Prop :=
  ∃ n₁ n₂ : ℕ, ¬ (f n₁ ≡ f n₂ [MOD M])

lemma aPerm_zero (A : Set ℕ) : aPerm A 0 = 1 := by
  classical
  unfold aPerm
  have : Unique { σ : Equiv.Perm (Fin 0) // AllCyclesIn A σ } :=
    { default := ⟨1, fun x => Fin.elim0 x⟩
      uniq := fun ⟨σ, _⟩ => Subtype.ext (Equiv.ext fun x => Fin.elim0 x) }
  exact Fintype.card_unique

/-! ## Section 2: Exact Combinatorial Proof of Kallat's Cycle-of-$n$ Recurrence `(1.2)` -/

section CycleRecurrence

/-- Orbit length (minimal positive iterate period) of $x$ under $\sigma \in S_n$. -/
private lemma exists_pos_pow_fix {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    ∃ k : ℕ, 0 < k ∧ (σ ^ k) x = x := by
  have hord : 0 < orderOf σ := orderOf_pos σ
  exact ⟨orderOf σ, hord, by rw [pow_orderOf_eq_one]; rfl⟩

private noncomputable def orbitLen {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) : ℕ := by
  classical exact Nat.find (exists_pos_pow_fix σ x)

private lemma orbitLen_pos {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    0 < orbitLen σ x := by
  classical exact (Nat.find_spec (exists_pos_pow_fix σ x)).1

private lemma pow_orbitLen_apply {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    (σ ^ orbitLen σ x) x = x := by
  classical exact (Nat.find_spec (exists_pos_pow_fix σ x)).2

private lemma pow_apply_ne_of_lt_orbitLen {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n)
    {k : ℕ} (hk0 : 0 < k) (hk : k < orbitLen σ x) : (σ ^ k) x ≠ x := by
  classical
  intro hEq
  exact Nat.find_min (exists_pos_pow_fix σ x) hk ⟨hk0, hEq⟩

private lemma zpow_mul_orbitLen_apply {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) (q : ℤ) :
    (σ ^ (q * (orbitLen σ x : ℤ))) x = x := by
  have h1 : (σ ^ (orbitLen σ x : ℤ)) x = x := by
    rw [zpow_natCast]; exact pow_orbitLen_apply σ x
  have hnat : ∀ m : ℕ, (σ ^ (m * orbitLen σ x)) x = x := by
    intro m
    induction m with
    | zero => simp
    | succ m ih =>
      rw [Nat.succ_mul, pow_add, Equiv.Perm.mul_apply, pow_orbitLen_apply, ih]
  rcases Int.eq_nat_or_neg q with ⟨m, rfl | rfl⟩
  · exact_mod_cast hnat m
  · have hinv : (σ ^ (m * orbitLen σ x))⁻¹ x = x := by
      apply (σ ^ (m * orbitLen σ x)).injective
      change (σ ^ (m * orbitLen σ x)) ((σ ^ (m * orbitLen σ x)).symm x) = _
      rw [Equiv.apply_symm_apply]
      exact (hnat m).symm
    have heq : (-(m : ℤ)) * (orbitLen σ x : ℤ) = -((m * orbitLen σ x : ℕ) : ℤ) := by push_cast; ring
    rw [heq, zpow_neg, zpow_natCast]
    exact hinv

private lemma pow_orbit_inj {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    Function.Injective (fun j : Fin (orbitLen σ x) => (σ ^ j.val) x) := by
  intro j₁ j₂ hEq
  apply Fin.ext
  by_contra hne
  have hlt_absurd : ∀ {a b : Fin (orbitLen σ x)}, a.val < b.val → (σ ^ a.val) x = (σ ^ b.val) x → False := by
    intro a b hlt h
    have hdiff : (σ ^ (b.val - a.val)) x = x := by
      apply (σ ^ a.val).injective
      rw [← Equiv.Perm.mul_apply, ← pow_add, Nat.add_sub_cancel' (le_of_lt hlt)]
      exact h.symm
    exact pow_apply_ne_of_lt_orbitLen σ x (by omega) (by have := b.isLt; omega) hdiff
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · exact hlt_absurd hlt hEq
  · exact hlt_absurd hgt hEq.symm

private lemma mem_sameCycle_iff_exists_fin {n : ℕ} (σ : Equiv.Perm (Fin n)) (x y : Fin n) :
    σ.SameCycle x y ↔ ∃ j : Fin (orbitLen σ x), (σ ^ j.val) x = y := by
  constructor
  · rintro ⟨k, rfl⟩
    let d := orbitLen σ x
    have hd : 0 < d := orbitLen_pos σ x
    have hdZ : (0 : ℤ) < (d : ℤ) := Int.natCast_pos.mpr hd
    let r : ℤ := k % (d : ℤ)
    have hr0 : 0 ≤ r := Int.emod_nonneg k (ne_of_gt hdZ)
    have hrlt : r < (d : ℤ) := Int.emod_lt_of_pos k hdZ
    let rN : ℕ := r.toNat
    have hrN_lt : rN < d := by omega
    have hrN_eq : (rN : ℤ) = r := Int.toNat_of_nonneg hr0
    refine ⟨⟨rN, hrN_lt⟩, ?_⟩
    have hdiv : k = (k / (d : ℤ)) * (d : ℤ) + r := by
      have := Int.mul_ediv_add_emod k (d : ℤ)
      linarith
    calc
      (σ ^ rN) x = (σ ^ r) x := by rw [← hrN_eq, zpow_natCast]
      _ = (σ ^ r) ((σ ^ ((k / (d : ℤ)) * (d : ℤ))) x) := by rw [zpow_mul_orbitLen_apply]
      _ = (σ ^ (r + (k / (d : ℤ)) * (d : ℤ))) x := by rw [← Equiv.Perm.mul_apply, ← zpow_add]
      _ = (σ ^ k) x := by rw [add_comm, ← hdiv]
  · rintro ⟨j, rfl⟩
    exact ⟨(j.val : ℤ), by simp⟩

private lemma card_sameCycle_eq_orbitLen {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    by classical exact (Finset.univ.filter (fun y : Fin n => σ.SameCycle x y)).card = orbitLen σ x := by
  classical
  have hEq : Finset.univ.filter (fun y : Fin n => σ.SameCycle x y) =
      Finset.univ.image (fun j : Fin (orbitLen σ x) => (σ ^ j.val) x) := by
    ext y
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image,
      mem_sameCycle_iff_exists_fin]
  rw [hEq, Finset.card_image_of_injective _ (pow_orbit_inj σ x), Finset.card_univ, Fintype.card_fin]

private lemma orbitLen_le_card {n : ℕ} (σ : Equiv.Perm (Fin n)) (x : Fin n) :
    orbitLen σ x ≤ n := by
  classical
  rw [← card_sameCycle_eq_orbitLen σ x]
  calc (Finset.univ.filter (fun y : Fin n => σ.SameCycle x y)).card
      ≤ (Finset.univ : Finset (Fin n)).card := Finset.card_le_card (Finset.subset_univ _)
    _ = n := Fintype.card_fin n

/-- Given `1 ≤ m ≤ n + 1` and an embedding `e : Fin (m - 1) ↪ Fin n`, build the explicit `m`-cycle
on `C_e = {Fin.last n} ∪ {e 0, ..., e (m - 2)}` combined with `τ` on the complement `Fin (n + 1 - m)`. -/
private noncomputable def orbitFinset {n m : ℕ} (e : Fin (m - 1) ↪ Fin n) : Finset (Fin (n + 1)) :=
  insert (Fin.last n) (Finset.univ.image (fun k : Fin (m - 1) => (e k).castSucc))

private lemma card_orbitFinset {n m : ℕ} (hm : 1 ≤ m) (e : Fin (m - 1) ↪ Fin n) :
    (orbitFinset e).card = m := by
  unfold orbitFinset
  have hnot : Fin.last n ∉ Finset.univ.image (fun k : Fin (m - 1) => (e k).castSucc) := by
    simp only [Finset.mem_image, Finset.mem_univ, true_and, not_exists]
    exact fun k => (Fin.castSucc_lt_last (e k)).ne
  rw [Finset.card_insert_of_notMem hnot,
    Finset.card_image_of_injective _ (fun a b h => e.injective (Fin.castSucc_injective n h)),
    Finset.card_univ, Fintype.card_fin]
  omega

private noncomputable def complEquiv {n m : ℕ} (hm1 : 1 ≤ m) (_hmn : m ≤ n + 1)
    (e : Fin (m - 1) ↪ Fin n) :
    { y : Fin (n + 1) // y ∉ orbitFinset e } ≃ Fin (n + 1 - m) := by
  classical
  apply Fintype.equivOfCardEq
  rw [Fintype.card_subtype_compl, Fintype.card_fin, Fintype.card_fin, Fintype.card_coe,
    card_orbitFinset hm1 e]

/-- Bijection `Fin m ≃ orbitFinset e` sending `0 ↦ Fin.last n` and `k + 1 ↦ (e k).castSucc`. -/
private noncomputable def orbitEquiv {n m : ℕ} (hm1 : 1 ≤ m) (e : Fin (m - 1) ↪ Fin n) :
    Fin m ≃ { y : Fin (n + 1) // y ∈ orbitFinset e } := by
  classical
  let fψ : Fin m → { y : Fin (n + 1) // y ∈ orbitFinset e } := fun j =>
    if hj : j.val = 0 then ⟨Fin.last n, Finset.mem_insert_self _ _⟩
    else ⟨(e ⟨j.val - 1, by have := j.isLt; omega⟩).castSucc,
      Finset.mem_insert_of_mem (Finset.mem_image.mpr ⟨_, Finset.mem_univ _, rfl⟩)⟩
  have hfψ_inj : Function.Injective fψ := by
    intro j₁ j₂ hEq
    have hval : (fψ j₁).1 = (fψ j₂).1 := congrArg Subtype.val hEq
    dsimp [fψ] at hval
    split_ifs at hval with h1 h2 h2
    · exact Fin.ext (h1.trans h2.symm)
    · exact ((Fin.castSucc_lt_last _).ne hval.symm).elim
    · exact ((Fin.castSucc_lt_last _).ne hval).elim
    · have hk := e.injective (Fin.castSucc_injective n hval)
      have hkv := congrArg Fin.val hk
      dsimp at hkv
      exact Fin.ext (by omega)
  have hcardψ : Fintype.card (Fin m) = Fintype.card { y : Fin (n + 1) // y ∈ orbitFinset e } := by
    rw [Fintype.card_fin, Fintype.card_coe, card_orbitFinset hm1 e]
  exact Equiv.ofBijective fψ ((Fintype.bijective_iff_injective_and_card fψ).mpr ⟨hfψ_inj, hcardψ⟩)

private lemma orbitEquiv_zero {n m : ℕ} (hm1 : 1 ≤ m) (e : Fin (m - 1) ↪ Fin n) :
    (orbitEquiv hm1 e ⟨0, by omega⟩).1 = Fin.last n := by
  simp [orbitEquiv]

private lemma orbitEquiv_succ {n m : ℕ} (hm1 : 1 ≤ m) (e : Fin (m - 1) ↪ Fin n) (k : Fin (m - 1)) :
    (orbitEquiv hm1 e ⟨k.val + 1, by have := k.isLt; omega⟩).1 = (e k).castSucc := by
  simp [orbitEquiv]

/-- Build a permutation of `Fin (n + 1)` from `(m, e, τ)`. -/
private noncomputable def buildPerm {n m : ℕ} (hm1 : 1 ≤ m) (hmn : m ≤ n + 1)
    (e : Fin (m - 1) ↪ Fin n) (τ : Equiv.Perm (Fin (n + 1 - m))) : Equiv.Perm (Fin (n + 1)) := by
  classical
  let φ := complEquiv hm1 hmn e
  let ψ := orbitEquiv hm1 e
  let cycM : Equiv.Perm (Fin m) :=
    { toFun := fun j => ⟨(j.val + 1) % m, Nat.mod_lt _ (by omega)⟩
      invFun := fun j => ⟨(j.val + (m - 1)) % m, Nat.mod_lt _ (by omega)⟩
      left_inv := fun j => by
        apply Fin.ext; dsimp
        have hj := j.isLt
        rw [Nat.mod_add_mod, show j.val + 1 + (m - 1) = j.val + m by omega,
          Nat.add_mod_right, Nat.mod_eq_of_lt hj]
      right_inv := fun j => by
        apply Fin.ext; dsimp
        have hj := j.isLt
        rw [Nat.mod_add_mod, show j.val + (m - 1) + 1 = j.val + m by omega,
          Nat.add_mod_right, Nat.mod_eq_of_lt hj] }
  let splitE : Fin (n + 1) ≃ { y // y ∈ orbitFinset e } ⊕ { y // y ∉ orbitFinset e } :=
    (Equiv.sumCompl (· ∈ orbitFinset e)).symm
  let permOnC : Equiv.Perm { y // y ∈ orbitFinset e } := ψ.symm.trans (cycM.trans ψ)
  let permOnCompl : Equiv.Perm { y // y ∉ orbitFinset e } := φ.trans (τ.trans φ.symm)
  exact splitE.trans ((Equiv.Perm.sumCongr permOnC permOnCompl).trans splitE.symm)

private lemma buildPerm_pow_last {n m : ℕ} (hm1 : 1 ≤ m) (hmn : m ≤ n + 1)
    (e : Fin (m - 1) ↪ Fin n) (τ : Equiv.Perm (Fin (n + 1 - m))) :
    ∀ j : ℕ,
      (buildPerm hm1 hmn e τ ^ j) (Fin.last n) =
        if hj : j % m = 0 then Fin.last n
        else (e ⟨j % m - 1, by have := Nat.mod_lt j (by omega : 0 < m); omega⟩).castSucc := by
  classical
  have hstep_last : buildPerm hm1 hmn e τ (Fin.last n) =
      if hm : m = 1 then Fin.last n else (e ⟨0, by omega⟩).castSucc := by
    unfold buildPerm
    dsimp only [Equiv.trans_apply]
    have hmem : Fin.last n ∈ orbitFinset e := Finset.mem_insert_self _ _
    simp only [Equiv.sumCompl_symm_apply_of_pos hmem, Equiv.Perm.sumCongr_apply, Sum.map_inl]
    have hψ_symm : (orbitEquiv hm1 e).symm ⟨Fin.last n, hmem⟩ = ⟨0, by omega⟩ := by
      rw [Equiv.symm_apply_eq]; exact Subtype.ext (orbitEquiv_zero hm1 e).symm
    change (orbitEquiv hm1 e ⟨(((orbitEquiv hm1 e).symm ⟨Fin.last n, hmem⟩).val + 1) % m,
      Nat.mod_lt _ (by omega)⟩).1 = _
    rw [hψ_symm]
    dsimp only
    by_cases hm : m = 1
    · subst hm
      simp only [↓reduceDIte]
      exact orbitEquiv_zero le_rfl e
    · have hmod : 1 % m = 1 := Nat.mod_eq_of_lt (by omega)
      simp only [hm, ↓reduceDIte]
      have hfin : (⟨(0 + 1) % m, Nat.mod_lt _ (by omega)⟩ : Fin m) = ⟨0 + 1, by omega⟩ :=
        Fin.ext (by simp [hmod])
      rw [hfin]
      exact orbitEquiv_succ hm1 e ⟨0, by omega⟩
  have hstep_e : ∀ k : Fin (m - 1),
      buildPerm hm1 hmn e τ ((e k).castSucc) =
        if hk : k.val + 1 < m - 1 then (e ⟨k.val + 1, hk⟩).castSucc else Fin.last n := by
    intro k
    unfold buildPerm
    dsimp only [Equiv.trans_apply]
    have hmem : (e k).castSucc ∈ orbitFinset e :=
      Finset.mem_insert_of_mem (Finset.mem_image.mpr ⟨k, Finset.mem_univ _, rfl⟩)
    simp only [Equiv.sumCompl_symm_apply_of_pos hmem, Equiv.Perm.sumCongr_apply, Sum.map_inl]
    have hψ_symm : (orbitEquiv hm1 e).symm ⟨(e k).castSucc, hmem⟩ = ⟨k.val + 1, by have := k.isLt; omega⟩ := by
      rw [Equiv.symm_apply_eq]; exact Subtype.ext (orbitEquiv_succ hm1 e k).symm
    change (orbitEquiv hm1 e ⟨(((orbitEquiv hm1 e).symm ⟨(e k).castSucc, hmem⟩).val + 1) % m,
      Nat.mod_lt _ (by omega)⟩).1 = _
    rw [hψ_symm]
    dsimp only
    by_cases hk : k.val + 1 < m - 1
    · have hmod : (k.val + 1 + 1) % m = k.val + 2 := Nat.mod_eq_of_lt (by omega)
      simp only [hk, ↓reduceDIte]
      have hfin : (⟨(k.val + 1 + 1) % m, Nat.mod_lt _ (by omega)⟩ : Fin m) =
          ⟨(k.val + 1) + 1, by omega⟩ := Fin.ext (by dsimp; omega)
      rw [hfin]
      exact orbitEquiv_succ hm1 e ⟨k.val + 1, hk⟩
    · have hk_eq : k.val + 1 + 1 = m := by have := k.isLt; omega
      simp only [hk, ↓reduceDIte]
      have hfin : (⟨(k.val + 1 + 1) % m, Nat.mod_lt _ (by omega)⟩ : Fin m) =
          ⟨0, by omega⟩ := Fin.ext (by simp [hk_eq])
      rw [hfin]
      exact orbitEquiv_zero hm1 e
  intro j
  induction j with
  | zero => simp
  | succ j ih =>
    rw [pow_succ', Equiv.Perm.mul_apply, ih]
    by_cases hj : j % m = 0
    · simp only [hj, ↓reduceDIte]
      rw [hstep_last]
      by_cases hm : m = 1
      · subst hm; simp only [Nat.mod_one, ↓reduceDIte]
      · have hmod : (j + 1) % m = 1 := by
          rw [Nat.add_mod, hj, zero_add, Nat.mod_mod, Nat.mod_eq_of_lt (by omega)]
        have hne0 : (j + 1) % m ≠ 0 := by omega
        simp only [hm, hne0, ↓reduceDIte]
        congr 2; apply Fin.ext; dsimp; omega
    · simp only [hj, ↓reduceDIte]
      rw [hstep_e]
      have hlt : j % m < m := Nat.mod_lt j (by omega)
      by_cases hk : j % m - 1 + 1 < m - 1
      · have hmod : (j + 1) % m = j % m + 1 := by
          rw [Nat.add_mod, Nat.mod_eq_of_lt (by omega : 1 < m), Nat.mod_eq_of_lt (by omega)]
        have hne0 : (j + 1) % m ≠ 0 := by omega
        simp only [hk, hne0, ↓reduceDIte]
        congr 2; apply Fin.ext; dsimp; omega
      · have hjm : j % m = m - 1 := by omega
        have hmod : (j + 1) % m = 0 := by
          rw [Nat.add_mod, hjm, show m - 1 + 1 % m = m by
            have : 1 < m := by omega
            rw [Nat.mod_eq_of_lt this]; omega, Nat.mod_self]
        simp only [hk, hmod, ↓reduceDIte]

private lemma buildPerm_orbitLen_last {n m : ℕ} (hm1 : 1 ≤ m) (hmn : m ≤ n + 1)
    (e : Fin (m - 1) ↪ Fin n) (τ : Equiv.Perm (Fin (n + 1 - m))) :
    orbitLen (buildPerm hm1 hmn e τ) (Fin.last n) = m := by
  classical
  unfold orbitLen
  rw [Nat.find_eq_iff]
  refine ⟨⟨by omega, ?_⟩, ?_⟩
  · rw [buildPerm_pow_last hm1 hmn e τ m]
    simp
  · intro k hk ⟨hk0, hfix⟩
    rw [buildPerm_pow_last hm1 hmn e τ k] at hfix
    have hmod : k % m = k := Nat.mod_eq_of_lt hk
    have hne0 : k % m ≠ 0 := by omega
    simp only [hne0, ↓reduceDIte] at hfix
    exact (Fin.castSucc_lt_last _).ne hfix

private lemma buildPerm_on_compl {n m : ℕ} (hm1 : 1 ≤ m) (hmn : m ≤ n + 1)
    (e : Fin (m - 1) ↪ Fin n) (τ : Equiv.Perm (Fin (n + 1 - m)))
    (y : { y : Fin (n + 1) // y ∉ orbitFinset e }) :
    buildPerm hm1 hmn e τ y.1 =
      ((complEquiv hm1 hmn e).symm (τ (complEquiv hm1 hmn e y))).1 := by
  classical
  unfold buildPerm
  dsimp only [Equiv.trans_apply]
  rw [Equiv.sumCompl_symm_apply_of_neg y.2]
  simp [complEquiv]

private lemma buildPerm_allCyclesIn {n m : ℕ} (A : Set ℕ) (hm1 : 1 ≤ m) (hmn : m ≤ n + 1)
    (hmA : m ∈ A) (e : Fin (m - 1) ↪ Fin n) (τ : Equiv.Perm (Fin (n + 1 - m)))
    (hτ : AllCyclesIn A τ) : AllCyclesIn A (buildPerm hm1 hmn e τ) := by
  classical
  let σ := buildPerm hm1 hmn e τ
  let φ := complEquiv hm1 hmn e
  intro x
  rw [card_sameCycle_eq_orbitLen]
  by_cases hx : x ∈ orbitFinset e
  · have hsame : σ.SameCycle (Fin.last n) x := by
      rcases Finset.mem_insert.mp hx with rfl | hx_img
      · exact Equiv.Perm.SameCycle.refl σ _
      · rcases Finset.mem_image.mp hx_img with ⟨k, _, rfl⟩
        rw [mem_sameCycle_iff_exists_fin, buildPerm_orbitLen_last hm1 hmn e τ]
        refine ⟨⟨k.val + 1, by have := k.isLt; omega⟩, ?_⟩
        rw [buildPerm_pow_last hm1 hmn e τ (k.val + 1)]
        have hmod : (k.val + 1) % m = k.val + 1 := Nat.mod_eq_of_lt (by have := k.isLt; omega)
        have hne0 : (k.val + 1) % m ≠ 0 := by omega
        simp only [hne0, ↓reduceDIte]
        congr 2; apply Fin.ext; dsimp; omega
    have hcard_eq : (Finset.univ.filter (fun y => σ.SameCycle x y)).card =
        (Finset.univ.filter (fun y => σ.SameCycle (Fin.last n) y)).card := by
      congr 1; ext y; simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      exact ⟨fun h => hsame.trans h, fun h => hsame.symm.trans h⟩
    rw [← card_sameCycle_eq_orbitLen σ x, hcard_eq, card_sameCycle_eq_orbitLen σ (Fin.last n),
      buildPerm_orbitLen_last hm1 hmn e τ]
    exact hmA
  · have hpow_compl : ∀ k : ℕ, ∀ y : { y : Fin (n + 1) // y ∉ orbitFinset e },
        (σ ^ k) y.1 = (φ.symm ((τ ^ k) (φ y))).1 := by
      intro k
      induction k with
      | zero => intro y; simp
      | succ k ih =>
        intro y
        rw [pow_succ', Equiv.Perm.mul_apply, ih y, pow_succ', Equiv.Perm.mul_apply]
        have h := buildPerm_on_compl hm1 hmn e τ (φ.symm ((τ ^ k) (φ y)))
        simpa [σ, φ] using h
    have horb_eq : orbitLen σ x = orbitLen τ (φ ⟨x, hx⟩) := by
      unfold orbitLen
      congr 1
      ext k
      constructor
      · rintro ⟨hk0, hfix⟩
        refine ⟨hk0, ?_⟩
        have h1 := hpow_compl k ⟨x, hx⟩
        rw [hfix] at h1
        have h2 : φ.symm ((τ ^ k) (φ ⟨x, hx⟩)) = ⟨x, hx⟩ := Subtype.ext h1.symm
        simpa using congrArg φ h2
      · rintro ⟨hk0, hfix⟩
        refine ⟨hk0, ?_⟩
        rw [hpow_compl k ⟨x, hx⟩, hfix, Equiv.symm_apply_apply]
    rw [horb_eq, ← card_sameCycle_eq_orbitLen τ (φ ⟨x, hx⟩)]
    exact hτ (φ ⟨x, hx⟩)

/-- Extracted embedding of the `m - 1` orbit elements after `Fin.last n`. -/
private noncomputable def orbitEmb {n : ℕ} (σ : Equiv.Perm (Fin (n + 1))) :
    Fin (orbitLen σ (Fin.last n) - 1) ↪ Fin n :=
  ⟨fun k => ⟨((σ ^ (k.val + 1)) (Fin.last n)).val, by
      have hlt := ((σ ^ (k.val + 1)) (Fin.last n)).isLt
      have hne : (σ ^ (k.val + 1)) (Fin.last n) ≠ Fin.last n :=
        pow_apply_ne_of_lt_orbitLen σ (Fin.last n) (by omega) (by have := k.isLt; omega)
      have hval : ((σ ^ (k.val + 1)) (Fin.last n)).val ≠ n := fun h => hne (Fin.ext h)
      omega⟩,
    fun k₁ k₂ hEq => by
      dsimp only at hEq
      have hval : ((σ ^ (k₁.val + 1)) (Fin.last n)).val = ((σ ^ (k₂.val + 1)) (Fin.last n)).val :=
        congrArg (Fin.val (n := n)) hEq
      have h1 : (σ ^ (k₁.val + 1)) (Fin.last n) = (σ ^ (k₂.val + 1)) (Fin.last n) := Fin.ext hval
      have h2 := pow_orbit_inj σ (Fin.last n)
        (a₁ := ⟨k₁.val + 1, by have := k₁.isLt; omega⟩)
        (a₂ := ⟨k₂.val + 1, by have := k₂.isLt; omega⟩) h1
      have h3 := congrArg Fin.val h2
      dsimp at h3
      exact Fin.ext (by omega)⟩

private lemma mem_orbitFinset_orbitEmb_iff {n : ℕ} (σ : Equiv.Perm (Fin (n + 1))) (y : Fin (n + 1)) :
    y ∈ orbitFinset (orbitEmb σ) ↔ σ.SameCycle (Fin.last n) y := by
  rw [mem_sameCycle_iff_exists_fin]
  unfold orbitFinset
  simp only [Finset.mem_insert, Finset.mem_image, Finset.mem_univ, true_and]
  constructor
  · rintro (rfl | ⟨k, rfl⟩)
    · exact ⟨⟨0, orbitLen_pos σ (Fin.last n)⟩, rfl⟩
    · refine ⟨⟨k.val + 1, by have := k.isLt; omega⟩, ?_⟩
      apply Fin.ext; rfl
  · rintro ⟨j, rfl⟩
    by_cases hj : j.val = 0
    · left; simp [hj]
    · right
      refine ⟨⟨j.val - 1, by have := j.isLt; omega⟩, ?_⟩
      apply Fin.ext
      have hsub : j.val - 1 + 1 = j.val := by omega
      change ((σ ^ (j.val - 1 + 1)) (Fin.last n)).val = ((σ ^ j.val) (Fin.last n)).val
      rw [hsub]

/-- **Equation `(1.2)` (`\label{eq:last0}`) of Kallat (`arXiv:2610.40342v1`):**
For every $A \subseteq \mathbb{N}$ and every $n \in \mathbb{N}$,
$$a_A(n + 1) = \sum_{\substack{1 \le m \le n + 1 \\ m \in A}} (n)_{m - 1} \, a_A(n + 1 - m).$$ -/
theorem aPerm_succ_rec (A : Set ℕ) (n : ℕ) :
    by
      classical
      exact aPerm A (n + 1) =
        ∑ m ∈ (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A),
          n.descFactorial (m - 1) * aPerm A (n + 1 - m) := by
  classical
  unfold aPerm
  let Mset : Finset ℕ := (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A)
  let invF : (Σ m : { m // m ∈ Mset }, (Fin (m.1 - 1) ↪ Fin n) ×
        { τ : Equiv.Perm (Fin (n + 1 - m.1)) // AllCyclesIn A τ }) →
      { σ : Equiv.Perm (Fin (n + 1)) // AllCyclesIn A σ } := fun ⟨⟨m, hmM⟩, e, ⟨τ, hτ⟩⟩ =>
    have hmIcc := (Finset.mem_filter.mp hmM).1
    have hmA := (Finset.mem_filter.mp hmM).2
    have hm1 : 1 ≤ m := (Finset.mem_Icc.mp hmIcc).1
    have hmn : m ≤ n + 1 := (Finset.mem_Icc.mp hmIcc).2
    ⟨buildPerm hm1 hmn e τ, buildPerm_allCyclesIn A hm1 hmn hmA e τ hτ⟩
  have hinv_surj : Function.Surjective invF := by
    rintro ⟨σ, hσ⟩
    set m := orbitLen σ (Fin.last n)
    have hm1 : 1 ≤ m := orbitLen_pos σ (Fin.last n)
    have hmn : m ≤ n + 1 := orbitLen_le_card σ (Fin.last n)
    have hmA : m ∈ A := by
      have h := hσ (Fin.last n)
      rwa [card_sameCycle_eq_orbitLen] at h
    have hmM : m ∈ Mset := Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨hm1, hmn⟩, hmA⟩
    let e : Fin (m - 1) ↪ Fin n := orbitEmb σ
    have hOrb_eq : ∀ y : Fin (n + 1), y ∈ orbitFinset e ↔ σ.SameCycle (Fin.last n) y :=
      mem_orbitFinset_orbitEmb_iff σ
    have hσ_compl : ∀ y : Fin (n + 1), y ∉ orbitFinset e → σ y ∉ orbitFinset e := by
      intro y hy hmem; apply hy; rw [hOrb_eq] at hmem ⊢; exact hmem.trans ⟨-1, by simp⟩
    have hσ_inv_compl : ∀ y : Fin (n + 1), y ∉ orbitFinset e → σ⁻¹ y ∉ orbitFinset e := by
      intro y hy hmem; apply hy; rw [hOrb_eq] at hmem ⊢; exact hmem.trans ⟨1, by simp⟩
    let φ := complEquiv hm1 hmn e
    let σRestr : Equiv.Perm { y : Fin (n + 1) // y ∉ orbitFinset e } :=
      { toFun := fun y => ⟨σ y.1, hσ_compl y.1 y.2⟩
        invFun := fun y => ⟨σ⁻¹ y.1, hσ_inv_compl y.1 y.2⟩
        left_inv := fun y => Subtype.ext (σ.symm_apply_apply y.1)
        right_inv := fun y => Subtype.ext (σ.apply_symm_apply y.1) }
    let τ : Equiv.Perm (Fin (n + 1 - m)) := φ.symm.trans (σRestr.trans φ)
    have hτ : AllCyclesIn A τ := by
      intro z
      rw [card_sameCycle_eq_orbitLen]
      have hpow_τ : ∀ k : ℕ, (τ ^ k) z = φ ((σRestr ^ k) (φ.symm z)) := by
        intro k
        induction k with
        | zero => simp
        | succ k ih =>
          rw [pow_succ', Equiv.Perm.mul_apply, ih, pow_succ', Equiv.Perm.mul_apply]
          simp [τ]
      have hpow_restr : ∀ k : ℕ, ∀ y : { y : Fin (n + 1) // y ∉ orbitFinset e },
          ((σRestr ^ k) y).1 = (σ ^ k) y.1 := by
        intro k
        induction k with
        | zero => intro y; rfl
        | succ k ih =>
          intro y
          rw [pow_succ', Equiv.Perm.mul_apply, pow_succ', Equiv.Perm.mul_apply]
          exact congrArg σ (ih y)
      have horb_eq : orbitLen τ z = orbitLen σ (φ.symm z).1 := by
        unfold orbitLen
        congr 1; ext k
        constructor
        · rintro ⟨hk0, hfix⟩
          refine ⟨hk0, ?_⟩
          rw [hpow_τ] at hfix
          have h1 : (σRestr ^ k) (φ.symm z) = φ.symm z := by
            simpa using congrArg φ.symm hfix
          rw [← hpow_restr k (φ.symm z), h1]
        · rintro ⟨hk0, hfix⟩
          refine ⟨hk0, ?_⟩
          rw [hpow_τ]
          have h1 : (σRestr ^ k) (φ.symm z) = φ.symm z := Subtype.ext (by rw [hpow_restr]; exact hfix)
          rw [h1, Equiv.apply_symm_apply]
      rw [horb_eq, ← card_sameCycle_eq_orbitLen σ (φ.symm z).1]
      exact hσ (φ.symm z).1
    refine ⟨⟨⟨m, hmM⟩, e, ⟨τ, hτ⟩⟩, ?_⟩
    apply Subtype.ext
    apply Equiv.ext
    intro x
    change buildPerm hm1 hmn e τ x = σ x
    by_cases hx : x ∈ orbitFinset e
    · rcases Finset.mem_insert.mp hx with rfl | hx_img
      · have h1 := buildPerm_pow_last hm1 hmn e τ 1
        simp only [pow_one] at h1
        rw [h1]
        by_cases hm : m = 1
        · have hmod : 1 % m = 0 := by simp [hm]
          simp only [hmod, ↓reduceDIte]
          have hfix : (σ ^ 1) (Fin.last n) = Fin.last n := by
            have h := pow_orbitLen_apply σ (Fin.last n)
            change (σ ^ m) (Fin.last n) = Fin.last n at h
            rwa [hm] at h
          simpa using hfix.symm
        · have hmod : 1 % m = 1 := Nat.mod_eq_of_lt (by omega)
          have hne0 : 1 % m ≠ 0 := by omega
          simp only [hne0, ↓reduceDIte]
          apply Fin.ext
          change ((σ ^ ((1 % m - 1) + 1)) (Fin.last n)).val = (σ (Fin.last n)).val
          rw [hmod]; simp
      · rcases Finset.mem_image.mp hx_img with ⟨k, _, rfl⟩
        have hstep1 := buildPerm_pow_last hm1 hmn e τ (k.val + 1)
        have hstep2 := buildPerm_pow_last hm1 hmn e τ (k.val + 2)
        have hmod1 : (k.val + 1) % m = k.val + 1 := Nat.mod_eq_of_lt (by have := k.isLt; omega)
        have hne1 : (k.val + 1) % m ≠ 0 := by omega
        simp only [hne1, ↓reduceDIte] at hstep1
        have heq_k : (e ⟨(k.val + 1) % m - 1, by have := Nat.mod_lt (k.val + 1) (by omega : 0 < m); omega⟩).castSucc =
            (e k).castSucc := by
          congr 2; apply Fin.ext; dsimp; omega
        rw [heq_k] at hstep1
        have hpow_step : buildPerm hm1 hmn e τ ((e k).castSucc) =
            (buildPerm hm1 hmn e τ ^ (k.val + 2)) (Fin.last n) := by
          rw [← hstep1, ← Equiv.Perm.mul_apply, ← pow_succ']
        rw [hpow_step, hstep2]
        have hek_eq : (e k).castSucc = (σ ^ (k.val + 1)) (Fin.last n) := by
          apply Fin.ext; rfl
        rw [hek_eq, ← Equiv.Perm.mul_apply, ← pow_succ']
        by_cases hlast : k.val + 2 = m
        · have hmod2 : (k.val + 2) % m = 0 := by rw [hlast, Nat.mod_self]
          simp only [hmod2, ↓reduceDIte]
          rw [hlast]
          exact (pow_orbitLen_apply σ (Fin.last n)).symm
        · have hlt : k.val + 2 < m := by have := k.isLt; omega
          have hmod2 : (k.val + 2) % m = k.val + 2 := Nat.mod_eq_of_lt hlt
          have hne2 : (k.val + 2) % m ≠ 0 := by omega
          simp only [hne2, ↓reduceDIte]
          apply Fin.ext
          change ((σ ^ (((k.val + 2) % m - 1) + 1)) (Fin.last n)).val = ((σ ^ (k.val + 2)) (Fin.last n)).val
          rw [hmod2]
          have hsub : k.val + 2 - 1 + 1 = k.val + 2 := by omega
          rw [hsub]
    · rw [buildPerm_on_compl hm1 hmn e τ ⟨x, hx⟩]
      dsimp only [τ, Equiv.trans_apply]
      rw [Equiv.symm_apply_apply, Equiv.symm_apply_apply]
      rfl
  have hinv_inj : Function.Injective invF := by
    rintro ⟨⟨m₁, hmM₁⟩, e₁, ⟨τ₁, hτ₁⟩⟩ ⟨⟨m₂, hmM₂⟩, e₂, ⟨τ₂, hτ₂⟩⟩ hEq
    have hm1 : 1 ≤ m₁ := (Finset.mem_Icc.mp (Finset.mem_filter.mp hmM₁).1).1
    have hmn1 : m₁ ≤ n + 1 := (Finset.mem_Icc.mp (Finset.mem_filter.mp hmM₁).1).2
    have hm2 : 1 ≤ m₂ := (Finset.mem_Icc.mp (Finset.mem_filter.mp hmM₂).1).1
    have hmn2 : m₂ ≤ n + 1 := (Finset.mem_Icc.mp (Finset.mem_filter.mp hmM₂).1).2
    have hperm : buildPerm hm1 hmn1 e₁ τ₁ = buildPerm hm2 hmn2 e₂ τ₂ := congrArg Subtype.val hEq
    have hm_eq : m₁ = m₂ := by
      have h1 := buildPerm_orbitLen_last hm1 hmn1 e₁ τ₁
      have h2 := buildPerm_orbitLen_last hm2 hmn2 e₂ τ₂
      rw [hperm] at h1
      exact h1.symm.trans h2
    subst hm_eq
    have he_eq : e₁ = e₂ := by
      ext k
      have hk_lt : k.val + 1 < m₁ := by have h := k.isLt; dsimp at h; omega
      have hmod : (k.val + 1) % m₁ = k.val + 1 := Nat.mod_eq_of_lt hk_lt
      have hne0 : (k.val + 1) % m₁ ≠ 0 := by omega
      have h1 := buildPerm_pow_last hm1 hmn1 e₁ τ₁ (k.val + 1)
      have h2 := buildPerm_pow_last hm1 hmn1 e₂ τ₂ (k.val + 1)
      rw [hperm] at h1
      have hEq' := h1.symm.trans h2
      simp only [hne0, ↓reduceDIte] at hEq'
      have hfin := Fin.castSucc_injective n hEq'
      have hk_fin : (⟨(k.val + 1) % m₁ - 1, by have := Nat.mod_lt (k.val + 1) (by omega : 0 < m₁); omega⟩ :
          Fin (m₁ - 1)) = k := Fin.ext (by dsimp; omega)
      rw [hk_fin] at hfin
      exact congrArg Fin.val hfin
    subst he_eq
    have hτ_eq : τ₁ = τ₂ := by
      apply Equiv.ext
      intro z
      let y := (complEquiv hm1 hmn1 e₁).symm z
      have h1 := buildPerm_on_compl hm1 hmn1 e₁ τ₁ y
      have h2 := buildPerm_on_compl hm1 hmn1 e₁ τ₂ y
      rw [hperm] at h1
      have hEq' := h1.symm.trans h2
      have hsub : (complEquiv hm1 hmn1 e₁).symm (τ₁ (complEquiv hm1 hmn1 e₁ y)) =
          (complEquiv hm1 hmn1 e₁).symm (τ₂ (complEquiv hm1 hmn1 e₁ y)) := Subtype.ext hEq'
      have h3 := (complEquiv hm1 hmn1 e₁).symm.injective hsub
      simpa [y] using h3
    subst hτ_eq
    rfl
  have hinv_bij : Function.Bijective invF := ⟨hinv_inj, hinv_surj⟩
  rw [← Fintype.card_of_bijective hinv_bij, Fintype.card_sigma]
  rw [← Finset.sum_coe_sort Mset]
  refine Finset.sum_congr rfl fun m _ => ?_
  rw [Fintype.card_prod, Fintype.card_embedding_eq, Fintype.card_fin, Fintype.card_fin]

end CycleRecurrence

/-! ## Section 3: Counterexample 1 — Odd $p$, Sign $+$ ($A = \{1, 7\}$, $p = 3$, $e = 3$) -/

/-- Cycle-length set $A_1 = \{1, 7\}$ for odd $p = 3$, $e = 3$ (sign $+$, predicted period $27$). -/
def A1 : Set ℕ := {1, 7}

lemma A1_isTypeII : IsTypeII A1 3 := by
  refine ⟨by decide, ?_⟩
  simp [A1]

lemma A1_not_negSign : ¬ typeIINegSign A1 3 3 := by
  unfold typeIINegSign A1
  simp

lemma A1_predictedPeriod : predictedPeriod A1 3 3 = 27 := by
  classical
  unfold predictedPeriod
  simp only [A1_not_negSign, ↓reduceIte]
  norm_num

private lemma aPerm_A1_rec_lt {n : ℕ} (hn : n < 6) :
    aPerm A1 (n + 1) = aPerm A1 n := by
  classical
  rw [aPerm_succ_rec A1 n]
  have hfilt : (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A1) = {1} := by
    ext m
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_singleton, A1, Set.mem_insert_iff,
      Set.mem_singleton_iff]
    omega
  rw [hfilt, Finset.sum_singleton]
  simp

private lemma aPerm_A1_rec_ge {n : ℕ} (hn : 6 ≤ n) :
    aPerm A1 (n + 1) = aPerm A1 n + n.descFactorial 6 * aPerm A1 (n - 6) := by
  classical
  rw [aPerm_succ_rec A1 n]
  have hfilt : (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A1) = {1, 7} := by
    ext m
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_insert, Finset.mem_singleton,
      A1, Set.mem_insert_iff, Set.mem_singleton_iff]
    omega
  rw [hfilt, Finset.sum_pair (by decide : (1 : ℕ) ≠ 7)]
  have hsub : n + 1 - 7 = n - 6 := by omega
  simp [hsub]

private lemma aPerm_A1_mod27 :
    ∀ n : ℕ, aPerm A1 n ≡ 1 + 18 * n.choose 7 [MOD 27] := by
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    cases n with
    | zero =>
      rw [aPerm_zero]
      simp [Nat.ModEq]
    | succ n =>
      by_cases hn : n < 6
      · rw [aPerm_A1_rec_lt hn]
        have hch1 : n.choose 7 = 0 := Nat.choose_eq_zero_of_lt (by omega)
        have hch2 : (n + 1).choose 7 = 0 := Nat.choose_eq_zero_of_lt (by omega)
        have hih := ih n (by omega)
        rw [hch1] at hih
        rw [hch2]
        exact hih
      · have hn6 : 6 ≤ n := by omega
        rw [aPerm_A1_rec_ge hn6]
        have h1 := ih n (by omega)
        have h2 := ih (n - 6) (by omega)
        have hdesc : n.descFactorial 6 = 720 * n.choose 6 := by
          have := Nat.descFactorial_eq_factorial_mul_choose n 6
          simpa [Nat.factorial] using this
        have hterm : n.descFactorial 6 * aPerm A1 (n - 6) ≡ 18 * n.choose 6 [MOD 27] := by
          rw [hdesc]
          have hmul : 720 * n.choose 6 * aPerm A1 (n - 6) ≡
              720 * n.choose 6 * (1 + 18 * (n - 6).choose 7) [MOD 27] :=
            Nat.ModEq.mul_left _ h2
          refine hmul.trans ?_
          change (720 * n.choose 6 * (1 + 18 * (n - 6).choose 7)) % 27 = (18 * n.choose 6) % 27
          have h720 : 720 * n.choose 6 * (1 + 18 * (n - 6).choose 7) =
              18 * n.choose 6 + 27 * (26 * n.choose 6 + 480 * n.choose 6 * (n - 6).choose 7) := by
            ring
          rw [h720, Nat.add_mul_mod_self_left]
        have hsum := h1.add hterm
        refine hsum.trans ?_
        rw [Nat.choose_succ_succ n 6]
        have heq : 1 + 18 * n.choose 7 + 18 * n.choose 6 = 1 + 18 * (n.choose 6 + n.choose 7) := by
          ring
        rw [heq]

private lemma choose_seven_periodic_mod3 (n : ℕ) :
    (n + 9).choose 7 ≡ n.choose 7 [MOD 3] := by
  open Polynomial in
  have hchar : (3 : Polynomial (ZMod 3)) = 0 := by
    have : ((3 : ℕ) : Polynomial (ZMod 3)) = 0 := by
      rw [← Polynomial.C_eq_natCast, show ((3 : ℕ) : ZMod 3) = 0 from by decide, map_zero]
    simpa using this
  have hcube : ((1 + Polynomial.X : Polynomial (ZMod 3)) ^ 3) = 1 + Polynomial.X ^ 3 := by
    have h1 : (1 + Polynomial.X : Polynomial (ZMod 3)) ^ 3 =
        1 + 3 * Polynomial.X + 3 * Polynomial.X ^ 2 + Polynomial.X ^ 3 := by ring
    rw [h1, hchar]; ring
  have hpow9 : ((1 + Polynomial.X : Polynomial (ZMod 3)) ^ 9) = 1 + Polynomial.X ^ 9 := by
    have h1 : (1 + Polynomial.X : Polynomial (ZMod 3)) ^ 9 =
        ((1 + Polynomial.X : Polynomial (ZMod 3)) ^ 3) ^ 3 := by ring
    rw [h1, hcube]
    have h2 : (1 + Polynomial.X ^ 3 : Polynomial (ZMod 3)) ^ 3 =
        1 + 3 * Polynomial.X ^ 3 + 3 * Polynomial.X ^ 6 + Polynomial.X ^ 9 := by ring
    rw [h2, hchar]; ring
  have hpoly : (Polynomial.X + 1 : Polynomial (ZMod 3)) ^ (n + 9) =
      (Polynomial.X + 1 : Polynomial (ZMod 3)) ^ n +
      (Polynomial.X + 1 : Polynomial (ZMod 3)) ^ n * Polynomial.X ^ 9 := by
    rw [pow_add, add_comm Polynomial.X 1, hpow9]
    ring
  have hcoeff := congrArg (fun p : Polynomial (ZMod 3) => p.coeff 7) hpoly
  rw [Polynomial.coeff_add, Polynomial.coeff_X_add_one_pow, Polynomial.coeff_X_add_one_pow,
    Polynomial.coeff_mul_X_pow'] at hcoeff
  simp only [show ¬ 9 ≤ 7 by decide, ↓reduceIte, add_zero] at hcoeff
  exact (ZMod.natCast_eq_natCast_iff ((n + 9).choose 7) (n.choose 7) 3).mp hcoeff

/-- **Counterexample 1 (odd $p$, sign $+$):**
For $A_1 = \{1, 7\}$, $p = 3$, $e = 3$, $p$ is of type II with sign $+$ (predicted period $27$),
yet $a_{A_1}(n) \bmod 27$ is non-constant with exact least period $9 < 27$. -/
theorem kallat_counterexample_odd_plus :
    IsTypeII A1 3 ∧
    ¬ typeIINegSign A1 3 3 ∧
    predictedPeriod A1 3 3 = 27 ∧
    NonConstantMod (aPerm A1) (3 ^ 3) ∧
    IsLeastPeriodMod (aPerm A1) (3 ^ 3) 9 ∧
    9 ≠ predictedPeriod A1 3 3 := by
  have hper : IsPeriodMod (aPerm A1) 27 9 := by
    refine ⟨by decide, fun n => ?_⟩
    have h1 := aPerm_A1_mod27 (n + 9)
    have h2 := aPerm_A1_mod27 n
    have hch := choose_seven_periodic_mod3 n
    have h18 : 18 * (n + 9).choose 7 ≡ 18 * n.choose 7 [MOD 27] := by
      change (18 * (n + 9).choose 7) % 27 = (18 * n.choose 7) % 27
      have hc : (n + 9).choose 7 % 3 = n.choose 7 % 3 := hch
      have hdiv1 := Nat.div_add_mod ((n + 9).choose 7) 3
      have hdiv2 := Nat.div_add_mod (n.choose 7) 3
      omega
    exact h1.trans ((Nat.ModEq.add_left 1 h18).trans h2.symm)
  have hval_le6 : ∀ r : ℕ, r ≤ 6 → aPerm A1 r % 27 = 1 := by
    intro r hr
    have h := aPerm_A1_mod27 r
    have hch : r.choose 7 = 0 := Nat.choose_eq_zero_of_lt (by omega)
    rw [hch] at h
    exact h
  have hval7 : aPerm A1 7 % 27 = 19 := by
    have h := aPerm_A1_mod27 7
    simpa [Nat.ModEq] using h
  have hval8 : aPerm A1 8 % 27 = 10 := by
    have h := aPerm_A1_mod27 8
    simpa [Nat.ModEq] using h
  refine ⟨A1_isTypeII, A1_not_negSign, A1_predictedPeriod, ?_, ⟨hper, ?_⟩, ?_⟩
  · refine ⟨0, 7, ?_⟩
    change aPerm A1 0 % 27 ≠ aPerm A1 7 % 27
    rw [hval_le6 0 (by decide), hval7]; decide
  · intro T ⟨hT0, hT⟩
    by_contra hlt
    have hTle8 : T ≤ 8 := by omega
    by_cases hT8 : T = 8
    · subst hT8
      have h08 : aPerm A1 8 % 27 = aPerm A1 0 % 27 := hT 0
      rw [hval8, hval_le6 0 (by decide)] at h08
      omega
    · have hle6 : 7 - T ≤ 6 := by omega
      have h7 : aPerm A1 ((7 - T) + T) % 27 = aPerm A1 (7 - T) % 27 := hT (7 - T)
      have hadd : (7 - T) + T = 7 := by omega
      rw [hadd, hval7, hval_le6 (7 - T) hle6] at h7
      omega
  · rw [A1_predictedPeriod]; decide

/-! ## Section 4: Counterexample 2 — Odd $p$, Sign $-$ ($A = \{5\}$, $p = 5$, $e = 2$) -/

/-- Cycle-length set $A_2 = \{5\}$ for odd $p = 5$, $e = 2$ (sign $-$, predicted period $50$). -/
def A2 : Set ℕ := {5}

lemma A2_isTypeII : IsTypeII A2 5 := by
  refine ⟨by decide, ?_⟩
  simp [A2]

lemma A2_negSign : typeIINegSign A2 5 2 := by
  left
  simp [A2]

lemma A2_predictedPeriod : predictedPeriod A2 5 2 = 50 := by
  classical
  unfold predictedPeriod
  simp only [A2_negSign, ↓reduceIte]
  norm_num

private lemma aPerm_A2_rec_lt {n : ℕ} (hn : n < 4) : aPerm A2 (n + 1) = 0 := by
  classical
  rw [aPerm_succ_rec A2 n]
  have hfilt : (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A2) = ∅ := by
    ext m
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.notMem_empty, iff_false, A2,
      Set.mem_singleton_iff]
    omega
  rw [hfilt, Finset.sum_empty]

private lemma aPerm_A2_rec_ge {n : ℕ} (hn : 4 ≤ n) :
    aPerm A2 (n + 1) = n.descFactorial 4 * aPerm A2 (n - 4) := by
  classical
  rw [aPerm_succ_rec A2 n]
  have hfilt : (Finset.Icc 1 (n + 1)).filter (fun m => m ∈ A2) = {5} := by
    ext m
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_singleton, A2, Set.mem_singleton_iff]
    omega
  rw [hfilt, Finset.sum_singleton]
  have hsub : n + 1 - 5 = n - 4 := by omega
  simp [hsub]

private lemma aPerm_A2_not_dvd : ∀ n : ℕ, n % 5 ≠ 0 → aPerm A2 n = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    intro hmod
    cases n with
    | zero => exact absurd rfl hmod
    | succ n =>
      by_cases hn : n < 4
      · exact aPerm_A2_rec_lt hn
      · rw [aPerm_A2_rec_ge (by omega), ih (n - 4) (by omega) (by omega), mul_zero]

private lemma aPerm_A2_five_mul :
    ∀ k : ℕ, aPerm A2 (5 * k) % 25 = if k % 2 = 0 then 1 else 24 := by
  intro k
  induction k with
  | zero =>
    simp [aPerm_zero]
  | succ k ih =>
    have hstep : aPerm A2 (5 * (k + 1)) = (5 * k + 4).descFactorial 4 * aPerm A2 (5 * k) := by
      have heq : 5 * (k + 1) = (5 * k + 4) + 1 := by omega
      rw [heq, aPerm_A2_rec_ge (by omega)]
      have hsub : 5 * k + 4 - 4 = 5 * k := by omega
      rw [hsub]
    have hfac : (5 * k + 4).descFactorial 4 % 25 = 24 := by
      have hexp : (5 * k + 4).descFactorial 4 =
          (5 * k + 4) * (5 * k + 3) * (5 * k + 2) * (5 * k + 1) := by
        simp [Nat.descFactorial_succ]
        ring
      rw [hexp]
      have hid : (5 * k + 4) * (5 * k + 3) * (5 * k + 2) * (5 * k + 1) =
          24 + 25 * (25 * k ^ 4 + 50 * k ^ 3 + 35 * k ^ 2 + 10 * k) := by
        ring
      rw [hid, Nat.add_mul_mod_self_left]
    rw [hstep, Nat.mul_mod, hfac, ih]
    by_cases hk : k % 2 = 0
    · have hk1 : (k + 1) % 2 ≠ 0 := by omega
      simp [hk, hk1]
    · have hk1 : (k + 1) % 2 = 0 := by omega
      simp [hk, hk1]

/-- **Counterexample 2 (odd $p$, sign $-$):**
For $A_2 = \{5\}$, $p = 5$, $e = 2$, $p$ is of type II with sign $-$ (predicted period $50$),
yet $a_{A_2}(n) \bmod 25$ is non-constant with exact least period $10 < 50$. -/
theorem kallat_counterexample_odd_minus :
    IsTypeII A2 5 ∧
    typeIINegSign A2 5 2 ∧
    predictedPeriod A2 5 2 = 50 ∧
    NonConstantMod (aPerm A2) (5 ^ 2) ∧
    IsLeastPeriodMod (aPerm A2) (5 ^ 2) 10 ∧
    10 ≠ predictedPeriod A2 5 2 := by
  have hper : IsPeriodMod (aPerm A2) 25 10 := by
    refine ⟨by decide, fun n => ?_⟩
    change aPerm A2 (n + 10) % 25 = aPerm A2 n % 25
    by_cases h5 : n % 5 = 0
    · obtain ⟨k, rfl⟩ : ∃ k, n = 5 * k := ⟨n / 5, by omega⟩
      have h10 : 5 * k + 10 = 5 * (k + 2) := by omega
      rw [h10, aPerm_A2_five_mul (k + 2), aPerm_A2_five_mul k]
      have hmod2 : (k + 2) % 2 = k % 2 := by omega
      rw [hmod2]
    · rw [aPerm_A2_not_dvd (n + 10) (by omega), aPerm_A2_not_dvd n h5]
  refine ⟨A2_isTypeII, A2_negSign, A2_predictedPeriod, ?_, ⟨hper, ?_⟩, ?_⟩
  · refine ⟨0, 1, ?_⟩
    change aPerm A2 0 % 25 ≠ aPerm A2 1 % 25
    rw [aPerm_zero, aPerm_A2_not_dvd 1 (by decide)]
    decide
  · intro T ⟨hT0, hT⟩
    by_contra hlt
    have h0T : aPerm A2 T % 25 = aPerm A2 0 % 25 := by
      simpa [Nat.ModEq] using hT 0
    rw [aPerm_zero] at h0T
    by_cases hT5 : T = 5
    · subst hT5
      have h5 := aPerm_A2_five_mul 1
      simp at h5
      omega
    · have hnot5 : T % 5 ≠ 0 := by omega
      rw [aPerm_A2_not_dvd T hnot5] at h0T
      omega
  · rw [A2_predictedPeriod]; decide

/-! ## Section 5: Counterexample 3 — Even Prime $p = 2$ ($A = \{2, 4\}$, $p = 2$, $e = 2$) -/

/-- Cycle-length set $A_3 = \{2, 4\}$ for $p = 2$, $e = 2$ (sign $+$, predicted period $4$). -/
def A3 : Set ℕ := {2, 4}

lemma A3_isTypeII : IsTypeII A3 2 := by
  refine ⟨by decide, ?_⟩
  simp [A3]

lemma A3_not_negSign : ¬ typeIINegSign A3 2 2 := by
  unfold typeIINegSign A3
  simp

lemma A3_predictedPeriod : predictedPeriod A3 2 2 = 4 := by
  classical
  unfold predictedPeriod
  simp only [A3_not_negSign, ↓reduceIte]
  norm_num

private lemma aPerm_A3_mod4 :
    ∀ n : ℕ, aPerm A3 n % 4 = if n % 2 = 0 then 1 else 0 := by
  classical
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => simp [aPerm_zero]
    | 1 =>
      rw [aPerm_succ_rec A3 0]
      have hfilt : (Finset.Icc 1 1).filter (fun m => m ∈ A3) = ∅ := by
        ext m; simp [A3]; omega
      rw [hfilt, Finset.sum_empty]; decide
    | 2 =>
      rw [aPerm_succ_rec A3 1]
      have hfilt : (Finset.Icc 1 2).filter (fun m => m ∈ A3) = {2} := by
        ext m; simp [A3]; omega
      rw [hfilt, Finset.sum_singleton]
      simp [aPerm_zero]
    | 3 =>
      rw [aPerm_succ_rec A3 2]
      have hfilt : (Finset.Icc 1 3).filter (fun m => m ∈ A3) = {2} := by
        ext m; simp [A3]; omega
      rw [hfilt, Finset.sum_singleton]
      have h1 : aPerm A3 1 % 4 = 0 := ih 1 (by decide)
      rw [show (2 : ℕ) - 1 = 1 by decide, Nat.descFactorial_one, Nat.mul_mod, h1]
      decide
    | n + 4 =>
      rw [aPerm_succ_rec A3 (n + 3)]
      have hfilt : (Finset.Icc 1 (n + 4)).filter (fun m => m ∈ A3) = {2, 4} := by
        ext m; simp [A3]; omega
      rw [hfilt, Finset.sum_pair (by decide : (2 : ℕ) ≠ 4)]
      have hsub2 : n + 4 - 2 = n + 2 := by omega
      have hsub4 : n + 4 - 4 = n := by omega
      rw [hsub2, hsub4]
      have hih2 := ih (n + 2) (by omega)
      have hih0 := ih n (by omega)
      have hdesc1 : (n + 3).descFactorial 1 = n + 3 := Nat.descFactorial_one (n + 3)
      have hdesc3 : (n + 3).descFactorial 3 = (n + 3) * (n + 2) * (n + 1) := by
        simp [Nat.descFactorial_succ]; ring
      rw [hdesc1, hdesc3]
      by_cases hn : n % 2 = 0
      · have h2 : (n + 2) % 2 = 0 := by omega
        have h4 : (n + 4) % 2 = 0 := by omega
        simp only [h2, ↓reduceIte] at hih2
        simp only [hn, ↓reduceIte] at hih0
        simp only [h4, ↓reduceIte]
        obtain ⟨k, rfl⟩ : ∃ k, n = 2 * k := ⟨n / 2, by omega⟩
        rw [Nat.add_mod, Nat.mul_mod (2 * k + 3), Nat.mul_mod ((2 * k + 3) * (2 * k + 2) * (2 * k + 1)),
          hih2, hih0]
        have hcase : ((2 * k + 3) % 4 * 1 % 4 +
            ((2 * k + 3) * (2 * k + 2) * (2 * k + 1)) % 4 * 1 % 4) % 4 = 1 := by
          have hk : k % 2 = 0 ∨ k % 2 = 1 := by omega
          rcases hk with hk0 | hk1
          · obtain ⟨q, rfl⟩ : ∃ q, k = 2 * q := ⟨k / 2, by omega⟩
            have hA : (2 * (2 * q) + 3) % 4 = 3 := by omega
            have hB : ((2 * (2 * q) + 3) * (2 * (2 * q) + 2) * (2 * (2 * q) + 1)) % 4 = 2 := by
              have : (2 * (2 * q) + 3) * (2 * (2 * q) + 2) * (2 * (2 * q) + 1) =
                  2 + 4 * (16 * q ^ 3 + 24 * q ^ 2 + 11 * q + 1) := by ring
              rw [this, Nat.add_mul_mod_self_left]
            rw [hA, hB]
          · obtain ⟨q, rfl⟩ : ∃ q, k = 2 * q + 1 := ⟨k / 2, by omega⟩
            have hA : (2 * (2 * q + 1) + 3) % 4 = 1 := by omega
            have hB : ((2 * (2 * q + 1) + 3) * (2 * (2 * q + 1) + 2) * (2 * (2 * q + 1) + 1)) % 4 = 0 := by
              have : (2 * (2 * q + 1) + 3) * (2 * (2 * q + 1) + 2) * (2 * (2 * q + 1) + 1) =
                  4 * ((4 * q + 5) * (q + 1) * (4 * q + 3)) := by ring
              rw [this, Nat.mul_mod_right]
            rw [hA, hB]
        exact hcase
      · have h2 : (n + 2) % 2 ≠ 0 := by omega
        have h4 : (n + 4) % 2 ≠ 0 := by omega
        simp only [h2, ↓reduceIte] at hih2
        simp only [hn, ↓reduceIte] at hih0
        simp only [h4, ↓reduceIte]
        rw [Nat.add_mod, Nat.mul_mod (n + 3), Nat.mul_mod ((n + 3) * (n + 2) * (n + 1)), hih2, hih0]
        simp

/-- **Counterexample 3 ($p = 2$, sign $+$):**
For $A_3 = \{2, 4\}$, $p = 2$, $e = 2$, $p$ is of type II with sign $+$ (predicted period $4$),
yet $a_{A_3}(n) \bmod 4$ is non-constant with exact least period $2 < 4$. -/
theorem kallat_counterexample_even :
    IsTypeII A3 2 ∧
    ¬ typeIINegSign A3 2 2 ∧
    predictedPeriod A3 2 2 = 4 ∧
    NonConstantMod (aPerm A3) (2 ^ 2) ∧
    IsLeastPeriodMod (aPerm A3) (2 ^ 2) 2 ∧
    2 ≠ predictedPeriod A3 2 2 := by
  have hper : IsPeriodMod (aPerm A3) 4 2 := by
    refine ⟨by decide, fun n => ?_⟩
    change aPerm A3 (n + 2) % 4 = aPerm A3 n % 4
    rw [aPerm_A3_mod4 (n + 2), aPerm_A3_mod4 n]
    have h2 : (n + 2) % 2 = n % 2 := by omega
    rw [h2]
  refine ⟨A3_isTypeII, A3_not_negSign, A3_predictedPeriod, ?_, ⟨hper, ?_⟩, ?_⟩
  · refine ⟨0, 1, ?_⟩
    change aPerm A3 0 % 4 ≠ aPerm A3 1 % 4
    rw [aPerm_A3_mod4 0, aPerm_A3_mod4 1]; decide
  · intro T ⟨hT0, hT⟩
    by_contra hlt
    have hT1 : T = 1 := by omega
    subst hT1
    have h01 : aPerm A3 1 % 4 = aPerm A3 0 % 4 := hT 0
    rw [aPerm_A3_mod4 1, aPerm_A3_mod4 0] at h01
    simp at h01
  · rw [A3_predictedPeriod]; decide

/-! ## Section 6: Direct Negation of Question 14.8 -/

/-- **Refutation of Kallat (`arXiv:2610.40342v1`), Question 14.8 (`\label{prob:composite}`):**
It is NOT true that for every set $A \subseteq \mathbb{N}$, every prime $p$ of type II for $A$,
and every $e \ge 1$ (even restricting to non-constant $a_A(n) \bmod p^e$), the least period of
$a_A(n) \bmod p^e$ equals $p^e$ (or $2p^e$ when the Lemma 13.2(a) sign is $-$). -/
theorem not_kallat_question_14_8 :
    ¬ (∀ (A : Set ℕ) (p e : ℕ),
        IsTypeII A p → 1 ≤ e → NonConstantMod (aPerm A) (p ^ e) →
        IsLeastPeriodMod (aPerm A) (p ^ e) (predictedPeriod A p e)) := by
  intro hall
  rcases kallat_counterexample_odd_plus with ⟨hII, _, hpred, hnc, hleast, hne⟩
  have h27 := hall A1 3 3 hII (by decide) hnc
  have hle1 : 9 ≤ predictedPeriod A1 3 3 := hleast.2 _ h27.1
  have hle2 : predictedPeriod A1 3 3 ≤ 9 := h27.2 _ hleast.1
  exact hne (le_antisymm hle1 hle2)

end OpenMath.Kallat261040342Ques148

#print axioms OpenMath.Kallat261040342Ques148.aPerm_succ_rec
#print axioms OpenMath.Kallat261040342Ques148.kallat_counterexample_odd_plus
#print axioms OpenMath.Kallat261040342Ques148.kallat_counterexample_odd_minus
#print axioms OpenMath.Kallat261040342Ques148.kallat_counterexample_even
#print axioms OpenMath.Kallat261040342Ques148.not_kallat_question_14_8

