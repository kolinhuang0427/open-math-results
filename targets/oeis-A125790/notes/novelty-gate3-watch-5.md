# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A125790/`

- **Checked UTC:** `2026-11-27T05:10:59Z` – `2026-11-27T05:53:04Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A125790/`)
- **Target Scope:** OEIS `A125790` (rev 47, `2026-03-22T15:37:03-04:00`), Mikhail Kurkov's May 03 2025 row generating function formula (`Conjecture: Row n has generating function A(n, x) ...`).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 522 files):**
   - `.venv/bin/python tools/novelty_grep.py "A125790" "125790" "Kurkov"`
   - Result: `0` hits for `A125790` or `125790`; `Kurkov` matches only unrelated `joaquimmj/oeis-conjectures` (`A006068`), `mathesis-papers` (`kurkov-binary-stirling-row-edge`, `kurkov-a340991-convolution-row-recursion`, `kurkov-a263634-log-polynomials`, `kurk396563`), and `trureturing` (`A057032`, `KurkovGrayInverseRecurrence`, `KurkovLowerBitRecurrence`, `KurkovRunAlternatingCount`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `all:A125790`: `0` results.
   - `all:Kurkov`: `37` total results (top 10 inspected: `2607.26613v1` by Sangtae Jeong on Lehmer / Comtet numbers, and 9 Lie-Poisson / $\kappa$-Minkowski electrodynamics preprints). None address `A125790`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A125790&fmt=json`):**
   - Revision `47`, timestamp `2026-03-22T15:37:03-04:00` (unchanged from Gate 1/2).
4. **Zenodo & Crossref:**
   - `https://zenodo.org/api/records?q=A125790&size=10`: `total=0`.
   - `https://api.crossref.org/works?query=A125790&rows=5`: `0` items.
5. **Web Search (`search_web`):**
   - `"A125790" "Kurkov"`: only the OEIS `A125790` entry and an unrelated LiveJournal hit.
6. **GitHub Read-Only Checks (`gh api` trees + `gh search`):**
   - Recursive tree grep (`125790|kurkov`) on `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures`: `(no match)` on all 15 repos.
   - `gh search prs --repo the-omega-institute/trureturing "A125790"`: `0` PRs.
   - `gh search issues --repo the-omega-institute/trureturing "A125790"`: 1 hit, issue `#29156` (*"Open problem (preregistration): prove Mikhail Kurkov’s second new conjecture (unnumbered shifted parity transform), MathOverflow 506710 (2026; no arXiv id)"*) — unrelated conjecture (MO 506710 column shifted parity transform, not Kurkov's May 2025 row generating function conjecture).

## What Was Not Covered
- Paywalled / offline literature not indexed by arXiv, Crossref, Zenodo, OEIS, GitHub, or web search; live OpenAlex API (`HTTP 429` from this runner, not applicable to an OEIS-only target with no arXiv/DOI).
