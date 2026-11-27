# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A091524/`

- **Checked UTC:** `2026-11-27T09:05:15Z`
- **Verdict:** **PASS** (no competing proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A091524" "091524" "2509.19162" "CayleyPy" "unitriangular"` -> `0` hits for `A091524` or `091524` across all 605 files.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A091524"` -> `[]`.
   - `gh search issues "A091524"` -> `[]`.
3. **Live OEIS JSON & Zenodo API:**
   - `oeis.org/search?q=id:A091524&fmt=json`: revision `27` (`2025-02-16T08:32:52-05:00`) unchanged; Kurkov's Apr 25, 2024 formula remains marked `Conjecture:`.
   - `zenodo.org/api/records?q=A091524&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"A091524" "Mikhail Kurkov" OR "sqrt(A028982(n)/A006337(n))" OR "Graham-Pollak"` -> surfaces only OEIS `A091524`, `A003151`, `A003152`, and Wolfram MathWorld Graham–Pollak sequence; no proof found.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (605 files, 434 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, Zenodo, and `search_web`.
