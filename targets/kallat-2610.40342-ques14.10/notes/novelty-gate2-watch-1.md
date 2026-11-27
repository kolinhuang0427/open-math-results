# Novelty Gate 2 Receipt — `targets/kallat-2610.40342-ques14.10`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T14:41:01Z`
- **Verdict:** **PASS — OPEN (no prior settlement of Question 14.10 `prob:gcdr` found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `721` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.40342" "Kallat" "prob:gcdr" "global gcd" "valuation calculus" --max-per-file 5 --max-total 60`
   - Result: `10` lines across `6/721` files — none touching Question 14.10 (`prob:gcdr`):
     - `the-omega-institute__trureturing/files.txt` (`kallat2026weightedpermutations.md` -> `arXiv:2610.15849v1` / OEIS A378495).
     - `arxiv/citing_papers.{json,md}` (`OpenAlex cited_by=0; S2=0`).
     - `formal/formal-conjectures-prs.{json,tsv}` (`#8038` -> Peter Bala / OEIS A012780).
     - `1337-solved-conjectures` snapshot `grep`: `0` matches for `kallat|2610.40342|g_3|g_r`.

2. **Live GitHub (`2026-11-27T14:41Z`):**
   - `gh search prs "2610.40342"` -> `0` matches.
   - `gh search issues "2610.40342"` -> `3` matches (`bguanmath/ArXiv_MathNT` `#437–#439` arXiv digest issues only).
   - `gh search code "2610.40342"` -> `50` matches (`top 25` shown):
     - `rainwangphy/aftd-platform` (`lean/AFTD/Kb/NumberTheory/RestrictedCycle*.lean`, `OP-746`): formalizes definitions and published helper lemmas (Theorem 5.1, Proposition 11.3(i)) and explicitly states *"No novelty claim; the uniform conjecture in Question 14.10 remains open"*. Live repo-scoped code search for `"111" OR "1248" OR "Lambda_r" OR "mod 81"` in `rainwangphy/aftd-platform` returned `0` matches.
     - `mathesis-papers/10.5281-zenodo.23903308` -> OEIS A378495 (`Theorem 4.1 / r=1` only).
     - `chokmah-me/fragile-proof-audit` -> harvest audit of `2610.40342` only.
     - `isLinXu/paper-list`, `ehijano/rss_fetch`, `LarsSivertsen/xeos_python` -> lists/RSS/numeric logs.
   - `gh search code 'repo:the-omega-institute/trureturing Kallat OR 2610.40342'` -> `0` matches.

3. **Live Zenodo, arXiv, Web (`2026-11-27T14:41Z`):**
   - Zenodo API `q=2610.40342` -> `0` hits (`23903309` / `23886386` / `24161993` from broad keyword search are unrelated to `prob:gcdr`).
   - arXiv API (`id_list=2610.40342`): sole version remains `arXiv:2610.40342v1` (`2026-10-29T16:04:37Z`); no `v2`.
   - `search_web`: only `arXiv:2610.40342v1` itself; no settlement of Question 14.10 (`prob:gcdr`) found.

## Coverage Limits

- Live Semantic Scholar / OpenAlex APIs remained rate-limited (`429`, covered by snapshot `citing_papers.md` `cited_by=0`). Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
