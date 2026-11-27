import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.Factorization.PrimePow
import Mathlib.Data.PNat.Defs
import Mathlib.Tactic

/-!
# Proof of Ziller's Conjecture 6.2 (`arXiv:2310.15628v2`)

Primary source:
Mario Ziller, *"On the distribution of values of Euler's totient function"* (v2 `2026-04-15`),
`arXiv:2310.15628v2`, Section 6 ("Concluding remarks"), Conjecture 6.2:
> **Conjecture 6.2.** All function values of `φ(x) / x^2` for `x ∈ ℕ` (`ℕ = {1, 2, 3, ...}`)
> are pairwise distinct.

(Section 6 also notes the equivalent reciprocal claim that `x^2 / φ(x)` is injective on `ℕ`.)

This file formalizes the complete proof (zero `sorry`, zero `native_decide`, standard axioms only):
1. `factorization_totient_of_primeFactors_le`: if `p` is prime and every prime factor `q` of
   `n > 0` satisfies `q ≤ p`, then `(Nat.totient n).factorization p = if p ∣ n then n.factorization p - 1 else 0`.
2. `totient_mul_sq_inj`: for positive integers `x, y > 0`, `φ(x) * y^2 = φ(y) * x^2 → x = y`.
3. **Main Theorems:**
   - `ziller_conjecture_6_2`: `(φ(x) : ℚ) / x^2 = (φ(y) : ℚ) / y^2 → x = y` for `x, y > 0`.
   - `ziller_conjecture_6_2_pnat`: `Function.Injective (fun x : ℕ+ => (Nat.totient x : ℚ) / (x : ℚ) ^ 2)`.
   - `ziller_conjecture_6_2_reciprocal`: `(x : ℚ)^2 / φ(x) = (y : ℚ)^2 / φ(y) → x = y` for `x, y > 0`.
-/

namespace OpenMath.Ziller231015628Conj62

/-- If `p` is prime and every prime factor `q` of `m > 0` satisfies `q < p`, then `p ∤ φ(m)`. -/
lemma not_dvd_totient_of_primeFactors_lt {p : ℕ} (hp : p.Prime) :
    ∀ m : ℕ, 0 < m → (∀ q ∈ m.primeFactors, q < p) → ¬ (p ∣ Nat.totient m) := by
  intro m
  induction m using Nat.strong_induction_on with
  | ind m ih =>
    intro hm hlt
    by_cases hm1 : m = 1
    · subst hm1
      simp [hp.not_dvd_one]
    · have hne : m.primeFactors.Nonempty := Nat.nonempty_primeFactors.mpr (by omega)
      obtain ⟨q, hq_mem⟩ := hne
      have hq_prime : q.Prime := Nat.prime_of_mem_primeFactors hq_mem
      have hq_dvd : q ∣ m := Nat.dvd_of_mem_primeFactors hq_mem
      have hq_lt : q < p := hlt q hq_mem
      set e := m.factorization q
      have he_pos : 0 < e := Nat.Prime.factorization_pos_of_dvd hq_prime hm.ne' hq_dvd
      have hqe_dvd : q ^ e ∣ m := Nat.ordProj_dvd m q
      set r := m / q ^ e
      have hm_eq : m = q ^ e * r := (Nat.mul_div_cancel' hqe_dvd).symm
      have hr_pos : 0 < r := by
        rcases Nat.eq_zero_or_pos r with hr0 | hrpos
        · rw [hr0, mul_zero] at hm_eq; omega
        · exact hrpos
      have hq_not_dvd_r : ¬ (q ∣ r) := by
        intro hqr
        have hq_succ : q ^ (e + 1) ∣ m := by
          rw [hm_eq, pow_succ]
          exact mul_dvd_mul_left (q ^ e) hqr
        have hle := (hq_prime.pow_dvd_iff_le_factorization hm.ne').mp hq_succ
        omega
      have hcop : Nat.Coprime (q ^ e) r :=
        (hq_prime.coprime_iff_not_dvd.mpr hq_not_dvd_r).pow_left e
      have hqe_gt1 : 1 < q ^ e := one_lt_pow₀ hq_prime.one_lt he_pos.ne'
      have hr_lt : r < m := by
        calc
          r = 1 * r := (one_mul r).symm
          _ < q ^ e * r := Nat.mul_lt_mul_of_pos_right hqe_gt1 hr_pos
          _ = m := hm_eq.symm
      have hr_primeFactors : ∀ s ∈ r.primeFactors, s < p := by
        intro s hs
        apply hlt s
        rw [Nat.mem_primeFactors] at hs ⊢
        exact ⟨hs.1, hs.2.1.trans ⟨q ^ e, by rw [hm_eq, mul_comm]⟩, hm.ne'⟩
      have hnot_r : ¬ (p ∣ Nat.totient r) := ih r hr_lt hr_pos hr_primeFactors
      have hnot_q : ¬ (p ∣ q) := Nat.not_dvd_of_pos_of_lt hq_prime.pos hq_lt
      have hnot_q1 : ¬ (p ∣ q - 1) :=
        Nat.not_dvd_of_pos_of_lt (Nat.sub_pos_of_lt hq_prime.one_lt) (by omega)
      have hnot_qe : ¬ (p ∣ Nat.totient (q ^ e)) := by
        rw [Nat.totient_prime_pow hq_prime he_pos]
        intro hd
        rcases hp.dvd_mul.mp hd with h1 | h2
        · exact hnot_q (hp.dvd_of_dvd_pow h1)
        · exact hnot_q1 h2
      rw [hm_eq, Nat.totient_mul hcop]
      intro hd
      rcases hp.dvd_mul.mp hd with h1 | h2
      · exact hnot_qe h1
      · exact hnot_r h2

/-- If `p` is prime and every prime factor of `n > 0` is `≤ p`, then
`v_p(φ(n)) = v_p(n) - 1` if `p ∣ n` and `0` otherwise. -/
lemma factorization_totient_of_primeFactors_le {p n : ℕ} (hp : p.Prime) (hn : 0 < n)
    (hle : ∀ q ∈ n.primeFactors, q ≤ p) :
    (Nat.totient n).factorization p = if p ∣ n then n.factorization p - 1 else 0 := by
  set e := n.factorization p
  have hpe_dvd : p ^ e ∣ n := Nat.ordProj_dvd n p
  set m := n / p ^ e
  have hn_eq : n = p ^ e * m := (Nat.mul_div_cancel' hpe_dvd).symm
  have hm_pos : 0 < m := by
    rcases Nat.eq_zero_or_pos m with hm0 | hmpos
    · rw [hm0, mul_zero] at hn_eq; omega
    · exact hmpos
  have hp_not_dvd_m : ¬ (p ∣ m) := by
    intro hpm
    have hsucc : p ^ (e + 1) ∣ n := by
      rw [hn_eq, pow_succ]
      exact mul_dvd_mul_left (p ^ e) hpm
    have hle' := (hp.pow_dvd_iff_le_factorization hn.ne').mp hsucc
    omega
  have hcop : Nat.Coprime (p ^ e) m :=
    (hp.coprime_iff_not_dvd.mpr hp_not_dvd_m).pow_left e
  have hm_lt : ∀ q ∈ m.primeFactors, q < p := by
    intro q hq
    have hq_n : q ∈ n.primeFactors := by
      rw [Nat.mem_primeFactors] at hq ⊢
      exact ⟨hq.1, hq.2.1.trans ⟨p ^ e, by rw [hn_eq, mul_comm]⟩, hn.ne'⟩
    have hq_le : q ≤ p := hle q hq_n
    have hq_ne : q ≠ p := by
      intro heq
      subst heq
      exact hp_not_dvd_m (Nat.dvd_of_mem_primeFactors hq)
    omega
  have hnot_tm : ¬ (p ∣ Nat.totient m) := not_dvd_totient_of_primeFactors_lt hp m hm_pos hm_lt
  have hfac_tm : (Nat.totient m).factorization p = 0 :=
    Nat.factorization_eq_zero_of_not_dvd hnot_tm
  by_cases hpdvd : p ∣ n
  · rw [ite_eq_left hpdvd]
    have he_pos : 0 < e := hp.factorization_pos_of_dvd hn.ne' hpdvd
    have htot_eq : Nat.totient n = p ^ (e - 1) * (p - 1) * Nat.totient m := by
      rw [hn_eq, Nat.totient_mul hcop, Nat.totient_prime_pow hp he_pos]
    have hne1 : p ^ (e - 1) ≠ 0 := (pow_pos hp.pos _).ne'
    have hne2 : p - 1 ≠ 0 := by have := hp.two_le; omega
    have hne3 : Nat.totient m ≠ 0 := (Nat.totient_pos.mpr hm_pos).ne'
    have hfac_p1 : (p - 1).factorization p = 0 :=
      Nat.factorization_eq_zero_of_not_dvd
        (Nat.not_dvd_of_pos_of_lt (Nat.sub_pos_of_lt hp.one_lt) (by omega))
    rw [htot_eq, Nat.factorization_mul (mul_ne_zero hne1 hne2) hne3,
      Nat.factorization_mul hne1 hne2, Finsupp.add_apply, Finsupp.add_apply,
      hp.factorization_pow, Finsupp.single_eq_same, hfac_p1, hfac_tm]
    omega
  · rw [ite_eq_right hpdvd]
    have he0 : e = 0 := Nat.factorization_eq_zero_of_not_dvd hpdvd
    have hmn : m = n := by rw [hn_eq, he0, pow_zero, one_mul]
    rw [← hmn, hfac_tm]

/-- Core integer form of Ziller's Conjecture 6.2:
for positive integers `x, y > 0`, `φ(x) * y^2 = φ(y) * x^2` implies `x = y`. -/
theorem totient_mul_sq_inj :
    ∀ {x y : ℕ}, 0 < x → 0 < y → Nat.totient x * y ^ 2 = Nat.totient y * x ^ 2 → x = y := by
  intro x y hx hy heq
  -- Strong induction on `N = x * y`
  have hmain : ∀ N : ℕ, ∀ x y : ℕ, x * y = N → 0 < x → 0 < y →
      Nat.totient x * y ^ 2 = Nat.totient y * x ^ 2 → x = y := by
    intro N
    induction N using Nat.strong_induction_on with
    | ind N ih =>
      intro x y hxy hx hy heq
      by_cases hxeq : x = y
      · exact hxeq
      · have hgt1 : 1 < x * y := by
          rcases Nat.eq_or_lt_of_le (Nat.one_le_iff_ne_zero.mpr hx.ne') with rfl | hx2
          · have hy2 : 1 < y := by omega
            omega
          · nlinarith
        have hne_pf : (x * y).primeFactors.Nonempty := Nat.nonempty_primeFactors.mpr hgt1
        set p := (x * y).primeFactors.max' hne_pf
        have hp_mem : p ∈ (x * y).primeFactors := Finset.max'_mem _ hne_pf
        have hp : p.Prime := Nat.prime_of_mem_primeFactors hp_mem
        have hp_dvd_xy : p ∣ x * y := Nat.dvd_of_mem_primeFactors hp_mem
        have hle_xy : ∀ q ∈ (x * y).primeFactors, q ≤ p := fun q hq => Finset.le_max' _ q hq
        have hle_x : ∀ q ∈ x.primeFactors, q ≤ p := by
          intro q hq
          apply hle_xy q
          rw [Nat.mem_primeFactors] at hq ⊢
          exact ⟨hq.1, hq.2.1.trans (dvd_mul_right x y), (Nat.mul_pos hx hy).ne'⟩
        have hle_y : ∀ q ∈ y.primeFactors, q ≤ p := by
          intro q hq
          apply hle_xy q
          rw [Nat.mem_primeFactors] at hq ⊢
          exact ⟨hq.1, hq.2.1.trans (dvd_mul_left y x), (Nat.mul_pos hx hy).ne'⟩
        -- Compare `p`-adic valuations of both sides of `φ(x) * y^2 = φ(y) * x^2`
        have hfac_eq := congrArg (fun n => n.factorization p) heq
        have htx0 : Nat.totient x ≠ 0 := (Nat.totient_pos.mpr hx).ne'
        have hty0 : Nat.totient y ≠ 0 := (Nat.totient_pos.mpr hy).ne'
        have hx20 : x ^ 2 ≠ 0 := (pow_pos hx 2).ne'
        have hy20 : y ^ 2 ≠ 0 := (pow_pos hy 2).ne'
        rw [Nat.factorization_mul htx0 hy20, Nat.factorization_mul hty0 hx20,
          Finsupp.add_apply, Finsupp.add_apply, Nat.factorization_pow, Nat.factorization_pow,
          Finsupp.smul_apply, Finsupp.smul_apply, smul_eq_mul, smul_eq_mul,
          factorization_totient_of_primeFactors_le hp hx hle_x,
          factorization_totient_of_primeFactors_le hp hy hle_y] at hfac_eq
        have hpdvd_or : p ∣ x ∨ p ∣ y := hp.dvd_mul.mp hp_dvd_xy
        have hpdvd_x : p ∣ x := by
          by_contra hnx
          have hpy : p ∣ y := hpdvd_or.resolve_left hnx
          have hx0 : x.factorization p = 0 := Nat.factorization_eq_zero_of_not_dvd hnx
          have hy_pos : 0 < y.factorization p := hp.factorization_pos_of_dvd hy.ne' hpy
          rw [ite_eq_right hnx, ite_eq_left hpy, hx0] at hfac_eq
          omega
        have hpdvd_y : p ∣ y := by
          by_contra hny
          have hy0 : y.factorization p = 0 := Nat.factorization_eq_zero_of_not_dvd hny
          have hx_pos : 0 < x.factorization p := hp.factorization_pos_of_dvd hx.ne' hpdvd_x
          rw [ite_eq_left hpdvd_x, ite_eq_right hny, hy0] at hfac_eq
          omega
        rw [ite_eq_left hpdvd_x, ite_eq_left hpdvd_y] at hfac_eq
        set e := x.factorization p
        have he_pos : 0 < e := hp.factorization_pos_of_dvd hx.ne' hpdvd_x
        have hey : y.factorization p = e := by
          have hy_pos : 0 < y.factorization p := hp.factorization_pos_of_dvd hy.ne' hpdvd_y
          omega
        -- Strip `p ^ e` from both `x` and `y`
        have hpe_x : p ^ e ∣ x := Nat.ordProj_dvd x p
        have hpe_y : p ^ e ∣ y := hey ▸ Nat.ordProj_dvd y p
        set x₀ := x / p ^ e
        set y₀ := y / p ^ e
        have hx_eq : x = p ^ e * x₀ := (Nat.mul_div_cancel' hpe_x).symm
        have hy_eq : y = p ^ e * y₀ := (Nat.mul_div_cancel' hpe_y).symm
        have hx₀_pos : 0 < x₀ := by
          rcases Nat.eq_zero_or_pos x₀ with h0 | hpos
          · rw [h0, mul_zero] at hx_eq; omega
          · exact hpos
        have hy₀_pos : 0 < y₀ := by
          rcases Nat.eq_zero_or_pos y₀ with h0 | hpos
          · rw [h0, mul_zero] at hy_eq; omega
          · exact hpos
        have hnot_x₀ : ¬ (p ∣ x₀) := by
          intro hd
          have hsucc : p ^ (e + 1) ∣ x := by
            rw [hx_eq, pow_succ]; exact mul_dvd_mul_left (p ^ e) hd
          have := (hp.pow_dvd_iff_le_factorization hx.ne').mp hsucc
          omega
        have hnot_y₀ : ¬ (p ∣ y₀) := by
          intro hd
          have hsucc : p ^ (e + 1) ∣ y := by
            rw [hy_eq, pow_succ]; exact mul_dvd_mul_left (p ^ e) hd
          have := (hp.pow_dvd_iff_le_factorization hy.ne').mp hsucc
          omega
        have hcop_x : Nat.Coprime (p ^ e) x₀ :=
          (hp.coprime_iff_not_dvd.mpr hnot_x₀).pow_left e
        have hcop_y : Nat.Coprime (p ^ e) y₀ :=
          (hp.coprime_iff_not_dvd.mpr hnot_y₀).pow_left e
        have heq' : Nat.totient x₀ * y₀ ^ 2 = Nat.totient y₀ * x₀ ^ 2 := by
          rw [hx_eq, hy_eq, Nat.totient_mul hcop_x, Nat.totient_mul hcop_y,
            mul_pow, mul_pow] at heq
          have hfac_pos : 0 < Nat.totient (p ^ e) * (p ^ e) ^ 2 :=
            Nat.mul_pos (Nat.totient_pos.mpr (pow_pos hp.pos e)) (pow_pos (pow_pos hp.pos e) 2)
          have hrew :
              (Nat.totient (p ^ e) * (p ^ e) ^ 2) * (Nat.totient x₀ * y₀ ^ 2) =
              (Nat.totient (p ^ e) * (p ^ e) ^ 2) * (Nat.totient y₀ * x₀ ^ 2) := by
            linarith
          exact Nat.eq_of_mul_eq_mul_left hfac_pos hrew
        have hpe_gt1 : 1 < p ^ e := one_lt_pow₀ hp.one_lt he_pos.ne'
        have hlt_N : x₀ * y₀ < N := by
          rw [← hxy, hx_eq, hy_eq]
          have hmul_eq : p ^ e * x₀ * (p ^ e * y₀) = (p ^ e * p ^ e) * (x₀ * y₀) := by ring
          rw [hmul_eq]
          have hpp : 1 < p ^ e * p ^ e := by nlinarith
          calc
            x₀ * y₀ = 1 * (x₀ * y₀) := (one_mul _).symm
            _ < (p ^ e * p ^ e) * (x₀ * y₀) :=
              Nat.mul_lt_mul_of_pos_right hpp (Nat.mul_pos hx₀_pos hy₀_pos)
        have hxy₀ : x₀ = y₀ := ih (x₀ * y₀) hlt_N x₀ y₀ rfl hx₀_pos hy₀_pos heq'
        rw [hx_eq, hy_eq, hxy₀]
  exact hmain (x * y) x y rfl hx hy heq

/-- **Main Theorem (Ziller `arXiv:2310.15628v2`, Conjecture 6.2):**
All function values of `φ(x) / x^2` for positive integers `x ∈ ℕ` are pairwise distinct. -/
theorem ziller_conjecture_6_2 {x y : ℕ} (hx : 0 < x) (hy : 0 < y)
    (h : (Nat.totient x : ℚ) / (x : ℚ) ^ 2 = (Nat.totient y : ℚ) / (y : ℚ) ^ 2) :
    x = y := by
  have hx2 : (x : ℚ) ^ 2 ≠ 0 := pow_ne_zero 2 (Nat.cast_ne_zero.mpr hx.ne')
  have hy2 : (y : ℚ) ^ 2 ≠ 0 := pow_ne_zero 2 (Nat.cast_ne_zero.mpr hy.ne')
  have hq : (Nat.totient x : ℚ) * (y : ℚ) ^ 2 = (Nat.totient y : ℚ) * (x : ℚ) ^ 2 := by
    field_simp at h
    linarith
  have hn : Nat.totient x * y ^ 2 = Nat.totient y * x ^ 2 := by
    exact_mod_cast hq
  exact totient_mul_sq_inj hx hy hn

/-- Equivalent `PNat` (`ℕ+`) injectivity formulation of Conjecture 6.2. -/
theorem ziller_conjecture_6_2_pnat :
    Function.Injective (fun x : ℕ+ => (Nat.totient x : ℚ) / (x : ℚ) ^ 2) := by
  intro x y h
  exact Subtype.ext (ziller_conjecture_6_2 x.pos y.pos h)

/-- Equivalent reciprocal formulation noted in Section 6 of `arXiv:2310.15628v2`:
`x^2 / φ(x)` is injective on positive integers. -/
theorem ziller_conjecture_6_2_reciprocal {x y : ℕ} (hx : 0 < x) (hy : 0 < y)
    (h : (x : ℚ) ^ 2 / (Nat.totient x : ℚ) = (y : ℚ) ^ 2 / (Nat.totient y : ℚ)) :
    x = y := by
  have htx : (Nat.totient x : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.totient_pos.mpr hx).ne'
  have hty : (Nat.totient y : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.totient_pos.mpr hy).ne'
  have hq : (Nat.totient x : ℚ) * (y : ℚ) ^ 2 = (Nat.totient y : ℚ) * (x : ℚ) ^ 2 := by
    field_simp at h
    linarith
  have hn : Nat.totient x * y ^ 2 = Nat.totient y * x ^ 2 := by
    exact_mod_cast hq
  exact totient_mul_sq_inj hx hy hn

#print axioms totient_mul_sq_inj
#print axioms ziller_conjecture_6_2
#print axioms ziller_conjecture_6_2_pnat
#print axioms ziller_conjecture_6_2_reciprocal

end OpenMath.Ziller231015628Conj62
