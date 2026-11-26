source: arXiv:2511.16335v1 (Daniela Ferrero, H. Tracy Hall, Leslie Hogben, Mark Hunnell, Ben Small, "Zero forcing propagation time intervals and graphs with fixed propagation time", published 2025-11-20)
status: candidate
owner: scout-7
updated: 2026-11-26T20:05:00Z
identifiers: 2511.16335, 2511.16335v1, Ferrero, Hall, Hogben, Hunnell, Small, standard fast join, fixed propagation time, PTbar, Conjecture 1.8

# Conjecture 1.8 of Ferrero–Hall–Hogben–Hunnell–Small (arXiv:2511.16335v1)

## Statement (quoted from primary source `NewFixedPropTime.tex`, lines 275-276 and 293-296, Section 1)

Definition 1.5 (lines 275-276):
> `A graph $G$ of order $n\geq 2$ is a \emph{standard fast join} if $G\cong K_n$ or $G=\bigvee_{i=1}^t G_i$ where $t\geq 2$ and each graph $G_i$ satisfies $G_i\cong n_iK_1$ or $G_i\cong K_{n_i}\du K_{m_i}$ with $n_i,m_i\geq 2$.`

Conjecture 1.8 (`\label{c:std}`, lines 293-296):
> `\begin{conjecture}\label{c:std}`
> `Let $G$ be a connected graph.`
> `If $\PTbar(G)=1$, then $G$ is a standard fast join.`
> `\end{conjecture}`

## Gate 1 Novelty Receipt

- **Checked at:** 2026-11-26T19:58:47Z
- **Sources & snapshots checked:**
  - Local `watch/snapshots/` (`grep -ri "2511.16335\|fixed propagation time" watch/snapshots/`) — no match.
  - `gh api 'search/repositories?q=2511.16335+OR+...'` — 0 results.
  - `gh api 'search/issues?q=2511.16335'` — 0 results.
  - `gh api 'search/issues?q=%22Ferrero%22+%22Hogben%22+propagation'` — 1 result: `the-omega-institute/trureturing/issues/8371` (closed, outcome: **terminal OPEN** — bounded attempt ended with no proof, no counterexample, and no finite scan).
  - `gh api 'search/issues?q=%22standard+fast+join%22'` — only `trureturing/issues/8371`.
  - `search_web` for `"2511.16335"` and `"PSD fast join" OR "standard fast join"` — only links to `arXiv:2511.16335v1`.
- **Near misses:**
  - `trureturing/issues/8371`: attempted Conjecture 1.8, explicitly closed as terminal OPEN with no resolution and no computational scan.
  - Paper itself (Theorem 5.10, Corollary 5.12): proves Conjecture 1.8 when $G$ is already a join of two graphs or when $\Z(G) \ge n-2$. Our counterexamples have connected complement (not a join) and $\Z(G) = n-4$.
- **Not covered:** Private unpublished manuscripts or post-v1 journal galley changes not indexed on arXiv or GitHub.
