# Gate 3 Novelty Check — `kovalyov-2611.32205-q1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:21:46Z`–`2026-11-27T17:22:03Z`
- **Target:** `targets/kovalyov-2611.32205-q1/` — Konstantin Kovalyov, *"Some conservativity results for weak arithmetic theories in a language with exponentiation"* (`arXiv:2611.32205v1`, `2026-11-24`), Section 3 Question 3.5(1)–(2) (`\mathsf{IOpen}+(\mathrm{Exp})` conservative over `\mathsf{IOpen}`, `\mathcal{L}_{\mathrm{OSR}}`-fragment is `\mathsf{IOpen}`)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**YES**)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/kovalyov-2611.32205-q1/notes/check-check-2.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.32205" "Kovalyov"`):**
   - `1` line across `1/745` files (`watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt` -> `Library/notes/derkachkovalyov2017indefinitestieltjes.md`, unrelated); `0` hits on `2611.32205` or Question 3.5.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:21:46Z`):**
   - `main` = `11641cdc821520c75001b9c07ee3b8d517bac201` (`2026-11-27T17:21:09Z`, PR `#1069`, Bourin crossed-Heinz gap) — unrelated.
   - `research` = `4f22969d17348dcd0ed052e8c304e6ced7ed5f76` (`2026-11-27T17:20:57Z`, single-stage lemma) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.32205"` -> `0` hits (`[]`).
   - `gh search issues "2611.32205"` -> `0` hits (`[]`).
   - `gh search code "Kovalyov" "IOpen"` -> `ehijano/rss_fetch` RSS XML, `yizhuan/research-radar` daily feed, `FormalizedFormalLogic/AlphaCentauri/references.yml` (verified via `gh api`: cites prior 2024 article *"Fragments of IOpen"* only), plus unrelated repos; `0` resolutions of `2611.32205` Question 3.5.
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2611.32205`) -> sole version `2611.32205v1` (`2026-11-24T08:51:14Z`).
   - Zenodo API (`q=2611.32205`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Kovalyov's `2026` paper.
   - Web search -> only Kovalyov's `arXiv:2611.32205` preprint; `0` resolutions of Question 3.5(1)–(2).
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/kovalyov-2611.32205-q1/notes/check-check-2.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:22:03Z`; private repositories and non-indexed preprints remain unobservable.
