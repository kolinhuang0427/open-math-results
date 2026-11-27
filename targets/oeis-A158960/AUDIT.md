# Adversarial Audit Report (`audit-1`): `targets/oeis-A158960/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A158960` — M. F. Hasler (Feb 16 2014) denominator conjecture for $H_n(1/5)$
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and live OEIS `A158960` (rev. 28, `2022-09-08T08:45:43-04:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A158960` JSON (rev. 28, `2022-09-08T08:45:43-04:00`, offset `0,2`):
  - `NAME`: `Numerator of Hermite(n, 1/5).`
  - `COMMENT`: `The denominators are 5^n = A000351(n) (conjectured). - _M. F. Hasler_, Feb 16 2014`
  - `FORMULA`: `D-finite with recurrence a(n) -2*a(n-1) +50*(n-1)*a(n-2)=0. [DLMF] - _R. J. Mathar_, Feb 16 2014` and `a(n) = 5^n * Hermite(n,1/5).` (G. C. Greubel).
  - Physicists' Hermite polynomials $H_0(x) = 1$, $H_1(x) = 2x$, $H_n(x) = 2x H_{n-1}(x) - 2(n-1) H_{n-2}(x)$ ($n \ge 2$, DLMF Table 18.9.1) match all 18 live OEIS data terms verbatim.

## 2. Line-by-Line Mathematical Audit
- Setting $b(n) := 5^n H_n(1/5)$ gives $b(0) = 1$, $b(1) = 2$, and for every $n \ge 2$:
  $$b(n) = 5^n \left(\frac{2}{5} H_{n-1}(1/5) - 2(n-1) H_{n-2}(1/5)\right) = 2 b(n-1) - 50(n-1) b(n-2).$$
- Induction yields $b(n) \in \mathbb{Z}$ and $b(n) \equiv 2^n \pmod 5$ for all $n \ge 0$ (since $50 \equiv 0 \pmod 5$, $b(0) = 1 = 2^0$, $b(1) = 2 = 2^1$).
- Because $5 \nmid 2^n$, we have $5 \nmid b(n)$ and hence $\gcd(b(n), 5^n) = 1$ for every $n \ge 0$ (including $n = 0$). Since $5^n > 0$, $H_n(1/5) = b(n)/5^n$ is in lowest terms, proving that the reduced denominator is $5^n$ and the numerator is $a(n) = b(n) = 5^n H_n(1/5)$ for all $n \ge 0$. Completely airtight.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A158960/notes/check-check-2.py` -> exit code `0`, `PASS` (verified all 18 live OEIS rev. 28 terms, exact `Fraction` evaluation of $H_n(1/5)$ with reduced denominator $5^n$ and $b(n) \equiv 2^n \not\equiv 0 \pmod 5$ for $0 \le n \le 100$, plus Greubel's explicit formula for $n \le 40$).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-5` `#664`, `watch-1` `#671`, `watch-6` `#672`; absent from `zenodo-23112421-oeis-ids.md`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).

---

## 4. Independent Lean 4 Statement-Fidelity Audit (Batch C, `2026-11-27T12:04Z`) — **PASS**

- **Module:** `lean/OpenMath/OeisA158960.lean` (imported in `lean/OpenMath.lean` L19; `.olean` present).
- **Statement fidelity vs live OEIS `A158960` (rev. 28) & `TARGET.md`:**
  - `physHermite` (L42–45) defines the physicists' Hermite polynomials $H_0(x) = 1$, $H_1(x) = 2x$, $H_{n+2}(x) = 2x H_{n+1}(x) - 2(n+1) H_n(x)$ (DLMF Table 18.9.1) over `Polynomial ℚ`.
  - `a158960` (L67–70) matches Mathar's recurrence $a(0)=1, a(1)=2, a(n+2)=2a(n+1)-50(n+1)a(n)$ (`a158960_initial` L146–149 checks `n = 0..7` matching live OEIS `%S`).
  - `hasler_conjecture_A158960 (n : ℕ)` (L131–133) proves `(Polynomial.eval (1 / 5 : ℚ) (physHermite n)).den = 5 ^ n ∧ (Polynomial.eval (1 / 5 : ℚ) (physHermite n)).num = a158960 n` for every `n : ℕ` (including `n = 0`), matching M. F. Hasler's 2014 conjecture verbatim with zero hidden hypotheses.
- **Hygiene & kernel check:** Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `partial`, `opaque`, or `set_option`.
- **Verification command:** `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/OeisA158960.lean` -> exit code `0`, 0 warnings.
- **Axioms (`#print axioms`):**
  - `OpenMath.OeisA158960.hermiteEval_eq_div`: `[propext, Classical.choice, Quot.sound]`
  - `OpenMath.OeisA158960.a158960_mod_five`: `[propext, Quot.sound]`
  - `OpenMath.OeisA158960.hasler_conjecture_A158960`: `[propext, Classical.choice, Quot.sound]`
- **Charter label upgrade:** **PASS** — eligible for `"machine-checked proof in Lean 4"`.
