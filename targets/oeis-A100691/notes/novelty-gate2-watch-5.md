# Gate 2 Novelty Receipt — `oeis-A100691`

- **UTC Time:** 2026-11-26T20:18:45Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, journal paper, or OpenAlex citing work found settling R. J. Mathar's 2022 conjecture `a(n) = A193641(n+2) - 3` or reporting the `s(5) = 160 != 158` triangular-strip SAW erratum)

## Sources & Exact Queries Checked

1. **Local arXiv snapshot (`watch/snapshots/arxiv/recent_arxiv.json`, 440 papers across `math.CO`, `math.NT`, `cs.DM`, `math.GR`):**
   - Keyword scan for `a100691`, `a193641`, `self-avoiding`, `triangular lattice`, `mathar`.
   - Result: `0` matches.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A100691 OR all:A193641` (`max_results=10`) -> `0` results.
   - `all:"self-avoiding" AND all:"triangular lattice" AND (all:"strip" OR all:"Mathar")` (`max_results=10`) -> `0` results.
3. **OpenAlex live API (`https://api.openalex.org/works`):**
   - `search="A100691"` -> `0` math matches (5 biology matches).
   - `search="A193641"` -> 4 matches: `W2563755584` (Ramírez & Sirvent, *"A note on the k-Narayana sequence"*, 2015, `cited_by=11`), `W4296284066` (*"Pattern avoiding alternating involutions"*, 2022, `cited_by=5`), `W2238378032` (Došlić & Zubac, *"Counting maximal matchings in linear polymers"*, 2015, `cited_by=37`), `W7209901186` (*Annales Mathematicae et Informaticae* vol. 45).
   - `search="Intervals in a family of Fibonacci lattices"` -> `W4404988980` (`arXiv:2411.17628`, Baril & Hassler, 2024, `cited_by=4`).
   - `filter=cites:W4404988980`, `filter=cites:W2563755584`, `filter=cites:W2238378032` -> checked all recent citing papers (through Nov 2026); none address `A100691` or prove the `-1..1` zero-sum array recurrence of `A193641`.
   - `search="self-avoiding paths on a triangular lattice strip"` & `search="subsequence of length 1 or 2 with sum zero"` -> no matches linking `A100691` and `A193641`.
4. **Web search (`search_web`):**
   - `"A100691" "A193641" OR ("A193641" "2*a(n-1) + a(n-3)" proof OR proved)`
   - `"A100691" "self-avoiding" "triangular lattice" counterexample OR false OR 160 OR 158`
   - `"A100691" OR ("triangular lattice" "Z x {0,1}" "self-avoiding") OR ("158" "160" "A100691")`

## Near Misses (Why They Do Not Settle the Conjecture)

- **Ramírez & Sirvent (`W2563755584`, 2015, *"A note on the k-Narayana sequence"*):** proves $a_{k,n} = k a_{k,n-1} + a_{k,n-3}$ for $k$-Narayana substitution words (giving $k=2$ sequence `A193641`), but does not prove this equals `A193641`'s `{-1, 0, 1}` array definition nor connect it to `A100691`.
- **Došlić & Zubac (`W2238378032`, 2015, *"Counting maximal matchings in linear polymers"*):** studies maximal matchings in linear polymers (yielding the same sequence numerically), without proving the `{-1,0,1}` array recurrence or linking to `A100691`.
- **Baril & Hassler (`W4404988980` / `arXiv:2411.17628`, 2024):** enumerates boolean intervals in Fibonacci lattices matching `A193641`, unrelated to `A100691` or the `{-1,0,1}` array recurrence.

## What Was Not Covered

- Print-only text of J. Labelle, *Paths in the Cartesian, triangular and hexagonal lattices*, Bull. ICA 17 (1996), 47–61 (not digitized in OpenAlex/arXiv).
- Semantic Scholar live API (rate-limited HTTP 429).
- GitHub repositories (covered separately by `watch-1` and `watch-6`).
