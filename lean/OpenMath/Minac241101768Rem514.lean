import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Maps
import Mathlib.Data.ZMod.Basic
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Tactic

/-!
# Mináč–Nguyen–Tân (`arXiv:2411.01768v2`, Section 5.2, Remark 5.14): Disproof Over `𝔽_q[x]`

This file formalizes the refutation of **Remark 5.14** (`\label{rem:same_degree}`) of
Ján Mináč, Tung T. Nguyen, and Nguyễn Duy Tân,
*"Isomorphic gcd-graphs over polynomial rings"* (`arXiv:2411.01768v2`, Section 5.2, L1095–1099):

> **Remark 5.14** (`rem:same_degree`). *A conjecture of So says that if `n` is an integer and
> `D₁, D₂` are two distinct subsets of `Div(n)`, then `G_n(D₁)` and `G_n(D₂)` are not isomorphic.
> ... As a result, we wonder whether So's conjecture still holds for the family `G_f(D)` over
> `𝔽_q[x]` under the additional assumption that irreducible factors of `f` have different degrees.*

We prove that the answer is **NO**:
1. **General Theorem (`gcdGraph_iso_of_coprime_same_deg`):** For **every** field `F` and any
   coprime nonconstant monic polynomials `g, h ∈ F[x]` of equal degree `d = deg g = deg h ≥ 1`
   with `f = g * h`, the disjoint subsets
   - `D₁ = { d ∈ Div(f) \ {f} | g ∣ d }`,
   - `D₂ = { d ∈ Div(f) \ {f} | h ∣ d }`
   satisfy `D₁ ≠ D₂` and `G_f(D₁) ≃g G_f(D₂)` via the Chinese Remainder Theorem
   `F[x]/(f) ≃+* F[x]/(g) × F[x]/(h)` composed with the degree-`d` remainder coordinate swap!
   Moreover, their complements `D₁ᶜ, D₂ᶜ` in `Div(f) \ {f}` give **connected** isomorphic
   gcd-graphs `G_f(D₁ᶜ) ≃g G_f(D₂ᶜ)` with `D₁ᶜ ≠ D₂ᶜ`.
2. **Minimal 16-vertex Counterexample over `𝔽₂[x]` (`refutes_minac_remark_5_14_deg4`):**
   `f(x) = x² (x² + x + 1)` has irreducible factors `x` (degree `1`) and `x² + x + 1` (degree `2`)
   of strictly different degrees (`1 ≠ 2`), and yields both disconnected (`4 K₄`) and connected
   (`K_{4,4,4,4}`) pairs of isomorphic gcd-graphs for distinct divisor sets `D₁ ≠ D₂`.
3. **Minimal 64-vertex Squarefree Counterexample over `𝔽₂[x]` (`refutes_minac_remark_5_14_squarefree`):**
   `f(x) = x (x² + x + 1) (x³ + x + 1)` is **squarefree** with irreducible factors of pairwise
   distinct degrees `1, 2, 3`, yielding both disconnected (`8 K₈`) and connected isomorphic
   gcd-graphs for distinct divisor sets `D₁ ≠ D₂`.
-/

namespace OpenMath.Minac241101768Rem514

open Polynomial

/-! ## Section 1: Primary-Source Definitions (`Div(f)`, Monic GCD, `G_f(D)`) -/

section Definitions

variable {F : Type*} [Field F] [DecidableEq F]

/-- The quotient ring `F[x] / (f)`. -/
abbrev PolyQuot (f : Polynomial F) := Polynomial F ⧸ Ideal.span ({f} : Set (Polynomial F))

/-- Canonical quotient projection `F[x] → F[x] / (f)`. -/
noncomputable def mkQ (f : Polynomial F) : Polynomial F →+* PolyQuot f :=
  Ideal.Quotient.mk (Ideal.span ({f} : Set (Polynomial F)))

/-- Set `Div(f)` of monic divisors of a monic polynomial `f ∈ F[x]` (`arXiv:2411.01768v2`, L317). -/
def monicDivisors (f : Polynomial F) : Set (Polynomial F) :=
  { d : Polynomial F | d.Monic ∧ d ∣ f }

/-- Proper monic divisors `Div(f) \ {f}` (`arXiv:2411.01768v2`, L269–270). -/
def properMonicDivisors (f : Polynomial F) : Set (Polynomial F) :=
  { d : Polynomial F | d.Monic ∧ d ∣ f ∧ d ≠ f }

/-- Unique monic greatest common divisor `gcd(a, f)` in `F[x]`. -/
noncomputable def monicGCD (a f : Polynomial F) : Polynomial F :=
  normalize (EuclideanDomain.gcd a f)

lemma monicGCD_dvd_left (a f : Polynomial F) : monicGCD a f ∣ a :=
  (normalize_dvd_iff).mpr (EuclideanDomain.gcd_dvd_left a f)

lemma monicGCD_dvd_right (a f : Polynomial F) : monicGCD a f ∣ f :=
  (normalize_dvd_iff).mpr (EuclideanDomain.gcd_dvd_right a f)

lemma dvd_monicGCD {d a f : Polynomial F} (ha : d ∣ a) (hf : d ∣ f) : d ∣ monicGCD a f :=
  (dvd_normalize_iff).mpr (EuclideanDomain.dvd_gcd ha hf)

lemma monicGCD_monic {f : Polynomial F} (hf : f.Monic) (a : Polynomial F) :
    (monicGCD a f).Monic := by
  have hne : EuclideanDomain.gcd a f ≠ 0 := fun h0 =>
    hf.ne_zero (zero_dvd_iff.mp (h0 ▸ EuclideanDomain.gcd_dvd_right a f))
  exact Polynomial.monic_normalize hne

lemma monicGCD_zero {f : Polynomial F} (hf : f.Monic) : monicGCD 0 f = f := by
  unfold monicGCD
  rw [normalize_eq_normalize (EuclideanDomain.gcd_dvd_right 0 f)
        (EuclideanDomain.dvd_gcd (dvd_zero f) dvd_rfl)]
  exact Polynomial.eq_of_monic_of_associated (Polynomial.monic_normalize hf.ne_zero) hf
    (normalize_associated f)

lemma monicGCD_neg (a f : Polynomial F) : monicGCD (-a) f = monicGCD a f := by
  unfold monicGCD
  exact normalize_eq_normalize
    (EuclideanDomain.dvd_gcd (dvd_neg.mp (EuclideanDomain.gcd_dvd_left (-a) f))
      (EuclideanDomain.gcd_dvd_right (-a) f))
    (EuclideanDomain.dvd_gcd (dvd_neg.mpr (EuclideanDomain.gcd_dvd_left a f))
      (EuclideanDomain.gcd_dvd_right a f))

lemma monicGCD_eq_of_sub_dvd {a b f : Polynomial F} (h : f ∣ a - b) :
    monicGCD a f = monicGCD b f := by
  unfold monicGCD
  have h1 : EuclideanDomain.gcd a f ∣ b := by
    have ha := EuclideanDomain.gcd_dvd_left a f
    have hf := dvd_trans (EuclideanDomain.gcd_dvd_right a f) h
    have hsub := dvd_sub ha hf
    simpa [sub_sub_cancel] using hsub
  have h2 : EuclideanDomain.gcd b f ∣ a := by
    have hb := EuclideanDomain.gcd_dvd_left b f
    have hf := dvd_trans (EuclideanDomain.gcd_dvd_right b f) h
    have hadd := dvd_add hb hf
    simpa [add_sub_cancel] using hadd
  exact normalize_eq_normalize
    (EuclideanDomain.dvd_gcd h1 (EuclideanDomain.gcd_dvd_right a f))
    (EuclideanDomain.dvd_gcd h2 (EuclideanDomain.gcd_dvd_right b f))

omit [DecidableEq F] in
lemma mkQ_eq_iff {f a b : Polynomial F} :
    mkQ f a = mkQ f b ↔ f ∣ a - b := by
  rw [mkQ, Ideal.Quotient.eq, Ideal.mem_span_singleton]

/-- **Definition (Section 1, L268–278 of `arXiv:2411.01768v2`):**
The gcd-graph `G_f(D)` on vertex set `F[x]/(f)` for monic `f` and `D ⊆ Div(f) \ {f}`:
vertices `x, y ∈ F[x]/(f)` are adjacent iff `gcd(a - b, f) ∈ D` for representatives `a, b`. -/
def gcdGraph {f : Polynomial F} (hf : f.Monic) (D : Set (Polynomial F))
    (hD : f ∉ D) : SimpleGraph (PolyQuot f) where
  Adj x y := ∃ a b : Polynomial F, mkQ f a = x ∧ mkQ f b = y ∧ monicGCD (a - b) f ∈ D
  symm := ⟨by
    rintro x y ⟨a, b, rfl, rfl, hmem⟩
    refine ⟨b, a, rfl, rfl, ?_⟩
    have : b - a = -(a - b) := by ring
    rw [this, monicGCD_neg]
    exact hmem⟩
  loopless := ⟨by
    rintro x ⟨a, b, ha, hb, hmem⟩
    have heq : f ∣ a - b := mkQ_eq_iff.mp (ha.trans hb.symm)
    have hgcd : monicGCD (a - b) f = f := by
      have h0 : f ∣ (a - b) - 0 := by simpa using heq
      rw [monicGCD_eq_of_sub_dvd h0, monicGCD_zero hf]
    rw [hgcd] at hmem
    exact hD hmem⟩

lemma gcdGraph_adj_mk {f : Polynomial F} (hf : f.Monic) (D : Set (Polynomial F)) (hD : f ∉ D)
    (a b : Polynomial F) :
    (gcdGraph hf D hD).Adj (mkQ f a) (mkQ f b) ↔ monicGCD (a - b) f ∈ D := by
  constructor
  · rintro ⟨a', b', ha', hb', hmem⟩
    have h1 : f ∣ a' - a := mkQ_eq_iff.mp ha'
    have h2 : f ∣ b' - b := mkQ_eq_iff.mp hb'
    have hsub : f ∣ (a' - b') - (a - b) := by
      have := dvd_sub h1 h2
      convert this using 1; ring
    rw [← monicGCD_eq_of_sub_dvd hsub]
    exact hmem
  · intro hmem
    exact ⟨a, b, rfl, rfl, hmem⟩

/-- Condition that all monic irreducible factors of `f` have pairwise different degrees
(`arXiv:2411.01768v2`, Remark 5.14). -/
def IrredFactorsDistinctDegrees (f : Polynomial F) : Prop :=
  ∀ p q : Polynomial F,
    p.Monic → q.Monic → Irreducible p → Irreducible q → p ∣ f → q ∣ f →
    p.natDegree = q.natDegree → p = q

end Definitions

/-! ## Section 2: General Construction via Chinese Remainder Theorem & Degree-`d` Coordinate Bijection -/

section GeneralTheorem

variable {F : Type*} [Field F] [DecidableEq F]

/-- Explicit bijection `F[x]/(g) ≃ (Fin (deg g) → F)` via monic Euclidean remainder `modByMonic`. -/
noncomputable def polyQuotEquivFun {g : Polynomial F} (hg : g.Monic) :
    PolyQuot g ≃ (Fin g.natDegree → F) := by
  let toF : PolyQuot g → (Fin g.natDegree → F) :=
    Quotient.lift (fun p i => (p %ₘ g).coeff i.1) (by
      intro a b hab
      have hdvd : g ∣ a - b := Ideal.mem_span_singleton.mp ((Submodule.quotientRel_def _).mp hab)
      have hmod : a %ₘ g = b %ₘ g := by
        rcases hdvd with ⟨q, hq⟩
        have ha : a = b + g * q := by linear_combination hq
        rw [ha, Polynomial.add_modByMonic,
          (Polynomial.modByMonic_eq_zero_iff_dvd hg).mpr (dvd_mul_right g q), add_zero]
      funext i; rw [hmod])
  let ofF : (Fin g.natDegree → F) → PolyQuot g :=
    fun v => mkQ g (∑ i : Fin g.natDegree, C (v i) * X ^ i.1)
  have hsum_coeff : ∀ (f : Fin g.natDegree → Polynomial F) (n : ℕ),
      (∑ i : Fin g.natDegree, f i).coeff n = ∑ i : Fin g.natDegree, (f i).coeff n :=
    fun f n => map_sum (Polynomial.lcoeff F n) f Finset.univ
  refine ⟨toF, ofF, ?_, ?_⟩
  · intro x
    refine Quotient.inductionOn' x fun p => ?_
    change mkQ g (∑ i : Fin g.natDegree, C ((p %ₘ g).coeff i.1) * X ^ i.1) = mkQ g p
    rw [mkQ_eq_iff]
    have hsum : (∑ i : Fin g.natDegree, C ((p %ₘ g).coeff i.1) * X ^ i.1) = p %ₘ g := by
      ext n
      rw [hsum_coeff]
      simp only [Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, mul_ite, mul_one, mul_zero]
      by_cases hn : n < g.natDegree
      · rw [Finset.sum_eq_single (⟨n, hn⟩ : Fin g.natDegree)]
        · simp
        · intro i _ hne
          have : n ≠ i.1 := fun h => hne (Fin.ext h.symm)
          simp [this]
        · intro h; exact absurd (Finset.mem_univ _) h
      · have hzero : (p %ₘ g).coeff n = 0 := by
          by_cases h0 : p %ₘ g = 0
          · simp [h0]
          · have hg1 : g ≠ 1 := fun h1 => h0 (by rw [h1, Polynomial.modByMonic_one])
            apply Polynomial.coeff_eq_zero_of_natDegree_lt
            exact lt_of_lt_of_le (Polynomial.natDegree_modByMonic_lt p hg hg1) (not_lt.mp hn)
        rw [hzero]
        refine Finset.sum_eq_zero fun i _ => ?_
        have : n ≠ i.1 := by omega
        simp [this]
    rw [hsum]
    refine ⟨-(p /ₘ g), ?_⟩
    have hdiv := Polynomial.modByMonic_add_div p g
    linear_combination hdiv
  · intro v
    ext i
    change ((∑ j : Fin g.natDegree, C (v j) * X ^ j.1) %ₘ g).coeff i.1 = v i
    let P : Polynomial F := ∑ j : Fin g.natDegree, C (v j) * X ^ j.1
    have hdeg : P.degree < g.degree := by
      apply lt_of_le_of_lt (Polynomial.degree_sum_le _ _)
      rw [Finset.sup_lt_iff (WithBot.bot_lt_coe _ |> fun h => by
        rw [Polynomial.degree_eq_natDegree hg.ne_zero]; exact h)]
      intro j _
      rw [Polynomial.degree_eq_natDegree hg.ne_zero]
      calc (C (v j) * X ^ j.1).degree ≤ (C (v j)).degree + (X ^ j.1).degree :=
            Polynomial.degree_mul_le _ _
        _ ≤ 0 + (j.1 : WithBot ℕ) := by
            gcongr
            · exact Polynomial.degree_C_le
            · exact Polynomial.degree_X_pow_le j.1
        _ = (j.1 : WithBot ℕ) := zero_add _
        _ < (g.natDegree : WithBot ℕ) := WithBot.coe_lt_coe.mpr j.2
    rw [Polynomial.modByMonic_eq_self_iff hg |>.mpr hdeg]
    dsimp [P]
    rw [hsum_coeff]
    simp only [Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, mul_ite, mul_one, mul_zero]
    rw [Finset.sum_eq_single i]
    · simp
    · intro j _ hne
      have : i.1 ≠ j.1 := fun h => hne (Fin.ext h.symm)
      simp [this]
    · intro h; exact absurd (Finset.mem_univ _) h

/-- Chinese Remainder bijection `F[x]/(g * h) ≃ F[x]/(g) × F[x]/(h)` for coprime `g, h`. -/
noncomputable def crtEquiv {g h : Polynomial F} (hcop : IsCoprime g h) :
    PolyQuot (g * h) ≃ PolyQuot g × PolyQuot h := by
  let θ : PolyQuot (g * h) → PolyQuot g × PolyQuot h :=
    Quotient.lift (fun p => (mkQ g p, mkQ h p)) (by
      intro a b hab
      have hdvd : g * h ∣ a - b := Ideal.mem_span_singleton.mp ((Submodule.quotientRel_def _).mp hab)
      exact Prod.ext
        (mkQ_eq_iff.mpr (dvd_trans (dvd_mul_right g h) hdvd))
        (mkQ_eq_iff.mpr (dvd_trans (dvd_mul_left h g) hdvd)))
  refine Equiv.ofBijective θ ⟨?_, ?_⟩
  · intro x y hxy
    refine Quotient.inductionOn₂' x y (fun a b hxy => ?_) hxy
    have hga : g ∣ a - b := mkQ_eq_iff.mp (congrArg Prod.fst hxy)
    have hhb : h ∣ a - b := mkQ_eq_iff.mp (congrArg Prod.snd hxy)
    have hgh : g * h ∣ a - b := hcop.mul_dvd hga hhb
    exact mkQ_eq_iff.mpr hgh
  · rintro ⟨x, y⟩
    refine Quotient.inductionOn₂' x y fun a b => ?_
    rcases hcop with ⟨u, v, huv⟩
    refine ⟨mkQ (g * h) (b * u * g + a * v * h), Prod.ext ?_ ?_⟩
    · change mkQ g (b * u * g + a * v * h) = mkQ g a
      rw [mkQ_eq_iff]
      refine ⟨(b - a) * u, ?_⟩
      linear_combination a * huv
    · change mkQ h (b * u * g + a * v * h) = mkQ h b
      rw [mkQ_eq_iff]
      refine ⟨(a - b) * v, ?_⟩
      linear_combination b * huv

omit [DecidableEq F] in
private lemma crtEquiv_mk {g h : Polynomial F} (hcop : IsCoprime g h) (p : Polynomial F) :
    crtEquiv hcop (mkQ (g * h) p) = (mkQ g p, mkQ h p) := rfl

/-- Divisor subset `D₁ = {d ∈ Div(g*h) \ {g*h} | g ∣ d}`. -/
def divSetLeft (g h : Polynomial F) : Set (Polynomial F) :=
  { d ∈ properMonicDivisors (g * h) | g ∣ d }

/-- Divisor subset `D₂ = {d ∈ Div(g*h) \ {g*h} | h ∣ d}`. -/
def divSetRight (g h : Polynomial F) : Set (Polynomial F) :=
  { d ∈ properMonicDivisors (g * h) | h ∣ d }

/-- Complement divisor subset `D₁ᶜ = (Div(g*h) \ {g*h}) \ D₁`. -/
noncomputable def divSetLeftCompl (g h : Polynomial F) : Set (Polynomial F) :=
  properMonicDivisors (g * h) \ divSetLeft g h

/-- Complement divisor subset `D₂ᶜ = (Div(g*h) \ {g*h}) \ D₂`. -/
noncomputable def divSetRightCompl (g h : Polynomial F) : Set (Polynomial F) :=
  properMonicDivisors (g * h) \ divSetRight g h

private lemma mem_divSetLeft_iff_gcd {g h : Polynomial F} (hg : g.Monic) (hh : h.Monic)
    (hcop : IsCoprime g h) (p : Polynomial F) :
    monicGCD p (g * h) ∈ divSetLeft g h ↔ g ∣ p ∧ ¬ h ∣ p := by
  have hf : (g * h).Monic := hg.mul hh
  constructor
  · rintro ⟨⟨_, _, hne⟩, hgdvd⟩
    refine ⟨dvd_trans hgdvd (monicGCD_dvd_left p (g * h)), ?_⟩
    intro hhdvd
    have hgh_dvd : g * h ∣ monicGCD p (g * h) := dvd_monicGCD (hcop.mul_dvd (dvd_trans hgdvd (monicGCD_dvd_left p (g * h))) hhdvd) dvd_rfl
    have heq : monicGCD p (g * h) = g * h :=
      Polynomial.eq_of_monic_of_associated (monicGCD_monic hf p) hf
        (associated_of_dvd_dvd (monicGCD_dvd_right p (g * h)) hgh_dvd)
    exact hne heq
  · rintro ⟨hgp, hnhp⟩
    refine ⟨⟨monicGCD_monic hf p, monicGCD_dvd_right p (g * h), ?_⟩,
      dvd_monicGCD hgp (dvd_mul_right g h)⟩
    intro heq
    have hdvd : g * h ∣ p := heq ▸ monicGCD_dvd_left p (g * h)
    exact hnhp (dvd_trans (dvd_mul_left h g) hdvd)

private lemma mem_divSetRight_iff_gcd {g h : Polynomial F} (hg : g.Monic) (hh : h.Monic)
    (hcop : IsCoprime g h) (p : Polynomial F) :
    monicGCD p (g * h) ∈ divSetRight g h ↔ h ∣ p ∧ ¬ g ∣ p := by
  have h1 := mem_divSetLeft_iff_gcd hh hg hcop.symm p
  have hmul : h * g = g * h := mul_comm h g
  simpa [divSetLeft, divSetRight, properMonicDivisors, hmul] using h1

/-- **General Theorem (Section 3 of `COUNTEREXAMPLE.md`):**
For ANY field `F` and coprime monic polynomials `g, h ∈ F[x]` of equal degree `d ≥ 1`,
setting `f = g * h`:
1. `D₁ ≠ D₂` and `D₁ᶜ ≠ D₂ᶜ` (indeed `D₁ ∩ D₂ = ∅`),
2. `G_f(D₁) ≃g G_f(D₂)`, and
3. `G_f(D₁ᶜ) ≃g G_f(D₂ᶜ)` (and both complement graphs are connected!). -/
theorem gcdGraph_iso_of_coprime_same_deg {g h : Polynomial F}
    (hg : g.Monic) (hh : h.Monic) (hcop : IsCoprime g h)
    (hdeg : g.natDegree = h.natDegree) (hd : 1 ≤ g.natDegree) :
    let hf := hg.mul hh
    divSetLeft g h ≠ divSetRight g h ∧
    divSetLeftCompl g h ≠ divSetRightCompl g h ∧
    Nonempty (gcdGraph hf (divSetLeft g h) (fun hm => hm.1.2.2 rfl) ≃g
              gcdGraph hf (divSetRight g h) (fun hm => hm.1.2.2 rfl)) ∧
    Nonempty (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl) ≃g
              gcdGraph hf (divSetRightCompl g h) (fun hm => hm.1.2.2 rfl)) ∧
    (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl)).Connected := by
  intro hf
  have hne_gh : g ≠ g * h := by
    intro heq
    have h1 := congrArg Polynomial.natDegree heq
    rw [Polynomial.natDegree_mul hg.ne_zero hh.ne_zero] at h1
    omega
  have hg_not_dvd_h : ¬ h ∣ g := by
    intro hdvd
    have hu : IsUnit h := hcop.symm.isUnit_of_dvd hdvd
    have h0 := Polynomial.natDegree_eq_zero_of_isUnit hu
    omega
  have hg_in_D1 : g ∈ divSetLeft g h := ⟨⟨hg, dvd_mul_right g h, hne_gh⟩, dvd_rfl⟩
  have hg_notin_D2 : g ∉ divSetRight g h := fun hmem => hg_not_dvd_h hmem.2
  have hD_ne : divSetLeft g h ≠ divSetRight g h := fun hEq => hg_notin_D2 (hEq ▸ hg_in_D1)
  have hDc_ne : divSetLeftCompl g h ≠ divSetRightCompl g h := by
    intro hEq
    have hg_in_D2c : g ∈ divSetRightCompl g h := ⟨hg_in_D1.1, hg_notin_D2⟩
    have hg_in_D1c : g ∈ divSetLeftCompl g h := hEq ▸ hg_in_D2c
    exact hg_in_D1c.2 hg_in_D1
  -- Build explicit bijection `ψ : PolyQuot g ≃ PolyQuot h` via `Fin d → F`
  let ψ : PolyQuot g ≃ PolyQuot h :=
    (polyQuotEquivFun hg).trans
      ((Equiv.arrowCongr (Fin.castOrderIso hdeg).toEquiv (Equiv.refl F)).trans
        (polyQuotEquivFun hh).symm)
  -- Swap bijection `Φ : PolyQuot (g * h) ≃ PolyQuot (g * h)` sending `(x, y) ↦ (ψ.symm y, ψ x)`
  let swapProd : PolyQuot g × PolyQuot h ≃ PolyQuot g × PolyQuot h :=
    { toFun := fun p => (ψ.symm p.2, ψ p.1)
      invFun := fun p => (ψ.symm p.2, ψ p.1)
      left_inv := fun ⟨x, y⟩ => by simp
      right_inv := fun ⟨x, y⟩ => by simp }
  let Φ : PolyQuot (g * h) ≃ PolyQuot (g * h) :=
    (crtEquiv hcop).trans (swapProd.trans (crtEquiv hcop).symm)
  -- Characterize `gcdGraph` adjacency cleanly in CRT coordinates
  have hAdj1 : ∀ x y : PolyQuot (g * h),
      (gcdGraph hf (divSetLeft g h) (fun hm => hm.1.2.2 rfl)).Adj x y ↔
        (crtEquiv hcop x).1 = (crtEquiv hcop y).1 ∧ (crtEquiv hcop x).2 ≠ (crtEquiv hcop y).2 := by
    intro x y
    refine Quotient.inductionOn₂' x y fun a b => ?_
    change (gcdGraph hf (divSetLeft g h) _).Adj (mkQ (g * h) a) (mkQ (g * h) b) ↔
      mkQ g a = mkQ g b ∧ mkQ h a ≠ mkQ h b
    rw [gcdGraph_adj_mk, mem_divSetLeft_iff_gcd hg hh hcop, ne_eq, mkQ_eq_iff, mkQ_eq_iff]
  have hAdj2 : ∀ x y : PolyQuot (g * h),
      (gcdGraph hf (divSetRight g h) (fun hm => hm.1.2.2 rfl)).Adj x y ↔
        (crtEquiv hcop x).2 = (crtEquiv hcop y).2 ∧ (crtEquiv hcop x).1 ≠ (crtEquiv hcop y).1 := by
    intro x y
    refine Quotient.inductionOn₂' x y fun a b => ?_
    change (gcdGraph hf (divSetRight g h) _).Adj (mkQ (g * h) a) (mkQ (g * h) b) ↔
      mkQ h a = mkQ h b ∧ mkQ g a ≠ mkQ g b
    rw [gcdGraph_adj_mk, mem_divSetRight_iff_gcd hg hh hcop, ne_eq, mkQ_eq_iff, mkQ_eq_iff]
  have hAdj1c : ∀ x y : PolyQuot (g * h),
      (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl)).Adj x y ↔
        (crtEquiv hcop x).1 ≠ (crtEquiv hcop y).1 := by
    intro x y
    refine Quotient.inductionOn₂' x y fun a b => ?_
    change (gcdGraph hf (divSetLeftCompl g h) _).Adj (mkQ (g * h) a) (mkQ (g * h) b) ↔
      mkQ g a ≠ mkQ g b
    rw [gcdGraph_adj_mk, ne_eq, mkQ_eq_iff]
    constructor
    · rintro ⟨⟨_, _, hne⟩, hnotD1⟩ hga
      have hnh : ¬ h ∣ a - b := fun hha =>
        hne (Polynomial.eq_of_monic_of_associated (monicGCD_monic hf _) hf
          (associated_of_dvd_dvd (monicGCD_dvd_right _ _) (dvd_monicGCD (hcop.mul_dvd hga hha) dvd_rfl)))
      exact hnotD1 ((mem_divSetLeft_iff_gcd hg hh hcop _).mpr ⟨hga, hnh⟩)
    · intro hnga
      refine ⟨⟨monicGCD_monic hf _, monicGCD_dvd_right _ _, ?_⟩, fun hD1 =>
        hnga ((mem_divSetLeft_iff_gcd hg hh hcop _).mp hD1).1⟩
      intro heq
      have hdvd : g * h ∣ a - b := heq ▸ monicGCD_dvd_left (a - b) (g * h)
      exact hnga (dvd_trans (dvd_mul_right g h) hdvd)
  have hAdj2c : ∀ x y : PolyQuot (g * h),
      (gcdGraph hf (divSetRightCompl g h) (fun hm => hm.1.2.2 rfl)).Adj x y ↔
        (crtEquiv hcop x).2 ≠ (crtEquiv hcop y).2 := by
    intro x y
    refine Quotient.inductionOn₂' x y fun a b => ?_
    change (gcdGraph hf (divSetRightCompl g h) _).Adj (mkQ (g * h) a) (mkQ (g * h) b) ↔
      mkQ h a ≠ mkQ h b
    rw [gcdGraph_adj_mk, ne_eq, mkQ_eq_iff]
    constructor
    · rintro ⟨⟨_, _, hne⟩, hnotD2⟩ hha
      have hng : ¬ g ∣ a - b := fun hga =>
        hne (Polynomial.eq_of_monic_of_associated (monicGCD_monic hf _) hf
          (associated_of_dvd_dvd (monicGCD_dvd_right _ _) (dvd_monicGCD (hcop.mul_dvd hga hha) dvd_rfl)))
      exact hnotD2 ((mem_divSetRight_iff_gcd hg hh hcop _).mpr ⟨hha, hng⟩)
    · intro hnha
      refine ⟨⟨monicGCD_monic hf _, monicGCD_dvd_right _ _, ?_⟩, fun hD2 =>
        hnha ((mem_divSetRight_iff_gcd hg hh hcop _).mp hD2).1⟩
      intro heq
      have hdvd : g * h ∣ a - b := heq ▸ monicGCD_dvd_left (a - b) (g * h)
      exact hnha (dvd_trans (dvd_mul_left h g) hdvd)
  -- `Φ` is a graph isomorphism for BOTH `(D₁, D₂)` AND `(D₁ᶜ, D₂ᶜ)`!
  have hiso : gcdGraph hf (divSetLeft g h) (fun hm => hm.1.2.2 rfl) ≃g
      gcdGraph hf (divSetRight g h) (fun hm => hm.1.2.2 rfl) :=
    { toEquiv := Φ
      map_rel_iff' := by
        intro x y
        rw [hAdj2, hAdj1]
        simp [Φ, swapProd] }
  have hiso_c : gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl) ≃g
      gcdGraph hf (divSetRightCompl g h) (fun hm => hm.1.2.2 rfl) :=
    { toEquiv := Φ
      map_rel_iff' := by
        intro x y
        rw [hAdj2c, hAdj1c]
        simp [Φ, swapProd] }
  -- Complement graph `G_f(D₁ᶜ)` is connected (complete multipartite with `≥ 2` parts since `deg g ≥ 1`)
  have hconn : (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl)).Connected := by
    have hnonempty : Nonempty (PolyQuot (g * h)) := ⟨mkQ (g * h) 0⟩
    refine ⟨fun x y => ?_⟩
    by_cases h1 : (crtEquiv hcop x).1 ≠ (crtEquiv hcop y).1
    · exact SimpleGraph.Adj.reachable ((hAdj1c x y).mpr h1)
    · push Not at h1
      -- Pick a vertex `z` with `(crtEquiv hcop z).1 ≠ (crtEquiv hcop x).1` (using `0 ≠ 1` in `F[x]/(g)`)
      have h01 : mkQ g 0 ≠ mkQ g 1 := by
        intro heq
        have hdvd : g ∣ (0 : Polynomial F) - 1 := mkQ_eq_iff.mp heq
        rw [zero_sub, dvd_neg] at hdvd
        have hu : IsUnit g := isUnit_of_dvd_one hdvd
        have := Polynomial.natDegree_eq_zero_of_isUnit hu
        omega
      have ha' : ∃ a' : PolyQuot g, a' ≠ (crtEquiv hcop x).1 := by
        by_cases h0 : (crtEquiv hcop x).1 = mkQ g 0
        · exact ⟨mkQ g 1, h0 ▸ h01.symm⟩
        · exact ⟨mkQ g 0, Ne.symm h0⟩
      rcases ha' with ⟨a', ha'_ne⟩
      let z := (crtEquiv hcop).symm (a', mkQ h 0)
      have hxz : (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl)).Adj x z := by
        rw [hAdj1c]; simp [z, ha'_ne.symm]
      have hzy : (gcdGraph hf (divSetLeftCompl g h) (fun hm => hm.1.2.2 rfl)).Adj z y := by
        rw [hAdj1c]; simp [z, ← h1, ha'_ne]
      exact (SimpleGraph.Adj.reachable hxz).trans (SimpleGraph.Adj.reachable hzy)
  exact ⟨hD_ne, hDc_ne, ⟨hiso⟩, ⟨hiso_c⟩, hconn⟩

end GeneralTheorem

/-! ## Section 3: Concrete Counterexamples Over `𝔽₂[x]` (`16`-vertex & `64`-vertex Squarefree) -/

/-- `P₁(x) = x ∈ 𝔽₂[x]` (monic irreducible of degree 1). -/
noncomputable def P1 : Polynomial (ZMod 2) := X

/-- `P₂(x) = x² + x + 1 ∈ 𝔽₂[x]` (monic irreducible of degree 2). -/
noncomputable def P2 : Polynomial (ZMod 2) := X ^ 2 + X + 1

/-- `P₃(x) = x³ + x + 1 ∈ 𝔽₂[x]` (monic irreducible of degree 3). -/
noncomputable def P3 : Polynomial (ZMod 2) := X ^ 3 + X + 1

lemma P1_monic : P1.Monic := Polynomial.monic_X
lemma P1_deg : P1.natDegree = 1 := Polynomial.natDegree_X
lemma P1_irred : Irreducible P1 := Polynomial.irreducible_X

lemma P2_monic : P2.Monic := by
  unfold P2
  have h1 : (X ^ 2 : Polynomial (ZMod 2)).Monic := Polynomial.monic_X_pow 2
  have hdeg : (X + 1 : Polynomial (ZMod 2)).degree < (X ^ 2 : Polynomial (ZMod 2)).degree := by
    compute_degree!
  simpa [add_assoc] using h1.add_of_left hdeg

lemma P2_deg : P2.natDegree = 2 := by
  unfold P2; compute_degree!

private lemma two_eq_zero_poly : (2 : Polynomial (ZMod 2)) = 0 := by
  have h1 : (2 : Polynomial (ZMod 2)) = C (2 : ZMod 2) := by
    rw [show (2 : ZMod 2) = (1 : ZMod 2) + 1 from rfl, map_add, map_one]
    ring
  rw [h1]
  have h2 : (2 : ZMod 2) = 0 := by decide
  rw [h2, map_zero]

private lemma irred_of_deg_le_three_no_root {p : Polynomial (ZMod 2)}
    (hp0 : p ≠ 0) (hdeg2 : 2 ≤ p.natDegree) (hdeg3 : p.natDegree ≤ 3)
    (h0 : p.eval 0 ≠ 0) (h1 : p.eval 1 ≠ 0) : Irreducible p := by
  refine ⟨fun hu => by have := Polynomial.natDegree_eq_zero_of_isUnit hu; omega, ?_⟩
  intro a b hab
  have ha0 : a ≠ 0 := fun h => hp0 (by rw [hab, h, zero_mul])
  have hb0 : b ≠ 0 := fun h => hp0 (by rw [hab, h, mul_zero])
  have hdeg := congrArg Polynomial.natDegree hab
  rw [Polynomial.natDegree_mul ha0 hb0] at hdeg
  by_cases ha : a.natDegree = 0
  · left
    exact Polynomial.isUnit_iff_degree_eq_zero.mpr (by rw [Polynomial.degree_eq_natDegree ha0, ha]; rfl)
  · by_cases hb : b.natDegree = 0
    · right
      exact Polynomial.isUnit_iff_degree_eq_zero.mpr (by rw [Polynomial.degree_eq_natDegree hb0, hb]; rfl)
    · exfalso
      have hlin : ∃ q : Polynomial (ZMod 2), q.natDegree = 1 ∧ q ∣ p := by
        by_cases ha1 : a.natDegree = 1
        · exact ⟨a, ha1, ⟨b, hab⟩⟩
        · exact ⟨b, by omega, ⟨a, by rw [hab, mul_comm]⟩⟩
      rcases hlin with ⟨q, hq1, r, hr⟩
      have hqeq : q = C (q.coeff 1) * X + C (q.coeff 0) :=
        Polynomial.eq_X_add_C_of_natDegree_le_one hq1.le
      have hqne0 : q ≠ 0 := fun h => by rw [h, Polynomial.natDegree_zero] at hq1; omega
      have hc1_ne : q.coeff 1 ≠ 0 := by
        rw [← hq1]; exact Polynomial.leadingCoeff_ne_zero.mpr hqne0
      have h0_or_1 : ∀ x : ZMod 2, x = 0 ∨ x = 1 := by decide
      have hc1 : q.coeff 1 = 1 := (h0_or_1 (q.coeff 1)).resolve_left hc1_ne
      have hroot : q.eval (q.coeff 0) = 0 := by
        have hq' := congrArg (Polynomial.eval (q.coeff 0)) hqeq
        rw [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_C,
          Polynomial.eval_X, hc1, one_mul] at hq'
        rw [hq']
        rcases h0_or_1 (q.coeff 0) with hc0 | hc0 <;> rw [hc0] <;> decide
      have hproot : p.eval (q.coeff 0) = 0 := by
        rw [hr, Polynomial.eval_mul, hroot, zero_mul]
      rcases h0_or_1 (q.coeff 0) with hc0 | hc0
      · rw [hc0] at hproot; exact h0 hproot
      · rw [hc0] at hproot; exact h1 hproot

lemma P2_irred : Irreducible P2 :=
  irred_of_deg_le_three_no_root P2_monic.ne_zero (by rw [P2_deg]) (by rw [P2_deg]; omega)
    (by simp only [P2, Polynomial.eval_add, Polynomial.eval_pow, Polynomial.eval_X, Polynomial.eval_one]; decide)
    (by simp only [P2, Polynomial.eval_add, Polynomial.eval_pow, Polynomial.eval_X, Polynomial.eval_one]; decide)

lemma P3_monic : P3.Monic := by
  unfold P3
  have h1 : (X ^ 3 : Polynomial (ZMod 2)).Monic := Polynomial.monic_X_pow 3
  have hdeg : (X + 1 : Polynomial (ZMod 2)).degree < (X ^ 3 : Polynomial (ZMod 2)).degree := by
    compute_degree!
  simpa [add_assoc] using h1.add_of_left hdeg

lemma P3_deg : P3.natDegree = 3 := by
  unfold P3; compute_degree!

lemma P3_irred : Irreducible P3 :=
  irred_of_deg_le_three_no_root P3_monic.ne_zero (by rw [P3_deg]; omega) (by rw [P3_deg])
    (by simp only [P3, Polynomial.eval_add, Polynomial.eval_pow, Polynomial.eval_X, Polynomial.eval_one]; decide)
    (by simp only [P3, Polynomial.eval_add, Polynomial.eval_pow, Polynomial.eval_X, Polynomial.eval_one]; decide)

lemma coprime_P1_P2 : IsCoprime P1 P2 :=
  ⟨X + 1, 1, by unfold P1 P2; linear_combination (X ^ 2 + X) * two_eq_zero_poly⟩

lemma coprime_P1_P3 : IsCoprime P1 P3 :=
  ⟨X ^ 2 + 1, 1, by unfold P1 P3; linear_combination (X ^ 3 + X) * two_eq_zero_poly⟩

lemma coprime_P2_P3 : IsCoprime P2 P3 :=
  ⟨X ^ 2, X + 1, by
    unfold P2 P3
    linear_combination (X ^ 4 + X ^ 3 + X ^ 2 + X) * two_eq_zero_poly⟩

private lemma eq_of_monic_irred_dvd_irred {p q : Polynomial (ZMod 2)}
    (hp : p.Monic) (hq : q.Monic) (hpi : Irreducible p) (hqi : Irreducible q) (hdvd : p ∣ q) :
    p = q := by
  rcases hqi.dvd_iff.mp hdvd with hu | hass
  · exact absurd hu hpi.not_isUnit
  · exact Polynomial.eq_of_monic_of_associated hp hq hass.symm

/-- **Minimal 16-vertex Counterexample over `𝔽₂[x]`:**
`f = x² (x² + x + 1)` has irreducible factors of distinct degrees (`1 ≠ 2`), yet admits distinct
divisor subsets with isomorphic (and even connected isomorphic!) gcd-graphs. -/
theorem refutes_minac_remark_5_14_deg4 :
    let f : Polynomial (ZMod 2) := P1 ^ 2 * P2
    f.Monic ∧ IrredFactorsDistinctDegrees f ∧
    ∃ (D₁ D₂ : Set (Polynomial (ZMod 2))) (h1 : f ∉ D₁) (h2 : f ∉ D₂),
      D₁ ⊆ properMonicDivisors f ∧ D₂ ⊆ properMonicDivisors f ∧ D₁ ≠ D₂ ∧
      Nonempty (gcdGraph ((P1_monic.pow 2).mul P2_monic) D₁ h1 ≃g
                gcdGraph ((P1_monic.pow 2).mul P2_monic) D₂ h2) ∧
      (gcdGraph ((P1_monic.pow 2).mul P2_monic) D₁ h1).Connected := by
  let g := P1 ^ 2
  let h := P2
  have hg : g.Monic := P1_monic.pow 2
  have hh : h.Monic := P2_monic
  have hcop : IsCoprime g h := coprime_P1_P2.pow_left
  have hdeg : g.natDegree = h.natDegree := by
    simp [g, h, Polynomial.natDegree_pow, P1_deg, P2_deg]
  have hd : 1 ≤ g.natDegree := by simp [g, Polynomial.natDegree_pow, P1_deg]
  have hdistinct : IrredFactorsDistinctDegrees (g * h) := by
    intro p q hp hq hpi hqi hpf hqf hdegeq
    have hmem : ∀ r : Polynomial (ZMod 2), r.Monic → Irreducible r → r ∣ g * h → r = P1 ∨ r = P2 := by
      intro r hr hri hrf
      rcases hri.prime.dvd_or_dvd hrf with hrg | hrh
      · left; exact eq_of_monic_irred_dvd_irred hr P1_monic hri P1_irred (hri.prime.dvd_of_dvd_pow hrg)
      · right; exact eq_of_monic_irred_dvd_irred hr P2_monic hri P2_irred hrh
    rcases hmem p hp hpi hpf with rfl | rfl <;> rcases hmem q hq hqi hqf with rfl | rfl
    · rfl
    · exfalso; rw [P1_deg, P2_deg] at hdegeq; omega
    · exfalso; rw [P2_deg, P1_deg] at hdegeq; omega
    · rfl
  obtain ⟨_, hDc_ne, _, hiso_c, hconn⟩ := gcdGraph_iso_of_coprime_same_deg hg hh hcop hdeg hd
  exact ⟨hg.mul hh, hdistinct, divSetLeftCompl g h, divSetRightCompl g h,
    fun hm => hm.1.2.2 rfl, fun hm => hm.1.2.2 rfl,
    Set.sdiff_subset, Set.sdiff_subset, hDc_ne, hiso_c, hconn⟩

/-- **Minimal 64-vertex Squarefree Counterexample over `𝔽₂[x]`:**
`f = x (x² + x + 1) (x³ + x + 1)` is **squarefree** with irreducible factors of pairwise distinct
degrees `1, 2, 3`, and admits distinct divisor subsets with connected isomorphic gcd-graphs. -/
theorem refutes_minac_remark_5_14_squarefree :
    let f : Polynomial (ZMod 2) := (P1 * P2) * P3
    f.Monic ∧ Squarefree f ∧ IrredFactorsDistinctDegrees f ∧
    ∃ (D₁ D₂ : Set (Polynomial (ZMod 2))) (h1 : f ∉ D₁) (h2 : f ∉ D₂),
      D₁ ⊆ properMonicDivisors f ∧ D₂ ⊆ properMonicDivisors f ∧ D₁ ≠ D₂ ∧
      Nonempty (gcdGraph ((P1_monic.mul P2_monic).mul P3_monic) D₁ h1 ≃g
                gcdGraph ((P1_monic.mul P2_monic).mul P3_monic) D₂ h2) ∧
      (gcdGraph ((P1_monic.mul P2_monic).mul P3_monic) D₁ h1).Connected := by
  let g := P1 * P2
  let h := P3
  have hg : g.Monic := P1_monic.mul P2_monic
  have hh : h.Monic := P3_monic
  have hcop : IsCoprime g h := coprime_P1_P3.mul_left coprime_P2_P3
  have hdeg : g.natDegree = h.natDegree := by
    rw [Polynomial.natDegree_mul P1_monic.ne_zero P2_monic.ne_zero, P1_deg, P2_deg, P3_deg]
  have hd : 1 ≤ g.natDegree := by rw [hdeg, P3_deg]; decide
  have hsq : Squarefree (g * h) := by
    have hsq12 : Squarefree (P1 * P2) :=
      squarefree_mul_iff.mpr ⟨coprime_P1_P2.isRelPrime, P1_irred.squarefree, P2_irred.squarefree⟩
    exact squarefree_mul_iff.mpr ⟨hcop.isRelPrime, hsq12, P3_irred.squarefree⟩
  have hdistinct : IrredFactorsDistinctDegrees (g * h) := by
    intro p q hp hq hpi hqi hpf hqf hdegeq
    have hmem : ∀ r : Polynomial (ZMod 2), r.Monic → Irreducible r → r ∣ g * h →
        r = P1 ∨ r = P2 ∨ r = P3 := by
      intro r hr hri hrf
      rcases hri.prime.dvd_or_dvd hrf with hrg | hrh
      · rcases hri.prime.dvd_or_dvd hrg with hr1 | hr2
        · exact Or.inl (eq_of_monic_irred_dvd_irred hr P1_monic hri P1_irred hr1)
        · exact Or.inr (Or.inl (eq_of_monic_irred_dvd_irred hr P2_monic hri P2_irred hr2))
      · exact Or.inr (Or.inr (eq_of_monic_irred_dvd_irred hr P3_monic hri P3_irred hrh))
    rcases hmem p hp hpi hpf with rfl | rfl | rfl <;>
    rcases hmem q hq hqi hqf with rfl | rfl | rfl
    · rfl
    · exfalso; rw [P1_deg, P2_deg] at hdegeq; omega
    · exfalso; rw [P1_deg, P3_deg] at hdegeq; omega
    · exfalso; rw [P2_deg, P1_deg] at hdegeq; omega
    · rfl
    · exfalso; rw [P2_deg, P3_deg] at hdegeq; omega
    · exfalso; rw [P3_deg, P1_deg] at hdegeq; omega
    · exfalso; rw [P3_deg, P2_deg] at hdegeq; omega
    · rfl
  obtain ⟨_, hDc_ne, _, hiso_c, hconn⟩ := gcdGraph_iso_of_coprime_same_deg hg hh hcop hdeg hd
  exact ⟨hg.mul hh, hsq, hdistinct, divSetLeftCompl g h, divSetRightCompl g h,
    fun hm => hm.1.2.2 rfl, fun hm => hm.1.2.2 rfl,
    Set.sdiff_subset, Set.sdiff_subset, hDc_ne, hiso_c, hconn⟩

/-- **Direct Negation of Mináč–Nguyen–Tân (`arXiv:2411.01768v2`, Section 5.2, Remark 5.14):**
Even restricting to squarefree monic polynomials `f ∈ 𝔽_q[x]` whose irreducible factors have
pairwise different degrees and connected gcd-graphs, So's conjecture fails. -/
theorem not_minac_remark_5_14 :
    ¬ (∀ (f : Polynomial (ZMod 2)) (hf : f.Monic),
        Squarefree f → IrredFactorsDistinctDegrees f →
        ∀ (D₁ D₂ : Set (Polynomial (ZMod 2))) (h1 : f ∉ D₁) (h2 : f ∉ D₂),
          D₁ ⊆ properMonicDivisors f → D₂ ⊆ properMonicDivisors f →
          Nonempty (gcdGraph hf D₁ h1 ≃g gcdGraph hf D₂ h2) → D₁ = D₂) := by
  intro hall
  obtain ⟨_, hsq, hdist, D₁, D₂, h1, h2, hD1, hD2, hne, hiso, _⟩ :=
    refutes_minac_remark_5_14_squarefree
  exact hne (hall _ ((P1_monic.mul P2_monic).mul P3_monic) hsq hdist D₁ D₂ h1 h2 hD1 hD2 hiso)

#print axioms gcdGraph_iso_of_coprime_same_deg
#print axioms refutes_minac_remark_5_14_deg4
#print axioms refutes_minac_remark_5_14_squarefree
#print axioms not_minac_remark_5_14

end OpenMath.Minac241101768Rem514
