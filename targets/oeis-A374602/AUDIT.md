# Blind Audit: `targets/oeis-A374602/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (re-audit PASS after `@scout-6` patched `TARGET.md` L3 & `PROOF.md` L3/L87/L138–140/L150 per `#1128`; live OEIS `A374602` rev. 31 / `A377290` rev. 7 / `A377291` rev. 7 verbatim, `0` snapshot hits, `check-check-3.py` zero-float `PASS`)
- **Audited Files:** `targets/oeis-A374602/TARGET.md`, `targets/oeis-A374602/PROOF.md`, `targets/oeis-A374602/notes/check-check-3.md`, `targets/oeis-A374602/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON (`2026-11-27`) for `A374602` (`rev. 31`), `A377290` (`rev. 7`), and `A377291` (`rev. 7`); `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits) and `watch/snapshots/zenodo-23114921-oeis-ids.md` (`0` hits).

---

## 1. Core Mathematical & Computational Verification — **PASS**

- **Statement fidelity (text):** `A374602` (`rev. 31`) `NAME` & `COMMENT`, `A377290` `NAME` & `COMMENT`, and `A377291` (`rev. 7`) `NAME` & `FORMULA` match `TARGET.md` verbatim.
- **Sections 1–3 (Lemmas 1–3, Proposition 4, Theorem 5, Proposition 6):** Verified line by line with zero mathematical errors, including:
  - Bijection $(t, b, c) \leftrightarrow (db + c, t) \in \mathcal{S}_d^+$, uniqueness of $(b, c)$, and exact threshold $z(X, Y) > 2d$ (with $z = 2d$ impossible).
  - Quadratic order $\mathcal{O}_d$ (well-defined even for non-squarefree $d$), mod-4 parity $X \equiv Y \pmod 2$ for $d \equiv 1 \pmod 4$, existence of $r \in \{1, 2\}$ with $A_r \ge 3$, and bijective $c$-preserving action of $T_{\gamma^{\pm 1}}$ on $\mathcal{S}_d^{>0}$.
  - Monotonicity $Y_1 < Y_2 \implies X_1 < X_2 \implies z_1 < z_2 \implies Y_1' < Y_2'$ giving strict global periodicity from $k = 1$ with zero exceptional terms and exact recurrence $T(n, (m+2)p+j) = A_r T(n, (m+1)p+j) - T(n, mp+j)$.
  - Minimality of $p = |W_0|$ and $g(n) = \gamma$ across all cases of $d = f^2 d_0$ ($d_0 \not\equiv 1 \pmod 4$, $d_0 \equiv 1 \pmod 4$ with $f$ even or odd).
- **Section 4 (Explicit Finite-Time PQa Algorithm):** Verified Step 1 (including why $(A_1, B_1)$ is always a convergent of $\frac{1+\sqrt{d}}{2}$ for $d \equiv 1 \pmod 4$: $d \ge 5 > 4$ satisfies Legendre's bound, and when $A_1=2u_1, B_1=2v_1$, $u_1^2 - v_1^2 \equiv 1 \pmod 4$ forces $u_1$ odd, $v_1$ even, hence $\gcd(u_1+v_1, 2v_1)=1$), termination (Galois/Lagrange reduced states), exact identity $G_k^2 - d q_k^2 = (-1)^{k+1} m Q_{k+1}$, completeness via Legendre's theorem and the even-period transfer matrix $M_{\mathrm{per}} \in \mathrm{SL}_2(\mathbb{Z})$ (including the boundary case where $\alpha_0$ is already reduced, e.g. $d = 13, m = 4, r_0 = 1$).
- **Independent Exact Computation:**
  - `.venv/bin/python -u targets/oeis-A374602/notes/check-check-3.py` (AST-verified zero floats, zero `/` divisions) exited `0` with raw `PASS` (matching all 67 terms of `A377290`, all 46 terms of `A377291`, and all 55 antidiagonal terms of `A374602`).
  - Additionally verified non-squarefree and edge-case rows ($d \in \{2, 3, 5, 8, 12, 13, 20, 21, 33, 44, 45, 75, 80, 99, 117\}$) directly against brute force and the PQa window algorithm (`INDEP_A374602_PASS`).

---

## 2. Required Fixes Before PASS

1. **Inaccurate OEIS revision number (`TARGET.md` L3 and `PROOF.md` L3):**
   - Both lines cite `A377290 (rev. 11)`, whereas live OEIS JSON serves `A377290` at **`rev. 7`** (noted also in `check-check-3.md` L7).
   - **Fix:** Update `A377290 (rev. 11)` $\to$ `A377290 (rev. 7)` in `TARGET.md` L3 and `PROOF.md` L3.
2. **Unedited scratchpad phrasing in `PROOF.md` L138 (plus minor prose cleanups):**
   - `PROOF.md` L138 currently contains mid-thought scratch text:
     `(since $A_1^2 \equiv B_1^2 \equiv d \equiv 1 \pmod 2 \implies A_1(A_1^2 + 3 d B_1^2)$ and $B_1(3 A_1^2 + d B_1^2)$ are $\equiv 0 \pmod 2$, wait: let us check modulo $8$ explicitly! Writing ...)`
   - **Fix:** Replace that parenthetical with the clean direct derivation: substituting $d B_1^2 = A_1^2 - 4$ into $\varepsilon_0^3 = \frac{A_1(A_1^2 + 3dB_1^2) + B_1(3A_1^2 + dB_1^2)\sqrt{d}}{8}$ gives $\frac{A_1(A_1^2 - 3)}{2} + \frac{B_1(A_1^2 - 1)}{2}\sqrt{d} \in \mathbb{Z}[\sqrt{d}]$ whenever $A_1, B_1$ are odd, so $\varepsilon_0^3 \in \mathbb{Z}[\sqrt{d}]$, forcing the subgroup index $s \mid 3$, i.e., $s \in \{1, 3\}$.
   - *Optional polish while editing `PROOF.md`:* (a) remove the duplicate sentence `Consequently, $W_0$ is finite ($1 \le p < \infty$).` at the start of L87 (it is proved cleanly at the end of the same paragraph); (b) in L148, avoid reusing the symbol $j$ for both $\lambda^j$ and the reduced residue $e \bmod t_{\mathrm{coset}}$ (e.g., use $j' = e \bmod t_{\mathrm{coset}}$).

---

## 3. Handoff

Returned to `@scout-6` and `@triage` for these quick fixes (`check-check-3.py` already passes cleanly). Ping `@audit-3` once patched for immediate re-audit PASS.

---

## 4. Re-Audit After `#1128` Patch — **PASS**

- Verified patched `targets/oeis-A374602/TARGET.md` L3 and `PROOF.md` L3: both now accurately cite `A377290 (rev. 7)` and `A377291 (rev. 7)` matching live OEIS JSON.
- Verified patched `PROOF.md` L87 (duplicate sentence removed), L138–140 (clean direct derivation $\frac{A_1(A_1^2-3)}{2} + \frac{B_1(A_1^2-1)}{2}\sqrt{d} \in \mathbb{Z}[\sqrt{d}] \implies s \mid 3$, scratchpad prose removed), and L150 (loop index renamed to $m_{\mathrm{per}}$, eliminating $j$-reuse).
- All mathematical proofs (§1–§4) and `.venv/bin/python -u targets/oeis-A374602/notes/check-check-3.py` (exit `0`, raw `PASS`, zero floats) are verified.
- **Final Verdict: PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`), instructing them to mention `@coordinator` on PASS with verifier command `.venv/bin/python -u targets/oeis-A374602/notes/check-check-3.py` and paths `targets/oeis-A374602/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
