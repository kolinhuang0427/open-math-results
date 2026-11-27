# Gate 3 Novelty Receipt (`watch-1`): `targets/lau-2208.14707-conj2/`

- **Checked UTC:** `2026-11-27T09:24Z`
- **Target:** Gee-Choon Lau, Wai-Chee Shiu, K. Premalatha, Ruixue Zhang, and M. Nalliah, *"A note on local antimagic chromatic number of lexicographic product graphs"*, `arXiv:2208.14707v1` (*Discrete Math. Lett.* 11 (2023), 76–83, `DOI:10.47443/dml.2022.149`), Section 2, **Conjecture 2.2**
- **Audited Artifacts Verified:** `TARGET.md`, `COUNTEREXAMPLE.md`, `AUDIT.md` (`@audit-2` re-audit PASS `2026-11-27T09:22Z`), cmd `.venv/bin/python targets/lau-2208.14707-conj2/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2208.14707`):** `0` hits across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2408.13346,2208.14707`):** `2208.14707v1` (`2022-08-31T09:13:32Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2208.14707&size=5`):** `0` hits.
4. **Prior Gate 2 checks (`09:14Z`):** OpenAlex on `10.47443/dml.2022.149` (`cited_by_count: 0`, confirmed in `AUDIT.md` §2.4), `gh search issues` `0`, web search `0` refutations.
