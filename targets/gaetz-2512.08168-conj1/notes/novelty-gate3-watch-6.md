# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/gaetz-2512.08168-conj1/` (Christian Gaetz & Yibo Gao `arXiv:2512.08168v2` §1.1 Conjecture 1.3 `conj:union-intersection`: $\mathrm{BP}(w)$ is closed under intersection and union for all Coxeter groups)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-27T00:49:00Z`
- **Requested by:** `@audit-2` (board #495)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 357 files incl. `aliromman__math.json`, `KnowledgeSense__math.json`, `trureturing-tools`):**
   - `KnowledgeSense__math.json`: `0` hits for `2512.08168`, `conj:union-intersection`, `Billey--Postnikov`, `Billey-Postnikov`.
   - `aliromman__math.json`: `0` hits for `2512.08168`, `conj:union-intersection`, `Billey--Postnikov`, `Billey-Postnikov`.
   - `the-omega-institute__trureturing-tools.json`: only `SCREENED-OUT-R52.md` mentioning `arXiv:2512.08168 Conjecture 1.9` (refuted inside `2512.08168` Theorem 6.2), not Conjecture 1.3.
   - `novelty_grep.py` across all 357 files clear (also verified `MattiaCalzavara/gaetz-gao-conjecture-proof` proves a separate strong $q$-log-concavity conjecture).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A079727" OR all:"2512.08168"' --max-results 5` -> `0` citing follow-ups; `2512.08168v2` (`2026-06-08`) remains sole latest version.

## Near Misses
- `trureturing-tools/SCREENED-OUT-R52.md` references `2512.08168` Conjecture 1.9 only.
- `MattiaCalzavara/gaetz-gao-conjecture-proof` treats Gaetz–Gao's strong $q$-log-concavity conjecture.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not citing `2512.08168`.
