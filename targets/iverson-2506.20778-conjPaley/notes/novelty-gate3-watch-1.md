# Gate 3 Novelty Receipt (`watch-1`): `targets/iverson-2506.20778-conjPaley/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Target:** Joseph W. Iverson and Dustin G. Mixon, *"Asymmetric SICs over finite fields"*, `arXiv:2506.20778v1` (`2025-06-25`), Section 4, Conjecture 22 (`\label{conj:Paley}`)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-2` re-audit PASS `2026-11-27T09:16Z`), cmd `.venv/bin/python -u targets/iverson-2506.20778-conjPaley/notes/check-check-1.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2506.20778 "Iverson" "Asymmetric SIC" "conj:Paley"`):** `8` lines across `5/608` files: only `watch/snapshots/arxiv/citing_papers.{json,md}` indexing this target itself (`OpenAlex cited_by=0; S2=None`), plus unrelated 2021 Greaves–Iverson–Jasper–Mixon records in `the-omega-institute/trureturing*`. `0` hits in `1337isnot1337/solved-conjectures` (`08:49Z` rebuild) or any competing repo.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2407.20048,2506.20778`):** `2506.20778v1` (`2025-06-25`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2506.20778&size=10`):** `0` hits.
4. **Web search (`"2506.20778" OR "Asymmetric SICs over finite fields" "conj:Paley"`):** Surfaced only `arXiv:2506.20778` itself; `0` settlements found.

## Coverage Limits
- OpenAlex (`HTTP 429`) and GitHub Search API `gh search issues/prs "2506.20778"` (`HTTP 403` rate limit) did not return live search results during this check; mitigated by `608`-file `watch/snapshots/**` grep (covering `1337isnot1337/solved-conjectures` rebuilt `08:49Z`, `trureturing`, `openai/math`, and `citing_papers.json`) plus live arXiv, Zenodo, and web search.
