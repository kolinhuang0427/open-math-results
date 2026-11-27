# Novelty Gate 2 Receipt — `targets/zhou-2609.23078-conj1`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T14:45:13Z`
- **Verdict:** **PASS — OPEN (no prior settlement outside type $A$ found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `721` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.23078" "You Zhou" "conj:main1-all-types" "maximal proper extremal subset" "extremal subset" --max-per-file 5 --max-total 60`
   - Result: `0 lines across 0/721 files in 0.89s`. Zero matches across `1337-solved-conjectures`, `hwzw-algebra-number-theory-drafts`, `insorrowmeow`, `mylesparslow`, `openai-math`, `discovered`, `formal`, or `arxiv` sweeps.

2. **Live GitHub (`2026-11-27T14:45Z`):**
   - `gh search prs "2609.23078"` -> `0` matches.
   - `gh search issues "2609.23078"` -> `0` matches.
   - `gh search code "2609.23078"` -> `13` matches (`12` shown: automated `LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `ehijano/rss_fetch`, `koutya0akari/arxiv-plug-in-for-mixi2` mirrors + 2 unrelated numeric/gcode hits).
   - `gh search code '"maximal proper extremal subset"'` -> `0` matches (`gh search code "maximal proper extremal subset"` in `notes/novelty-attack.md` matched only the same arXiv RSS/digest mirrors).
   - `gh search code 'repo:the-omega-institute/trureturing 2609.23078 OR "You Zhou"'` -> `0` matches.

3. **Live Zenodo, arXiv, Web (`2026-11-27T14:45Z`):**
   - Zenodo API (`q=2609.23078 OR "maximal proper extremal subset"`): `0` hits (`total: 0`).
   - arXiv API (`id_list=2609.23078`): sole version remains `arXiv:2609.23078v1` (`2026-09-19T15:20:17Z`).
   - `search_web`: queries for `"2609.23078"`, `"maximal proper extremal subset" "crystal basis"`, `"You Zhou" "extremal subset"`, `"Kashiwara" "extremal subset"` found only `arXiv:2609.23078v1` itself (proved in type $A$, open for general types).

## Coverage Limits

- Live Semantic Scholar / OpenAlex APIs remained rate-limited (`429` recorded in `notes/novelty-attack.md`). Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
