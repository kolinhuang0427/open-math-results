# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A178072/` (`OEIS:A178072` rev. 35, R. J. Mathar Jun 14 2016 7-term recurrence)
- **Timestamp (UTC):** `2026-11-27T11:22Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A178072`
   - Result: `0` lines across `0/652` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A178072` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A178072&fmt=json`):**
   - `A178072` rev. `35` (`2025-05-11`) still marks Mathar's Jun 14 2016 recurrence as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A178072%22`):**
   - `0` hits.
5. **Citing-Paper Check on `arXiv:2306.05025` (`S2`) & Web Search:**
   - Semantic Scholar returned `0` citations for `arXiv:2306.05025`. Web search `"A178072" conjecture OR proof OR recurrence OR Mathar` returned only OEIS links.

## Coverage Limits

- OpenAlex returned HTTP 429 on `2306.05025`; Semantic Scholar (`0` citations), OEIS, arXiv, Zenodo, web search, and snapshots are clear.
