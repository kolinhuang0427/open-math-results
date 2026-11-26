# Adversarial Literature & Computational Audit Helper Report (`wei-2310.17337-conj1.5`)

**Checked UTC:** `2026-11-26T20:15:00Z`  
**Target:** `targets/wei-2310.17337-conj1.5/` — Wei, Zhang, Zhao, *"On the $C_4$-isolation number of a graph"*, `arXiv:2310.17337v1` (Conjecture 1.5).

---

## 1. `arXiv:2510.08361` (Borg & Scicluna, *"Isolation of non-triangle cycles in graphs"*)
- **Latest version checked:** `arXiv:2510.08361v2` (`v1`: 2025-10-09; `v2`: 2026-10-20; published as *Discrete Appl. Math.* 394 (2026), DOI `10.1016/j.dam.2026.08.006`). Extracted TeX at `tools/.arxiv_cache/eprint/2510.08361/published_ver.tex`.
- **Every mention of Wei–Zhang–Zhao / `2310.17337` / `(m+1)/6`:**
  - Abstract (line 66): *"Our result yields the inequality $\iota(G,\{C_4\}) \leq (m+1)/6$ of Wei, Zhang and Zhao."*
  - Section 1 (line 72): cites `\cite{WZZ}` as motivation.
  - Section 1 (lines 157–162): states Wei, Zhang, and Zhao (`\cite{WZZ}`) proved $\iota(G, \{C_4\}) \le (m+1)/6$ for connected $G \not\simeq C_4$, and Theorem 2 (`\label{mainresult}`) generalizes it to $\iota(G, \mathcal{C}') \le (m+1)/6$ where $\mathcal{C}' = \{C_k : k \ge 4\}$.
  - Section 1 (line 175): notes `\cite{WZZ}` splits into subcubic vs. non-subcubic cases.
  - Bibliography (line 446): `\bibitem{WZZ}` cites the DMAA published version (`https://doi.org/10.1142/S1793830926500679`).
- **Conjecture 1.5 / `C_k`-isolation for $k \ge 5$ / counterexamples:** **Zero mentions** anywhere in `published_ver.tex`. Does not mention `(m+1)/(k+2)` or any counterexample.

---

## 2. Published Journal Version of `2310.17337` (`10.1142/s1793830926500679`)
- **Metadata (Crossref / OpenAlex `W7163506673` / Semantic Scholar):** *"On the $C_4$-isolation number of a graph"*, Xiaohua Wei, Gang Zhang, Biao Zhao, *Discrete Mathematics, Algorithms and Applications*, published online `2026-07-21`, DOI `10.1142/s1793830926500679`. (`2310.17337` remains `v1` only on arXiv, 2023-10-26.)
- **Abstract difference found:**
  - `arXiv:2310.17337v1` abstract ends with: *"Moreover, we conjecture that if $G \ncong C_k$ is a connected graph of size $m$, then $\iota(G,C_k) \leq \frac{m+1}{k+2}$."*
  - Published DMAA (2026) abstract (verified identically in Crossref, OpenAlex, Semantic Scholar) replaces that last sentence with: *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open."*
- **Scope caveat:** DMAA 2026 full-text PDF is closed-access behind World Scientific's paywall, so we cannot inspect Section 1 of the journal PDF to see whether Conjecture 1.5 itself was modified or dropped in the journal body. However:
  1. `TARGET.md` explicitly anchors to `arXiv:2310.17337v1` (Section 1, Conjecture 1.5, lines 119–121 of `C_4-isolation.tex`), which is verbatim accurate.
  2. The DMAA abstract explicitly states the general $C_k$-isolation problem remains open (no refutation or counterexample).

---

## 3. Deep Literature Search (2023–2026): Novelty & Related Works
Checked arXiv (`tools/arxiv_fetch.py`), OpenAlex API (author IDs & citation graphs), Crossref API, Semantic Scholar API, and `search_web`:

- **Citations to Wei–Zhang–Zhao (`W7163506673` / `10.1142/s1793830926500679`):** OpenAlex reports **3 citing works** (note: `watch/snapshots/arxiv/citing/wei-2310.17337-conj1.5.json` only queried arXiv ID `2310.17337` and recorded `citing_count: 0`, missing these 3 DOI citations):
  1. **Yanfang Liang & Baoyindureng Wu (2025/2026)**, *"Cycle isolation in graphs"*, *Discrete Appl. Math.* 378 (2026), 1–11 (`10.1016/j.dam.2025.06.058`). Studies **all-cycle** isolation $\iota(G, \mathcal{C})$ in terms of size $m$ and **girth** $g$, proving $\iota(G, \mathcal{C}) \le \frac{m+1}{g+2}$ ($G \not\cong C_g$) for girths $g \in \{4, 5, 6\}$ (following Zhang & Wu 2024 papers `10.1007/s40840-024-01655-x`, `10.1007/s00373-024-02768-7`, `10.1016/j.disc.2024.114190`). Does **not** address $\iota(G, C_k)$ without a girth $\ge k$ constraint or refute Conjecture 1.5 (all counterexamples here have girth $< k$: truncated tetrahedron has girth $3 < 8$, $GP(9,2)$ has girth $5 < 14$).
  2. **Yuhui Zhao (2025)**, *"Total Isolation Number of the Cartesian Product of Paths and Cycles"* (`10.12677/aam.2025.149398`) — Cartesian products / total isolation.
  3. **Peter Borg & Dayle Scicluna (2026)**, *"Isolation of non-triangle cycles in graphs"* (`arXiv:2510.08361v2`, `10.1016/j.dam.2026.08.006`) — see Section 1 above.
- **Bartolo, Borg & Scicluna (`arXiv:2310.09128v2`, *Discrete Math.* 347 (2024), 114161):** Order-based $C_4$-isolation ($\iota(G, C_4) \le n/5$ outside 9 exceptions); cites Borg (`arXiv:2303.13709`) for the lower bound $c(C_k) \ge \frac{2}{2k+1} > \frac{1}{k+1}$ on **order-based** $C_k$-isolation ($k \ge 5$). Does not study size-based $C_k$-isolation.
- **Borg (`arXiv:2303.13709v4`, *Discrete Math.* 349 (2026), 114706):** The graph $C(k-1)$ used for order-based $C_k$-isolation ($k \ge 5$) is $(k-1)$-regular on $2k$ vertices, hence $m = k(k-1) \gg k+2$, so it gives $\iota \approx \frac{2}{2k+1}n \ll \frac{m+1}{k+2}$ and does **not** refute Conjecture 1.5.
- **Other 2024–2026 isolation papers checked:** Chen & Cui (`10.1016/j.disc.2026.115076`, proves $\iota(G, \mathcal{C}') \le n/5$ outside $\mathcal{E}_4$); Chen, Cui, Zhang (`10.1016/j.dam.2025.01.037`); El Zein & Shreif (`10.1007/s00373-025-02946-1`, *"Isolation of Connected Graphs in Terms of Size"*); Zhang, Yang, Jin (`arXiv:2411.03666`); Borg (`arXiv:2602.22856v1`); Borg & Kaemawichanurat (`arXiv:2611.19361v1`); Baluci & Borg (`arXiv:2611.17489v1`); Li, Zhang, Qu (`arXiv:2611.24477v2`). None settle or refute Conjecture 1.5 or mention the truncated tetrahedron / generalized Petersen counterexamples.
- **Novelty conclusion:** No published paper, preprint, or public repository found refutes Wei–Zhang–Zhao Conjecture 1.5.

---

## 4. Watch Snapshots & GitHub (Read-Only)
- `watch/snapshots/`: Only hits are `watch/snapshots/arxiv/citing/wei-2310.17337-conj1.5.json` (`citing_count: 0`, checked `2310.17337` only) and `watch/snapshots/arxiv/openalex_works_cache.json`.
- GitHub (`gh search code`, `gh search repos`, `1337isnot1337/solved-conjectures` issues, `Leo66Gao/solved-conjectures`): Zero hits for `1793830926500679`, `C_k-isolation`, `truncated tetrahedron` + `isolation`, or Wei–Zhang–Zhao Conjecture 1.5.

---

## 5. Mechanical & Structural Verification
1. **Checker script rerun:** `.venv/bin/python targets/wei-2310.17337-conj1.5/notes/check-check-1.py` exited `0` and printed:
   - `TruncatedTetrahedron: n=12, m=18, k=8, iota(G,C_8)=2, (m+1)/(k+2)=19/10, diff=1/10`
   - `GP(9,2): n=18, m=27, k=14, iota(G,C_14)=2, (m+1)/(k+2)=7/4, diff=1/4`
   - `GP(11,2): n=22, m=33, k=18, iota(G,C_18)=2, (m+1)/(k+2)=17/10, diff=3/10`
   - `PASS`
2. **Independent NetworkX inspection of Truncated Tetrahedron:**
   - Isomorphic to `nx.truncated_tetrahedron_graph()` (`True`).
   - `n = 12`, `m = 18`, `girth = 3`, connected (`True`), $3$-regular, automorphism group order `24`, vertex-transitive (`True`).
   - `G - N[0]` has 8 vertices `{4,5,6,7,8,9,10,11}`, 10 edges, degree sequence `[2,2,2,2,3,3,3,3]`.
   - Simple cycles in `G - N[0]`: two $C_3$'s, one $C_6$, two $C_7$'s, and **one $C_8$ subgraph** `(4, 5, 10, 9, 11, 8, 6, 7)` (non-induced, as `G - N[0]` has 10 edges).
   - **Definition check:** Wei–Zhang–Zhao (`C_4-isolation.tex`, line 76) define $D$ as a $C_k$-isolating set if *"G - N[D] does not contain members of $\mathcal{F}$ as subgraphs"* (subgraph, **not** induced subgraph). So the non-induced $C_8$ subgraph is 100% valid.
   - Across all $k \in [3, 11]$ on the truncated tetrahedron: $k \in \{4,5\}$ do not appear ($\iota = 0$); $k \in \{3,6,7\}$ have $\iota \ge 2$ but satisfy $\iota \le 19/(k+2)$; $k \in \{9,10,11\}$ have $\iota = 1 \le 19/(k+2)$; **only $k=8$ violates** ($2 > 19/10$).
3. **Search for smaller / $k \in \{5,6,7\}$ counterexamples:**
   - All 1,252 graphs in `nx.graph_atlas` ($n \le 7$): `0` counterexamples.
   - Tested `Prism(3..9)`, `Mobius(3..9)`, `GP(5..10, step)`, and named graphs: `0` counterexamples for $k \in \{5,6,7\}$. Additional cubic counterexamples found for larger $k$: `GP(8,2)` ($n=16, m=24, k=11$), `GP(9,3)` ($n=18, m=27, k=13$), `GP(9,4)` ($n=18, m=27, k=14$), `GP(10,1..4)` ($n=20, m=30, k=14,15$), `Desargues` ($n=20, m=30, k=14$), `Dodecahedral` ($n=20, m=30, k=14,15$), `Truncated-cube` ($n=24, m=36, k=17,18$).
   - Note on minimality: for any $3$-regular graph ($m = \frac{3}{2}n$) where every $G - N[v]$ has a Hamiltonian $C_{n-4}$, $\iota(G, C_{n-4}) \ge 2 > \frac{\frac{3}{2}n+1}{n-2}$ holds iff $n > 10$, making $n=12, m=18, k=8$ the smallest cubic counterexample of this form.

---

## 6. Follow-Up Checks (`#66`)

1. **El Zein & Shreif (`10.1007/s00373-025-02946-1`, *Graphs and Combinatorics* 41, article 91, 2025, *"Isolation of Connected Graphs in Terms of Size"*):**
   - **Springer abstract retrieved directly** (`https://link.springer.com/article/10.1007/s00373-025-02946-1`): studies general $H$-isolation in terms of $m(G)$, $m(H)$, and domination number $\gamma(H)$. Building on Zhang & Wu (*Discrete Appl. Math.* 357:99–111, 2024: $\iota(G,H) \le \gamma(H)\frac{m(G)+s}{m(H)+1}$) and Borg (*Discrete Appl. Math.* 371:247–253, 2025: $\iota(G,H) \le \frac{m(G)+1}{m(H)+2}$ for $\gamma(H)=1$), El Zein & Shreif prove that for any connected $H$ with $\gamma(H) \ge 2$ and any graph $G$,
     $$\iota(G,H) \le \gamma(H)\frac{m(G)}{m(H)+\gamma(H)+1},$$
     with equality iff $H = P_4$ and every component of $G$ is $P_4$ (*"Several problems are posed."*).
   - For $H = C_k$ ($k \ge 4$), $\gamma(C_k) = \lceil k/3 \rceil \ge 2$; at $k=8, m=18$ this gives $\iota(G, C_8) \le 3 \cdot \frac{18}{12} = 4.5$, much weaker than $\frac{m+1}{k+2} = \frac{19}{10}$.
   - Crossref reference list (ref 14) cites `Wei, X., Zhang, G., Zhao, B.: On the C4-isolation number of a graph. arXiv:2310.17337 (2023)` as background; **no mention of $C_k$-isolation, Conjecture 1.5, or any counterexample** appears in the Springer abstract or metadata (no arXiv preprint exists; full Springer PDF is paywalled).

2. **Additional TeX & Abstract Inspections (`2602.22856v1`, `2411.03666v1`, `Liang–Wu`):**
   - **`arXiv:2602.22856v1` (Borg & Caro, *"Results on three problems on isolation of graphs"*, `submission.tex`):** Addresses NP-completeness of $F$-ISP, minimum degree $\delta$ bounds on $\iota(G,F)$, and $\iota(G, t\mathcal{F})$ vs. $\iota(G, \mathcal{F})$. Line 97 mentions size bounds `\cite{Borgrc2,BFK2,CZ,ZW2}` for $K_k$ and all-cycles $\mathcal{C}$. **Zero mentions** of Wei–Zhang–Zhao (`2310.17337` / `10.1142/s1793830926500679`), $C_4$-isolation, $C_k$-isolation, or Conjecture 1.5.
   - **`arXiv:2411.03666v1` (Zhang, Yang, Jin, *"Isolation partitions in graphs"*, `main.tex` — co-authored by Gang Zhang of `2310.17337`):** Studies vertex partitions into disjoint $k$-clique or all-cycle ($\mathcal{C}$) isolating sets. **Zero mentions** of Wei–Zhang–Zhao (`2310.17337`), $C_k$-isolation, `(m+1)/(k+2)`, or Conjecture 1.5 anywhere in text or bibliography.
   - **Liang & Wu (`10.1016/j.dam.2025.06.058`, *Discrete Appl. Math.* 378 (2026) 1–11, *"Cycle isolation in graphs"*):** Crossref reference list (ref 12) cites `arXiv:2310.17337`. Studies **all-cycle** isolation $\iota_c(G) = \iota(G,\mathcal{C})$ in terms of size $m$ and girth $g$, proving $\iota_c(G) \le \frac{m+1}{g+2}$ ($G \not\cong C_g$) for $g \in \{4,5,6\}$ (no arXiv preprint; Elsevier full PDF paywalled).
   - **DMAA 2026 abstract edit:** Crossref metadata shows `10.1142/s1793830926500679` was created `2026-06-04` and published online `2026-07-21` (nearly 3 years after `2310.17337v1`). None of the inspected preprints/abstracts explain why the DMAA 2026 abstract replaced the conjecture sentence with *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open"* or report any counterexample (DMAA 2026 body PDF is paywalled).

3. **`arXiv:2303.13709v4` (Borg, *"Isolation of regular graphs, stars and $k$-chromatic graphs"*, `arxiv_final.tex`):**
   - Studies **order-based** isolation bounds ($\iota(G, \mathcal{F}) \le n/(k+1)$, and $c(C_k) \ge \frac{2}{2k+1}$ for $k \ge 5$).
   - Lists `BFK2` (*Isolation of $k$-cliques II*) in `\bibitem{BFK2}` (line 539) without even citing it in the body text; **zero mentions** of size-based bounds (`|E(G)|`, `(m+1)/(k+2)`), Wei–Zhang–Zhao, or $C_k$-isolation by size $m$.
