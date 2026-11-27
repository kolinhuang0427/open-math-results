# Adversarial Audit Report (`audit-1`): `targets/oeis-A121747/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A121747` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `@scout-5` patch in `#548`), `notes/check-check-1.md`, `notes/check-check-1.py`, and live OEIS `A121747` (rev. 15, `2024-08-21T12:26:20-04:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A121747` JSON (rev. 15, `2024-08-21T12:26:20-04:00`, offset `1,2`):
  - Sequence name and primary recurrence $a(n) = n\,a(n-1) - d(n-1) + (n-1)!\lfloor n/2\rfloor$ ($n \ge 2$, $a(1) = 1$) with $d(1) = 1, d(2) = 0, d(2m) = \sum_{j=1}^{m-1}(2j+1)!$ ($m \ge 2$), $d(2m+1) = -d(2m)$ ($m \ge 1$) match verbatim, reproducing all 21 live OEIS terms.
  - All 6 polynomials $C_0(n), \dots, C_5(n)$ of R. J. Mathar's Jul 26 2022 `Conjecture D-finite with recurrence ... = 0` match verbatim.
  - Quantifier domain $n \ge 6$ covers every integer $n$ for which all arguments $n-5, \dots, n$ lie in the offset-$1$ domain $\mathbb{Z}_{\ge 1}$.

## 2. Line-by-Line Mathematical Audit
- **Step 1 (`PROOF.md` L12–21 — re-audited after `#548` patch):**
  - Prior FAIL Issue 1 ($m = 1$ boundary slip invoking undefined $d(0)$) is resolved: L20 explicitly verifies $d(2) + d(1) = 0 + 1 = 1!$ for $m = 1$ and uses the defining equations for $m \ge 2$, establishing $W(2m) = (2m-2)!(2m^2-1)$ ($m \ge 2$) and $W(2m+1) = (2m-1)!(2m^2+m-1)$ ($m \ge 1$) without boundary gaps.
- **Step 2 (`PROOF.md` L23–36):** Exact operator factorization $M(n) = \sum_{i=0}^3 c_i(n) W(n-i)$ identically in $\mathbb{Z}[n]$ for all $n \ge 6$.
- **Step 3 (`PROOF.md` L38–59 — re-audited after `#548` patch):**
  - Prior FAIL Issue 2 (spurious extra $(2r-5)$ factor in $P_{\mathrm{even}}(r)$) is resolved: the extraneous $(2r-5)$ factor has been removed from all 4 terms of $P_{\mathrm{even}}(r)$, so $M(2r) = (2r-5)!\, P_{\mathrm{even}}(r)$ ($r \ge 3$) and $M(2r+1) = (2r-4)!\, P_{\mathrm{odd}}(r)$ ($r \ge 3$) both hold with exact factorial ratios and positive factors for all $n \ge 6$, and both $P_{\mathrm{even}}(r)$ and $P_{\mathrm{odd}}(r)$ vanish identically in $\mathbb{Z}[r]$ (verified independently by auditor and equivalent in the integral domain $\mathbb{Z}[r]$ to $(2r-5)P_{\mathrm{even}}(r) = 0$ checked in `check-check-1.py`).
- **Step 4 (`PROOF.md` L61–66 — re-audited after `#548` patch):**
  - Prior FAIL Issue 3 (three wrong coefficients in the $m = 0$ boundary sum) is resolved: L66 now evaluates $C_0(5),\dots,C_4(5)$ verbatim as $(-7)(262) + 21(44) + 207(8) - 135(2) - 476(1) = 0$.
  - With $a(0) = 0$, $\sum_{m \ge 1} M(m+5)\frac{x^m}{m!} = 0$ yields a non-trivial homogeneous order-6 polynomial-coefficient linear ODE for $\hat{y}(x)$ with nonzero leading coefficient $-9x(x-1)^2(x+1)$ on $\hat{y}^{(6)}(x)$, proving D-finiteness.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A121747/notes/check-check-1.py` -> exit code `0`, `PASS` (verified OEIS data, Step 1 $k=3..60$, Step 2 in $\mathbb{Z}[n]$, Step 3 exact $\mathbb{Z}[r]$ vanishing, $M(n)=0$ for $n=6..60$, and homogeneous order-6 EGF ODE with leading coeff $-9x(x-1)^2(x+1)$ through $x^{39}$; plus auditor verified all 21 live OEIS terms and exact reduced $P_{\mathrm{even}}(r) \equiv 0$ in $\mathbb{Z}[r]$).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#504`, `watch-5` `#500`, `watch-6` `#499`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
