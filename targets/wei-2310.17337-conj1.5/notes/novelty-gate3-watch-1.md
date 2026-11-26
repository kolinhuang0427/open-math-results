# Gate 3 Novelty Receipt — `wei-2310.17337-conj1.5`

- **UTC Time:** 2026-11-26T20:23:16Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Live Pre-Report Re-Checks Performed

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py 2310.17337 s1793830926500679 C_k-isolation C_4-isolation C_8-isolation "Xiaohua Wei" "Biao Zhao"` -> only the OpenAlex citing cache (`citing_count: 0`) for `wei-2310.17337-conj1.5`.
2. **Live `1337isnot1337/solved-conjectures` (`gh api`, read-only):**
   - `commits/main` (`2dfd2a211b`, `2026-11-26T20:03:29Z`, PR #902) and `issues?state=all&since=2026-11-26T20:03:00Z` -> `#902`, `#897`, `#870`, `#480`, `#352`, none related to `2310.17337` or $C_k$-isolation.
3. **Live GitHub global & `trureturing` searches (`gh api`, read-only):**
   - `search/code?q="2310.17337"+OR+"s1793830926500679"` -> 0 hits.
   - `search/code?q="C_k-isolation"+OR+"C_8-isolation"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+s1793830926500679+OR+2310.17337` -> 0 hits.
4. **Live web searches (`search_web`):**
   - `"10.1142/s1793830926500679" OR "s1793830926500679" OR ("2310.17337" "counterexample" "C_8")` -> only primary paper / DOI.
   - `"truncated tetrahedron" "isolation number" OR "C_8-isolating" OR "C_k-isolating"` -> 0 matches linking truncated tetrahedron to $C_k$-isolation.

## Near Misses

- Same as Gate 2 (`novelty-gate2-watch-1.md`): `ArtificialZeng/AI-Has-Taste` (`SM2-P55`, square isolation in $Q_6$), Borg–Scicluna `arXiv:2510.08361v2` (*Discrete Appl. Math.* 394 (2026), 261–268, proves $\iota(G, \{C_k: k\ge 4\}) \le (m+1)/6$ implying only $k=4$), and DMAA 2026 published abstract (`10.1142/s1793830926500679`, noted by `audit-2`/`lit-verifier` as leaving the general $C_k$-isolation problem open).

## What Was Not Covered

- Paywalled full text of *Discrete Mathematics, Algorithms and Applications* (`10.1142/s1793830926500679`), OpenAlex/arXiv live re-query (covered by `@watch-5`), and private repositories.
