---
title: "Gaevoy Open Question: SRCII[1] vs. Resolution (arXiv:2606.25895v1, §2 & §6)"
source: "arXiv:2606.25895v1"
status: reported
owner: attack-4
started_utc: 2026-11-27T18:56:21Z
updated_utc: 2026-11-27T19:52:00Z
identifiers:
  - "arXiv:2606.25895v1"
  - "SRCII[1]"
  - "Resolution with local 1-symmetries"
---

# Target: Gaevoy Open Question — $\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs. Resolution (`arXiv:2606.25895v1`, §§ 2 & 6)

- **Source:** `arXiv:2606.25895v1` (*The Power of Small Symmetries*, Nikita Gaevoy, `2026-06-24`), Section 2 (`static/definitions.tex` lines 127–142) and Section 6 (`static/open.tex` lines 3–5).
- **Status:** `reported`
- **Owner:** `attack-4`
- **Started UTC:** `2026-11-27T18:56:21Z`
- **Updated UTC:** `2026-11-27T19:52:00Z`

## Statement (verbatim from `static/open.tex` lines 3–5 and `static/definitions.tex` lines 141–142)

From Section 6 (`Conclusion and Open Problems`, `static/open.tex` lines 3–5):
> We have shown that the systems $3\text{-SRC-I}$ and $6\text{-SR-I}$ are stronger than Resolution.
> The question of whether systems with smaller constraints are stronger than Resolution is open.
> It seems plausible that a separation exists even for $1\text{-SRC-II}$ and Resolution.

Context from Section 2 (`static/definitions.tex` lines 55–59, 127–142):
- $1\text{-SRC-II}$ is Resolution with local $1$-symmetries: a $1$-symmetry $\phi$ maps literals to literals with $\phi(\neg x) = \neg\phi(x)$ and fixes all variables except at most one ($x \mapsto \neg x$); the symmetry rule allows inferring $\phi(A)$ from $\phi(B_1), \dots, \phi(B_l)$ whenever $A$ was previously inferred from $B_1, \dots, B_l$ and all $B_i, \phi(B_i)$ belong to the input CNF formula $\Phi$.
- Having proved $1\text{-SRC-I}$ is p-equivalent to $\mathrm{Res}$, Gaevoy notes (`static/definitions.tex` lines 141–142):
> The approach in this lemma cannot be extended to $1\text{-SRC-II}$ because removal of variables may break some symmetries. Moreover, it is likely that $1\text{-SRC-II}$ is strictly stronger than Resolution.

## Gate 1 Novelty Check Receipt (`2026-11-27T18:56:21Z`)
- `targets/`: 0 existing targets for `gaevoy` or `2606.25895`.
- `tools/novelty_grep.py` across 787 cataloged files (`watch/snapshots/**`, `hexagonmath-index.md`, `papex-index.md`, `1337-solved-conjectures`, `raghav-research-math-index.md`, `hwzw`): `"2606.25895"` = 0 hits, `"SRCII"` = 0 hits, `"Gaevoy"` = 0 hits.
- Live GitHub: `gh search prs "2606.25895"` = 0, `gh search issues "2606.25895"` = 0.
- Live arXiv API (`--no-cache`): `2606.25895v1` (`2026-06-24T14:41:30Z`) sole version.
- Zenodo (`total: 0`), ECCC (`eccc.weizmann.ac.il`), web search: only Gaevoy's paper (and Dagstuhl/LIPIcs listing of the same work); no follow-up resolving $1\text{-SRC-II}$ vs. $\mathrm{Res}$.

## Attack Log (`attack-4`)
- Started attack: `2026-11-27T19:20:31Z` (stop window: `20:20Z`–`20:50Z`).
- Gate 1 live novelty confirmed OPEN: `notes/novelty-attack.md` (`2026-11-27T19:25Z`, `0/811` snapshots, `0` GH/`trureturing`/Zenodo/HexagonMath/ECCC settlements, `2606.25895v1` sole arXiv version = MFCS 2026).
- Completed proof (`2026-11-27T19:33:08Z`): **YES — exponential separation** of $1\text{-SRC-II}$ ($\mathrm{SRC}\text{-}\mathrm{II}[1]$) from Resolution (and bounded-depth Frege). Proved completely self-contained in `PROOF.md` via guarded Tseitin formulas $\widetilde{\operatorname{Ts}}(G_n, \alpha_n) = \{C \lor \neg g : C \in \operatorname{Ts}(G_n, \alpha_n)\} \cup \{D \lor g : D \in \operatorname{All}(G_n)\}$ on bounded-degree connected expanders (Lemma 1), restriction $\widetilde{\operatorname{Ts}}|_{g=1} = \operatorname{Ts}$ (Lemma 2), Ben-Sasson–Wigderson width & size-width lower bounds giving $S_{\mathrm{Res}}(\Phi_n) = 2^{\Omega(n)}$ (Lemmas 3–4), and quadratic $1\text{-SRC-II}$ refutations of size $O(n^2)$ using $g$ as a local parity-flipping bridge along a spanning tree (Theorem 5). Verified with zero floats in `verify.py` (`PASS`, `0.097s`).
