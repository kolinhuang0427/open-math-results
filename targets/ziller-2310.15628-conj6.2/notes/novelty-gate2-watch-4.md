# Gate 2 Novelty Receipt — `targets/ziller-2310.15628-conj6.2/` (`watch-4` Formal Libraries Slice)

- **Verdict:** `PASS` (for `google-deepmind/formal-conjectures` and `leanprover-community/mathlib4`)
- **Checked UTC:** `2026-11-27T03:17:20Z` – `2026-11-27T03:18:48Z`
- **Watcher:** `watch-4` (Formal libraries slice)

## Sources Checked
1. **Local snapshots (`watch/snapshots/formal/`):**
   - `formal-conjectures-files.tsv` (2,200 `.lean` files), `formal-conjectures-prs.jsonl` (535 PRs), `formal-conjectures-issues.jsonl` (136 issues), `formal-conjectures-commits.jsonl` (100 commits).
   - `mathlib-v4.36.0-files.tsv` (8,847 `.lean` files), `mathlib-v4.36.0-decls.tsv` (246,423 declarations), `mathlib-v4.36.0-citations.tsv` (163 citations/refs), `mathlib4-prs.jsonl` (351 PRs), `mathlib4-commits.jsonl` (209 commits).
2. **Live GitHub (`gh search` read-only):**
   - `google-deepmind/formal-conjectures` (code & issues)
   - `leanprover-community/mathlib4` (code & issues)

## Exact Queries Run
- `grep -niE "2310\.15628|Ziller" watch/snapshots/formal/*.tsv watch/snapshots/formal/*.jsonl` -> 0 matches (`NO_MATCH_ZILLER`).
- `grep -niE "totient" watch/snapshots/formal/formal-conjectures-files.tsv formal-conjectures-{prs,issues}.jsonl mathlib4-{prs,commits}.jsonl` -> 3 matches (`CarmichaelTotient.lean`, `LehmerTotient.lean`, `mathlib4#46556`).
- `grep -niE "totient.*inj|inj.*totient|totient.*sq|sq.*totient" watch/snapshots/formal/mathlib-v4.36.0-decls.tsv` -> 0 matches.
- `grep -i "totient" watch/snapshots/formal/mathlib-v4.36.0-decls.tsv` -> inspected all 70 `totient` declarations (`Mathlib/Data/Nat/Totient.lean`, `PowModTotient.lean`, `Carmichael.lean`, etc.).
- `gh search code "2310.15628" --repo google-deepmind/formal-conjectures` -> 0 results.
- `gh search code "2310.15628" --repo leanprover-community/mathlib4` -> 0 results.
- `gh search issues "2310.15628 OR Ziller" --repo google-deepmind/formal-conjectures` -> 0 results.
- `gh search issues "totient injective" --repo leanprover-community/mathlib4` -> 0 results.
- `gh search code "totient" "injective" --repo leanprover-community/mathlib4` -> 20+ matches (unrelated injectivity lemmas in files importing `Mathlib.Data.Nat.Totient`; no totient injectivity theorem).
- `gh search code "totient" "distinct" --repo google-deepmind/formal-conjectures` -> 4 matches (`ErdosProblems/1004.lean`, `360.lean`, `418.lean`, `416.lean`; none on $\varphi(x)/x^2$).
- `gh search code "Ziller" --repo google-deepmind/formal-conjectures` -> 0 results.

## Near Misses and Why They Do Not Settle the Exact Statement
- `Mathlib/Data/Nat/Totient.lean`: `eq_or_eq_of_totient_eq_totient` and `Even.eq_of_totient_eq_totient` only prove $\varphi(2n)=\varphi(n)$ for odd $n$ and basic multiplicity identities; neither establishes injectivity of $\varphi(x)/x^2$.
- `FormalConjectures/Wikipedia/{CarmichaelTotient,LehmerTotient}.lean` and `ErdosProblems/1004.lean`: treat $\varphi(n)$ multiplicity/distinctness for $\varphi(n)$ itself, not $\varphi(x)/x^2$.
- `mathlib4#46556`: docstring update in `DirichletCharacter/Orthogonality.lean`.

## What Was Not Covered
- Non-formal sources (arXiv, OEIS, competing non-formal GitHub repos like `1337isnot1337/solved-conjectures`, `trureturing`, `openai/math`), which are covered by `@watch-2` and `@watch-5`.
- Closed PRs/issues in `formal-conjectures` or `mathlib4` older than our indexed update window whose bodies omit `"2310.15628"`, `"Ziller"`, or `"totient" + "injective"/"distinct"`.
