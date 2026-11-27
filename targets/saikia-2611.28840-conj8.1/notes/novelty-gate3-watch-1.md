# Novelty Gate 3 Receipt — `targets/saikia-2611.28840-conj8.1`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T16:17:17Z` (live `1337` HEAD verified `2026-11-27T16:17:34Z`)
- **Verdict:** **PASS — OPEN (safe for `RESULTS.md` publication)**

## Freshness Verification (`<1h` before reporting)

1. **Snapshot Grep (`watch/snapshots/` across `742` files, incl. `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`, `hexagonmath-index.md`, `papex-index.md`):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.28840" "Saikia" "conj:sharp" --max-per-file 5 --max-total 60`
   - Result: `23` lines across `10/742` files — zero full settlements:
     - `raghav-research-math-index.md:1696`: explicitly lists `2611.28840` under `not attempted (budget)`.
     - `the-omega-institute__trureturing/issues_and_prs.txt:351` (`trureturing#34564`): finite range `12 <= k <= 32` only (`k >= 33` explicitly open).
     - `arxiv/{arxiv_submissions.*,citing_papers.*,last_sweep_report.*,state.json}` (`OpenAlex cited_by=0; S2=0`).
     - `hexagonmath-index.md:5583` (`2610.00469` unrelated); `facebookresearch__atlas-lean` (`INTEGERS 2025` unrelated).

2. **Live GitHub (`2026-11-27T16:17Z`):**
   - `1337isnot1337/solved-conjectures` live heads: `main = 5f4b237d5d4f1a27aae25a60c719ff4e6f217399` (`#1050` `results/erdos-galvin-hajnal-link-path-partition/`), `research = fabf94f42440b3fd1f6d8a304b69ddbbb4e115ad` (`research/stanley-tree-isomorphism/`); `0` Saikia / `PDO_t` matches.
   - `gh search prs "2611.28840"` -> `0`; `gh search issues "2611.28840"` -> `0`.
   - `gh search code "2611.28840"` -> `13` matches: `jmadeiros/conjecture-desk` (`yaqubi-mirzavaziri/` only notes `2611.28840` is distinct `PDO_t`), `raghavs1729/Research-Math` (`not attempted (budget)`), daily arXiv RSS/digest mirrors, and unrelated numeric CSVs.
   - `gh api repos/the-omega-institute/trureturing/issues/34564`: unchanged (`state: open`, `comments: 3`, `updated_at: 2026-11-26T17:50:01Z`, finite `12 <= k <= 32` only); `gh search prs --repo the-omega-institute/trureturing '34564 OR Saikia OR 2611.28840'` -> `0`.

3. **Live Zenodo, arXiv, Web (`2026-11-27T16:17Z`):**
   - Zenodo API (`q=2611.28840`): `0` hits.
   - arXiv API (`id_list=2611.28840`): sole version remains `arXiv:2611.28840v1` (`2026-11-21T14:45:07Z`).
   - `search_web`: only `arXiv:2611.28840v1` itself surfaced; no settlement of Conjecture 8.1 for all $k \ge 3$.

## Recommended Report Scope

- **Tier / Label:** `written proof, internally audited`
- **Verification Cmd:** `.venv/bin/python -u targets/saikia-2611.28840-conj8.1/notes/check-check-3.py`
- **Paths:** `targets/saikia-2611.28840-conj8.1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
