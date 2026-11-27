# Independent Blind Audit — `targets/marberg-2611.19371-conj/`

- **Auditor:** `audit-2`
- **Verdict:** **FAIL** (1 localized gap in Lemma 5 L332/L339; Sections 1–4, primary-source fidelity, & `check-check-3.py` all **PASS** — instant PASS once patched!)
- **Audited UTC:** 2026-11-27T11:24Z
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary source: `tools/.arxiv_cache/eprint/2611.19371v1/{involution_pipe_dream_shifted_rpp_arxiv_v1.tex,preamble.tex}` (`arXiv:2611.19371v1`, Eric Marberg, Alejandro H. Morales, & Tianyi Yu, *Bumpless pipe dreams for involutions and shifted plane partitions*)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/marberg-2611.19371-conj/TARGET.md)
  - [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/marberg-2611.19371-conj/PROOF.md)
  - [check-check-3.md](file:///Users/kolinhuang/Documents/open-math/targets/marberg-2611.19371-conj/notes/check-check-3.md) and [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/marberg-2611.19371-conj/notes/check-check-3.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

## 1. Primary Source & Statement Fidelity — **PASS**

Verified every theorem/definition number directly from `preamble.tex` (L35–56, all shared `[theorem]` counter within section) and `involution_pipe_dream_shifted_rpp_arxiv_v1.tex`:
- **Definition 2.7** (L1044–1053): unique isobaric divided-difference characterization of $\widehat{\mathfrak{G}}^{(\beta)}_z$ ($\partial_i, \overline{\partial}_i$ at L1002–1007; $\mathcal{H}(z) = \{w : w \circ w^{-1} = z\}$ at L741; $\widehat{\mathfrak{G}}_z = \sum_{w \in \mathcal{H}(z)} \beta^{\ell(w) - \ell_{\mathrm{inv}}(z)} \mathfrak{G}_{w^{-1}}$ at L1062 — equivalent via $v = w^{-1}$ to `TARGET.md` L20).
- **Proposition 2.8** (`prop:partition function inv Grothendieck`, L1065).
- **Conjecture 3.8** (`\label{iG-conj}`, Section 3.3, L2885–2890; also unnumbered Intro `conjecture*`, L595–604): verbatim match in both `TARGET.md` and `PROOF.md`.
- **Proposition 3.12** (`word-pd-prop`, L3097–3139), **eq. `(cross-bump-blank-eq)`** (L3183), **Corollary 3.15** (`k-sub-cor`, L3192), **Proposition 3.19** (`sym-bij-prop`, L3754–3787), **eqs. `(double-def)`–`(double-eq)`** (L3524–3536), **Proposition 7.1** (`iG-conj-cor`, L6803–6811): all verified verbatim.

## 2. Adversarial Mathematical Audit

- **Section 1 (Change of variables & folded lattice model, L20–83):** **PASS.** Every identity (`(1)`–`(5)`), including exact transpose symmetry of $W(u,v)$, verified.
- **Section 2 (Lemma 1: unfolding bijection & Demazure propagation, L86–115):** **PASS.** Checked all adjacency agreements (off-diagonal horizontal/vertical and diagonal $(i,i-1)/(i,i)$ and $(i+1,i)/(i,i)$), south/west boundary unfolding, and diagonal-by-diagonal Demazure propagation $\phi_E(p) = p \circ \mathrm{kpi}(E)$ (independently verified exhaustively on all 7 square K-BPDs for $n=3$ across all $6$ permutations $p \in S_3$).
- **Section 3 (Lemmas 2 & 3: folded $0$-Hecke $R$-matrices, Bulk YBE, & Diagonal Reflection Equation, L118–263):** **PASS.** Independently verified **every single one** of the 20 bulk YBE occupancy patterns ($k = 0..3$, L169–200) and all 16 diagonal reflection patterns ($k = 0..4$, L216–262) symbolically in SymPy against direct matrix contraction of $R, R_V, W, K$, as well as the $0$-Hecke composition semantics (L148–154) and $k=3,4$ braid identities ($\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$, $\sigma_1(\sigma_2\sigma_1\sigma_3\sigma_2)\sigma_1 = w_0^{(4)} = \sigma_3(\sigma_2\sigma_1\sigma_3\sigma_2)\sigma_3$).
- **Section 4 (Lemma 4: 3-stage train argument & divided-difference recurrence, L268–315):** **PASS.** Checked all three stages (horizontal push across cols $1..i-1$, $2\times 2$ diagonal reflection, vertical push across rows $i+2..n$), Case 1 $u_{i+1}$ cancellation, Case 2 explicit determination of $F_1 \sqcup F_2 = \{w, y_0\}$ in Subcases 2a and 2b, and exact algebraic conversion to $\overline{\partial}_i R_{z'} = R_z$ in $\mathbb{Z}[\beta, x_1, \dots, x_n]$.
- **Section 5 (Lemma 5: Uniqueness of $\mathsf{InvBPD}_K(w_0^{(n)})$, L321–342) — 1 LOCALIZED BLOCKING GAP:**
  - **Defect (L332 & L339):** The 4th bullet of the downward induction on column $k = n, \dots, 1$ (L332) only states that *"every cell $(r, k)$ with $r < n+1-k$ has no vertical segment entering from south or exiting north (hence is $\mathsf{B}$ or $\mathsf{H}$)"*, and the inductive step (L339) argues: *"Because $(n+1-k, k) = \mathsf{C}$ has neither a north nor a west connection, no vertical pipe exists in column $k$ above row $n+1-k$."*
  - **Why this is a non-sequitur:** Knowing $(n+1-k, k) = \mathsf{C}$ has no north connection only shows no vertical pipe enters $(n-k, k)$ **from the south**; it does **not** rule out a pipe entering some cell $(r, k)$ ($r < n+1-k$) from the **west**, turning north at a $\mathsf{J}$ (upturn) tile at $(r, k)$, and later turning east at a $\mathsf{C}$ tile at $(r', k)$ ($r' < r$). (For instance, in $n = 4, k = 2$, $(3, 2) = \mathsf{C}$ does not by itself forbid $(2, 2) = \mathsf{J}$ and $(1, 2) = \mathsf{C}$ without invoking the cells to the east of column $k$.)
  - **Exact fix:** Strengthen the 4th bullet of the inductive hypothesis (L332) to *"every cell $(r, k)$ with $r < n+1-k$ is $\mathsf{B}$ (blank)"*. Then in the inductive step (L339), for every $r < n+1-k$, cell $(r, k+1)$ lies on or above the antidiagonal $r + (k+1) \le n+1$, so by the inductive hypothesis for column $k+1$ it is either $\mathsf{C}$ (if $r + k + 1 = n+1$) or $\mathsf{B}$ (if $r + k + 1 \le n$); in either case $(r, k+1)$ has **no west connection**, so $(r, k)$ has **no east connection**. Going top-down for $r = 1, 2, \dots, n-k$, cell $(r, k)$ also has **no north connection** (empty north boundary at $r = 1$, and $(r-1, k) = \mathsf{B}$ by top-down induction for $r > 1$). Among the six bumpless pipe dream tiles $\{\mathsf{B}, \mathsf{H}, \mathsf{V}, \mathsf{J}, \mathsf{C}, \mathsf{P}\}$, the unique tile with neither an east nor a north connection is $\mathsf{B}$; hence every $(r, k)$ with $r < n+1-k$ is $\mathsf{B}$. (Note: this also immediately makes L341's conclusion on $r+c \le n$ already established.)
- **Main Theorem (L345–353) & Remark (L357):** **PASS** (verified $\ell_{\mathrm{inv}}(w_0^{(n)}) = \lfloor n^2/4 \rfloor$ for all $n \ge 1$).

## 3. Independent Mechanical Verification & Gate 2 Novelty

- AST check of `targets/marberg-2611.19371-conj/notes/check-check-3.py`: **`FLOAT_CONSTANTS: 0 []`**.
- Executed `.venv/bin/python -u targets/marberg-2611.19371-conj/notes/check-check-3.py`: exit code `0`, `PASS`.
- Gate 2 novelty receipts (`watch-1`, `watch-5`, `watch-6`): all **PASS**.

## 4. Required Fix

Patch **Lemma 5 (L332 & L339)** in `targets/marberg-2611.19371-conj/PROOF.md` as described in §2 above, then ping `@audit-2` for an instant re-audit PASS!

---

## 5. Re-Audit Verdict (`audit-2`, `2026-11-27T11:28Z`) — **PASS**

Verified `@attack-2`'s patch to Lemma 5 (`#1151`, `targets/marberg-2611.19371-conj/PROOF.md` L332, L339, L341):
- Strengthened IH bullet 4 (L332) to `every cell (r, k) with r < n + 1 - k is B (blank)`.
- Inductive step (L339) cleanly establishes $(r, k) = \mathsf{B}$ for all $1 \le r \le n - k$ by top-down induction using $(r, k+1) \in \{\mathsf{C}, \mathsf{B}\}$ (no west edge $\implies$ no east edge at $(r, k)$) and empty north edge (grid boundary for $r=1$, $(r-1, k) = \mathsf{B}$ for $r > 1$), noting that every BPD tile except $\mathsf{B}$ has a north or east connection.
- Concluding cell classification (L341) directly follows from bullets 1, 3, and 4.

**Final Audit Verdict:** **PASS.** Handing off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check.
