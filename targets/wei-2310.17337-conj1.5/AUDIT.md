# Adversarial Audit Report: `wei-2310.17337-conj1.5`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T20:22Z`
- **Verdict:** **PASS**
- **Charter Label:** `"counterexample, verified by exact computation"`
- **Independent Verifier:** `targets/wei-2310.17337-conj1.5/notes/check-check-1.py` (report: `targets/wei-2310.17337-conj1.5/notes/check-check-1.md`)

---

## 1. Isolation & Materials Inspected

In accordance with `CHARTER.md`, this audit was conducted without reading `verify.py`, `notes/screen-*`, `notes/attack-*`, or any author commentary. Inspected materials:
1. Primary source: `tools/.arxiv_cache/eprint/2310.17337v1/C_4-isolation.tex` (`arXiv:2310.17337v1`, sole version on arXiv).
2. `targets/wei-2310.17337-conj1.5/TARGET.md`.
3. `targets/wei-2310.17337-conj1.5/COUNTEREXAMPLE.md`.
4. `targets/wei-2310.17337-conj1.5/notes/check-check-1.md` and `targets/wei-2310.17337-conj1.5/notes/check-check-1.py`.
5. Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and independent adversarial literature/verification notes (`notes/audit-lit-wei.md`, produced by Flash helper `lit-verifier`).

---

## 2. Primary-Source Fidelity Audit

Verified directly against `C_4-isolation.tex` (Xiaohua Wei, Gang Zhang, Biao Zhao, *"On the $C_4$-isolation number of a graph"*, `arXiv:2310.17337v1`):
- **Scope & Definitions (Abstract line 67; Section 1 lines 74–76, 94):** Graphs are simple and finite; order is $n = |V(G)|$, size is $m = |E(G)|$; $N_G[v] = \{v\} \cup N_G(v)$, $N_G[D] = \bigcup_{v \in D} N_G[v]$, and $G - S = G[V(G) \setminus S]$. For integer $k \ge 3$, $C_k$ is the cycle of length $k$. A set $D \subseteq V(G)$ is a $C_k$-isolating set of $G$ if $G - N_G[D]$ contains no $C_k$ as a **subgraph** (not necessarily induced; consistent with the paper's own treatment of $K_4^-$ and $K_4$ in Theorem 1.4). $\iota(G, C_k)$ is the minimum size of a $C_k$-isolating set.
- **Exact Verbatim Conjecture (Section 1, Conjecture 1.5, `\label{conj1.5}`, lines 119–121; also Abstract line 67):**
  > If $G \ncong C_k$ is a connected graph of size $m$, then $$\iota(G, C_k) \leq \frac{m+1}{k+2}.$$
- **No Hidden Hypotheses:** Checked the entire LaTeX source (lines 1–392). No additional girth, connectivity, degree, or $k$-range restrictions appear anywhere in the abstract, Section 1, Proposition 1.6, or Section 2.
- **Fidelity Verdict:** Exact match across `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-1.py`. Zero quantifier, hypothesis, or definition drift.

---

## 3. Adversarial Mathematical & Code Audit

### 3.1 Hand Verification of the Primary Witness (`k = 8`)
Let $G$ be the truncated tetrahedral graph specified in `COUNTEREXAMPLE.md` on $V(G) = \{0, 1, \dots, 11\}$ with four vertex-disjoint triangles $T_0=\{0,1,2\}, T_1=\{3,4,5\}, T_2=\{6,7,8\}, T_3=\{9,10,11\}$ and six matching edges $\{0,3\}, \{1,6\}, \{2,9\}, \{4,7\}, \{5,10\}, \{8,11\}$.

1. **Hypotheses of Conjecture 1.5:**
   - Simple & finite: $n = 12$; no self-loops; all 12 endpoints of the 6 matching edges are distinct and lie in distinct triangles, so no parallel edges.
   - Size $m$: $4 \cdot 3 + 6 = 18$, and every vertex has degree $3$ ($12 \cdot 3 / 2 = 18$).
   - Connected: contracting each triangle $T_i$ yields $K_4$, which is connected.
   - $G \ncong C_8$: $|V(G)| = 12 \neq 8$ (and $G$ is $3$-regular).
   - $k = 8 \ge 3$ is an integer.
2. **Vertex-Transitivity (independently proved):**
   Map each vertex to the ordered pair $(i, j)$ ($i \neq j \in \{0,1,2,3\}$) where the vertex lies in $T_i$ and its matching edge goes to $T_j$: $0=(0,1), 1=(0,2), 2=(0,3), 3=(1,0), 4=(1,2), 5=(1,3), 6=(2,0), 7=(2,1), 8=(2,3), 9=(3,0), 10=(3,1), 11=(3,2)$. Triangle edges connect $(i,j) \sim (i,l)$ ($j \neq l$) and matching edges connect $(i,j) \sim (j,i)$. Thus $S_4$ acts as a subgroup of $\mathrm{Aut}(G)$ via $\pi \cdot (i,j) = (\pi(i), \pi(j))$, which is transitive on all $12$ vertices.
3. **Lower Bound $\iota(G, C_8) \ge 2$:**
   For $v = 0$, $N_G[0] = \{0,1,2,3\}$, so $V(G) \setminus N_G[0] = \{4,5,6,7,8,9,10,11\}$. The sequence $(4, 5, 10, 9, 11, 8, 6, 7, 4)$ visits $8$ distinct vertices outside $N_G[0]$ using valid edges $\{4,5\} \subset T_1$, $\{5,10\}$, $\{10,9\}, \{9,11\} \subset T_3$, $\{11,8\}$, $\{8,6\}, \{6,7\} \subset T_2$, and $\{7,4\}$. (It is a non-induced $C_8$ subgraph with chords $\{10,11\}$ and $\{7,8\}$, which satisfies the primary source's subgraph definition.) By vertex-transitivity, $G - N_G[v]$ contains $C_8$ for every $v \in V(G)$ (and $G - N_G[\emptyset] = G$ contains the same $C_8$). Hence no set of size $\le 1$ isolates $C_8$, so $\iota(G, C_8) \ge 2$.
4. **Upper Bound $\iota(G, C_8) \le 2$:**
   For $D = \{0, 4\}$, $N_G[D] = \{0,1,2,3\} \cup \{3,4,5,7\} = \{0,1,2,3,4,5,7\}$, leaving $|V(G) \setminus N_G[D]| = 5 < 8$, so $G - N_G[D]$ cannot contain $C_8$. Thus $\iota(G, C_8) = 2$.
5. **Exact Violation:**
   $$\iota(G, C_8) = 2 > \frac{19}{10} = \frac{18 + 1}{8 + 2} = \frac{m + 1}{k + 2} \qquad (2 \cdot 10 = 20 > 19).$$

### 3.2 Audit of Independent Verifier (`notes/check-check-1.py`)
Audited all 185 lines of `notes/check-check-1.py`:
- Uses exact integer and `fractions.Fraction` arithmetic exclusively (zero floating point).
- `find_ck_subgraph` performs a sound and complete DFS for simple $k$-cycles anchored at their minimum vertex `start` with `nxt > start` and `used` set; no pruning drops any valid cycle, and closing via `start in sub_adj[curr]` at `len(path) == k` ensures a valid simple $C_k$ subgraph.
- `exact_isolation_number_upto` exhaustively tests all $\sum_{s=0}^{2} \binom{n}{s}$ subsets of size $\le 2$.
- Independently rerun by `lit-verifier` (`.venv/bin/python targets/wei-2310.17337-conj1.5/notes/check-check-1.py`), returning exit code `0` and `PASS` on the truncated tetrahedron ($k=8$, $2 > 19/10$) as well as both secondary witnesses mentioned in `COUNTEREXAMPLE.md`: $GP(9,2)$ ($k=14$, $2 > 7/4$) and $GP(11,2)$ ($k=18$, $2 > 17/10$).
- Also cross-checked via NetworkX (`nx.truncated_tetrahedron_graph()`, automorphism group order 24, unique $C_8$ in $G - N[0]$).

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks across arXiv TeX sources, OpenAlex, Crossref, Springer/Elsevier/World Scientific abstracts, and GitHub (`notes/audit-lit-wei.md`) confirmed:
- **No prior refutation or settlement found** in arXiv, OpenAlex citations to Wei–Zhang–Zhao, Borg & Scicluna (`arXiv:2510.08361v2`, *Discrete Appl. Math.* 394, 2026), Liang & Wu (*Discrete Appl. Math.* 378, 2026), El Zein & Shreif (*Graphs Combin.* 41, 2025), Borg & Caro (`arXiv:2602.22856v1`), Zhang–Yang–Jin (`arXiv:2411.03666v1`), Borg (`arXiv:2303.13709v4`), Bartolo–Borg–Scicluna (`arXiv:2310.09128v2`), or competing GitHub conjecture repositories.
- **Important Caveat (Published Journal Version):** `arXiv:2310.17337v1` was subsequently published in *Discrete Mathematics, Algorithms and Applications* (online `2026-07-21`, DOI `10.1142/s1793830926500679`). While the arXiv `v1` abstract explicitly states Conjecture 1.5, the published DMAA abstract replaces that closing sentence with *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open."* Because the DMAA full-text PDF is paywalled, we cannot verify whether Section 1 of the journal version retained, modified, or dropped Conjecture 1.5. This refutation is strictly verified against `arXiv:2310.17337v1` (Section 1, Conjecture 1.5), and the DMAA abstract itself confirms no resolution of general $C_k$-isolation had appeared.
- **What Is Not Established:**
  - This is a finite counterexample at $k = 8$ (plus $k = 14, 18$ via $GP(9,2), GP(11,2)$), which completely refutes the universal Conjecture 1.5 for general $k \ge 3$, but does **not** settle whether $\iota(G, C_k) \le \frac{m+1}{k+2}$ holds for the specific small values $k \in \{5, 6, 7\}$ (no counterexample was found for $k \in \{5, 6, 7\}$ in our auxiliary checks).
  - It does **not** refute the girth-restricted all-cycle bound $\iota(G, \mathcal{C}) \le \frac{m+1}{g+2}$ studied by Liang & Wu (2026), since the truncated tetrahedron has girth $3 < 8$ (and $GP(9,2)$ has girth $5 < 14$).
  - Internal audit and exact computation are not formal peer review.

---

## 5. Final Verdict

**PASS** — `"counterexample, verified by exact computation"`. Gate 3 novelty cleared (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`, checked `2026-11-26T20:23–20:24Z`).
