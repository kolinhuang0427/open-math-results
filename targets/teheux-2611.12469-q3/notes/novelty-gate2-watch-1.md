# Novelty Gate 2 Receipt — `targets/teheux-2611.12469-q3`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T14:12:27Z`
- **Verdict:** **PASS — OPEN (no prior settlement of Question 8.4(3) `q:correspondence` found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `721` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.12469" "Teheux" "q:correspondence" "median algebra" "poc-set" --max-per-file 5 --max-total 60`
   - Result: `16` lines across `6/721` files — solely `watch/snapshots/arxiv/` feed/target entries for `2611.12469v1`. Zero hits in `1337-solved-conjectures`, `trureturing`, `hwzw-algebra-number-theory-drafts`, `insorrowmeow`, `mylesparslow`, or `openai-math`.

2. **Live GitHub (`2026-11-27T14:12Z`):**
   - `gh search prs "2611.12469"` -> `0` matches.
   - `gh search issues "2611.12469"` -> `1` match: `the-omega-institute/trureturing#29092` (verified live via `gh api`: `state: open`, `comments: 0`, created/updated `2026-11-11T02:10:13Z`, scoped solely to Question 8.4(2) second sentence `ST(\sigma)`, explicitly stating *"does not solve the other parts of Question 8.4"*).
   - `gh search code "2611.12469"` -> `5` matches (`ehijano/rss_fetch` RSS feeds, `koutya0akari` arXiv tracker, unrelated numeric coord).
   - `gh search code '"Dualities and completions of median algebras"'` -> `0` matches.
   - `gh search code 'repo:the-omega-institute/trureturing Teheux'` -> `0` matches.

3. **Live arXiv, Zenodo, Web:**
   - arXiv API (`id_list=2611.12469`): sole version remains `arXiv:2611.12469v1` (`2026-11-09T14:19:48Z`).
   - Zenodo API (`2611.12469 OR "Dualities and completions of median algebras" OR ("median algebras" "profinite completion")`): `22` hits (`top 10` inspected: `18252933` etc. — generic equational theory / music / profinite group records; `0` for `2611.12469` or Teheux median algebras per `notes/novelty-attack.md`).
   - `search_web`: queries for `"2611.12469"`, `"Dualities and completions of median algebras" "Teheux"`, and `"median algebra" "profinite completion" "finite subalgebra"` returned only `arXiv:2611.12469v1` itself; no settlement of Question 8.4(3).

## Coverage Limits

- Unauthenticated Semantic Scholar and OpenAlex APIs remained rate-limited (covered by `notes/novelty-attack.md` + snapshot `citing_papers.md` `cited_by=0`). Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
