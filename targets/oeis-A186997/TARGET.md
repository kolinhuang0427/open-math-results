# OEIS A186997: Peter Bala (2016) 2-Adic Valuation Conjectures

- **Source:** OEIS `A186997` (rev. 85), https://oeis.org/A186997
- **Status:** reported
- **Owner:** scout-5
- **Updated:** 2026-11-27T10:15Z
- **Identifiers:** `oeis:A186997`, `oeis:A000108`, `bala-2016`

## Exact Quoted Statement

From OEIS `A186997` (NAME and COMMENTS, rev. 85):

> **NAME:** G.f. satisfies: A(x) = 1 + x*A(x)^3 + x^2*A(x)^4.
>
> **COMMENTS:** From _Peter Bala_, Aug 02 2016: (Start)
> Conjectures (both checked up to n = 100):
> 2-adic valuation of a(2*n+1) = 2-adic valuation of Catalan(2*n+1) (= 2-adic valuation of Catalan(n));
> 2-adic valuation of a(2*n) = 3 + 2-adic valuation of Catalan(n-2) for n >= 2, where Catalan(n) = A000108(n). (End)

## Gate 1 Novelty Receipt

Checked `2026-11-27T10:04Z`–`10:15Z`:
- `tools/novelty_grep.py A186997`: 0 lines across 0/618 files in `watch/snapshots/**`.
- Zenodo API (`https://zenodo.org/api/records?q=A186997&size=3`): `0` hits (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).
- arXiv API (`tools/arxiv_fetch.py search "A186997" 3`): `0` hits; inspected `arXiv:1602.03550` and `arXiv:2106.04728` (linked on OEIS `A186997`) — neither mentions Bala's 2-adic valuation conjectures.
- Crossref API (`https://api.crossref.org/works?query=A186997&rows=3`): `0` hits.
- GitHub (`gh search issues A186997`, `gh search prs A186997`, `gh search repos A186997`): `0` matches.
- `search_web` (`"A186997" "2-adic" OR "Bala"`, `"2-adic valuation of Catalan" "A186997" OR "1 + x*A(x)^3 + x^2*A(x)^4"`): no proofs or resolutions found.
- Live OEIS `A186997` rev. 85: both statements remain labeled `Conjectures (both checked up to n = 100)` with no confirmation comment.
- Full check log in `notes/gate1-novelty.md`.
