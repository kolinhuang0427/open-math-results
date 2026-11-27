# Novelty Gate 3 Receipt — `targets/zhou-2609.23078-conj1`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T15:06:53Z` (live `1337` HEAD verified `2026-11-27T15:07:13Z`)
- **Verdict:** **PASS — OPEN (safe for `RESULTS.md` publication)**

## Freshness Verification (`<1h` before reporting)

1. **Snapshot Grep (`watch/snapshots/` across `729` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.23078" "You Zhou" "conj:main1-all-types" "maximal proper extremal subset" "extremal subset" --max-per-file 5 --max-total 60`
   - Result: `4` lines across `2/729` files — solely `watch/snapshots/arxiv/citing_papers.{json,md}` (`OpenAlex cited_by=0; S2=0` for our own `zhou-2609.23078-conj1`). Zero competing settlement hits across all tracked repos/ledgers.

2. **Live GitHub (`2026-11-27T15:06Z`–`15:07Z`):**
   - `1337isnot1337/solved-conjectures` live heads: `main = 19e230a58a91e2ceaf9ed22c01645cea61e85513` (`#1032` `results/caiolo-ferroni-hoster/`), `research = 46cbbe58f4bf7134e86d5173d13bb2423359c124` (`research/erdos-hajnal-tuza-local-transversals/`); `0` hits on You Zhou / crystal basis extremal subsets.
   - `gh search prs "2609.23078"` -> `0`; `gh search issues "2609.23078"` -> `0`.
   - `gh search code "2609.23078"` -> `13` (`12` shown: automated arXiv RSS/digest mirrors + 2 unrelated numeric/gcode hits).
   - `gh search code '"maximal proper extremal subset"'` -> `0`.
   - `gh search code 'repo:the-omega-institute/trureturing 2609.23078 OR "You Zhou"'` -> `0`.

3. **Live Zenodo, arXiv, HexagonMath, Web (`2026-11-27T15:06Z`):**
   - Zenodo API (`q=2609.23078 OR "maximal proper extremal subset"`): `0` hits.
   - arXiv API (`id_list=2609.23078`): sole version remains `arXiv:2609.23078v1` (`2026-09-19T15:20:17Z`).
   - `https://hexagonmath.org/abs/2609.23078`: HTTP `404` (`search_web` `site:hexagonmath.org` `0` hits).
   - `search_web`: no resolution of Conjecture 1 / Conjecture 4.1 (`conj:main1-all-types`) outside type $A$.

## Recommended Report Scope

- **Tier / Label:** `written proof, internally audited`
- **Verification Cmd:** `.venv/bin/python -u targets/zhou-2609.23078-conj1/notes/check-check-2.py`
- **Paths:** `targets/zhou-2609.23078-conj1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
