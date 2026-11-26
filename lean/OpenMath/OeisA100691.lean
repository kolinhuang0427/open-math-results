import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Data.List.Nodup
import Mathlib.SetTheory.Cardinal.Finite

/-!
# Resolution of R. J. Mathar's 2022 Conjecture on OEIS A100691 and A193641

Primary sources:
- OEIS **A100691** (rev 11, 2022-07-22):
  Name: *"Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."*
  Tabulated data (`a_OEIS(n)`): `1, 4, 12, 30, 70, 158, 352, 780, ...`
  Formula: `G.f.: (1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)]`,
  `a(n) = 2*a(n-1) + a(n-3) + 6` for `n >= 4`,
  `Conjecture: a(n) = A193641(n+2) - 3, n > 0` (R. J. Mathar, Jul 22 2022).
- OEIS **A193641** (rev 48, 2026-09-16):
  Name: *"Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."*
  Formula: `Empirical: a(n) = 2*a(n-1) + a(n-3)`.

We formalize BOTH parts of the resolution:
1. **Part 1 (Sequence / Recurrence Reading — TRUE for all `n ≥ 1`):**
   Directly from the combinatorial definition of `A193641(n)`, we prove via exact bijections
   on the 3-class partition `(U, V, W)` that:
   - `A193641 0 = 1`, `A193641 1 = 1`, `A193641 2 = 3`,
   - `A193641 (m + 3) = 2 * A193641 (m + 2) + A193641 m` for all `m : ℕ`,
   - `aOEIS n = A193641 (n + 2) - 3` for all `n ≥ 1` (where `aOEIS` is verified to match
     the generating function `(1+z^2)(1+z+z^2)/((1-z)(1-2z-z^3))` coefficient-for-coefficient).
2. **Part 2 (Combinatorial Definition Reading — FALSE at `n = 5`):**
   We define the triangular lattice strip graph `triStripGraph` on `ℤ × Fin 2` and the exact
   set of `n`-step self-avoiding paths `IsSAW n` starting at `(0, 0)`. We prove that for every
   `n : ℕ`, `sawCount n = (sawPaths n).length`, yielding `sawCount 0..5 = 1, 4, 12, 30, 70, 160`
   and the explicit refutation `sawCount 5 = 160 ≠ 158 = A193641 (5 + 2) - 3`.
-/

namespace OpenMath.OeisA100691

/-! ## Part 1: Combinatorial Proof of the Recurrence for `A193641` and `a_OEIS(n) = A193641(n+2) - 3` -/

/-- Integers in `{-1, 0, 1}`. -/
abbrev TriInt := {x : ℤ // x ∈ ({-1, 0, 1} : Finset ℤ)}

def triNeg : TriInt := ⟨-1, by decide⟩
def triZero : TriInt := ⟨0, by decide⟩
def triPos : TriInt := ⟨1, by decide⟩

lemma triInt_cases (a : TriInt) : a.val = -1 ∨ a.val = 0 ∨ a.val = 1 := by
  have h := a.property
  simp only [Finset.mem_insert, Finset.mem_singleton] at h
  exact h

def triNegate (a : TriInt) : TriInt :=
  ⟨-a.val, by
    rcases triInt_cases a with h | h | h <;> simp [h]⟩

@[simp] lemma triNegate_val (a : TriInt) : (triNegate a).val = -a.val := rfl

lemma triInt_eq_of_ne_zero_of_add_ne_zero {a b : TriInt}
    (ha : a.val ≠ 0) (hb : b.val ≠ 0) (hsum : a.val + b.val ≠ 0) : b = a := by
  apply Subtype.ext
  rcases triInt_cases a with ha' | ha' | ha' <;>
  rcases triInt_cases b with hb' | hb' | hb' <;> omega

lemma triInt_eq_negate_of_add_eq_zero {a b : TriInt} (hsum : a.val + b.val = 0) :
    b = triNegate a := by
  apply Subtype.ext
  change b.val = -a.val
  omega

/-- Position `i : Fin n` in `x : Fin n → ℤ` belongs to a contiguous subarray of length 1
(`x i = 0`) or length 2 (`x i + x (i+1) = 0` or `x (i-1) + x i = 0`) with sum zero. -/
def IsCovered {n : ℕ} (x : Fin n → ℤ) (i : Fin n) : Prop :=
  x i = 0 ∨
  (∃ h : i.val + 1 < n, x i + x ⟨i.val + 1, h⟩ = 0) ∨
  (∃ _ : 0 < i.val, x ⟨i.val - 1, by have := i.isLt; omega⟩ + x i = 0)

/-- An array `x : Fin n → {-1, 0, 1}` satisfies the defining condition of OEIS `A193641`:
every position `i` is in a contiguous length-1 or length-2 subarray with sum zero. -/
def IsValidA193641 {n : ℕ} (x : Fin n → TriInt) : Prop :=
  ∀ i : Fin n, IsCovered (fun j => (x j).val) i

/-- OEIS `A193641(n)`: number of valid arrays of length `n` over `{-1, 0, 1}`. -/
noncomputable def A193641 (n : ℕ) : ℕ :=
  Nat.card {x : Fin n → TriInt // IsValidA193641 x}

/-! ### Prefix Helpers (`snoc` and `init`) -/

def snocTri {n : ℕ} (x : Fin n → TriInt) (a : TriInt) : Fin (n + 1) → TriInt :=
  fun i => if h : i.val < n then x ⟨i.val, h⟩ else a

def initTri {n : ℕ} (x : Fin (n + 1) → TriInt) : Fin n → TriInt :=
  fun i => x ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩

lemma snocTri_lt {n : ℕ} (x : Fin n → TriInt) (a : TriInt) {i : Fin (n + 1)} (h : i.val < n) :
    snocTri x a i = x ⟨i.val, h⟩ := by
  simp [snocTri, h]

lemma snocTri_last {n : ℕ} (x : Fin n → TriInt) (a : TriInt) :
    snocTri x a ⟨n, Nat.lt_succ_self n⟩ = a := by
  simp [snocTri]

@[simp] lemma initTri_snocTri {n : ℕ} (x : Fin n → TriInt) (a : TriInt) :
    initTri (snocTri x a) = x := by
  funext i
  simp [initTri, snocTri, i.isLt]

lemma snocTri_initTri {n : ℕ} (x : Fin (n + 1) → TriInt) :
    snocTri (initTri x) (x ⟨n, Nat.lt_succ_self n⟩) = x := by
  funext i
  by_cases h : i.val < n
  · simp [snocTri, initTri, h]
  · have hi : i = ⟨n, Nat.lt_succ_self n⟩ := Fin.ext (by dsimp; have := i.isLt; omega)
    subst hi
    simp [snocTri]

/-! ### The Three-Class Partition `(U, V, W)` -/

/-- Every position `i < n - 1` is covered inside `x`. -/
def InitCovered {n : ℕ} (x : Fin n → TriInt) : Prop :=
  ∀ i : Fin n, i.val + 1 < n → IsCovered (fun j => (x j).val) i

/-- `U(n)`: valid arrays of length `n` that are empty (`n = 0`) or end in `0`. -/
def ClassU (n : ℕ) :=
  {x : Fin n → TriInt // IsValidA193641 x ∧ ∀ h : 0 < n, (x ⟨n - 1, by omega⟩).val = 0}

/-- `V(n)`: valid arrays of length `n` ending in `±1` (so `n > 0` and last entry is nonzero). -/
def ClassV (n : ℕ) :=
  {x : Fin n → TriInt // IsValidA193641 x ∧ ∃ _ : 0 < n, (x ⟨n - 1, by omega⟩).val ≠ 0}

/-- `W(n)`: arrays of length `n` with `0..n-2` covered inside `x`, but `n-1` NOT covered inside `x`. -/
def ClassW (n : ℕ) :=
  {x : Fin n → TriInt // InitCovered x ∧ ∃ _ : 0 < n, ¬ IsCovered (fun j => (x j).val) ⟨n - 1, by omega⟩}

noncomputable def countU (n : ℕ) : ℕ := Nat.card (ClassU n)
noncomputable def countV (n : ℕ) : ℕ := Nat.card (ClassV n)
noncomputable def countW (n : ℕ) : ℕ := Nat.card (ClassW n)

instance (n : ℕ) : Finite (ClassU n) := Subtype.finite
instance (n : ℕ) : Finite (ClassV n) := Subtype.finite
instance (n : ℕ) : Finite (ClassW n) := Subtype.finite
instance (n : ℕ) : Finite {x : Fin n → TriInt // IsValidA193641 x} := Subtype.finite

/-- Lifting coverage from `initTri x` to `x`. -/
lemma isCovered_lift {n : ℕ} {x : Fin (n + 1) → TriInt} {i : Fin n}
    (hcov : IsCovered (fun j => (initTri x j).val) i) :
    IsCovered (fun j => (x j).val) ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩ := by
  rcases hcov with h0 | ⟨hlt, hsum⟩ | ⟨hpos, hsum⟩
  · exact Or.inl h0
  · exact Or.inr (Or.inl ⟨Nat.lt_succ_of_lt hlt, hsum⟩)
  · exact Or.inr (Or.inr ⟨hpos, hsum⟩)

/-- Pushing coverage down from `x` to `initTri x` when `i + 1 < n`. -/
lemma isCovered_init_of_lt_pred {n : ℕ} {x : Fin (n + 1) → TriInt} {i : Fin n}
    (hlt : i.val + 1 < n) (hcov : IsCovered (fun j => (x j).val) ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩) :
    IsCovered (fun j => (initTri x j).val) i := by
  rcases hcov with h0 | ⟨_, hsum⟩ | ⟨hpos, hsum⟩
  · exact Or.inl h0
  · exact Or.inr (Or.inl ⟨hlt, hsum⟩)
  · exact Or.inr (Or.inr ⟨hpos, hsum⟩)

lemma initCovered_of_valid {n : ℕ} {x : Fin (n + 1) → TriInt}
    (hv : IsValidA193641 x) : InitCovered (initTri x) := by
  intro i hlt
  exact isCovered_init_of_lt_pred hlt (hv ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩)

/-- Partition identity: `A193641 n = U(n) + V(n)`. -/
def validEquivUSumV (n : ℕ) :
    {x : Fin n → TriInt // IsValidA193641 x} ≃ ClassU n ⊕ ClassV n where
  toFun x :=
    if h : 0 < n then
      if hz : (x.val ⟨n - 1, by omega⟩).val = 0 then
        Sum.inl ⟨x.val, x.property, fun _ => hz⟩
      else
        Sum.inr ⟨x.val, x.property, h, hz⟩
    else
      Sum.inl ⟨x.val, x.property, fun h' => absurd h' h⟩
  invFun
    | Sum.inl u => ⟨u.val, u.property.1⟩
    | Sum.inr v => ⟨v.val, v.property.1⟩
  left_inv x := by
    by_cases h : 0 < n
    · by_cases hz : (x.val ⟨n - 1, by omega⟩).val = 0 <;> simp [h, hz]
    · simp [h]
  right_inv s := by
    rcases s with u | v
    · dsimp only
      by_cases h : 0 < n
      · have hz := u.property.2 h
        simp only [h, hz, dite_true]
        rfl
      · simp only [h, dite_false]
        rfl
    · dsimp only
      obtain ⟨h, hz⟩ := v.property.2
      simp only [h, hz, dite_true, dite_false]
      rfl

lemma A193641_eq_U_add_V (n : ℕ) : A193641 n = countU n + countV n := by
  unfold A193641 countU countV
  rw [Nat.card_congr (validEquivUSumV n), Nat.card_sum]

/-- Transition 1: `U(n + 1) = A193641(n)`. -/
def classUSuccEquivValid (n : ℕ) :
    ClassU (n + 1) ≃ {x : Fin n → TriInt // IsValidA193641 x} where
  toFun u :=
    ⟨initTri u.val, by
      intro i
      have hiLt : i.val < n := i.isLt
      have hcov := u.property.1 ⟨i.val, Nat.lt_succ_of_lt hiLt⟩
      have hlast0 : (u.val ⟨n, Nat.lt_succ_self n⟩).val = 0 := u.property.2 (Nat.zero_lt_succ n)
      rcases hcov with h0 | ⟨hlt, hsum⟩ | ⟨hpos, hsum⟩
      · exact Or.inl h0
      · by_cases hin : i.val + 1 < n
        · exact Or.inr (Or.inl ⟨hin, hsum⟩)
        · have heq : (⟨i.val + 1, hlt⟩ : Fin (n + 1)) = ⟨n, Nat.lt_succ_self n⟩ :=
            Fin.ext (by dsimp; omega)
          have hsum' : (u.val ⟨i.val, Nat.lt_succ_of_lt hiLt⟩).val +
              (u.val ⟨i.val + 1, hlt⟩).val = 0 := hsum
          rw [heq, hlast0, add_zero] at hsum'
          exact Or.inl hsum'
      · exact Or.inr (Or.inr ⟨hpos, hsum⟩)⟩
  invFun x :=
    ⟨snocTri x.val triZero, by
      refine ⟨fun i => ?_, fun _ => by simp [snocTri_last, triZero]⟩
      by_cases hi : i.val < n
      · exact isCovered_lift (x := snocTri x.val triZero) (i := ⟨i.val, hi⟩) (by
          simpa [initTri_snocTri] using x.property ⟨i.val, hi⟩)
      · have hiLt : i.val < n + 1 := i.isLt
        have heq : i = ⟨n, Nat.lt_succ_self n⟩ := Fin.ext (by dsimp; omega)
        subst heq
        exact Or.inl (by simp [snocTri_last, triZero])⟩
  left_inv u := by
    apply Subtype.ext
    have hlast : u.val ⟨n, Nat.lt_succ_self n⟩ = triZero :=
      Subtype.ext (u.property.2 (Nat.zero_lt_succ n))
    conv_rhs => rw [← snocTri_initTri u.val, hlast]
  right_inv x := by
    apply Subtype.ext
    exact initTri_snocTri x.val triZero

lemma countU_succ (n : ℕ) : countU (n + 1) = A193641 n := by
  unfold countU A193641
  exact Nat.card_congr (classUSuccEquivValid n)

/-- Helper: if `x ∈ ClassW (n + 1)`, then `initTri x` is valid. -/
lemma valid_initTri_of_classW {n : ℕ} (w : ClassW (n + 1)) :
    IsValidA193641 (initTri w.val) := by
  intro i
  have hiLt : i.val < n := i.isLt
  have hcov := w.property.1 ⟨i.val, Nat.lt_succ_of_lt hiLt⟩ (by dsimp; omega)
  have hnotlast := w.property.2.2
  rcases hcov with h0 | ⟨hlt, hsum⟩ | ⟨hpos, hsum⟩
  · exact Or.inl h0
  · by_cases hin : i.val + 1 < n
    · exact Or.inr (Or.inl ⟨hin, hsum⟩)
    · exfalso
      apply hnotlast
      refine Or.inr (Or.inr ⟨by dsimp; omega, ?_⟩)
      have hidx1 : (⟨n - 1, by omega⟩ : Fin (n + 1)) = ⟨i.val, Nat.lt_succ_of_lt hiLt⟩ :=
        Fin.ext (by dsimp; omega)
      have hidx2 : (⟨n, Nat.lt_succ_self n⟩ : Fin (n + 1)) = ⟨i.val + 1, hlt⟩ :=
        Fin.ext (by dsimp; omega)
      change (w.val ⟨n - 1, by omega⟩).val + (w.val ⟨n, Nat.lt_succ_self n⟩).val = 0
      rw [hidx1, hidx2]
      exact hsum
  · exact Or.inr (Or.inr ⟨hpos, hsum⟩)

/-- Transition 2: `W(n + 1) = 2 * U(n) + V(n)`. -/
def classWSuccEquiv (n : ℕ) :
    ClassW (n + 1) ≃ (ClassU n × Bool) ⊕ ClassV n where
  toFun w :=
    let hv : IsValidA193641 (initTri w.val) := valid_initTri_of_classW w
    if h : 0 < n then
      if hz : (initTri w.val ⟨n - 1, by omega⟩).val = 0 then
        Sum.inl (⟨initTri w.val, hv, fun _ => hz⟩, decide ((w.val ⟨n, Nat.lt_succ_self n⟩).val = 1))
      else
        Sum.inr ⟨initTri w.val, hv, h, hz⟩
    else
      Sum.inl (⟨initTri w.val, hv, fun h' => absurd h' h⟩,
        decide ((w.val ⟨n, Nat.lt_succ_self n⟩).val = 1))
  invFun
    | Sum.inl (u, b) =>
      let a : TriInt := if b then triPos else triNeg
      ⟨snocTri u.val a, by
        refine ⟨fun i hi => ?_, Nat.zero_lt_succ n, ?_⟩
        · exact isCovered_lift (x := snocTri u.val a) (i := ⟨i.val, by omega⟩) (by
            simpa [initTri_snocTri] using u.property.1 ⟨i.val, by omega⟩)
        · rintro (h0 | ⟨hlt, _⟩ | ⟨hpos, hsum⟩)
          · change (snocTri u.val a ⟨n, Nat.lt_succ_self n⟩).val = 0 at h0
            rw [snocTri_last] at h0
            cases b <;> simp [a, triPos, triNeg] at h0
          · simp at hlt
          · have hpos' : 0 < n := hpos
            have hlt : n - 1 < n := by omega
            have h1 : snocTri u.val a ⟨n - 1, by omega⟩ = u.val ⟨n - 1, hlt⟩ :=
              snocTri_lt u.val a hlt
            have h2 : snocTri u.val a ⟨n, Nat.lt_succ_self n⟩ = a := snocTri_last u.val a
            change (snocTri u.val a ⟨n - 1, by omega⟩).val +
              (snocTri u.val a ⟨n, Nat.lt_succ_self n⟩).val = 0 at hsum
            rw [h1, h2, u.property.2 hpos', zero_add] at hsum
            cases b <;> simp [a, triPos, triNeg] at hsum⟩
    | Sum.inr v =>
      let hn : 0 < n := v.property.2.1
      let a : TriInt := v.val ⟨n - 1, by omega⟩
      ⟨snocTri v.val a, by
        refine ⟨fun i hi => ?_, Nat.zero_lt_succ n, ?_⟩
        · exact isCovered_lift (x := snocTri v.val a) (i := ⟨i.val, by omega⟩) (by
            simpa [initTri_snocTri] using v.property.1 ⟨i.val, by omega⟩)
        · rintro (h0 | ⟨hlt, _⟩ | ⟨_, hsum⟩)
          · change (snocTri v.val a ⟨n, Nat.lt_succ_self n⟩).val = 0 at h0
            rw [snocTri_last] at h0
            exact v.property.2.2 h0
          · simp at hlt
          · have hlt : n - 1 < n := by omega
            have h1 : snocTri v.val a ⟨n - 1, by omega⟩ = a := snocTri_lt v.val a hlt
            have h2 : snocTri v.val a ⟨n, Nat.lt_succ_self n⟩ = a := snocTri_last v.val a
            change (snocTri v.val a ⟨n - 1, by omega⟩).val +
              (snocTri v.val a ⟨n, Nat.lt_succ_self n⟩).val = 0 at hsum
            rw [h1, h2] at hsum
            have ha0 : a.val = 0 := by omega
            exact v.property.2.2 ha0⟩
  left_inv w := by
    apply Subtype.ext
    have hnotlast := w.property.2.2
    have hlast_ne0 : (w.val ⟨n, Nat.lt_succ_self n⟩).val ≠ 0 :=
      fun h0 => hnotlast (Or.inl h0)
    by_cases h : 0 < n
    · by_cases hz : (initTri w.val ⟨n - 1, by omega⟩).val = 0
      · simp only [h, hz, dite_true]
        have hlast_eq : (if decide ((w.val ⟨n, Nat.lt_succ_self n⟩).val = 1) then triPos else triNeg) =
            w.val ⟨n, Nat.lt_succ_self n⟩ := by
          apply Subtype.ext
          rcases triInt_cases (w.val ⟨n, Nat.lt_succ_self n⟩) with h1 | h1 | h1
          · simp [h1, triNeg]
          · exact absurd h1 hlast_ne0
          · simp [h1, triPos]
        rw [hlast_eq, snocTri_initTri]
      · simp only [h, hz, dite_true, dite_false]
        have hsum_ne0 : (initTri w.val ⟨n - 1, by omega⟩).val +
            (w.val ⟨n, Nat.lt_succ_self n⟩).val ≠ 0 := by
          intro hsum
          apply hnotlast
          exact Or.inr (Or.inr ⟨h, hsum⟩)
        have heq : w.val ⟨n, Nat.lt_succ_self n⟩ = initTri w.val ⟨n - 1, by omega⟩ :=
          triInt_eq_of_ne_zero_of_add_ne_zero hz hlast_ne0 hsum_ne0
        rw [← heq, snocTri_initTri]
    · simp only [h, dite_false]
      have hlast_eq : (if decide ((w.val ⟨n, Nat.lt_succ_self n⟩).val = 1) then triPos else triNeg) =
          w.val ⟨n, Nat.lt_succ_self n⟩ := by
        apply Subtype.ext
        rcases triInt_cases (w.val ⟨n, Nat.lt_succ_self n⟩) with h1 | h1 | h1
        · simp [h1, triNeg]
        · exact absurd h1 hlast_ne0
        · simp [h1, triPos]
      rw [hlast_eq, snocTri_initTri]
  right_inv s := by
    rcases s with ⟨u, b⟩ | v
    · dsimp only
      by_cases h : 0 < n
      · have hz : (initTri (snocTri u.val (if b then triPos else triNeg)) ⟨n - 1, by omega⟩).val = 0 := by
          rw [initTri_snocTri]; exact u.property.2 h
        simp only [h, hz, dite_true]
        apply congrArg Sum.inl
        apply Prod.ext
        · exact Subtype.ext (initTri_snocTri _ _)
        · cases b <;> simp [snocTri_last, triPos, triNeg]
      · simp only [h, dite_false]
        apply congrArg Sum.inl
        apply Prod.ext
        · exact Subtype.ext (initTri_snocTri _ _)
        · cases b <;> simp [snocTri_last, triPos, triNeg]
    · dsimp only
      obtain ⟨h, hz⟩ := v.property.2
      have hz' : (initTri (snocTri v.val (v.val ⟨n - 1, by omega⟩)) ⟨n - 1, by omega⟩).val ≠ 0 := by
        rw [initTri_snocTri]; exact hz
      simp only [h, hz', dite_true, dite_false]
      exact congrArg Sum.inr (Subtype.ext (initTri_snocTri _ _))

lemma countW_succ (n : ℕ) : countW (n + 1) = 2 * countU n + countV n := by
  unfold countW countU countV
  rw [Nat.card_congr (classWSuccEquiv n), Nat.card_sum, Nat.card_prod]
  simp only [Nat.card_eq_fintype_card, Fintype.card_bool]
  omega

/-- Transition 3: `V(n + 1) = V(n) + W(n)`. -/
noncomputable def classVSuccEquiv (n : ℕ) :
    ClassV (n + 1) ≃ ClassV n ⊕ ClassW n where
  toFun v :=
    have hcovn : IsCovered (fun j => (v.val j).val) ⟨n, Nat.lt_succ_self n⟩ :=
      v.property.1 ⟨n, Nat.lt_succ_self n⟩
    have hne0 : (v.val ⟨n, Nat.lt_succ_self n⟩).val ≠ 0 := v.property.2.2
    have hn_and_sum : ∃ h : 0 < n, (initTri v.val ⟨n - 1, by omega⟩).val +
        (v.val ⟨n, Nat.lt_succ_self n⟩).val = 0 := by
      rcases hcovn with h0 | ⟨hlt, _⟩ | ⟨hpos, hsum⟩
      · exact absurd h0 hne0
      · simp at hlt
      · exact ⟨hpos, hsum⟩
    have hn : 0 < n := hn_and_sum.1
    have hprev_ne0 : (initTri v.val ⟨n - 1, by omega⟩).val ≠ 0 := by
      have hsum := hn_and_sum.2
      omega
    have hinit : InitCovered (initTri v.val) := initCovered_of_valid v.property.1
    open Classical in
    if hlast : IsCovered (fun j => (initTri v.val j).val) ⟨n - 1, by omega⟩ then
      Sum.inl ⟨initTri v.val, fun i => by
        by_cases hi : i.val + 1 < n
        · exact hinit i hi
        · have hiLt : i.val < n := i.isLt
          have heq : i = ⟨n - 1, by omega⟩ := Fin.ext (by dsimp; omega)
          rw [heq]
          exact hlast, hn, hprev_ne0⟩
    else
      Sum.inr ⟨initTri v.val, hinit, hn, hlast⟩
  invFun
    | Sum.inl v =>
      let hn : 0 < n := v.property.2.1
      let a : TriInt := triNegate (v.val ⟨n - 1, by omega⟩)
      ⟨snocTri v.val a, by
        refine ⟨fun i => ?_, Nat.zero_lt_succ n, ?_⟩
        · by_cases hi : i.val < n
          · exact isCovered_lift (x := snocTri v.val a) (i := ⟨i.val, hi⟩) (by
              simpa [initTri_snocTri] using v.property.1 ⟨i.val, hi⟩)
          · have hiLt : i.val < n + 1 := i.isLt
            have heq : i = ⟨n, Nat.lt_succ_self n⟩ := Fin.ext (by dsimp; omega)
            rw [heq]
            refine Or.inr (Or.inr ⟨hn, ?_⟩)
            have h1 : snocTri v.val a ⟨n - 1, by omega⟩ = v.val ⟨n - 1, by omega⟩ :=
              snocTri_lt v.val a (by dsimp; omega)
            have h2 : snocTri v.val a ⟨n, Nat.lt_succ_self n⟩ = a := snocTri_last v.val a
            change (snocTri v.val a ⟨n - 1, by omega⟩).val +
              (snocTri v.val a ⟨n, Nat.lt_succ_self n⟩).val = 0
            rw [h1, h2]
            simp [a]
        · change (snocTri v.val a ⟨n, Nat.lt_succ_self n⟩).val ≠ 0
          rw [snocTri_last]
          simp [a, v.property.2.2]⟩
    | Sum.inr w =>
      let hn : 0 < n := w.property.2.1
      let a : TriInt := triNegate (w.val ⟨n - 1, by omega⟩)
      have hw_ne0 : (w.val ⟨n - 1, by omega⟩).val ≠ 0 :=
        fun h0 => w.property.2.2 (Or.inl h0)
      ⟨snocTri w.val a, by
        refine ⟨fun i => ?_, Nat.zero_lt_succ n, ?_⟩
        · by_cases hi : i.val + 1 < n
          · exact isCovered_lift (x := snocTri w.val a) (i := ⟨i.val, by omega⟩) (by
              simpa [initTri_snocTri] using w.property.1 ⟨i.val, by omega⟩ hi)
          · by_cases hi' : i.val < n
            · have heq : i = ⟨n - 1, by omega⟩ := Fin.ext (by dsimp; omega)
              rw [heq]
              refine Or.inr (Or.inl ⟨by dsimp; omega, ?_⟩)
              have h1 : snocTri w.val a ⟨n - 1, by omega⟩ = w.val ⟨n - 1, by omega⟩ :=
                snocTri_lt w.val a (by dsimp; omega)
              have h2 : snocTri w.val a ⟨n - 1 + 1, by omega⟩ = a := by
                have hidx : (⟨n - 1 + 1, by omega⟩ : Fin (n + 1)) = ⟨n, Nat.lt_succ_self n⟩ :=
                  Fin.ext (by dsimp; omega)
                rw [hidx, snocTri_last]
              change (snocTri w.val a ⟨n - 1, by omega⟩).val +
                (snocTri w.val a ⟨n - 1 + 1, by omega⟩).val = 0
              rw [h1, h2]
              simp [a]
            · have hiLt : i.val < n + 1 := i.isLt
              have heq : i = ⟨n, Nat.lt_succ_self n⟩ := Fin.ext (by dsimp; omega)
              rw [heq]
              refine Or.inr (Or.inr ⟨hn, ?_⟩)
              have h1 : snocTri w.val a ⟨n - 1, by omega⟩ = w.val ⟨n - 1, by omega⟩ :=
                snocTri_lt w.val a (by dsimp; omega)
              have h2 : snocTri w.val a ⟨n, Nat.lt_succ_self n⟩ = a := snocTri_last w.val a
              change (snocTri w.val a ⟨n - 1, by omega⟩).val +
                (snocTri w.val a ⟨n, Nat.lt_succ_self n⟩).val = 0
              rw [h1, h2]
              simp [a]
        · change (snocTri w.val a ⟨n, Nat.lt_succ_self n⟩).val ≠ 0
          rw [snocTri_last]
          simp [a, hw_ne0]⟩
  left_inv v := by
    apply Subtype.ext
    have hcovn : IsCovered (fun j => (v.val j).val) ⟨n, Nat.lt_succ_self n⟩ :=
      v.property.1 ⟨n, Nat.lt_succ_self n⟩
    have hne0 : (v.val ⟨n, Nat.lt_succ_self n⟩).val ≠ 0 := v.property.2.2
    have hn_and_sum : ∃ h : 0 < n, (initTri v.val ⟨n - 1, by omega⟩).val +
        (v.val ⟨n, Nat.lt_succ_self n⟩).val = 0 := by
      rcases hcovn with h0 | ⟨hlt, _⟩ | ⟨hpos, hsum⟩
      · exact absurd h0 hne0
      · simp at hlt
      · exact ⟨hpos, hsum⟩
    have hn : 0 < n := hn_and_sum.1
    have hlast_eq : triNegate (initTri v.val ⟨n - 1, by omega⟩) = v.val ⟨n, Nat.lt_succ_self n⟩ :=
      (triInt_eq_negate_of_add_eq_zero hn_and_sum.2).symm
    dsimp only
    split_ifs
    · change snocTri (initTri v.val) (triNegate (initTri v.val ⟨n - 1, by omega⟩)) = v.val
      rw [hlast_eq, snocTri_initTri]
    · change snocTri (initTri v.val) (triNegate (initTri v.val ⟨n - 1, by omega⟩)) = v.val
      rw [hlast_eq, snocTri_initTri]
  right_inv s := by
    rcases s with v | w
    · have hn : 0 < n := v.property.2.1
      have hcov : IsCovered (fun j => (initTri (snocTri v.val (triNegate (v.val ⟨n - 1, by omega⟩))) j).val)
          ⟨n - 1, by omega⟩ := by
        rw [initTri_snocTri]; exact v.property.1 ⟨n - 1, by omega⟩
      dsimp only
      split_ifs with h
      · exact congrArg Sum.inl (Subtype.ext (initTri_snocTri _ _))
      · exact absurd hcov h
    · have hn : 0 < n := w.property.2.1
      have hncov : ¬ IsCovered (fun j => (initTri (snocTri w.val (triNegate (w.val ⟨n - 1, by omega⟩))) j).val)
          ⟨n - 1, by omega⟩ := by
        rw [initTri_snocTri]; exact w.property.2.2
      dsimp only
      split_ifs with h
      · exact absurd h hncov
      · exact congrArg Sum.inr (Subtype.ext (initTri_snocTri _ _))

lemma countV_succ (n : ℕ) : countV (n + 1) = countV n + countW n := by
  unfold countV countW
  rw [Nat.card_congr (classVSuccEquiv n), Nat.card_sum]

/-! ### Base Cases (`n = 0`) and Proof of the Main Recurrence -/

lemma countU_zero : countU 0 = 1 := by
  unfold countU
  have : Unique (ClassU 0) :=
    { default := ⟨Fin.elim0, fun i => Fin.elim0 i, fun h => absurd h (Nat.lt_irrefl 0)⟩
      uniq := fun u => Subtype.ext (funext fun i => Fin.elim0 i) }
  exact Nat.card_unique

lemma countV_zero : countV 0 = 0 := by
  unfold countV
  have : IsEmpty (ClassV 0) := ⟨fun v => absurd v.property.2.1 (Nat.lt_irrefl 0)⟩
  rw [Nat.card_congr (Equiv.equivEmpty (ClassV 0))]
  simp

lemma countW_zero : countW 0 = 0 := by
  unfold countW
  have : IsEmpty (ClassW 0) := ⟨fun w => absurd w.property.2.1 (Nat.lt_irrefl 0)⟩
  rw [Nat.card_congr (Equiv.equivEmpty (ClassW 0))]
  simp

theorem A193641_zero : A193641 0 = 1 := by
  have h1 := A193641_eq_U_add_V 0
  have h2 := countU_zero
  have h3 := countV_zero
  omega

theorem A193641_one : A193641 1 = 1 := by
  have hA1 : A193641 1 = countU 1 + countV 1 := A193641_eq_U_add_V 1
  have hU1 : countU 1 = A193641 0 := countU_succ 0
  have hV1 : countV 1 = countV 0 + countW 0 := countV_succ 0
  have hA0 := A193641_zero
  have hV0 := countV_zero
  have hW0 := countW_zero
  omega

theorem A193641_two : A193641 2 = 3 := by
  have hA2 : A193641 2 = countU 2 + countV 2 := A193641_eq_U_add_V 2
  have hU2 : countU 2 = A193641 1 := countU_succ 1
  have hV2 : countV 2 = countV 1 + countW 1 := countV_succ 1
  have hW1 : countW 1 = 2 * countU 0 + countV 0 := countW_succ 0
  have hV1 : countV 1 = countV 0 + countW 0 := countV_succ 0
  have hA1 := A193641_one
  have hU0 := countU_zero
  have hV0 := countV_zero
  have hW0 := countW_zero
  omega

/-- **Part 1 Main Theorem (A):** OEIS `A193641` satisfies the exact linear recurrence
`A193641(m + 3) = 2 * A193641(m + 2) + A193641(m)` for all `m : ℕ`. -/
theorem A193641_recurrence (m : ℕ) :
    A193641 (m + 3) = 2 * A193641 (m + 2) + A193641 m := by
  have hA1 : A193641 (m + 1) = countU (m + 1) + countV (m + 1) := A193641_eq_U_add_V (m + 1)
  have hA2 : A193641 (m + 2) = countU (m + 2) + countV (m + 2) := A193641_eq_U_add_V (m + 2)
  have hA3 : A193641 (m + 3) = countU (m + 3) + countV (m + 3) := A193641_eq_U_add_V (m + 3)
  have hU1 : countU (m + 1) = A193641 m := countU_succ m
  have hU2 : countU (m + 2) = A193641 (m + 1) := countU_succ (m + 1)
  have hU3 : countU (m + 3) = A193641 (m + 2) := countU_succ (m + 2)
  have hW2 : countW (m + 2) = 2 * countU (m + 1) + countV (m + 1) := countW_succ (m + 1)
  have hV3 : countV (m + 3) = countV (m + 2) + countW (m + 2) := countV_succ (m + 2)
  omega

/-- The sequence tabulated in OEIS `A100691`:
`1, 4, 12, 30, 70, 158, 352, 780, ...` with `a(n) = 2*a(n-1) + a(n-3) + 6` for `n ≥ 4`. -/
def aOEIS : ℕ → ℕ
  | 0 => 1
  | 1 => 4
  | 2 => 12
  | 3 => 30
  | n + 4 => 2 * aOEIS (n + 3) + aOEIS (n + 1) + 6

/-- Coefficient-wise generating function identity confirming that `aOEIS` is the exact
power series expansion of `(1+z^2)(1+z+z^2)/((1-z)(1-2z-z^3)) = (1+z+2z^2+z^3+z^4)/(1-3z+2z^2-z^3+z^4)`. -/
theorem aOEIS_gf_identity (n : ℕ) :
    (aOEIS n : ℤ)
      - 3 * (if 1 ≤ n then (aOEIS (n - 1) : ℤ) else 0)
      + 2 * (if 2 ≤ n then (aOEIS (n - 2) : ℤ) else 0)
      - (if 3 ≤ n then (aOEIS (n - 3) : ℤ) else 0)
      + (if 4 ≤ n then (aOEIS (n - 4) : ℤ) else 0) =
    match n with
    | 0 => 1
    | 1 => 1
    | 2 => 2
    | 3 => 1
    | 4 => 1
    | _ + 5 => 0 := by
  match n with
  | 0 => decide
  | 1 => decide
  | 2 => decide
  | 3 => decide
  | 4 => decide
  | k + 5 =>
    simp only [Nat.reduceLeDiff, ↓reduceIte]
    have h1 : aOEIS (k + 5) = 2 * aOEIS (k + 4) + aOEIS (k + 2) + 6 := rfl
    have h2 : aOEIS (k + 4) = 2 * aOEIS (k + 3) + aOEIS (k + 1) + 6 := rfl
    have hsub1 : k + 5 - 1 = k + 4 := by omega
    have hsub2 : k + 5 - 2 = k + 3 := by omega
    have hsub3 : k + 5 - 3 = k + 2 := by omega
    have hsub4 : k + 5 - 4 = k + 1 := by omega
    rw [hsub1, hsub2, hsub3, hsub4]
    omega

/-- **Part 1 Main Theorem (B):** Mathar's 2022 conjecture holds for ALL `n ≥ 1` under the
OEIS tabulated/GF sequence reading: `aOEIS n = A193641 (n + 2) - 3` (and `aOEIS n + 3 = A193641 (n + 2)`). -/
theorem aOEIS_add_three_eq_A193641 (n : ℕ) (hn : 1 ≤ n) :
    aOEIS n + 3 = A193641 (n + 2) := by
  have h0 : A193641 0 = 1 := A193641_zero
  have h1 : A193641 1 = 1 := A193641_one
  have h2 : A193641 2 = 3 := A193641_two
  have h3 : A193641 3 = 2 * A193641 2 + A193641 0 := A193641_recurrence 0
  have h4 : A193641 4 = 2 * A193641 3 + A193641 1 := A193641_recurrence 1
  have h5 : A193641 5 = 2 * A193641 4 + A193641 2 := A193641_recurrence 2
  induction n using Nat.strong_induction_on with
  | ind k ih =>
    match k with
    | 0 => omega
    | 1 => change 4 + 3 = A193641 3; omega
    | 2 => change 12 + 3 = A193641 4; omega
    | 3 => change 30 + 3 = A193641 5; omega
    | m + 4 =>
      have ha : aOEIS (m + 4) = 2 * aOEIS (m + 3) + aOEIS (m + 1) + 6 := rfl
      have ih1 : aOEIS (m + 3) + 3 = A193641 (m + 5) := ih (m + 3) (by omega) (by omega)
      have ih3 : aOEIS (m + 1) + 3 = A193641 (m + 3) := ih (m + 1) (by omega) (by omega)
      have hrec : A193641 (m + 6) = 2 * A193641 (m + 5) + A193641 (m + 3) :=
        A193641_recurrence (m + 3)
      have hgoal : m + 4 + 2 = m + 6 := by omega
      rw [hgoal]
      omega

theorem aOEIS_eq_A193641_sub_three (n : ℕ) (hn : 1 ≤ n) :
    aOEIS n = A193641 (n + 2) - 3 := by
  have h := aOEIS_add_three_eq_A193641 n hn
  omega

theorem A193641_seven : A193641 7 = 161 := by
  have h : aOEIS 5 + 3 = A193641 7 := aOEIS_add_three_eq_A193641 5 (by omega)
  have ha : aOEIS 5 = 158 := by decide
  omega

/-! ## Part 2: Exact Self-Avoiding Path Count `s(5) = 160 ≠ 158` on the Triangular Strip `ℤ × {0, 1}` -/

/-- Vertex set of the strip `ℤ × {0, 1}`. -/
abbrev StripVertex := ℤ × Fin 2

/-- The triangular lattice strip graph on `ℤ × {0, 1}`:
horizontal edges `(x, y) -- (x+1, y)`, vertical edges `(x, 0) -- (x, 1)`,
and diagonal edges `(x-1, 1) -- (x, 0)` (every vertex has degree 4). -/
def triStripGraph : SimpleGraph StripVertex where
  Adj u v :=
    (u.2 = v.2 ∧ (v.1 = u.1 + 1 ∨ u.1 = v.1 + 1)) ∨
    (u.1 = v.1 ∧ u.2 ≠ v.2) ∨
    (u.2 = 1 ∧ v.2 = 0 ∧ v.1 = u.1 + 1) ∨
    (u.2 = 0 ∧ v.2 = 1 ∧ u.1 = v.1 + 1)
  symm := ⟨by
    rintro ⟨x1, y1⟩ ⟨x2, y2⟩ (⟨hy, hx⟩ | ⟨hx, hy⟩ | ⟨h1, h2, hx⟩ | ⟨h1, h2, hx⟩)
    · exact Or.inl ⟨hy.symm, hx.symm⟩
    · exact Or.inr (Or.inl ⟨hx.symm, hy.symm⟩)
    · exact Or.inr (Or.inr (Or.inr ⟨h2, h1, hx⟩))
    · exact Or.inr (Or.inr (Or.inl ⟨h2, h1, hx⟩))⟩
  loopless := ⟨by
    rintro ⟨x, y⟩ (⟨_, h | h⟩ | ⟨_, h⟩ | ⟨h1, h2, _⟩ | ⟨h1, h2, _⟩)
    · omega
    · omega
    · exact h rfl
    · exact absurd (h1.symm.trans h2) (by decide)
    · exact absurd (h1.symm.trans h2) (by decide)⟩

/-- An `n`-step self-avoiding path on `triStripGraph` starting at `(0, 0)`. -/
def IsSAW (n : ℕ) (p : Fin (n + 1) → StripVertex) : Prop :=
  p 0 = (0, 0) ∧
  Function.Injective p ∧
  ∀ i : Fin n, triStripGraph.Adj (p i.castSucc) (p i.succ)

/-- Exact count `s(n)` of `n`-step self-avoiding paths starting at `(0, 0)` on `ℤ × {0, 1}`. -/
noncomputable def sawCount (n : ℕ) : ℕ :=
  Nat.card {p : Fin (n + 1) → StripVertex // IsSAW n p}

/-- The 4 neighbors of any vertex `v` in `triStripGraph`. -/
def stepDir (v : StripVertex) (d : Fin 4) : StripVertex :=
  match v.2, d with
  | 0, 0 => (v.1 + 1, 0)
  | 0, 1 => (v.1 - 1, 0)
  | 0, 2 => (v.1, 1)
  | 0, 3 => (v.1 - 1, 1)
  | 1, 0 => (v.1 + 1, 1)
  | 1, 1 => (v.1 - 1, 1)
  | 1, 2 => (v.1, 0)
  | 1, 3 => (v.1 + 1, 0)

def allDirs : List (Fin 4) := [0, 1, 2, 3]

lemma stepDir_injective (v : StripVertex) : Function.Injective (stepDir v) := by
  rcases v with ⟨x, y⟩
  intro d1 d2 h
  match y with
  | 0 =>
    match d1, d2 with
    | 0, 0 | 1, 1 | 2, 2 | 3, 3 => rfl
    | 0, 1 | 0, 2 | 0, 3 | 1, 0 | 1, 2 | 1, 3 | 2, 0 | 2, 1 | 2, 3 | 3, 0 | 3, 1 | 3, 2 =>
      simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
      omega
  | 1 =>
    match d1, d2 with
    | 0, 0 | 1, 1 | 2, 2 | 3, 3 => rfl
    | 0, 1 | 0, 2 | 0, 3 | 1, 0 | 1, 2 | 1, 3 | 2, 0 | 2, 1 | 2, 3 | 3, 0 | 3, 1 | 3, 2 =>
      simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
      omega

lemma adj_iff_exists_stepDir (u v : StripVertex) :
    triStripGraph.Adj u v ↔ ∃ d : Fin 4, stepDir u d = v := by
  rcases u with ⟨x1, y1⟩
  rcases v with ⟨x2, y2⟩
  match y1, y2 with
  | 0, 0 =>
    dsimp only [triStripGraph]
    constructor
    · rintro (⟨_, h | h⟩ | ⟨_, hne⟩ | ⟨h1, _, _⟩ | ⟨_, h2, _⟩)
      · exact ⟨0, by simp [stepDir]; omega⟩
      · exact ⟨1, by simp [stepDir]; omega⟩
      · exact absurd rfl hne
      · exact absurd h1 (by decide)
      · exact absurd h2 (by decide)
    · rintro ⟨d, h⟩
      match d with
      | 0 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inl ⟨rfl, Or.inl h.1.symm⟩
      | 1 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inl ⟨rfl, Or.inr (by omega)⟩
      | 2 | 3 =>
        simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
        omega
  | 0, 1 =>
    dsimp only [triStripGraph]
    constructor
    · rintro (⟨hy, _⟩ | ⟨hx, _⟩ | ⟨h1, _, _⟩ | ⟨_, _, hx⟩)
      · exact absurd hy (by decide)
      · exact ⟨2, by simp [stepDir]; omega⟩
      · exact absurd h1 (by decide)
      · exact ⟨3, by simp [stepDir]; omega⟩
    · rintro ⟨d, h⟩
      match d with
      | 0 | 1 =>
        simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
        omega
      | 2 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inr (Or.inl ⟨h.1, by decide⟩)
      | 3 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inr (Or.inr (Or.inr ⟨rfl, rfl, by omega⟩))
  | 1, 0 =>
    dsimp only [triStripGraph]
    constructor
    · rintro (⟨hy, _⟩ | ⟨hx, _⟩ | ⟨_, _, hx⟩ | ⟨h1, _, _⟩)
      · exact absurd hy (by decide)
      · exact ⟨2, by simp [stepDir]; omega⟩
      · exact ⟨3, by simp [stepDir]; omega⟩
      · exact absurd h1 (by decide)
    · rintro ⟨d, h⟩
      match d with
      | 0 | 1 =>
        simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
        omega
      | 2 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inr (Or.inl ⟨h.1, by decide⟩)
      | 3 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inr (Or.inr (Or.inl ⟨rfl, rfl, h.1.symm⟩))
  | 1, 1 =>
    dsimp only [triStripGraph]
    constructor
    · rintro (⟨_, h | h⟩ | ⟨_, hne⟩ | ⟨_, h2, _⟩ | ⟨h1, _, _⟩)
      · exact ⟨0, by simp [stepDir]; omega⟩
      · exact ⟨1, by simp [stepDir]; omega⟩
      · exact absurd rfl hne
      · exact absurd h2 (by decide)
      · exact absurd h1 (by decide)
    · rintro ⟨d, h⟩
      match d with
      | 0 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inl ⟨rfl, Or.inl h.1.symm⟩
      | 1 =>
        simp only [stepDir, Prod.mk.injEq] at h
        exact Or.inl ⟨rfl, Or.inr (by omega)⟩
      | 2 | 3 =>
        simp only [stepDir, Prod.mk.injEq, Fin.ext_iff] at h
        omega

/-- Exact DFS enumerator of all `n`-step self-avoiding paths (stored head-last: `[p n, ..., p 0]`). -/
def sawPaths : ℕ → List (List StripVertex)
  | 0 => [[(0, 0)]]
  | n + 1 =>
    (sawPaths n).flatMap fun path =>
      match path with
      | [] => []
      | v :: _ =>
        allDirs.filterMap fun d =>
          let w := stepDir v d
          if w ∈ path then none else some (w :: path)

/-- Predicate characterizing lists in `sawPaths n`: reversed `n`-step SAWs `[p n, ..., p 0]`. -/
def IsRevSAW (n : ℕ) (L : List StripVertex) : Prop :=
  L.length = n + 1 ∧
  L.getLast? = some (0, 0) ∧
  L.Nodup ∧
  L.IsChain (fun a b => triStripGraph.Adj b a)

lemma mem_allDirs (d : Fin 4) : d ∈ allDirs := by
  revert d; decide

lemma allDirs_nodup : allDirs.Nodup := by decide

lemma mem_sawPaths_iff (n : ℕ) (L : List StripVertex) :
    L ∈ sawPaths n ↔ IsRevSAW n L := by
  induction n generalizing L with
  | zero =>
    simp only [sawPaths, List.mem_singleton, IsRevSAW]
    constructor
    · rintro rfl
      refine ⟨rfl, rfl, List.nodup_singleton _, List.IsChain.singleton _⟩
    · rintro ⟨hlen, hlast, _, _⟩
      rcases L with _ | ⟨a, _ | ⟨b, t⟩⟩
      · simp at hlen
      · simp only [List.getLast?_singleton, Option.some.injEq] at hlast
        rw [hlast]
      · simp at hlen
  | succ n ih =>
    simp only [sawPaths, List.mem_flatMap]
    constructor
    · rintro ⟨path, hpath, hmem⟩
      have hrev := (ih path).mp hpath
      rcases path with _ | ⟨v, rest⟩
      · simp [IsRevSAW] at hrev
      · simp only [List.mem_filterMap] at hmem
        obtain ⟨d, _, hsome⟩ := hmem
        by_cases hw : stepDir v d ∈ v :: rest
        · simp [hw] at hsome
        · simp only [hw, ↓reduceIte, Option.some.injEq] at hsome
          subst hsome
          refine ⟨by simpa using hrev.1, ?_, List.nodup_cons.mpr ⟨hw, hrev.2.2.1⟩, ?_⟩
          · simpa using hrev.2.1
          · exact List.IsChain.cons_cons ((adj_iff_exists_stepDir v (stepDir v d)).mpr ⟨d, rfl⟩)
              hrev.2.2.2
    · rintro ⟨hlen, hlast, hnodup, hchain⟩
      rcases L with _ | ⟨w, path⟩
      · simp at hlen
      · rcases path with _ | ⟨v, rest⟩
        · simp at hlen
        · have hadj : triStripGraph.Adj v w := (List.isChain_cons_cons.mp hchain).1
          have hchain' : (v :: rest).IsChain (fun a b => triStripGraph.Adj b a) :=
            (List.isChain_cons_cons.mp hchain).2
          have hnodup_cons := List.nodup_cons.mp hnodup
          have hrev' : IsRevSAW n (v :: rest) :=
            ⟨by simpa using hlen, by simpa using hlast, hnodup_cons.2, hchain'⟩
          obtain ⟨d, hd⟩ := (adj_iff_exists_stepDir v w).mp hadj
          refine ⟨v :: rest, (ih (v :: rest)).mpr hrev', ?_⟩
          simp only [List.mem_filterMap]
          refine ⟨d, mem_allDirs d, ?_⟩
          rw [hd]
          simp [hnodup_cons.1]

lemma sawPaths_nodup (n : ℕ) : (sawPaths n).Nodup := by
  induction n with
  | zero => exact List.nodup_singleton _
  | succ n ih =>
    rw [sawPaths, List.nodup_flatMap]
    refine ⟨fun path _ => ?_, ?_⟩
    · rcases path with _ | ⟨v, rest⟩
      · exact List.nodup_nil
      · refine List.Nodup.filterMap ?_ allDirs_nodup
        intro d1 d2 L h1 h2
        dsimp only at h1 h2
        rw [Option.mem_def] at h1 h2
        by_cases hw1 : stepDir v d1 ∈ v :: rest
        · simp [hw1] at h1
        · by_cases hw2 : stepDir v d2 ∈ v :: rest
          · simp [hw2] at h2
          · simp only [hw1, ↓reduceIte, Option.some.injEq] at h1
            simp only [hw2, ↓reduceIte, Option.some.injEq] at h2
            have hstep : stepDir v d1 = stepDir v d2 :=
              (List.cons.inj (h1.trans h2.symm)).1
            exact stepDir_injective v hstep
    · refine ih.imp_of_mem fun {path1 path2} _ _ hne => List.disjoint_left.mpr fun L hL1 hL2 => ?_
      rcases path1 with _ | ⟨v1, r1⟩
      · simp at hL1
      · rcases path2 with _ | ⟨v2, r2⟩
        · simp at hL2
        · simp only [List.mem_filterMap] at hL1 hL2
          obtain ⟨d1, _, h1⟩ := hL1
          obtain ⟨d2, _, h2⟩ := hL2
          by_cases hw1 : stepDir v1 d1 ∈ v1 :: r1
          · simp [hw1] at h1
          · by_cases hw2 : stepDir v2 d2 ∈ v2 :: r2
            · simp [hw2] at h2
            · simp only [hw1, ↓reduceIte, Option.some.injEq] at h1
              simp only [hw2, ↓reduceIte, Option.some.injEq] at h2
              exact hne (List.cons.inj (h1.trans h2.symm)).2

/-- Bijection between `n`-step self-avoiding paths (`Fin (n+1) → StripVertex`) and `IsRevSAW n`. -/
def sawEquivRevSAW (n : ℕ) :
    {p : Fin (n + 1) → StripVertex // IsSAW n p} ≃ {L : List StripVertex // IsRevSAW n L} where
  toFun p :=
    ⟨(List.ofFn p.val).reverse, by
      refine ⟨by simp, ?_, ?_, ?_⟩
      · rw [List.getLast?_reverse, List.head?_eq_getElem?]
        rw [List.getElem?_eq_getElem (by simp)]
        simp [p.property.1]
      · rw [List.nodup_reverse, List.nodup_ofFn]
        exact p.property.2.1
      · rw [List.isChain_iff_getElem]
        intro i hi
        have hlen : (List.ofFn p.val).reverse.length = n + 1 := by simp
        have hi' : n - 1 - i < n := by omega
        simp only [List.getElem_reverse, List.length_ofFn, List.getElem_ofFn]
        have hstep := p.property.2.2 ⟨n - 1 - i, hi'⟩
        have h1 : (⟨n - 1 - i, hi'⟩ : Fin n).castSucc = ⟨n + 1 - 1 - (i + 1), by omega⟩ :=
          Fin.ext (by dsimp [Fin.castSucc]; omega)
        have h2 : (⟨n - 1 - i, hi'⟩ : Fin n).succ = ⟨n + 1 - 1 - i, by omega⟩ :=
          Fin.ext (by dsimp [Fin.succ]; omega)
        rwa [h1, h2] at hstep⟩
  invFun L :=
    ⟨fun i => L.val.reverse[i.val]'(by rw [List.length_reverse, L.property.1]; exact i.isLt), by
      have hlen : L.val.reverse.length = n + 1 := by rw [List.length_reverse, L.property.1]
      refine ⟨?_, ?_, ?_⟩
      · have hhead : L.val.reverse.head? = some (0, 0) := by
          rw [List.head?_reverse]; exact L.property.2.1
        have h0 : L.val.reverse.head? = some (L.val.reverse[0]'(by omega)) := by
          rw [List.head?_eq_getElem?]
          exact List.getElem?_eq_getElem (by omega)
        exact Option.some.inj (h0.symm.trans hhead)
      · intro i j hij
        have hnodup : L.val.reverse.Nodup := List.nodup_reverse.mpr L.property.2.2.1
        have heq := (List.Nodup.getElem_inj_iff hnodup).mp hij
        exact Fin.ext heq
      · intro i
        have hiLt : i.val < n := i.isLt
        have hchain := (List.isChain_iff_getElem).mp L.property.2.2.2
        have hj : n - 1 - i.val + 1 < L.val.length := by rw [L.property.1]; omega
        have hadj := hchain (n - 1 - i.val) hj
        simp only [List.getElem_reverse, L.property.1, Fin.val_castSucc, Fin.val_succ]
        have hidx1 : n - 1 - i.val + 1 = n + 1 - 1 - i.val := by omega
        have hidx2 : n - 1 - i.val = n + 1 - 1 - (i.val + 1) := by omega
        convert hadj using 2
        · exact hidx1.symm
        · exact hidx2.symm⟩
  left_inv p := by
    apply Subtype.ext
    funext i
    simp only [List.reverse_reverse, List.getElem_ofFn, Fin.eta]
  right_inv L := by
    apply Subtype.ext
    have hlen : L.val.reverse.length = n + 1 := by rw [List.length_reverse, L.property.1]
    have hofFn : List.ofFn (fun i : Fin (n + 1) =>
        L.val.reverse[i.val]'(by omega)) = L.val.reverse := by
      apply List.ext_getElem
      · simp [hlen]
      · intro i hi1 hi2
        rw [List.getElem_ofFn]
    dsimp only
    rw [hofFn, List.reverse_reverse]

/-- Exact formula for all `n : ℕ`: `sawCount n = (sawPaths n).length`. -/
theorem sawCount_eq_length_sawPaths (n : ℕ) : sawCount n = (sawPaths n).length := by
  unfold sawCount
  rw [Nat.card_congr (sawEquivRevSAW n)]
  have heq : {L : List StripVertex // IsRevSAW n L} ≃ {L : List StripVertex // L ∈ sawPaths n} :=
    Equiv.subtypeEquivRight (fun L => (mem_sawPaths_iff n L).symm)
  rw [Nat.card_congr heq]
  have hfin : {L : List StripVertex // L ∈ sawPaths n} ≃ Fin (sawPaths n).length :=
    { toFun := fun x => ⟨(sawPaths n).idxOf x.val, List.idxOf_lt_length_of_mem x.property⟩
      invFun := fun i => ⟨(sawPaths n)[i.val], List.getElem_mem i.isLt⟩
      left_inv := fun x => Subtype.ext (List.getElem_idxOf _)
      right_inv := fun i => Fin.ext ((sawPaths_nodup n).idxOf_getElem i.val i.isLt) }
  rw [Nat.card_congr hfin, Nat.card_eq_fintype_card, Fintype.card_fin]

/-! ### Exact Evaluation of `s(0..5)` and Refutation at `n = 5` -/

theorem sawCount_zero : sawCount 0 = 1 := by rw [sawCount_eq_length_sawPaths]; rfl
theorem sawCount_one : sawCount 1 = 4 := by rw [sawCount_eq_length_sawPaths]; rfl
theorem sawCount_two : sawCount 2 = 12 := by rw [sawCount_eq_length_sawPaths]; rfl
theorem sawCount_three : sawCount 3 = 30 := by rw [sawCount_eq_length_sawPaths]; rfl
theorem sawCount_four : sawCount 4 = 70 := by rw [sawCount_eq_length_sawPaths]; rfl
theorem sawCount_five : sawCount 5 = 160 := by rw [sawCount_eq_length_sawPaths]; rfl

/-- **Part 2 Main Theorem:** Under the combinatorial definition of OEIS `A100691` (actual
`n`-step self-avoiding paths on the triangular lattice strip `ℤ × {0, 1}`), Mathar's
conjecture `s(n) = A193641(n + 2) - 3` fails at `n = 5`: `s(5) = 160 ≠ 158 = A193641(7) - 3`. -/
theorem refutes_combinatorial_reading_at_five :
    sawCount 5 = 160 ∧
    A193641 (5 + 2) - 3 = 158 ∧
    sawCount 5 ≠ A193641 (5 + 2) - 3 := by
  have hs := sawCount_five
  have hA : A193641 (5 + 2) = 161 := A193641_seven
  omega

theorem not_mathar_combinatorial_conjecture :
    ¬ (∀ n : ℕ, 1 ≤ n → sawCount n = A193641 (n + 2) - 3) := by
  intro hconj
  have h5 := hconj 5 (by omega)
  exact refutes_combinatorial_reading_at_five.2.2 h5

#print axioms A193641_recurrence
#print axioms aOEIS_gf_identity
#print axioms aOEIS_eq_A193641_sub_three
#print axioms sawCount_eq_length_sawPaths
#print axioms sawCount_five
#print axioms refutes_combinatorial_reading_at_five
#print axioms not_mathar_combinatorial_conjecture

end OpenMath.OeisA100691
