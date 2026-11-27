# Adversarial Audit Report (`audit-1`): `targets/oeis-A121752/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A121752` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `@scout-5` patch in `#548`), `notes/check-check-2.md`, `notes/check-check-2.py`, and live OEIS `A121752` (rev. 4, `2022-07-26T11:29:39-04:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A121752` JSON (rev. 4, `2022-07-26T11:29:39-04:00`, offset `1,2`):
  - Sequence name and primary recurrence $a(n) = (2n-3)a(n-1) - (n-1)(n-3)a(n-2) + (n-2)!\bigl(n\lfloor n/2\rfloor - (n-2)\lfloor(n-1)/2\rfloor - 1\bigr)$ with $a(1) = 1, a(2) = 2$ match verbatim.
  - All 6 polynomials $C_0(n), \dots, C_5(n)$ of R. J. Mathar's Jul 26 2022 `Conjecture D-finite with recurrence ... = 0` match verbatim.
  - Quantifier domain $n \ge 6$ covers every integer $n$ for which all arguments $n-5, \dots, n$ lie in the offset-$1$ domain $\mathbb{Z}_{\ge 1}$.

## 2. Line-by-Line Mathematical Audit
- **Step 1 (`PROOF.md` L17–32):** Exact first-order reduction $D(k) - (k-3)D(k-1) = (k-2)! f(k)$ ($k \ge 3$), base $D(3) = 1$, telescoping $D(k) = (k-3)! S(k)$ for all $k \ge 3$, parity formulas $f(2m) = 4m-3$, $f(2m+1) = 2m-1$, and induction for $S(2r) = (r-1)(4r^2-3r+1)$ ($r \ge 2$) and $S(2r+1) = r^2(4r-3)$ ($r \ge 1$).
- **Step 2 (`PROOF.md` L34–48):** Exact operator factorization $M(n) = \sum_{i=0}^4 e_i(n) D(n-i)$ identically in $\mathbb{Z}[n]$ for all $n \ge 6$.
- **Step 3 (`PROOF.md` L50–79 — re-audited after `#548` patch):**
  - Prior FAIL Issue 1 ($M(6) = P_{\mathrm{even}}(3)$ zero-factor bug) is completely resolved: $M(6) = 0$ is evaluated directly from $e_4(6) = 0$, $(e_0(6),\dots,e_3(6)) = (-1537, 4529, 32700, -24428)$, and $(D(6),\dots,D(3)) = (336, 40, 11, 1)$ as $-516432 + 181160 + 359700 - 24428 = 0$; $M(2r) = (2r-7)! P_{\mathrm{even}}(r)$ is restricted strictly to $r \ge 4$ ($n \ge 8$) and $M(2r+1) = (2r-6)! P_{\mathrm{odd}}(r)$ holds for all $r \ge 3$ ($n \ge 7$), with $P_{\mathrm{even}}(r) = P_{\mathrm{odd}}(r) \equiv 0 \in \mathbb{Z}[r]$.
  - Prior FAIL Issue 2 (D-finiteness boundary term & nontriviality) is completely resolved: extending $a(0) := 0$ and verifying $M(5) = \sum_{j=0}^5 C_j(5) a(5-j) = 0$ directly from $(C_0(5),\dots,C_4(5)) = (-1077, 8231, 2428, -43474, 2038)$ and $(a(5),\dots,a(1)) = (235, 39, 7, 2, 1)$, $\sum_{m \ge 0} M(m+5)\frac{x^m}{m!} = 0$ translates directly into a non-trivial homogeneous order-6 polynomial-coefficient linear ODE $L[\hat{y}](x) = 0$ with leading $\hat{y}^{(6)}(x)$ coefficient $-460x(x-1)^2(x+1) \not\equiv 0$ (where the $-460x$ term comes from $C_0(m+5) = -460m - 1077$ and $+460x^2 + 460x^3 - 460x^4$ from $C_1, C_2, C_3$), proving D-finiteness of $\hat{y}(x)$.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python targets/oeis-A121752/notes/check-check-2.py` -> exit code `0`, `PASS` (verified all 19 live OEIS rev. 4 terms, Step 1 $k=3..80$, Step 2 in $\mathbb{Z}[n]$, $P_{\mathrm{even}} = P_{\mathrm{odd}} = 0$ in $\mathbb{Z}[r]$, direct $M(n) = 0$ for $n = 6..80$, and EGF ODE; plus auditor verified exact order-6 leading coeff $-460x(x-1)^2(x+1)$ and $M(5) = 0$ symbolically).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#466`, `watch-5` `#461`, `watch-6` `#462`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
