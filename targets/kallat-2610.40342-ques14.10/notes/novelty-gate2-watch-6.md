# Gate 2 Novelty Receipt (`watch-6`) — `targets/kallat-2610.40342-ques14.10/`

- **Checked UTC:** `2026-11-27T14:40:56Z`–`2026-11-27T14:41:09Z`
- **Target:** Ahaan Kallat, *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, `arXiv:2610.40342v1` (2026-10-29), Section 14 **Question 14.10** (`\label{prob:gcdr}`: Q1 $g_3(n) \ne G_3(n)$ iff $n \equiv 30 \pmod{81}, n \ge 111$; Q2 $g_r(n) = G_r(n)$ for $r \ge 4$; $r=3$ exact forms for Q3/Q4).
- **Verdict:** **OPEN / PASS**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `721` snapshots):**
   - `2610.40342`, `Kallat` -> `citing_papers.*` (`OpenAlex cited_by=0; S2=0`), `trureturing` (`Library/FiniteGroups/kallat2026weightedpermutations.md`, `A378495` / `2610.15849`), `formal-conjectures-prs.*` (`#8038`, OEIS `A012780`).
   - `prob:gcdr`, `global gcd` -> **`0` hits** (`0/721`).
2. **Live GitHub (`gh` CLI) & `trureturing` `dev`:**
   - `gh search repos "2610.40342"`, `gh search prs "2610.40342"`, `gh search code '"prob:gcdr"'` -> `[]`.
   - `gh search issues "2610.40342"` -> automated `bguanmath/ArXiv_MathNT` digests only.
   - `gh search code 2610.40342` -> `rainwangphy/aftd-platform` (`OP-746`, formalizes definitions & published $n < 2(r+1)$ / Prop 11.3(i) helpers only, explicitly leaving Question 14.10 open), `chokmah-me/fragile-proof-audit` (audit of `2610.40342`), `mathesis-papers/10.5281-zenodo.23903308` (`A378495` only).
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` -> unrelated `KrizekIntegralityGcdRecordRefutation` / `SchulteShiftedProductGcdRowSumConvolution` only (`0` hits for `2610.40342` / `Kallat` / `gcdr`).
3. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?id_list=2610.40342` -> sole version `2610.40342v1` (`2026-10-29T16:04:37Z`); `au:Kallat` -> 5 entries, none newer or solving `prob:gcdr`.
   - `zenodo.org/api/records?q=2610.40342` -> `0`; `q=Kallat+permutation` -> `23903309` (`A378495` only).
   - `search_web` -> returns only `arXiv:2610.40342v1`.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all checked public sources confirm Question 14.10 (`prob:gcdr`) remains open.
