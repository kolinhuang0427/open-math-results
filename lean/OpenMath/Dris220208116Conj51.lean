import Mathlib.NumberTheory.LSeries.PrimesInAP
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.ZMod.QuotientRing
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# Proof of Conjecture 5.1 of Dris (`arXiv:2202.08116v1`)

Primary source:
Jose Arnaldo Bebita Dris, *"A new approach to odd perfect numbers via GCDs"*,
`arXiv:2202.08116v1` [math.NT], Abstract (lines 57–59) & Section 5 Conjecture 5.1
(`\label{AsymptoticDensity2}`, lines 386–391):

> The asymptotic density `A` of positive integers `m` with
> `gcd(m, σ(m²)) = gcd(m², σ(m²))` satisfies `A = 0`.

We give a complete, zero-`sorry` proof in Lean 4:
1. **Prime reciprocal divergence in arithmetic progressions (`not_summable_one_div_primes_modEq`):**
   Derived directly from Mathlib's `ArithmeticFunction.vonMangoldt.LSeries_residueClass_lower_bound`
   and `summable_residueClass_non_primes_div` via an elementary dyadic telescoping sum.
2. **Lemma 1 (`not_mem_drisSet_of_prime_witnesses`):**
   For any prime `p ≡ 1 (mod 6)`, `(ZMod p)ˣ` contains an element of order `3` (by Cauchy's
   theorem `exists_prime_orderOf_dvd_card`), yielding a residue `r_p` coprime to `p` such that
   every prime `q ≡ r_p (mod p)` satisfies `p ∣ σ(q²) = 1 + q + q²`. If `p ∥ m` and two distinct
   such primes `q₁, q₂` satisfy `q₁ ∥ m` and `q₂ ∥ m`, then `p² ∣ σ(m²)`, forcing `m ∉ DrisSet`.
3. **Periodic CRT density & Chebyshev bound (`densityRatio_periodic_le`, `chebyshev_bad_card_le`):**
   Exact finite-product cardinality and variance bounds on `ZMod (∏ q ∈ S, q²) ≃+* Π q : S, ZMod (q²)`.
4. **Main theorem (`dris_conjecture_5_1`):**
   `Filter.Tendsto (densityRatio DrisSet) Filter.atTop (nhds 0)`.
-/

namespace OpenMath.Dris220208116Conj51

open scoped ArithmeticFunction.sigma BigOperators Classical
open Filter Topology

/-! ## Section 0: Exact Primary-Source Statement -/

/-- The set `A = {m ∈ ℤ_{≥ 1} : gcd(m, σ(m²)) = gcd(m², σ(m²))}` from Dris (`arXiv:2202.08116v1`). -/
def DrisSet : Set ℕ :=
  {m : ℕ | 1 ≤ m ∧ Nat.gcd m (σ 1 (m ^ 2)) = Nat.gcd (m ^ 2) (σ 1 (m ^ 2))}

/-- The counting ratio `|S ∩ {1, ..., X}| / X` for asymptotic density. -/
noncomputable def densityRatio (S : Set ℕ) (X : ℕ) : ℝ :=
  (((Finset.Icc 1 X).filter (· ∈ S)).card : ℝ) / (X : ℝ)

/-! ## Section 1: Divergence of `∑_{p ≡ a [MOD q]} 1/p` from Mathlib's `PrimesInAP` -/

section PrimeReciprocalDivergence

open ArithmeticFunction.vonMangoldt

/-- Elementary dyadic telescoping bound: for every `u > 0` and `M : ℕ`,
`∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k) ≤ 2 / u`. -/
lemma dyadic_exp_sum_le {u : ℝ} (hu : 0 < u) (M : ℕ) :
    ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k) ≤ 2 / u := by
  have hstep : ∀ k : ℕ,
      u * ((2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) ≤
        2 * (Real.exp (-u * (2 : ℝ)⁻¹ ^ (k + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) := by
    intro k
    have h1 := Real.add_one_le_exp (u * (2 : ℝ)⁻¹ ^ (k + 1))
    have hexp_pos : 0 < Real.exp (-u * (2 : ℝ)⁻¹ ^ k) := Real.exp_pos _
    have hmul := mul_le_mul_of_nonneg_right h1 hexp_pos.le
    have hpow : u * (2 : ℝ)⁻¹ ^ (k + 1) + (-u * (2 : ℝ)⁻¹ ^ k) = -u * (2 : ℝ)⁻¹ ^ (k + 1) := by
      rw [pow_succ]; ring
    rw [← Real.exp_add, hpow] at hmul
    have hmul2 : u * (2 : ℝ)⁻¹ ^ (k + 1) * Real.exp (-u * (2 : ℝ)⁻¹ ^ k) ≤
        Real.exp (-u * (2 : ℝ)⁻¹ ^ (k + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ k) := by
      linarith
    have h2 : u * ((2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) =
        2 * (u * (2 : ℝ)⁻¹ ^ (k + 1) * Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) := by
      rw [pow_succ]; ring
    linarith
  have hsum :
      u * (∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) ≤
        2 * (Real.exp (-u * (2 : ℝ)⁻¹ ^ (M + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ 0)) := by
    rw [Finset.mul_sum]
    calc
      ∑ k ∈ Finset.range (M + 1), u * ((2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k))
          ≤ ∑ k ∈ Finset.range (M + 1),
              2 * (Real.exp (-u * (2 : ℝ)⁻¹ ^ (k + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) :=
            Finset.sum_le_sum fun k _ => hstep k
      _ = 2 * ∑ k ∈ Finset.range (M + 1),
              (Real.exp (-u * (2 : ℝ)⁻¹ ^ (k + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) := by
            rw [← Finset.mul_sum]
      _ = 2 * (Real.exp (-u * (2 : ℝ)⁻¹ ^ (M + 1)) - Real.exp (-u * (2 : ℝ)⁻¹ ^ 0)) := by
            rw [Finset.sum_range_sub (fun k => Real.exp (-u * (2 : ℝ)⁻¹ ^ k))]
  have hle1 : Real.exp (-u * (2 : ℝ)⁻¹ ^ (M + 1)) ≤ 1 := by
    rw [Real.exp_le_one_iff]
    have : 0 ≤ u * (2 : ℝ)⁻¹ ^ (M + 1) := by positivity
    linarith
  have hpos0 : 0 ≤ Real.exp (-u * (2 : ℝ)⁻¹ ^ 0) := (Real.exp_pos _).le
  have hfinal :
      u * (∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * Real.exp (-u * (2 : ℝ)⁻¹ ^ k)) ≤ 2 := by
    linarith
  exact (le_div_iff₀ hu).mpr (by linarith)

/-- For any `n ≥ 2` and `M : ℕ`,
`∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k) ≤ 2 / ((n : ℝ) * Real.log n)`. -/
lemma dyadic_rpow_sum_le {n : ℕ} (hn : 2 ≤ n) (M : ℕ) :
    ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k) ≤
      2 / ((n : ℝ) * Real.log n) := by
  have hn_pos : (0 : ℝ) < n := by positivity
  have hn_gt1 : (1 : ℝ) < n := by exact_mod_cast (by omega : 1 < n)
  have hlog_pos : 0 < Real.log (n : ℝ) := Real.log_pos hn_gt1
  have hterm : ∀ k : ℕ,
      (2 : ℝ)⁻¹ ^ k / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k) =
        ((n : ℝ)⁻¹) * ((2 : ℝ)⁻¹ ^ k * Real.exp (-Real.log (n : ℝ) * (2 : ℝ)⁻¹ ^ k)) := by
    intro k
    rw [Real.rpow_add hn_pos, Real.rpow_one, Real.rpow_def_of_pos hn_pos]
    rw [div_eq_mul_inv, mul_inv, ← Real.exp_neg, ← neg_mul]
    ring
  simp_rw [hterm, ← Finset.mul_sum]
  calc
    (n : ℝ)⁻¹ * ∑ k ∈ Finset.range (M + 1),
        (2 : ℝ)⁻¹ ^ k * Real.exp (-Real.log (n : ℝ) * (2 : ℝ)⁻¹ ^ k)
      ≤ (n : ℝ)⁻¹ * (2 / Real.log (n : ℝ)) :=
          mul_le_mul_of_nonneg_left (dyadic_exp_sum_le hlog_pos M) (by positivity)
    _ = 2 / ((n : ℝ) * Real.log (n : ℝ)) := by ring

/-- Divergence of `∑_{p ≡ a [MOD q]} 1 / p` for any `q ≥ 1` and invertible `a : ZMod q`. -/
theorem not_summable_one_div_primes_eq_mod {q : ℕ} [NeZero q] {a : ZMod q} (ha : IsUnit a) :
    ¬ Summable (fun n : ℕ ↦ if n.Prime ∧ (n : ZMod q) = a then (1 : ℝ) / (n : ℝ) else 0) := by
  intro hsum_p
  have hsum_np : Summable fun n : ℕ ↦ (if n.Prime then 0 else residueClass a n) / (n : ℝ) :=
    summable_residueClass_non_primes_div a
  -- Combine prime and non-prime bounds: `g n := (if n.Prime ∧ n = a then 2 / n else 0) + 2 * nonprime`.
  let g : ℕ → ℝ := fun n =>
    2 * (if n.Prime ∧ (n : ZMod q) = a then (1 : ℝ) / (n : ℝ) else 0) +
    2 * ((if n.Prime then 0 else residueClass a n) / (n : ℝ))
  have hg_sum : Summable g := (hsum_p.mul_left 2).add (hsum_np.mul_left 2)
  obtain ⟨C, hC⟩ := LSeries_residueClass_lower_bound ha
  -- For any `M : ℕ`, sum the lower bound at `x_k = 1 + 2^{-k}` weighted by `2^{-k}`.
  have hM_bound : ∀ M : ℕ, ((M + 1 : ℕ) : ℝ) * (q.totient : ℝ)⁻¹ - 2 * |C| ≤ ∑' n, g n := by
    intro M
    have hterm_summable : ∀ k : ℕ,
        Summable fun n : ℕ => (2 : ℝ)⁻¹ ^ k * (residueClass a n / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k)) := by
      intro k
      apply Summable.mul_left
      refine LSeries.summable_real_of_abscissaOfAbsConv_lt ?_
      refine (abscissaOfAbsConv_residueClass_le_one a).trans_lt ?_
      have hpos : (0 : ℝ) < (2 : ℝ)⁻¹ ^ k := by positivity
      exact_mod_cast (by linarith : (1 : ℝ) < 1 + (2 : ℝ)⁻¹ ^ k)
    have hlower :
        ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * ((q.totient : ℝ)⁻¹ / ((1 + (2 : ℝ)⁻¹ ^ k) - 1) - C) ≤
        ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * (∑' n, residueClass a n / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k)) := by
      refine Finset.sum_le_sum fun k _ => ?_
      refine mul_le_mul_of_nonneg_left (hC ?_) (by positivity)
      constructor
      · have : (0 : ℝ) < (2 : ℝ)⁻¹ ^ k := by positivity
        linarith
      · have : (2 : ℝ)⁻¹ ^ k ≤ 1 := pow_le_one₀ (by positivity) (by norm_num)
        linarith
    -- Simplify the LHS of `hlower`.
    have hlhs :
        ((M + 1 : ℕ) : ℝ) * (q.totient : ℝ)⁻¹ - 2 * |C| ≤
        ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * ((q.totient : ℝ)⁻¹ / ((1 + (2 : ℝ)⁻¹ ^ k) - 1) - C) := by
      have hsimp : ∀ k : ℕ,
          (2 : ℝ)⁻¹ ^ k * ((q.totient : ℝ)⁻¹ / ((1 + (2 : ℝ)⁻¹ ^ k) - 1) - C) =
            (q.totient : ℝ)⁻¹ - C * (2 : ℝ)⁻¹ ^ k := by
        intro k
        have hpos : (2 : ℝ)⁻¹ ^ k ≠ 0 := by positivity
        rw [add_sub_cancel_left]
        field_simp [hpos]
      simp_rw [hsimp, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
        ← Finset.mul_sum]
      have hgeom : ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k ≤ 2 := by
        have hsum_g := geom_sum_eq (show (2 : ℝ)⁻¹ ≠ 1 by norm_num) (M + 1)
        rw [hsum_g]
        have hdiv : ((2 : ℝ)⁻¹ ^ (M + 1) - 1) / ((2 : ℝ)⁻¹ - 1) = 2 - 2 * (2 : ℝ)⁻¹ ^ (M + 1) := by
          ring
        rw [hdiv]
        have : (0 : ℝ) ≤ (2 : ℝ)⁻¹ ^ (M + 1) := by positivity
        linarith
      have hgeom_nn : 0 ≤ ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k :=
        Finset.sum_nonneg fun _ _ => by positivity
      have hC_le : C * ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k ≤ 2 * |C| := by
        calc
          C * ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k
              ≤ |C| * ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k :=
                mul_le_mul_of_nonneg_right (le_abs_self C) hgeom_nn
          _ ≤ |C| * 2 := mul_le_mul_of_nonneg_left hgeom (abs_nonneg C)
          _ = 2 * |C| := by ring
      linarith
    -- Swap finite sum and tsum on the RHS, and bound termwise by `g n`.
    have hrhs :
        ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * (∑' n, residueClass a n / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k)) ≤
        ∑' n, g n := by
      simp_rw [← tsum_mul_left]
      rw [← Summable.tsum_finsetSum (fun k _ => hterm_summable k)]
      refine Summable.tsum_le_tsum (fun n => ?_)
        (summable_sum fun k _ => hterm_summable k) hg_sum
      -- Termwise bound for `n : ℕ`.
      by_cases hn2 : 2 ≤ n
      · have hfactor :
            ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k * (residueClass a n / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k)) =
              residueClass a n * ∑ k ∈ Finset.range (M + 1), (2 : ℝ)⁻¹ ^ k / (n : ℝ) ^ (1 + (2 : ℝ)⁻¹ ^ k) := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun k _ => by ring
        rw [hfactor]
        have hdyad := mul_le_mul_of_nonneg_left (dyadic_rpow_sum_le hn2 M) (residueClass_nonneg a n)
        refine hdyad.trans ?_
        dsimp only [g]
        by_cases hp : n.Prime
        · by_cases hmod : (n : ZMod q) = a
          · have hlog_pos : 0 < Real.log (n : ℝ) :=
              Real.log_pos (by exact_mod_cast hp.one_lt)
            have hrc : residueClass a n = Real.log (n : ℝ) := by
              simp [residueClass, Set.indicator, hmod, ArithmeticFunction.vonMangoldt_apply_prime hp]
            simp only [hp, hmod, and_self, ↓reduceIte, zero_div, mul_zero, add_zero, hrc]
            have hlog_ne : Real.log (n : ℝ) ≠ 0 := hlog_pos.ne'
            have hn_ne : (n : ℝ) ≠ 0 := by positivity
            have : Real.log (n : ℝ) * (2 / ((n : ℝ) * Real.log (n : ℝ))) = 2 * (1 / (n : ℝ)) := by
              field_simp [hlog_ne, hn_ne]
            exact this.le
          · have hrc : residueClass a n = 0 := by
              simp [residueClass, Set.indicator, hmod]
            rw [hrc]
            simp [hp, hmod]
        · -- Non-prime `n ≥ 2`: either `residueClass a n = 0` or `n ≥ 4`, where `Real.log n ≥ 1`.
          simp only [hp, false_and, ↓reduceIte, mul_zero, zero_add]
          by_cases hrc0 : residueClass a n = 0
          · rw [hrc0]; simp
          · have hpp : IsPrimePow n := by
              by_contra hnotpp
              apply hrc0
              have hv0 : ArithmeticFunction.vonMangoldt n = 0 :=
                ArithmeticFunction.vonMangoldt_eq_zero_iff.mpr hnotpp
              simp [residueClass, Set.indicator, hv0]
            have hn4 : 4 ≤ n := by
              obtain ⟨p, k, hp_p, hk_pos, rfl⟩ := hpp
              have hk2 : 2 ≤ k := by
                by_contra hlt
                have hk1 : k = 1 := by omega
                subst hk1
                rw [pow_one] at hp
                exact hp hp_p.nat_prime
              have hp2 : 2 ≤ p := hp_p.nat_prime.two_le
              calc
                4 = 2 ^ 2 := by norm_num
                _ ≤ p ^ 2 := Nat.pow_le_pow_left hp2 2
                _ ≤ p ^ k := Nat.pow_le_pow_right (by omega) hk2
            have hlog_ge1 : (1 : ℝ) ≤ Real.log (n : ℝ) := by
              have hhalf : (1 / 2 : ℝ) ≤ Real.exp (-(1 / 2 : ℝ)) := by
                have := Real.add_one_le_exp (-(1 / 2 : ℝ)); linarith
              have hexp_half : Real.exp (1 / 2 : ℝ) ≤ 2 := by
                rw [Real.exp_neg] at hhalf
                have hpos := Real.exp_pos (1 / 2 : ℝ)
                have := (le_inv_comm₀ (by positivity) hpos).mp hhalf
                linarith
              have h3 : Real.exp 1 ≤ (4 : ℝ) := by
                have : Real.exp 1 = Real.exp (1 / 2 : ℝ) * Real.exp (1 / 2 : ℝ) := by
                  rw [← Real.exp_add]; norm_num
                rw [this]; nlinarith [Real.exp_pos (1 / 2 : ℝ)]
              have hle : Real.exp 1 ≤ (n : ℝ) := h3.trans (by exact_mod_cast hn4)
              rw [← Real.log_exp 1]
              exact Real.log_le_log (Real.exp_pos 1) hle
            have hn_pos : (0 : ℝ) < n := by positivity
            have hrc_nn : 0 ≤ residueClass a n := residueClass_nonneg a n
            have hdiv : 2 / ((n : ℝ) * Real.log (n : ℝ)) ≤ 2 / (n : ℝ) := by
              refine div_le_div_of_nonneg_left (by norm_num) hn_pos ?_
              nlinarith
            calc
              residueClass a n * (2 / ((n : ℝ) * Real.log (n : ℝ)))
                  ≤ residueClass a n * (2 / (n : ℝ)) :=
                    mul_le_mul_of_nonneg_left hdiv hrc_nn
              _ = 2 * (residueClass a n / (n : ℝ)) := by ring
      · -- `n < 2`, i.e., `n = 0` or `n = 1`: `residueClass a n = 0`.
        have hrc0 : residueClass a n = 0 := by
          have hn01 : n = 0 ∨ n = 1 := by omega
          rcases hn01 with rfl | rfl
          · exact residueClass_apply_zero a
          · simp [residueClass, Set.indicator]
        have hg_nn : 0 ≤ g n := by
          dsimp only [g]
          have h1 : 0 ≤ (if n.Prime ∧ (n : ZMod q) = a then (1 : ℝ) / (n : ℝ) else 0) := by
            split_ifs <;> positivity
          have h2 : 0 ≤ (if n.Prime then 0 else residueClass a n) / (n : ℝ) := by
            split_ifs
            · simp
            · exact div_nonneg (residueClass_nonneg a n) (Nat.cast_nonneg n)
          linarith
        simpa [hrc0] using hg_nn
    exact (hlhs.trans hlower).trans hrhs
  -- Choose `M` large enough to violate `hM_bound M`.
  have hphi_pos : (0 : ℝ) < (q.totient : ℝ) :=
    Nat.cast_pos.mpr (Nat.totient_pos.mpr (NeZero.pos q))
  obtain ⟨M, hM⟩ := exists_nat_gt ((∑' n, g n + 2 * |C|) * (q.totient : ℝ))
  have hlt : ∑' n, g n < ((M + 1 : ℕ) : ℝ) * (q.totient : ℝ)⁻¹ - 2 * |C| := by
    have h1 : ∑' n, g n + 2 * |C| < (M : ℝ) * (q.totient : ℝ)⁻¹ := by
      rw [lt_mul_inv_iff₀ hphi_pos]
      exact hM
    have h2 : (M : ℝ) * (q.totient : ℝ)⁻¹ ≤ ((M + 1 : ℕ) : ℝ) * (q.totient : ℝ)⁻¹ := by
      gcongr
      exact_mod_cast Nat.le_succ M
    linarith
  exact absurd (hM_bound M) (not_le.mpr hlt)

/-- Divergence of partial sums `∑_{p < N, p prime, p ≡ a [MOD q]} ((p - 1 : ℝ) / p²)` to `+∞`. -/
lemma tendsto_sum_alpha_primes_eq_mod {q : ℕ} [NeZero q] {a : ZMod q} (ha : IsUnit a) :
    Tendsto (fun N : ℕ =>
      ∑ p ∈ (Finset.range N).filter (fun n : ℕ => n.Prime ∧ (n : ZMod q) = a),
        ((p - 1 : ℝ) / (p : ℝ) ^ 2))
      atTop atTop := by
  let f : ℕ → ℝ := fun n =>
    if n.Prime ∧ (n : ZMod q) = a then ((n - 1 : ℝ) / (n : ℝ) ^ 2) else 0
  have hf_nn : ∀ n, 0 ≤ f n := by
    intro n
    dsimp only [f]
    split_ifs with h
    · have h1 : (1 : ℝ) ≤ n := by exact_mod_cast h.1.one_lt.le
      have h2 : (0 : ℝ) ≤ (n : ℝ) ^ 2 := by positivity
      exact div_nonneg (by linarith) h2
    · exact le_rfl
  have hnot_sum : ¬ Summable f := by
    intro hsf
    apply not_summable_one_div_primes_eq_mod ha
    refine Summable.of_nonneg_of_le (fun n => by split_ifs <;> positivity) (fun n => ?_)
      (hsf.mul_left 2)
    dsimp only [f]
    split_ifs with h
    · have hp2 : (2 : ℝ) ≤ n := by exact_mod_cast h.1.two_le
      have hp_pos : (0 : ℝ) < n := by linarith
      have : (1 : ℝ) / (n : ℝ) ≤ 2 * ((n - 1 : ℝ) / (n : ℝ) ^ 2) := by
        rw [div_le_iff₀ hp_pos]
        field_simp [hp_pos.ne']
        nlinarith
      exact this
    · simp
  have hdiv := (not_summable_iff_tendsto_nat_atTop_of_nonneg hf_nn).mp hnot_sum
  refine hdiv.congr fun N => ?_
  rw [Finset.sum_filter]

end PrimeReciprocalDivergence

/-! ## Section 2: Lemma 1 (Prime-Power Divisibility Criterion) -/

section Lemma1

/-- Exact divisibility predicate `p ∥ m` (`p ∣ m` and `¬ p² ∣ m`). -/
def ExactDvd (p m : ℕ) : Prop :=
  p ∣ m ∧ ¬ (p ^ 2 ∣ m)

instance (p m : ℕ) : Decidable (ExactDvd p m) :=
  inferInstanceAs (Decidable (p ∣ m ∧ ¬ (p ^ 2 ∣ m)))

/-- For any prime `p ≡ 1 [MOD 6]`, there exists a unit `r : ZMod p` such that every prime `q`
with `(q : ZMod p) = r` satisfies `p ∣ σ 1 (q ^ 2)`. -/
lemma exists_good_residue_of_prime_mod_six {p : ℕ} (hp : p.Prime) (hmod : p % 6 = 1) :
    ∃ r : ZMod p, IsUnit r ∧ ∀ q : ℕ, q.Prime → (q : ZMod p) = r → p ∣ σ 1 (q ^ 2) := by
  have : Fact p.Prime := ⟨hp⟩
  have : NeZero p := ⟨hp.ne_zero⟩
  have : Fact (Nat.Prime 3) := ⟨by decide⟩
  have hdvd3 : 3 ∣ Fintype.card (ZMod p)ˣ := by
    rw [ZMod.card_units_eq_totient, Nat.totient_prime hp]
    omega
  obtain ⟨u, hu⟩ := exists_prime_orderOf_dvd_card 3 hdvd3
  refine ⟨(u : ZMod p), u.isUnit, fun q hq hqr => ?_⟩
  have hu3 : (u : ZMod p) ^ 3 = 1 := by
    rw [← Units.val_pow_eq_pow_val, ← hu, pow_orderOf_eq_one, Units.val_one]
  have hu1 : (u : ZMod p) ≠ 1 := by
    intro h1
    have hu_eq : u = 1 := Units.ext h1
    rw [hu_eq, orderOf_one] at hu
    omega
  have hquad : (u : ZMod p) ^ 2 + (u : ZMod p) + 1 = 0 := by
    have hfac : ((u : ZMod p) - 1) * ((u : ZMod p) ^ 2 + (u : ZMod p) + 1) = 0 := by
      linear_combination hu3
    exact (mul_eq_zero.mp hfac).resolve_left (sub_ne_zero.mpr hu1)
  have hsig : σ 1 (q ^ 2) = 1 + q + q ^ 2 := by
    rw [ArithmeticFunction.sigma_one_apply_prime_pow hq]
    simp [Finset.sum_range_succ]
  rw [hsig, ← ZMod.natCast_eq_zero_iff]
  push_cast
  rw [hqr]
  linear_combination hquad

/-- **Lemma 1:** If `p ∥ m` and there exist two distinct primes `q₁, q₂` with `q₁ ∥ m`, `q₂ ∥ m`,
and `p ∣ σ 1 (q₁ ^ 2)`, `p ∣ σ 1 (q₂ ^ 2)`, then `m ∉ DrisSet`. -/
lemma not_mem_drisSet_of_witnesses {p q₁ q₂ m : ℕ}
    (hq₁ : q₁.Prime) (hq₂ : q₂.Prime) (hne : q₁ ≠ q₂)
    (hp_ex : ExactDvd p m) (hq₁_ex : ExactDvd q₁ m) (hq₂_ex : ExactDvd q₂ m)
    (hd₁ : p ∣ σ 1 (q₁ ^ 2)) (hd₂ : p ∣ σ 1 (q₂ ^ 2)) :
    m ∉ DrisSet := by
  intro hm
  have hcop12 : q₁.Coprime q₂ := (Nat.coprime_primes hq₁ hq₂).mpr hne
  have hmul_dvd : q₁ * q₂ ∣ m := hcop12.mul_dvd_of_dvd_of_dvd hq₁_ex.1 hq₂_ex.1
  obtain ⟨k, rfl⟩ := hmul_dvd
  have hcop1k : q₁.Coprime k := by
    refine hq₁.coprime_iff_not_dvd.mpr fun h => hq₁_ex.2 ?_
    obtain ⟨t, rfl⟩ := h
    exact ⟨q₂ * t, by ring⟩
  have hcop2k : q₂.Coprime k := by
    refine hq₂.coprime_iff_not_dvd.mpr fun h => hq₂_ex.2 ?_
    obtain ⟨t, rfl⟩ := h
    exact ⟨q₁ * t, by ring⟩
  have hsq : (q₁ * q₂ * k) ^ 2 = q₁ ^ 2 * (q₂ ^ 2 * k ^ 2) := by ring
  have hcop_a : (q₁ ^ 2).Coprime (q₂ ^ 2 * k ^ 2) :=
    (hcop12.pow 2 2).mul_right (hcop1k.pow 2 2)
  have hcop_b : (q₂ ^ 2).Coprime (k ^ 2) := hcop2k.pow 2 2
  have hsig_eq : σ 1 ((q₁ * q₂ * k) ^ 2) = σ 1 (q₁ ^ 2) * (σ 1 (q₂ ^ 2) * σ 1 (k ^ 2)) := by
    rw [hsq, ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop_a,
      ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop_b]
  have hp2_sig : p ^ 2 ∣ σ 1 ((q₁ * q₂ * k) ^ 2) := by
    rw [hsig_eq, sq, ← mul_assoc]
    exact dvd_mul_of_dvd_left (mul_dvd_mul hd₁ hd₂) _
  have hp2_sq : p ^ 2 ∣ (q₁ * q₂ * k) ^ 2 := pow_dvd_pow_of_dvd hp_ex.1 2
  have hp2_gcd : p ^ 2 ∣ Nat.gcd ((q₁ * q₂ * k) ^ 2) (σ 1 ((q₁ * q₂ * k) ^ 2)) :=
    Nat.dvd_gcd hp2_sq hp2_sig
  rw [← hm.2] at hp2_gcd
  exact hp_ex.2 (dvd_trans hp2_gcd (Nat.gcd_dvd_left _ _))

end Lemma1

/-! ## Section 3: Exact Periodic Density & CRT Moments on `Π q : S, ZMod (q²)` -/

section CRTDensity

/-- Upper bound on the counting ratio of any periodic set `P : ZMod N → Prop`:
`densityRatio {m | P (m : ZMod N)} X ≤ (#{x : ZMod N | P x} : ℝ) / N + N / X`. -/
lemma densityRatio_periodic_le {N : ℕ} [NeZero N] (P : ZMod N → Prop) [DecidablePred P]
    {X : ℕ} (hX : 1 ≤ X) :
    densityRatio {m : ℕ | P (m : ZMod N)} X ≤
      ((Finset.univ.filter P).card : ℝ) / (N : ℝ) + (N : ℝ) / (X : ℝ) := by
  have hN_pos : 0 < N := NeZero.pos N
  let Q := X / N
  let c := (Finset.univ.filter P).card
  -- Cover `Icc 1 X` by `Q` full periods of length `N` plus a tail of length `< N`.
  have hcard_le :
      ((Finset.Icc 1 X).filter (fun m : ℕ => P (m : ZMod N))).card ≤ Q * c + N := by
    have hsplit : Finset.Icc 1 X ⊆
        (Finset.range Q).biUnion (fun j => Finset.Icc (j * N + 1) ((j + 1) * N)) ∪
        Finset.Icc (Q * N + 1) X := by
      intro m hm
      rw [Finset.mem_Icc] at hm
      by_cases hle : m ≤ Q * N
      · rw [Finset.mem_union, Finset.mem_biUnion]
        left
        refine ⟨(m - 1) / N, Finset.mem_range.mpr ?_, Finset.mem_Icc.mpr ?_⟩
        · exact Nat.div_lt_of_lt_mul (by rw [mul_comm]; omega)
        · have h1 := Nat.div_add_mod (m - 1) N
          rw [mul_comm] at h1
          have h2 := Nat.mod_lt (m - 1) hN_pos
          have hm1 : m - 1 + 1 = m := by omega
          have hmul : ((m - 1) / N + 1) * N = (m - 1) / N * N + N := by ring
          constructor <;> omega
      · rw [Finset.mem_union, Finset.mem_Icc]
        right
        omega
    have hfilt := Finset.card_le_card (Finset.filter_subset_filter (fun m : ℕ => P (m : ZMod N)) hsplit)
    rw [Finset.filter_union] at hfilt
    refine hfilt.trans ((Finset.card_union_le _ _).trans (add_le_add ?_ ?_))
    · rw [Finset.filter_biUnion]
      refine Finset.card_biUnion_le.trans ?_
      have hblock : ∀ j : ℕ,
          ((Finset.Icc (j * N + 1) ((j + 1) * N)).filter (fun m : ℕ => P (m : ZMod N))).card = c := by
        intro j
        refine Finset.card_bij (fun m _ => (m : ZMod N)) (fun m hm => ?_) (fun m₁ hm₁ m₂ hm₂ heq => ?_)
          (fun x hx => ?_)
        · rw [Finset.mem_filter] at hm ⊢
          exact ⟨Finset.mem_univ _, hm.2⟩
        · rw [Finset.mem_filter, Finset.mem_Icc] at hm₁ hm₂
          have hmod : m₁ ≡ m₂ [MOD N] := (ZMod.natCast_eq_natCast_iff m₁ m₂ N).mp heq
          have hdvd : N ∣ (max m₁ m₂ - min m₁ m₂) := by
            rcases le_total m₁ m₂ with h | h
            · rw [max_eq_right h, min_eq_left h]
              exact (Nat.modEq_iff_dvd' h).mp hmod
            · rw [max_eq_left h, min_eq_right h]
              exact (Nat.modEq_iff_dvd' h).mp hmod.symm
          have hlt : max m₁ m₂ - min m₁ m₂ < N := by
            have hmul : (j + 1) * N = j * N + N := by ring
            rcases le_total m₁ m₂ with h | h
            · rw [max_eq_right h, min_eq_left h]; omega
            · rw [max_eq_left h, min_eq_right h]; omega
          have hzero : max m₁ m₂ - min m₁ m₂ = 0 := Nat.eq_zero_of_dvd_of_lt hdvd hlt
          omega
        · rw [Finset.mem_filter] at hx
          let m := if x.val = 0 then (j + 1) * N else j * N + x.val
          refine ⟨m, Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ?_, ?_⟩, ?_⟩
          · dsimp only [m]
            have hmul : (j + 1) * N = j * N + N := by ring
            split_ifs with hx0
            · constructor <;> omega
            · have hxlt := x.val_lt
              constructor <;> omega
          · have hcast : (m : ZMod N) = x := by
              dsimp only [m]
              split_ifs with hx0
              · rw [Nat.cast_mul, ZMod.natCast_self, mul_zero]
                exact (ZMod.val_eq_zero x).mp hx0 |>.symm
              · rw [Nat.cast_add, Nat.cast_mul, ZMod.natCast_self, mul_zero, zero_add,
                  ZMod.natCast_zmod_val]
            rw [hcast]
            exact hx.2
          · dsimp only [m]
            split_ifs with hx0
            · rw [Nat.cast_mul, ZMod.natCast_self, mul_zero]
              exact (ZMod.val_eq_zero x).mp hx0 |>.symm
            · rw [Nat.cast_add, Nat.cast_mul, ZMod.natCast_self, mul_zero, zero_add,
                ZMod.natCast_zmod_val]
      simp_rw [hblock, Finset.sum_const, Finset.card_range, smul_eq_mul]
      exact le_rfl
    · refine (Finset.card_filter_le _ _).trans ?_
      rw [Nat.card_Icc]
      have hdiv : Q * N + X % N = X := by
        dsimp only [Q]; rw [mul_comm]; exact Nat.div_add_mod X N
      have hmod := Nat.mod_lt X hN_pos
      omega
  unfold densityRatio
  simp only [Set.mem_ofPred_eq]
  have hX_pos : (0 : ℝ) < X := by exact_mod_cast hX
  have hN_rpos : (0 : ℝ) < N := by exact_mod_cast hN_pos
  have hQN_le : (Q : ℝ) * (N : ℝ) ≤ (X : ℝ) := by
    exact_mod_cast Nat.div_mul_le_self X N
  have hQ_le : (Q : ℝ) / (X : ℝ) ≤ 1 / (N : ℝ) := by
    rw [div_le_div_iff₀ hX_pos hN_rpos]
    linarith
  have hle_r : (((Finset.Icc 1 X).filter (fun m : ℕ => P (m : ZMod N))).card : ℝ) ≤
      (Q : ℝ) * (c : ℝ) + (N : ℝ) := by exact_mod_cast hcard_le
  calc
    (((Finset.Icc 1 X).filter (fun m : ℕ => P (m : ZMod N))).card : ℝ) / (X : ℝ)
        ≤ ((Q : ℝ) * (c : ℝ) + (N : ℝ)) / (X : ℝ) :=
          div_le_div_of_nonneg_right hle_r hX_pos.le
    _ = ((Q : ℝ) / (X : ℝ)) * (c : ℝ) + (N : ℝ) / (X : ℝ) := by ring
    _ ≤ (1 / (N : ℝ)) * (c : ℝ) + (N : ℝ) / (X : ℝ) := by
          gcongr
    _ = (c : ℝ) / (N : ℝ) + (N : ℝ) / (X : ℝ) := by ring

/-- Exact-divisibility residue predicate on `ZMod (p²)`: `p ∣ x.val ∧ x ≠ 0`. -/
def zmodHit (p : ℕ) (x : ZMod (p ^ 2)) : Prop :=
  p ∣ x.val ∧ x ≠ 0

instance (p : ℕ) : DecidablePred (zmodHit p) :=
  fun x => inferInstanceAs (Decidable (p ∣ x.val ∧ x ≠ 0))

lemma exactDvd_iff_zmodHit {p : ℕ} (hp : p.Prime) (m : ℕ) :
    ExactDvd p m ↔ zmodHit p (m : ZMod (p ^ 2)) := by
  have : NeZero (p ^ 2) := ⟨pow_ne_zero 2 hp.ne_zero⟩
  unfold ExactDvd zmodHit
  have hval : ((m : ZMod (p ^ 2)).val) = m % p ^ 2 := ZMod.val_natCast (n := p ^ 2) m
  rw [hval, Ne, ZMod.natCast_eq_zero_iff]
  have hdvd : p ∣ m % p ^ 2 ↔ p ∣ m := by
    have h1 : p ∣ p ^ 2 := dvd_pow_self p (by decide)
    have h2 : m % p ^ 2 + p ^ 2 * (m / p ^ 2) = m := Nat.mod_add_div m (p ^ 2)
    constructor
    · intro h
      rw [← h2]
      exact dvd_add h (dvd_mul_of_dvd_left h1 _)
    · intro h
      have h3 : p ∣ p ^ 2 * (m / p ^ 2) := dvd_mul_of_dvd_left h1 _
      exact (Nat.dvd_add_left h3).mp (h2.symm ▸ h)
  exact ⟨fun ⟨h1, h2⟩ => ⟨hdvd.mpr h1, h2⟩, fun ⟨h1, h2⟩ => ⟨hdvd.mp h1, h2⟩⟩

/-- Exactly `p - 1` residues in `ZMod (p²)` satisfy `zmodHit p`. -/
lemma card_filter_zmodHit {p : ℕ} (hp : p.Prime) [NeZero (p ^ 2)] :
    (Finset.univ.filter (zmodHit p)).card = p - 1 := by
  have hp_pos : 0 < p := hp.pos
  have hbij : (Finset.univ.filter (zmodHit p)).card = (Finset.Icc 1 (p - 1)).card := by
    refine Finset.card_bij (fun x _ => x.val / p) (fun x hx => ?_) (fun x₁ hx₁ x₂ hx₂ heq => ?_)
      (fun k hk => ?_)
    · rw [Finset.mem_filter] at hx
      rw [Finset.mem_Icc]
      obtain ⟨hdvd, hne0⟩ := hx.2
      have hval_ne0 : x.val ≠ 0 := fun h0 => hne0 ((ZMod.val_eq_zero x).mp h0)
      have hval_lt : x.val < p ^ 2 := x.val_lt
      obtain ⟨k, hk⟩ := hdvd
      have hdiv : x.val / p = k := by rw [hk, Nat.mul_div_cancel_left k hp_pos]
      rw [hdiv]
      have hk_pos : 1 ≤ k := by
        by_contra h0
        have : k = 0 := by omega
        rw [this, mul_zero] at hk
        exact hval_ne0 hk
      have hk_lt : k < p := by
        by_contra hge
        have : p ^ 2 ≤ p * k := by rw [sq]; exact Nat.mul_le_mul_left p (by omega)
        omega
      omega
    · rw [Finset.mem_filter] at hx₁ hx₂
      apply ZMod.val_injective
      have h1 := Nat.mul_div_cancel' hx₁.2.1
      have h2 := Nat.mul_div_cancel' hx₂.2.1
      rw [← h1, ← h2, heq]
    · rw [Finset.mem_Icc] at hk
      have hmul_lt : p * k < p ^ 2 := by
        rw [sq]
        exact Nat.mul_lt_mul_of_pos_left (by omega) hp_pos
      refine ⟨((p * k : ℕ) : ZMod (p ^ 2)), Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩, ?_⟩
      · have hval : ((p * k : ℕ) : ZMod (p ^ 2)).val = p * k := by
          rw [ZMod.val_natCast, Nat.mod_eq_of_lt hmul_lt]
        refine ⟨by rw [hval]; exact dvd_mul_right p k, fun h0 => ?_⟩
        have hzero := (ZMod.val_eq_zero _).mpr h0
        rw [hval] at hzero
        exact Nat.mul_ne_zero hp.ne_zero (by omega) hzero
      · have hval : ((p * k : ℕ) : ZMod (p ^ 2)).val = p * k := by
          rw [ZMod.val_natCast, Nat.mod_eq_of_lt hmul_lt]
        rw [hval, Nat.mul_div_cancel_left k hp_pos]
  rw [hbij, Nat.card_Icc]
  omega

/-- Coprimality of `p ↦ p²` on a finite set of primes. -/
lemma pairwise_coprime_prime_sq (S : Finset ℕ) (hS : ∀ p ∈ S, p.Prime) :
    Pairwise (Function.onFun Nat.Coprime fun p : S => (p : ℕ) ^ 2) := by
  intro p q hne
  have hne' : (p : ℕ) ≠ (q : ℕ) := fun h => hne (Subtype.ext h)
  exact ((Nat.coprime_primes (hS p.val p.property) (hS q.val q.property)).mpr hne').pow 2 2

/-- For a finite set of primes `S`, `N = ∏ p ∈ S, p²` is positive. -/
lemma prod_prime_sq_ne_zero (S : Finset ℕ) (hS : ∀ p ∈ S, p.Prime) :
    (∏ p ∈ S, p ^ 2) ≠ 0 := by
  rw [Finset.prod_ne_zero_iff]
  intro p hp
  exact pow_ne_zero 2 (hS p hp).ne_zero

/-- Exact CRT density of `E_S = {m : ∀ p ∈ S, ¬ p ∥ m}`:
`densityRatio E_S X ≤ ∏ p ∈ S, (1 - (p - 1 : ℝ) / p²) + (∏ p ∈ S, p²) / X`. -/
lemma densityRatio_avoid_all_le (S : Finset ℕ) (hS : ∀ p ∈ S, p.Prime) {X : ℕ} (hX : 1 ≤ X) :
    densityRatio {m : ℕ | ∀ p ∈ S, ¬ ExactDvd p m} X ≤
      (∏ p ∈ S, (1 - ((p - 1 : ℝ) / (p : ℝ) ^ 2))) + ((∏ p ∈ S, p ^ 2 : ℕ) : ℝ) / (X : ℝ) := by
  let N := ∏ p : S, (p : ℕ) ^ 2
  have hN_eq : N = ∏ p ∈ S, p ^ 2 := Finset.prod_attach S (fun p => p ^ 2)
  have : NeZero N := ⟨hN_eq.symm ▸ prod_prime_sq_ne_zero S hS⟩
  have : ∀ p : S, NeZero ((p : ℕ) ^ 2) := fun p => ⟨pow_ne_zero 2 (hS p.val p.property).ne_zero⟩
  let e : ZMod N ≃+* Π p : S, ZMod ((p : ℕ) ^ 2) :=
    ZMod.prodEquivPi (fun p : S => (p : ℕ) ^ 2) (pairwise_coprime_prime_sq S hS)
  let P : ZMod N → Prop := fun x => ∀ p : S, ¬ zmodHit p.val (e x p)
  have hset_eq : {m : ℕ | ∀ p ∈ S, ¬ ExactDvd p m} = {m : ℕ | P (m : ZMod N)} := by
    ext m
    simp only [Set.mem_ofPred_eq, P]
    constructor
    · intro hm p
      have hecast : e (m : ZMod N) p = (m : ZMod ((p : ℕ) ^ 2)) := by
        simp [e]
      rw [hecast, ← exactDvd_iff_zmodHit (hS p.val p.property)]
      exact hm p.val p.property
    · intro hm p hp
      have hecast : e (m : ZMod N) ⟨p, hp⟩ = (m : ZMod (p ^ 2)) := by
        simp [e]
      rw [exactDvd_iff_zmodHit (hS p hp), ← hecast]
      exact hm ⟨p, hp⟩
  rw [hset_eq]
  refine (densityRatio_periodic_le P hX).trans ?_
  have hrem_eq : (N : ℝ) / (X : ℝ) = ((∏ p ∈ S, p ^ 2 : ℕ) : ℝ) / (X : ℝ) := by rw [hN_eq]
  rw [hrem_eq]
  refine add_le_add ?_ le_rfl
  -- Compute `(Finset.univ.filter P).card / N` via `e`.
  let Q : (Π p : S, ZMod ((p : ℕ) ^ 2)) → Prop := fun y => ∀ p : S, ¬ zmodHit p.val (y p)
  have hcard_eq : (Finset.univ.filter P).card = (Finset.univ.filter Q).card := by
    refine Finset.card_bij (fun x _ => e x) (fun x hx => ?_) (fun _ _ _ _ h => e.injective h)
      (fun y hy => ?_)
    · rw [Finset.mem_filter] at hx ⊢
      exact ⟨Finset.mem_univ _, hx.2⟩
    · rw [Finset.mem_filter] at hy
      exact ⟨e.symm y, Finset.mem_filter.mpr ⟨Finset.mem_univ _, by simpa [P, Q] using hy.2⟩,
        e.apply_symm_apply y⟩
  have hpi_eq : Finset.univ.filter Q =
      Fintype.piFinset (fun p : S => Finset.univ.filter (fun y : ZMod ((p : ℕ) ^ 2) => ¬ zmodHit p.val y)) := by
    ext y
    simp [Q, Fintype.mem_piFinset]
  have hcard_Q : (Finset.univ.filter Q).card = ∏ p : S, ((p : ℕ) ^ 2 - (p.val - 1)) := by
    rw [hpi_eq, Fintype.card_piFinset]
    refine Finset.prod_congr rfl fun p _ => ?_
    have hcompl := Finset.card_filter_add_card_filter_not
      (s := (Finset.univ : Finset (ZMod ((p : ℕ) ^ 2)))) (zmodHit p.val)
    rw [card_filter_zmodHit (hS p.val p.property), Finset.card_univ, ZMod.card] at hcompl
    omega
  rw [hcard_eq, hcard_Q]
  change ((∏ p : S, ((p : ℕ) ^ 2 - (p.val - 1)) : ℕ) : ℝ) / ((∏ p : S, (p : ℕ) ^ 2 : ℕ) : ℝ) ≤ _
  push_cast
  rw [← Finset.prod_div_distrib]
  rw [← Finset.prod_attach S (fun p => 1 - ((p - 1 : ℝ) / (p : ℝ) ^ 2))]
  refine le_of_eq (Finset.prod_congr rfl fun p _ => ?_)
  have hp := hS p.val p.property
  have hp1 : 1 ≤ p.val := hp.one_lt.le
  have hp_sq : p.val ≤ p.val ^ 2 := Nat.le_self_pow two_ne_zero p.val
  have hp_le : p.val - 1 ≤ p.val ^ 2 := (Nat.sub_le p.val 1).trans hp_sq
  have hp2_ne : ((p : ℕ) : ℝ) ^ 2 ≠ 0 := by positivity
  rw [Nat.cast_sub hp_le, Nat.cast_sub hp1]
  push_cast
  field_simp [hp2_ne]

/-- Exact variance / Chebyshev bound on the product space `Π q : S, ZMod (q²)`:
if `μ = ∑ q ∈ S, (q - 1) / q² ≥ 2`, then
`#{y : Π q : S, ZMod (q²) | #{q ∈ S | zmodHit q (y q)} ≤ 1} / (∏ q ∈ S, q²) ≤ μ / (μ - 1)²`. -/
lemma chebyshev_bad_card_le (S : Finset ℕ) (hS : ∀ q ∈ S, q.Prime)
    [∀ q : S, NeZero ((q : ℕ) ^ 2)]
    (hmu : 2 ≤ ∑ q ∈ S, ((q - 1 : ℝ) / (q : ℝ) ^ 2)) :
    let Ω := Π q : S, ZMod ((q : ℕ) ^ 2)
    let B : Finset Ω := Finset.univ.filter fun y =>
      (Finset.univ.filter fun q : S => zmodHit q.val (y q)).card ≤ 1
    let μ : ℝ := ∑ q ∈ S, ((q - 1 : ℝ) / (q : ℝ) ^ 2)
    (B.card : ℝ) / ((∏ q ∈ S, q ^ 2 : ℕ) : ℝ) ≤ μ / (μ - 1) ^ 2 := by
  intro Ω B μ
  let α : S → ℝ := fun q => ((q.val - 1 : ℝ) / (q.val : ℝ) ^ 2)
  have hμ_eq : μ = ∑ q : S, α q := (Finset.sum_attach S (fun q => ((q - 1 : ℝ) / (q : ℝ) ^ 2))).symm
  let N : ℕ := ∏ q ∈ S, q ^ 2
  have hN_card : Fintype.card Ω = N := by
    rw [Fintype.card_pi]
    simp_rw [ZMod.card]
    exact Finset.prod_attach S (fun q => q ^ 2)
  have hN_pos : (0 : ℝ) < (N : ℝ) :=
    Nat.cast_pos.mpr (Nat.pos_of_ne_zero (prod_prime_sq_ne_zero S hS))
  let X : S → Ω → ℝ := fun q y => if zmodHit q.val (y q) then 1 else 0
  let Y : S → Ω → ℝ := fun q y => X q y - α q
  -- Single-coordinate sum of `Y q` is `0`.
  have hY_single : ∀ q : S,
      ∑ z : ZMod ((q : ℕ) ^ 2), ((if zmodHit q.val z then (1 : ℝ) else 0) - α q) = 0 := by
    intro q
    rw [Finset.sum_sub_distrib, Finset.sum_boole, card_filter_zmodHit (hS q.val q.property),
      Finset.sum_const, Finset.card_univ, ZMod.card, nsmul_eq_mul]
    have hq := hS q.val q.property
    have hq1 : 1 ≤ q.val := hq.one_lt.le
    have hq2_ne : ((q.val : ℝ) ^ 2) ≠ 0 := by positivity
    rw [Nat.cast_sub hq1]
    dsimp only [α]
    push_cast
    field_simp [hq2_ne]
    ring
  -- Single-coordinate sum of `(Y q)²` is `q² * α q * (1 - α q) ≤ q² * α q`.
  have hY_sq_single : ∀ q : S,
      ∑ z : ZMod ((q : ℕ) ^ 2), ((if zmodHit q.val z then (1 : ℝ) else 0) - α q) ^ 2 ≤
        ((q : ℕ) : ℝ) ^ 2 * α q := by
    intro q
    have hsq_term : ∀ z : ZMod ((q : ℕ) ^ 2),
        ((if zmodHit q.val z then (1 : ℝ) else 0) - α q) ^ 2 =
          (1 - 2 * α q) * (if zmodHit q.val z then (1 : ℝ) else 0) + (α q) ^ 2 := by
      intro z
      split_ifs <;> ring
    simp_rw [hsq_term, Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_boole,
      card_filter_zmodHit (hS q.val q.property), Finset.sum_const, Finset.card_univ, ZMod.card,
      nsmul_eq_mul]
    have hq := hS q.val q.property
    have hq1 : 1 ≤ q.val := hq.one_lt.le
    have hq2_ne : ((q.val : ℝ) ^ 2) ≠ 0 := by positivity
    rw [Nat.cast_sub hq1]
    have hα_nn : 0 ≤ α q := by
      dsimp only [α]
      have : (1 : ℝ) ≤ q.val := by exact_mod_cast hq1
      exact div_nonneg (by linarith) (by positivity)
    have hident :
        (1 - 2 * α q) * ((q.val : ℝ) - 1) + ((q.val ^ 2 : ℕ) : ℝ) * (α q) ^ 2 =
          ((q.val : ℝ) ^ 2) * α q - ((q.val : ℝ) ^ 2) * (α q) ^ 2 := by
      dsimp only [α]
      push_cast
      field_simp [hq2_ne]
      ring
    push_cast at hident ⊢
    nlinarith [sq_nonneg (α q)]
  -- Factoring sums over `Ω` along one coordinate `q`.
  have hsum_single_coord : ∀ (q : S) (g : ZMod ((q : ℕ) ^ 2) → ℝ),
      ∑ y : Ω, g (y q) =
        ((∏ r ∈ (Finset.univ.erase q), ((r : ℕ) ^ 2)) : ℝ) * ∑ z : ZMod ((q : ℕ) ^ 2), g z := by
    intro q g
    let e := Equiv.piSplitAt q (fun r : S => ZMod ((r : ℕ) ^ 2))
    rw [Fintype.sum_equiv e (fun y => g (y q)) (fun p => g p.1) (fun y => rfl)]
    rw [Fintype.sum_prod_type, Finset.sum_comm]
    simp_rw [Finset.sum_const, nsmul_eq_mul]
    congr 1
    rw [Finset.card_univ, Fintype.card_pi]
    simp_rw [ZMod.card]
    have hprod_nat : (∏ r : {r : S // r ≠ q}, ((r.val : ℕ) ^ 2)) =
        ∏ r ∈ Finset.univ.erase q, ((r : ℕ) ^ 2) := by
      refine Finset.prod_bij (fun r _ => r.val)
        (fun r _ => Finset.mem_erase.mpr ⟨r.property, Finset.mem_univ _⟩)
        (fun _ _ _ _ h => Subtype.ext h)
        (fun r hr => ⟨⟨r, (Finset.mem_erase.mp hr).1⟩, Finset.mem_univ _, rfl⟩)
        (fun _ _ => rfl)
    rw [hprod_nat]
    push_cast
    rfl
  -- Cross terms `∑ y : Ω, Y q₁ y * Y q₂ y = 0` for `q₁ ≠ q₂`.
  have hcross : ∀ q₁ q₂ : S, q₁ ≠ q₂ → ∑ y : Ω, Y q₁ y * Y q₂ y = 0 := by
    intro q₁ q₂ hne
    let e1 := Equiv.piSplitAt q₁ (fun r : S => ZMod ((r : ℕ) ^ 2))
    let q₂' : {r : S // r ≠ q₁} := ⟨q₂, hne.symm⟩
    let e2 := Equiv.piSplitAt q₂' (fun r : {r : S // r ≠ q₁} => ZMod ((r.val : ℕ) ^ 2))
    let e := e1.trans (Equiv.prodCongr (Equiv.refl _) e2)
    rw [Fintype.sum_equiv e (fun y => Y q₁ y * Y q₂ y)
      (fun t => ((if zmodHit q₁.val t.1 then (1 : ℝ) else 0) - α q₁) *
        ((if zmodHit q₂.val t.2.1 then (1 : ℝ) else 0) - α q₂)) (fun y => rfl)]
    rw [Fintype.sum_prod_type]
    simp_rw [Fintype.sum_prod_type]
    have h1 : ∀ z₁,
        ∑ z₂ : ZMod ((q₂ : ℕ) ^ 2),
          ∑ _rest : (∀ r : {r : {r : S // r ≠ q₁} // r ≠ q₂'}, ZMod ((r.val.val : ℕ) ^ 2)),
            ((if zmodHit q₁.val z₁ then (1 : ℝ) else 0) - α q₁) *
              ((if zmodHit q₂.val z₂ then (1 : ℝ) else 0) - α q₂) = 0 := by
      intro z₁
      simp_rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      rw [← Finset.mul_sum, ← Finset.mul_sum, hY_single q₂, mul_zero, mul_zero]
    exact Finset.sum_eq_zero fun z₁ _ => h1 z₁
  -- Diagonal terms `∑ y : Ω, (Y q y)² ≤ N * α q`.
  have hdiag : ∀ q : S, ∑ y : Ω, (Y q y) ^ 2 ≤ (N : ℝ) * α q := by
    intro q
    have h1 := hsum_single_coord q (fun z => ((if zmodHit q.val z then (1 : ℝ) else 0) - α q) ^ 2)
    change ∑ y : Ω, ((if zmodHit q.val (y q) then (1 : ℝ) else 0) - α q) ^ 2 ≤ _
    rw [h1]
    have hprod_eq : (∏ r ∈ Finset.univ.erase q, ((r : ℕ) ^ 2)) * (q.val ^ 2) = N := by
      have hmul := Finset.mul_prod_erase (Finset.univ : Finset S) (fun r : S => (r : ℕ) ^ 2) (Finset.mem_univ q)
      rw [mul_comm] at hmul
      rw [hmul, Finset.prod_coe_sort S (fun r => r ^ 2)]
    calc
      ((∏ r ∈ Finset.univ.erase q, ((r : ℕ) ^ 2)) : ℝ) *
          ∑ z : ZMod ((q : ℕ) ^ 2), ((if zmodHit q.val z then (1 : ℝ) else 0) - α q) ^ 2
        ≤ ((∏ r ∈ Finset.univ.erase q, ((r : ℕ) ^ 2)) : ℝ) * (((q : ℕ) : ℝ) ^ 2 * α q) :=
          mul_le_mul_of_nonneg_left (hY_sq_single q) (by positivity)
      _ = (((∏ r ∈ Finset.univ.erase q, ((r : ℕ) ^ 2)) * (q.val ^ 2) : ℕ) : ℝ) * α q := by
          push_cast; ring
      _ = (N : ℝ) * α q := by rw [hprod_eq]
  -- Total variance bound: `∑ y : Ω, (∑ q, Y q y)² ≤ N * μ`.
  have hvar : ∑ y : Ω, (∑ q : S, Y q y) ^ 2 ≤ (N : ℝ) * μ := by
    have hexpand : ∀ y : Ω, (∑ q : S, Y q y) ^ 2 = ∑ q₁ : S, ∑ q₂ : S, Y q₁ y * Y q₂ y := by
      intro y
      rw [sq, Finset.sum_mul_sum]
    simp_rw [hexpand]
    rw [Finset.sum_comm]
    calc
      ∑ q₁ : S, ∑ y : Ω, ∑ q₂ : S, Y q₁ y * Y q₂ y
          = ∑ q₁ : S, ∑ q₂ : S, ∑ y : Ω, Y q₁ y * Y q₂ y :=
            Finset.sum_congr rfl fun _ _ => Finset.sum_comm
      _ = ∑ q₁ : S, ∑ y : Ω, (Y q₁ y) ^ 2 := by
            refine Finset.sum_congr rfl fun q₁ _ => ?_
            rw [Finset.sum_eq_single q₁]
            · simp_rw [sq]
            · intro q₂ _ hne; exact hcross q₁ q₂ hne.symm
            · intro h; exact absurd (Finset.mem_univ q₁) h
      _ ≤ ∑ q₁ : S, (N : ℝ) * α q₁ := Finset.sum_le_sum fun q₁ _ => hdiag q₁
      _ = (N : ℝ) * μ := by rw [← Finset.mul_sum, ← hμ_eq]
  -- Chebyshev step on `B`.
  have hcheb : (B.card : ℝ) * (μ - 1) ^ 2 ≤ (N : ℝ) * μ := by
    calc
      (B.card : ℝ) * (μ - 1) ^ 2 = ∑ _y ∈ B, (μ - 1) ^ 2 := by
        rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ ∑ y ∈ B, (∑ q : S, Y q y) ^ 2 := by
        refine Finset.sum_le_sum fun y hy => ?_
        rw [Finset.mem_filter] at hy
        have hfx : ∑ q : S, X q y = ((Finset.univ.filter fun q : S => zmodHit q.val (y q)).card : ℝ) := by
          simp [X, Finset.sum_boole]
        have hfx_le1 : ∑ q : S, X q y ≤ 1 := by
          rw [hfx]; exact_mod_cast hy.2
        have hsumY : ∑ q : S, Y q y = (∑ q : S, X q y) - μ := by
          simp only [Y, Finset.sum_sub_distrib, hμ_eq]
        rw [hsumY]
        nlinarith
      _ ≤ ∑ y : Ω, (∑ q : S, Y q y) ^ 2 :=
        Finset.sum_le_univ_sum_of_nonneg fun _ => sq_nonneg _
      _ ≤ (N : ℝ) * μ := hvar
  have hden_pos : 0 < (μ - 1) ^ 2 := by nlinarith
  rw [div_le_div_iff₀ hN_pos hden_pos]
  linarith

/-- Density upper bound for the finite-cutoff bad set `B̃_{Q} = {m : #{q ∈ Q | q ∥ m} ≤ 1}`. -/
lemma densityRatio_bad_le (Q : Finset ℕ) (hQ : ∀ q ∈ Q, q.Prime)
    (hmu : 2 ≤ ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2)) {X : ℕ} (hX : 1 ≤ X) :
    let μ := ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2)
    densityRatio {m : ℕ | (Q.filter (fun q => ExactDvd q m)).card ≤ 1} X ≤
      μ / (μ - 1) ^ 2 + ((∏ q ∈ Q, q ^ 2 : ℕ) : ℝ) / (X : ℝ) := by
  intro μ
  let N := ∏ q : Q, (q : ℕ) ^ 2
  have hN_eq : N = ∏ q ∈ Q, q ^ 2 := Finset.prod_attach Q (fun q => q ^ 2)
  have : NeZero N := ⟨hN_eq.symm ▸ prod_prime_sq_ne_zero Q hQ⟩
  have : ∀ q : Q, NeZero ((q : ℕ) ^ 2) := fun q => ⟨pow_ne_zero 2 (hQ q.val q.property).ne_zero⟩
  let e : ZMod N ≃+* Π q : Q, ZMod ((q : ℕ) ^ 2) :=
    ZMod.prodEquivPi (fun q : Q => (q : ℕ) ^ 2) (pairwise_coprime_prime_sq Q hQ)
  let P : ZMod N → Prop := fun x =>
    (Finset.univ.filter fun q : Q => zmodHit q.val (e x q)).card ≤ 1
  have hset_eq :
      {m : ℕ | (Q.filter (fun q => ExactDvd q m)).card ≤ 1} = {m : ℕ | P (m : ZMod N)} := by
    ext m
    simp only [Set.mem_ofPred_eq, P]
    have hcard : (Q.filter (fun q => ExactDvd q m)).card =
        (Finset.univ.filter fun q : Q => zmodHit q.val (e (m : ZMod N) q)).card := by
      refine Finset.card_bij (fun q hq => ⟨q, (Finset.mem_filter.mp hq).1⟩)
        (fun q hq => ?_) (fun _ _ _ _ h => congrArg Subtype.val h) (fun q hq => ?_)
      · rw [Finset.mem_filter] at hq ⊢
        have hecast : e (m : ZMod N) ⟨q, hq.1⟩ = (m : ZMod (q ^ 2)) := by
          simp [e]
        rw [hecast, ← exactDvd_iff_zmodHit (hQ q hq.1)]
        exact ⟨Finset.mem_univ _, hq.2⟩
      · rw [Finset.mem_filter] at hq
        have hecast : e (m : ZMod N) q = (m : ZMod ((q : ℕ) ^ 2)) := by
          simp [e]
        rw [hecast, ← exactDvd_iff_zmodHit (hQ q.val q.property)] at hq
        exact ⟨q.val, Finset.mem_filter.mpr ⟨q.property, hq.2⟩, rfl⟩
    rw [hcard]
  rw [hset_eq]
  refine (densityRatio_periodic_le P hX).trans ?_
  have hrem_eq : (N : ℝ) / (X : ℝ) = ((∏ q ∈ Q, q ^ 2 : ℕ) : ℝ) / (X : ℝ) := by rw [hN_eq]
  rw [hrem_eq]
  refine add_le_add ?_ le_rfl
  let Ω := Π q : Q, ZMod ((q : ℕ) ^ 2)
  let B : Finset Ω := Finset.univ.filter fun y =>
    (Finset.univ.filter fun q : Q => zmodHit q.val (y q)).card ≤ 1
  have hcard_eq : (Finset.univ.filter P).card = B.card := by
    refine Finset.card_bij (fun x _ => e x) (fun x hx => ?_) (fun _ _ _ _ h => e.injective h)
      (fun y hy => ?_)
    · rw [Finset.mem_filter] at hx ⊢
      exact ⟨Finset.mem_univ _, hx.2⟩
    · rw [Finset.mem_filter] at hy
      exact ⟨e.symm y, Finset.mem_filter.mpr ⟨Finset.mem_univ _, by simpa [P] using hy.2⟩,
        e.apply_symm_apply y⟩
  have hN_cast : (N : ℝ) = ((∏ q ∈ Q, q ^ 2 : ℕ) : ℝ) := by rw [hN_eq]
  rw [hcard_eq, hN_cast]
  exact chebyshev_bad_card_le Q hQ hmu

end CRTDensity

/-! ## Section 4: Main Theorem — Conjecture 5.1 of Dris (`arXiv:2202.08116v1`) -/

/-- Abstract finite union bound for `densityRatio` (keeps `Classical.propDecidable` uniform). -/
lemma densityRatio_le_add_sum {ι : Type*} [Fintype ι]
    (A E : Set ℕ) (B : ι → Set ℕ) {X : ℕ} (hX : 1 ≤ X)
    (hcover : ∀ m ∈ A, m ∈ E ∨ ∃ i : ι, m ∈ B i) :
    densityRatio A X ≤ densityRatio E X + ∑ i : ι, densityRatio (B i) X := by
  have hX_pos : (0 : ℝ) < X := by exact_mod_cast hX
  unfold densityRatio
  rw [← Finset.sum_div, ← add_div]
  refine div_le_div_of_nonneg_right ?_ hX_pos.le
  norm_cast
  have hsub : (Finset.Icc 1 X).filter (· ∈ A) ⊆
      (Finset.Icc 1 X).filter (· ∈ E) ∪
        Finset.univ.biUnion (fun i : ι => (Finset.Icc 1 X).filter (· ∈ B i)) := by
    intro m hm
    rw [Finset.mem_filter] at hm
    rw [Finset.mem_union, Finset.mem_filter, Finset.mem_biUnion]
    rcases hcover m hm.2 with hE | ⟨i, hB⟩
    · exact Or.inl ⟨hm.1, hE⟩
    · exact Or.inr ⟨i, Finset.mem_univ _, Finset.mem_filter.mpr ⟨hm.1, hB⟩⟩
  exact (Finset.card_le_card hsub).trans
    ((Finset.card_union_le _ _).trans (add_le_add le_rfl Finset.card_biUnion_le))

/-- **Conjecture 5.1 of Dris (`arXiv:2202.08116v1`):**
The set `A = {m ≥ 1 : gcd(m, σ(m²)) = gcd(m², σ(m²))}` has asymptotic density `0`. -/
theorem dris_conjecture_5_1 :
    Tendsto (densityRatio DrisSet) atTop (nhds 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  -- Step 1: Choose a finite set `T` of primes `p ≡ 1 (mod 6)` with `∏_{p ∈ T} (1 - (p-1)/p²) < ε / 3`.
  have ha6 : IsUnit (1 : ZMod 6) := isUnit_one
  have hT_div := tendsto_sum_alpha_primes_eq_mod (q := 6) (a := 1) ha6
  obtain ⟨M₀, hM₀⟩ := Filter.eventually_atTop.mp ((tendsto_atTop.mp hT_div) (Real.log (3 / ε) + 1))
  let T : Finset ℕ := (Finset.range M₀).filter (fun p : ℕ => p.Prime ∧ (p : ZMod 6) = 1)
  have hT_prime : ∀ p ∈ T, p.Prime := fun p hp => (Finset.mem_filter.mp hp).2.1
  have hT_mod : ∀ p ∈ T, p % 6 = 1 := fun p hp => by
    have h1 := (Finset.mem_filter.mp hp).2.2
    have h2 : p ≡ 1 [MOD 6] := (ZMod.natCast_eq_natCast_iff p 1 6).mp (by simpa using h1)
    simpa [Nat.ModEq] using h2
  have hprod_lt : ∏ p ∈ T, (1 - ((p - 1 : ℝ) / (p : ℝ) ^ 2)) < ε / 3 := by
    have hsum_ge : Real.log (3 / ε) + 1 ≤ ∑ p ∈ T, ((p - 1 : ℝ) / (p : ℝ) ^ 2) :=
      hM₀ M₀ le_rfl
    have hprod_le : ∏ p ∈ T, (1 - ((p - 1 : ℝ) / (p : ℝ) ^ 2)) ≤
        Real.exp (-∑ p ∈ T, ((p - 1 : ℝ) / (p : ℝ) ^ 2)) := by
      rw [← Finset.sum_neg_distrib, Real.exp_sum]
      refine Finset.prod_le_prod₀ (fun p hp => ?_) (fun p _ => Real.one_sub_le_exp_neg _)
      have hp_pos : (0 : ℝ) < (p : ℝ) := by exact_mod_cast (hT_prime p hp).pos
      have hp2 : (2 : ℝ) ≤ (p : ℝ) := by exact_mod_cast (hT_prime p hp).two_le
      have h1 : (p : ℝ) - 1 ≤ (p : ℝ) ^ 2 := by nlinarith
      have hdiv : ((p - 1 : ℝ) / (p : ℝ) ^ 2) ≤ 1 :=
        (div_le_one (pow_pos hp_pos 2)).mpr h1
      linarith
    have hexp_lt : Real.exp (-∑ p ∈ T, ((p - 1 : ℝ) / (p : ℝ) ^ 2)) < ε / 3 := by
      have harg : -∑ p ∈ T, ((p - 1 : ℝ) / (p : ℝ) ^ 2) < Real.log (ε / 3) := by
        have hneg : Real.log (ε / 3) = -Real.log (3 / ε) := by
          rw [← Real.log_inv, inv_div]
        linarith
      calc
        Real.exp (-∑ p ∈ T, ((p - 1 : ℝ) / (p : ℝ) ^ 2))
            < Real.exp (Real.log (ε / 3)) := Real.exp_lt_exp.mpr harg
        _ = ε / 3 := Real.exp_log (by positivity)
    exact hprod_le.trans_lt hexp_lt
  -- Step 2: For each `p ∈ T`, choose a root `r_p` and a finite set `Q_p` of primes `q ≡ r_p [MOD p]`
  -- with `μ_p ≥ 2` and `μ_p / (μ_p - 1)² < ε / (3 * (T.card + 1))`.
  have hQ_exists : ∀ p ∈ T,
      ∃ Q : Finset ℕ,
        (∀ q ∈ Q, q.Prime ∧ p ∣ σ 1 (q ^ 2)) ∧
        2 ≤ ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2) ∧
        (∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2)) /
          ((∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2)) - 1) ^ 2 <
          ε / (3 * ((T.card : ℝ) + 1)) := by
    intro p hp
    have hp_prime := hT_prime p hp
    have : NeZero p := ⟨hp_prime.ne_zero⟩
    obtain ⟨r, hr_unit, hr_dvd⟩ := exists_good_residue_of_prime_mod_six hp_prime (hT_mod p hp)
    have hdiv := tendsto_sum_alpha_primes_eq_mod (q := p) (a := r) hr_unit
    let δ : ℝ := ε / (3 * ((T.card : ℝ) + 1))
    have hδ_pos : 0 < δ := by positivity
    let B_bound : ℝ := max 2 (2 / δ + 2)
    obtain ⟨M, hM⟩ := Filter.eventually_atTop.mp ((tendsto_atTop.mp hdiv) B_bound)
    let Q := (Finset.range M).filter (fun q : ℕ => q.Prime ∧ (q : ZMod p) = r)
    have hμ_ge : B_bound ≤ ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2) := hM M le_rfl
    have hμ_ge2 : 2 ≤ ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2) :=
      (le_max_left _ _).trans hμ_ge
    refine ⟨Q, fun q hq => ?_, hμ_ge2, ?_⟩
    · rw [Finset.mem_filter] at hq
      exact ⟨hq.2.1, hr_dvd q hq.2.1 hq.2.2⟩
    · set μ := ∑ q ∈ Q, ((q - 1 : ℝ) / (q : ℝ) ^ 2)
      have hμ_gt : 2 / δ + 1 < μ := by
        have := (le_max_right (2 : ℝ) (2 / δ + 2)).trans hμ_ge
        linarith
      have hμ1_pos : 0 < μ - 1 := by linarith
      have h1 : μ ≤ 2 * (μ - 1) := by linarith
      have h2 : 2 / δ < μ - 1 := by linarith
      have h3 : μ / (μ - 1) ^ 2 ≤ 2 / (μ - 1) := by
        rw [div_le_div_iff₀ (pow_pos hμ1_pos 2) hμ1_pos]
        nlinarith
      have h4 : 2 / (μ - 1) < δ := by
        rw [div_lt_iff₀ hμ1_pos]
        have := (div_lt_iff₀ hδ_pos).mp h2
        linarith
      exact h3.trans_lt h4
  choose Q hQ_prop hQ_ge2 hQ_lt using hQ_exists
  -- Step 3: Covering `DrisSet ⊆ E_T ∪ ⋃_{p ∈ T} B̃_p`.
  have hcover : ∀ m ∈ DrisSet,
      (∀ p ∈ T, ¬ ExactDvd p m) ∨
      ∃ p : T, ((Q p.val p.property).filter (fun q => ExactDvd q m)).card ≤ 1 := by
    intro m hm
    by_contra hnot
    push Not at hnot
    obtain ⟨⟨p, hpT, hp_ex⟩, hgt1⟩ := hnot
    have hcard_ge2 : 2 ≤ ((Q p hpT).filter (fun q => ExactDvd q m)).card := hgt1 ⟨p, hpT⟩
    have hcard_gt1 : 1 < ((Q p hpT).filter (fun q => ExactDvd q m)).card := by omega
    obtain ⟨q₁, hq₁, q₂, hq₂, hne⟩ := Finset.one_lt_card.mp hcard_gt1
    rw [Finset.mem_filter] at hq₁ hq₂
    have hp₁ := hQ_prop p hpT q₁ hq₁.1
    have hp₂ := hQ_prop p hpT q₂ hq₂.1
    exact not_mem_drisSet_of_witnesses hp₁.1 hp₂.1 hne hp_ex hq₁.2 hq₂.2 hp₁.2 hp₂.2 hm
  -- Step 4: Combine finite union bound on `densityRatio` for all large `X`.
  let C_tot : ℝ :=
    ((∏ p ∈ T, p ^ 2 : ℕ) : ℝ) + ∑ p : T, ((∏ q ∈ Q p.val p.property, q ^ 2 : ℕ) : ℝ)
  have hC_nn : 0 ≤ C_tot := by positivity
  obtain ⟨X₀, hX₀⟩ := exists_nat_gt (3 * C_tot / ε)
  refine ⟨max 1 X₀, fun X hX => ?_⟩
  have hX1 : 1 ≤ X := (le_max_left 1 X₀).trans hX
  have hX0 : X₀ ≤ X := (le_max_right 1 X₀).trans hX
  have hX_pos : (0 : ℝ) < X := by exact_mod_cast hX1
  have hnonneg : 0 ≤ densityRatio DrisSet X := by
    unfold densityRatio; positivity
  rw [Real.dist_eq, sub_zero, abs_of_nonneg hnonneg]
  -- Finite union bound on `Icc 1 X`.
  have hunion :
      densityRatio DrisSet X ≤
        densityRatio {m : ℕ | ∀ p ∈ T, ¬ ExactDvd p m} X +
        ∑ p : T, densityRatio {m : ℕ | ((Q p.val p.property).filter (fun q => ExactDvd q m)).card ≤ 1} X :=
    densityRatio_le_add_sum DrisSet {m : ℕ | ∀ p ∈ T, ¬ ExactDvd p m}
      (fun p : T => {m : ℕ | ((Q p.val p.property).filter (fun q => ExactDvd q m)).card ≤ 1})
      hX1 hcover
  have hE_le := densityRatio_avoid_all_le T hT_prime hX1
  have hB_le :
      ∑ p : T, densityRatio {m : ℕ | ((Q p.val p.property).filter (fun q => ExactDvd q m)).card ≤ 1} X ≤
        (∑ p : T, (ε / (3 * ((T.card : ℝ) + 1)))) +
        (∑ p : T, ((∏ q ∈ Q p.val p.property, q ^ 2 : ℕ) : ℝ)) / (X : ℝ) := by
    rw [Finset.sum_div, ← Finset.sum_add_distrib]
    refine Finset.sum_le_sum fun p _ => ?_
    have h1 := densityRatio_bad_le (Q p.val p.property)
      (fun q hq => (hQ_prop p.val p.property q hq).1) (hQ_ge2 p.val p.property) hX1
    exact h1.trans (add_le_add (hQ_lt p.val p.property).le le_rfl)
  have hB_sum_lt : ∑ _p : T, (ε / (3 * ((T.card : ℝ) + 1))) ≤ ε / 3 := by
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_coe, nsmul_eq_mul]
    have hden : (0 : ℝ) < (T.card : ℝ) + 1 := by positivity
    have hle : (T.card : ℝ) / ((T.card : ℝ) + 1) ≤ 1 := by
      rw [div_le_one hden]; linarith
    calc
      (T.card : ℝ) * (ε / (3 * ((T.card : ℝ) + 1)))
          = ((T.card : ℝ) / ((T.card : ℝ) + 1)) * (ε / 3) := by
            simp only [div_eq_mul_inv, mul_inv]
            ring
      _ ≤ 1 * (ε / 3) := mul_le_mul_of_nonneg_right hle (by positivity)
      _ = ε / 3 := one_mul _
  have hC_div_lt : C_tot / (X : ℝ) < ε / 3 := by
    have hX_gt : 3 * C_tot / ε < (X : ℝ) := hX₀.trans_le (by exact_mod_cast hX0)
    rw [div_lt_iff₀ hX_pos]
    have := (div_lt_iff₀ hε).mp hX_gt
    linarith
  have htotal :
      densityRatio DrisSet X < ε / 3 + ε / 3 + ε / 3 := by
    have h1 : densityRatio DrisSet X ≤
        (∏ p ∈ T, (1 - ((p - 1 : ℝ) / (p : ℝ) ^ 2))) +
        (∑ _p : T, (ε / (3 * ((T.card : ℝ) + 1)))) +
        C_tot / (X : ℝ) := by
      have hC_split : C_tot / (X : ℝ) =
          ((∏ p ∈ T, p ^ 2 : ℕ) : ℝ) / (X : ℝ) +
          (∑ p : T, ((∏ q ∈ Q p.val p.property, q ^ 2 : ℕ) : ℝ)) / (X : ℝ) := by
        dsimp only [C_tot]; rw [add_div]
      linarith [hunion, hE_le, hB_le]
    linarith [h1, hprod_lt, hB_sum_lt, hC_div_lt]
  linarith

#print axioms not_summable_one_div_primes_eq_mod
#print axioms dris_conjecture_5_1

end OpenMath.Dris220208116Conj51
