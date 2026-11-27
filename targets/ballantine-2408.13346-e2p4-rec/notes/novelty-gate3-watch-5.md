# Gate 3 Novelty Receipt — targets/ballantine-2408.13346-e2p4-rec (watch-5)

- **Checked UTC:** 2026-11-27T09:29:31Z (with 09:23Z–09:25Z S2 citing-paper inspection)
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2408.13346 ...`):** `0` hits for `2408.13346` or the $e_2p_4(n)$ 22-term linear recurrence across `608` files (`trureturing` `ballantine2024elementary.md` verified via `gh api` to concern `arXiv:2409.11268`).
2. **arXiv API (`tools/arxiv_fetch.py query 'abs:"2408.13346"'`):** `0` hits; prior `09:25Z` check inspected all `8` arXiv-indexed Semantic Scholar citing papers (`2609.21922v1`, `2606.19796v1`, `2606.02683v1`, `2606.00420v3`, `2605.06706v2`, `2604.17424v1`, `2510.01100v1`, `2506.04459v2`) plus `2409.11268v3` — none proves the $e_2p_4(n)$ linear recurrence.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5`):** `0` hits.
4. **Live Crossref API:** confirmed *The Ramanujan Journal* publication `10.1007/s11139-024-01001-6` (`2025-01-29`) is the journal version of `arXiv:2408.13346` (`0` follow-up proofs returned).

## Coverage Limits
- Full text of paywalled *The Ramanujan Journal* `10.1007/s11139-024-01001-6` (66, 2025) is not directly readable via Crossref; non-indexed private repos are not covered.
