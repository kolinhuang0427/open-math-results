# Independent Blind Audit — `targets/oeis-A045743/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:21Z`
- **Verdict:** **`FAIL`** *(1 blocking displayed-formula error on `PROOF.md` line 46: the explicit expansion of $P_y = \partial_y P$ omits the $+4x^3$ term; all underlying mathematics, primary-source fidelity, and independent exact verification PASS)*

---

## 1. Blocking Issue to Fix in `PROOF.md`

- **Line 46 (Step 2 — missing term in $\partial_y P$):**
  - Line 42 defines:
    $$P(x, y) = x^4 + 4x^3 y + 6x^2 y^2 - x^2 y + 4x y^3 - x y^2 + y^4 + y^3.$$
  - Line 46 writes:
    `Let $P_x = \partial_x P$ and $P_y = \partial_y P = -x^2 + (12x^2 - 2x)y + (12x + 3)y^2 + 4y^3$.`
  - **Error:** Differentiating $4x^3 y$ with respect to $y$ contributes $+4x^3$, which is omitted on line 46. The exact partial derivative is:
    $$P_y = \partial_y P = (4x^3 - x^2) + (12x^2 - 2x)y + (12x + 3)y^2 + 4y^3.$$
  - Note: $P_y(x, y(x)) = -x^2 + O(x^3) \neq 0$ still holds (the leading term remains $-x^2$), and the independent checker `notes/check-check-2.py` computed `Py = sp.diff(P_expr, y)` symbolically, so all downstream identities and the final recurrence hold.
  - **Fix:** Restore `+ 4x^3` in the displayed expression for $P_y$ on line 46 of `PROOF.md` and ping `@audit-2` for immediate re-audit PASS.

---

## 2. What Passed (No Rework Needed)

1. **Primary-Source Fidelity (`OEIS A045743`, rev. 14, `2022-07-26T14:31:19-04:00`, offset `2,2`):**
   - Verified verbatim against live OEIS JSON (`https://oeis.org/search?q=id:A045743&fmt=json`): Name, offset `2,2`, closed-form sum `Sum_{i=0..floor((n-2)/2)} binomial(n-2+i, i)*binomial(3*n-3-i, n-2-2*i)/(n-1)`, Paul D. Hanna's (2010) algebraic equation `x*F(x)^4 = (1-F(x))*(1-3*F(x)+F(x)^2)` (matching $G = F - 1$ identically), and every coefficient of R. J. Mathar's Jul 26, 2022 5-term recurrence $C_0(n), \dots, C_4(n)$ match `TARGET.md` and `PROOF.md` verbatim.
2. **Mathematical Audit (`PROOF.md` Steps 1–3, modulo L46 above):**
   - **Step 1 (Lagrange inversion):** $\Phi(t) = (1+t)^4 / (1+t-t^2) = (1+t)^3 (1 - t^2/(1+t))^{-1} \in 1 + t\mathbb{Z}[[t]]$; formal negative-binomial expansion yields $[t^{m-1}]\Phi(t)^m = m\,a(m+1)$ for all $m \ge 1$ (since $2i \le m-1 \implies 3m - i > 0$); Lagrange inversion uniquely gives $G(x) = \sum_{m \ge 1} a(m+1) x^m$ satisfying $G(1 + G - G^2) = x(1+G)^4$; multiplying by $x^3$ for $y(x) = x G(x)$ yields $P(x, y(x)) = 0$ identically in $\mathbb{Z}[[x]]$. Airtight.
   - **Step 2 (Order-4 ODE):** Induction formula for $N_{k+1}$ checked by hand ($P_y^{2k-1} y^{(k)} = N_k(x, y(x))$ for $k = 1, 2, 3, 4$); powers of $P_y$ in $Q(x, y)$ match $P_y^7(p_{\mathrm{inhom}} + \sum_{k=0}^4 p_k y^{(k)})$; exact division $P(x, y) \mid Q(x, y)$ in $\mathbb{Z}[x, y]$ verified symbolically with zero remainder; cancellation of $P_y(x, y(x))^7 \neq 0$ in the integral domain $\mathbb{Z}[[x]]$ yields the exact ODE. Airtight (once L46 is corrected).
   - **Step 3 (Coefficient extraction for $n \ge 6$):** Checked monomial degree ranges across $p_0, \dots, p_4$ ($d - k \in [0, 4]$), $\deg p_{\mathrm{inhom}} = 5 < 6$, and edge cases $n \in \{6, 7\}$ where $n - d < 0$ matches the vanishing falling factorial $\prod_{i=0}^{k-1}(m - i) = 0$ identically; exact equality with $C_0(n), \dots, C_4(n)$ in $\mathbb{Z}[n]$ verified. Airtight.
3. **Independent Checker Re-run (`notes/check-check-2.py`):**
   - Command: `.venv/bin/python targets/oeis-A045743/notes/check-check-2.py`
   - Exit code: `0`
   - Raw output: `PASS (OEIS data n=2..22, Lagrange/P(x,y)=0, exact Z[x,y] div Q/P=R, Z[n] C_0..C_4 match, recurrence n=6..50)`
4. **Gate 2 Novelty Receipts:** `notes/novelty-gate2-watch-1.md` and `notes/novelty-gate2-watch-5.md` both **PASS** (`watch-6` pending per `#277`; check before Gate 3 handoff on re-audit).

---

## 3. Handoff

Returned to `@scout-5` and `@triage` for the 1-line fix to `PROOF.md` L46 (`+ 4x^3` in $P_y$). Ping `@audit-2` once fixed for immediate re-audit PASS.

---

## 4. Re-Audit Verdict (`@audit-2`, `2026-11-27T09:23Z`) — **PASS**

Verified `@scout-5`'s fix in `targets/oeis-A045743/PROOF.md` line 46: now correctly reads $P_y = \partial_y P = (4x^3 - x^2) + (12x^2 - 2x)y + (12x + 3)y^2 + 4y^3$. Also verified all three Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) are **PASS**.

All prior checks (live OEIS `A045743` rev. 14 fidelity, Steps 1–3 mathematical audit, and independent verifier `.venv/bin/python targets/oeis-A045743/notes/check-check-2.py` raw `PASS`) remain clear.

**Final Verdict: PASS** (label: `"written proof, internally audited"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.
