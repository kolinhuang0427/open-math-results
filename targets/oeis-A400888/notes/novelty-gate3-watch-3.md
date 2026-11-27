# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A400888/`

- **Checked (UTC):** `2026-11-27T04:40:08Z` – `2026-11-27T04:40:56Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for OEIS `A400888` surjectivity conjecture by M. Jeremie Lafitte (Levitas))

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py "400888" A400888 "Lafitte" "Levitas" "Gosper-Lafitte" "Stern vectors"`):**
   - `0` lines across `0/470` files (including `watch/snapshots/ai-collections/`, `1337-solved-conjectures/`, `discovered/`, `formal/`, `arxiv/`).
2. **Live competing & OEIS GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `400888|lafitte|levitas|gosper.?lafitte`):**
   - `1337isnot1337/solved-conjectures` (`19,882` files, `pushed=2026-11-27T04:39:39Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T04:18:42Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T04:30:11Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,042` files, `pushed=2026-11-27T04:40:13Z`, `truncated=True`) -> `0` hits in returned tree.
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`1,784` files, `pushed=2026-11-27T04:40:12Z`) -> `0` hits.
   - `DomTheDeveloper/open-math-agents` (`446` files, `pushed=2026-11-27T04:36:48Z`) -> `0` hits.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T04:40:26Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,080` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> `0` hits in returned tree.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `chy4pro/automath` (`2,969` files, `pushed=2026-10-12T05:25:06Z`) -> `0` hits.
   - `joaquimmj/oeis-conjectures` (`1,122` files, `pushed=2026-11-19T16:39:12Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & GitHub search (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, TheJustinSunPrize/awards, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&sort=updated&direction=desc&per_page=100` -> `0` hits.
   - `search/issues?q=400888+repo:the-omega-institute/trureturing` -> `0`; `Lafitte+repo:the-omega-institute/trureturing` -> `0`; `400888+repo:1337isnot1337/solved-conjectures` -> `0`.
   - Global `search/issues?q=%22A400888%22` -> `2` unrelated software QA/ticket hits (`cesarvangerwen-glitch/echoborn`, `y-l-g/tablo`).
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A400888&fmt=json`):**
   - Still at `revision 16`, `time=2026-10-15T16:25:59-04:00` (`comments_count=5`, conjecture status unchanged since Gate 1).
5. **Zenodo API:**
   - `"A400888"` -> `total=0`; `"Gosper-Lafitte"` -> `total=0`.

## Near Misses and Why They Don't Settle the Exact Statement
- `archmageirvine/joeis` (`A400888.java` noted in Gate 1): jOEIS Java sequence generator only, not a surjectivity proof.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed offline manuscripts or private repos are not covered.
