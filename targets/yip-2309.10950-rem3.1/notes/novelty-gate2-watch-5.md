# Gate 2 Novelty Check — `yip-2309.10950-rem3.1` (watch-5)

- **UTC Timestamp:** `2026-11-26T22:43:03Z`
- **Target:** `targets/yip-2309.10950-rem3.1/TARGET.md`
- **Verdict:** **PASS** (no public proof or resolution of the $d=2$ case of `thm:VLM` for `GPS(q, 2)` when $q \ge 49$ is an odd square found on arXiv, Zenodo, Crossref, or local snapshots)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2309.10950 "GPS(q,2)" "van Lint-MacWilliams" "Yip"`
   - Result: 26 lines across 10 of 277 snapshot files (Asgarli–Ghioca–Yip blocking pencil / Erdős–Ingham related papers); 0 hits on `2309.10950` or `GPS(q,2)`.

2. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - Checked primary paper `2309.10950v2` (*Can. J. Math.* 78 (2026) 594–618, DOI `10.4153/S0008414X24000920`).
   - Checked recent/related papers `2611.28533v1`, `2608.02568v3`, `2607.25711v2`, `2505.04061v2`, plus 14 Chi Hoi Yip papers (2023–2026).

3. **Zenodo API (`https://zenodo.org/api/records`):**
   - Queries: `2309.10950`, `"GPS(q,2)"`, `"Chi Hoi Yip"`
   - Result: 0 hits.

4. **Crossref API (`https://api.crossref.org/works/10.4153/S0008414X24000920`):**
   - Result: `is-referenced-by-count: 2`, `update-to: None` (no retraction/corrigendum/settlement notice).

5. **Web Search (`search_web`):**
   - Searched for `"GPS(q,2)"`, `"2309.10950"`, and Yip's generalized Paley sum graph / van Lint–MacWilliams remark. Only the primary paper `2309.10950` / *Canad. J. Math.* 78 (2026) appeared.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2505.04061v2` (and related Paley/Cayley-graph papers in Yip's 2023–2026 output): Treats difference-set / Cayley graphs ($A - A \subseteq S \cup \{0\}$) rather than Cayley sum graphs `GPS(q, 2)` ($A \hat{+} A \subseteq S_2 \cup \{0\}$); does not settle the $d=2$ remark for odd squares $q \ge 49$.
- Asgarli–Ghioca–Yip snapshot hits (`novelty_grep.py`): Concern blocking sets / pencils and Erdős–Ingham problems, unrelated to $A \hat{+} A \subseteq S_2 \cup \{0\}$ in `GPS(q, 2)`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP rate limit (`HTTP 429 Too Many Requests`), so full citing-paper enumeration beyond Crossref's `is-referenced-by-count: 2` was not retrieved from OpenAlex/S2.
- Closed-access/paywalled journals not indexed in arXiv/Zenodo/Crossref metadata and private repositories.
