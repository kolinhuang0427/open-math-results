# Gate 3 Novelty Re-Check — `oeis-A006255` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:08:25Z`
- **Target:** `targets/oeis-A006255/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Padhi's 2026 Graham-sequence threshold conjecture found across live OEIS, arXiv, Zenodo, Crossref, web search, snapshots, `aliromman/math`, or `the-omega-institute/trureturing-tools`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 333 files incl. `aliromman__math.json` & `trureturing-tools.json`):**
   - `A006255 Corneth Padhi` -> 4 lines across 3/333 files (`1337-solved-conjectures/issues_all.jsonl` line 698 on a permutation recurrence; `jaideepsaipadhi/erdos-sums-almost-primes` on Gorodetsky–Lichtman–Wong); 0 matches on `A006255` or Corneth's Graham conjecture.
   - `"A006255" "6255" "Graham"` -> 97 lines across 50/333 files (Erdős–Graham problems #195/#282/#342/#432/#479/#810, Graham pebbling `#3102`, Marica–Schönheim `GrahamConjecture`, `46255` PR); 0 hits on `A006255`.

2. **GitHub Live Checks (`gh search` / `gh api`, read-only):**
   - `gh search prs --repo aliromman/math "... OR A006255 ..."` -> 0 matches.
   - `gh search code --repo aliromman/math "... OR A006255 ..."` -> 0 matches.
   - `gh api "repos/aliromman/math/pulls?state=all&per_page=100"` filtered for `006255` -> 0 matches (`NO_PR_MATCH`).
   - `gh search code --repo the-omega-institute/trureturing-tools "... OR A006255 ..."` and `contents` check -> 0 matches (`NO_TRUTOOLS_MATCH`).
   - `gh search prs --repo the-omega-institute/trureturing "... OR A006255 ..."` -> 0 matches.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A006255&fmt=json`):**
   - Confirmed `revision: 106` (`2026-06-19T00:16:16-04:00`) unchanged; comment still reads: `Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A006255` -> `0` entries.
   - `all:Padhi AND all:Graham` -> `0` entries.

5. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=A006255` -> `0` hits; `q="Ron Graham" 171` -> unrelated records (`The Raleigh Game`, `Champ 1.7.1`, etc.).
   - Crossref `query=A006255` -> 1 unrelated biomedical hit (`10.1101/mcs.a006255`).

6. **Web Search (`search_web`):**
   - `"A006255" "Padhi" OR "b(n)^2 >= 2 * n"` -> only OEIS `A006255` itself.

## Near Misses & Why They Do Not Settle the Exact Statement

- Erdős–Selfridge (1992) / Adenwalla (`arXiv:2504.19196`): Establish `P(n) > sqrt(2n) + 1 => a(n) = n + P(n)`, leaving open the critical boundary `sqrt(2n) <= P(n) <= sqrt(2n) + 1` (containing `n = 171`).
- `jaideepsaipadhi/erdos-sums-almost-primes` & `1337isnot1337` #698: Separate works by Jaideep Padhi on sums of almost primes and permutation recurrences, unrelated to OEIS `A006255`.
- `CONTESTED.md`: absent from `targets/oeis-A006255/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works in this Gate 3 check.
- Closed-access journals and unindexed private notes.
