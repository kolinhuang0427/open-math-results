import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Powerset
import Mathlib.GroupTheory.Coset.Basic
import Mathlib.GroupTheory.Index
import Mathlib.GroupTheory.Subgroup.Simple
import Mathlib.Tactic

/-!
# Ciobanu–Turaev (`arXiv:2604.22375v1`, Section 3.1, Conjecture 1): `VPL^∀(G) = REG^∀(G)`

This file formalizes the complete proof of Conjecture 1 (`\label{conjecture1}`) of
Laura Ciobanu and Vladimir Turaev, *"Visibly Pushdown Languages in Groups"*
(`arXiv:2604.22375v1`, Section 1.1 & Section 3.1, lines 204–215 and 370–372):

> **Conjecture 1.** In all groups, every `VPL^∀` set is recognisable. In other words,
> the classes `VPL^∀` and `REG^∀` are equal.

Specifically, for every finitely generated group `G` (represented by a finite alphabet `Alph`
and a map `gen : Alph → G` whose canonical monoid homomorphism `π : List Alph → G` is surjective,
including the symmetric generating set `Alph = X ⊕ X` for `G = ⟨X⟩`), a subset `S ⊆ G` has
visibly pushdown preimage `π⁻¹(S)` if and only if `π⁻¹(S)` is regular (equivalently, `S`
is a finite union of cosets of a finite-index normal subgroup of `G`, i.e., recognisable).

## Main Results

* `OpenMath.Ciobanu260422375Conj1.vpa_empty_stack_on_mc`:
  Lemma 2(1) — every run of a VPA on a matched-call word `u ∈ MC(Alph)` starting with empty
  stack ends with empty stack.
* `OpenMath.Ciobanu260422375Conj1.vplForall_finiteIndex_stabL`:
  For every `S ∈ VPL^∀(G)`, the left-stabilizer subgroup `Stab_L(S) = {h ∈ G | h S = S}`
  has finite index `[G : Stab_L(S)] ≤ 2^|Q| < ∞` (both Case 1 `Σ_r = ∅` and Case 2 `Σ_r ≠ ∅`).
* `OpenMath.Ciobanu260422375Conj1.ciobanu_turaev_conjecture_1`:
  `IsVPLForall gen S ↔ IsREGForall gen S` (and `↔ IsRecognisable S`) for every finitely
  generated group `G` and every surjective monoid presentation `gen : Alph → G`.
* `OpenMath.Ciobanu260422375Conj1.ciobanu_turaev_conjecture_1_symGen`:
  The explicit `Σ = X ∪ X⁻¹` (`X ⊕ X`) specialization matching `G = ⟨X⟩`.
-/

namespace OpenMath.Ciobanu260422375Conj1

/-! ## Section 1: Words, Regular Languages, and Visibly Pushdown Automata -/

/-- Canonical monoid homomorphism `π : Alph* → G` induced by `gen : Alph → G`. -/
def evalWord {Alph G : Type*} [Monoid G] (gen : Alph → G) (w : List Alph) : G :=
  (w.map gen).prod

lemma evalWord_nil {Alph G : Type*} [Monoid G] (gen : Alph → G) :
    evalWord gen [] = 1 := by
  simp [evalWord]

lemma evalWord_cons {Alph G : Type*} [Monoid G] (gen : Alph → G) (a : Alph) (w : List Alph) :
    evalWord gen (a :: w) = gen a * evalWord gen w := by
  simp [evalWord]

lemma evalWord_append {Alph G : Type*} [Monoid G] (gen : Alph → G) (u v : List Alph) :
    evalWord gen (u ++ v) = evalWord gen u * evalWord gen v := by
  simp [evalWord]

lemma evalWord_singleton {Alph G : Type*} [Monoid G] (gen : Alph → G) (a : Alph) :
    evalWord gen [a] = gen a := by
  simp [evalWord]

/-- Standard deterministic finite automaton (DFA) over an alphabet `Alph`. -/
structure DetFA (Alph : Type*) where
  Q : Type
  [fintypeQ : Fintype Q]
  start : Q
  step : Q → Alph → Q
  accept : Set Q

attribute [instance] DetFA.fintypeQ

namespace DetFA

def evalFrom {Alph : Type*} (D : DetFA Alph) : D.Q → List Alph → D.Q
  | q, [] => q
  | q, a :: w => D.evalFrom (D.step q a) w

def Accepts {Alph : Type*} (D : DetFA Alph) (w : List Alph) : Prop :=
  D.evalFrom D.start w ∈ D.accept

end DetFA

/-- A language `L ⊆ Alph*` is regular (`REG`) if it is accepted by some finite automaton. -/
def IsRegular {Alph : Type*} (L : Set (List Alph)) : Prop :=
  ∃ D : DetFA Alph, ∀ w : List Alph, w ∈ L ↔ D.Accepts w

/-- Partition of a pushdown alphabet `Σ = Σ_c ⊔ Σ_i ⊔ Σ_r` into call, internal, and return letters. -/
inductive LetterKind
  | call
  | intern
  | ret
  deriving DecidableEq

/-- Visibly pushdown automaton (VPA) `M = (Q, Γ, δ, Q_0, F)` over `(Alph, kind)` following
Ciobanu–Turaev (`arXiv:2604.22375v1`, Section 1.1):
- no `ε`-transitions;
- `Γ` is the finite non-bottom stack alphabet (`Γ \ {⊥}`), and `List Γ` models the stack above
  the unique bottom-of-stack symbol `⊥` (`[]` means only `⊥` is on the stack);
- call letters (`Σ_c`) push a symbol `γ : Γ`;
- internal letters (`Σ_i`) leave the stack unchanged;
- return letters (`Σ_r`) pop the top symbol if the stack is non-empty, and leave `[]` (`⊥`)
  unchanged if the stack is empty;
- acceptance is by final state `q ∈ F` with arbitrary final stack contents. -/
structure VPA (Alph : Type*) (kind : Alph → LetterKind) where
  Q : Type
  [fintypeQ : Fintype Q]
  Γ : Type
  [fintypeΓ : Fintype Γ]
  start : Set Q
  accept : Set Q
  δ_call : Q → Alph → Q → Γ → Prop
  δ_intern : Q → Alph → Q → Prop
  δ_ret_nonempty : Q → Alph → Γ → Q → Prop
  δ_ret_empty : Q → Alph → Q → Prop

attribute [instance] VPA.fintypeQ VPA.fintypeΓ

namespace VPA

/-- Single-letter transition relation of a VPA. -/
def Step {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind) (a : Alph) :
    (M.Q × List M.Γ) → (M.Q × List M.Γ) → Prop
  | (q, σ), (q', σ') =>
    match kind a with
    | .call => ∃ γ : M.Γ, σ' = γ :: σ ∧ M.δ_call q a q' γ
    | .intern => σ' = σ ∧ M.δ_intern q a q'
    | .ret =>
      match σ with
      | [] => σ' = [] ∧ M.δ_ret_empty q a q'
      | γ :: rest => σ' = rest ∧ M.δ_ret_nonempty q a γ q'

/-- Multi-step run of a VPA on a word `w ∈ Alph*`. -/
def Run {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind) :
    List Alph → (M.Q × List M.Γ) → (M.Q × List M.Γ) → Prop
  | [], c, c' => c = c'
  | a :: w, c, c' => ∃ c₁, M.Step a c c₁ ∧ M.Run w c₁ c'

lemma run_append {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind)
    (u v : List Alph) (c₀ c₂ : M.Q × List M.Γ) :
    M.Run (u ++ v) c₀ c₂ ↔ ∃ c₁, M.Run u c₀ c₁ ∧ M.Run v c₁ c₂ := by
  induction u generalizing c₀ with
  | nil =>
    simp [Run]
  | cons a u ih =>
    constructor
    · rintro ⟨c', hstep, hrun⟩
      rcases (ih c').mp hrun with ⟨c₁, hu, hv⟩
      exact ⟨c₁, ⟨c', hstep, hu⟩, hv⟩
    · rintro ⟨c₁, ⟨c', hstep, hu⟩, hv⟩
      exact ⟨c', hstep, (ih c').mpr ⟨c₁, hu, hv⟩⟩

/-- Acceptance of a word `w ∈ Alph*` from `(q₀, ⊥)` (`q₀ ∈ Q_0`) to `(qf, σ)` (`qf ∈ F`). -/
def Accepts {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind) (w : List Alph) : Prop :=
  ∃ q₀ ∈ M.start, ∃ qf ∈ M.accept, ∃ σ : List M.Γ, M.Run w (q₀, []) (qf, σ)

end VPA

/-- A language `L ⊆ Alph*` is visibly pushdown (`VPL`) if it is accepted by some VPA for some
partition `Alph = Σ_c ⊔ Σ_i ⊔ Σ_r`. -/
def IsVPL {Alph : Type*} (L : Set (List Alph)) : Prop :=
  ∃ (kind : Alph → LetterKind) (M : VPA Alph kind), ∀ w : List Alph, w ∈ L ↔ M.Accepts w

/-- `S ∈ REG^∀(G)` relative to a generating alphabet `gen : Alph → G`: `π⁻¹(S) ∈ REG`. -/
def IsREGForall {Alph G : Type*} [Monoid G] (gen : Alph → G) (S : Set G) : Prop :=
  IsRegular (evalWord gen ⁻¹' S)

/-- `S ∈ VPL^∀(G)` relative to a generating alphabet `gen : Alph → G`: `π⁻¹(S) ∈ VPL`. -/
def IsVPLForall {Alph G : Type*} [Monoid G] (gen : Alph → G) (S : Set G) : Prop :=
  IsVPL (evalWord gen ⁻¹' S)

/-- Intrinsic group-theoretic recognisability: `S` is a union of cosets of a finite-index
normal subgroup `N ⊴ G` (Proposition 4 of `arXiv:2604.22375v1`). -/
def IsRecognisable {G : Type*} [Group G] (S : Set G) : Prop :=
  ∃ N : Subgroup G, N.Normal ∧ N.FiniteIndex ∧ ∀ n ∈ N, ∀ s ∈ S, n * s ∈ S

/-! ## Section 2: Easy Direction (`REG^∀ ⊆ VPL^∀`) -/

/-- Every regular language is visibly pushdown (with `Σ_i = Σ`, `Σ_c = Σ_r = ∅`). -/
theorem isRegular_imp_isVPL {Alph : Type*} {L : Set (List Alph)} (h : IsRegular L) : IsVPL L := by
  rcases h with ⟨D, hD⟩
  let kind : Alph → LetterKind := fun _ => .intern
  let M : VPA Alph kind :=
    { Q := D.Q
      Γ := Unit
      start := {D.start}
      accept := D.accept
      δ_call := fun _ _ _ _ => False
      δ_intern := fun q a q' => q' = D.step q a
      δ_ret_nonempty := fun _ _ _ _ => False
      δ_ret_empty := fun _ _ _ => False }
  have hrunU : ∀ (w : List Alph) (q q' : D.Q) (σ σ' : List Unit),
      M.Run w (q, σ) (q', σ') ↔ q' = D.evalFrom q w ∧ σ' = σ := by
    intro w
    induction w with
    | nil =>
      intro q q' σ σ'; simp [VPA.Run, DetFA.evalFrom, eq_comm]
    | cons a w ih =>
      intro q q' σ σ'
      constructor
      · rintro ⟨⟨q₁, σ₁⟩, ⟨hσ, hq⟩, htail⟩
        subst hσ; subst hq
        exact (ih (D.step q a) q' σ₁ σ').mp htail
      · rintro ⟨rfl, rfl⟩
        exact ⟨(D.step q a, σ'), ⟨rfl, rfl⟩, (ih (D.step q a) _ σ' σ').mpr ⟨rfl, rfl⟩⟩
  refine ⟨kind, M, fun w => ?_⟩
  rw [hD w, DetFA.Accepts, VPA.Accepts]
  constructor
  · intro hacc
    exact ⟨D.start, rfl, D.evalFrom D.start w, hacc, [], (hrunU w _ _ [] []).mpr ⟨rfl, rfl⟩⟩
  · rintro ⟨q₀, hq₀, qf, hqf, σ, hr⟩
    rw [Set.mem_singleton_iff] at hq₀
    subst hq₀
    rcases (hrunU w _ _ [] σ).mp hr with ⟨rfl, _⟩
    exact hqf

/-! ## Section 3: Left-Stabilizer Subgroup and Reduction to Finite Index -/

/-- The left-stabilizer subgroup `H = Stab_L(S) = {h ∈ G | h S = S}`. -/
def stabL {G : Type*} [Group G] (S : Set G) : Subgroup G where
  carrier := {h : G | ∀ g : G, h * g ∈ S ↔ g ∈ S}
  mul_mem' := fun {a b} ha hb g => by rw [mul_assoc, ha, hb]
  one_mem' := fun g => by simp
  inv_mem' := fun {a} ha g => by
    have h := ha (a⁻¹ * g)
    simpa [mul_assoc] using h.symm

/-- If `Stab_L(S)` has finite index in `G`, then `S` is recognisable (invariant under a
finite-index normal subgroup `N ⊴ G`, namely the kernel of the left action on `G ⧸ Stab_L(S)`). -/
lemma recognisable_of_finiteIndex_stabL {G : Type*} [Group G] {S : Set G}
    (hfin : (stabL S).FiniteIndex) : IsRecognisable S := by
  let H := stabL S
  have : Finite (G ⧸ H) := Subgroup.finite_quotient_of_finiteIndex
  let φ : G →* Equiv.Perm (G ⧸ H) := MulAction.toPermHom G (G ⧸ H)
  let N := φ.ker
  have hN_norm : N.Normal := φ.normal_ker
  have hN_le : N ≤ H := by
    intro g hg
    have hact := Equiv.ext_iff.mp hg ((1 : G) : G ⧸ H)
    have hact' : ((g * 1 : G) : G ⧸ H) = ((1 : G) : G ⧸ H) := hact
    rw [mul_one, QuotientGroup.eq] at hact'
    exact H.inv_mem_iff.mp (by simpa using hact')
  have hN_fin : N.FiniteIndex := by
    have : Finite ((G ⧸ H) → (G ⧸ H)) := inferInstance
    have : Finite (Equiv.Perm (G ⧸ H)) :=
      Finite.of_injective (fun e : Equiv.Perm (G ⧸ H) => (e : (G ⧸ H) → (G ⧸ H)))
        DFunLike.coe_injective
    have hinj : Function.Injective (QuotientGroup.kerLift φ) :=
      QuotientGroup.kerLift_injective φ
    have : Finite (G ⧸ N) := Finite.of_injective _ hinj
    exact Subgroup.finiteIndex_of_finite_quotient
  refine ⟨N, hN_norm, hN_fin, fun n hn s hs => (hN_le hn s).mpr hs⟩

/-- Any recognisable subset `S ⊆ G` has regular preimage `π⁻¹(S)` under every monoid
homomorphism `evalWord gen : Alph* → G`. -/
theorem isREGForall_of_recognisable {Alph G : Type*} [Group G] (gen : Alph → G) {S : Set G}
    (hrec : IsRecognisable S) : IsREGForall gen S := by
  rcases hrec with ⟨N, hN_norm, hN_fin, hN_inv⟩
  have : N.Normal := hN_norm
  have : N.FiniteIndex := hN_fin
  have : Finite (G ⧸ N) := Subgroup.finite_quotient_of_finiteIndex
  let e : (G ⧸ N) ≃ Fin (Nat.card (G ⧸ N)) := Finite.equivFin (G ⧸ N)
  let D : DetFA Alph :=
    { Q := Fin (Nat.card (G ⧸ N))
      start := e (1 : G ⧸ N)
      step := fun q a => e (e.symm q * (gen a : G ⧸ N))
      accept := {q | ∃ s ∈ S, e (s : G ⧸ N) = q} }
  have heval : ∀ (w : List Alph) (x : G ⧸ N),
      D.evalFrom (e x) w = e (x * QuotientGroup.mk (s := N) (evalWord gen w)) := by
    intro w
    induction w with
    | nil =>
      intro x
      simp [DetFA.evalFrom, evalWord_nil, QuotientGroup.mk_one]
    | cons a w ih =>
      intro x
      simp only [DetFA.evalFrom, evalWord_cons, QuotientGroup.mk_mul]
      change D.evalFrom (e (e.symm (e x) * (gen a : G ⧸ N))) w = _
      rw [e.symm_apply_apply, ih, mul_assoc]
  refine ⟨D, fun w => ?_⟩
  rw [Set.mem_preimage, DetFA.Accepts]
  have hstart : D.evalFrom D.start w = e (QuotientGroup.mk (s := N) (evalWord gen w)) := by
    simpa [D] using heval w 1
  rw [hstart]
  constructor
  · intro hw
    exact ⟨evalWord gen w, hw, rfl⟩
  · rintro ⟨s, hs, heq⟩
    have hq : (s : G ⧸ N) = QuotientGroup.mk (s := N) (evalWord gen w) := e.injective heq
    rw [QuotientGroup.eq] at hq
    have hns : evalWord gen w * s⁻¹ ∈ N := by
      have hconj := hN_norm.conj_mem (s⁻¹ * evalWord gen w) hq s
      simpa [mul_assoc] using hconj
    have hmul := hN_inv (evalWord gen w * s⁻¹) hns s hs
    simpa [mul_assoc] using hmul

/-! ## Section 4: Case 1 (`Σ_r = ∅`) — Stack-Oblivious Projection -/

private lemma run_ignore_stack_of_no_ret {Alph : Type*} {kind : Alph → LetterKind}
    (M : VPA Alph kind) (hnoret : ∀ a : Alph, kind a ≠ .ret)
    (w : List Alph) (q q' : M.Q) (σ₁ σ₂ σ₁' : List M.Γ) :
    M.Run w (q, σ₁) (q', σ₁') → ∃ σ₂', M.Run w (q, σ₂) (q', σ₂') := by
  induction w generalizing q σ₁ σ₂ with
  | nil =>
    intro h
    simp only [VPA.Run, Prod.mk.injEq] at h
    exact ⟨σ₂, by simp [VPA.Run, h.1]⟩
  | cons a w ih =>
    rintro ⟨⟨qm, σm⟩, hstep, htail⟩
    cases hka : kind a with
    | call =>
      simp only [VPA.Step, hka] at hstep
      rcases hstep with ⟨γ, hσ, hδ⟩
      subst hσ
      obtain ⟨σ₂', hrun'⟩ := ih qm (γ :: σ₁) (γ :: σ₂) htail
      exact ⟨σ₂', ⟨(qm, γ :: σ₂), by simp [VPA.Step, hka]; exact hδ, hrun'⟩⟩
    | intern =>
      simp only [VPA.Step, hka] at hstep
      rcases hstep with ⟨hσ, hδ⟩
      subst hσ
      obtain ⟨σ₂', hrun'⟩ := ih qm σm σ₂ htail
      exact ⟨σ₂', ⟨(qm, σ₂), by simp [VPA.Step, hka, hδ], hrun'⟩⟩
    | ret =>
      exact absurd hka (hnoret a)

private lemma finiteIndex_stabL_case1 {Alph G : Type*} [Group G] (gen : Alph → G)
    (hsurj : Function.Surjective (evalWord gen)) {S : Set G}
    {kind : Alph → LetterKind} (M : VPA Alph kind)
    (hM : ∀ w : List Alph, evalWord gen w ∈ S ↔ M.Accepts w)
    (hnoret : ∀ a : Alph, kind a ≠ .ret) : (stabL S).FiniteIndex := by
  let H := stabL S
  let reach (u : List Alph) : Set M.Q :=
    {q : M.Q | ∃ q₀ ∈ M.start, ∃ σ : List M.Γ, M.Run u (q₀, []) (q, σ)}
  have hreach_eq : ∀ u₁ u₂ : List Alph, reach u₁ = reach u₂ →
      QuotientGroup.mk (s := H) (evalWord gen u₁)⁻¹ =
      QuotientGroup.mk (s := H) (evalWord gen u₂)⁻¹ := by
    intro u₁ u₂ heq
    rw [QuotientGroup.eq]
    rw [inv_inv]
    intro g
    obtain ⟨v, hv⟩ := hsurj ((evalWord gen u₂)⁻¹ * g)
    have h1 : evalWord gen (u₁ ++ v) = evalWord gen u₁ * (evalWord gen u₂)⁻¹ * g := by
      rw [evalWord_append, hv, mul_assoc]
    have h2 : evalWord gen (u₂ ++ v) = g := by
      rw [evalWord_append, hv, mul_inv_cancel_left]
    rw [← h1, ← h2, hM (u₁ ++ v), hM (u₂ ++ v)]
    have hacc_iff : ∀ u : List Alph, M.Accepts (u ++ v) ↔
        ∃ q ∈ reach u, ∃ qf ∈ M.accept, ∃ σ : List M.Γ, M.Run v (q, []) (qf, σ) := by
      intro u
      constructor
      · rintro ⟨q₀, hq₀, qf, hqf, σf, hr⟩
        rcases (M.run_append u v (q₀, []) (qf, σf)).mp hr with ⟨⟨qm, σm⟩, hru, hrv⟩
        obtain ⟨σ', hrv'⟩ := run_ignore_stack_of_no_ret M hnoret v qm qf σm [] σf hrv
        exact ⟨qm, ⟨q₀, hq₀, σm, hru⟩, qf, hqf, σ', hrv'⟩
      · rintro ⟨qm, ⟨q₀, hq₀, σm, hru⟩, qf, hqf, σ', hrv'⟩
        obtain ⟨σf, hrv⟩ := run_ignore_stack_of_no_ret M hnoret v qm qf [] σm σ' hrv'
        exact ⟨q₀, hq₀, qf, hqf, σf, (M.run_append u v (q₀, []) (qf, σf)).mpr ⟨(qm, σm), hru, hrv⟩⟩
    rw [hacc_iff u₁, hacc_iff u₂, heq]
  -- Map each coset `c : G ⧸ H` to `reach u` for a chosen word `u` with `c = (evalWord gen u)⁻¹`.
  have hsurj_coset : ∀ c : G ⧸ H, ∃ u : List Alph, c = QuotientGroup.mk (s := H) (evalWord gen u)⁻¹ := by
    intro c
    induction c using QuotientGroup.induction_on with
    | H x =>
      obtain ⟨u, hu⟩ := hsurj x⁻¹
      exact ⟨u, by rw [hu, inv_inv]⟩
  let f : (G ⧸ H) → Set M.Q := fun c => reach (Classical.choose (hsurj_coset c))
  have hf_inj : Function.Injective f := by
    intro c₁ c₂ hfeq
    have hc₁ := Classical.choose_spec (hsurj_coset c₁)
    have hc₂ := Classical.choose_spec (hsurj_coset c₂)
    rw [hc₁, hc₂]
    exact hreach_eq _ _ hfeq
  have : Finite (Set M.Q) := Finite.of_fintype _
  have : Finite (G ⧸ H) := Finite.of_injective f hf_inj
  exact Subgroup.finiteIndex_of_finite_quotient

/-! ## Section 5: Case 2 (`Σ_r ≠ ∅`) — Matched-Call Submonoid `MC(Alph)` -/

/-- Number of call letters (`Σ_c`) in a word `w`. -/
def countCall {Alph : Type*} (kind : Alph → LetterKind) : List Alph → ℕ
  | [] => 0
  | a :: w => (if kind a = .call then 1 else 0) + countCall kind w

/-- Number of return letters (`Σ_r`) in a word `w`. -/
def countRet {Alph : Type*} (kind : Alph → LetterKind) : List Alph → ℕ
  | [] => 0
  | a :: w => (if kind a = .ret then 1 else 0) + countRet kind w

lemma countCall_append {Alph : Type*} (kind : Alph → LetterKind) (u v : List Alph) :
    countCall kind (u ++ v) = countCall kind u + countCall kind v := by
  induction u with
  | nil => simp [countCall]
  | cons a u ih => simp [countCall, ih, add_assoc]

lemma countRet_append {Alph : Type*} (kind : Alph → LetterKind) (u v : List Alph) :
    countRet kind (u ++ v) = countRet kind u + countRet kind v := by
  induction u with
  | nil => simp [countRet]
  | cons a u ih => simp [countRet, ih, add_assoc]

/-- The matched-call (non-positive-suffix) sublanguage `MC(Alph)`:
every suffix `s` of `w` satisfies `#_c(s) ≤ #_r(s)`. -/
def InMC {Alph : Type*} (kind : Alph → LetterKind) (w : List Alph) : Prop :=
  ∀ u s : List Alph, w = u ++ s → countCall kind s ≤ countRet kind s

/-- Lemma 1(1): `[] ∈ MC(Alph)`. -/
lemma inMC_nil {Alph : Type*} (kind : Alph → LetterKind) : InMC kind [] := by
  intro u s h
  have hs : s = [] := (List.append_eq_nil_iff.mp h.symm).2
  subst hs
  simp [countCall, countRet]

/-- Lemma 1(1): `MC(Alph)` is closed under concatenation. -/
lemma inMC_append {Alph : Type*} (kind : Alph → LetterKind) {u v : List Alph}
    (hu : InMC kind u) (hv : InMC kind v) : InMC kind (u ++ v) := by
  intro p s h
  rcases List.append_eq_append_iff.mp h.symm with ⟨t, hp, hs⟩ | ⟨t, hu_eq, hv_eq⟩
  · -- `u = p ++ t` and `s = t ++ v`
    rw [hs, countCall_append, countRet_append]
    have h1 := hu p t hp
    have h2 := hv [] v rfl
    omega
  · -- `p = u ++ t` and `v = t ++ s`
    exact hv t s hv_eq

/-- Lemma 1(2): every return letter lies in `MC(Alph)`. -/
lemma inMC_ret {Alph : Type*} (kind : Alph → LetterKind) {a : Alph} (ha : kind a = .ret) :
    InMC kind [a] := by
  intro u s h
  cases u with
  | nil =>
    simp only [List.nil_append] at h
    subst h
    simp [countCall, countRet, ha]
  | cons b u' =>
    simp only [List.cons_append, List.cons.injEq] at h
    have hs : s = [] := (List.append_eq_nil_iff.mp h.2.symm).2
    subst hs
    simp [countCall, countRet]

/-- Lemma 1(2): every internal letter lies in `MC(Alph)`. -/
lemma inMC_intern {Alph : Type*} (kind : Alph → LetterKind) {a : Alph} (ha : kind a = .intern) :
    InMC kind [a] := by
  intro u s h
  cases u with
  | nil =>
    simp only [List.nil_append] at h
    subst h
    simp [countCall, countRet, ha]
  | cons b u' =>
    simp only [List.cons_append, List.cons.injEq] at h
    have hs : s = [] := (List.append_eq_nil_iff.mp h.2.symm).2
    subst hs
    simp [countCall, countRet]

/-- Lemma 1(2): every call-return pair `[a, b]` (`a ∈ Σ_c`, `b ∈ Σ_r`) lies in `MC(Alph)`. -/
lemma inMC_call_ret {Alph : Type*} (kind : Alph → LetterKind) {a b : Alph}
    (ha : kind a = .call) (hb : kind b = .ret) : InMC kind [a, b] := by
  intro u s h
  cases u with
  | nil =>
    simp only [List.nil_append] at h
    subst h
    simp [countCall, countRet, ha, hb]
  | cons x u' =>
    cases u' with
    | nil =>
      simp only [List.cons_append, List.nil_append, List.cons.injEq] at h
      rw [← h.2]
      simp [countCall, countRet, hb]
    | cons y u'' =>
      simp only [List.cons_append, List.cons.injEq] at h
      have hs : s = [] := (List.append_eq_nil_iff.mp h.2.2.symm).2
      subst hs
      simp [countCall, countRet]

/-- Stack-height suffix bound for every VPA run: either the stack never hits empty on a return
letter (giving `|σ₁| + #_r(w) ≤ |σ₀| + #_c(w)`), or some suffix `s` starts after an empty-stack
return step (giving `|σ₁| + #_r(s) ≤ #_c(s)`). -/
private lemma vpa_run_stack_bound {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind)
    (w : List Alph) (q₀ q₁ : M.Q) (σ₀ σ₁ : List M.Γ) :
    M.Run w (q₀, σ₀) (q₁, σ₁) →
      (σ₁.length + countRet kind w ≤ σ₀.length + countCall kind w) ∨
      (∃ u s : List Alph, w = u ++ s ∧ σ₁.length + countRet kind s ≤ countCall kind s) := by
  induction w generalizing q₀ σ₀ with
  | nil =>
    intro h
    simp only [VPA.Run, Prod.mk.injEq] at h
    left
    simp [countCall, countRet, h.2]
  | cons a w ih =>
    rintro ⟨⟨qm, σm⟩, hstep, htail⟩
    rcases ih qm σm htail with h1 | ⟨u, s, hw, hs⟩
    · cases hka : kind a with
      | call =>
        simp only [VPA.Step, hka] at hstep
        rcases hstep with ⟨γ, rfl, _⟩
        left
        simp only [List.length_cons, countCall, countRet, hka, ↓reduceIte, reduceCtorEq] at h1 ⊢
        omega
      | intern =>
        simp only [VPA.Step, hka] at hstep
        rcases hstep with ⟨rfl, _⟩
        left
        simp only [countCall, countRet, hka, ↓reduceIte, reduceCtorEq] at h1 ⊢
        omega
      | ret =>
        cases σ₀ with
        | nil =>
          simp only [VPA.Step, hka] at hstep
          rcases hstep with ⟨rfl, _⟩
          right
          refine ⟨[a], w, rfl, ?_⟩
          simpa using h1
        | cons γ rest =>
          simp only [VPA.Step, hka] at hstep
          rcases hstep with ⟨rfl, _⟩
          left
          simp only [List.length_cons, countCall, countRet, hka, ↓reduceIte, reduceCtorEq] at h1 ⊢
          omega
    · right
      exact ⟨a :: u, s, by simp [hw], hs⟩

/-- **Lemma 2(1) (Empty stack on `MC(Alph)`):** every valid run of a VPA on any word `u ∈ MC(Alph)`
starting with empty stack `[]` (`⊥`) terminates with empty stack `[]` (`⊥`). -/
theorem vpa_empty_stack_on_mc {Alph : Type*} {kind : Alph → LetterKind} (M : VPA Alph kind)
    {u : List Alph} (hu : InMC kind u) {q₀ q₁ : M.Q} {σ : List M.Γ}
    (hrun : M.Run u (q₀, []) (q₁, σ)) : σ = [] := by
  have hlen : σ.length = 0 := by
    rcases vpa_run_stack_bound M u q₀ q₁ [] σ hrun with h1 | ⟨p, s, hp, hs⟩
    · have hmc := hu [] u rfl
      simp only [List.length_nil, zero_add] at h1
      omega
    · have hmc := hu p s hp
      omega
  exact List.eq_nil_of_length_eq_zero hlen

private lemma finiteIndex_stabL_case2 {Alph G : Type*} [Group G] (gen : Alph → G)
    (hsurj : Function.Surjective (evalWord gen)) {S : Set G}
    {kind : Alph → LetterKind} (M : VPA Alph kind)
    (hM : ∀ w : List Alph, evalWord gen w ∈ S ↔ M.Accepts w)
    (hret : ∃ y₀ : Alph, kind y₀ = .ret) : (stabL S).FiniteIndex := by
  let H := stabL S
  let Mmc : Set G := {g : G | ∃ u : List Alph, InMC kind u ∧ evalWord gen u = g}
  -- Lemma 1(1): `1 ∈ Mmc` and `Mmc` is closed under multiplication.
  have h1_mem : (1 : G) ∈ Mmc := ⟨[], inMC_nil kind, evalWord_nil gen⟩
  have hmul_mem : ∀ {x y : G}, x ∈ Mmc → y ∈ Mmc → x * y ∈ Mmc := by
    rintro x y ⟨u, hu, rfl⟩ ⟨v, hv, rfl⟩
    exact ⟨u ++ v, inMC_append kind hu hv, evalWord_append gen u v⟩
  -- Lemma 1(2): `Mmc` generates `G` as a group.
  have hgen_grp : Subgroup.closure Mmc = ⊤ := by
    rcases hret with ⟨y₀, hy₀⟩
    have hy₀_mem : gen y₀ ∈ Subgroup.closure Mmc :=
      Subgroup.subset_closure ⟨[y₀], inMC_ret kind hy₀, evalWord_singleton gen y₀⟩
    have hgen_mem : ∀ a : Alph, gen a ∈ Subgroup.closure Mmc := by
      intro a
      cases hka : kind a with
      | ret =>
        exact Subgroup.subset_closure ⟨[a], inMC_ret kind hka, evalWord_singleton gen a⟩
      | intern =>
        exact Subgroup.subset_closure ⟨[a], inMC_intern kind hka, evalWord_singleton gen a⟩
      | call =>
        have hpair : gen a * gen y₀ ∈ Subgroup.closure Mmc :=
          Subgroup.subset_closure
            ⟨[a, y₀], inMC_call_ret kind hka hy₀, by simp [evalWord]⟩
        have hmul := Subgroup.mul_mem _ hpair (Subgroup.inv_mem _ hy₀_mem)
        simpa [mul_assoc] using hmul
    rw [eq_top_iff]
    intro g _
    obtain ⟨w, rfl⟩ := hsurj g
    induction w with
    | nil =>
      rw [evalWord_nil]
      exact Subgroup.one_mem _
    | cons a w ih =>
      rw [evalWord_cons]
      exact Subgroup.mul_mem _ (hgen_mem a) (ih trivial)
  -- Lemma 2(2)-(3): Reachable state set `R(u) ⊆ Q` determines the coset `((π u)⁻¹ : G ⧸ H)`.
  let reach (u : List Alph) : Set M.Q :=
    {q : M.Q | ∃ q₀ ∈ M.start, M.Run u (q₀, []) (q, [])}
  have hreach_coset : ∀ {u₁ u₂ : List Alph}, InMC kind u₁ → InMC kind u₂ →
      reach u₁ = reach u₂ →
      QuotientGroup.mk (s := H) (evalWord gen u₁)⁻¹ =
      QuotientGroup.mk (s := H) (evalWord gen u₂)⁻¹ := by
    intro u₁ u₂ hu₁ hu₂ heq
    rw [QuotientGroup.eq]
    rw [inv_inv]
    intro g
    obtain ⟨v, hv⟩ := hsurj ((evalWord gen u₂)⁻¹ * g)
    have h1 : evalWord gen (u₁ ++ v) = evalWord gen u₁ * (evalWord gen u₂)⁻¹ * g := by
      rw [evalWord_append, hv, mul_assoc]
    have h2 : evalWord gen (u₂ ++ v) = g := by
      rw [evalWord_append, hv, mul_inv_cancel_left]
    rw [← h1, ← h2, hM (u₁ ++ v), hM (u₂ ++ v)]
    have hacc_iff : ∀ u : List Alph, InMC kind u → (M.Accepts (u ++ v) ↔
        ∃ q ∈ reach u, ∃ qf ∈ M.accept, ∃ σ : List M.Γ, M.Run v (q, []) (qf, σ)) := by
      intro u hu
      constructor
      · rintro ⟨q₀, hq₀, qf, hqf, σf, hr⟩
        rcases (M.run_append u v (q₀, []) (qf, σf)).mp hr with ⟨⟨qm, σm⟩, hru, hrv⟩
        have hσm : σm = [] := vpa_empty_stack_on_mc M hu hru
        subst hσm
        exact ⟨qm, ⟨q₀, hq₀, hru⟩, qf, hqf, σf, hrv⟩
      · rintro ⟨qm, ⟨q₀, hq₀, hru⟩, qf, hqf, σf, hrv⟩
        exact ⟨q₀, hq₀, qf, hqf, σf, (M.run_append u v (q₀, []) (qf, σf)).mpr ⟨(qm, []), hru, hrv⟩⟩
    rw [hacc_iff u₁ hu₁, hacc_iff u₂ hu₂, heq]
  -- Lemma 3: `Ω = { ((m⁻¹ : G) : G ⧸ H) | m ∈ Mmc }` is finite and invariant under `G`.
  let Ω : Set (G ⧸ H) := {c : G ⧸ H | ∃ m ∈ Mmc, c = ((m⁻¹ : G) : G ⧸ H)}
  have hΩ_fin : Ω.Finite := by
    have hΩ_sub : ∀ c : Ω, ∃ u : List Alph, InMC kind u ∧
        c.1 = QuotientGroup.mk (s := H) (evalWord gen u)⁻¹ := by
      rintro ⟨c, m, ⟨u, hu, rfl⟩, rfl⟩
      exact ⟨u, hu, rfl⟩
    let φ : Ω → Set M.Q := fun c => reach (Classical.choose (hΩ_sub c))
    have hφ_inj : Function.Injective φ := by
      intro c₁ c₂ hfeq
      apply Subtype.ext
      have hc₁ := Classical.choose_spec (hΩ_sub c₁)
      have hc₂ := Classical.choose_spec (hΩ_sub c₂)
      rw [hc₁.2, hc₂.2]
      exact hreach_coset hc₁.1 hc₂.1 hfeq
    have : Finite (Set M.Q) := Finite.of_fintype _
    have : Finite Ω := Finite.of_injective φ hφ_inj
    exact Set.toFinite Ω
  -- For every `m ∈ Mmc`, left multiplication by `m⁻¹` on `G ⧸ H` maps `Ω` into `Ω`, hence onto `Ω`.
  have hΩ_inv_Mmc : ∀ m ∈ Mmc, (fun c : G ⧸ H => m⁻¹ • c) '' Ω = Ω := by
    classical
    intro m hm
    have hmaps : Set.MapsTo (fun c : G ⧸ H => m⁻¹ • c) Ω Ω := by
      rintro c ⟨m', hm', rfl⟩
      refine ⟨m' * m, hmul_mem hm' hm, ?_⟩
      change ((m⁻¹ * m'⁻¹ : G) : G ⧸ H) = (((m' * m)⁻¹ : G) : G ⧸ H)
      rw [mul_inv_rev]
    have hsub : hΩ_fin.toFinset.image (fun c : G ⧸ H => m⁻¹ • c) ⊆ hΩ_fin.toFinset := by
      intro x hx
      rcases Finset.mem_image.mp hx with ⟨c, hc, rfl⟩
      rw [Set.Finite.mem_toFinset] at hc ⊢
      exact hmaps hc
    have heqF : hΩ_fin.toFinset.image (fun c : G ⧸ H => m⁻¹ • c) = hΩ_fin.toFinset := by
      refine Finset.eq_of_subset_of_card_le hsub ?_
      rw [Finset.card_image_of_injective _ (MulAction.injective m⁻¹)]
    ext x
    have hx := Finset.ext_iff.mp heqF x
    simpa [Set.Finite.mem_toFinset] using hx
  -- The stabilizer subgroup `K = {g ∈ G | (g⁻¹ • ·) '' Ω = Ω}` contains `Mmc`, so `K = G`.
  let K : Subgroup G :=
    { carrier := {g : G | (fun c : G ⧸ H => g⁻¹ • c) '' Ω = Ω}
      one_mem' := by simp
      mul_mem' := fun {a b} ha hb => by
        change (fun c : G ⧸ H => (a * b)⁻¹ • c) '' Ω = Ω
        have hcomp : (fun c : G ⧸ H => (a * b)⁻¹ • c) =
            (fun c => b⁻¹ • c) ∘ (fun c => a⁻¹ • c) := by
          ext c; simp [mul_inv_rev, mul_smul]
        rw [hcomp, Set.image_comp, ha, hb]
      inv_mem' := fun {a} ha => by
        change (fun c : G ⧸ H => a⁻¹⁻¹ • c) '' Ω = Ω
        change (fun c : G ⧸ H => a⁻¹ • c) '' Ω = Ω at ha
        rw [inv_inv]
        have hcomp : (fun c : G ⧸ H => a • c) '' ((fun c : G ⧸ H => a⁻¹ • c) '' Ω) = Ω := by
          rw [← Set.image_comp]
          have : (fun c : G ⧸ H => a • c) ∘ (fun c : G ⧸ H => a⁻¹ • c) = id := by
            ext c; simp [smul_smul]
          rw [this, Set.image_id]
        rwa [ha] at hcomp }
  have hK_top : K = ⊤ := by
    rw [eq_top_iff, ← hgen_grp, Subgroup.closure_le]
    intro m hm
    exact hΩ_inv_Mmc m hm
  have h1Ω : ((1 : G) : G ⧸ H) ∈ Ω := ⟨1, h1_mem, by simp⟩
  have hΩ_univ : Ω = Set.univ := by
    ext c
    simp only [Set.mem_univ, iff_true]
    induction c using QuotientGroup.induction_on with
    | H x =>
      have hxK : x⁻¹ ∈ K := by rw [hK_top]; trivial
      have hmem : (x⁻¹)⁻¹ • ((1 : G) : G ⧸ H) ∈ (fun c : G ⧸ H => (x⁻¹)⁻¹ • c) '' Ω :=
        Set.mem_image_of_mem _ h1Ω
      rw [hxK] at hmem
      have hxeq : (x⁻¹)⁻¹ • ((1 : G) : G ⧸ H) = (x : G ⧸ H) := by
        change (((x⁻¹)⁻¹ * 1 : G) : G ⧸ H) = (x : G ⧸ H)
        simp
      rwa [hxeq] at hmem
  have : Finite (G ⧸ H) := by
    rw [hΩ_univ] at hΩ_fin
    exact Set.finite_univ_iff.mp hΩ_fin
  exact Subgroup.finiteIndex_of_finite_quotient

/-! ## Section 6: Main Theorems (Conjecture 1 of Ciobanu–Turaev) -/

/-- For every finitely generated group `G` and every `S ∈ VPL^∀(G)`, the left-stabilizer
subgroup `Stab_L(S)` has finite index in `G`. -/
theorem vplForall_finiteIndex_stabL {Alph G : Type*} [Group G] (gen : Alph → G)
    (hsurj : Function.Surjective (evalWord gen)) {S : Set G}
    (hvpl : IsVPLForall gen S) : (stabL S).FiniteIndex := by
  rcases hvpl with ⟨kind, M, hM⟩
  by_cases hret : ∃ y₀ : Alph, kind y₀ = .ret
  · exact finiteIndex_stabL_case2 gen hsurj M hM hret
  · push Not at hret
    exact finiteIndex_stabL_case1 gen hsurj M hM hret

/-- **Main Theorem (Ciobanu–Turaev, `arXiv:2604.22375v1`, Section 3.1, Conjecture 1):**
In every finitely generated group `G` (for any finite monoid generating alphabet `Alph` with
surjective `π : Alph* → G`), a subset `S ⊆ G` belongs to `VPL^∀(G)` if and only if it belongs
to `REG^∀(G)` (and equivalently if and only if `S` is recognisable). -/
theorem ciobanu_turaev_conjecture_1 {Alph G : Type*} [Group G] (gen : Alph → G)
    (hsurj : Function.Surjective (evalWord gen)) (S : Set G) :
    IsVPLForall gen S ↔ IsREGForall gen S := by
  constructor
  · intro hvpl
    exact isREGForall_of_recognisable gen
      (recognisable_of_finiteIndex_stabL (vplForall_finiteIndex_stabL gen hsurj hvpl))
  · intro hreg
    exact isRegular_imp_isVPL hreg

/-- Equivalence of `VPL^∀(G)`, `REG^∀(G)`, and intrinsic recognisability. -/
theorem vplForall_iff_recognisable {Alph G : Type*} [Group G] (gen : Alph → G)
    (hsurj : Function.Surjective (evalWord gen)) (S : Set G) :
    IsVPLForall gen S ↔ IsRecognisable S := by
  constructor
  · intro hvpl
    exact recognisable_of_finiteIndex_stabL (vplForall_finiteIndex_stabL gen hsurj hvpl)
  · intro hrec
    exact isRegular_imp_isVPL (isREGForall_of_recognisable gen hrec)

/-- Symmetric generating-set map `Σ = X ⊔ X` sending `inl x ↦ f x` and `inr x ↦ (f x)⁻¹`. -/
def symGen {X G : Type*} [Group G] (f : X → G) : X ⊕ X → G :=
  Sum.elim f (fun x => (f x)⁻¹)

lemma evalWord_symGen_surjective {X G : Type*} [Group G] (f : X → G)
    (hgen : Subgroup.closure (Set.range f) = ⊤) :
    Function.Surjective (evalWord (symGen f)) := by
  have hrevInv : ∀ u : List (X ⊕ X),
      evalWord (symGen f) (u.map Sum.swap).reverse = (evalWord (symGen f) u)⁻¹ := by
    intro u
    induction u with
    | nil => simp [evalWord]
    | cons a l ih =>
      simp only [List.map_cons, List.reverse_cons, evalWord_append, evalWord_cons,
        mul_inv_rev, ih]
      cases a with
      | inl x => simp [symGen, evalWord]
      | inr x => simp [symGen, evalWord]
  intro g
  have hg : g ∈ Subgroup.closure (Set.range f) := by rw [hgen]; trivial
  refine Subgroup.closure_induction ?_ ?_ ?_ ?_ hg
  · rintro _ ⟨x, rfl⟩
    exact ⟨[Sum.inl x], by simp [evalWord, symGen]⟩
  · exact ⟨[], evalWord_nil _⟩
  · rintro x y _ _ ⟨u, rfl⟩ ⟨v, rfl⟩
    exact ⟨u ++ v, evalWord_append _ u v⟩
  · rintro x _ ⟨u, rfl⟩
    exact ⟨(u.map Sum.swap).reverse, hrevInv u⟩

/-- **Conjecture 1 for a finitely generated group `G = ⟨X⟩` with symmetric alphabet `Σ = X ∪ X⁻¹`.** -/
theorem ciobanu_turaev_conjecture_1_symGen {X G : Type*} [Group G] (f : X → G)
    (hgen : Subgroup.closure (Set.range f) = ⊤) (S : Set G) :
    IsVPLForall (symGen f) S ↔ IsREGForall (symGen f) S :=
  ciobanu_turaev_conjecture_1 (symGen f) (evalWord_symGen_surjective f hgen) S

#print axioms vpa_empty_stack_on_mc
#print axioms vplForall_finiteIndex_stabL
#print axioms ciobanu_turaev_conjecture_1
#print axioms vplForall_iff_recognisable
#print axioms ciobanu_turaev_conjecture_1_symGen

end OpenMath.Ciobanu260422375Conj1
