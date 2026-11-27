# Gate 2 Novelty Receipt — `targets/dawsey-2107.14284-conj5.1/` (`watch-4` Formal Libraries Slice)

- **Verdict:** `PASS` (for `google-deepmind/formal-conjectures` and `leanprover-community/mathlib4`)
- **Checked UTC:** `2026-11-27T07:56:12Z`
- **Watcher:** `watch-4` (Formal libraries slice)

## Sources Checked
1. **Local snapshots (`watch/snapshots/formal/`):**
   - `formal-conjectures-files.tsv` (2,200 `.lean` files), `formal-conjectures-prs.jsonl` (547 PRs), `formal-conjectures-issues.jsonl` (141 issues), `formal-conjectures-commits.jsonl` (100 commits).
   - `mathlib-v4.36.0-files.tsv` (8,847 `.lean` files), `mathlib-v4.36.0-decls.tsv` (246,423 declarations), `mathlib-v4.36.0-citations.tsv` (163 citations/refs), `mathlib4-prs.jsonl` (374 PRs), `mathlib4-commits.jsonl` (209 commits).
2. **Live GitHub (`gh search` read-only):**
   - `google-deepmind/formal-conjectures` (code & issues)
   - `leanprover-community/mathlib4` (code & issues)

## Exact Queries Run
- `grep -niE "2107\.14284|Dawsey|Just.*Schneider|Cesaro.*prime" watch/snapshots/formal/*.tsv watch/snapshots/formal/*.jsonl` -> 0 matches (`NO_MATCH_DAWSEY_SNAPSHOT`).
- `grep -niE "cesaro|LSeries|Dirichlet.*prime" watch/snapshots/formal/formal-conjectures-{files.tsv,prs.jsonl,issues.jsonl}` -> 0 matches (`NO_FC_MATCH`).
- `grep -niE "cesaro" watch/snapshots/formal/mathlib-v4.36.0-{decls,citations}.tsv` -> 2 matches (`Filter.Tendsto.cesaro_smul`, `Filter.Tendsto.cesaro` in `Mathlib/Analysis/Asymptotics/SpecificAsymptotics.lean`).
- `gh search code "2107.14284" --repo google-deepmind/formal-conjectures` -> 0 results.
- `gh search code "2107.14284" --repo leanprover-community/mathlib4` -> 0 results.
- `gh search code "Dawsey" --repo google-deepmind/formal-conjectures` -> 0 results.
- `gh search issues "2107.14284 OR Dawsey" --repo google-deepmind/formal-conjectures` -> 0 results.
- `gh search issues "2107.14284 OR Dawsey" --repo leanprover-community/mathlib4` -> 0 results.

## Near Misses and Why They Do Not Settle the Exact Statement
- `Mathlib/Analysis/Asymptotics/SpecificAsymptotics.lean` (`Filter.Tendsto.cesaro`, `Filter.Tendsto.cesaro_smul`): only proves standard Cesàro mean convergence for convergent sequences, not Abelian prime-index Dirichlet series limits $\sum_p f(\mathrm{idx}(p)) p^{-s} / \sum_p p^{-s}$.

## What Was Not Covered
- Non-formal sources (arXiv, journals, competing non-formal GitHub repos), which are covered by `@watch-1` and `@watch-5`.
- Closed PRs/issues in `formal-conjectures` or `mathlib4` older than our indexed update window whose bodies omit `"2107.14284"` and `"Dawsey"`.
