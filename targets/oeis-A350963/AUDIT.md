# Adversarial Audit Report: `targets/oeis-A350963/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T08:50Z` (re-audit after L111/L165/L166 fix)
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A350963` (`https://oeis.org/search?q=id:A350963&fmt=text`, revision `#54`, `2025-11-05 15:22:48`) and Rémy Sigrist's OEIS-linked PARI/GP file `https://oeis.org/A350963/a350963.gp.txt`.
- `targets/oeis-A350963/TARGET.md`
- `targets/oeis-A350963/PROOF.md`
- Prior `targets/oeis-A350963/AUDIT.md`
- `targets/oeis-A350963/notes/check-check-1.md` and `targets/oeis-A350963/notes/check-check-1.py`
- Confirmed no `targets/oeis-A350963/CONTESTED.md` exists.

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Verification of Prior FAIL Fixes (All Resolved)

All three boundary-inequality defects at `k = 0` flagged in the previous audit are now corrected and verified exact for all $k \ge 0$:
1. **`PROOF.md` L111 (Prop. 2.1, Ray $R_2$, $v=(1,-k,2)$, $k \ge 0$):** Now states $F_5 = \lfloor(3 - 4k)/3\rfloor \le 1 < 2k + 2$, $F_7 = 1 < 2k + 2$, and $F_2, F_3, F_8 \le 0$. Exact for all $k \ge 0$ (including $k=0$ where $F_5 = 1 < 2$).
2. **`PROOF.md` L165 (Prop. 2.3 Case A, Ray $R_1$, $u=(1,-k,3)$, $k \ge 0$):** Now states $F_5(u) = \lfloor(4 - 4k)/3\rfloor \le 1 \le 2k + 1$, $F_7(u) = 1 \le 2k + 1$, and $F_2, F_3, F_8 \le 0$. Exact for all $k \ge 0$.
3. **`PROOF.md` L166 (Prop. 2.3 Case A, Ray $R_2$, $u=(2,-k,3)$, $k \ge 0$):** Now states $F_5(u) = \lfloor(6 - 4k)/3\rfloor \le 2 \le 2k + 2$, $F_7(u) = 2 \le 2k + 2$, and $F_2, F_3, F_8 \le 0$. Exact for all $k \ge 0$.

---

## 3. Full Independent Mathematical & Mechanical Verification

1. **Primary-Source Fidelity (PASS):**
   - Live OEIS `A350963` (rev 54, `2025-11-05`) matches `TARGET.md` and `PROOF.md` verbatim: conjectured g.f. `-(2*t^7-6*t^6-24*t^5-33*t^4-33*t^3-28*t^2-9*t-1)/((1-t^2)*(1-t^4))` remains explicitly marked `Conjectured g.f.`; unit-square edge adjacency matches OEIS *"share a (long or short) edge"* and `a350963.gp.txt` (`DX = 4 - I`, `DY = 6*I`, `T[1..6]`, `neighbourhood`, root `T[4]` = `(0,0,3)`).
   - Verified Section 1.1–1.2 exact mod-$\Lambda$ partition of all 24 classes, exact 50-edge adjacency table `C[0..5]`, R/G/B degree breakdowns, and exact on-the-nose half-turn automorphism $\iota(u,v) = (3-u, 5-v)$ exchanging $T_0 \leftrightarrow T_3$, $T_1 \leftrightarrow T_2$, $T_4 \leftrightarrow T_5$, proving independence of choice of type-R root.
2. **Section 2 — Global Distance Formula $d(v) = D^*(v)$ (PASS):**
   - **Prop. 2.1:** Verified $D^*(0,0,3)=0$, exact $1$-Lipschitz property of $F_1,\dots,F_8$ across all 50 directed edges and residues $r = (x+2y)\bmod 3$, and $D(u) \ge D(v)$ for all non-$E_{\mathrm{exc}}$ neighbors of all three rays $R_1, R_2, R_3$ algebraically for all $k$.
   - **Lemma 2.2:** Verified $-3 \le 3F_s - M_s \le 6$ and all 20 non-adjacent pair identities yielding $M^* \le 60 \implies v \in B_{\mathrm{core}} = [-20,20] \times [-10,10] \times \{0..5\}$.
   - **Prop. 2.3:** Verified $D^*(v) \ge 21$ outside $B_{\mathrm{core}}$, Case A explicit descent on $R_1, R_2, R_3$, and **symbolically verified every cell of the Case B descent table** across all $8\text{ seams} \times 6\text{ tiles} \times 3\text{ residues } r \in \{0,1,2\}$ plus all split cases and footnote fallbacks. Independently checked all 3 omitted equalities (each excluded by $E_{\mathrm{exc}}$ or integer parity) and all 4 starred $o=2$ exclusions of $E_{\mathrm{exc}}$ (including $\lfloor(-4y+6)/3\rfloor \le -2y-5$ for $y \le -11$).
3. **Section 3 — Octagonal Enumeration & Generating Function (PASS):**
   - Independently verified the rectangle-minus-four-corners decomposition, arithmetic progression identities, all 6 breakpoint-ordering and 18 endpoint-nonnegativity affine inequalities for all $m \ge 1$, all 24 polynomials $|B_t(4m+r)|$, and the 4 totals $B(4m+r)$ **symbolically in SymPy** for all $m \ge 1$.
   - Verified pairwise disjointness of $R_1, R_2, R_3$, $\Delta_{\mathrm{exc}}(n) = -1$ (even $n \ge 2$) / $+1$ (odd $n \ge 3$), shell counts $a(n)$ for all $n \ge 0$, and multiplication by $(1-t^2)(1-t^4)$ reproducing Sloane's conjectured generating function verbatim.
4. **Independent Verifier Execution (PASS):**
   - Ran `.venv/bin/python -u targets/oeis-A350963/notes/check-check-1.py`: exit code `0`, `PASS` in `0.81s` (confirms $B_{\mathrm{core}}$ 5,166 vertices, collar descent, BFS through radius 55 matching $D^*$ and all 54 OEIS terms, and GF expansion to $t^{100}$).

---

## 4. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python -u targets/oeis-A350963/notes/check-check-1.py` and paths `targets/oeis-A350963/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
