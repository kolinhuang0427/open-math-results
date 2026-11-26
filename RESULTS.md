# Verified Results

Results listed here have cleared all gates in `CHARTER.md`:
1. Exact statement quoted from the primary source (with version/section) and confirmed by a checker.
2. Mechanical verification (`verify.py` / exact computation or lemma check) where applicable.
3. Independent Pro audit (`AUDIT.md`), without seeing the author's commentary.
4. Third novelty gate passed in the hour before reporting.
5. Coordinator verification run and inspected.

Allowed labels:
- `counterexample, verified by exact computation`
- `written proof, internally audited`
- `Lean-checked` (no `sorry`, no axioms beyond `propext`, `Classical.choice`, and `Quot.sound`)

None of these labels constitutes peer review, and each entry states what is not established.

---

### `ferrero-2511.16335-conj1.8` — Counterexample to Ferrero–Hall–Hogben–Hunnell–Small Conjecture 1.8

- **Summary**: Ferrero, Hall, Hogben, Hunnell, and Small conjectured that every connected graph whose upper standard zero forcing propagation time equals 1 must be a "standard fast join" (either a complete graph or a join of edgeless graphs and double cliques). We refuted this conjecture by exhibiting the 12-vertex, 24-edge circulant graph $C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$, which is connected and satisfies $\overline{\mathrm{PT}}(G) = 1$ yet has a connected complement and zero forcing number $8 < n - 2$, so it is not a standard fast join. We further proved that the entire infinite family of cycle blowups $C_6[r_0 K_1, \dots, r_5 K_1]$ with $r_i \ge 2$ gives counterexamples.
- **Exact statement & source**:
  - Source: Daniela Ferrero, H. Tracy Hall, Leslie Hogben, Mark Hunnell, Ben Small, *"Zero forcing propagation time intervals and graphs with fixed propagation time"*, `arXiv:2511.16335v1` (`NewFixedPropTime.tex`, Section 1, Definition 1.5 lines 275–276 and Conjecture 1.8 `\label{c:std}` lines 293–296; verified verbatim in *Australasian Journal of Combinatorics*, Vol. 96(2), 2026, pp. 374–394, revised 2 June 2026).
  - Definition 1.5: *"A graph $G$ of order $n\geq 2$ is a standard fast join if $G\cong K_n$ or $G=\bigvee_{i=1}^t G_i$ where $t\geq 2$ and each graph $G_i$ satisfies $G_i\cong n_iK_1$ or $G_i\cong K_{n_i}\dot{\cup} K_{m_i}$ with $n_i,m_i\geq 2$."*
  - Conjecture 1.8: *"Let $G$ be a connected graph. If $\overline{\mathrm{PT}}(G)=1$, then $G$ is a standard fast join."*
- **Label**: `counterexample, verified by exact computation` (for the explicit 12-vertex witness $C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$, supplemented by `written proof, internally audited` for the infinite family $C_6[r_0 K_1, \dots, r_5 K_1]$, $r_i \ge 2$).
- **Verification command**: `.venv/bin/python targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T20:20:58Z`–`20:21:30Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing` (issue `#8371` closed `2026-09-16` as terminal OPEN with no resolution), GitHub search, live arXiv API (`2511.16335v1` unchanged), OpenAlex `W4416550551` (`cited_by_count: 0`), AJC Vol. 96(2) revised PDF, and web search; 0 prior resolutions found.
- **What is not established**: Global minimality of $n = 12$ across all connected graphs of order $n \le 11$ is not proved (only minimality within the $C_6[r_0 K_1, \dots, r_5 K_1]$ with $r_i \ge 2$ family). Internal auditing and exact computation are not external peer review.

---

### `wei-2310.17337-conj1.5` — Counterexample to Wei–Zhang–Zhao Conjecture 1.5

- **Summary**: Wei, Zhang, and Zhao conjectured that for every connected graph $G \ncong C_k$ of size $m$, the $C_k$-isolation number satisfies $\iota(G, C_k) \le (m + 1)/(k + 2)$, having proved $k = 4$ and building on Borg–Fenech–Kaemawichanurat's $k = 3$ theorem. We refuted this conjecture at $k = 8$ using the 12-vertex, 18-edge truncated tetrahedral graph, for which deleting the closed neighborhood of any single vertex leaves an 8-cycle subgraph so $\iota(G, C_8) = 2 > 19/10 = (m+1)/(k+2)$. The generalized Petersen graphs $GP(9, 2)$ (at $k = 14$, $\iota = 2 > 7/4$) and $GP(11, 2)$ (at $k = 18$, $\iota = 2 > 17/10$) also refute the bound.
- **Exact statement & source**:
  - Source: Xiaohua Wei, Gang Zhang, Biao Zhao, *"On the $C_4$-isolation number of a graph"*, `arXiv:2310.17337v1` (`C_4-isolation.tex`, Section 1, Conjecture 1.5 `\label{conj1.5}`, lines 119–121, and Abstract line 67).
  - Statement: *"If $G \ncong C_k$ is a connected graph of size $m$, then $\iota(G, C_k) \le \frac{m+1}{k+2}$."*
- **Label**: `counterexample, verified by exact computation`
- **Verification command**: `.venv/bin/python targets/wei-2310.17337-conj1.5/notes/check-check-1.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T20:23:09Z`–`20:24:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live `1337isnot1337/solved-conjectures`, GitHub code/repo/issue searches, live arXiv API (`2310.17337v1` unchanged), OpenAlex `W7163506673` (`cited_by_count: 3`: Borg–Scicluna `10.1016/j.dam.2026.08.006`, Liang–Wu `10.1016/j.dam.2025.06.058`, `10.12677/aam.2025.149398`), Crossref `10.1142/s1793830926500679`, and web search; no prior refutation or settlement found.
- **What is not established**:
  - **Published DMAA journal version caveat (`AUDIT.md` §4):** `arXiv:2310.17337v1` was later published in *Discrete Mathematics, Algorithms and Applications* (online `2026-07-21`, DOI `10.1142/s1793830926500679`). The published DMAA abstract replaces the closing statement of Conjecture 1.5 with *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open,"* and because the DMAA full-text PDF is paywalled, it is unverified whether Section 1 of the published journal text retained, modified, or dropped Conjecture 1.5; this refutation applies strictly to `arXiv:2310.17337v1` (Section 1, Conjecture 1.5).
  - Does not settle whether $\iota(G, C_k) \le (m+1)/(k+2)$ holds for the small individual values $k \in \{5, 6, 7\}$, and does not refute the girth-restricted bound $\iota(G, \mathcal{C}) \le (m+1)/(g+2)$ studied by Liang & Wu (2026) (the truncated tetrahedron has girth $3 < 8$ and $GP(9,2)$ has girth $5 < 14$).
  - Internal audit and exact computation are not external peer review.
