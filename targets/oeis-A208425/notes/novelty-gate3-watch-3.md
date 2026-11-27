# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A208425/`

- **Checked (UTC):** `2026-11-27T03:34:54Z` – `2026-11-27T03:52:15Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Zhi-Wei Sun's `A208425` Part (ii) Case $p \equiv 1 \pmod{3}$, i.e., `conjecture_2` of `FormalConjectures/OEIS/208425.lean`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py 208425 A208425`):**
   - `watch/snapshots/formal/formal-conjectures-files.tsv` & `last_sweep.json`: `FormalConjectures/OEIS/208425.lean` (open target definition).
   - `watch/snapshots/discovered/Varun-Dudipala__sun-conjectures-lean.json` (`pushed=2026-11-19T00:19:09Z`): explicitly resolves ONLY `conjecture_3` ($p \equiv 2 \pmod 3$) and notes Part (i) and $p \equiv 1 \pmod 3$ are not proved there.
   - `watch/snapshots/arxiv/citing/oeis-A208425.json` (`0` new resolving entries); 7 AI collections under `watch/snapshots/ai-collections/` (`54,475` files, `297` issues/PRs as of `2026-11-27T03:50:11Z`) returned `0` hits.
2. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `208425`):**
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
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & `the-omega-institute/trureturing` searches (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, TheJustinSunPrize/awards, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&sort=updated&direction=desc&per_page=100` -> `0` hits for `208425`.
   - `search/issues?q=208425+repo:1337isnot1337/solved-conjectures` -> `0` hits.
   - `search/issues?q=208425+repo:the-omega-institute/trureturing` -> `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A208425&fmt=json`):**
   - Still at `revision 60`, `time=2025-11-05T15:22:21-05:00` (unchanged since Gate 1; conjecture status intact).
5. **Zenodo API (`https://zenodo.org/api/records?q=A208425&size=5`):**
   - `total=0`.

## Near Misses and Why They Don't Settle the Exact Statement
- `Varun-Dudipala/sun-conjectures-lean` (`SunConjectures/A208425/Solution.lean`): proves `conjecture_3` ($p \equiv 2 \pmod 3$) only and explicitly states Part (i) and $p \equiv 1 \pmod 3$ (`conjecture_2`) are not proved there.
- `arXiv:2012.05121v3` (Pan–Sun, 2026) & `epoch-research/LeanOpenProblems-results`: Pan–Sun settles Part (i) (`conjecture_1`) only; `LeanOpenProblems-results` runs on `oeis_208425_conjecture_0` failed (`sorryAx`).

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook` rather than a full tree dump; offline/non-indexed manuscripts that omit `A208425`/`208425` are not covered.
