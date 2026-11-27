# Gate 2 Novelty Receipt (`watch-5`) — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked at (UTC):** `2026-11-27T12:02:13Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)**
- **Target:** Dochtermann, Huang, Mawhinney, Oh, Xu (`arXiv:2609.13361v1`, 2026-09-11), *Matroids with cycle systems are regular*, Section 7 Conjecture 7.5 (`\label{conj:C>=3 ind}`: if $M$ has a circuit system $\mathcal{C}$ with $\mathcal{C}_{[g]}$ a circuit, then $\mathcal{C}_{\ge 3}$ is independent) — plus implied Conjecture 7.4 (`conj:unique`) via Main Theorem $\mathcal{C}_{\ge 3} = \emptyset$.

## Exact Queries & Results
1. **Local snapshot grep (`tools/novelty_grep.py`, 690 files):**
   - Query: `.venv/bin/python tools/novelty_grep.py 2609.13361 2609.17446 2509.11460 "circuit system" Dochtermann "conj:C>=3"`
   - Output: `6` lines across `2/690` files:
     - `watch/snapshots/discovered/tamnd__arxiv.json` lines 991, 6460, 11869, 17004, 22269 (paper metadata/bib/census index only; already verified stub/index, no proof of Conjecture 7.5).
     - `watch/snapshots/1337-solved-conjectures/open_issues_claims.md:606` (`#336 [open]` Stanley's pure O-sequence conjecture — discusses Corry et al. `2509.11460` and Oh `2609.17446` on 2-sums/one-element connections; explicitly `[open]`, no mention of `2609.13361` or `conj:C>=3 ind`).
   - `grep -iE "2609\.13361|dochtermann" watch/snapshots/insorrowmeow-oeis-ids.md`: `0` hits.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `query 'id:2609.13361 OR id:2609.17446 OR id:2509.11460'`: `2609.13361v1` (updated `2026-09-11T17:52:05Z`, no journal_ref/DOI) and `2509.11460v1` (updated `2025-09-14`) remain sole versions; `2609.17446v2` (SuHo Oh, `2026-09-19T13:12:33Z`) inspected directly via HTML (`https://arxiv.org/html/2609.17446v2`). Cites `[15]` (`2609.13361`) only in §1, §3.1 Theorem 3.4 (*"Every matroid admitting a cycle system is regular"*), §4.5, Acknowledgements, Use of AI tools — **0 mentions** of `"circuit system"`, `"Conjecture 7.4"`, `"Conjecture 7.5"`, or $\mathcal{C}_{\ge 3}$ independence.
   - `query 'all:"circuit system" AND matroid'`: `0` results.
   - `query 'all:"cycle system" AND matroid'`: `3` results (`2609.17446v2`, `2609.13361v1`, `2509.11460v1`).
3. **GitHub live checks:**
   - `gh api 'repos/the-omega-institute/trureturing/git/trees/dev?recursive=1' | grep -iE "2609|dochtermann|circuit.?sys|cycle.?sys"`: `0` hits.
   - `gh search issues "2609.13361"`: `0` hits.
   - `gh search repos "circuit-system matroid"`: `0` hits.
4. **Zenodo / Parslow Ledger / Web search:**
   - `https://zenodo.org/api/records?q=2609.13361&size=5`: `total: 0`.
   - `https://mylesparslow-collab.github.io/demos/conjecture-ledger/index.html`: `0` hits for `2609.13361`, `dochtermann`, `circuit system`.
   - Web search (`"2609.13361" OR ("Dochtermann" "circuit system" "conjecture")`): returns only `arXiv:2609.13361` primary preprint.

## Coverage Limits
- **Semantic Scholar API:** returned HTTP `429` (`Too Many Requests`) during `12:01Z` query.
- **OpenAlex API:** `works?search=Matroids+with+cycle+systems+are+regular` and `works?search=Cycle+systems+coparking+functions` both returned `[]` (no indexed records matched those exact search strings).
- `gh search code` not queried separately (avoided 10 req/min rate limit; covered via 690 snapshots + `trureturing` `dev` tree + `gh search issues`/`repos`, and `watch-6` `#1379` verified `cmu-l3/reuF2F` `by sorry` stub).
