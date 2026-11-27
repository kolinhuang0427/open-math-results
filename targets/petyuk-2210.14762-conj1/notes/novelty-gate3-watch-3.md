# Gate 3 Novelty Receipt (`watch-3`) — `targets/petyuk-2210.14762-conj1/`

- **Checked (UTC):** `2026-11-27T03:34:54Z` – `2026-11-27T03:52:15Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Petyuk `arXiv:2210.14762v2` Conjecture 1: non-word-representability of simplified de Bruijn graphs $S(n,k)$ for $n \ge 4, k \ge 3$)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py "2210.14762" Petyuk "simplified de Bruijn"`):**
   - Only `watch/snapshots/arxiv/citing/petyuk-2210.14762-conj1.json` and `watch/snapshots/arxiv/openalex_works_cache.json` metadata records for `2210.14762` itself (`0` hits across `watch/snapshots/ai-collections/` `54,475` files / `297` issues+PRs as of `2026-11-27T03:50:11Z`, `formal/`, `discovered/`).
2. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2210\.14762|petyuk|bruijn|word[-_]?rep`):**
   - `1337isnot1337/solved-conjectures` (`19,821` files, `pushed=2026-11-27T03:41:07Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T03:14:22Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T03:40:32Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,011` files, `pushed=2026-11-27T03:41:24Z`, `truncated=True`) -> path hits are `CSLibExt/Bioinformatics/Assembly/DeBruijn.lean` and `CSLibExt/Languages/LambdaCalculus/DeBruijn/**` (genome assembly / nameless lambda terms only).
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`1,625` files, `pushed=2026-11-27T03:41:21Z`) -> path hit `proofs/Erdos110.erdos_110.variants.de_bruijn_erdos.lean` (De Bruijn–Erdős theorem, unrelated).
   - `DomTheDeveloper/open-math-agents` (`446` files, `pushed=2026-11-27T03:39:51Z`) -> `0` hits.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T03:26:22Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,213` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> path hits `old-word-replay.py` / `word_replay.py` only.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & GitHub search (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&per_page=100` -> `0` hits; `TheJustinSunPrize/awards#5595` (`Erdős 638`) matched regex only on unrelated word/string text.
   - `search/issues?q=2210.14762+repo:1337isnot1337/solved-conjectures` -> `0`.
   - `search/issues?q=2210.14762+repo:the-omega-institute/trureturing` and `Petyuk+repo:the-omega-institute/trureturing` -> `0`.
   - Global `search/issues?q=%222210.14762%22` -> `0`; `search/issues?q=Petyuk+%22word-representable%22` -> `0`; `search/issues?q=%22simplified+de+Bruijn%22` -> `6` bioinformatics/CS software issues (`lh3/gfatools`, `gilbertohasnofb/auxjad`, `vercel-labs/zerolang`, `gerbenvoshol/kallisto`, `hargoniX/Leanwuzla`, `chrisquince/STRONG`), none on word-representability.
4. **Zenodo API:**
   - `"2210.14762"` -> `total=0`; `"simplified de Bruijn"` -> `total=0`; `Petyuk` -> `7` proteomics/biology records (Vladislav Petyuk) only.

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing#32548` / `#32586`: de Bruijn universal cycles registration, unrelated to word-representability of $S(n,k)$.
- `Huang–Kitaev–Pyatkin` (`2312.10377v1`) & `Roy–Hariharasubramanian` (`2605.02268v2`): treat distance-restricted $S_m(n,k)$ and shift graphs $G(n,k)$ respectively; Petyuk's Conjecture 1 for $S(n,k)$ ($n \ge 4, k \ge 3$) remains open in those papers.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed offline papers or private repositories are not covered.
