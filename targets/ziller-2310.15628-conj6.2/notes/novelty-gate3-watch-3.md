# Gate 3 Novelty Receipt (`watch-3`) — `targets/ziller-2310.15628-conj6.2/`

- **Checked (UTC):** `2026-11-27T06:36:49Z` – `2026-11-27T06:48:42Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Mario Ziller `arXiv:2310.15628v2` Section 6 Conjecture 6.2 on pairwise distinctness of $\varphi(x)/x^2$ for $x \in \mathbb{N}$)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 522 files via `.venv/bin/python tools/novelty_grep.py "2310.15628" Ziller A373318 A373319 "varphi(x)/x^2"`):**
   - `2310.15628` appears only in `watch/snapshots/arxiv/citing/ziller-2310.15628-conj6.2.json`, `latest_sweep.json`, and `openalex_works_cache.json`, plus `watch/snapshots/formal/last_sweep.json`.
   - `Ziller` matches unrelated Gerbicz–Ziller `u(n)` tables for Erdős #854 (`plasma-ai__erdos`, `techno-optimist__erdos-frontier-atlas`); `A373319` matches unrelated `erdosproblems` PR replacing `A373319` with `A373119` for Problem 121.
2. **arXiv API (`.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.15628`):**
   - `2310.15628v2` (`2026-04-15T17:18:47Z`) remains the latest version.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A373318&fmt=json` & `A373319`):**
   - `A373318` (`rev=9`, `2024-06-01T04:03:07-04:00`) and `A373319` (`rev=15`, `2025-09-10T17:43:39-04:00`): unitary-divisor asymptotic density numerator/denominator sequences, unrelated to $\varphi(x)/x^2$ injectivity.
4. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2310\.15628|ziller|373318|373319|totient.?square|phi.?div.?x2`):**
   - `1337isnot1337/solved-conjectures` (`19,927` files, `pushed=2026-11-27T06:34:11Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T06:29:39Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T06:30:32Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,097` files, `pushed=2026-11-27T06:39:18Z`, `truncated=True`) -> `0` hits in returned tree.
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`2,314` files, `pushed=2026-11-27T06:40:19Z`) -> `0` hits.
   - `DomTheDeveloper/open-math-agents` (`2,218` files, `pushed=2026-11-27T06:29:44Z`) -> `0` hits.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T06:26:02Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,080` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> `0` hits in returned tree.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `chy4pro/automath` (`2,969` files, `pushed=2026-10-12T05:25:06Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
5. **Live issues/PRs & GitHub search (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, TheJustinSunPrize/awards, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&sort=updated&direction=desc&per_page=100` -> `0` hits.
   - `search/issues?q=2310.15628+repo:the-omega-institute/trureturing` -> `#24177` (*Mike Klein's global-convergence conjecture in OEIS A349824*, citing `2310.15628` only in passing around Mohan Lal, unrelated to Conjecture 6.2).
   - `Ziller+repo:the-omega-institute/trureturing` -> `0`; `A373318+OR+A373319+repo:the-omega-institute/trureturing` -> `0`; `2310.15628+repo:1337isnot1337/solved-conjectures` -> `0`.
   - Global `search/issues?q=%222310.15628%22` -> `#24177` only; `"Mario Ziller" OR "varphi(x)/x^2"` -> unrelated software/math issues.
6. **Zenodo API:**
   - `"2310.15628"` -> `total=0`; `"Mario Ziller"` -> `1` unrelated record (`22710993`, *Study of the empirical Hausdorff fractal dimension of primorial sieve*).

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing#24177`: concerns Mike Klein's OEIS `A349824` conjecture, not Ziller Conjecture 6.2 ($\varphi(x)/x^2$).
- `arXiv:2310.15628v2` itself proves only the squarefree/coprime partial case of $\varphi(x)/x^2$ distinctness and leaves Conjecture 6.2 open.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed problem books or private repositories are not covered.
