# Gate 3 Novelty Receipt (`watch-3`) — `targets/cassaigne-2602.21895-conjC4/`

- **Checked (UTC):** `2026-11-27T06:31:37Z` – `2026-11-27T06:53:31Z`
- **Verdict:** **CONTESTED** (active competing public proof plan & unmerged Lean 4 settlement in `the-omega-institute/trureturing#24005` and `#29075`; see `CONTESTED.md`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 522 files via `.venv/bin/python tools/novelty_grep.py "2602.21895" Cassaigne Espinoza Stipulanti A357448 "base 3/2" Dekking`):**
   - `2602.21895` appears only in `watch/snapshots/arxiv/citing/cassaigne-2602.21895-conjC4.json`, `latest_sweep.json`, `openalex_works_cache.json`, and `watch/snapshots/formal/last_sweep.json`.
   - `joaquimmj/oeis-conjectures` (`A285076`) and `Cassaigne` 2014 additive-cube papers are unrelated.
2. **arXiv API (`.venv/bin/python tools/arxiv_fetch.py query --id-list 2602.21895`):**
   - `2602.21895v1` (`2026-02-25T13:24:47Z`) remains sole/latest version.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A357448&fmt=json`):**
   - `rev=20`, `time=2026-03-04T18:59:14-05:00` (`comments_count=5`, unchanged).
4. **Live competing GitHub repo trees (`gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1`, regex `2602\.21895|cassaigne|espinoza|stipulanti|357448|base.?3.?2|t_?3_?2`):**
   - `1337isnot1337/solved-conjectures` (`19,927` files, `pushed=2026-11-27T06:27:37Z`) -> `0` hits.
   - `aliromman/math` (`937` files, `pushed=2026-11-27T06:29:39Z`) -> `0` tree hits (`#84` is unrelated Presutti–Stromquist Conj 10.1).
   - `KnowledgeSense/math` (`5,377` files, `pushed=2026-10-14T07:35:52Z`) -> `0` hits.
   - `rainwangphy/aftd-platform` (`28,161` files, `pushed=2026-11-27T06:30:32Z`) -> `0` hits.
   - `valyuAI/research` (`5,381` files, `pushed=2026-10-27T16:11:42Z`) -> `4` false-positive `t32.mp3`/`t32.png` assets.
   - `facebookresearch/atlas-lean` (`54,099` files, `pushed=2026-11-27T06:31:05Z`, `truncated=True`) -> `0` hits in returned tree.
   - `JENW1N/complete-math-solutions` (`425` files) -> `0` hits; `TheJustinSunPrize/awards` (`82` files) -> `0` hits.
   - `GuillaumeBAUD-coder/open-math-agents` (`2,294` files, `pushed=2026-11-27T06:31:50Z`), `DomTheDeveloper/open-math-agents` (`2,218` files), `DomTheDeveloper/ProofPlaygrond` (`68` files) -> `0` hits.
   - `CrocSwap/integer-mult-bounds` (`54,080` files, `truncated=True`), `linustalacko/small-true-things` (`37` files) -> `0` hits; `chy4pro/automath` (`2,969` files) -> `erdos624` `3_2_EH` SAT certs only.
   - `the-omega-institute/trureturing-tools` (`1,713` files, `dev`) and `trureturing-mdbook` (`39` files) -> `0` path hits; `trureturing` `main` `D5/S1/Words/TwoBlockSubstitution/` has `ThueMorseFrequency.lean` only.
5. **Live `the-omega-institute/trureturing` searches (`gh api search/issues` + `issues/24005` & `issues/29075`):**
   - **MATCH (`CONTESTED`):** `search/issues?q=A357448+repo:the-omega-institute/trureturing` & `Dekking "3/2"` returned **`the-omega-institute/trureturing#24005`** (`open` preregistration on Dekking Conjecture 7 / `A357448` / `t' = \varphi(t_{3/2})` citing `2602.21895v1`, with a full 4-step Toeplitz-skeleton + residue-transfer proof plan for existence of all $\mu[w]$ and $\mu[00]=1/10, \mu[01]=4/10$) and **`the-omega-institute/trureturing#29075`** (`open`, `2026-11-11T00:58:12Z`, *Escape audit unfinished: ThueMorseBaseThreeHalvesFactorFrequency*, recording Lean 4 `result : claim` compiling with standard axioms on unmerged branch `lane/math/op-dekking2301` commit `57dc5140f9b`).
   - `#14986`, `#15108` (`2202.13548v1` 2-block substitution) and `#24159` (`2406.09302v4` reflection complexity) are distinct problems.
6. **Zenodo API:**
   - `"2602.21895"` -> `total=0`; `"Thue-Morse" "base 3/2"` -> unrelated Thue–Morse records.

## What Was Not Covered
- Private/unmerged branch `lane/math/op-dekking2301` commit `57dc5140f9b` returned HTTP 404 via public `gh api`; `facebookresearch/atlas-lean` and `CrocSwap/integer-mult-bounds` trees truncated past ~50k entries.
