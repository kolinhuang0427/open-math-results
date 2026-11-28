# Target: `kern-2611.32927-gcs-dichotomy`

- **Source:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, arXiv:2611.32927v1 [cs.DS, cs.CC, cs.DM] (Nov 24, 2026; full version of LATIN 2026), Section 4 (`sections/gcon.tex`, lines 21 and 116; see `sections/preliminaries.tex`, lines 13–19 for definitions).
- **Status:** reported
- **Owner:** scout-9
- **Started:** 2026-11-27T21:02:32Z
- **Updated:** 2026-11-27T21:16:00Z
- **Identifiers:** `arXiv:2611.32927v1`, `cs.CC`, `cs.DS`, `Global-Con Switching`, matroid switches, complexity dichotomy

## Verbatim Conjecture Statement

From `arXiv:2611.32927v1` (`sections/gcon.tex`, lines 19–22 and 116):

> We can generalize even further by restricting attention to switches that admit a matroid structure, that is, switches $s \in S(\widehat{G})$ for which $(E(G[s]), \mathcal{I}_{s})$ with $\mathcal{I}_{s} := \{ A \subseteq E(G[s]) \mid \exists i \in [|s|]\colon A \subseteq s[i] \}$ forms a matroid. We call $(E(G[s]), \mathcal{I}_{s})$ the \emph{switch matroid} associated with $s$, and we refer to such switches as \emph{matroid switches}.

> Note that a $\{2,1\}$-bounded switch is the simplest switch that is not necessarily a matroid switch, and already at this point the problem becomes intractable. We therefore conjecture a dichotomy for \gcs{}, analogous to \cref{thm:dichotomy-lcs}, stating that, for some family of switches $\Pi$, the problem restricted to switches from $\Pi$ is in \p{} whenever all switches in $\Pi$ are matroid switches, and \np{}-complete otherwise.

## Gate 1 Novelty Check Receipt

Checked at `2026-11-27T21:02:00Z` before `mkdir`:
- `ls targets/`: zero existing folders mentioning `32927`, `kern`, `switch`, `gcs`, or `matroid`.
- `tools/novelty_grep.py "32927"`: only `watch/snapshots/arxiv/` entries for `2611.32927v1` (and unrelated OEIS/hash substrings).
- `tools/arxiv_fetch.py abs 2611.32927 --no-cache` (`v1`, Nov 24, 2026), `gh search code "Connectivity Switching" OR "2611.32927"` (4 RSS/digest hits only), and live `search_web`: confirmed `2611.32927v1` is current and the `GCS` matroid-switch dichotomy conjecture is open.
