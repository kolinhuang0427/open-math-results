# Adversarial Audit Report: `targets/oeis-A158826/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T09:08Z` (re-audit after L62–63 fix)
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A158826` (`https://oeis.org/search?q=id:A158826&fmt=text`, rev `#54`, `2026-05-25 10:12:49`).
- `targets/oeis-A158826/TARGET.md`
- `targets/oeis-A158826/PROOF.md` (post-patch)
- `targets/oeis-A158826/notes/check-check-1.md` and `targets/oeis-A158826/notes/check-check-1.py`
- Confirmed no `targets/oeis-A158826/CONTESTED.md` exists, and Gate 2 PASS receipts from `watch-1` (`#122`), `watch-5` (`#123`), and `watch-6` (`#131`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Verification of Prior FAIL Fix (Resolved)

- **`PROOF.md` lines 61–63 (Step 3):** The negative-factorial defect at $n \in \{6, 7, 8\}$ is cleanly fixed. Line 62–63 now establishes directly for all $n \ge 6$, $0 \le d \le 4$, $0 \le r \le d + 1$ that $[x^{n-4}](x^r y^{(d)}(x)) = \bigl(\prod_{s=1}^d (n-4-r+s)\bigr) a(n - (r+4-d))$, splitting into $n - 4 - r \ge 0$ (where the factorial ratio is well-defined; note $d = 0 \implies r \le 1 \implies n - 4 - r \ge 1 \ge 0$) and $n - 4 - r < 0$ (where LHS $= 0$ and $n - 4 - r + 1 \le 0 < 1 \le n - 4 - r + d$ forces a $0$ factor in the product, so RHS $= 0$). Verified exact for all $n \ge 6$.

---

## 3. Full Independent Mathematical & Mechanical Verification (PASS)

1. **Primary-Source Fidelity (PASS):** Live OEIS `A158826` (rev 54, offset `1,2`) matches `TARGET.md` and `PROOF.md` verbatim; Mathar's Aug 30 2021 recurrence remains explicitly marked `Conjecture D-finite with recurrence ...`.
2. **Steps 1–3 Mathematical Proof (PASS):**
   - **Step 1:** $F(f(x)) = x$ ($F(t) = t(1-t)$), $P_3(y(x)) = x$ with $P_3(y) = F(F(F(y)))$, and the patched L29 nested-radical identities ($1 - 4F(t) = (1-2t)^2$, $1 - 2f(u) = \sqrt{1-4u}$, $1 - 4f(u) = -1 + 2\sqrt{1-4u}$) verified exact.
   - **Step 2:** Implicit differentiation identities for $y', y'', y''', y''''$, univariate polynomial identity $U(y) = 0$ in $\mathbb{Z}[y]$, and cancellation of the unit $P_3'(y(x))^7 = (1 - 6x + O(x^2))^7$ verified exact.
   - **Step 3:** Exact extraction of $[x^{n-4}]$ for all $n \ge 6$ (with $[x^{n-4}] c_0(x) = 0$ since $\deg c_0 = 1 < 2 \le n - 4$) yields all 6 degree-4 polynomial coefficients in $\mathbb{Z}[n]$, matching Mathar's recurrence verbatim.
3. **Independent Verifier Execution (PASS):**
   - Re-executed `.venv/bin/python targets/oeis-A158826/notes/check-check-1.py`: exit code `0`, `PASS` (verified symbolic $P_3(y)$, implicit derivatives, $U(y) = 0$ in $\mathbb{Z}[y]$, Step 3 symbolic coefficient extraction in $\mathbb{Z}[n]$, 21 OEIS prefix terms, $P_3(y(x)) \equiv x \pmod{x^{100}}$, and Mathar's recurrence for $6 \le n \le 99$).

---

## 4. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python targets/oeis-A158826/notes/check-check-1.py` and paths `targets/oeis-A158826/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
