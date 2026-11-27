---
source: OEIS A119262 (rev. 55), https://oeis.org/A119262
status: reported
owner: scout-5
updated: 2026-11-27T10:25Z
identifiers:
  - oeis:A119262
  - irwin-2017
---

# OEIS A119262: Benedict W. J. Irwin (2017) Hessenberg Determinant Conjecture

## Exact Quoted Statement

From OEIS `A119262` (NAME and FORMULA, rev. 55):

> **NAME:** Number of B-trees of order infinity with n leaves, where a(n) = Sum_{k=1..floor(n/2)} a(k)*C(n-k-1,n-2*k) for n >= 2, with a(0)=0, a(1)=1.
>
> **FORMULA:** Conjecture: Let M_n be an n X n matrix whose elements are m_ij = 0 for i < j - 1, m_ij = -1 for i = j - 1, and m_ij = binomial(i - j, n - i) otherwise. Then a(n + 1) = Det(M_n). - _Benedict W. J. Irwin_, Apr 19 2017

## Gate 1 Novelty Receipt

Checked `2026-11-27T10:22Z`–`10:25Z`:
- `tools/novelty_grep.py A119262`: 0 lines across 0/618 files in `watch/snapshots/**`.
- Zenodo API (`https://zenodo.org/api/records?q=A119262&size=3`): `0` hits (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).
- arXiv API (`tools/arxiv_fetch.py search "A119262" 3`): `0` hits.
- Crossref API (`https://api.crossref.org/works?query=A119262&rows=3`): `0` hits.
- GitHub (`gh search issues A119262`, `gh search prs A119262`, `gh search repos A119262`): `0` matches.
- `search_web` (`"A119262" "Det(M_n)" OR "m_ij = binomial" OR "Irwin"`): no proofs or resolutions found for `A119262`.
- Live OEIS `A119262` rev. 55: Irwin's Apr 19 2017 formula remains prefixed with `Conjecture:` with no confirmation note.
- Full check log in `notes/gate1-novelty.md`.
