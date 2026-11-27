# Adversarial Audit Report (`audit-1`): `targets/schwob-2606.12129-conj8.7/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Ludovic Schwob, `arXiv:2606.12129v1` (*Middle orders: all distributive lattices between weak and Bruhat*), Section 8, **Conjecture 8.7** (`\label{cnj:Dtype}`, `Middle_order.tex` L910–913)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2606.12129/Middle_order.tex` (`2606.12129v1`, latest on arXiv API)
- **Verdict:** **PASS** *(Re-audit after `#1005` & `#1050` patches; all localized slips in Lemmas 6 & 7 are completely resolved and verified.)*

---

## 1. Primary-Source & Citation Audit — PASS
- Verified verbatim against `tools/.arxiv_cache/eprint/2606.12129/Middle_order.tex` (`2606.12129v1`, sole version on arXiv):
  - **Conjecture 8.7** (`\label{cnj:Dtype}`, L910–913) matches `TARGET.md` and `PROOF.md` verbatim.
  - All cited numbers match compiled LaTeX counters (shared `\newtheorem{thm}[section]` across `thm, lem, prop, nota, cor, defi, cnj, exmp, rmk`): **Proposition 3.8** (`pr:covers`, L291–299), **Proposition 4.1** (`pr:rhombus`, L316–322), **Theorem 4.13** (L491–497), **Definition 7.1** (L731–734), and Section 8 L838 ($\omega$-sorting order containment).
  - Independent exact-arithmetic verifier `.venv/bin/python -u targets/schwob-2606.12129-conj8.7/notes/check-check-2.py` exited `0` (`PASS`, zero floats, zero `/` divisions).
  - Gate 2 novelty receipts clear (`watch-1`, `watch-5`, `watch-6`).

---

## 2. Required Localized Fixes in `PROOF.md`

### Issue 1 (Wrong Formula — `PROOF.md` L155, Lemma 6 Step 7)
For the dual lower-cover rhombus at step $s_3$ below $v_5 = (3, -2, n, -1, \vec{d})$ (whose two lower covers are $u_4 = v_5 t_{1,4}^+ = (-1, -2, n, 3, \vec{d})$ and $v_5 s_3 = v_5 t_{3,4}^+ = (3, -2, -1, n, \vec{d})$), L155 states:
> *"the second candidate $((-1, -2, n, 3, \vec{d}) \cdot t_{3,4}^+) \cdot t_{1,4}^+ = (n, -2, 3, -1, \vec{d})$ has length greater than $\ell(u_4 s_3)$ (since $-1 < n$)"*

That expression computes $u_4 t_{3,4}^+ t_{1,4}^+ = v_5 t_{1,4}^+ t_{3,4}^+ t_{1,4}^+$ (which is not even a reflection neighbor of $v_5 s_3$) rather than the Lemma 1(2) second candidate $v_5 t_{3,4}^+ t_{1,4}^+ = (v_5 s_3) t_{1,4}^+$.

**Fix:** Replace with the true Lemma 1(2) second candidate:
$$(v_5 s_3) \cdot t_{1,4}^+ = (3, -2, -1, n, \vec{d}) \cdot t_{1,4}^+ = (n, -2, -1, 3, \vec{d}),$$
whose length strictly exceeds $\ell(v_5 s_3)$ (since $(v_5 s_3)(1) = 3 < n = (v_5 s_3)(4)$), so it is not a lower cover of $v_5 s_3$.

### Issue 2 (False Arithmetic — `PROOF.md` L179, Lemma 7 Claim 1)
When bounding $\ell(x t_{1,3}^+ t_{1,3}^-) - \ell(e_1)$ for $e_1 = (n, -m, -1, 2, \vec{r})$ and $w := e_1 t_{1,3}^- = (1, -m, -n, 2, \vec{r})$, L179 writes:
> *"net $+2$ from $-m$ plus $+2$ from $2$ since $2 - n < 0$"*

Position $4$ (value $2$, lying to the right of $\{1, 3\}$) actually contributes **$0$**, not $+2$: in $e_1$, pairs $(n, 2)$ and $(-1, 2)$ contribute $1 + 0 = 1$, and in $w$, pairs $(1, 2)$ and $(-n, 2)$ contribute $0 + 1 = 1$. The exact length change is $+1$ from $(1, 3)$ plus $+2$ from $-m$, giving $\ell(w) = \ell(e_1) + 3 = \ell(x) + 4 > \ell(x) + 2$ (adding an extra $+2$ would falsely give $\ell(x) + 6$).

**Fix:** Delete *"plus $+2$ from $2$ since $2 - n < 0$"* and state simply that $\ell(w) = \ell(e_1) + 3 = \ell(x) + 4 > \ell(x) + 2$ ($+1$ from $(1, 3)$ and $+2$ from $-m$, with all positions $> 3$ unchanged).

### Optional Minor Clarity Note (`PROOF.md` L152, Lemma 6 Step 5)
Add *"and $(u_3, v_4)$ is weak"* right before *"hence $(u_4, v_4) \notin E(\mathbf{L})$"* so the uniqueness-of-join exclusion is immediately explicit.

---

## 3. Verified Sound Sections (Everything Else — Airtight)
- **Section 2 (Conventions & Lemma 1):** Signed-permutation realization, exact $D_n$ length formula, and all cases of Lemma 1 (including $D_3$ Type II order-4 check) verified completely.
- **Section 3 (Lemma 2, Theorem 3, Corollaries 4–5):** Parabolic restriction, dual $\mathbf{L}^*$, Birkhoff splitting equivalence $(1)\Leftrightarrow(2)\Leftrightarrow(3)$ via fiber-size length summation, join-irreducible reduction for minuscule quotients, and uniqueness of splitting roots via highest root $\theta$ verified completely airtight.
- **Section 4 (Overlap Trichotomy):** Exhaustive compatibility reduction across $J_0 \cap J_1$, $J_0 \cap J_{n-1}$, $J_1 \cap J_{n-1}$ ($\cong A_{n-2}$) to `(B1)`, `(B2)`, `(G2)`, `(G1)` up to $\tau$ verified completely.
- **Section 5 (Lemmas 6 & 7, modulo Issues 1–2):** All witnesses, Prop 3.8 applications, rhombus steps, and $W_{J_{n-1}}$ parabolic-component contradictions verified across $n = 4$ and all $n \ge 5$.
- **Section 6 (Lemma 8, Case (G2)):** Explicit ${}^{J_{n-1}} D_n$ structure, $k = 3$ chain, and $4 \le k \le n$ induction $(u_j, a_j)$ verified completely.
- **Section 7 (Lemmas 9 & 10, Case (G1)):** Explicit ${}^{J_0} D_n$ & $\mathcal{J}({}^{J_0} D_n)$ characterization, all 8 subcases of Lemma 9, Part 1 ($y_A$ & $y_B$ chains for $2 \le a \le n - 2$), and Part 2 (Subcases 2a odd $n \ge 5$ and 2b even $n \ge 4$) verified completely.
- **Section 8 (Main Theorem):** Clean induction from $D_3 \cong A_3$ (Theorem 4.13) to all $D_n$ ($n \ge 4$).

---

## 4. Re-Audit of `#1005` Patch — FAIL (1 Remaining Reversed Sign on L179)

Checked `git diff` on `PROOF.md`:
- **Issue 1 (L155)** and **L152 clarity note**: **RESOLVED** cleanly.
- **Issue 2 (L179)**: The arithmetic (`+1` from `(1,3)`, `+2` from `-m`, `0` from positions `k >= 4`, giving `\ell(w) = \ell(e_1) + 3 = \ell(x) + 4`) is now fixed, **EXCEPT** the parenthetical on L179 still retains the false inequality `before: $n > -m > -1$`! Since $m = n - 1 \ge 3$, we have $-m \le -3 < -1$ (if $n > -m > -1$ were true, pairs $(1,2)$ and $(2,3)$ would give $2$ inversions and total $2 + 1 = 3$, contradicting `contributing $1 + 1 = 2$` on the very same line).

**Remaining 1-line fix (`PROOF.md` L179):** Change `before: $n > -m > -1$` to `before: $n > -m$ and $-m < -1$` (or `before: $n > -1 > -m$`). Everything else is 100% PASS; once fixed, ping `@audit-1` for immediate PASS.

---

## 5. Final Re-Audit (`#1050`) — PASS

Verified `git diff` and `PROOF.md` L179 verbatim: `before: $n > -m$, $-m < -1$, $n - m = 1 > 0$, $-m - 1 < 0$, contributing $1 + 1 = 2$`, with `after: $1 > -m > -n$, $1 - m < 0$, $-m - n < 0$, contributing $2 + 2 = 4$`, and all positions $k \ge 4$ contributing $0$, giving exact $\ell(w) = \ell(e_1) + 3 = \ell(x) + 4 > \ell(x) + 2$. No other lines were altered, and `.venv/bin/python -u targets/schwob-2606.12129-conj8.7/notes/check-check-2.py` already passed (exit `0`, `PASS`, untouched since initial audit).

**Final Verdict:** **PASS**. Ready for Gate 3 novelty verification.
