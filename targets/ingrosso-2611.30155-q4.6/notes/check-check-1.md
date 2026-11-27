# Independent Check Report: `targets/ingrosso-2611.30155-q4.6`

- **Verdict:** **PASS**
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, pure integer table / BFS arithmetic)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2611.30155/pronormali_arxiv.tex` (E. Ingrosso, M. Trombetti, and A. Zitouni, *Groups with dual classes of subgroups*, `arXiv:2611.30155v1`).
- Confirmed `TARGET.md` reproduces **Theorem 4.5** (`\label{sip}`, lines 772–774), **Question 4.6** (lines 784–786), and the definitions of pronormal subgroup (line 178), pro-norm $N_{\mathrm{pro}}(G)$ (lines 190, 225), and locally graded group (line 219) verbatim; verified compiled section-based numbering (`\numberwithin{theo}{section}`: `Theorem 3.1` `\label{pgroups}` L359, `Theorem 4.5` `\label{sip}` L772, `Question 4.6` L784).
- Confirmed mathematical soundness of `PROOF.md`:
  - **Lemma 1 ($P_G(H) = N_G(H)$ for subnormal $H \le G$):** Valid in any group (finite or infinite); note $H^y \neq H \implies J = \langle H, H^y \rangle \neq H$ holds generally because $J = H \implies u \in H \implies H^y = H^u = H$.
  - **Lemma 2 ($N_{\mathrm{pro}}(G)$ conjugation-invariant):** Clean conjugation transfer $K^{g^{-1} y} = K^{g^{-1} u} \implies K^{y^g} = K^{u^g}$ with $u^g \in \langle K, K^{y^g} \rangle$.
  - **Theorem (defect $\le 2$):** Cases 1 ($H$ pronormal $\implies H \trianglelefteq G$) and 2 ($H \subseteq N_{\mathrm{pro}}(G) \implies H^G \le N_G(H) \implies H \trianglelefteq H^G \trianglelefteq G$) hold for arbitrary groups (even without locally gradedness).
  - **Tightness ($M_{16}$):** Exact subgroup classification verifies $M_{16}$ is finite (hence locally graded), satisfies the dual condition, and $H = \langle x \rangle$ has exact subnormal defect $2$.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **$M_{16}$ (order $16$, $11$ subgroups):** Verified group axioms, exact norm/pro-norm ($|N(M_{16})| = |N_{\mathrm{pro}}(M_{16})| = 8$), verified every subgroup containing $a^4$ is normal, the only non-trivial subgroups avoiding $a^4$ are $\langle x \rangle$ and $\langle x a^4 \rangle$ (both in $N_{\mathrm{pro}}(M_{16})$ with exact defect $2$ via $H^G = \langle x, a^4 \rangle$), and verified Lemma 1, Lemma 2, and $K \trianglelefteq K^G \trianglelefteq G$.
2. **Additional paper/test groups:** Verified `D_8` ($|G|=8$, fails hypothesis), `S_3 x S_3` ($|G|=36$, $|N_{\mathrm{pro}}|=18$, `hyp=True`, `max_defect=2`), and `M_16 \ltimes C_3` ($|G|=48$, $|N_{\mathrm{pro}}|=24$, `hyp=True`, `max_defect=2`), checking Lemma 1, Lemma 2, and $K \trianglelefteq K^G \trianglelefteq G$ on all $11+10+60+36 = 117$ subgroups.

## 3. Gate 2 Novelty Status
- Passed by `watch-1` (`#1683`), `watch-6` (`#1682`), and `watch-5` (`#1684`, receipt `notes/novelty-gate2-watch-5.md` on disk).
