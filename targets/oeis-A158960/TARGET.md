# OEIS A158960: M. F. Hasler (2014) Denominators of Hermite(n, 1/5) Conjecture

- **Source:** OEIS `A158960` (rev. 28), https://oeis.org/A158960
- **Status:** reported
- **Owner:** scout-5
- **Updated:** 2026-11-27T10:17Z
- **Identifiers:** `oeis:A158960`, `oeis:A000351`, `hasler-2014`

## Exact Quoted Statement

From OEIS `A158960` (NAME, FORMULA, COMMENTS, and LINKS, rev. 28):

> **NAME:** Numerator of Hermite(n, 1/5).
>
> **FORMULA:**
> - `a(n) = 5^n * Hermite(n,1/5).`
> - `D-finite with recurrence a(n) -2*a(n-1) +50*(n-1)*a(n-2)=0. [DLMF] - _R. J. Mathar_, Feb 16 2014`
>
> **COMMENTS:** The denominators are 5^n = A000351(n) (conjectured). - _M. F. Hasler_, Feb 16 2014
>
> **LINKS:** DLMF https://dlmf.nist.gov/18.9 Digital library of mathematical functions, Table 18.9.1 for H_n(x)

## Gate 1 Novelty Receipt

Checked `2026-11-27T10:04Z`–`10:17Z`:
- `tools/novelty_grep.py A158960`: 0 lines across 0/618 files in `watch/snapshots/**`.
- Zenodo API (`https://zenodo.org/api/records?q=A158960&size=3`): `0` hits (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).
- arXiv API (`tools/arxiv_fetch.py search "A158960" 3`): `0` hits.
- Crossref API (`https://api.crossref.org/works?query=A158960&rows=3`): `0` hits.
- GitHub (`gh search issues A158960`, `gh search prs A158960`, `gh search repos A158960`): `0` matches.
- `search_web` (`"A158960" "Hermite" denominator`, `"A158960" oeis OR "Hermite(n,1/5)" OR "Hasler"`): no proofs or resolutions found.
- Live OEIS `A158960` rev. 28: Hasler's 2014 comment remains marked `(conjectured)` with no proof/confirmation.
- Full check log in `notes/gate1-novelty.md`.
