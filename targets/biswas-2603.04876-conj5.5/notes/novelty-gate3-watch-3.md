# Gate 3 Novelty Receipt (`watch-3`) — `targets/biswas-2603.04876-conj5.5/`

- **Checked (UTC):** `2026-11-27T04:19:05Z` – `2026-11-27T04:21:10Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Biswas–Mandal–Saha `arXiv:2603.04876v1` Conjecture 5.5 on $\mathcal{RV}_{\mathrm{chordal}}(n)$)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 470 files via `.venv/bin/python tools/novelty_grep.py "2603.04876" Biswas "RV_chordal" "v-number" "Cameron-Walker"`):**
   - `2603.04876` hits only `watch/snapshots/arxiv/citing/biswas-2603.04876-conj5.5.json`, `latest_sweep.json`, and `openalex_works_cache.json` (`2603.04876v1` itself).
   - `watch/snapshots/ai-collections/` (`54,475` files, `297` issues+PRs as of `2026-11-27T04:19:05Z`): `ArtificialZeng/AI-Has-Taste` matches `v-number` only for integral-closure monomial ideals (`BW2-B74-P02`, `BM2-B08-P04`, `SM2-P52`), unrelated to chordal graph $\mathcal{RV}_{\mathrm{chordal}}(n)$.
2. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2603\.04876|biswas|mandal|kamalesh|cameron.?walker|v[-_]?number|rv[-_]?chordal`):**
   - `1337isnot1337/solved-conjectures` (`19,848` files, `pushed=2026-11-27T04:20:07Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T04:18:42Z`) -> `0` hits.
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T04:20:09Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `0` hits.
   - `facebookresearch/atlas-lean` (`54,029` files, `pushed=2026-11-27T04:20:25Z`, `truncated=True`) -> `0` hits in returned tree.
   - `JENW1N/complete-math-solutions` (`425` files, `pushed=2026-10-11T02:27:03Z`) -> `0` hits.
   - `TheJustinSunPrize/awards` (`82` files, `pushed=2026-11-25T08:37:13Z`) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`1,718` files, `pushed=2026-11-27T04:20:23Z`) -> `0` hits.
   - `DomTheDeveloper/open-math-agents` (`446` files, `pushed=2026-11-27T04:19:20Z`) -> `0` hits.
   - `DomTheDeveloper/ProofPlaygrond` (`68` files, `pushed=2026-11-27T04:18:30Z`) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,080` files, `pushed=2026-11-10T14:54:58Z`, `truncated=True`) -> `0` hits in returned tree.
   - `linustalacko/small-true-things` (`37` files, `pushed=2026-11-27T02:36:05Z`) -> `0` hits.
   - `chy4pro/automath` (`2,969` files, `pushed=2026-10-12T05:25:06Z`) -> `0` hits.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`, `pushed=2026-11-27T02:20:34Z`) -> `0` hits.
   - `the-omega-institute/trureturing-mdbook` (`39` files, `pushed=2026-11-20T04:15:53Z`) -> `0` hits.
3. **Live issues/PRs & GitHub search (`gh api`):**
   - `repos/{1337isnot1337/solved-conjectures, aliromman/math, TheJustinSunPrize/awards, GuillaumeBAUD-coder/open-math-agents}/issues?state=all&sort=updated&direction=desc&per_page=100` -> `0` hits.
   - `search/issues?q=2603.04876+repo:1337isnot1337/solved-conjectures` -> `0`.
   - `search/issues?q=2603.04876+repo:the-omega-institute/trureturing` -> `0`; `Biswas+repo:the-omega-institute/trureturing` -> `7` unrelated items (`Biswas–Łobejko–Mazurek`, `Biswas–Shankar–Sivasubramanian` `2609.08562`, etc.); `"v-number"+chordal+repo:the-omega-institute/trureturing` -> `6` unrelated chordal/graph items (`#30836`, `#30309`, `#22764`, `#31744`, `#22515`, `#22865`).
   - Global `search/issues?q=%222603.04876%22` -> `0`; `search/issues?q=%22RV_chordal%22+OR+%22v-number+of+Graphs%22` -> `31` unrelated software/non-Biswas items (matching `of Graphs`).
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=%222603.04876%22&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=%22Lattice+points+arising+from+regularity%22&size=5` -> `total=0`.

## Near Misses and Why They Don't Settle the Exact Statement
- `ArtificialZeng/AI-Has-Taste` (`BW2-B74-P02`, `BM2-B08-P04`, `SM2-P52`): study the $v$-number of monomial ideals under integral closure, not the $(r,v)$ region $\mathcal{RV}_{\mathrm{chordal}}(n)$ of connected chordal edge ideals.
- `the-omega-institute/trureturing` `#13176` / `#13253` (`Biswas–Shankar–Sivasubramanian`, `arXiv:2609.08562`) and `#30836` / `#30309` (chordal PSD completion / clique multicover): different papers and invariants.

## What Was Not Covered
- `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` `git/trees` were truncated past ~50k entries (`truncated=True`), and `the-omega-institute/trureturing` was queried via `search/issues` + `trureturing-tools`/`trureturing-mdbook`; non-indexed off-arXiv manuscripts or private repos are not covered.
