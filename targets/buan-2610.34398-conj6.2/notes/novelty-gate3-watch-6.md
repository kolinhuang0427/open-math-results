# Gate 3 (<1h) Live Novelty Receipt (`watch-6`) — `targets/buan-2610.34398-conj6.2/`

- **Checked UTC:** `2026-11-27T11:52:43Z`–`2026-11-27T11:53:05Z`
- **Target:** Buan–Hanson–Marsh, *Lifting $\tau$-exceptional sequences*, `arXiv:2610.34398v1` (2026-10-25), Section 7.1, **Conjecture 7.2** (`\label{conj:TFordered}`; legacy slug `targets/buan-2610.34398-conj6.2/`).
- **Audit Status:** `@audit-1` **PASS** (`AUDIT.md`, `#1351`, `check-check-2.py` zero-float PASS across 434 TF-ordered sequences).
- **Verdict:** **OPEN / CLEAR FOR GATE 5 REPORTING**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `689` Sweep 6 snapshot files):**
   - `2610.34398` -> **`0` hits** (`0/689`).
   - `TF-ordered` -> **`0` hits** (`0/689`).
   - `conj:TFordered` -> **`0` hits** (`0/689`).
   - `Lifting \tau-exceptional` -> **`0` hits** (`0/689`).
   - `Buan` -> **`0` hits** (`0/689`). *(Note: standalone `Hanson` only hits unrelated `Lambie-Hanson` set-theory entries.)*
2. **Live arXiv (`export.arxiv.org/api/query`):**
   - `id_list=2610.34398` -> sole entry `http://arxiv.org/abs/2610.34398v1` (`updated: 2026-10-25T15:59:39Z`, *Lifting $\tau$-exceptional sequences*); no `v2` or erratum.
   - `search_query=all:"TF-ordered"+OR+all:2610.34398` -> `3` entries (`2610.34398v1`, `2501.13694v1` older 2025 paper, `2410.01963v1` older 2024 paper); `0` follow-up papers settling Conjecture 7.2.
3. **GitHub Live Search (`gh` CLI):**
   - `gh search code 2610.34398` -> RSS/feed mirrors (`ehijano/rss_fetch`, `koutya0akari/arxiv-plug-in-for-mixi2`) plus numeric substring hits in non-math datasets, `0` proof files.
   - `gh search code '"TF-ordered"'` -> `0` math proofs (Terraform/AI prompt keyword noise + unrelated older repo `terland/tau/notes/tau-exceptional sequences`).
   - `gh search code '"conj:TFordered"'` -> `[]`.
   - `gh search repos "2610.34398"` -> `[]`; `gh search repos "TF-ordered"` -> `0` math repos (Terraform/Wikipedia search engine noise).
   - `gh search issues "2610.34398"` -> `[]`.
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` (filtered `2610|34398|buan|tf.?ordered`) -> `0_HITS`.
4. **Live Zenodo & Web Search:**
   - `zenodo.org/api/records?q=2610.34398` -> `0` hits.
   - `zenodo.org/api/records?q="TF-ordered"` -> `0` hits.
   - `search_web` (`"2610.34398" OR ("TF-ordered" "Buan" "Hanson" "Marsh")`) -> returns solely the `2610.34398` arXiv paper and White Rose repository metadata; `0` follow-up proofs.

## Coverage Limits

- Unindexed private repositories or behind-paywall preprints not surfaced by arXiv, Zenodo, GitHub search, or web search remain out of scope; all public channels searched confirm `arXiv:2610.34398v1` Conjecture 7.2 (`\label{conj:TFordered}`) remains open.
