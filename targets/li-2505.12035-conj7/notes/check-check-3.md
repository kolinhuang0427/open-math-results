# Independent Check Report: targets/li-2505.12035-conj7/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2505.12035v1` (`2025-05-17T14:55:02Z`, sole version), *"An Ore-type theorem for $[3]$-graphs"* by Yupei Li, Linyuan Lu, Ruth Luo, cached TeX source `tools/.arxiv_cache/eprint/2505.12035/main_arxiv.tex`.
- **Exact theorem/conjecture numbering & statement:**
  - Section 1 (`\section{Introduction}`), lines 155–156, `\begin{conjecture}\label{conj:ore}` (Conjecture 7 under the shared `theorem` counter: Theorems 1–5, Construction 6 `\label{const1}`, Conjecture 7 `\label{conj:ore}`):
    > Let $n\geq 6$, and let $\mathcal{H}$ be a $[3]$-graph on $n$ vertices such that every pair $u,v \in V(\mathcal{H})$ of non-adjacent vertices satisfies $d_{\partial \mathcal{H}}(u) + d_{\partial \mathcal{H}}(v) \geq n+1$. Then $\mathcal{H}$ contains a Hamiltonian Berge cycle.
  - Definitions checked in `main_arxiv.tex` (lines 94–113, 152–153):
    - Hypergraph $\mathcal{H}$ is a family of subsets of $V(\mathcal{H})$; $[3]$-graph means edge sizes in $[3] = \{1,2,3\}$ (lines 94–95, 153).
    - Co-degree $d_{\mathcal{H}}(u,v)$ = number of edges containing $\{u,v\}$; $u,v$ are adjacent iff $d_{\mathcal{H}}(u,v)\ge 1$, else non-adjacent (lines 101–102).
    - $2$-shadow $\partial \mathcal{H}$ is the simple $2$-uniform graph on $V(\mathcal{H})$ with $uv \in E(\partial \mathcal{H}) \iff d_{\mathcal{H}}(u,v) \ge 1$ (line 103); $d_{\partial \mathcal{H}}(u) = |N_{\mathcal{H}}(u)|$ (line 152).
    - Hamiltonian Berge cycle: $n$ distinct vertices $v_1,\dots,v_n \in V(\mathcal{H})$ and $n$ distinct edges $e_1,\dots,e_n \in E(\mathcal{H})$ with $\{v_i,v_{i+1}\} \subseteq e_i$ ($v_{n+1}\equiv v_1$) (lines 110–113).
  - Note: No extra hypothesis (`|E| \ge n`, covering, connectedness, or minimum shadow degree) appears in Conjecture 7 (lines 166–178 only require $n \ge 6$ and $n \ge d_0 + 4$ for Theorem 8).
- **Fidelity:** `TARGET.md` and `COUNTEREXAMPLE.md` match `arXiv:2505.12035v1` verbatim with zero quantifier, hypothesis, or definition drift.

## 2. Independent Mechanical Check

- Independently wrote `targets/li-2505.12035-conj7/notes/check-check-3.py` (strictly without reading `verify.py`) implementing the definitions directly from `main_arxiv.tex` and verifying both explicit witnesses in `COUNTEREXAMPLE.md`:
  - **Witness 1 ($n=6$):** $V=\{0,1,2,3,4,5\}$, $E=\{\{0,1,2\},\{0,1,3\},\{0,2,4\},\{1,2,5\},\{3,4,5\}\}$. Exact checks confirm simple $3$-uniform hypergraph ($[3]$-graph), $|E|=5 < 6$, $2$-shadow is $4$-regular ($K_{2,2,2}$, complement $\{\{0,5\},\{1,4\},\{2,3\}\}$), non-adjacent degree sums are all $8 \ge n+1 = 7$, and exhaustive backtracking confirms zero Hamiltonian Berge cycles.
  - **Witness 2 ($n=7$, linear):** $V=\{0,1,2,3,4,5,6\}$, $E=\{\{0,3,4\},\{0,5,6\},\{1,3,5\},\{1,4,6\},\{2,3,6\},\{2,4,5\}\}$. Exact checks confirm simple linear $3$-uniform hypergraph ($[3]$-graph), $|E|=6 < 7$, $2$-shadow degrees $[4,4,4,6,6,6,6]$, non-adjacent pairs $(0,1),(0,2),(1,2)$ all have degree sum $8 \ge n+1 = 8$, and exhaustive backtracking confirms zero Hamiltonian Berge cycles.

- **Command run:**
```bash
.venv/bin/python targets/li-2505.12035-conj7/notes/check-check-3.py
```

- **Raw output:**
```text
Witness 1 PASS: n=6, |E|=5 < 6, shadow_degs=[4, 4, 4, 4, 4, 4], non_adj=[(0, 5), (1, 4), (2, 3)], min_non_adj_sum=8 >= 7, hamiltonian_berge_cycle=False
Witness 2 PASS: n=7, |E|=6 < 7, shadow_degs=[4, 4, 4, 6, 6, 6, 6], non_adj=[(0, 1), (0, 2), (1, 2)], min_non_adj_sum=8 >= 8, hamiltonian_berge_cycle=False
PASS
```
