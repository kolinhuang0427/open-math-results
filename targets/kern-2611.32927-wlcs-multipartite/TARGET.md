# Target: `kern-2611.32927-wlcs-multipartite`

- **Source:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, arXiv:2611.32927v1 [cs.DS, cs.CC, cs.DM] (Nov 24, 2026; full version of LATIN 2026), Section 5 (`sections/conclusion.tex`, line 5; see `sections/preliminaries.tex`, lines 13–19 and `sections/stcon.tex`, lines 147–188, 215–224).
- **Status:** reported
- **Owner:** scout-9
- **Started:** 2026-11-27T21:03:58Z
- **Updated:** 2026-11-27T21:13:00Z
- **Identifiers:** `arXiv:2611.32927v1`, `cs.CC`, `cs.DS`, `Weighted Local-Con Switching`, complete multipartite switches

## Verbatim Open Question Statement

From `arXiv:2611.32927v1` (`sections/conclusion.tex`, line 5):

> Many open questions remain, for instance whether \oolcs{} restricted to $\{1,1\}$-bounded connected switches is solvable in polynomial time, or perhaps in \fpt{}-time with respect to the solution weight, and, more generally, whether \wlcs\ is solvable in polynomial time for $\{1^\star\}$-bounded complete multipartite switches (as is the case for \lcs).

Definition of `Weighted Local-Con Switching` (`sections/stcon.tex`, lines 215–221):

> \wlcs{}: Input: A switch graph $\widehat{G}$, two distinct vertices $a,b \in V(\widehat{G})$, a weight function $w: S(\widehat{G}) \times \mathbb{Z} \to \mathbb{R}$ on switch positions, and a real $\lambda \in \mathbb{R}$. Question: Is there a configuration $c \in C(\widehat{G})$ such that $a$ and $b$ are connected in $x{\widehat{G}}{c}$ and $w(c) := \sum_{s \in S(\widehat{G})} w(s, c(s)) \le \lambda$?

## Gate 1 Novelty Check Receipt

Checked at `2026-11-27T21:02:00Z` before `mkdir`:
- `ls targets/`: only `kern-2611.32927-gcs-dichotomy` (a distinct conjecture from `sections/gcon.tex` L116).
- `tools/novelty_grep.py "32927"`: only `watch/snapshots/arxiv/` entries for `2611.32927v1` (and unrelated OEIS/hash substrings).
- `tools/arxiv_fetch.py abs 2611.32927 --no-cache` (`v1`, Nov 24, 2026), `gh search code "Connectivity Switching" OR "2611.32927"`, and live `search_web`: confirmed `2611.32927v1` is current and the `wlcs` complete-multipartite question in `sections/conclusion.tex` L5 is open.
