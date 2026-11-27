import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Order.Filter.AtTopBot.Basic
import Mathlib.Tactic

/-!
# Vasilyev (`arXiv:2611.20344v2`, Section 7, Question 7.3 `q:types` & Remark 4.4 `rem:types`)

This file formalizes the affirmative resolution of **Question 7.3** (`\label{q:types}`, lines 1991–1993)
and **Remark 4.4** (`\label{rem:types}`, lines 1134–1145) of Oleg Vasilyev,
*"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"*
(`arXiv:2611.20344v2`, `updown.tex`):

> **Definition 1.1 (`def:TS`).** For `x ∈ ℕ₊ = {1, 2, 3, ...}`, let `U(x) = ⌈3x/2⌉` and
> `D(x) = ⌈x/2⌉`, and for `S ⊆ ℕ₊`, let `T_S(x) = U(x)` if `x ∈ S` and `D(x)` if `x ∉ S`.
>
> **Question 7.3 (`q:types`).** *Is there a map with infinitely many cycles and a divergent orbit
> (Remark 4.4)?*

We answer **YES** and prove the stronger exact orbit-type statement `(k, l) = (∞, 1)` of
Remark 4.4 (`rem:types`): there exists `S ⊆ ℕ₊` such that:
1. `T_S` has a **divergent orbit** starting at `1` (`t ↦ (T_S)^[t] 1` is injective and tends to `+∞`,
   hence visits infinitely many distinct values and never enters a cycle);
2. `T_S` has **infinitely many pairwise disjoint cycles** (each of length `≥ 2`, all disjoint from
   the divergent orbit of `1`); and
3. Every `x ≥ 1` either eventually enters one of these cycles or eventually coincides with the
   orbit of `1` — so `T_S` has **exact orbit type `(k, l) = (∞, 1)`** (infinitely many cycles and
   a unique equivalence class of divergent orbits).

## Proof Outline
1. **Closed-Box Trap Lemma (`closed_box_trap`):** Whenever `B ≥ 5`, `B ≡ 5 (mod 6)`,
   `U(ℕ₊ \ R) ⊆ ℕ₊ \ R`, and `R ∩ [B + 1, U(B) - 1] = ∅`, the finite box
   `V(B) = [B + 1, 3B - 1] \ (R ∪ {2B})` is nonempty and closed under `f_B` (`U` on `[B+1, 2B-1]`,
   `D` on `[2B+1, 3B-1]`) with `f_B(x) ≠ x`, yielding a simple cycle `C(B) ⊆ V(B)` of length `≥ 2`.
2. **Admissible Ray `U`-Invariance (`admissible_ray_U_inv`):** Any admissible ray `R` starting at `1`
   (taking `U`-steps or `D`-steps only at `x ≡ 2 (mod 6)`, whose target `D(x) ≡ 1 (mod 3) ∉ Im(U)`)
   satisfies `U(ℕ₊ \ R) ⊆ ℕ₊ \ R`.
3. **Admissible Stage Extension (`admissible_stage_extension`):** For every `H ≥ 5`, there is a
   finite simple admissible path from `H` to `H' > 3B` with `B > 5H`, `B ≡ 5 (mod 6)`, avoiding
   `[B + 1, U(B) - 1]`, using `2`-adic parity flipping (`3^e u` vs `3^{e+1} u mod 4`) and
   `v₂(5q + 3)` descent in Subcase B3b.
4. **Global Construction (`vasilyev_question_7_3_orbit_type_infty_one`):** Concatenating
   `P₀ = [1, 2, 3, 5]` with stages `P₁, P₂, ...` yields an admissible ray `R`, pairwise disjoint
   trap cycles `C(B_m)`, and the explicit set `S ⊆ ℕ₊` realizing exact orbit type `(∞, 1)`.
-/

namespace OpenMath.Vasilyev261120344Q73

/-! ## Section 1: Primary-Source Definitions (`U`, `D`, `T_S`, Cycles, Divergent Orbits) -/

/-- Up step `U(x) = ⌈3x/2⌉ = (3x + 1) / 2` for `x ∈ ℕ₊` (`Definition 1.1` of `arXiv:2611.20344v2`). -/
def U (x : ℕ) : ℕ := (3 * x + 1) / 2

/-- Down step `D(x) = ⌈x/2⌉ = (x + 1) / 2` for `x ∈ ℕ₊` (`Definition 1.1` of `arXiv:2611.20344v2`). -/
def D (x : ℕ) : ℕ := (x + 1) / 2

open Classical in
/-- The generalized Collatz map `T_S(x) = U(x)` if `x ∈ S`, `D(x)` if `x ∉ S` (`eq:TS`). -/
noncomputable def T (S : Set ℕ) (x : ℕ) : ℕ :=
  if x ∈ S then U x else D x

/-- `x` lies on a cycle (periodic orbit) of `f` (`∃ k ≥ 1, f^[k] x = x`). -/
def IsPeriodicPoint (f : ℕ → ℕ) (x : ℕ) : Prop :=
  ∃ k : ℕ, 1 ≤ k ∧ f^[k] x = x

/-- Forward orbit `{ f^[k] x | k : ℕ }` of `x` under `f`. -/
def Orbit (f : ℕ → ℕ) (x : ℕ) : Set ℕ :=
  { y : ℕ | ∃ k : ℕ, f^[k] x = y }

/-- An orbit starting at `x` is divergent if it never repeats a value (equivalently is unbounded
in `ℕ₊`, since every bounded orbit in `ℕ₊` is eventually periodic). -/
def IsDivergentOrbit (f : ℕ → ℕ) (x : ℕ) : Prop :=
  Function.Injective (fun t : ℕ => f^[t] x)

/-- Two orbits eventually coincide (`Remark 4.4` of `arXiv:2611.20344v2`). -/
def EventuallyCoincide (f : ℕ → ℕ) (x y : ℕ) : Prop :=
  ∃ i j : ℕ, f^[i] x = f^[j] y

lemma U_eq_two_mul (m : ℕ) : U (2 * m) = 3 * m := by unfold U; omega
lemma U_eq_two_mul_add_one (m : ℕ) : U (2 * m + 1) = 3 * m + 2 := by unfold U; omega
lemma D_eq_two_mul (m : ℕ) : D (2 * m) = m := by unfold D; omega
lemma D_eq_two_mul_add_one (m : ℕ) : D (2 * m + 1) = m + 1 := by unfold D; omega

lemma two_mul_U (x : ℕ) : 2 * U x = 3 * x + x % 2 := by unfold U; omega
lemma two_mul_D (x : ℕ) : 2 * D x = x + x % 2 := by unfold D; omega

lemma U_gt {x : ℕ} (hx : 1 ≤ x) : x < U x := by unfold U; omega
lemma U_pos {x : ℕ} (hx : 1 ≤ x) : 1 ≤ U x := by unfold U; omega
lemma D_pos {x : ℕ} (hx : 1 ≤ x) : 1 ≤ D x := by unfold D; omega
lemma D_lt {x : ℕ} (hx : 2 ≤ x) : D x < x := by unfold D; omega

lemma T_pos (S : Set ℕ) {x : ℕ} (hx : 1 ≤ x) : 1 ≤ T S x := by
  unfold T; split_ifs
  · exact U_pos hx
  · exact D_pos hx

lemma U_strictMono : StrictMono U := by
  intro a b hab; unfold U; omega

lemma U_injective : Function.Injective U := U_strictMono.injective

lemma D_mono : Monotone D := by
  intro a b hab; unfold D; omega

lemma U_mod_three_ne_one {x : ℕ} (_hx : 1 ≤ x) : U x % 3 ≠ 1 := by
  unfold U; omega

lemma U_iter_pos {x : ℕ} (hx : 1 ≤ x) (k : ℕ) : 1 ≤ U^[k] x := by
  induction k with
  | zero => exact hx
  | succ k ih => rw [Function.iterate_succ_apply']; exact U_pos ih

lemma U_iter_strictMono {x : ℕ} (hx : 1 ≤ x) : StrictMono (fun k => U^[k] x) := by
  refine strictMono_nat_of_lt_succ fun k => ?_
  rw [Function.iterate_succ_apply']
  exact U_gt (U_iter_pos hx k)

lemma U_iter_two_pow_mul (e u : ℕ) : U^[e] (2 ^ e * u) = 3 ^ e * u := by
  induction e generalizing u with
  | zero => simp
  | succ e ih =>
    rw [Function.iterate_succ_apply]
    have h1 : 2 ^ (e + 1) * u = 2 * (2 ^ e * u) := by ring
    rw [h1, U_eq_two_mul]
    have h2 : 3 * (2 ^ e * u) = 2 ^ e * (3 * u) := by ring
    rw [h2, ih (3 * u)]
    ring

/-! ## Section 2: Elementary 2-adic Valuation & Odd-Part Helpers -/

/-- Exact 2-adic valuation `v₂(n)` for `n : ℕ` (with `v₂(0) = 0`). -/
def v2 : ℕ → ℕ
  | 0 => 0
  | n + 1 => if (n + 1) % 2 = 0 then v2 ((n + 1) / 2) + 1 else 0

/-- Odd part `n / 2^{v₂(n)}` for `n : ℕ` (with `oddPart 0 = 0`). -/
def oddPart : ℕ → ℕ
  | 0 => 0
  | n + 1 => if (n + 1) % 2 = 0 then oddPart ((n + 1) / 2) else n + 1

lemma two_pow_v2_mul_oddPart (n : ℕ) : 2 ^ v2 n * oddPart n = n := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => simp [v2, oddPart]
    | m + 1 =>
      rw [v2, oddPart]
      split_ifs with hev
      · have hlt : (m + 1) / 2 < m + 1 := by omega
        have hih := ih ((m + 1) / 2) hlt
        calc 2 ^ (v2 ((m + 1) / 2) + 1) * oddPart ((m + 1) / 2)
            = 2 * (2 ^ v2 ((m + 1) / 2) * oddPart ((m + 1) / 2)) := by ring
          _ = 2 * ((m + 1) / 2) := by rw [hih]
          _ = m + 1 := by omega
      · simp

lemma oddPart_mod_two {n : ℕ} (hn : 1 ≤ n) : oddPart n % 2 = 1 := by
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    match n with
    | 0 => omega
    | m + 1 =>
      rw [oddPart]
      split_ifs with hev
      · exact ih ((m + 1) / 2) (by omega) (by omega)
      · omega

lemma oddPart_pos {n : ℕ} (hn : 1 ≤ n) : 1 ≤ oddPart n := by
  have := oddPart_mod_two hn; omega

lemma v2_two_mul {n : ℕ} (hn : 1 ≤ n) : v2 (2 * n) = v2 n + 1 := by
  obtain ⟨k, hk⟩ : ∃ k, 2 * n = k + 1 := ⟨2 * n - 1, by omega⟩
  rw [hk, v2]
  have hev : (k + 1) % 2 = 0 := by omega
  have hdiv : (k + 1) / 2 = n := by omega
  simp [hev, hdiv]

lemma v2_odd_mul {a b : ℕ} (ha : a % 2 = 1) (hb : 1 ≤ b) : v2 (a * b) = v2 b := by
  induction b using Nat.strong_induction_on with
  | ind b ih =>
    by_cases hbe : b % 2 = 0
    · have hhalf : 1 ≤ b / 2 := by omega
      have h1 : b = 2 * (b / 2) := by omega
      have h2 : a * b = 2 * (a * (b / 2)) := by
        calc a * b = a * (2 * (b / 2)) := by rw [← h1]
          _ = 2 * (a * (b / 2)) := by ring
      have hpos : 1 ≤ a * (b / 2) := Nat.mul_pos (by omega) hhalf
      rw [h2, v2_two_mul hpos]
      conv_rhs => rw [h1, v2_two_mul hhalf]
      rw [ih (b / 2) (by omega) hhalf]
    · have hab_odd : (a * b) % 2 = 1 := by
        rw [Nat.mul_mod, ha]; omega
      have hb_odd : b % 2 = 1 := by omega
      obtain ⟨k1, hk1⟩ : ∃ k1, a * b = k1 + 1 := ⟨a * b - 1, by
        have : 1 ≤ a * b := Nat.mul_pos (by omega) hb; omega⟩
      obtain ⟨k2, hk2⟩ : ∃ k2, b = k2 + 1 := ⟨b - 1, by omega⟩
      rw [hk1, hk2, v2, v2]
      have hne1 : (k1 + 1) % 2 ≠ 0 := by omega
      have hne2 : (k2 + 1) % 2 ≠ 0 := by omega
      simp [hne1, hne2]

lemma two_pow_succ_lt_three_pow {e : ℕ} (he : 2 ≤ e) : 2 ^ (e + 1) < 3 ^ e := by
  induction e, he using Nat.le_induction with
  | base => decide
  | succ m hm ih =>
    have h1 : 2 ^ (m + 1 + 1) = 2 * 2 ^ (m + 1) := by ring
    have h2 : 3 ^ (m + 1) = 3 * 3 ^ m := by ring
    omega

/-! ## Section 3: Admissible Edges, Lemma 1 (Closed-Box Trap), and Lemma 2 (`U`-Invariance) -/

/-- Admissible directed edge `x → y` in the up-down graph `G`:
either a `U`-step `y = U x`, or a `D`-step `y = D x` with `x ≡ 2 (mod 6)` (so `y ≡ 1 (mod 3)`). -/
def AdmissibleStep (x y : ℕ) : Prop :=
  (1 ≤ x ∧ y = U x) ∨ (1 ≤ x ∧ x % 6 = 2 ∧ y = D x)

lemma admissibleStep_pos {x y : ℕ} (h : AdmissibleStep x y) : 1 ≤ y := by
  rcases h with ⟨hx, rfl⟩ | ⟨hx, _, rfl⟩
  · exact U_pos hx
  · exact D_pos hx

/-- **Lemma 2 (Admissible Ray `U`-Invariance):**
If `r : ℕ → ℕ` is an admissible sequence starting at `r 0 = 1`, then `U(ℕ₊ \ Im(r)) ⊆ ℕ₊ \ Im(r)`. -/
theorem admissible_ray_U_inv {r : ℕ → ℕ} (hr0 : r 0 = 1)
    (hstep : ∀ t : ℕ, AdmissibleStep (r t) (r (t + 1))) :
    ∀ x : ℕ, 1 ≤ x → x ∉ Set.range r → U x ∉ Set.range r := by
  intro x hx hnot hmem
  rcases hmem with ⟨t, ht⟩
  cases t with
  | zero =>
    have hUgt : 2 ≤ U x := by unfold U; omega
    omega
  | succ t =>
    rcases hstep t with ⟨_, hU⟩ | ⟨_, hmod6, hD⟩
    · have heq : r t = x := U_injective (hU.symm.trans ht)
      exact hnot ⟨t, heq⟩
    · have hmod3 : D (r t) % 3 = 1 := by unfold D; omega
      have hne3 : U x % 3 ≠ 1 := U_mod_three_ne_one hx
      rw [hD] at ht
      omega

/-- Trap map `f_B` on `[B + 1, 3B - 1] \ {2B}`: `U` on `[B + 1, 2B - 1]` and `D` on `[2B + 1, 3B - 1]`. -/
def trapMap (B x : ℕ) : ℕ :=
  if x ≤ 2 * B - 1 then U x else D x

/-- **Lemma 1 (Closed-Box Trap Lemma):**
For any `R ⊆ ℕ` with `U(ℕ₊ \ R) ⊆ ℕ₊ \ R` and any `B ≥ 5`, `B ≡ 5 (mod 6)` with
`R ∩ [B + 1, U(B) - 1] = ∅`, the trap map `f_B` admits a periodic point `c` whose entire orbit
lies in `[B + 1, 3B - 1] \ (R ∪ {2B})` and has minimal period `≥ 2` (`f_B(x) ≠ x` on the cycle). -/
theorem closed_box_trap {R : Set ℕ} {B : ℕ} (hB5 : 5 ≤ B) (hBmod : B % 6 = 5)
    (hU_inv : ∀ x : ℕ, 1 ≤ x → x ∉ R → U x ∉ R)
    (hgap : ∀ x : ℕ, B + 1 ≤ x → x ≤ U B - 1 → x ∉ R) :
    ∃ c : ℕ, IsPeriodicPoint (trapMap B) c ∧
      (∀ y ∈ Orbit (trapMap B) c,
        B + 1 ≤ y ∧ y ≤ 3 * B - 1 ∧ y ∉ R ∧ y ≠ 2 * B ∧ trapMap B y ≠ y) := by
  have hUB : 2 * U B = 3 * B + 1 := by unfold U; omega
  have hmem_inv : ∀ x : ℕ,
      (B + 1 ≤ x ∧ x ≤ 3 * B - 1 ∧ x ∉ R ∧ x ≠ 2 * B) →
      (B + 1 ≤ trapMap B x ∧ trapMap B x ≤ 3 * B - 1 ∧ trapMap B x ∉ R ∧ trapMap B x ≠ 2 * B) := by
    intro x ⟨hxlo, hxhi, hxR, hx2B⟩
    unfold trapMap
    split_ifs with hle
    · refine ⟨?_, ?_, hU_inv x (by omega) hxR, ?_⟩
      · have := U_gt (x := x) (by omega); omega
      · unfold U; omega
      · intro heq
        have hne3 : U x % 3 ≠ 1 := U_mod_three_ne_one (by omega)
        have h2B3 : (2 * B) % 3 = 1 := by omega
        omega
    · have hDlo : B + 1 ≤ D x := by unfold D; omega
      have hDhi : D x ≤ U B - 1 := by unfold D; omega
      refine ⟨hDlo, by omega, hgap (D x) hDlo hDhi, by omega⟩
  have hstart : B + 1 ≤ B + 1 ∧ B + 1 ≤ 3 * B - 1 ∧ (B + 1) ∉ R ∧ B + 1 ≠ 2 * B :=
    ⟨le_rfl, by omega, hgap (B + 1) le_rfl (by omega), by omega⟩
  have hiter_in : ∀ t : ℕ,
      let y := (trapMap B)^[t] (B + 1)
      B + 1 ≤ y ∧ y ≤ 3 * B - 1 ∧ y ∉ R ∧ y ≠ 2 * B := by
    intro t
    induction t with
    | zero => exact hstart
    | succ t ih =>
      dsimp only at ih ⊢
      rw [Function.iterate_succ_apply']
      exact hmem_inv _ ih
  -- Pigeonhole on the finite interval `Icc (B + 1) (3 * B - 1)`
  let g : ℕ → Finset.Icc (B + 1) (3 * B - 1) := fun t =>
    ⟨(trapMap B)^[t] (B + 1), Finset.mem_Icc.mpr ⟨(hiter_in t).1, (hiter_in t).2.1⟩⟩
  obtain ⟨t₁, t₂, hne, hgeq⟩ := Finite.exists_ne_map_eq_of_infinite g
  have hval : (trapMap B)^[t₁] (B + 1) = (trapMap B)^[t₂] (B + 1) := congrArg Subtype.val hgeq
  wlog hlt : t₁ < t₂ generalizing t₁ t₂
  · exact this t₂ t₁ hne.symm hgeq.symm hval.symm (by omega)
  let c := (trapMap B)^[t₁] (B + 1)
  have hper : IsPeriodicPoint (trapMap B) c := by
    refine ⟨t₂ - t₁, by omega, ?_⟩
    change (trapMap B)^[t₂ - t₁] ((trapMap B)^[t₁] (B + 1)) = (trapMap B)^[t₁] (B + 1)
    rw [← Function.iterate_add_apply, Nat.sub_add_cancel hlt.le]
    exact hval.symm
  refine ⟨c, hper, ?_⟩
  rintro y ⟨k, rfl⟩
  have heq : (trapMap B)^[k] c = (trapMap B)^[k + t₁] (B + 1) := by
    dsimp [c]; rw [← Function.iterate_add_apply]
  rw [heq]
  obtain ⟨hlo, hhi, hR, h2B⟩ := hiter_in (k + t₁)
  refine ⟨hlo, hhi, hR, h2B, ?_⟩
  unfold trapMap
  split_ifs
  · exact (U_gt (x := (trapMap B)^[k + t₁] (B + 1)) (by omega)).ne'
  · exact (D_lt (x := (trapMap B)^[k + t₁] (B + 1)) (by omega)).ne

/-! ## Section 4: Lemma 3 (Admissible Stage Extension) -/

/-- A pure `U`-prefix `[H, U H, ..., U^[k] H]` of length `k + 1` (represented by `k` and endpoint `w = U^[k] H`).
Given any `k : ℕ`, `uPath H k = [H, U H, ..., U^[k] H]`. -/
def uPath (H k : ℕ) : List ℕ :=
  (List.range (k + 1)).map (fun i => U^[i] H)

/-- Tail of `uPath H k` (excluding `H`), i.e., `[U H, ..., U^[k] H]`. -/
def uTail (H k : ℕ) : List ℕ :=
  (List.range k).map (fun i => U^[i + 1] H)

/-- Output of one stage extending from head `H ≥ 5` to new head `H' > 3B`:
`verts` lists the vertices strictly after `H` (`[p_1, ..., p_L]`, nonempty, ending at `H'`). -/
structure Stage (H : ℕ) where
  verts : List ℕ
  B : ℕ
  H' : ℕ
  hnonempty : verts ≠ []
  hB_gt : 5 * H < B
  hB_mod : B % 6 = 5
  hH'_gt : 3 * B < H'
  hlast : verts.getLast hnonempty = H'
  hfirst : AdmissibleStep H (verts.head hnonempty)
  hsteps : ∀ i : ℕ, (hi : i + 1 < verts.length) → AdmissibleStep verts[i] verts[i + 1]
  hnodup : (H :: verts).Nodup
  hgt : ∀ x ∈ verts, H < x
  hle : ∀ x ∈ verts, x ≤ H'
  hgap : ∀ x ∈ verts, ¬ (B + 1 ≤ x ∧ x ≤ U B - 1)

/-- Helper A: Pure `U`-chain from `H ≥ 5` to `A` with `A % 4 = 3` and `U A > 5 * H` yields a `Stage H`. -/
private lemma stage_of_pure_U {H k : ℕ} (hH : 5 ≤ H) (hmod4 : (U^[k] H) % 4 = 3)
    (hBgt : 5 * H < U (U^[k] H)) : Nonempty (Stage H) := by
  let A := U^[k] H
  let B := U A
  let C := U B
  let H' := U (U C)
  have hB_mod : B % 6 = 5 := by
    have hA4 : A % 4 = 3 := hmod4
    change (3 * A + 1) / 2 % 6 = 5
    omega
  have hH'_gt : 3 * B < H' := by
    have h1 : 2 * C = 3 * B + 1 := by dsimp [C]; unfold U; omega
    have h2 : 3 * C ≤ 2 * U C := by unfold U; omega
    have h3 : 3 * U C ≤ 2 * U (U C) := by unfold U; omega
    dsimp [H']; omega
  -- Total `U`-steps from `H` to `H'`: `k + 4`
  let L := k + 4
  let verts := uTail H L
  have hlen : verts.length = L := by simp [verts, uTail]
  have hne : verts ≠ [] := by intro h; rw [h] at hlen; simp [L] at hlen
  have hU_succ : ∀ m, U^[m + 1] H = U (U^[m] H) := fun m => Function.iterate_succ_apply' U m H
  have hB_eq : U^[k + 1] H = B := by rw [hU_succ]
  have hC_eq : U^[k + 2] H = C := by rw [hU_succ, hB_eq]
  have hUC_eq : U^[k + 3] H = U C := by rw [hU_succ, hC_eq]
  have hH'_eq : U^[k + 4] H = H' := by rw [hU_succ, hUC_eq]
  have hget : ∀ (i : ℕ) (hi : i < verts.length), verts[i] = U^[i + 1] H := by
    intro i hi; simp [verts, uTail]
  refine ⟨{
    verts := verts
    B := B
    H' := H'
    hnonempty := hne
    hB_gt := hBgt
    hB_mod := hB_mod
    hH'_gt := hH'_gt
    hlast := by
      rw [List.getLast_eq_getElem, hget]
      simp [hlen, L, hH'_eq]
    hfirst := by
      rw [List.head_eq_getElem, hget]
      exact Or.inl ⟨by omega, by simp⟩
    hsteps := by
      intro i hi
      rw [hget i (by omega), hget (i + 1) hi]
      exact Or.inl ⟨U_iter_pos (by omega) (i + 1), by rw [Function.iterate_succ_apply']⟩
    hnodup := by
      have hfull : H :: verts = (List.range (L + 1)).map (fun i => U^[i] H) := by
        rw [List.range_succ_eq_map, List.map_cons, List.map_map]
        simp [verts, uTail, Function.comp_def]
      rw [hfull]
      exact (List.nodup_range).map (U_iter_strictMono (by omega)).injective
    hgt := by
      intro x hx
      rcases List.mem_map.mp hx with ⟨i, _, rfl⟩
      exact U_iter_strictMono (by omega) (Nat.succ_pos i)
    hle := by
      intro x hx
      rcases List.mem_map.mp hx with ⟨i, hi, rfl⟩
      have hil : i + 1 ≤ L := List.mem_range.mp hi
      rw [← hH'_eq]
      exact (U_iter_strictMono (by omega)).monotone hil
    hgap := by
      intro x hx ⟨hlo, hhi⟩
      rcases List.mem_map.mp hx with ⟨i, hi, rfl⟩
      by_cases hle1 : i + 1 ≤ k + 1
      · have : U^[i + 1] H ≤ B := by
          rw [← hB_eq]; exact (U_iter_strictMono (by omega)).monotone hle1
        omega
      · have hge2 : k + 2 ≤ i + 1 := by omega
        have : C ≤ U^[i + 1] H := by
          rw [← hC_eq]; exact (U_iter_strictMono (by omega)).monotone hge2
        omega
  }⟩

/-- Helper B: `U`-chain from `H ≥ 5` to `y = U^[k] H` (`k ≥ 1`, `y % 6 = 2`), followed by one
admissible `D`-step `y → d = D y` (`H < d`), followed by `s + 3` `U`-steps from `d` to
`A = U^[s] d` (`A % 4 = 3`), `B = U A` (`B > y`, `B > 5 * H`), `C = U B`, `U C`, `H' = U (U C)`
yields a `Stage H`. -/
private lemma stage_of_one_D {H k s : ℕ} (hH : 5 ≤ H) (hk : 1 ≤ k)
    (hy_mod : (U^[k] H) % 6 = 2)
    (hd_gt : H < D (U^[k] H))
    (hA_mod : (U^[s] (D (U^[k] H))) % 4 = 3)
    (hB_gt_y : U^[k] H < U (U^[s] (D (U^[k] H))))
    (hB_gt_5H : 5 * H < U (U^[s] (D (U^[k] H)))) : Nonempty (Stage H) := by
  let y := U^[k] H
  let d := D y
  let A := U^[s] d
  let B := U A
  let C := U B
  let H' := U (U C)
  have hd_gt' : H < d := hd_gt
  have hd_pos : 1 ≤ d := by omega
  have hd_mod3 : d % 3 = 1 := by
    have hy6 : y % 6 = 2 := hy_mod
    change (y + 1) / 2 % 3 = 1
    omega
  have hB_mod : B % 6 = 5 := by
    have hA4 : A % 4 = 3 := hA_mod
    change (3 * A + 1) / 2 % 6 = 5
    omega
  have hH'_gt : 3 * B < H' := by
    have h1 : 2 * C = 3 * B + 1 := by dsimp [C]; unfold U; omega
    have h2 : 3 * C ≤ 2 * U C := by unfold U; omega
    have h3 : 3 * U C ≤ 2 * U (U C) := by unfold U; omega
    dsimp [H']; omega
  let p1 := uTail H k
  let p2 := uPath d (s + 4)
  let verts := p1 ++ p2
  have hp1_len : p1.length = k := by simp [p1, uTail]
  have hp2_len : p2.length = s + 5 := by simp [p2, uPath]
  have hp1_ne : p1 ≠ [] := by intro h; rw [h] at hp1_len; simp at hp1_len; omega
  have hp2_ne : p2 ≠ [] := by intro h; rw [h] at hp2_len; simp at hp2_len
  have hne : verts ≠ [] := List.append_ne_nil_of_right_ne_nil p1 hp2_ne
  have hU_succ : ∀ x m, U^[m + 1] x = U (U^[m] x) := fun x m => Function.iterate_succ_apply' U m x
  have hB_eq : U^[s + 1] d = B := by rw [hU_succ]
  have hC_eq : U^[s + 2] d = C := by rw [hU_succ, hB_eq]
  have hUC_eq : U^[s + 3] d = U C := by rw [hU_succ, hC_eq]
  have hH'_eq : U^[s + 4] d = H' := by rw [hU_succ, hUC_eq]
  -- Disjointness between `H :: p1 = {U^[j] H | j ≤ k}` and `p2 = {U^[i] d | i ≤ s + 4}`:
  have hdisj : ∀ (j i : ℕ), U^[j] H ≠ U^[i] d := by
    intro j i heq
    induction j generalizing i with
    | zero =>
      simp only [Function.iterate_zero_apply] at heq
      have hge : d ≤ U^[i] d := (U_iter_strictMono hd_pos).monotone (Nat.zero_le i)
      omega
    | succ j ih =>
      cases i with
      | zero =>
        simp only [Function.iterate_zero_apply, Function.iterate_succ_apply'] at heq
        have hne3 : U (U^[j] H) % 3 ≠ 1 := U_mod_three_ne_one (U_iter_pos (by omega) j)
        omega
      | succ i =>
        rw [Function.iterate_succ_apply', Function.iterate_succ_apply'] at heq
        exact ih i (U_injective heq)
  have hget1 : ∀ (i : ℕ) (hi : i < p1.length), p1[i] = U^[i + 1] H := by
    intro i hi; simp only [p1, uTail, List.getElem_map, List.getElem_range]
  have hget2 : ∀ (i : ℕ) (hi : i < p2.length), p2[i] = U^[i] d := by
    intro i hi; simp only [p2, uPath, List.getElem_map, List.getElem_range]
  have hlen_v : verts.length = p1.length + p2.length := List.length_append
  have hyB : y < B := hB_gt_y
  refine ⟨{
    verts := verts
    B := B
    H' := H'
    hnonempty := hne
    hB_gt := hB_gt_5H
    hB_mod := hB_mod
    hH'_gt := hH'_gt
    hlast := by
      rw [show verts.getLast hne = p2.getLast hp2_ne from List.getLast_append_of_ne_nil hne hp2_ne]
      rw [List.getLast_eq_getElem, hget2]
      simp [hp2_len, hH'_eq]
    hfirst := by
      rw [show verts.head hne = p1.head hp1_ne from List.head_append_of_ne_nil hp1_ne]
      rw [List.head_eq_getElem, hget1]
      exact Or.inl ⟨by omega, by simp⟩
    hsteps := by
      intro i hi
      by_cases hlt1 : i + 1 < p1.length
      · have h1 : verts[i] = p1[i] := List.getElem_append_left (by omega)
        have h2 : verts[i + 1] = p1[i + 1] := List.getElem_append_left hlt1
        rw [h1, h2, hget1, hget1]
        exact Or.inl ⟨U_iter_pos (by omega) (i + 1), by rw [Function.iterate_succ_apply']⟩
      · by_cases heq1 : i + 1 = p1.length
        · have h1 : verts[i] = p1[i] := List.getElem_append_left (by omega)
          have h2 : verts[i + 1] = p2[0] := by
            rw [List.getElem_append_right (by omega)]
            simp [heq1]
          rw [h1, h2, hget1, hget2]
          have hik : i + 1 = k := by omega
          rw [hik]
          exact Or.inr ⟨U_iter_pos (by omega) k, hy_mod, rfl⟩
        · have hi2 : i - p1.length < p2.length := by omega
          have hi2' : i + 1 - p1.length < p2.length := by omega
          have h1 : verts[i] = p2[i - p1.length] := List.getElem_append_right (by omega)
          have h2 : verts[i + 1] = p2[i + 1 - p1.length] := List.getElem_append_right (by omega)
          rw [h1, h2, hget2 _ hi2, hget2 _ hi2']
          have hidx : i + 1 - p1.length = (i - p1.length) + 1 := by omega
          rw [hidx]
          exact Or.inl ⟨U_iter_pos hd_pos _, by rw [Function.iterate_succ_apply']⟩
    hnodup := by
      have h1 : H :: p1 = (List.range (k + 1)).map (fun j => U^[j] H) := by
        rw [List.range_succ_eq_map, List.map_cons, List.map_map]
        simp [p1, uTail, Function.comp_def]
      have hnd1 : (H :: p1).Nodup := by
        rw [h1]; exact (List.nodup_range).map (U_iter_strictMono (by omega)).injective
      have hnd2 : p2.Nodup :=
        (List.nodup_range).map (U_iter_strictMono hd_pos).injective
      have hcons : H :: verts = (H :: p1) ++ p2 := rfl
      rw [hcons, List.nodup_append]
      refine ⟨hnd1, hnd2, ?_⟩
      intro a ha b hb
      rw [h1] at ha
      rcases List.mem_map.mp ha with ⟨j, _, rfl⟩
      rcases List.mem_map.mp hb with ⟨i, _, rfl⟩
      exact hdisj j i
    hgt := by
      intro x hx
      rcases List.mem_append.mp hx with hx1 | hx2
      · rcases List.mem_map.mp hx1 with ⟨j, _, rfl⟩
        exact U_iter_strictMono (by omega) (Nat.succ_pos j)
      · rcases List.mem_map.mp hx2 with ⟨i, _, rfl⟩
        have hge : d ≤ U^[i] d := (U_iter_strictMono hd_pos).monotone (Nat.zero_le i)
        omega
    hle := by
      intro x hx
      rcases List.mem_append.mp hx with hx1 | hx2
      · rcases List.mem_map.mp hx1 with ⟨j, hj, rfl⟩
        have hjk : j + 1 ≤ k := List.mem_range.mp hj
        have hle_y : U^[j + 1] H ≤ y := (U_iter_strictMono (by omega)).monotone hjk
        have hB_lt_H' : B < H' := by omega
        omega
      · rcases List.mem_map.mp hx2 with ⟨i, hi, rfl⟩
        have his : i ≤ s + 4 := Nat.lt_succ_iff.mp (List.mem_range.mp hi)
        rw [← hH'_eq]
        exact (U_iter_strictMono hd_pos).monotone his
    hgap := by
      intro x hx ⟨hlo, hhi⟩
      rcases List.mem_append.mp hx with hx1 | hx2
      · rcases List.mem_map.mp hx1 with ⟨j, hj, rfl⟩
        have hjk : j + 1 ≤ k := List.mem_range.mp hj
        have hle_y : U^[j + 1] H ≤ y := (U_iter_strictMono (by omega)).monotone hjk
        omega
      · rcases List.mem_map.mp hx2 with ⟨i, hi, rfl⟩
        by_cases hle1 : i ≤ s + 1
        · have : U^[i] d ≤ B := by
            rw [← hB_eq]; exact (U_iter_strictMono hd_pos).monotone hle1
          omega
        · have hge2 : s + 2 ≤ i := by omega
          have : C ≤ U^[i] d := by
            rw [← hC_eq]; exact (U_iter_strictMono hd_pos).monotone hge2
          omega
  }⟩

/-- Phase 2 from any odd vertex `w = U^[k] H > 5 * H` (`k ≥ 1`), terminating by strong induction
on `v₂(5 * ((w - 9) / 16) + 3)` for Subcase B3b. -/
private lemma stage_of_odd_above {H : ℕ} (hH : 5 ≤ H) :
    ∀ n : ℕ, ∀ k : ℕ, 1 ≤ k → (U^[k] H) % 2 = 1 → 5 * H < U^[k] H →
      v2 (5 * ((U^[k] H - 9) / 16) + 3) ≤ n → Nonempty (Stage H) := by
  intro n
  induction n using Nat.strong_induction_on with
  | ind n ih =>
    intro k hk hw_odd hw_gt hv2_le
    set w := U^[k] H with hw_def
    have hw_ge26 : 26 ≤ w := by omega
    by_cases hmod4 : w % 4 = 3
    · -- Case A: `w ≡ 3 (mod 4)`
      exact stage_of_pure_U hH (by rw [← hw_def]; exact hmod4)
        (by rw [← hw_def]; have := U_gt (x := w) (by omega); omega)
    · -- Case B: `w ≡ 1 (mod 4)`, write `w = 4 * m + 1`
      have hm_eq : w = 4 * (w / 4) + 1 := by omega
      let m := w / 4
      have hm_ge6 : 6 ≤ m := by omega
      have hy_eq : U^[k + 1] H = 6 * m + 2 := by
        rw [Function.iterate_succ_apply', ← hw_def]; unfold U; omega
      by_cases hm4_0 : m % 4 = 0
      · -- Subcase B1: `m = 4q`, `w = 16q + 1 → 24q + 2 → 36q + 3 ≡ 3 (mod 4)`
        have hA_eq : U^[k + 2] H = 9 * m + 3 := by
          rw [Function.iterate_succ_apply', hy_eq]; unfold U; omega
        have hA_mod : (U^[k + 2] H) % 4 = 3 := by omega
        have hB_gt : 5 * H < U (U^[k + 2] H) := by
          have := U_gt (x := U^[k + 2] H) (by omega); omega
        exact stage_of_pure_U hH hA_mod hB_gt
      · by_cases hm_odd : m % 2 = 1
        · -- Subcase B2: `m` odd, `3m + 1 = 2^e * u` with `e ≥ 1`, `u` odd
          have h3m_even : (3 * m + 1) % 2 = 0 := by omega
          let e := v2 (3 * m + 1)
          let u := oddPart (3 * m + 1)
          have heu : 2 ^ e * u = 3 * m + 1 := two_pow_v2_mul_oddPart (3 * m + 1)
          have hu_odd : u % 2 = 1 := oddPart_mod_two (by omega)
          have hu_pos : 1 ≤ u := oddPart_pos (by omega)
          have he_ge1 : 1 ≤ e := by
            have : 3 * m + 1 = 2 * ((3 * m + 1) / 2) := by omega
            have hv : v2 (3 * m + 1) = v2 ((3 * m + 1) / 2) + 1 := by
              conv_lhs => rw [this]
              exact v2_two_mul (by omega)
            dsimp [e]; omega
          have hy_pow : U^[k + 1] H = 2 ^ (e + 1) * u := by
            rw [hy_eq]; calc 6 * m + 2 = 2 * (3 * m + 1) := by omega
              _ = 2 * (2 ^ e * u) := by rw [heu]
              _ = 2 ^ (e + 1) * u := by ring
          have hpow_mod : (3 ^ (e + 1) * u) % 4 = 3 ∨ (3 ^ e * u) % 4 = 3 := by
            have h3e_odd : (3 ^ e) % 2 = 1 := by
              have : Odd (3 ^ e) := Odd.pow (by decide : Odd 3)
              exact Nat.odd_iff.mp this
            have h3eu_odd : (3 ^ e * u) % 2 = 1 := by rw [Nat.mul_mod, h3e_odd, hu_odd]
            have hnext : 3 ^ (e + 1) * u = 3 * (3 ^ e * u) := by ring
            omega
          rcases hpow_mod with hB2a | hB2b
          · -- Subcase B2a: pure `U`-steps from `y = 2^{e+1} u` to `3^{e+1} u ≡ 3 (mod 4)`
            have hreach : U^[k + 1 + (e + 1)] H = 3 ^ (e + 1) * u := by
              rw [add_comm (k + 1) (e + 1), Function.iterate_add_apply, hy_pow, U_iter_two_pow_mul]
            have hB_gt : 5 * H < U (U^[k + 1 + (e + 1)] H) := by
              have h1 : w < U^[k + 1 + (e + 1)] H :=
                U_iter_strictMono (by omega) (by omega)
              have h2 := U_gt (x := U^[k + 1 + (e + 1)] H) (by omega)
              omega
            exact stage_of_pure_U hH (by rw [hreach]; exact hB2a) hB_gt
          · -- Subcase B2b: one admissible `D`-step `y → d = 2^e * u`, then `e` `U`-steps to `3^e * u`
            have hy_mod6 : (U^[k + 1] H) % 6 = 2 := by omega
            have hd_eq : D (U^[k + 1] H) = 2 ^ e * u := by
              rw [hy_eq]; unfold D; omega
            have hd_gt : H < D (U^[k + 1] H) := by rw [hd_eq, heu]; omega
            have hA_eq : U^[e] (D (U^[k + 1] H)) = 3 ^ e * u := by
              rw [hd_eq, U_iter_two_pow_mul]
            have hB_gt_y : U^[k + 1] H < U (U^[e] (D (U^[k + 1] H))) := by
              rw [hA_eq, hy_pow]
              by_cases he1 : e = 1
              · rw [he1]; unfold U; omega
              · have hlt := two_pow_succ_lt_three_pow (by omega : 2 ≤ e)
                have hmul : 2 ^ (e + 1) * u < 3 ^ e * u := Nat.mul_lt_mul_of_pos_right hlt (by omega)
                have hU := U_gt (x := 3 ^ e * u) (Nat.mul_pos (Nat.one_le_pow _ _ (by decide)) hu_pos)
                omega
            have hB_gt_5H : 5 * H < U (U^[e] (D (U^[k + 1] H))) := by
              have : w < U^[k + 1] H := U_iter_strictMono (by omega) (by omega)
              omega
            exact stage_of_one_D hH (by omega) hy_mod6 hd_gt (by rw [hA_eq]; exact hB2b)
              hB_gt_y hB_gt_5H
        · -- Subcase B3: `m % 4 = 2`, so `w = 16q + 9` where `q = (w - 9) / 16`
          let q := (w - 9) / 16
          have hq_eq : w = 16 * q + 9 := by omega
          have hq_ge1 : 1 ≤ q := by omega
          by_cases hq_even : q % 2 = 0
          · -- Subcase B3a: `q = 2r` even, `w = 32r + 9 → y = 48r + 14 →_D d = 24r + 7 →_U A = 36r + 11`
            have hy_eq' : U^[k + 1] H = 24 * q + 14 := by
              rw [Function.iterate_succ_apply', ← hw_def]; unfold U; omega
            have hy_mod6 : (U^[k + 1] H) % 6 = 2 := by omega
            have hd_eq : D (U^[k + 1] H) = 12 * q + 7 := by rw [hy_eq']; unfold D; omega
            have hd_gt : H < D (U^[k + 1] H) := by omega
            have hA_eq : U^[1] (D (U^[k + 1] H)) = 18 * q + 11 := by
              simp only [Function.iterate_one, hd_eq]; unfold U; omega
            have hA_mod : (U^[1] (D (U^[k + 1] H))) % 4 = 3 := by omega
            have hB_eq : U (U^[1] (D (U^[k + 1] H))) = 27 * q + 17 := by
              rw [hA_eq]; unfold U; omega
            have hB_gt_y : U^[k + 1] H < U (U^[1] (D (U^[k + 1] H))) := by omega
            have hB_gt_5H : 5 * H < U (U^[1] (D (U^[k + 1] H))) := by omega
            exact stage_of_one_D hH (by omega) hy_mod6 hd_gt hA_mod hB_gt_y hB_gt_5H
          · -- Subcase B3b: `q` odd, two `U`-steps to `w' = 36q + 21`
            have hy_eq' : U^[k + 1] H = 24 * q + 14 := by
              rw [Function.iterate_succ_apply', ← hw_def]; unfold U; omega
            have hw'_eq : U^[k + 2] H = 36 * q + 21 := by
              rw [Function.iterate_succ_apply', hy_eq']; unfold U; omega
            by_cases hq4 : q % 4 = 3
            · -- `w' = 144r + 129 ≡ 1 (mod 16)` → immediately enters B1 (`+ 2` `U`-steps to `≡ 3 mod 4`)
              have hA_eq : U^[k + 4] H = 81 * q + 48 := by
                have h1 : U^[k + 3] H = 54 * q + 32 := by
                  rw [Function.iterate_succ_apply', hw'_eq]; unfold U; omega
                rw [Function.iterate_succ_apply', h1]; unfold U; omega
              have hA_mod : (U^[k + 4] H) % 4 = 3 := by omega
              have hB_gt : 5 * H < U (U^[k + 4] H) := by
                have := U_gt (x := U^[k + 4] H) (by omega); omega
              exact stage_of_pure_U hH hA_mod hB_gt
            · -- `q % 4 = 1`: `w' = 16 * q' + 9` with `4 * (5q' + 3) = 9 * (5q + 3)`
              let q' := (U^[k + 2] H - 9) / 16
              have hq'_rel : 4 * (5 * q' + 3) = 9 * (5 * q + 3) := by omega
              have hv2_drop : v2 (5 * q' + 3) + 2 = v2 (5 * q + 3) := by
                have hL : v2 (4 * (5 * q' + 3)) = v2 (5 * q' + 3) + 2 := by
                  have h4 : 4 * (5 * q' + 3) = 2 * (2 * (5 * q' + 3)) := by ring
                  rw [h4, v2_two_mul (by omega), v2_two_mul (by omega)]
                have hR : v2 (9 * (5 * q + 3)) = v2 (5 * q + 3) :=
                  v2_odd_mul (by decide) (by omega)
                rw [← hL, hq'_rel, hR]
              have hq_def : (U^[k] H - 9) / 16 = q := by rw [← hw_def]
              rw [hq_def] at hv2_le
              exact ih (v2 (5 * q' + 3)) (by omega) (k + 2) (by omega) (by omega) (by omega) le_rfl

/-- **Lemma 3 (Admissible Stage Extension):**
For every `H ≥ 5`, there exists a valid `Stage H`. -/
theorem admissible_stage_extension {H : ℕ} (hH : 5 ≤ H) : Nonempty (Stage H) := by
  -- Phase 1: 4 `U`-steps to `x₀ > 5 * H`, then `v2 x₀` `U`-steps to odd `w₀ ≥ x₀ > 5 * H`
  let x₀ := U^[4] H
  have hx₀_gt : 5 * H < x₀ := by
    have h1 : 3 * H ≤ 2 * U H := by unfold U; omega
    have h2 : 3 * U H ≤ 2 * U (U H) := by unfold U; omega
    have h3 : 3 * U (U H) ≤ 2 * U (U (U H)) := by unfold U; omega
    have h4 : 3 * U (U (U H)) ≤ 2 * U (U (U (U H))) := by unfold U; omega
    have hx4 : x₀ = U (U (U (U H))) := rfl
    omega
  let e₀ := v2 x₀
  let u₀ := oddPart x₀
  have hx₀_fac : 2 ^ e₀ * u₀ = x₀ := two_pow_v2_mul_oddPart x₀
  have hw₀_eq : U^[4 + e₀] H = 3 ^ e₀ * u₀ := by
    rw [add_comm 4 e₀, Function.iterate_add_apply]
    change U^[e₀] x₀ = 3 ^ e₀ * u₀
    rw [← hx₀_fac, U_iter_two_pow_mul]
  have hw₀_odd : (U^[4 + e₀] H) % 2 = 1 := by
    rw [hw₀_eq]
    have h3 : (3 ^ e₀) % 2 = 1 := Nat.odd_iff.mp (Odd.pow (by decide : Odd 3))
    have hu : u₀ % 2 = 1 := oddPart_mod_two (by omega)
    rw [Nat.mul_mod, h3, hu]
  have hw₀_gt : 5 * H < U^[4 + e₀] H := by
    have hle : x₀ ≤ U^[4 + e₀] H := (U_iter_strictMono (by omega)).monotone (by omega : 4 ≤ 4 + e₀)
    omega
  exact stage_of_odd_above hH (v2 (5 * ((U^[4 + e₀] H - 9) / 16) + 3)) (4 + e₀) (by omega)
    hw₀_odd hw₀_gt le_rfl

/-! ## Section 5: Global Ray Construction, Disjoint Trap Cycles, and Exact Orbit Type `(∞, 1)` -/

/-- Recursive sequence of heads `H_0 = 5`, `H_{m+1} = (stage m).H'`. -/
private noncomputable def stageHeadPair : ℕ → Σ H : ℕ, PLift (5 ≤ H)
  | 0 => ⟨5, ⟨le_rfl⟩⟩
  | m + 1 =>
    let prev := stageHeadPair m
    let st := Classical.choice (admissible_stage_extension prev.2.down)
    ⟨st.H', ⟨by have := st.hB_gt; have := st.hH'_gt; have := prev.2.down; omega⟩⟩

private noncomputable def headVal (m : ℕ) : ℕ := (stageHeadPair m).1

private lemma headVal_ge5 (m : ℕ) : 5 ≤ headVal m := (stageHeadPair m).2.down

private noncomputable def stageAt (m : ℕ) : Stage (headVal m) :=
  Classical.choice (admissible_stage_extension (headVal_ge5 m))

private lemma headVal_zero : headVal 0 = 5 := rfl

private lemma headVal_succ (m : ℕ) : headVal (m + 1) = (stageAt m).H' := rfl

private lemma headVal_lt_B (m : ℕ) : 5 * headVal m < (stageAt m).B := (stageAt m).hB_gt

private lemma B_lt_headVal_succ (m : ℕ) : 3 * (stageAt m).B < headVal (m + 1) := (stageAt m).hH'_gt

private lemma headVal_strictMono : StrictMono headVal := by
  refine strictMono_nat_of_lt_succ fun m => ?_
  have h1 := headVal_lt_B m
  have h2 := B_lt_headVal_succ m
  have h3 := headVal_ge5 m
  omega

/-- Segment `0` is `[1, 2, 3, 5]`; segment `m + 1` is `(stageAt m).verts`. -/
private noncomputable def seg (m : ℕ) : List ℕ :=
  match m with
  | 0 => [1, 2, 3, 5]
  | m + 1 => (stageAt m).verts

private lemma seg_ne_nil (m : ℕ) : seg m ≠ [] := by
  cases m with
  | zero => simp [seg]
  | succ m => exact (stageAt m).hnonempty

private lemma seg_len_pos (m : ℕ) : 0 < (seg m).length :=
  List.length_pos_of_ne_nil (seg_ne_nil m)

private lemma seg_last (m : ℕ) : (seg m).getLast (seg_ne_nil m) = headVal m := by
  cases m with
  | zero => rfl
  | succ m => exact (stageAt m).hlast

/-- Cumulative start index of segment `m` in the infinite ray `raySeq`. -/
private noncomputable def cumLen : ℕ → ℕ
  | 0 => 0
  | m + 1 => cumLen m + (seg m).length

private lemma cumLen_strictMono : StrictMono cumLen :=
  strictMono_nat_of_lt_succ fun m => by
    change cumLen m < cumLen m + (seg m).length
    have := seg_len_pos m; omega

private lemma exists_seg_idx (t : ℕ) :
    ∃ m : ℕ, cumLen m ≤ t ∧ t < cumLen (m + 1) := by
  have hbound : ∃ M : ℕ, t < cumLen M := ⟨t + 1, by
    have hle := cumLen_strictMono.id_le (t + 1)
    simp only [id_eq] at hle
    omega⟩
  let M := Nat.find hbound
  have hM : t < cumLen M := Nat.find_spec hbound
  cases hMeq : M with
  | zero =>
    rw [hMeq] at hM; simp [cumLen] at hM
  | succ m =>
    have hprev : ¬ (t < cumLen m) := Nat.find_min hbound (by omega)
    exact ⟨m, by omega, by rwa [← hMeq]⟩

private lemma seg_idx_unique {t m₁ m₂ : ℕ}
    (h1 : cumLen m₁ ≤ t ∧ t < cumLen (m₁ + 1))
    (h2 : cumLen m₂ ≤ t ∧ t < cumLen (m₂ + 1)) : m₁ = m₂ := by
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · have : cumLen (m₁ + 1) ≤ cumLen m₂ := cumLen_strictMono.monotone (by omega)
    omega
  · have : cumLen (m₂ + 1) ≤ cumLen m₁ := cumLen_strictMono.monotone (by omega)
    omega

/-- The infinite admissible ray `r : ℕ → ℕ` obtained by concatenating `seg 0, seg 1, seg 2, ...`. -/
private noncomputable def raySeq (t : ℕ) : ℕ :=
  let m := Classical.choose (exists_seg_idx t)
  have hm := Classical.choose_spec (exists_seg_idx t)
  (seg m)[t - cumLen m]'(by
    have h1 : cumLen m ≤ t := hm.1
    have h2 : t < cumLen m + (seg m).length := hm.2
    omega)

private lemma raySeq_eq {t m : ℕ} (h1 : cumLen m ≤ t) (h2 : t < cumLen (m + 1)) :
    raySeq t = (seg m)[t - cumLen m]'(by have h2' : t < cumLen m + (seg m).length := h2; omega) := by
  unfold raySeq
  have heq : Classical.choose (exists_seg_idx t) = m :=
    seg_idx_unique (Classical.choose_spec (exists_seg_idx t)) ⟨h1, h2⟩
  subst heq
  rfl

private lemma raySeq_zero : raySeq 0 = 1 := by
  rw [raySeq_eq (t := 0) (m := 0) (by simp [cumLen]) (by simp [cumLen, seg])]
  rfl

private lemma raySeq_admissible (t : ℕ) : AdmissibleStep (raySeq t) (raySeq (t + 1)) := by
  obtain ⟨m, h1, h2⟩ := exists_seg_idx t
  rw [raySeq_eq h1 h2]
  by_cases hlt : t + 1 < cumLen (m + 1)
  · rw [raySeq_eq (by omega) hlt]
    have hidx : t + 1 - cumLen m = (t - cumLen m) + 1 := by omega
    simp only [hidx]
    cases m with
    | zero =>
      have ht : t = 0 ∨ t = 1 ∨ t = 2 := by
        have hlt' : t + 1 < 4 := by simpa [cumLen, seg] using hlt
        omega
      rcases ht with rfl | rfl | rfl <;> (left; simp [cumLen, seg, U])
    | succ m =>
      exact (stageAt m).hsteps (t - cumLen (m + 1)) (by
        have hlt' : t + 1 < cumLen (m + 1) + (stageAt m).verts.length := hlt; omega)
  · have hEq : t + 1 = cumLen (m + 1) := by omega
    have hnext : t + 1 < cumLen (m + 2) := by
      change t + 1 < cumLen (m + 1) + (seg (m + 1)).length
      have := seg_len_pos (m + 1); omega
    rw [raySeq_eq (by omega) hnext]
    have hlast_idx : (seg m)[t - cumLen m]'(by have h2' : t < cumLen m + (seg m).length := h2; omega) =
        headVal m := by
      rw [← seg_last m, List.getLast_eq_getElem]
      congr 1
      have hEq' : t + 1 = cumLen m + (seg m).length := hEq
      omega
    have hfirst_idx : (seg (m + 1))[t + 1 - cumLen (m + 1)]'(by
        have hnext' : t + 1 < cumLen (m + 1) + (seg (m + 1)).length := hnext; omega) =
        (stageAt m).verts.head (stageAt m).hnonempty := by
      rw [List.head_eq_getElem]
      simp [seg, hEq]
    rw [hlast_idx, hfirst_idx]
    exact (stageAt m).hfirst

private lemma seg_bounds {m x : ℕ} (hx : x ∈ seg m) :
    (m = 0 → 1 ≤ x ∧ x ≤ headVal 0) ∧
    (∀ k, m = k + 1 → headVal k < x ∧ x ≤ headVal (k + 1)) := by
  constructor
  · rintro rfl
    simp only [seg, List.mem_cons, List.not_mem_nil, or_false] at hx
    rw [headVal_zero]
    rcases hx with rfl | rfl | rfl | rfl <;> omega
  · rintro k rfl
    exact ⟨(stageAt k).hgt x hx, (stageAt k).hle x hx⟩

private lemma seg_nodup (m : ℕ) : (seg m).Nodup := by
  cases m with
  | zero => decide
  | succ k => exact ((List.nodup_cons.mp (stageAt k).hnodup).2)

private lemma raySeq_injective : Function.Injective raySeq := by
  intro t₁ t₂ hEq
  obtain ⟨m₁, h1a, h1b⟩ := exists_seg_idx t₁
  obtain ⟨m₂, h2a, h2b⟩ := exists_seg_idx t₂
  rw [raySeq_eq h1a h1b, raySeq_eq h2a h2b] at hEq
  have hm_eq : m₁ = m₂ := by
    by_contra hne
    have hseg_lt : ∀ {a b : ℕ} {x : ℕ}, a < b → x ∈ seg a → x ∈ seg b → False := by
      intro a b x hlt hxa hxb
      have hx1_le : x ≤ headVal a := by
        cases a with
        | zero => exact ((seg_bounds hxa).1 rfl).2
        | succ k => exact ((seg_bounds hxa).2 k rfl).2
      obtain ⟨kb, rfl⟩ : ∃ kb, b = kb + 1 := ⟨b - 1, by omega⟩
      have hx2_gt : headVal kb < x := ((seg_bounds hxb).2 kb rfl).1
      have hmono : headVal a ≤ headVal kb := headVal_strictMono.monotone (by omega)
      omega
    have hx1_mem : (seg m₁)[t₁ - cumLen m₁]'(by have h1b' : t₁ < cumLen m₁ + (seg m₁).length := h1b; omega) ∈ seg m₁ :=
      List.getElem_mem _
    have hx2_mem : (seg m₂)[t₂ - cumLen m₂]'(by have h2b' : t₂ < cumLen m₂ + (seg m₂).length := h2b; omega) ∈ seg m₂ :=
      List.getElem_mem _
    rcases lt_or_gt_of_ne hne with hlt | hgt
    · exact hseg_lt hlt hx1_mem (hEq ▸ hx2_mem)
    · exact hseg_lt hgt hx2_mem (hEq.symm ▸ hx1_mem)
  subst hm_eq
  have hidx_eq : t₁ - cumLen m₁ = t₂ - cumLen m₁ :=
    (List.Nodup.getElem_inj_iff (seg_nodup m₁)).mp hEq
  omega

private lemma raySeq_gap (m : ℕ) :
    ∀ x : ℕ, (stageAt m).B + 1 ≤ x → x ≤ U (stageAt m).B - 1 → x ∉ Set.range raySeq := by
  intro x hlo hhi ⟨t, ht⟩
  obtain ⟨j, hj1, hj2⟩ := exists_seg_idx t
  rw [raySeq_eq hj1 hj2] at ht
  have hx_mem : x ∈ seg j := by rw [← ht]; exact List.getElem_mem _
  by_cases hlt : j ≤ m
  · have hx_le : x ≤ headVal j := by
      cases j with
      | zero => exact ((seg_bounds hx_mem).1 rfl).2
      | succ k => exact ((seg_bounds hx_mem).2 k rfl).2
    have hjm : headVal j ≤ headVal m := headVal_strictMono.monotone hlt
    have hBm := headVal_lt_B m
    have h5 := headVal_ge5 m
    omega
  · by_cases heq : j = m + 1
    · subst heq
      exact (stageAt m).hgap x hx_mem ⟨hlo, hhi⟩
    · obtain ⟨k, rfl⟩ : ∃ k, j = k + 1 := ⟨j - 1, by omega⟩
      have hx_gt : headVal k < x := ((seg_bounds hx_mem).2 k rfl).1
      have hmk : headVal (m + 1) ≤ headVal k := headVal_strictMono.monotone (by omega)
      have h3B := B_lt_headVal_succ m
      have hUB : 2 * U (stageAt m).B = 3 * (stageAt m).B + 1 := by
        have := (stageAt m).hB_mod; unfold U; omega
      omega

/-- **Main Theorem (Affirmative Answer to Vasilyev `arXiv:2611.20344v2` Question 7.3 & Remark 4.4):**
There exists `S ⊆ ℕ₊` such that the up-down map `T_S` has:
1. A divergent orbit starting at `1` (`IsDivergentOrbit (T S) 1` and `Tendsto (T S)^[·] 1 atTop atTop`);
2. Infinitely many pairwise disjoint cycles `cyc : ℕ → ℕ` (all of length `≥ 2`, all disjoint from
   `Orbit (T S) 1`);
3. Exact orbit type `(k, l) = (∞, 1)` (every `x ≥ 1` either eventually enters some cycle `cyc m`
   or eventually coincides with the divergent orbit of `1`). -/
theorem vasilyev_question_7_3_orbit_type_infty_one :
    ∃ (S : Set ℕ) (cyc : ℕ → ℕ),
      (∀ x ∈ S, 1 ≤ x) ∧
      IsDivergentOrbit (T S) 1 ∧
      Filter.Tendsto (fun t => (T S)^[t] 1) Filter.atTop Filter.atTop ∧
      (∀ m : ℕ, 1 ≤ cyc m ∧ IsPeriodicPoint (T S) (cyc m) ∧ T S (cyc m) ≠ cyc m) ∧
      Pairwise (fun m₁ m₂ => Disjoint (Orbit (T S) (cyc m₁)) (Orbit (T S) (cyc m₂))) ∧
      (∀ m : ℕ, Disjoint (Orbit (T S) (cyc m)) (Orbit (T S) 1)) ∧
      (∀ x : ℕ, 1 ≤ x →
        (∃ m t : ℕ, (T S)^[t] x ∈ Orbit (T S) (cyc m)) ∨ EventuallyCoincide (T S) x 1) := by
  let R : Set ℕ := Set.range raySeq
  have hR_Uinv : ∀ x : ℕ, 1 ≤ x → x ∉ R → U x ∉ R :=
    admissible_ray_U_inv raySeq_zero raySeq_admissible
  -- Apply Lemma 1 (`closed_box_trap`) at each anchor `B_m = (stageAt m).B`
  have htrap : ∀ m : ℕ,
      ∃ c : ℕ, IsPeriodicPoint (trapMap (stageAt m).B) c ∧
        (∀ y ∈ Orbit (trapMap (stageAt m).B) c,
          (stageAt m).B + 1 ≤ y ∧ y ≤ 3 * (stageAt m).B - 1 ∧
          y ∉ R ∧ y ≠ 2 * (stageAt m).B ∧ trapMap (stageAt m).B y ≠ y) := fun m =>
    closed_box_trap
      (by have := headVal_ge5 m; have := headVal_lt_B m; omega)
      (stageAt m).hB_mod
      hR_Uinv
      (raySeq_gap m)
  let cyc : ℕ → ℕ := fun m => Classical.choose (htrap m)
  have hcyc_per : ∀ m, IsPeriodicPoint (trapMap (stageAt m).B) (cyc m) :=
    fun m => (Classical.choose_spec (htrap m)).1
  have hcyc_box : ∀ m y, y ∈ Orbit (trapMap (stageAt m).B) (cyc m) →
      (stageAt m).B + 1 ≤ y ∧ y ≤ 3 * (stageAt m).B - 1 ∧
      y ∉ R ∧ y ≠ 2 * (stageAt m).B ∧ trapMap (stageAt m).B y ≠ y :=
    fun m => (Classical.choose_spec (htrap m)).2
  -- Trap intervals `[B_m + 1, 3 B_m - 1]` are strictly separated
  have hbox_lt : ∀ m₁ m₂ : ℕ, m₁ < m₂ → 3 * (stageAt m₁).B - 1 < (stageAt m₂).B + 1 := by
    intro m₁ m₂ hlt
    have h1 := B_lt_headVal_succ m₁
    have h2 : headVal (m₁ + 1) ≤ headVal m₂ := headVal_strictMono.monotone (by omega)
    have h3 := headVal_lt_B m₂
    have h4 := headVal_ge5 m₂
    omega
  have hbox_disj : ∀ m₁ m₂ y, m₁ ≠ m₂ →
      y ∈ Orbit (trapMap (stageAt m₁).B) (cyc m₁) →
      y ∉ Orbit (trapMap (stageAt m₂).B) (cyc m₂) := by
    intro m₁ m₂ y hne h1 h2
    have hb1 := hcyc_box m₁ y h1
    have hb2 := hcyc_box m₂ y h2
    rcases lt_or_gt_of_ne hne with hlt | hgt
    · have := hbox_lt m₁ m₂ hlt; omega
    · have := hbox_lt m₂ m₁ hgt; omega
  -- Define `S` explicitly: ray `U`-steps union cycle `U`-steps
  let S : Set ℕ :=
    { x | (∃ t : ℕ, raySeq t = x ∧ raySeq (t + 1) = U x) ∨
          (∃ m : ℕ, x ∈ Orbit (trapMap (stageAt m).B) (cyc m) ∧ x ≤ 2 * (stageAt m).B - 1) }
  have hS_pos : ∀ x ∈ S, 1 ≤ x := by
    rintro x (⟨t, rfl, _⟩ | ⟨m, hmem, _⟩)
    · cases t with
      | zero => rw [raySeq_zero]
      | succ t => exact admissibleStep_pos (raySeq_admissible t)
    · have := (hcyc_box m x hmem).1; omega
  -- `T S` agrees with `raySeq` on `R`
  have hT_ray : ∀ t : ℕ, T S (raySeq t) = raySeq (t + 1) := by
    intro t
    have hstep := raySeq_admissible t
    unfold T
    split_ifs with hmem
    · rcases hmem with ⟨t', ht', hU⟩ | ⟨m, hc, _⟩
      · have heq : t' = t := raySeq_injective ht'
        rw [← heq, hU, ht']
      · exact absurd ⟨t, rfl⟩ (hcyc_box m (raySeq t) hc).2.2.1
    · rcases hstep with ⟨_, hU⟩ | ⟨_, _, hD⟩
      · exact absurd (Or.inl ⟨t, rfl, hU⟩) hmem
      · exact hD.symm
  have hT_iter_one : ∀ t : ℕ, (T S)^[t] 1 = raySeq t := by
    intro t
    induction t with
    | zero => simp [raySeq_zero]
    | succ t ih => rw [Function.iterate_succ_apply', ih, hT_ray]
  -- `T S` agrees with `trapMap (stageAt m).B` on each cycle `Orbit (trapMap B_m) (cyc m)`
  have hT_cyc : ∀ m y, y ∈ Orbit (trapMap (stageAt m).B) (cyc m) →
      T S y = trapMap (stageAt m).B y := by
    intro m y hy
    unfold T trapMap
    by_cases hle : y ≤ 2 * (stageAt m).B - 1
    · have hS : y ∈ S := Or.inr ⟨m, hy, hle⟩
      simp [hS, hle]
    · have hnotS : y ∉ S := by
        rintro (⟨t, ht, _⟩ | ⟨m', hy', hle'⟩)
        · exact (hcyc_box m y hy).2.2.1 ⟨t, ht⟩
        · have hm : m' = m := by
            by_contra hne; exact hbox_disj m' m y hne hy' hy
          subst hm; exact hle hle'
      simp [hnotS, hle]
  have hT_iter_cyc : ∀ m k, (T S)^[k] (cyc m) = (trapMap (stageAt m).B)^[k] (cyc m) := by
    intro m k
    induction k with
    | zero => rfl
    | succ k ih =>
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih]
      exact hT_cyc m _ ⟨k, rfl⟩
  have hOrb_cyc_eq : ∀ m, Orbit (T S) (cyc m) = Orbit (trapMap (stageAt m).B) (cyc m) := by
    intro m; ext y; simp only [Orbit, Set.mem_ofPred_eq, hT_iter_cyc]
  have hOrb_one_eq : Orbit (T S) 1 = R := by
    ext y; simp only [Orbit, R, Set.mem_ofPred_eq, Set.mem_range, hT_iter_one]
  -- Every `x ∉ R ∪ ⋃ m, C_m` with `x ≥ 1` has `x ≥ 2` and `T S x = D x < x`
  have hdescent : ∀ x : ℕ, 1 ≤ x →
      (∃ m t : ℕ, (T S)^[t] x ∈ Orbit (T S) (cyc m)) ∨ EventuallyCoincide (T S) x 1 := by
    intro x hx
    induction x using Nat.strong_induction_on with
    | ind x ih =>
      by_cases hR : x ∈ R
      · right
        rcases hR with ⟨j, hj⟩
        exact ⟨0, j, by simp [hT_iter_one, hj]⟩
      · by_cases hC : ∃ m, x ∈ Orbit (T S) (cyc m)
        · left
          rcases hC with ⟨m, hm⟩
          exact ⟨m, 0, hm⟩
        · have hx_notS : x ∉ S := by
            rintro (⟨t, ht, _⟩ | ⟨m, hm, _⟩)
            · exact hR ⟨t, ht⟩
            · exact hC ⟨m, (hOrb_cyc_eq m).symm ▸ hm⟩
          have hx_ge2 : 2 ≤ x := by
            by_contra hlt
            have hx1 : x = 1 := by omega
            exact hR ⟨0, raySeq_zero.trans hx1.symm⟩
          have hTx : T S x = D x := by unfold T; simp [hx_notS]
          have hDx_lt : D x < x := D_lt hx_ge2
          have hDx_pos : 1 ≤ D x := D_pos hx
          rcases ih (D x) hDx_lt hDx_pos with ⟨m, t, ht⟩ | ⟨i, j, hij⟩
          · left
            refine ⟨m, t + 1, ?_⟩
            rw [Function.iterate_succ_apply, hTx]
            exact ht
          · right
            refine ⟨i + 1, j, ?_⟩
            rw [Function.iterate_succ_apply, hTx]
            exact hij
  -- `Tendsto (T S)^[·] 1 atTop atTop` from injectivity of `raySeq`
  have htend : Filter.Tendsto (fun t => (T S)^[t] 1) Filter.atTop Filter.atTop := by
    rw [Filter.tendsto_atTop_atTop]
    intro M
    -- Since `raySeq` is injective, the preimage of `{0, ..., M}` is finite!
    have hfin : (raySeq ⁻¹' Set.Iic M).Finite :=
      (Set.finite_Iic M).preimage raySeq_injective.injOn
    obtain ⟨N, hN⟩ : ∃ N : ℕ, ∀ t ∈ hfin.toFinset, t < N :=
      ⟨hfin.toFinset.sup id + 1, fun t ht => Nat.lt_succ_of_le (Finset.le_sup (f := id) ht)⟩
    refine ⟨N, fun t ht => ?_⟩
    rw [hT_iter_one]
    by_contra hlt
    have hmem : t ∈ hfin.toFinset := hfin.mem_toFinset.mpr (show raySeq t ≤ M by omega)
    have := hN t hmem
    omega
  refine ⟨S, cyc, hS_pos, ?_, htend, ?_, ?_, ?_, hdescent⟩
  · -- Divergent orbit of `1`
    intro t₁ t₂ h
    dsimp only at h
    rw [hT_iter_one, hT_iter_one] at h
    exact raySeq_injective h
  · -- Each `cyc m` is a cycle of `T S` of length `≥ 2` in `ℕ₊`
    intro m
    have hself : cyc m ∈ Orbit (trapMap (stageAt m).B) (cyc m) := ⟨0, rfl⟩
    have hbox := hcyc_box m (cyc m) hself
    refine ⟨by omega, ?_, ?_⟩
    · rcases hcyc_per m with ⟨k, hk1, hk⟩
      exact ⟨k, hk1, by rw [hT_iter_cyc, hk]⟩
    · rw [hT_cyc m (cyc m) hself]
      exact hbox.2.2.2.2
  · -- Pairwise disjoint cycles
    intro m₁ m₂ hne
    rw [hOrb_cyc_eq, hOrb_cyc_eq, Set.disjoint_left]
    intro y hy1 hy2
    exact hbox_disj m₁ m₂ y hne hy1 hy2
  · -- Every cycle is disjoint from the divergent orbit of `1`
    intro m
    rw [hOrb_cyc_eq, hOrb_one_eq, Set.disjoint_left]
    intro y hyC hyR
    exact (hcyc_box m y hyC).2.2.1 hyR

/-- **Direct Affirmative Resolution of Vasilyev (`arXiv:2611.20344v2`, Question 7.3 `q:types`):**
There exists a subset `S ⊆ ℕ₊` such that `T_S` has infinitely many pairwise disjoint cycles
and a divergent orbit. -/
theorem vasilyev_question_7_3 :
    ∃ (S : Set ℕ) (cyc : ℕ → ℕ) (x₀ : ℕ),
      (∀ x ∈ S, 1 ≤ x) ∧
      1 ≤ x₀ ∧ IsDivergentOrbit (T S) x₀ ∧
      (∀ m : ℕ, 1 ≤ cyc m ∧ IsPeriodicPoint (T S) (cyc m)) ∧
      Pairwise (fun m₁ m₂ => Disjoint (Orbit (T S) (cyc m₁)) (Orbit (T S) (cyc m₂))) := by
  obtain ⟨S, cyc, hS, hdiv, _, hcyc, hdisj, _, _⟩ := vasilyev_question_7_3_orbit_type_infty_one
  exact ⟨S, cyc, 1, hS, le_rfl, hdiv, fun m => ⟨(hcyc m).1, (hcyc m).2.1⟩, hdisj⟩

#print axioms closed_box_trap
#print axioms admissible_ray_U_inv
#print axioms admissible_stage_extension
#print axioms vasilyev_question_7_3_orbit_type_infty_one
#print axioms vasilyev_question_7_3

end OpenMath.Vasilyev261120344Q73
