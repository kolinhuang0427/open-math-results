# Gate 2 Novelty Receipt — targets/ballantine-2408.13346-e2p4-rec (watch-5)

- **Checked UTC:** 2026-11-27T09:23:33Z – 2026-11-27T09:25:08Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2408.13346 Ballantine e2p4`):** `11` lines across `4/608` files — `facebookresearch/atlas-lean#10666` (unrelated 2026 Ballantine–Merca paper) and `the-omega-institute/trureturing` (`BallantineRegularSymmetricImageRefutation` + `Library/Recurrence/ballantine2024elementary.md`, verified via `gh api` to concern `arXiv:2409.11268` Conjecture 16 on `pre_j`, not `2408.13346`).
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2408.13346v1` sole version; `abs:"2408.13346"` = `0` hits; inspected abstracts of Semantic Scholar citing preprints (`2609.21922v1`, `2606.19796v1`, `2606.02683v1`, `2606.00420v3`, `2605.06706v2`, `2604.17424v1`, `2510.01100v1`, `2506.04459v2`) — none addresses the $e_2p_4(n)$ 22-term linear recurrence.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5`):** `0` hits.
4. **Live OpenAlex + Semantic Scholar:** `W4406937392` (`cited_by=9`) and S2 `9` citing papers inspected by title/abstract; none proves the `e_2p_4(n)` linear recurrence.
5. **Web search (`search_web` `"2408.13346" OR "e_2p_4(n)" ...`):** no proof of the conjectured recurrence found.

## Coverage Limits
- Non-indexed private repos or paywalled papers not mentioning `2408.13346` / `e_2p_4(n)` in indexed metadata/abstracts are not covered.
