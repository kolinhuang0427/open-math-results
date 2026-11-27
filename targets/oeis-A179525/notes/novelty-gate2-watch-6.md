# Gate 2 Novelty Check — targets/oeis-A179525/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:59:43Z`
- **Target:** `targets/oeis-A179525/` (`status: candidate`, `owner: scout-5`) — Sergei N. Gladkovskii (May 13 2013) 3-step continued fraction conjecture $Q(0)$ AND Peter Bala (May 16 2017) even-product generating function conjecture $\sum_{n \ge 0} (1+x)^{2n+1} \prod_{k=1}^{2n}(1-(1+x)^k)$ for `A179525` (`\sum_{n\ge 0} \prod_{k=1}^n ((1+x)^k - 1)`).
- **Verdict:** **PASS** (no settled proof or counterexample found for either statement).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A179525 "179525"` (now 636 files including `watch/snapshots/zenodo-23114921-oeis-ids.md`)
   - Result: `3` lines across `3/635` files — inspected completely:
     - `AlexenderSokolov/cross-theory-formal-database`: `editable-corpus/items/179525_author_proof.tex` verified via `gh api` to be Anna Weigandt's *"Changing Bases with Pipe Dream Combinatorics"* (unrelated item index `179525`).
     - `mathlib4-prs.{json,tsv}`: CI workflow run URL `45917952569` (substring false positive).
     - `watch/snapshots/zenodo-23114921-oeis-ids.md` (`10.5281/zenodo.23114921`, Blanco Gómez `2026-10-03`, `43` OEIS IDs extracted from all 10 PDF pages + `verify_core.py`): `A179525` **not present** (`False`).
2. **Live OEIS (`A179525` rev `74`, `2026-04-28T18:58:30-04:00` & cross-ref `A158690` rev `52`):**
   - Both Gladkovskii's `Q(k)` (`Conjecture.`) and Bala's `Sum_{n >= 0} (1+x)^(2*n+1)*Product_{k=1..2*n} (1-(1+x)^k)` (`Conjectural g.f.`) remain open in `A179525` (`rev. 74`) and cross-referenced `A158690` (`rev. 52`).
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A179525%22&size=5`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A179525`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos "A179525"`, `gh search issues "A179525"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear.

## Coverage Limits
- `gh search code` not run after `0` repo/issue/target-snapshot hits under rate-limit budget; `arXiv` searched via literal OEIS ID `A179525`.
