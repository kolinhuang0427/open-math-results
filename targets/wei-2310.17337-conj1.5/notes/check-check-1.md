# Independent Check Report: `wei-2310.17337-conj1.5` (`check-1`)

- **Checked at (UTC):** `2026-11-26T20:01:32Z`
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity and independent exact-arithmetic verification)

## 1. Primary-Source Fidelity Check

- **Primary source fetched:** `arXiv:2310.17337v1` via `.venv/bin/python tools/arxiv_fetch.py eprint 2310.17337v1 --extract` (`/Users/kev/Documents/open-math/tools/.arxiv_cache/eprint/2310.17337v1/C_4-isolation.tex`). Also verified via `tools/arxiv_fetch.py query --id-list 2310.17337` that `v1` is the sole version on arXiv.
- **Exact sections & lines checked in `C_4-isolation.tex`:**
  - Abstract (line 67)
  - Section 1 (Introduction), definitions (lines 74–76, 94)
  - Section 1, Conjecture 1.5 (`\label{conj1.5}`, lines 119–121):
    > If $G \ncong C_k$ is a connected graph of size $m$, then $$\iota(G,C_k) \leq \frac{m+1}{k+2}.$$
- **Word-for-word comparison against `TARGET.md` and `COUNTEREXAMPLE.md`:**
  - Graphs are simple and finite (line 74).
  - $N_G[v] = \{v\} \cup N_G(v)$, $N_G[S] = \bigcup_{v \in S} N_G[v]$, and $G-S$ denotes $G[V \setminus S]$ (line 74).
  - $C_k$ is the cycle of length $k$ ($k \ge 3$); $D \subseteq V(G)$ is a $C_k$-isolating set if $G - N[D]$ contains no $C_k$ as a subgraph; $\iota(G, C_k)$ is the cardinality of a smallest $C_k$-isolating set (lines 67, 76, 94).
  - Conjecture 1.5 verbatim matches both `TARGET.md` and `COUNTEREXAMPLE.md`. Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from `C_4-isolation.tex` definitions and the explicit construction in `COUNTEREXAMPLE.md`, without reading `verify.py` or any file in `notes/`.
- **Verifier script:** `targets/wei-2310.17337-conj1.5/notes/check-check-1.py` (exact integer/rational arithmetic with `fractions.Fraction`, exhaustive subset search for $|D| \in \{0, 1, 2\}$, explicit DFS simple-$C_k$ subgraph test).
- **Verified claims:**
  1. Primary witness ($k = 8$): Truncated tetrahedral graph on $n = 12$ vertices and $m = 18$ edges is simple, finite, connected, $3$-regular, and $G \ncong C_8$.
  2. For $D = \{0\}$, $G - N[0]$ has $8$ vertices $\{4,5,6,7,8,9,10,11\}$ and contains the $8$-cycle $(4, 5, 10, 9, 11, 8, 6, 7, 4)$.
  3. Exhaustively across all $\binom{12}{0} + \binom{12}{1} = 13$ subsets of size $\le 1$, $G - N[D]$ contains a $C_8$ subgraph; for $D = \{0, 4\}$, $|V(G) \setminus N[D]| = 5 < 8$, so no $C_8$ exists. Hence $\iota(G, C_8) = 2$ exactly.
  4. Exact rational comparison: $\iota(G, C_8) = 2 > \frac{18+1}{8+2} = \frac{19}{10}$ (excess $\frac{1}{10}$).
  5. Secondary witnesses mentioned in `COUNTEREXAMPLE.md` also verified: `GP(9,2)` ($n=18, m=27, k=14, \iota=2 > 7/4$) and `GP(11,2)` ($n=22, m=33, k=18, \iota=2 > 17/10$).

### Command & Raw Output

Command:
```bash
.venv/bin/python targets/wei-2310.17337-conj1.5/notes/check-check-1.py
```

Raw output:
```text
TruncatedTetrahedron: n=12, m=18, k=8, iota(G,C_8)=2, (m+1)/(k+2)=19/10, diff=1/10
GP(9,2): n=18, m=27, k=14, iota(G,C_14)=2, (m+1)/(k+2)=7/4, diff=1/4
GP(11,2): n=22, m=33, k=18, iota(G,C_18)=2, (m+1)/(k+2)=17/10, diff=3/10
PASS
```
