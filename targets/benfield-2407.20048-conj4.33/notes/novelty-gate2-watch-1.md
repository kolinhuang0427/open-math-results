# Gate 2 Novelty Receipt (`watch-1`): `targets/benfield-2407.20048-conj4.33/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Target:** Brennan Benfield and Oliver Lippard, *"Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers"*, `arXiv:2407.20048v2` (`2025-01-30`), Section 4.2, Conjecture 4.33 (`\label{even-K-exceptions}`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2407.20048 "Question 4.33" "Conjecture 4.33"`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`). Also `grep -iE "benfield|pisano|lucas" watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt | grep -i "^Problems/"` shows only `pisano-order-range-refutation.md` (Conjecture 5.3(v)) and unrelated Lucas/Pisano problems.
2. **Live GitHub (`gh search issues "2407.20048"` & `gh search prs --repo the-omega-institute/trureturing "Benfield"` & `gh api repos/the-omega-institute/trureturing/issues/23317`):**
   - `the-omega-institute/trureturing#9448` / PR `#9451` (merged `2026-09-22`): settles only Conjecture 5.3(v), unrelated to Conjecture 4.33.
   - `the-omega-institute/trureturing#23317` (`state: open`, `0` comments): open preregistration on **Question 4.34** (`arXiv:2407.20048v2`). Its body explicitly notes *"neither the claim nor its negation has been proved in Lean"* and *"Conjecture 4.33 of the source is excluded as an already implied neighboring statement"* (not proved/settled on `main`).
   - `the-omega-institute/trureturing` `D5/S1/Recurrence/LucasEvenPeriods.lean` and `Library/ArithUnits/fiebigmbirikaspilker2025lucas.md` address `arXiv:2408.14632v2` (Fiebig–Mbirika–Spilker, whose converses assume $p$ or $m$ odd and companion vs trace periods), not Conjecture 4.33 (`even-K-exceptions`).
3. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2407.20048,2506.20778` & `2408.14632`):** `2407.20048v2` (`2025-01-30T20:24:47Z`) remains the latest arXiv version; primary `fiborder.tex` lines 675–682 still state `\label{even-K-exceptions}` as an open conjecture.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=10` and `q=Benfield+Lippard&size=10`):** `0` hits for `2407.20048`; `Benfield+Lippard` hits are unrelated biology/arts records.
5. **Web search (`"2407.20048" "Conjecture 4.33" OR "even-K-exceptions" OR "Fibonacci Quarterly" "Benfield" "Lippard"`):** Surfaced only `arXiv:2407.20048` itself; no settlement of Conjecture 4.33 found.

## Coverage Limits
- Journal publication *The Fibonacci Quarterly* 63(2) (2025), 240–258 (`doi:10.1080/00150517.2025.2460555`) is paywalled (HTTP 403 per prior access records) and was not inspected beyond `arXiv:2407.20048v2`.
- OpenAlex API returned HTTP 429; `gh search prs "2407.20048"` returned `[]` before GitHub Search API rate-limited later calls.
