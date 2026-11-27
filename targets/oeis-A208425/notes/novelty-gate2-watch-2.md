# Gate 2 Novelty Receipt — `oeis-A208425`

- **UTC Time:** 2026-11-27T01:48:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #587)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "A208425" "208425"` -> matches only `FormalConjectures/OEIS/208425.lean` (open) and `Varun-Dudipala/sun-conjectures-lean` (`conjecture_3`, $p \equiv 2 \pmod 3$ only). 0 matches in `1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `arxiv`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A208425&fmt=json`):**
   - Revision 60 (`2025-11-05T15:22:21-05:00`) still lists Sun's Nov 12, 2016 Conjectures (i) and (ii).
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2012.05121` -> `2012.05121v3` (Pan & Sun, *Frontiers in Combinatorics and Number Theory* 2 (2026), 55–62), which settles `conjecture_1` (Part (i)) only and does not address `conjecture_2` ($p \equiv 1 \pmod 3$).
4. **Live GitHub (`gh api`, read-only):**
   - Checked `Varun-Dudipala/sun-conjectures-lean` tree (25 files): covers `SunConjectures/A208425` (`conjecture_3` for $p \equiv 2 \pmod 3$ only).
   - Checked `JENW1N/complete-math-solutions` tree (425 files): 0 matches for `208425`.
   - Repo-scoped `search/issues` & `search/code` for `A208425` / `208425` across `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing`, `trureturing-tools`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `TheJustinSunPrize/awards`: 0 hits for `A208425` (numeric `208425` hits only unrelated line/seed IDs).
   - Global `search/issues?q=A208425`: 0 hits.
5. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=A208425+OR+208425+OR+%22central+trinomial%22+supercongruence&size=10` (67 hits, top hits unrelated biological/crabs metadata from numeric IDs).
   - `search_web` for `"A208425" OR ("2012.05121" "p == 1 (mod 3)") OR ("central trinomial" "2(p-1)/3")`: no proof of `conjecture_2` found.

## Near Misses & Why They Do Not Settle the Exact Statement

- **Pan & Sun (`arXiv:2012.05121v3`, 2026):** settles `conjecture_1` (Part (i)), not Part (ii) (`conjecture_2`).
- **`Varun-Dudipala/sun-conjectures-lean` (`SunConjectures/A208425`):** settles `conjecture_3` ($p \equiv 2 \pmod 3$), explicitly leaving $p \equiv 1 \pmod 3$ (`conjecture_2`) open.

## What Was Not Covered

- Closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, OEIS, or web search.
