# Gate 3 Novelty Receipt (`watch-3`) — `targets/gaetz-2512.08168-conj1/`

- **Checked (UTC):** `2026-11-27T03:34:54Z` – `2026-11-27T03:52:15Z` (live refresh of prior `00:42Z` receipt across expanded 15 competing repos + Zenodo)
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Conjecture 1.3 `conj:union-intersection` of `arXiv:2512.08168v2`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py 2512.08168 Gaetz "conj:union-intersection"`):**
   - `watch/snapshots/arxiv/index.md` / `cat_math.CO.json` / `recent_arxiv.json` (`Gaetz–Gao` `2611.33572v1` *Reflection subgroups and the Lookup Conjecture*), `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json`, `watch/snapshots/arxiv/openalex_works_cache.json` (`2512.08168` record), and `watch/snapshots/discovered/MattiaCalzavara__gaetz-gao-conjecture-proof.json` (strong $q$-log-concavity).
   - `watch/snapshots/discovered/the-omega-institute__trureturing-tools.json`: `SCREENED-OUT-R52.md` cites only `2512.08168` Conjecture 1.9.
   - `watch/snapshots/ai-collections/` (`54,475` files, `297` issues+PRs as of `2026-11-27T03:50:11Z`) -> `0` hits.
2. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2512\.08168|gaetz|billey|postnikov|union[-_]?intersection`):**
   - `1337isnot1337/solved-conjectures` (`19,821` files, `pushed=2026-11-27T03:41:07Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T03:14:22Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T03:40:32Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,011` files, `pushed=2026-11-27T03:41:24Z`, `truncated=True`) -> `0` hits in returned tree.
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`1,625` files, `pushed=2026-11-27T03:41:21Z`) -> `0` hits.
   - `DomTheDeveloper/open-math-agents` (`446` files, `pushed=2026-11-27T03:39:51Z`) -> `0` hits.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T03:26:22Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,213` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> `0` hits in returned tree.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` path hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & `the-omega-institute/trureturing` searches (`gh api`):**
   - `1337isnot1337/solved-conjectures` latest 100 issues/PRs -> `#315` (Stanley's tree-isomorphism) and `#353` (Athanasiadis–Chapoton $q$-zeta) matched regex on unrelated body text only; `aliromman/math`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents` -> `0` hits.
   - `search/issues?q=2512.08168+repo:the-omega-institute/trureturing` -> 1 hit (`#7333` standing lane log); `search/issues?q=Gaetz+repo:the-omega-institute/trureturing` -> 1 unrelated hit (`#24638` on `A391810`); global `"2512.08168" OR "conj:union-intersection"` -> `#7333` only.
   - `the-omega-institute/trureturing-tools` `SCREENED-OUT-R52.md` mentions ONLY `arXiv:2512.08168 Conjecture 1.9` (refuted by Theorem 6.2 of the paper itself), NOT Conjecture 1.3.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=%222512.08168%22&size=5` -> `total=0`; `https://zenodo.org/api/records?q=%222512.08168%22+OR+%22Billey-Postnikov%22&size=5` -> `total=0`.

## Near Misses and Why They Don't Settle the Exact Statement
- `MattiaCalzavara/gaetz-gao-conjecture-proof`: settles Gaetz–Gao's strong $q$-log-concavity conjecture, unrelated to Billey–Postnikov posets (`2512.08168`).
- `the-omega-institute/trureturing-tools` `SCREENED-OUT-R52.md`: notes `2512.08168` Conjecture 1.9 only (settled in Theorem 6.2 of `2512.08168` itself), not Conjecture 1.3 (`conj:union-intersection`).
- `Gaetz–Gao` `arXiv:2611.33572v1`: reflection subgroups and the Lookup Conjecture, distinct from Conjecture 1.3.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed private repositories or closed-access publications are not covered.
