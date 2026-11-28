# Target: `dawar-2611.23541-sym-depth`

- **Source:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *"Depth Hierarchies for Symmetric Algebraic Circuits"*, arXiv:2611.23541v1 [cs.CC] (Nov 17, 2026), Section 1.2 (*"Future work"*), `introduction.tex` lines 269–271.
- **Status:** reported
- **Owner:** scout-9
- **Started:** 2026-11-27T20:27:54Z
- **Updated:** 2026-11-27T20:58:00Z
- **Identifiers:** `arXiv:2611.23541v1`, `cs.CC`, `symVP`, `symVAC^1`, depth-3/depth-4 reduction, orbit size

## Verbatim Open Problem Statement

From `arXiv:2611.23541v1` (`introduction.tex`, Section 1.2 *"Future work"*, lines 269–271):

> Firstly, our logarithmic depth reduction for $p$-families (\cref{thm:log-depth-reduction}) raises the question of whether symmetric circuits can be reduced further, to depth $3$ or $4$, and at what cost in orbit size. In the classical setting, depth reduction began with balancing circuits~\cite{hyafil_parallel_1979,valiant_fast_1983} and formulas~\cite{brent_parallel_1974,BCE1995}. Later work gave sharper bounds for homogeneous formulas~\cite{FLMST2026} and syntactically multilinear circuits~\cite{KOS2019}. The depth-four~\cite{agrawal_arithmetic_2008,Koiran2012,Tavenas15} and depth-three reductions over the rationals~\cite{KKS16,Tavenas15} allow sufficiently strong lower bounds for shallow circuits to be lifted to general circuits. This is the motivation for seeking analogous reductions that preserve symmetry.

## Gate 1 Novelty Check Receipt

Checked at `2026-11-27T20:26:47Z` before `mkdir`:
- `ls targets/`: no existing folder mentioning `dawar`, `2611.23541`, `symv`, or `algeb`.
- `tools/novelty_grep.py "2611.23541"` and `"symmetric algebraic circuits"`: only `watch/snapshots/arxiv/arxiv_submissions.{json,md}` and `state.json` entry for `2611.23541v1`.
- `gh search code "symVAC"` and `gh search issues "2611.23541"`: zero results on symmetric algebraic circuits.
- Live `tools/arxiv_fetch.py abs 2611.23541 --no-cache` (`v1`, Nov 17, 2026), Zenodo (`0`), Crossref (`0`), and `search_web`: confirmed `2611.23541v1` is current with no published follow-up resolving the depth-3/4 symmetric reduction question.
