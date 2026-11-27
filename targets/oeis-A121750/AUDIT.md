# Adversarial Audit Report (`audit-1`): `targets/oeis-A121750/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A121750` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `@scout-5` Step 1 patch in `#559`), `notes/check-check-2.md`, `notes/check-check-2.py`, and live OEIS `A121750` (rev. 13, `2024-08-20T11:15:52-04:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A121750` JSON (rev. 13, `2024-08-20T11:15:52-04:00`, offset `1,3`):
  - Sequence name and primary recurrence $a(n) = n\,a(n-1) + d(n-1) + (n-1)!\lfloor(n-1)/2\rfloor$ ($n \ge 2$, $a(1) = 0$) with $d(1) = 1, d(2) = 0, d(2m) = \sum_{j=1}^{m-1}(2j+1)!$ ($m \ge 2$), $d(2m+1) = -d(2m)$ ($m \ge 1$) match verbatim, reproducing all 19 live OEIS terms.
  - All 7 polynomials $C_0(n), \dots, C_6(n)$ of R. J. Mathar's Jul 26 2022 `Conjecture D-finite with recurrence ... = 0` match verbatim.
  - Quantifier domain $n \ge 7$ covers every integer $n$ for which all arguments $n-6, \dots, n$ lie in the offset-$1$ domain $\mathbb{Z}_{\ge 1}$.

## 2. Line-by-Line Mathematical Audit
- **Step 1 (`PROOF.md` L12–21 — re-audited after `#559` patch):**
  - Prior FAIL issue (L20 boundary slip invoking undefined $d(0)$ at $m = 1$) is completely resolved: L20 now explicitly evaluates $d(2) + d(1) = 0 + 1 = 1!$ for $m = 1$ and uses the defining equations for $m \ge 2$, establishing $W(2m) = (2m-2)!(2m^2-2m)$ ($m \ge 2$) and $W(2m+1) = (2m-1)!(2m^2+m)$ ($m \ge 1$) without boundary gaps.
- **Step 2 (`PROOF.md` L23–37):** Exact operator factorization $M(n) = \sum_{i=0}^4 c_i(n) W(n-i)$ identically in $\mathbb{Z}[n]$ for all $n \ge 7$.
- **Step 3 (`PROOF.md` L39–62):** Both $M(2r) = (2r-6)!\, P_{\mathrm{even}}(r)$ ($r \ge 4$) and $M(2r+1) = (2r-5)!\, P_{\mathrm{odd}}(r)$ ($r \ge 3$) have exact factorial ratios with positive factors for all $n \ge 7$, and $P_{\mathrm{even}}(r) = P_{\mathrm{odd}}(r) \equiv 0$ in $\mathbb{Z}[r]$.
- **Step 4 (`PROOF.md` L64–69):** Exact $m = 0$ boundary sum $1(1338) - 8(184) - 14(26) + 95(5) + 20(1) = -3$, exact order-6 leading coefficient $1 - x - x^2 + x^3 = (1-x)^2(1+x) \neq 0$, and differentiation eliminates $-3$ to give a non-trivial homogeneous order-7 polynomial-coefficient linear ODE with leading coefficient $(1-x)^2(1+x)$ on $\hat{y}^{(7)}(x)$, proving D-finiteness of $\hat{y}(x)$.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A121750/notes/check-check-2.py` -> exit code `0`, `PASS` (verified OEIS data $n=1..19$, Step 1 $k=3..80$, Step 2 in $\mathbb{Z}[n]$, $P_{\mathrm{even}} = P_{\mathrm{odd}} = 0$, $M(n)=0$ for $n=7..80$, and the order-6/7 EGF ODE through $x^{18}$).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#504`, `watch-5` `#500`, `watch-6` `#499`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
