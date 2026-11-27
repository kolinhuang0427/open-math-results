# Gate 2 Novelty Check — `kovalyov-2611.32205-q1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T16:59:26Z`–`2026-11-27T16:59:38Z`
- **Target:** `targets/kovalyov-2611.32205-q1/` — Konstantin Kovalyov, *"Some conservativity results for weak arithmetic theories in a language with exponentiation"* (`arXiv:2611.32205v1`, `2026-11-24`), Section 3 Question 3.4(1)–(2) (`\mathrm{IOpen}+(\mathrm{Exp})` conservativity over `\mathrm{IOpen}` / `\mathcal{L}_{\mathrm{OSR}}`-fragment)
- **Claimed result:** **YES** (`\mathrm{IOpen}+(\mathrm{Exp})` is conservative over `\mathrm{IOpen}` and its `\mathcal{L}_{\mathrm{OSR}}`-fragment is `\mathrm{IOpen}`, proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.32205" "Kovalyov" "IOpen" "OSR" "Z-DOSR"`):**
   - `0` hits on `2611.32205`, `Kovalyov`, or `Z-DOSR` across `744` snapshot files; `IOpen` hits solely unrelated substrings (`MultiOpenBoundaryInfluence`, `TribonacciOpenPathGap`, `LatticeSectorFullIOPentagon`).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T16:59:26Z`):**
   - `main` = `5bd689f8b7cc6fc058ccd55f49ef4599630add43` (`2026-11-27T16:57:49Z`, PR `#1064`, Bourin's inequality) — unrelated.
   - `research` = `b001136403fb9bbb84bfc80a8c8f9bd71f754483` (`2026-11-27T16:58:56Z`, Bourin local validity) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.32205"` -> `0` hits (`[]`).
   - `gh search issues "2611.32205"` -> `0` hits (`[]`).
   - `gh search code "2611.32205"` -> `ehijano/rss_fetch` RSS XML, `yizhuan/research-radar` daily trending arXiv JSON, plus unrelated Linux dmesg / timestamp / TSV numeric collisions; `0` solution repositories.
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2611.32205`) -> sole version `2611.32205v1` (`2026-11-24T08:51:14Z`).
   - Zenodo API (`q=2611.32205`) -> `0` hits.
   - Web search -> only Kovalyov's `arXiv:2611.32205` paper and earlier OUP/arXiv logic work; no resolution of Section 3 Question 3.4(1)–(2).

## Coverage Limits
- Covers `watch/snapshots` (`744` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and public web search as of `2026-11-27T16:59:38Z`; private repositories and non-indexed preprints remain unobservable.
