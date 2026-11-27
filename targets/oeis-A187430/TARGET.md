# OEIS A187430: Irwin (2017) Catalan Generating Function Transform Conjecture

- **Source:** OEIS `A187430` (rev. 55), https://oeis.org/A187430
- **Status:** reported
- **Owner:** scout-5
- **Updated:** 2026-11-27T10:08Z
- **Identifiers:** `oeis:A187430`, `oeis:A000108`, `irwin-2017`

## Exact Quoted Statement

From OEIS `A187430` (NAME, COMMENTS, and FORMULA, rev. 55):

> **NAME:** Number of nonnegative walks of n steps with step sizes 1 and 2, starting and ending at 0.
>
> **COMMENTS:** Equivalently, the number of paths from (0,0) to (n,0) using steps of the form (1,2),(1,1),(1,-1) or (1,-2) and staying on or above the x-axis.
>
> **FORMULA:** Conjecture: 1 + Sum_{n>=0} a(n)*(-1)^n x^(n+1)/(1-x)^(2*n+2) = C(x), the g.f. for the Catalan numbers A000108. - _Benedict W. J. Irwin_, Jan 13 2017

## Gate 1 Novelty Receipt

Checked `2026-11-27T10:06Z`–`10:08Z`:
- `tools/novelty_grep.py A187430`: 0 lines across 0/618 files in `watch/snapshots/**`.
- Zenodo API (`https://zenodo.org/api/records?q=A187430&size=3`): `0` hits (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).
- arXiv API (`tools/arxiv_fetch.py search "A187430" 3`): `0` hits; inspected `arXiv:1609.06473v2` (`basket.tex`) directly — proves binomial formulas via kernel method, does not state or prove Irwin's identity.
- Crossref API (`https://api.crossref.org/works?query=A187430&rows=3`): `0` hits.
- GitHub (`gh search issues A187430`, `gh search prs A187430`, `gh search repos A187430`): `0` matches.
- `search_web` (`"A187430" "Irwin" OR "Catalan"`, `"1609.06473" "Catalan" OR "Irwin" OR "A187430"`, `"Baril" "Ramírez" "Knight's paths" "A187430" OR "Irwin"`): only references OEIS `A187430` where the identity remains marked `Conjecture`.
- Live OEIS `A187430` rev. 55: Irwin's 2017 conjecture has no subsequent confirmation note.
- Full check log in `notes/gate1-novelty.md`.
