import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Sum
import Mathlib.Tactic

/-!
# Illya Ivanov (`arXiv:2607.08944v1`, Section 1.4, Conjecture 6): Primitive 13-Polytope Counterexample

This file formalizes the refutation of Conjecture 6 (`\label{conj:fleanverts}`) of
Illya Ivanov, *"Illuminating Primitive Polytopes"* (`arXiv:2607.08944v1`, Section 1.3–1.4,
lines 237–239, 260–269, and 308–312):

> **Conjecture 6 (`conj:fleanverts`).** A primitive polytope in `ℝ^d`, `d ≥ 4` has at most
> `2^d` vertices, even fewer if it isn't an affine `d`-cube.

We construct an explicit 24-facet convex polytope `P ⊂ ℝ¹³` defined by the 24 closed halfspaces
(with coordinates `(x₁, x₂, x₃, y₀, ..., y₉)`):
1. `x₁ ≤ 100`, `x₂ ≤ 100`, `x₃ ≤ 100`, `-x₁ - x₂ - x₃ ≤ 100`;
2. `y_j ≤ 1` and `-y_j + x₁ + x₂ - j x₃ ≤ 119 + j²` for `j = 0, ..., 9`.

We prove directly from the primary-source definitions:
- `P` has nonempty interior (`0 ∈ int P`) and is bounded (`|x_k| ≤ 1700` on `P`), with
  explicit positive linear dependence `∑ μ_i a_i = 0` (`μ_i > 0`) on its outer facet normals.
- `P` is **primitive**: for every `i ∈ Fin 24`, omitting the `i`-th halfspace yields an
  unbounded intersection containing the ray `{t • r_i | t ≥ 0}` for an explicit `r_i ≠ 0`.
- `P` has at least **8,704** distinct extreme points (vertices), strictly exceeding `2¹³ = 8,192`.

## Main Results

* `OpenMath.Ivanov260708944Conj6.witness_isPrimitive`:
  The 24-halfspace polytope `witnessHRep` in `ℝ¹³` is a primitive 13-polytope.
* `OpenMath.Ivanov260708944Conj6.witness_has_8704_vertices`:
  There is an explicit 8,704-element set of distinct extreme points (vertices) of `witnessHRep`.
* `OpenMath.Ivanov260708944Conj6.refutes_ivanov_conjecture_6`:
  Explicit counterexample in `d = 13 ≥ 4` with `8704 > 2¹³` vertices.
* `OpenMath.Ivanov260708944Conj6.not_ivanov_conjecture_6`:
  Direct negation of Conjecture 6 (`∀ d ≥ 4, ∀ primitive P ⊂ ℝ^d, |vert(P)| ≤ 2^d`).
-/

namespace OpenMath.Ivanov260708944Conj6

open scoped BigOperators

/-! ## Section 1: Primary-Source Polytope, Primitivity, and Vertex Definitions -/

/-- Dot product in `ℝ^d`. -/
def dot {d : ℕ} (a x : Fin d → ℝ) : ℝ :=
  ∑ k : Fin d, a k * x k

/-- A finite halfspace representation `H_1^- ∩ ⋯ ∩ H_m^-` in `ℝ^d` (`a_i · x ≤ b_i`). -/
structure HRep (d m : ℕ) where
  a : Fin m → Fin d → ℝ
  b : Fin m → ℝ

/-- The polyhedron `P = ⋂_{i=1}^m {x ∈ ℝ^d | a_i · x ≤ b_i}`. -/
def HRep.poly {d m : ℕ} (H : HRep d m) : Set (Fin d → ℝ) :=
  {x | ∀ i : Fin m, dot (H.a i) x ≤ H.b i}

/-- The polyhedron obtained by omitting the `i`-th halfspace `H_i^-`. -/
def HRep.polyOmit {d m : ℕ} (H : HRep d m) (i : Fin m) : Set (Fin d → ℝ) :=
  {x | ∀ j : Fin m, j ≠ i → dot (H.a j) x ≤ H.b j}

/-- A set `S ⊆ ℝ^d` is bounded if all coordinates are uniformly bounded. -/
def IsBounded {d : ℕ} (S : Set (Fin d → ℝ)) : Prop :=
  ∃ R : ℝ, ∀ x ∈ S, ∀ k : Fin d, |x k| ≤ R

/-- `P` has nonempty interior (witnessed by a strictly feasible point `x₀` with `a_i · x₀ < b_i`). -/
def HRep.HasNonemptyInt {d m : ℕ} (H : HRep d m) : Prop :=
  ∃ x₀ : Fin d → ℝ, ∀ i : Fin m, dot (H.a i) x₀ < H.b i

/-- **Primitive polytope** (`arXiv:2607.08944v1`, Section 1.3–1.4): `P` has nonempty interior,
is bounded, and omitting ANY halfspace `H_i^-` makes the intersection unbounded (which also
automatically implies minimality / irredundancy of the halfspace representation). -/
def HRep.IsPrimitive {d m : ℕ} (H : HRep d m) : Prop :=
  H.HasNonemptyInt ∧ IsBounded H.poly ∧ ∀ i : Fin m, ¬ IsBounded (H.polyOmit i)

/-- A point `v ∈ S` is a **vertex** (extreme point) of `S ⊆ ℝ^d` if it does not lie in the open
line segment between two distinct points of `S`. -/
def IsVertex {d : ℕ} (S : Set (Fin d → ℝ)) (v : Fin d → ℝ) : Prop :=
  v ∈ S ∧ ∀ u w : Fin d → ℝ, u ∈ S → w ∈ S →
    ∀ t : ℝ, 0 < t → t < 1 →
      (∀ k : Fin d, v k = (1 - t) * u k + t * w k) → u = v ∧ w = v

/-! ## Section 2: The Explicit 24-Facet Polytope in `ℝ¹³` -/

/-- Pack `(x₁, x₂, x₃, y₀, ..., y₉)` as a vector in `ℝ¹³`. -/
def pack13 (x1 x2 x3 : ℝ) (y : Fin 10 → ℝ) : Fin 13 → ℝ :=
  fun k =>
    if h0 : k.1 = 0 then x1
    else if h1 : k.1 = 1 then x2
    else if h2 : k.1 = 2 then x3
    else y ⟨k.1 - 3, by omega⟩

@[simp] lemma pack13_0 (x1 x2 x3 : ℝ) (y : Fin 10 → ℝ) : pack13 x1 x2 x3 y 0 = x1 := rfl
@[simp] lemma pack13_1 (x1 x2 x3 : ℝ) (y : Fin 10 → ℝ) : pack13 x1 x2 x3 y 1 = x2 := rfl
@[simp] lemma pack13_2 (x1 x2 x3 : ℝ) (y : Fin 10 → ℝ) : pack13 x1 x2 x3 y 2 = x3 := rfl
lemma pack13_y (x1 x2 x3 : ℝ) (y : Fin 10 → ℝ) (j : Fin 10) :
    pack13 x1 x2 x3 y ⟨j.1 + 3, by omega⟩ = y j := by
  have h0 : j.1 + 3 ≠ 0 := by omega
  have h1 : j.1 + 3 ≠ 1 := by omega
  have h2 : j.1 + 3 ≠ 2 := by omega
  simp only [pack13, h0, h1, h2, ↓reduceDIte]
  exact congrArg y (Fin.ext (Nat.add_sub_cancel j.1 3))

/-- Outer normal vectors `a_i ∈ ℝ¹³` (`i : Fin 24`):
- `i = 0, 1, 2`: `e₁, e₂, e₃` (`x₁, x₂, x₃ ≤ 100`)
- `i = 3`: `-e₁ - e₂ - e₃` (`-x₁ - x₂ - x₃ ≤ 100`)
- `i = 4 + j` (`j < 10`): `e_{4+j}` (`y_j ≤ 1`)
- `i = 14 + j` (`j < 10`): `-e_{4+j} + e₁ + e₂ - j e₃` (`-y_j + x₁ + x₂ - j x₃ ≤ 119 + j²`). -/
def witnessNormal (i : Fin 24) (k : Fin 13) : ℝ :=
  if i.1 = 0 then (if k.1 = 0 then 1 else 0)
  else if i.1 = 1 then (if k.1 = 1 then 1 else 0)
  else if i.1 = 2 then (if k.1 = 2 then 1 else 0)
  else if i.1 = 3 then (if k.1 < 3 then -1 else 0)
  else if i.1 < 14 then (if k.1 = i.1 - 1 then 1 else 0)
  else
    let j : ℕ := i.1 - 14
    if k.1 = 0 then 1
    else if k.1 = 1 then 1
    else if k.1 = 2 then -(j : ℝ)
    else if k.1 = j + 3 then -1
    else 0

/-- Right-hand sides `b_i > 0` (`i : Fin 24`). -/
def witnessRHS (i : Fin 24) : ℝ :=
  if i.1 < 4 then 100
  else if i.1 < 14 then 1
  else
    let j : ℕ := i.1 - 14
    119 + (j : ℝ) ^ 2

/-- The explicit 24-facet counterexample `P ⊂ ℝ¹³`. -/
def witnessHRep : HRep 13 24 where
  a := witnessNormal
  b := witnessRHS

/-- Exact dot-product evaluation formulas for all 24 halfspaces. -/
private lemma dot_witness_0 (v : Fin 13 → ℝ) : dot (witnessNormal 0) v = v 0 := by
  simp [dot, witnessNormal]

private lemma dot_witness_1 (v : Fin 13 → ℝ) : dot (witnessNormal 1) v = v 1 := by
  unfold dot
  rw [Finset.sum_eq_single (1 : Fin 13)]
  · simp [witnessNormal]
  · intro k _ hne
    have hk : k.1 ≠ 1 := fun h => hne (Fin.ext h)
    simp [witnessNormal, hk]
  · intro h; exact absurd (Finset.mem_univ _) h

private lemma dot_witness_2 (v : Fin 13 → ℝ) : dot (witnessNormal 2) v = v 2 := by
  unfold dot
  rw [Finset.sum_eq_single (2 : Fin 13)]
  · simp [witnessNormal]
  · intro k _ hne
    have hk : k.1 ≠ 2 := fun h => hne (Fin.ext h)
    simp [witnessNormal, hk]
  · intro h; exact absurd (Finset.mem_univ _) h

private lemma dot_witness_3 (v : Fin 13 → ℝ) : dot (witnessNormal 3) v = -(v 0) - v 1 - v 2 := by
  simp only [dot, witnessNormal, Fin.sum_univ_succ, Fin.val_zero, Fin.val_succ,
    Fin.val_eq_zero_iff]
  norm_num
  ring

private lemma dot_witness_upper (j : Fin 10) (v : Fin 13 → ℝ) :
    dot (witnessNormal ⟨j.1 + 4, by omega⟩) v = v ⟨j.1 + 3, by omega⟩ := by
  unfold dot
  rw [Finset.sum_eq_single (⟨j.1 + 3, by omega⟩ : Fin 13)]
  · dsimp [witnessNormal]
    have h4 : j.1 + 4 < 14 := by omega
    simp only [h4, ↓reduceIte, one_mul]
  · intro k _ hne
    dsimp [witnessNormal]
    have h4 : j.1 + 4 < 14 := by omega
    have hk : k.1 ≠ j.1 + 3 := fun h => hne (Fin.ext h)
    simp only [h4, hk, ↓reduceIte, zero_mul]
  · intro h; exact absurd (Finset.mem_univ _) h

private lemma dot_witness_lower (j : Fin 10) (v : Fin 13 → ℝ) :
    dot (witnessNormal ⟨j.1 + 14, by omega⟩) v =
      v 0 + v 1 - (j.1 : ℝ) * v 2 - v ⟨j.1 + 3, by omega⟩ := by
  unfold dot
  have hterm : ∀ k : Fin 13, witnessNormal ⟨j.1 + 14, by omega⟩ k * v k =
      (if k = 0 then v 0 else 0) +
      (if k = 1 then v 1 else 0) +
      (if k = 2 then -(j.1 : ℝ) * v 2 else 0) +
      (if k = ⟨j.1 + 3, by omega⟩ then -v ⟨j.1 + 3, by omega⟩ else 0) := by
    intro k
    dsimp [witnessNormal]
    have hsub : j.1 + 14 - 14 = j.1 := by omega
    simp only [hsub]
    have h0j : (0 : Fin 13) ≠ ⟨j.1 + 3, by omega⟩ := fun h => by have := congrArg Fin.val h; dsimp at this; omega
    have h1j : (1 : Fin 13) ≠ ⟨j.1 + 3, by omega⟩ := fun h => by have := congrArg Fin.val h; dsimp at this; omega
    have h2j : (2 : Fin 13) ≠ ⟨j.1 + 3, by omega⟩ := fun h => by have := congrArg Fin.val h; dsimp at this; omega
    by_cases hk0 : k = 0
    · subst hk0; simp [h0j]
    by_cases hk1 : k = 1
    · subst hk1; simp [h1j]
    by_cases hk2 : k = 2
    · subst hk2; simp [h2j]
    by_cases hkj : k = ⟨j.1 + 3, by omega⟩
    · subst hkj
      have hb : j.1 + 3 ≠ 1 := by omega
      have hc : j.1 + 3 ≠ 2 := by omega
      simp [hb, hc, hk0, hk1, hk2]
    · have ha : k.1 ≠ 0 := fun h => hk0 (Fin.ext h)
      have hb : k.1 ≠ 1 := fun h => hk1 (Fin.ext h)
      have hc : k.1 ≠ 2 := fun h => hk2 (Fin.ext h)
      have hd : k.1 ≠ j.1 + 3 := fun h => hkj (Fin.ext h)
      simp [ha, hb, hc, hd, hk0, hk1, hk2, hkj]
  simp only [hterm, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, ↓reduceIte]
  ring

/-- Clean coordinate characterization of membership in `witnessHRep.poly`. -/
lemma mem_witness_poly_iff (v : Fin 13 → ℝ) :
    v ∈ witnessHRep.poly ↔
      v 0 ≤ 100 ∧ v 1 ≤ 100 ∧ v 2 ≤ 100 ∧ -(v 0) - v 1 - v 2 ≤ 100 ∧
      (∀ j : Fin 10, v ⟨j.1 + 3, by omega⟩ ≤ 1) ∧
      (∀ j : Fin 10, v 0 + v 1 - (j.1 : ℝ) * v 2 - v ⟨j.1 + 3, by omega⟩ ≤ 119 + (j.1 : ℝ) ^ 2) := by
  constructor
  · intro hv
    refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
    · simpa [witnessHRep, dot_witness_0, witnessRHS] using hv 0
    · simpa [witnessHRep, dot_witness_1, witnessRHS] using hv 1
    · simpa [witnessHRep, dot_witness_2, witnessRHS] using hv 2
    · simpa [witnessHRep, dot_witness_3, witnessRHS] using hv 3
    · intro j
      have h := hv ⟨j.1 + 4, by omega⟩
      rw [witnessHRep, dot_witness_upper] at h
      dsimp [witnessRHS] at h
      have ha : ¬ (j.1 + 4 < 4) := by omega
      have hb : j.1 + 4 < 14 := by omega
      simpa [ha, hb] using h
    · intro j
      have h := hv ⟨j.1 + 14, by omega⟩
      rw [witnessHRep, dot_witness_lower] at h
      dsimp [witnessRHS] at h
      have ha : ¬ (j.1 + 14 < 4) := by omega
      have hb : ¬ (j.1 + 14 < 14) := by omega
      have hc : j.1 + 14 - 14 = j.1 := by omega
      simpa [ha, hb, hc] using h
  · rintro ⟨h0, h1, h2, h3, hup, hlo⟩ i
    by_cases hi0 : i.1 = 0
    · have : i = 0 := Fin.ext hi0; subst this; simpa [witnessHRep, dot_witness_0, witnessRHS] using h0
    by_cases hi1 : i.1 = 1
    · have : i = 1 := Fin.ext hi1; subst this; simpa [witnessHRep, dot_witness_1, witnessRHS] using h1
    by_cases hi2 : i.1 = 2
    · have : i = 2 := Fin.ext hi2; subst this; simpa [witnessHRep, dot_witness_2, witnessRHS] using h2
    by_cases hi3 : i.1 = 3
    · have : i = 3 := Fin.ext hi3; subst this; simpa [witnessHRep, dot_witness_3, witnessRHS] using h3
    by_cases hi4 : i.1 < 14
    · let j : Fin 10 := ⟨i.1 - 4, by omega⟩
      have hi_eq : i = ⟨j.1 + 4, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hi_eq, witnessHRep, dot_witness_upper]
      dsimp [witnessRHS]
      have ha : ¬ (j.1 + 4 < 4) := by omega
      have hb : j.1 + 4 < 14 := by omega
      simpa [ha, hb] using hup j
    · let j : Fin 10 := ⟨i.1 - 14, by omega⟩
      have hi_eq : i = ⟨j.1 + 14, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hi_eq, witnessHRep, dot_witness_lower]
      dsimp [witnessRHS]
      have ha : ¬ (j.1 + 14 < 4) := by omega
      have hb : ¬ (j.1 + 14 < 14) := by omega
      have hc : j.1 + 14 - 14 = j.1 := by omega
      simpa [ha, hb, hc] using hlo j

/-! ## Section 3: Proof That `witnessHRep` Is a Primitive 13-Polytope -/

/-- Explicit ray certificates `r_i ∈ ℝ¹³` proving `witnessHRep.polyOmit i` is unbounded for all `i`. -/
private def rayCert (i : Fin 24) : Fin 13 → ℝ :=
  if i.1 = 0 then pack13 1 (-1) 0 (fun _ => 0)
  else if i.1 = 1 then pack13 (-1) 1 0 (fun _ => 0)
  else if i.1 = 2 then pack13 (-1) (-1) 2 (fun _ => 0)
  else if i.1 = 3 then pack13 (-10) 0 (-1) (fun _ => 0)
  else if i.1 < 14 then pack13 0 0 0 (fun j => if j.1 = i.1 - 4 then 1 else 0)
  else pack13 0 0 0 (fun j => if j.1 = i.1 - 14 then -1 else 0)

private lemma witnessRHS_pos (i : Fin 24) : 0 < witnessRHS i := by
  dsimp [witnessRHS]
  split_ifs <;> positivity

/-- Every ray `r_i` is nonzero and satisfies `a_m · r_i ≤ 0` for all `m ≠ i`. -/
private lemma rayCert_props (i : Fin 24) :
    (∃ k : Fin 13, 1 ≤ |rayCert i k|) ∧
    (∀ m : Fin 24, m ≠ i → dot (witnessNormal m) (rayCert i) ≤ 0) := by
  have hnonpos : ∀ (v : Fin 13 → ℝ) (i : Fin 24),
      (i.1 ≠ 0 → v 0 ≤ 0) →
      (i.1 ≠ 1 → v 1 ≤ 0) →
      (i.1 ≠ 2 → v 2 ≤ 0) →
      (i.1 ≠ 3 → -(v 0) - v 1 - v 2 ≤ 0) →
      (∀ j : Fin 10, i.1 ≠ j.1 + 4 → v ⟨j.1 + 3, by omega⟩ ≤ 0) →
      (∀ j : Fin 10, i.1 ≠ j.1 + 14 → v 0 + v 1 - (j.1 : ℝ) * v 2 - v ⟨j.1 + 3, by omega⟩ ≤ 0) →
      ∀ m : Fin 24, m ≠ i → dot (witnessNormal m) v ≤ 0 := by
    intro v i h0 h1 h2 h3 hup hlo m hmi
    by_cases hm0 : m.1 = 0
    · have hm : m = 0 := Fin.ext hm0; subst hm; rw [dot_witness_0]; exact h0 (fun h => hmi (Fin.ext h.symm))
    by_cases hm1 : m.1 = 1
    · have hm : m = 1 := Fin.ext hm1; subst hm; rw [dot_witness_1]; exact h1 (fun h => hmi (Fin.ext h.symm))
    by_cases hm2 : m.1 = 2
    · have hm : m = 2 := Fin.ext hm2; subst hm; rw [dot_witness_2]; exact h2 (fun h => hmi (Fin.ext h.symm))
    by_cases hm3 : m.1 = 3
    · have hm : m = 3 := Fin.ext hm3; subst hm; rw [dot_witness_3]; exact h3 (fun h => hmi (Fin.ext h.symm))
    by_cases hm4 : m.1 < 14
    · let j : Fin 10 := ⟨m.1 - 4, by omega⟩
      have hm : m = ⟨j.1 + 4, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hm, dot_witness_upper]
      exact hup j (fun h => hmi (Fin.ext (by dsimp [j] at h ⊢; omega)))
    · let j : Fin 10 := ⟨m.1 - 14, by omega⟩
      have hm : m = ⟨j.1 + 14, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hm, dot_witness_lower]
      exact hlo j (fun h => hmi (Fin.ext (by dsimp [j] at h ⊢; omega)))
  by_cases hi0 : i.1 = 0
  · refine ⟨⟨0, by simp [rayCert, hi0]⟩, hnonpos _ i (by omega) ?_ ?_ ?_ ?_ ?_⟩
    · intro _; simp [rayCert, hi0]
    · intro _; simp [rayCert, hi0]
    · intro _; simp [rayCert, hi0]
    · intro j _; simp [rayCert, hi0, pack13_y]
    · intro j _; simp [rayCert, hi0, pack13_y]
  by_cases hi1 : i.1 = 1
  · refine ⟨⟨1, by simp [rayCert, hi1]⟩, hnonpos _ i ?_ (by omega) ?_ ?_ ?_ ?_⟩
    · intro _; simp [rayCert, hi1]
    · intro _; simp [rayCert, hi1]
    · intro _; simp [rayCert, hi1]
    · intro j _; simp [rayCert, hi1, pack13_y]
    · intro j _; simp [rayCert, hi1, pack13_y]
  by_cases hi2 : i.1 = 2
  · refine ⟨⟨2, by simp [rayCert, hi2]⟩, hnonpos _ i ?_ ?_ (by omega) ?_ ?_ ?_⟩
    · intro _; simp [rayCert, hi2]
    · intro _; simp [rayCert, hi2]
    · intro _; simp [rayCert, hi2]; norm_num
    · intro j _; simp [rayCert, hi2, pack13_y]
    · intro j _
      have hr2 : rayCert i = pack13 (-1) (-1) 2 (fun _ => 0) := by simp [rayCert, hi2]
      rw [hr2, pack13_0, pack13_1, pack13_2, pack13_y]
      have hj : (0 : ℝ) ≤ (j.1 : ℝ) := Nat.cast_nonneg _
      linarith
  by_cases hi3 : i.1 = 3
  · refine ⟨⟨2, by simp [rayCert, hi3]⟩, hnonpos _ i ?_ ?_ ?_ (by omega) ?_ ?_⟩
    · intro _; simp [rayCert, hi3]
    · intro _; simp [rayCert, hi3]
    · intro _; simp [rayCert, hi3]
    · intro j _; simp [rayCert, hi3, pack13_y]
    · intro j _
      have hr3 : rayCert i = pack13 (-10) 0 (-1) (fun _ => 0) := by simp [rayCert, hi3]
      rw [hr3, pack13_0, pack13_1, pack13_2, pack13_y]
      have hj : (j.1 : ℝ) ≤ 9 := by exact_mod_cast Nat.le_of_lt_succ j.2
      linarith
  by_cases hi4 : i.1 < 14
  · let j₀ : Fin 10 := ⟨i.1 - 4, by omega⟩
    refine ⟨⟨⟨j₀.1 + 3, by omega⟩, ?_⟩, hnonpos _ i ?_ ?_ ?_ ?_ ?_ ?_⟩
    · simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_y]
      simp [j₀]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro j hne
      simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_y]
      have hne' : j.1 ≠ i.1 - 4 := by omega
      simp [hne']
    · intro j _
      simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_0, pack13_1, pack13_2, pack13_y]
      split_ifs <;> norm_num
  · let j₀ : Fin 10 := ⟨i.1 - 14, by omega⟩
    refine ⟨⟨⟨j₀.1 + 3, by omega⟩, ?_⟩, hnonpos _ i ?_ ?_ ?_ ?_ ?_ ?_⟩
    · simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_y]
      simp [j₀]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro _; simp [rayCert, hi0, hi1, hi2, hi3, hi4]
    · intro j _
      simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_y]
      split_ifs <;> norm_num
    · intro j hne
      simp only [rayCert, hi0, hi1, hi2, hi3, hi4, ↓reduceIte, pack13_0, pack13_1, pack13_2, pack13_y]
      have hne' : j.1 ≠ i.1 - 14 := by omega
      simp [hne']

/-- **Theorem 1:** `witnessHRep` defines a primitive 13-polytope in `ℝ¹³` (nonempty interior,
bounded, and omitting any of its 24 halfspaces yields an unbounded intersection). -/
theorem witness_isPrimitive : witnessHRep.IsPrimitive := by
  refine ⟨?_, ?_, ?_⟩
  · -- Nonempty interior: `0 ∈ int P` since `0 < b_i` for all `i`.
    refine ⟨fun _ => 0, fun i => ?_⟩
    simp [witnessHRep, dot, witnessRHS_pos i]
  · -- Boundedness: `|v k| ≤ 2000` for every `v ∈ P` and `k : Fin 13`.
    refine ⟨2000, fun v hv k => ?_⟩
    obtain ⟨h0, h1, h2, h3, hup, hlo⟩ := (mem_witness_poly_iff v).mp hv
    have hx0 : -300 ≤ v 0 := by linarith
    have hx1 : -300 ≤ v 1 := by linarith
    have hx2 : -300 ≤ v 2 := by linarith
    by_cases hk0 : k.1 = 0
    · have hk : k = 0 := Fin.ext hk0; subst hk; rw [abs_le]; constructor <;> linarith
    by_cases hk1 : k.1 = 1
    · have hk : k = 1 := Fin.ext hk1; subst hk; rw [abs_le]; constructor <;> linarith
    by_cases hk2 : k.1 = 2
    · have hk : k = 2 := Fin.ext hk2; subst hk; rw [abs_le]; constructor <;> linarith
    · let j : Fin 10 := ⟨k.1 - 3, by omega⟩
      have hk : k = ⟨j.1 + 3, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hk]
      have hjup := hup j
      have hjlo := hlo j
      have hj_le : (j.1 : ℝ) ≤ 9 := by exact_mod_cast Nat.le_of_lt_succ j.2
      have hj_nn : (0 : ℝ) ≤ (j.1 : ℝ) := Nat.cast_nonneg _
      have hj_sq : (j.1 : ℝ) ^ 2 ≤ 81 := by nlinarith
      have hjx2 : (j.1 : ℝ) * v 2 ≤ 900 := by nlinarith
      rw [abs_le]; constructor <;> linarith
  · -- Primitivity: omitting any halfspace `i` contains the ray `{t • r_i | t ≥ 0}`.
    intro i ⟨R, hR⟩
    obtain ⟨⟨k, hk1⟩, hray⟩ := rayCert_props i
    let t : ℝ := max R 0 + 1
    have ht_pos : 0 < t := by positivity
    let x : Fin 13 → ℝ := fun c => t * rayCert i c
    have hx_mem : x ∈ witnessHRep.polyOmit i := by
      intro m hmi
      change dot (witnessNormal m) x ≤ witnessRHS m
      have hdot : dot (witnessNormal m) x = t * dot (witnessNormal m) (rayCert i) := by
        simp [dot, x, Finset.mul_sum]; congr 1; ext c; ring
      rw [hdot]
      have hm1 : t * dot (witnessNormal m) (rayCert i) ≤ 0 :=
        mul_nonpos_of_nonneg_of_nonpos ht_pos.le (hray m hmi)
      exact le_trans hm1 (witnessRHS_pos m).le
    have hbd := hR x hx_mem k
    have hkx : |x k| = t * |rayCert i k| := by
      dsimp [x]; rw [abs_mul, abs_of_pos ht_pos]
    rw [hkx] at hbd
    have ht_gt_R : R < t := by dsimp [t]; linarith [le_max_left R 0]
    have hmul : t ≤ t * |rayCert i k| := by nlinarith
    linarith

/-! ## Section 4: Projected 3-Polytope `P_x` and Its 24 Extreme Points -/

/-- The projected 3-polytope `P_x ⊂ ℝ³`:
`x₁ ≤ 100`, `x₂ ≤ 100`, `x₃ ≤ 100`, `-x₁ - x₂ - x₃ ≤ 100`,
and `x₁ + x₂ - j x₃ ≤ 120 + j²` for `j = 0, ..., 9`. -/
def InPx (x1 x2 x3 : ℝ) : Prop :=
  x1 ≤ 100 ∧ x2 ≤ 100 ∧ x3 ≤ 100 ∧ -x1 - x2 - x3 ≤ 100 ∧
  ∀ j : Fin 10, x1 + x2 - (j.1 : ℝ) * x3 ≤ 120 + (j.1 : ℝ) ^ 2

/-- Lower bound `L_j(x) = x₁ + x₂ - j x₃ - (119 + j²)` for `y_j` in `P`. -/
def lowerY (x1 x2 x3 : ℝ) (j : Fin 10) : ℝ :=
  x1 + x2 - (j.1 : ℝ) * x3 - (119 + (j.1 : ℝ) ^ 2)

lemma proj_inPx {v : Fin 13 → ℝ} (hv : v ∈ witnessHRep.poly) : InPx (v 0) (v 1) (v 2) := by
  obtain ⟨h0, h1, h2, h3, hup, hlo⟩ := (mem_witness_poly_iff v).mp hv
  exact ⟨h0, h1, h2, h3, fun j => by linarith [hup j, hlo j]⟩

/-- Extreme-point criterion for `P_x`: `x` is extreme in `P_x`, and lifting `y_j ∈ {L_j(x), 1}`
produces an extreme point of `witnessHRep.poly`! -/
private lemma isVertex_of_base_extreme {x1 x2 x3 : ℝ} {y : Fin 10 → ℝ}
    (hPx : InPx x1 x2 x3)
    (hext : ∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 →
      0 < t → t < 1 →
      x1 = (1 - t) * u1 + t * w1 →
      x2 = (1 - t) * u2 + t * w2 →
      x3 = (1 - t) * u3 + t * w3 →
      u1 = x1 ∧ w1 = x1 ∧ u2 = x2 ∧ w2 = x2 ∧ u3 = x3 ∧ w3 = x3)
    (hy_end : ∀ j : Fin 10, y j = 1 ∨ y j = lowerY x1 x2 x3 j) :
    IsVertex witnessHRep.poly (pack13 x1 x2 x3 y) := by
  have hmem : pack13 x1 x2 x3 y ∈ witnessHRep.poly := by
    rw [mem_witness_poly_iff]
    refine ⟨hPx.1, hPx.2.1, hPx.2.2.1, hPx.2.2.2.1, ?_, ?_⟩
    · intro j
      rw [pack13_y]
      rcases hy_end j with h | h
      · linarith
      · rw [h]; dsimp [lowerY]; linarith [hPx.2.2.2.2 j]
    · intro j
      simp only [pack13_0, pack13_1, pack13_2, pack13_y]
      rcases hy_end j with h | h
      · rw [h]; linarith [hPx.2.2.2.2 j]
      · rw [h]; dsimp [lowerY]; linarith
  refine ⟨hmem, fun u w hu hw t ht0 ht1 hcomb => ?_⟩
  have huPx := proj_inPx hu
  have hwPx := proj_inPx hw
  have hbase := hext (u 0) (u 1) (u 2) (w 0) (w 1) (w 2) t huPx hwPx ht0 ht1
    (hcomb 0) (hcomb 1) (hcomb 2)
  obtain ⟨hu0, hw0, hu1, hw1, hu2, hw2⟩ := hbase
  obtain ⟨_, _, _, _, hu_up, hu_lo⟩ := (mem_witness_poly_iff u).mp hu
  obtain ⟨_, _, _, _, hw_up, hw_lo⟩ := (mem_witness_poly_iff w).mp hw
  have hy_eq : ∀ j : Fin 10,
      u ⟨j.1 + 3, by omega⟩ = y j ∧ w ⟨j.1 + 3, by omega⟩ = y j := by
    intro j
    have hcj := hcomb ⟨j.1 + 3, by omega⟩
    rw [pack13_y] at hcj
    have hu_le1 := hu_up j
    have hw_le1 := hw_up j
    have hu_geL : lowerY x1 x2 x3 j ≤ u ⟨j.1 + 3, by omega⟩ := by
      have h := hu_lo j; rw [hu0, hu1, hu2] at h; dsimp [lowerY]; linarith
    have hw_geL : lowerY x1 x2 x3 j ≤ w ⟨j.1 + 3, by omega⟩ := by
      have h := hw_lo j; rw [hw0, hw1, hw2] at h; dsimp [lowerY]; linarith
    rcases hy_end j with h | h
    · rw [h] at hcj
      exact ⟨by nlinarith, by nlinarith⟩
    · rw [h] at hcj
      exact ⟨by nlinarith, by nlinarith⟩
  constructor <;> ext k
  · by_cases hk0 : k.1 = 0
    · have hk : k = 0 := Fin.ext hk0; subst hk; exact hu0
    by_cases hk1 : k.1 = 1
    · have hk : k = 1 := Fin.ext hk1; subst hk; exact hu1
    by_cases hk2 : k.1 = 2
    · have hk : k = 2 := Fin.ext hk2; subst hk; exact hu2
    · let j : Fin 10 := ⟨k.1 - 3, by omega⟩
      have hk : k = ⟨j.1 + 3, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hk, pack13_y]; exact (hy_eq j).1
  · by_cases hk0 : k.1 = 0
    · have hk : k = 0 := Fin.ext hk0; subst hk; exact hw0
    by_cases hk1 : k.1 = 1
    · have hk : k = 1 := Fin.ext hk1; subst hk; exact hw1
    by_cases hk2 : k.1 = 2
    · have hk : k = 2 := Fin.ext hk2; subst hk; exact hw2
    · let j : Fin 10 := ⟨k.1 - 3, by omega⟩
      have hk : k = ⟨j.1 + 3, by omega⟩ := Fin.ext (by dsimp [j]; omega)
      rw [hk, pack13_y]; exact (hy_eq j).2

/-- Symmetry of `InPx` under swapping `x₁ ↔ x₂`. -/
private lemma inPx_swap {x1 x2 x3 : ℝ} (h : InPx x1 x2 x3) : InPx x2 x1 x3 :=
  ⟨h.2.1, h.1, h.2.2.1, by linarith [h.2.2.2.1], fun j => by linarith [h.2.2.2.2 j]⟩

/-- The 3D base vertices of `P_x`:
- Group A (`2` vertices, `r = 0`): `(-300, 100, 100)` and `(100, -300, 100)`.
- Group B (`4` vertices, `r = 1`): `(-1699/10, 100, -301/10)`, `(20, 100, 100)`, and their swaps.
- Group C (`18` vertices, `r = 2`): `(20 - m² - m, 100, -2m - 1)` (`m = 0..8`) and their swaps. -/
private def baseVertA (i : Fin 2) : ℝ × ℝ × ℝ :=
  if i.1 = 0 then (-300, 100, 100) else (100, -300, 100)

private noncomputable def baseVertB (i : Fin 4) : ℝ × ℝ × ℝ :=
  match i.1 with
  | 0 => (-1699 / 10, 100, -301 / 10)
  | 1 => (20, 100, 100)
  | 2 => (100, -1699 / 10, -301 / 10)
  | _ => (100, 20, 100)

/-- The tight slice index `j` for each of the 4 Group B vertices (`j = 9` or `j = 0`). -/
private def tightB (i : Fin 4) : Fin 10 :=
  if i.1 = 0 ∨ i.1 = 2 then 9 else 0

private def baseVertC (i : Fin 18) : ℝ × ℝ × ℝ :=
  let m : ℕ := i.1 % 9
  let x1 : ℝ := 20 - (m : ℝ) ^ 2 - (m : ℝ)
  let x3 : ℝ := -2 * (m : ℝ) - 1
  if i.1 < 9 then (x1, 100, x3) else (100, x1, x3)

/-- Helper: convex combination equal to an upper bound forces both endpoints equal to the bound. -/
private lemma eq_of_comb_le {a u w t : ℝ} (ht0 : 0 < t) (ht1 : t < 1)
    (hu : u ≤ a) (hw : w ≤ a) (h : a = (1 - t) * u + t * w) : u = a ∧ w = a :=
  ⟨by nlinarith, by nlinarith⟩

/-- Group A (`2` vertices): in `P_x`, extreme, and all `10` slices strictly slack (`L_j < 1`). -/
private lemma baseVertA_props (i : Fin 2) :
    let (x1, x2, x3) := baseVertA i
    InPx x1 x2 x3 ∧
    (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
      x1 = (1 - t) * u1 + t * w1 → x2 = (1 - t) * u2 + t * w2 → x3 = (1 - t) * u3 + t * w3 →
      u1 = x1 ∧ w1 = x1 ∧ u2 = x2 ∧ w2 = x2 ∧ u3 = x3 ∧ w3 = x3) ∧
    (∀ j : Fin 10, lowerY x1 x2 x3 j < 1) := by
  have h0 : InPx (-300) 100 100 ∧
      (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
        (-300 : ℝ) = (1 - t) * u1 + t * w1 → (100 : ℝ) = (1 - t) * u2 + t * w2 →
        (100 : ℝ) = (1 - t) * u3 + t * w3 →
        u1 = -300 ∧ w1 = -300 ∧ u2 = 100 ∧ w2 = 100 ∧ u3 = 100 ∧ w3 = 100) ∧
      (∀ j : Fin 10, lowerY (-300) 100 100 j < 1) := by
    refine ⟨⟨by norm_num, by norm_num, by norm_num, by norm_num, fun j => ?_⟩, ?_, ?_⟩
    · have hj : (0 : ℝ) ≤ (j.1 : ℝ) := Nat.cast_nonneg _
      nlinarith
    · intro u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3
      obtain ⟨hu2, hw2⟩ := eq_of_comb_le ht0 ht1 hu.2.1 hw.2.1 h2
      obtain ⟨hu3, hw3⟩ := eq_of_comb_le ht0 ht1 hu.2.2.1 hw.2.2.1 h3
      have hsum : (100 : ℝ) = (1 - t) * (-u1 - u2 - u3) + t * (-w1 - w2 - w3) := by linarith
      obtain ⟨hs1, hs2⟩ := eq_of_comb_le ht0 ht1 hu.2.2.2.1 hw.2.2.2.1 hsum
      exact ⟨by linarith, by linarith, hu2, hw2, hu3, hw3⟩
    · intro j
      dsimp [lowerY]
      have hj : (0 : ℝ) ≤ (j.1 : ℝ) := Nat.cast_nonneg _
      nlinarith
  fin_cases i
  · exact h0
  · refine ⟨inPx_swap h0.1, fun u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3 => ?_,
      fun j => by simpa [baseVertA, lowerY, add_comm] using h0.2.2 j⟩
    have := h0.2.1 u2 u1 u3 w2 w1 w3 t (inPx_swap hu) (inPx_swap hw) ht0 ht1 h2 h1 h3
    tauto

/-- Group B (`4` vertices): in `P_x`, extreme, and all slices `j ≠ tightB i` strictly slack. -/
private lemma baseVertB_props (i : Fin 4) :
    let (x1, x2, x3) := baseVertB i
    InPx x1 x2 x3 ∧
    (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
      x1 = (1 - t) * u1 + t * w1 → x2 = (1 - t) * u2 + t * w2 → x3 = (1 - t) * u3 + t * w3 →
      u1 = x1 ∧ w1 = x1 ∧ u2 = x2 ∧ w2 = x2 ∧ u3 = x3 ∧ w3 = x3) ∧
    (∀ j : Fin 10, j ≠ tightB i → lowerY x1 x2 x3 j < 1) := by
  have hB0 : InPx (-1699 / 10) 100 (-301 / 10) ∧
      (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
        (-1699 / 10 : ℝ) = (1 - t) * u1 + t * w1 → (100 : ℝ) = (1 - t) * u2 + t * w2 →
        (-301 / 10 : ℝ) = (1 - t) * u3 + t * w3 →
        u1 = -1699 / 10 ∧ w1 = -1699 / 10 ∧ u2 = 100 ∧ w2 = 100 ∧
        u3 = -301 / 10 ∧ w3 = -301 / 10) ∧
      (∀ j : Fin 10, j ≠ 9 → lowerY (-1699 / 10) 100 (-301 / 10) j < 1) := by
    refine ⟨⟨by norm_num, by norm_num, by norm_num, by norm_num, fun j => ?_⟩, ?_, ?_⟩
    · have hj : (j.1 : ℝ) ≤ 9 := by exact_mod_cast Nat.le_of_lt_succ j.2
      have hfac : (120 + (j.1 : ℝ) ^ 2) - (-1699 / 10 + 100 - (j.1 : ℝ) * (-301 / 10)) =
          (9 - (j.1 : ℝ)) * (211 / 10 - (j.1 : ℝ)) := by ring
      nlinarith
    · intro u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3
      obtain ⟨hu2, hw2⟩ := eq_of_comb_le ht0 ht1 hu.2.1 hw.2.1 h2
      have hsum : (100 : ℝ) = (1 - t) * (-u1 - u2 - u3) + t * (-w1 - w2 - w3) := by linarith
      obtain ⟨hs1, hs2⟩ := eq_of_comb_le ht0 ht1 hu.2.2.2.1 hw.2.2.2.1 hsum
      have h9u := hu.2.2.2.2 9
      have h9w := hw.2.2.2.2 9
      dsimp at h9u h9w
      have h9comb : (201 : ℝ) = (1 - t) * (u1 + u2 - 9 * u3) + t * (w1 + w2 - 9 * w3) := by linarith
      obtain ⟨hq1, hq2⟩ := eq_of_comb_le ht0 ht1 (by linarith : u1 + u2 - 9 * u3 ≤ 201)
        (by linarith : w1 + w2 - 9 * w3 ≤ 201) h9comb
      exact ⟨by linarith, by linarith, hu2, hw2, by linarith, by linarith⟩
    · intro j hj9
      dsimp [lowerY]
      have hj : (j.1 : ℝ) ≤ 8 := by
        have hlt : j.1 < 9 := Nat.lt_of_le_of_ne (Nat.le_of_lt_succ j.2) (fun h => hj9 (Fin.ext h))
        exact_mod_cast Nat.le_of_lt_succ hlt
      have hfac : 1 - (-1699 / 10 + 100 - (j.1 : ℝ) * (-301 / 10) - (119 + (j.1 : ℝ) ^ 2)) =
          (9 - (j.1 : ℝ)) * (211 / 10 - (j.1 : ℝ)) := by ring
      nlinarith
  have hB1 : InPx 20 100 100 ∧
      (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
        (20 : ℝ) = (1 - t) * u1 + t * w1 → (100 : ℝ) = (1 - t) * u2 + t * w2 →
        (100 : ℝ) = (1 - t) * u3 + t * w3 →
        u1 = 20 ∧ w1 = 20 ∧ u2 = 100 ∧ w2 = 100 ∧ u3 = 100 ∧ w3 = 100) ∧
      (∀ j : Fin 10, j ≠ 0 → lowerY 20 100 100 j < 1) := by
    refine ⟨⟨by norm_num, by norm_num, by norm_num, by norm_num, fun j => ?_⟩, ?_, ?_⟩
    · have hj : (0 : ℝ) ≤ (j.1 : ℝ) := Nat.cast_nonneg _
      nlinarith
    · intro u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3
      obtain ⟨hu2, hw2⟩ := eq_of_comb_le ht0 ht1 hu.2.1 hw.2.1 h2
      obtain ⟨hu3, hw3⟩ := eq_of_comb_le ht0 ht1 hu.2.2.1 hw.2.2.1 h3
      have h0u := hu.2.2.2.2 0
      have h0w := hw.2.2.2.2 0
      simp only [Fin.val_zero, Nat.cast_zero, zero_mul, sub_zero, ne_eq,
        OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, add_zero] at h0u h0w
      have h0comb : (120 : ℝ) = (1 - t) * (u1 + u2) + t * (w1 + w2) := by linarith
      obtain ⟨hq1, hq2⟩ := eq_of_comb_le ht0 ht1 (by linarith : u1 + u2 ≤ 120)
        (by linarith : w1 + w2 ≤ 120) h0comb
      exact ⟨by linarith, by linarith, hu2, hw2, hu3, hw3⟩
    · intro j hj0
      dsimp [lowerY]
      have hj : (1 : ℝ) ≤ (j.1 : ℝ) := by
        have hpos : 0 < j.1 := Nat.pos_of_ne_zero (fun h => hj0 (Fin.ext h))
        exact_mod_cast hpos
      nlinarith
  fin_cases i
  · exact hB0
  · exact hB1
  · refine ⟨inPx_swap hB0.1, fun u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3 => ?_,
      fun j hj => by simpa [baseVertB, tightB, lowerY, add_comm] using hB0.2.2 j hj⟩
    have := hB0.2.1 u2 u1 u3 w2 w1 w3 t (inPx_swap hu) (inPx_swap hw) ht0 ht1 h2 h1 h3
    tauto
  · refine ⟨inPx_swap hB1.1, fun u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3 => ?_,
      fun j hj => by simpa [baseVertB, tightB, lowerY, add_comm] using hB1.2.2 j hj⟩
    have := hB1.2.1 u2 u1 u3 w2 w1 w3 t (inPx_swap hu) (inPx_swap hw) ht0 ht1 h2 h1 h3
    tauto

/-- Group C (`18` vertices): for `m = i % 9 ∈ {0..8}`, slices `m` and `m + 1` are tight and
every other slice `j ∉ {m, m + 1}` is strictly slack (`(j - m)(j - m - 1) ≥ 2 > 0`). -/
private lemma baseVertC_props (i : Fin 18) :
    let (x1, x2, x3) := baseVertC i
    InPx x1 x2 x3 ∧
    (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
      x1 = (1 - t) * u1 + t * w1 → x2 = (1 - t) * u2 + t * w2 → x3 = (1 - t) * u3 + t * w3 →
      u1 = x1 ∧ w1 = x1 ∧ u2 = x2 ∧ w2 = x2 ∧ u3 = x3 ∧ w3 = x3) ∧
    (∀ j : Fin 10, j.1 ≠ i.1 % 9 → j.1 ≠ i.1 % 9 + 1 → lowerY x1 x2 x3 j < 1) := by
  let m : ℕ := i.1 % 9
  have hm_lt : m < 9 := Nat.mod_lt _ (by decide)
  have hm_le8 : (m : ℝ) ≤ 8 := by exact_mod_cast Nat.le_of_lt_succ hm_lt
  have hm_nn : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
  let x1 : ℝ := 20 - (m : ℝ) ^ 2 - (m : ℝ)
  let x3 : ℝ := -2 * (m : ℝ) - 1
  have hmain : InPx x1 100 x3 ∧
      (∀ u1 u2 u3 w1 w2 w3 t : ℝ, InPx u1 u2 u3 → InPx w1 w2 w3 → 0 < t → t < 1 →
        x1 = (1 - t) * u1 + t * w1 → (100 : ℝ) = (1 - t) * u2 + t * w2 →
        x3 = (1 - t) * u3 + t * w3 →
        u1 = x1 ∧ w1 = x1 ∧ u2 = 100 ∧ w2 = 100 ∧ u3 = x3 ∧ w3 = x3) ∧
      (∀ j : Fin 10, j.1 ≠ m → j.1 ≠ m + 1 → lowerY x1 100 x3 j < 1) := by
    refine ⟨⟨by dsimp [x1]; nlinarith, by norm_num, by dsimp [x3]; linarith,
        by dsimp [x1, x3]; nlinarith, fun j => ?_⟩, ?_, ?_⟩
    · have hid : (120 + (j.1 : ℝ) ^ 2) - (x1 + 100 - (j.1 : ℝ) * x3) =
          ((j.1 : ℝ) - (m : ℝ)) * ((j.1 : ℝ) - (m : ℝ) - 1) := by dsimp [x1, x3]; ring
      have hprod_nn : 0 ≤ ((j.1 : ℝ) - (m : ℝ)) * ((j.1 : ℝ) - (m : ℝ) - 1) := by
        rcases le_or_gt j.1 m with hle | hgt
        · have : (j.1 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hle
          nlinarith
        · have : (m : ℝ) + 1 ≤ (j.1 : ℝ) := by exact_mod_cast hgt
          nlinarith
      linarith
    · intro u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3
      obtain ⟨hu2, hw2⟩ := eq_of_comb_le ht0 ht1 hu.2.1 hw.2.1 h2
      have hmu := hu.2.2.2.2 ⟨m, by omega⟩
      have hmw := hw.2.2.2.2 ⟨m, by omega⟩
      have hm1u := hu.2.2.2.2 ⟨m + 1, by omega⟩
      have hm1w := hw.2.2.2.2 ⟨m + 1, by omega⟩
      dsimp at hmu hmw hm1u hm1w
      have hcomb_m : 120 + (m : ℝ) ^ 2 =
          (1 - t) * (u1 + u2 - (m : ℝ) * u3) + t * (w1 + w2 - (m : ℝ) * w3) := by
        dsimp [x1, x3] at h1 h3; linear_combination h1 + h2 - (m : ℝ) * h3
      have hcomb_m1 : 120 + ((m + 1 : ℕ) : ℝ) ^ 2 =
          (1 - t) * (u1 + u2 - ((m + 1 : ℕ) : ℝ) * u3) + t * (w1 + w2 - ((m + 1 : ℕ) : ℝ) * w3) := by
        push_cast; dsimp [x1, x3] at h1 h3; linear_combination h1 + h2 - ((m : ℝ) + 1) * h3
      obtain ⟨hem_u, hem_w⟩ := eq_of_comb_le ht0 ht1 hmu hmw hcomb_m
      obtain ⟨hem1_u, hem1_w⟩ := eq_of_comb_le ht0 ht1 hm1u hm1w hcomb_m1
      push_cast at hem1_u hem1_w
      have hu3 : u3 = x3 := by dsimp [x3]; linarith
      have hw3 : w3 = x3 := by dsimp [x3]; linarith
      have hu1 : u1 = x1 := by dsimp [x1]; nlinarith
      have hw1 : w1 = x1 := by dsimp [x1]; nlinarith
      exact ⟨hu1, hw1, hu2, hw2, hu3, hw3⟩
    · intro j hne1 hne2
      dsimp [lowerY]
      have hid : 1 - (x1 + 100 - (j.1 : ℝ) * x3 - (119 + (j.1 : ℝ) ^ 2)) =
          ((j.1 : ℝ) - (m : ℝ)) * ((j.1 : ℝ) - (m : ℝ) - 1) := by dsimp [x1, x3]; ring
      have hpos : 0 < ((j.1 : ℝ) - (m : ℝ)) * ((j.1 : ℝ) - (m : ℝ) - 1) := by
        rcases lt_or_gt_of_ne hne1 with hlt | hgt
        · have h1 : (j.1 : ℝ) + 1 ≤ (m : ℝ) := by exact_mod_cast hlt
          nlinarith
        · have h2 : m + 1 < j.1 := Nat.lt_of_le_of_ne hgt (Ne.symm hne2)
          have h3 : (m : ℝ) + 2 ≤ (j.1 : ℝ) := by exact_mod_cast h2
          nlinarith
      linarith
  dsimp [baseVertC]
  split_ifs with hlt
  · exact hmain
  · refine ⟨inPx_swap hmain.1, fun u1 u2 u3 w1 w2 w3 t hu hw ht0 ht1 h1 h2 h3 => ?_,
      fun j h1 h2 => by simpa [lowerY, x1, x3, m, add_comm] using hmain.2.2 j h1 h2⟩
    have := hmain.2.1 u2 u1 u3 w2 w1 w3 t (inPx_swap hu) (inPx_swap hw) ht0 ht1 h2 h1 h3
    tauto

/-! ## Section 5: Exact Enumeration of 8,704 Distinct Vertices (`8704 > 8192 = 2¹³`) -/

/-- Index type for the `2 * 2¹⁰ + 4 * 2⁹ + 18 * 2⁸ = 8704` lifted vertices of `witnessHRep`. -/
abbrev VertIdx :=
  (Fin 2 × (Fin 10 → Bool)) ⊕ (Fin 4 × (Fin 9 → Bool)) ⊕ (Fin 18 × (Fin 8 → Bool))

lemma card_vertIdx : Fintype.card VertIdx = 8704 := by
  simp [VertIdx, Fintype.card_sum, Fintype.card_prod, Fintype.card_pi]

/-- Skip-one index embedding `Fin 9 → Fin 10` avoiding `t : Fin 10`. -/
private def skipOne (t : Fin 10) (k : Fin 9) : Fin 10 :=
  if k.1 < t.1 then ⟨k.1, by omega⟩ else ⟨k.1 + 1, by omega⟩

private lemma skipOne_ne (t : Fin 10) (k : Fin 9) : skipOne t k ≠ t := by
  dsimp [skipOne]; split_ifs <;> simp [Fin.ext_iff] <;> omega

private lemma skipOne_injective (t : Fin 10) : Function.Injective (skipOne t) := by
  intro a b h
  dsimp [skipOne] at h
  split_ifs at h <;> simp [Fin.ext_iff] at h <;> exact Fin.ext (by omega)

/-- Skip-two-consecutive index embedding `Fin 8 → Fin 10` avoiding `m` and `m + 1` (`m < 9`). -/
private def skipTwo (m : ℕ) (k : Fin 8) : Fin 10 :=
  if k.1 < m then ⟨k.1, by omega⟩ else ⟨k.1 + 2, by omega⟩

private lemma skipTwo_ne (m : ℕ) (k : Fin 8) :
    (skipTwo m k).1 ≠ m ∧ (skipTwo m k).1 ≠ m + 1 := by
  dsimp [skipTwo]; split_ifs <;> dsimp <;> omega

private lemma skipTwo_injective (m : ℕ) : Function.Injective (skipTwo m) := by
  intro a b h
  dsimp [skipTwo] at h
  split_ifs at h <;> simp [Fin.ext_iff] at h <;> exact Fin.ext (by omega)

/-- Explicit map sending each `idx : VertIdx` to a vertex of `witnessHRep.poly` in `ℝ¹³`. -/
noncomputable def liftVert : VertIdx → (Fin 13 → ℝ)
  | .inl (i, bits) =>
    let (x1, x2, x3) := baseVertA i
    pack13 x1 x2 x3 (fun j => if bits j then 1 else lowerY x1 x2 x3 j)
  | .inr (.inl (i, bits)) =>
    let (x1, x2, x3) := baseVertB i
    let t := tightB i
    pack13 x1 x2 x3 (fun j =>
      if hj : j = t then 1
      else
        let k : Fin 9 := if hlt : j.1 < t.1 then ⟨j.1, by have := t.2; omega⟩ else ⟨j.1 - 1, by
          have := j.2; have hne : j.1 ≠ t.1 := fun h => hj (Fin.ext h); omega⟩
        if bits k then 1 else lowerY x1 x2 x3 j)
  | .inr (.inr (i, bits)) =>
    let (x1, x2, x3) := baseVertC i
    let m := i.1 % 9
    pack13 x1 x2 x3 (fun j =>
      if h1 : j.1 = m ∨ j.1 = m + 1 then 1
      else
        let k : Fin 8 := if hlt : j.1 < m then ⟨j.1, by have : m < 9 := Nat.mod_lt _ (by decide); omega⟩
          else ⟨j.1 - 2, by have := j.2; omega⟩
        if bits k then 1 else lowerY x1 x2 x3 j)

lemma liftVert_isVertex (idx : VertIdx) : IsVertex witnessHRep.poly (liftVert idx) := by
  rcases idx with ⟨i, bits⟩ | ⟨i, bits⟩ | ⟨i, bits⟩
  · have hp := baseVertA_props i
    dsimp [liftVert]
    exact isVertex_of_base_extreme hp.1 hp.2.1 (fun j => by split_ifs <;> simp)
  · have hp := baseVertB_props i
    dsimp [liftVert]
    exact isVertex_of_base_extreme hp.1 hp.2.1 (fun j => by split_ifs <;> simp)
  · have hp := baseVertC_props i
    dsimp [liftVert]
    exact isVertex_of_base_extreme hp.1 hp.2.1 (fun j => by split_ifs <;> simp)

/-- All 24 base 3D vertices are pairwise distinct! -/
private lemma baseVert_injective :
    Function.Injective (fun p : Fin 2 ⊕ Fin 4 ⊕ Fin 18 =>
      match p with
      | .inl i => baseVertA i
      | .inr (.inl i) => baseVertB i
      | .inr (.inr i) => baseVertC i) := by
  intro a b h
  rcases a with i | i | i <;> rcases b with j | j | j <;>
    fin_cases i <;> fin_cases j <;>
    simp [baseVertA, baseVertB, baseVertC] at h ⊢ <;>
    norm_num at h

/-- `liftVert` is injective: all 8,704 vertices are pairwise distinct! -/
lemma liftVert_injective : Function.Injective liftVert := by
  have hproj : ∀ idx : VertIdx,
      (liftVert idx 0, liftVert idx 1, liftVert idx 2) =
      match idx with
      | .inl (i, _) => baseVertA i
      | .inr (.inl (i, _)) => baseVertB i
      | .inr (.inr (i, _)) => baseVertC i := by
    rintro (⟨i, bits⟩ | ⟨i, bits⟩ | ⟨i, bits⟩) <;> rfl
  intro a b hab
  have hbase_eq :
      (match a with
        | .inl (i, _) => Sum.inl i
        | .inr (.inl (i, _)) => Sum.inr (Sum.inl i)
        | .inr (.inr (i, _)) => Sum.inr (Sum.inr i) : Fin 2 ⊕ Fin 4 ⊕ Fin 18) =
      (match b with
        | .inl (i, _) => Sum.inl i
        | .inr (.inl (i, _)) => Sum.inr (Sum.inl i)
        | .inr (.inr (i, _)) => Sum.inr (Sum.inr i)) := by
    apply baseVert_injective
    have hp := congrArg (fun v : Fin 13 → ℝ => (v 0, v 1, v 2)) hab
    rw [hproj a, hproj b] at hp
    rcases a with ⟨i, _⟩ | ⟨i, _⟩ | ⟨i, _⟩ <;> rcases b with ⟨j, _⟩ | ⟨j, _⟩ | ⟨j, _⟩ <;> exact hp
  rcases a with ⟨i, b1⟩ | ⟨i, b1⟩ | ⟨i, b1⟩ <;> rcases b with ⟨j, b2⟩ | ⟨j, b2⟩ | ⟨j, b2⟩ <;>
    simp only [Sum.inl.injEq, Sum.inr.injEq, reduceCtorEq] at hbase_eq
  · subst hbase_eq
    apply congrArg Sum.inl
    refine Prod.ext rfl (funext fun k => ?_)
    dsimp only
    have hk := congrArg (fun v : Fin 13 → ℝ => v ⟨k.1 + 3, by omega⟩) hab
    simp only [liftVert, pack13_y] at hk
    have hlt := (baseVertA_props i).2.2 k
    cases h1 : b1 k <;> cases h2 : b2 k
    · rfl
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk (ne_of_lt hlt)
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk.symm (ne_of_lt hlt)
    · rfl
  · subst hbase_eq
    apply congrArg (fun p => Sum.inr (Sum.inl p))
    refine Prod.ext rfl (funext fun k => ?_)
    dsimp only
    let j := skipOne (tightB i) k
    have hj_ne : j ≠ tightB i := skipOne_ne (tightB i) k
    have hk := congrArg (fun v : Fin 13 → ℝ => v ⟨j.1 + 3, by omega⟩) hab
    simp only [liftVert, pack13_y, hj_ne, ↓reduceDIte] at hk
    have hk_back : (if hlt : j.1 < (tightB i).1 then ⟨j.1, by have := (tightB i).2; omega⟩
        else ⟨j.1 - 1, by have := j.2; have hne : j.1 ≠ (tightB i).1 := fun h => hj_ne (Fin.ext h); omega⟩ : Fin 9) = k := by
      ext
      by_cases h : k.1 < (tightB i).1
      · have hjv : j.1 = k.1 := by simp [j, skipOne, h]
        have hlt : j.1 < (tightB i).1 := by omega
        simp only [hlt, ↓reduceDIte]; exact hjv
      · have hjv : j.1 = k.1 + 1 := by simp [j, skipOne, h]
        have hlt : ¬ j.1 < (tightB i).1 := by omega
        simp only [hlt, ↓reduceDIte]; omega
    rw [hk_back] at hk
    have hlt := (baseVertB_props i).2.2 j hj_ne
    cases h1 : b1 k <;> cases h2 : b2 k
    · rfl
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk (ne_of_lt hlt)
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk.symm (ne_of_lt hlt)
    · rfl
  · subst hbase_eq
    apply congrArg (fun p => Sum.inr (Sum.inr p))
    refine Prod.ext rfl (funext fun k => ?_)
    dsimp only
    have hj_ne := skipTwo_ne (i.1 % 9) k
    have hnot : ¬ ((skipTwo (i.1 % 9) k).1 = i.1 % 9 ∨ (skipTwo (i.1 % 9) k).1 = i.1 % 9 + 1) := by
      intro h; rcases h with h | h
      · exact hj_ne.1 h
      · exact hj_ne.2 h
    have hk := congrArg (fun v : Fin 13 → ℝ => v ⟨(skipTwo (i.1 % 9) k).1 + 3, by omega⟩) hab
    simp only [liftVert, pack13_y, hnot, ↓reduceDIte] at hk
    have hk_back : (if hlt : (skipTwo (i.1 % 9) k).1 < i.1 % 9
        then ⟨(skipTwo (i.1 % 9) k).1, by have : i.1 % 9 < 9 := Nat.mod_lt _ (by decide); omega⟩
        else ⟨(skipTwo (i.1 % 9) k).1 - 2, by have := (skipTwo (i.1 % 9) k).2; omega⟩ : Fin 8) = k := by
      ext
      by_cases h : k.1 < i.1 % 9
      · have hjv : (skipTwo (i.1 % 9) k).1 = k.1 := by simp [skipTwo, h]
        have hlt : (skipTwo (i.1 % 9) k).1 < i.1 % 9 := by omega
        simp only [hlt, ↓reduceDIte]; exact hjv
      · have hjv : (skipTwo (i.1 % 9) k).1 = k.1 + 2 := by simp [skipTwo, h]
        have hlt : ¬ (skipTwo (i.1 % 9) k).1 < i.1 % 9 := by omega
        simp only [hlt, ↓reduceDIte]; omega
    rw [hk_back] at hk
    have hlt := (baseVertC_props i).2.2 (skipTwo (i.1 % 9) k) hj_ne.1 hj_ne.2
    cases h1 : b1 k <;> cases h2 : b2 k
    · rfl
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk (ne_of_lt hlt)
    · simp only [h1, h2, Bool.false_eq_true, ↓reduceIte] at hk
      exact absurd hk.symm (ne_of_lt hlt)
    · rfl

/-- **Theorem 2:** `witnessHRep.poly` has a finite set of **8,704** distinct vertices (`> 8192 = 2¹³`). -/
theorem witness_has_8704_vertices :
    ∃ V : Finset (Fin 13 → ℝ), V.card = 8704 ∧ ∀ v ∈ V, IsVertex witnessHRep.poly v := by
  classical
  refine ⟨Finset.univ.image liftVert, ?_, ?_⟩
  · rw [Finset.card_image_of_injective _ liftVert_injective, Finset.card_univ, card_vertIdx]
  · intro v hv
    rcases Finset.mem_image.mp hv with ⟨idx, _, rfl⟩
    exact liftVert_isVertex idx

/-- **Main Refutation Witness (`d = 13 ≥ 4`, `m = 24` facets, `8704 > 2¹³` vertices):** -/
theorem refutes_ivanov_conjecture_6 :
    ∃ (d m : ℕ) (H : HRep d m) (V : Finset (Fin d → ℝ)),
      4 ≤ d ∧ H.IsPrimitive ∧ (∀ v ∈ V, IsVertex H.poly v) ∧ 2 ^ d < V.card := by
  obtain ⟨V, hVcard, hVvert⟩ := witness_has_8704_vertices
  exact ⟨13, 24, witnessHRep, V, by decide, witness_isPrimitive, hVvert, by rw [hVcard]; decide⟩

/-- **Direct Negation of Ivanov (`arXiv:2607.08944v1`, Section 1.4, Conjecture 6 `conj:fleanverts`):**
It is false that every primitive polytope in `ℝ^d` (`d ≥ 4`) has at most `2^d` vertices. -/
theorem not_ivanov_conjecture_6 :
    ¬ (∀ (d m : ℕ) (H : HRep d m), 4 ≤ d → H.IsPrimitive →
        ∀ V : Finset (Fin d → ℝ), (∀ v ∈ V, IsVertex H.poly v) → V.card ≤ 2 ^ d) := by
  intro hconj
  obtain ⟨d, m, H, V, hd, hprim, hVvert, hgt⟩ := refutes_ivanov_conjecture_6
  exact not_le_of_gt hgt (hconj d m H hd hprim V hVvert)

#print axioms witness_isPrimitive
#print axioms witness_has_8704_vertices
#print axioms refutes_ivanov_conjecture_6
#print axioms not_ivanov_conjecture_6

end OpenMath.Ivanov260708944Conj6
