# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/alexandersson-2609.05131-prob10.1/` (`arXiv:2609.05131v2` §10 Problem 10.1 `prob:consecutiveChowInterlacing`)
- **Timestamp (UTC):** `2026-11-27T11:42Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.05131 consecutiveChowInterlacing`
   - Result: hits only `1337-solved-conjectures/closed_issues.md` (unrelated excedance problem) and `watch/snapshots/arxiv/` citing-paper record for `2611.07267`; `0` settlement hits across `658` snapshot files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `id:2609.05131` -> `2609.05131v2` (`2026-09-23`) remains latest version.
3. **Citing-Paper Inspection (`Semantic Scholar`):**
   - Returned `1` citation: `arXiv:2611.07267v1` (Melanie Ferreri & Lucy Martinez, *Pattern avoidance classes of parking permutations with fixed lucky sets*, `2026-11-05`). Inspected HTML directly: cites `2609.05131` only in §1 background for tieless parking functions / Chow polynomial; `0` interlacing or Problem 10.1 results.
4. **GitHub, Zenodo, `mylesparslow`, & Web:**
   - `gh search issues "2609.05131"`: only `PerAlexandersson/RealRooted#665` (Theorem 3.1 Smirnov transfer, unrelated to Problem 10.1).
   - Zenodo live API (`"2609.05131"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `search_web`: `0` prior proofs.

## Coverage Limits

- OpenAlex returned HTTP 429 on `2609.05131`; Semantic Scholar (`1` citation `2611.07267`, inspected), arXiv, Zenodo, `gh search issues`, snapshots, and web search are clear.
