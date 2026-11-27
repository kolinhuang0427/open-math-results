---
source: arXiv:2604.22375v1 (Section 3.1, Conjecture 1 / \label{conjecture1}, lines 370–372)
status: reported
owner: scout-12
updated: 2026-11-27T09:47:14Z
identifiers: ["2604.22375", "2604.22375v1", "Ciobanu", "Turaev", "Visibly Pushdown Languages", "VPL", "conjecture1"]
---

# Ciobanu–Turaev (arXiv:2604.22375v1): $\mathbf{VPL}^\forall = \mathbf{REG}^\forall$ in Groups

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2604.22375v1/Arxiv_version.tex`, definitions lines 204–215, Conjecture 1 lines 370–372)

For a finitely generated group $G = \langle X \rangle$ with $\Sigma = X \cup X^{-1}$ and canonical monoid epimorphism $\pi : \Sigma^\star \to G$: a subset $S \subseteq G$ is in $\mathbf{VPL}^\forall$ if $\pi^{-1}(S) \in \mathbf{VPL}$ (accepted by a visibly pushdown automaton for some partition $\Sigma = \Sigma_c \sqcup \Sigma_i \sqcup \Sigma_r$), and is in $\mathbf{REG}^\forall$ (*recognisable*) if $\pi^{-1}(S) \in \mathbf{REG}$.

> \begin{conj}\label{conjecture1}
>     In all groups, every $\mathbf{VPL}^\forall$ set is recognisable. In other words, the classes $\mathbf{VPL}^\forall$ and $\mathbf{REG}^\forall$ are equal. 
> \end{conj}

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T09:44:00Z` (start time recorded)
- `tools/novelty_grep.py 2604.22375`: 0 hits across all 608 files in `watch/snapshots/**`.
- `gh search issues "2604.22375"` and `gh search prs "2604.22375"`: 0 results.
- `search_web` (`"2604.22375" OR ("Visibly Pushdown Languages in Groups" "recognisable")`) and `gh search code "2604.22375"`: only `arXiv:2604.22375` itself and arXiv feed/listing repos (`Lyken17/arXiv-stats`, `SauersML/group-approximation`, `ehijano/rss_fetch`); 0 follow-up papers or solutions found.
