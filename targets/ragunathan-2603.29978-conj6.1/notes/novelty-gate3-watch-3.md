# Gate 3 Novelty Receipt (`watch-3`) — `targets/ragunathan-2603.29978-conj6.1/`

- **Checked (UTC):** `2026-11-27T03:34:54Z` – `2026-11-27T03:52:15Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Ragunathan–Van Tuyl `arXiv:2603.29978v2` Conjecture 6.1 on the Weak Lefschetz Property of $A(\mathtt{vdw}(n,k))$)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py "2603.29978" Ragunathan "vdw(n,k)" "van der Waerden simplicial"`):**
   - Only `watch/snapshots/arxiv/citing/ragunathan-2603.29978-conj6.1.json` and `watch/snapshots/arxiv/openalex_works_cache.json` (`2603.29978` metadata itself).
   - `watch/snapshots/ai-collections/` (`54,475` files, `297` issues+PRs as of `2026-11-27T03:50:11Z`): only generic substring match on `Conjecture 6.1` (`Argus-AiTeam/argus-mathematics` family `20001036`, Seymour–Sullivan Conjecture 6.1).
2. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2603\.29978|ragunathan|van.?tuyl|vdw|waerden`):**
   - `1337isnot1337/solved-conjectures` (`19,821` files, `pushed=2026-11-27T03:41:07Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T03:14:22Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T03:40:32Z`) -> 2 false-positive substring hits (`PhyslibWirtingerFderivDWirtinger*.lean` matching `vdw` inside `DWirtinger`).
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,011` files, `pushed=2026-11-27T03:41:24Z`, `truncated=True`) -> `VanDerWaerden*.lean` files in `MathlibExt` (Ramsey / additive combinatorics / Van der Waerden matrix permanent only, not `vdw(n,k)` simplicial WLP).
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`1,625` files, `pushed=2026-11-27T03:41:21Z`) & `DomTheDeveloper/open-math-agents` (`446` files, `pushed=2026-11-27T03:39:51Z`) -> `Erdos499` / `Erdos1186` Van der Waerden variants only.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T03:26:22Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,213` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> `0` hits in returned tree.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & GitHub search (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, TheJustinSunPrize/awards, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&per_page=100` -> `0` hits.
   - `search/issues?q=2603.29978+repo:1337isnot1337/solved-conjectures` -> `0`; `2603.29978+repo:the-omega-institute/trureturing` -> `0`; `Ragunathan+repo:the-omega-institute/trureturing` -> `0`; `"Van Tuyl"+repo:the-omega-institute/trureturing` -> 2 unrelated hits (`#28950` Zabokritskiy/Yohananov, `#26405` Koljančić–Oblak Problem).
   - Global `search/issues?q=%222603.29978%22` -> `0`; `search/issues?q=%22van+der+Waerden+simplicial%22` -> `0`.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=%222603.29978%22&size=5` -> `total=0`; `https://zenodo.org/api/records?q=%222603.29978%22+OR+%22van+der+Waerden+simplicial%22&size=5` -> `total=0`.

## Near Misses and Why They Don't Settle the Exact Statement
- `chy4pro/automath` (per Gate 1): lists `2603.29978` only as an open arXiv entry brief, not a resolution.
- `rjwalters/lean-genius` issues (`van-der-waerden-first-moment`) & `facebookresearch/atlas-lean` `VanDerWaerden*.lean`: concern Ramsey/Van der Waerden numbers and permanents, unrelated to Stanley–Reisner WLP of $\mathtt{vdw}(n,k)$.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed theses or papers omitting `2603.29978` and `van der Waerden simplicial` are not covered.
