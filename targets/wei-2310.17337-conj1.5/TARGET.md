---
source: https://arxiv.org/abs/2310.17337v1 (Conjecture 1.5, Section 1)
status: reported
owner: scout-9
updated: 2026-11-26T20:34:00Z
identifiers:
  - 2310.17337
  - wei-2310.17337-conj1.5
  - Xiaohua Wei
  - Gang Zhang
  - Biao Zhao
  - C_4-isolation
  - C_k-isolation
---

# Target: Wei–Zhang–Zhao Conjecture 1.5 (`2310.17337v1`)

## Primary Source & Exact Statement

**Source:** Xiaohua Wei, Gang Zhang, Biao Zhao, *"On the $C_4$-isolation number of a graph"*, `arXiv:2310.17337v1 [math.CO]`, Section 1 (Introduction), Conjecture 1.5 (`\label{conj1.5}`, lines 119–121 of `C_4-isolation.tex`).

**Definitions from Section 1 (`C_4-isolation.tex`, lines 74–76):**
- Graphs considered are simple and finite.
- For a vertex $v \in V(G)$, $N_G[v] = \{v\} \cup \{u \in V(G) : uv \in E(G)\}$, and for $D \subseteq V(G)$, $N_G[D] = \bigcup_{v \in D} N_G[v]$.
- $C_k$ is the cycle of length $k$ ($k \ge 3$).
- A subset $D \subseteq V(G)$ is a *$C_k$-isolating set* of $G$ if $G - N[D]$ does not contain $C_k$ as a subgraph.
- The *$C_k$-isolation number* of $G$, denoted $\iota(G, C_k)$, is the cardinality of a smallest $C_k$-isolating set of $G$.

**Exact Verbatim Statement (`C_4-isolation.tex`, Conjecture 1.5):**
> If $G \ncong C_k$ is a connected graph of size $m$, then
> $$\iota(G, C_k) \le \frac{m+1}{k+2}.$$

## Known Cases in Source
- $k = 3$: Proved by Borg, Fenech, Kaemawichanurat (2022), Theorem 1.3.
- $k = 4$: Proved in this paper (`2310.17337v1`), Theorem 1.4.

## Gate 1 Novelty Receipt
- **UTC Timestamp:** `2026-11-26T19:56:00Z`
- **Sources / Snapshots Checked:**
  - `watch/snapshots/1337-solved-conjectures/` (`CONTENTS.md`, `HISTORY.md`, `README.md`, `issues_all.jsonl`)
  - `watch/snapshots/openai-math/` (`CONTENTS.md`)
  - arXiv API via `tools/arxiv_fetch.py`
  - Web search via `search_web`
- **Exact Queries:**
  - `grep -rn -i "isolation\|C_k\|C_5" watch/snapshots/1337-solved-conjectures watch/snapshots/openai-math`
  - `tools/arxiv_fetch.py query 'cat:math.CO AND abs:isolation AND (abs:cycle OR abs:C_4 OR abs:C_5 OR abs:C_k) AND submittedDate:[202310010000 TO 202612312359]' --max-results 20`
  - `search_web`: `"On the C_4-isolation number of a graph" OR "2310.17337" OR "C_5-isolation" OR "C_k-isolation" "Wei"`
  - `search_web`: `"Xiaohua Wei" "Gang Zhang" "C_4-isolation" OR "C_k-isolation" 2024 2025 2026`
  - `search_web`: `"Bartolo" "Borg" "Scicluna" OR "isolation" "C_5" OR "C_6" 2024 2025 2026`
- **Near Misses:**
  - `arXiv:2510.08361v2` (Peter Borg, Dayle Scicluna, Oct 2025 / *Discrete Appl. Math.* 394 (2026), 261–268): *"Isolation of non-triangle cycles in graphs"* proves $\iota(G, \mathcal{C}') \le (m+1)/6$ for $\mathcal{C}' = \{C_k : k \ge 4\}$, implying the $k=4$ bound of Wei–Zhang–Zhao; does not address individual $C_k$-isolation for $k \ge 5$ or Conjecture 1.5.
  - `arXiv:2611.24477v2` (Minhui Li, Shumin Zhang, Junhao Qu, Nov 2026): *"The isolation number of uniform hypertrees"* proves $\iota(T) \le \lfloor n/(2r-1)\rfloor$ for $r$-uniform hypertrees and $\lfloor n/5\rfloor$ for cycle isolation in connected triangle-block graphs (order-based bound for triangles, not size-based bound for $C_k$, $k \ge 5$).
  - Bartolo, Borg, Scicluna (2024–2026): $C_4$-isolation by order (`arXiv:2310.09128`) and $P_3$-isolation; does not address size-based $C_k$-isolation for $k \ge 5$.
  - `1337isnot1337/solved-conjectures` issue #538 / `sonntag-teichert`: unrelated domination hypergraph / permanent results.
- **Not Covered:**
  - Closed-access journal articles not indexed on arXiv or open web search summaries (note `2310.17337` appeared in *Discrete Mathematics, Algorithms and Applications*), and papers not containing `isolation` + `cycle`/`C_4`/`C_5`/`C_k` in arXiv abstracts.
