# Adversarial Audit Report (`audit-1`): `targets/maric-2603.08876-conj1/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Nevena Marić, `arXiv:2603.08876v1` (*Hierarchical threshold structure in Max-Cut with geometric edge weights*, 2026-03-09), Section 5 (`\label{sec:global}`), **Conjecture 5.1** (`\label{conj:global}` [Global Optimality])
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and primary source `tools/.arxiv_cache/eprint/2603.08876v1/LexiCut-arXiv.tex` (`2603.08876v1`, sole version on arXiv)
- **Verdict:** **PASS** *(Re-Audit #1 — all 4 blocking issues from initial FAIL in §§2–3 have been cleanly patched and independently re-verified; label: `written proof, internally audited`)*

---

## 1. Primary-Source & Citation Verification — PASS (for `TARGET.md` and `PROOF.md`)

- Verified verbatim against `tools/.arxiv_cache/eprint/2603.08876v1/LexiCut-arXiv.tex` (`2603.08876v1`, confirmed sole version on `abs/2603.08876.html`):
  - **Conjecture 5.1** (`\label{conj:global}`, L698–700): *"For $n \geq 7$ and $r \in (r_k(n), r_{k-1}(n))$, the $k$-isolated cut $C_k$ achieves the maximum weight among all $2^{n-1}$ cuts."* — matches `TARGET.md` and `PROOF.md` verbatim.
  - All compiled LaTeX counters match `PROOF.md` exactly: Section 2 eq. (1) (`\label{eq:edge_index}`, L153), Section 4 **Theorems 4.7** (`\label{thm:unique_roots}`, L499), **4.9** (`\label{thm:monotonicity}`, L578), and **4.10** (`\label{thm:isolated_optimality}`, L610), and Section 5 (`\label{sec:global}`, L692).
  - Gate 2 novelty receipts clear (`watch-6` `#701`, `watch-1` `#707`; `citing_papers.md` shows `OpenAlex cited_by=0; S2=0`).

---

## 2. Required Fixes in `PROOF.md` (`@attack-6`)

### Issue 1 (Blocking Algebra Bug — `PROOF.md` L134–135, Lemma 3.3 Subcase $a \ge 2, b = a + 1$)
L134 claims:
$$\frac{\Delta_{\mathrm{comb}}}{A_{a+1} A_{a+2} B_{a+1}} = (x - x^d)\left(\frac{S_A}{A_{a+1}} - 1\right) + (x - 1) = x\left[(1 - x^{d-1})\frac{S_A}{A_{a+1}} - (1 - x^d)\right].$$
This equality is **false**: expanding the LHS gives $(x - x^d)\frac{S_A}{A_{a+1}} - (1 - x^d)$, whereas expanding the RHS gives $(x - x^d)\frac{S_A}{A_{a+1}} - x(1 - x^d)$, which differs by $-(1 - x)(1 - x^d) \ne 0$ (e.g., at $x = 1/2, d = 3, S_A/A_{a+1} = 2$, LHS $= -1/8 < 0$ while RHS $= +5/16 > 0$). Moreover, using the true LHS, the weak lower bound $\frac{S_A}{A_{a+1}} > 2$ on L135 is insufficient (it yields $2x - 1 - x^d < 0$ for $x < 1/2$).

**Fix:** Replace L134–135 with the exact identity
$$\frac{\Delta_{\mathrm{comb}}}{A_{a+1} A_{a+2} B_{a+1}} = (x - x^d)\frac{S_A}{A_{a+1}} - (1 - x^d) = (1 - x^{d-1})\left(x\frac{S_A}{A_{a+1}}\right) - (1 - x^d),$$
and observe that since $a \ge 2$ and $M = d + 1 \ge 4$,
$$x\frac{S_A}{A_{a+1}} \ge x\left(\frac{A_a + A_{a-1}}{A_{a+1}}\right) = x^{-(M-1)} + x^{-2M} > 2,$$
whence $\frac{\Delta_{\mathrm{comb}}}{A_{a+1}A_{a+2}B_{a+1}} > 2(1 - x^{d-1}) - (1 - x^d) = 1 - 2x^{d-1} + x^d > 0$ on $(0, 1)$ for all $d \ge 3$.

### Minor Clarity Notes (optional while editing `PROOF.md`)
- **L299 (Theorem 5.3 B2(a), $L \ge 11$):** Clarify that the positive-term integral $\int_{2/L}^{u_*}$ is taken to be $0$ whenever $u_* \le 2/L$ (or use lower limit $2/11$ clipped at $0$, since $u_*$ can drop below $2/11$ near $v = 50/61$).
- **L149 (Theorem 4.1(1)):** Note `strictly increasing for $(L, d) \ne (2, 1)$` (which holds for all interior $n \ge 7$ triples).

---

## 3. Required Fixes in `notes/check-check-3.py` and `notes/check-check-3.md` (`@check-3`)

### Checker Bug A (Blocking Over-Pruning in Stage 6 — `notes/check-check-3.py` L1219, L1227, L1266, L1268; also L1011, L1087)
Multiplying $1 + x^{M-1} < u^{-1} \le 1 + x^{M-1} + x^{2M-3}$ by $u = x^M$ gives
$$x^M + x^{2M-1} < 1 \le x^M + x^{2M-1} + x^{3M-3}.$$
`check-check-3.py` mistakenly uses `x**(M - 1)` instead of `x**M` on L1219, L1227, L1266, L1268 (and L1011, L1087). Because $x^{M-1} > x^M$, L1227 and L1266 **over-pruned and skipped** the genuinely feasible strip $x^M + x^{2M-1} < 1 \le x^{M-1} + x^{2M-1}$ in Theorem 5.4 ($r^* = 2, 6 \le M \le 34$).
- **Fix:** Replace `**(M - 1)` with `**M` on L1011, L1087, L1219, L1227, L1266, L1268. *(Auditor independently verified all 493 pairs PASS with the true `x**M` condition in 618 leaves.)*

### Checker Bug B (Blocking Skipped Pair `(4, 1)` in Stage 4 Step 3 — `notes/check-check-3.py` L691)
L691 skips `(L, d) != (4, 1)` instead of `(L, d) != (4, 2)`: `(4, 1)` ($M = 5$) is a **feasible** active pair for $n \ge 8, a \ge 2$ ($x \in [0.9415, 0.9515]$), whereas `(4, 2)` is the pair excluded by $1 + x^5 + x^9 + x^{12} < u^{-1} + u^{-2}$ (`PROOF.md` L278).
- **Fix:** Change L691 from `if (L, d) != (4, 1):` to `if (L, d) != (4, 2):` and add the explicit `(4, 2)` infeasibility assertion. *(Auditor independently verified `(4, 1)` PASS via exact Sturm chain on $[0.94, 0.96]$ and `(4, 2)` infeasible with margin $> 0.193$.)*

### Checker Bug C (Invalid Monotonicity Bound in Stage 4 Step 2 `M >= 30` — `notes/check-check-3.py` L611)
L611 evaluates `(iv.mpf(1) + u_iv - (r_iv - iv.mpf(1)) * G4_iv)` at $M = 30$. As $M \to \infty$ with $u$ fixed, $(r - 1)G_5 = 1 - u^{4/M} \to 0$, so the $M = 30$ value is a **lower** bound rather than an upper bound on the subtracted factor $1 + u - (r-1)G_5$.
- **Fix:** Replace `(iv.mpf(1) + u_iv - (r_iv - iv.mpf(1)) * G4_iv)` on L611 with the valid universal upper bound `(iv.mpf(1) + u_iv)`. *(Auditor independently verified this PASSES in 1 box.)*

### Checker Report Issue D (`notes/check-check-3.md` L5–17)
`notes/check-check-3.md` contains garbled text describing a wrong label (`\label{c2}`), tournament weights `2^{-(N-i)}`, canonical cut `A = {1, ..., n-1}`, `f(A) >= 1`, `b_0 <= 12`, and `phi_{12}(u)` on `[3/4, 1]`. Please rewrite `notes/check-check-3.md` to accurately reflect `LexiCut-arXiv.tex` (`\label{conj:global}`) and the repaired `check-check-3.py`.

---

## 4. Verified Sound Sections (Everything Else — Airtight)
- **Sections 1–2:** Reduction to non-isolated cuts, rank-1 factorization $w(i, j) = A_i B_j$, Lemma 2.1, Lemma 2.2 ($\alpha_L > \alpha_U$, unique $r^* \in \{1, \dots, L-1\}$, $\mathrm{hi}_p > 0$).
- **Section 3 (except L134–135):** Lemma 3.1, Lemma 3.2 ($L \le 3$, $L = 4$, $L \ge 5$), Lemma 3.3 ($a = 1, b = 2$).
- **Section 4:** Theorem 4.1 (all cases 1–6) and Theorem 4.2 ($n = 7$, exact Sturm chains + 3-vertex flip $F = \{1, 3, 4\}$).
- **Section 5:** Proposition 5.0 (all parts 1–5, Hermite–Hadamard midpoint bound, $S_{\mathrm{err}}$ integral bound, $G(x)$ bound), Theorem 5.1 (L215 polynomial identity independently verified exact; all cases 1–5), Lemma 5.2, Theorem 5.2 (Steps 1–3), Theorem 5.3 (Parts B2(a) including exact $Mt$/$(M-1)t$ identities & positive/negative integral bounds, and B2(b)), Theorem 5.4 (all cases 1–4), and Section 6 Main Theorem case coverage.


---

## 5. Re-Audit #1 (`@audit-1`, `2026-11-27`) — PASS

Re-audited after `@attack-6`'s `#1211` patches to `PROOF.md` and `@check-3`'s `#1233` patches to `notes/check-check-3.py` and `notes/check-check-3.md`:

1. **`PROOF.md` (Issue 1 + minor notes):**
   - Verified L134–135 verbatim:
     $$\frac{\Delta_{\mathrm{comb}}}{A_{a+1}A_{a+2}B_{a+1}} = (x - x^d)\left(\frac{S_A}{A_{a+1}} - 1\right) + (x - 1) = (x - x^d)\frac{S_A}{A_{a+1}} - (1 - x^d) = (1 - x^{d-1})\left(x\frac{S_A}{A_{a+1}}\right) - (1 - x^d),$$
     with $x \frac{S_A}{A_{a+1}} \ge x\bigl(\frac{A_a + A_{a-1}}{A_{a+1}}\bigr) = x(x^{-M} + x^{-(2M+1)}) = x^{-(M-1)} + x^{-2M} > 2$ ($a \ge 2$, $M = d + 1 \ge 4$) and $f(x) = 1 - 2x^{d-1} + x^d$ satisfying $f(1) = 0$, $f'(x) = x^{d-2}(dx - 2d + 2) < 0$ on $(0, 1)$ for all $d \ge 3$. Airtight.
   - Verified minor clarity notes incorporated cleanly on L149 ($(L, d) \ne (2, 1)$) and L299 ($\int_{\min(2/L, u_*)}^{u_*}$ taken as $0$ whenever $u_* \le 2/L$).
2. **`notes/check-check-3.py` (Checker Bugs A, B, C):**
   - Verified Bug A fixed: exact `x**M + x**(2*M-1)` condition on L1020, L1096, L1228, L1236, L1275, L1277 (rigorous outward bisection brackets `x_lo_M` and `x_hi_M` checked).
   - Verified Bug B fixed: L692 changed to `if (L, d) != (4, 2):` (`assert len(pairs) == 27`, keeping active `(4, 1)`), and L699–705 explicitly certifies `(4, 2)` infeasibility ($x^{12}(1 + x^5 + x^9 + x^{12}) - x^6 - 1 < 0$) across the full `[x42_lo, x42_hi]` bracket.
   - Verified Bug C fixed: L611 uses the valid universal upper bound `(iv.mpf(1) + u_iv)` on the subtracted factor for $M \ge 30$ (and verified `E6_lb` valid via Lemma 5.2 $\partial E / \partial S_0 < 0$ at $S_0 = 1 + S(x) \le F_M(u)$).
   - Independent AST check confirms `FLOATS: []` (zero floating-point literals or `float` calls).
   - Independent full execution: `.venv/bin/python -u targets/maric-2603.08876-conj1/notes/check-check-3.py` -> exit code `0`, raw output `PASS` across all `[1/6]`–`[6/6]` stages.
3. **`notes/check-check-3.md` (Issue D):**
   - Rewritten cleanly; accurately documents `LexiCut-arXiv.tex` (`\label{conj:global}`), `PROOF.md`, and the repaired `check-check-3.py` run.

**Final Verdict:** **PASS.** Ready for Gate 3 freshness verification (`<1h`) by `@watch-1`, `@watch-5`, `@watch-6` prior to `@coordinator` final check.
