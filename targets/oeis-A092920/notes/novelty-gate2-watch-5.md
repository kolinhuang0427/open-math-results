# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A092920/`

- **Checked UTC:** `2026-11-27T06:14:21Z` – `2026-11-27T06:36:35Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A092920/`)
- **Target Scope:** OEIS `A092920` (rev 56, `2026-03-14T12:38:00-04:00`), Mikhail Kurkov's Apr 24 2023 conjecture: $a(n) = \sum_{k=0}^{2^{n-1}-1} b(k)$ for $n > 0$ with $a(0)=1$, where $b(2^m(2n+1)) = \sum_{k=0}^{[m>0](m-1)} \binom{m-1}{k} b(2^k n)$ ($b(0)=1$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 522 files):**
   - `.venv/bin/python tools/novelty_grep.py "A092920" "strongly monotone" "Kurkov"`
   - Result: `0` hits for `A092920` or `"strongly monotone"`; `Kurkov` matches only unrelated `joaquimmj/oeis-conjectures` (`A006068`), `mathesis-papers` (`kurkov-binary-stirling-row-edge`, `kurkov-a340991-convolution-row-recursion`, `kurkov-a263634-log-polynomials`, `kurk396563`), and `trureturing` (`A057032`, `KurkovGrayInverseRecurrence`, `KurkovLowerBitRecurrence`, `KurkovRunAlternatingCount`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `all:A092920`: `0` results.
   - `all:"strongly monotone partitions"`: `0` results.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A092920&fmt=json`):**
   - Revision `56`, timestamp `2026-03-14T12:38:00-04:00`; formula remains marked `Conjecture: a(n) = Sum_{k=0..2^(n-1) - 1} b(k) for n > 0 ... - _Mikhail Kurkov_, Apr 24 2023`.
4. **Zenodo & Crossref:**
   - `https://zenodo.org/api/records?q=A092920&size=5`: `total=0` (`strongly monotone partitions` broad keywords returned unrelated ML/biology hits).
   - `https://api.crossref.org/works?query=A092920&rows=5`: `0` items.
5. **Web Search (`search_web`):**
   - `"A092920" "Kurkov" OR "strongly monotone partitions" "2^(n-1)"`: only OEIS `A092920` and general set-partition/pattern-avoidance literature.
6. **GitHub Read-Only Checks (`gh api` trees + `gh search`):**
   - Recursive tree grep (`092920|strongly.?monotone`) across all 15 competing repos (`aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures`): `0` matches.
   - `gh search issues/prs --repo the-omega-institute/trureturing "A092920"`: `0` hits.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, Zenodo, Crossref, GitHub, or web search.
