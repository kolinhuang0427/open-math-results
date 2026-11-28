# Gate 2 Novelty Check — `gaevoy-2606.25895-src2-1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T19:34:14Z`–`2026-11-27T19:34:46Z`
- **Target:** `targets/gaevoy-2606.25895-src2-1/` — Nikita Gaevoy, *"The Power of Small Symmetries"* (`arXiv:2606.25895v1`, `2026-06-24`; MFCS 2026 LIPIcs Vol. 386, Art. 97, `DOI:10.4230/LIPIcs.MFCS.2026.97`), §§ 2 & 6 ($\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs Resolution)
- **Claimed result:** **YES — exponential separation** of $1\text{-SRC-II}$ ($\mathrm{SRC}\text{-}\mathrm{II}[1]$) from Resolution and bounded-depth Frege via guarded Tseitin formulas $\widetilde{\operatorname{Ts}}(G_n, \alpha_n)$ (`PROOF.md`, zero-float `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.25895" "Gaevoy" "SRC-II" "SRCII"`):**
   - `0` lines across `0/811` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T19:34:14Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `68951fa0c7c192ac9922e7413d67911f8e3ff3ee` (`2026-11-27T19:32:03Z`, countable edge-Ramsey witnesses) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.25895"` -> `0` hits (`[]`).
   - `gh search issues "2606.25895"` -> `0` hits (`[]`).
   - `gh search code "2606.25895"` -> June 2026 arXiv RSS/digest mirrors (`Lyken17/arXiv-stats`, `qiao-925/news-digest`, `ehijano/rss_fetch`, `claudlos/carlos-debrief`) + unrelated numeric CSV/JSON collisions only.
   - `gh search code '"SRC-II" "Resolution"'` -> `0` hits (`[]`); `gh search code "SRCII[1]"` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2606.25895`) -> sole version `2606.25895v1` (`2026-06-24T14:41:30Z`).
   - Zenodo API (`q=2606.25895`) -> `0` hits.
   - Crossref (`10.4230/LIPIcs.MFCS.2026.97`) -> empty/not indexed (`0` hits for title query).
   - `search_web` -> only Gaevoy's `arXiv:2606.25895` / Dagstuhl LIPIcs MFCS 2026 paper (`0` resolutions of $\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs Resolution).

## Coverage Limits
- Covers `watch/snapshots` (`811` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and `search_web` as of `2026-11-27T19:34:46Z`; Crossref has not indexed `10.4230/LIPIcs.MFCS.2026.97`, and private repositories / non-indexed preprints remain unobservable.
