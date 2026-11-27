# Novelty Gate 2 Receipt — `targets/schneider-2611.20267-q7.4`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T14:47:40Z`
- **Verdict:** **PASS — OPEN (no prior settlement of Question 7.4 found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `725` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.20267" "Schneider" "q:7.4" "Question 7.4" --max-per-file 5 --max-total 60`
   - Result: `12` lines across `7/725` files — all `Schneider` hits are unrelated (Gelfond–Schneider, Grauert–Riemenschneider, Barth–Schneider, Samuel Schneider); `0` hits for `2611.20267` or Scott Schneider.

2. **Live GitHub (`2026-11-27T14:47Z`):**
   - `gh search prs "2611.20267"` -> `0`; `gh search prs '"Borel combinatorics"'` -> `0`.
   - `gh search issues "2611.20267"` -> `0`; `gh search issues '"2611.20267" OR ("Scott Schneider" hypersmooth)'` -> `0`.
   - `gh search code "2611.20267"` -> `10` hits, all unrelated numeric collisions in CSV/JSON files (`dataset_maestro.csv`, `VaxModel-paper`, `flight-mh370-revisited`).
   - `gh search code '"hypersmooth equivalence relations" "Schneider"'` -> `0` matches.
   - `gh search code 'repo:the-omega-institute/trureturing "2611.20267"'` -> `0` matches.

3. **Live Zenodo, arXiv, Web (`2026-11-27T14:47Z`):**
   - Zenodo API (`q=2611.20267`) -> `0` hits; (`q="Borel combinatorics of" hypersmooth`) -> `1` unrelated robotics document (`17768652`, *CollectiveOS Exobody Node Program*, `2025-11-30`).
   - arXiv API (`id_list=2611.20267`): sole version remains `arXiv:2611.20267v1` (`2026-11-15T21:47:51Z`).
   - `search_web`: queries for `"2611.20267"`, `"Question 7.4"`, `"Borel combinatorics of" "hypersmooth equivalence relations"`: no settlement of Question 7.4 found.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs remained rate-limited externally. Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
