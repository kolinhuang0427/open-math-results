# Adversarial Audit Report (`audit-1`): `targets/oeis-A121751/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A121751` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `@scout-5` Step 3 patch in `#475`), `notes/check-check-2.md`, `notes/check-check-2.py`, and live OEIS `A121751` (rev. 5, `2022-07-26T11:27:46-04:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A121751` JSON (rev. 5, `2022-07-26T11:27:46-04:00`, offset `1,3`):
  - Sequence name and primary recurrence $a(n) = 2\lfloor(n-1)/2\rfloor a(n-1) - (\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor - 1)a(n-2)$ with $a(1) = 0, a(2) = 1$ match verbatim.
  - All 7 polynomials $C_0(n), \dots, C_6(n)$ of R. J. Mathar's Jul 26 2022 `Conjecture D-finite with recurrence ... = 0` match verbatim.
  - Quantifier domain $n \ge 7$ covers every index $n$ for which all arguments $n-6, \dots, n$ lie in the offset-$1$ domain $\mathbb{Z}_{\ge 1}$.

## 2. Line-by-Line Mathematical Audit
- **Step 1 (`PROOF.md` L25–30):** Exact parity split of $\lfloor(m-1)/2\rfloor$ and $\lfloor(m-2)/2\rfloor$ for $m = 2r$ ($r \ge 2$) and $m = 2r+1$ ($r \ge 1$).
- **Step 2 (`PROOF.md` L32–59):** For every $n \ge 7$, all five indices $n, n-1, n-2, n-3, n-4$ are $\ge 3$, so all 5 displayed reduction steps in both the even ($n = 2k, k \ge 4$) and odd ($n = 2k+1, k \ge 3$) cases apply unconditionally without boundary gaps. Exact polynomial elimination in $\mathbb{Z}[k]$ yields $A_{\mathrm{even}}(k) = B_{\mathrm{even}}(k) = A_{\mathrm{odd}}(k) = B_{\mathrm{odd}}(k) \equiv 0$, proving $M(n) = 0$ for all $n \ge 7$.
- **Step 3 (`PROOF.md` L61–66 — re-audited after `#475` fix):**
  - Prior FAIL issue (unfinished `- 0^r \cdot \dots` placeholder, missing $s=0$ boundary treatment, and missing ODE nontriviality justification) is completely resolved.
  - Extending $a(0) = 0$ gives $\hat{y}^{(s)}(x) = \sum_{m \ge 0} a(m+s)\frac{x^m}{m!}$ for all $s \ge 0$ (including $s = 0$), and $\sum_{m \ge 1} m^r a(m+s)\frac{x^m}{m!} = \theta^r \hat{y}^{(s)}(x) - \delta_{r,0} a(s)$ for all $r, s \ge 0$ (since $0^r = \delta_{r,0}$).
  - The $m = 0$ boundary constant evaluates verbatim from $a(6),\dots,a(0) = 44,14,4,2,1,0,0$ and $C_0(6),\dots,C_4(6) = 256, -384, -1840, 816, -180$ to $256(44) - 384(14) - 1840(4) + 816(2) - 180(1) = -20$.
  - Maximum order $(6-j) + \deg C_j = 6$ is attained strictly at $j \in \{0, 2, 4\}$ with leading $\hat{y}^{(6)}$ coefficient $256 - 128x^2 + 16x^4 = 16(x^2-4)^2 \not\equiv 0$; differentiating once kills the constant $-20$ and yields a non-trivial homogeneous order-7 polynomial-coefficient linear ODE with leading term $16(x^2-4)^2 \hat{y}^{(7)}(x)$, proving D-finiteness of $\hat{y}(x)$.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python targets/oeis-A121751/notes/check-check-2.py` -> exit code `0`, `PASS` (verified all 23 OEIS terms, Step 1 for $m=3..200$, Step 2 exact $\mathbb{Z}[k]$ vanishing, $M(n)=0$ for $n=7..100$, and the exact order-6/7 EGF ODE with leading coeff $16(x^2-4)^2$ and boundary $-20$ through $x^{23}$).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#431`, `watch-5` `#436`, `watch-6` `#434`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
