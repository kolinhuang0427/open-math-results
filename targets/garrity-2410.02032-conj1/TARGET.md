# Target: `garrity-2410.02032-conj1`

- **Source:** Thomas Garrity and Otto Vaughn Osterman, *"On the Factor Complexity Associated with a Family of Multidimensional Continued Fraction Algorithms"*, `arXiv:2410.02032v2` (`Final_Revision-Garrity-Osterman.tex`, *Combinatorics and Number Theory* 15 (2026), 239–292, DOI `10.2140/cnt.2026.15.239`), Section 8 (*Statements on Complexity for All TRIP Maps*, `L2020`), **Conjecture 1** (`\label{conj:e-23-e}`, L2149–2151).
- **Status:** reported
- **Owner:** scout-11
- **Created (UTC):** 2026-11-27T10:00:56Z
- **Updated (UTC):** 2026-11-27T10:22:00Z
- **Identifiers:** `arXiv:2410.02032v2`, `DOI:10.2140/cnt.2026.15.239`, `Conjecture 1` (`\label{conj:e-23-e}`), `Section 10` (`\label{sec:e-23-e}`), `S(e,23,e)`-adic languages.

## Definitions (quoted from `arXiv:2410.02032v2`, Sections 3, 4, 7 & 10)

- **Alphabet & Language (`Section 4`, Definition 12, `L664–669`):** Over $\mathcal{A} = \{1, 2, 3\}$, for a coding sequence $\mathbf{\sigma} = (\sigma_0, \sigma_1, \dots)$ of substitutions,
  $$\mathcal{L}(\mathbf{\sigma}) = \{ w \in \mathcal{A}^* : w \text{ is a factor of } (\sigma_0 \circ \sigma_1 \circ \cdots \circ \sigma_{n-1})(c) \text{ for some } n \in \mathbb{N},\ c \in \mathcal{A} \}.$$
  The factor complexity is $p_{\mathcal{L}}(n) := |\{ w \in \mathcal{L} : |w| = n \}|$ (`Section 3`, `L460–462`).
- **Farey substitutions for $T(e, 23, e)$ (`Section 10`, `L2663–2667`):**
  $$S_0(e,23,e):\ 1 \mapsto 2,\ 2 \mapsto 13,\ 3 \mapsto 3; \qquad S_1(e,23,e):\ 1 \mapsto 1,\ 2 \mapsto 2,\ 3 \mapsto 13.$$
- **Conjugates and Twins (`Section 7`, Propositions 18–19, `L1935–1977`):** Replacing $\mathcal{L}$ by $\rho(\mathcal{L})$ ($\rho \in S_3$) or its reversal $R(\mathcal{L})$ preserves factor complexity identically (`L1942`, `L1967`).

## Verbatim Conjecture Statement (`arXiv:2410.02032v2`, Section 8, L2149–2151)

> **Conjecture 1** (`\label{conj:e-23-e}`). The complexity function $p_{\mathcal{L}}$ for $S(e,23,e)$-adic language $\mathcal{L}$ (and any of its five conjugates or six twins) satisfies the bound $p_{\mathcal{L}}(n) \leq 3n$.

## Gate 1 Novelty Check Receipt (`2026-11-27T10:00Z`)

- `targets/` check: no existing `garrity-2410.02032*` folder.
- `.venv/bin/python tools/novelty_grep.py "2410.02032" "Garrity" "S(e,23,e)"` across all 617 files in `watch/snapshots/**`: `0` hits.
- `.venv/bin/python tools/arxiv_fetch.py query --max-results 10 '"Garrity" AND "TRIP"'` and `'"Osterman" AND "complexity"'`: `2410.02032v2` (`2026-07-21`, published *Comb. Number Th.* 15 (2026)) is latest; Conjecture 1 (`conj:e-23-e`) remains open in `v2` (Section 10 sets up a partial proof strategy without completing it).
- `search_web` for `"2410.02032" OR ("TRIP map" "S(e,23,e)") "3n"`: returns only `arXiv:2410.02032`; no external resolution found.
- Verdict: OPEN, clear to attack.
