# Gate 3 Novelty Receipt (`watch-1`): `targets/mbirika-2301.05758-ques30/`

- **Checked UTC:** `2026-11-27T10:20:52Z`–`2026-11-27T10:20:58Z` (post-`AUDIT.md` re-audit PASS)
- **Target:** aBa Mbirika, Janee Schrader, and Jürgen Spilker, *"Pell and associated Pell braid sequences as GCDs of sums of $k$ consecutive Pell, balancing, and related numbers"*, `arXiv:2301.05758v3` (*J. Integer Sequences* 26(6), 2023, Art. 23.6.4), Section 6.1, **Question 30** ($\mathcal{G}_C^2(k), \mathcal{G}_B^2(k), \mathcal{G}_c^2(k), \mathcal{G}_b^2(k)$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2301.05758" "Mbirika" "Question 30" "ques30"`):** Matched `5/618` files, all referencing either `the-omega-institute/trureturing`'s `MbirikaAssociatedPellGcdEntryPointRefutation` (Conjecture 32 only), `Library/ArithUnits/fiebigmbirikaspilker2025lucas.md` (`2408.14632`), or `watch/snapshots/arxiv/` citing `2204.12626`; `0` hits for Question 30 across `618` files (`1337isnot1337/solved-conjectures` refreshed at `10:20Z`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2301.05758"`):** `2301.05758v3` (`2023-06-28T16:23:02Z`, *J. Integer Seq.* 26(6) 2023) remains the latest version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2301.05758&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search prs/repos "2301.05758"`):** Only `the-omega-institute/trureturing#9100` (Conjecture 32 refutation); `0` repos. (`gh search issues "2301.05758"` hit HTTP 403 API rate limit at `10:20:57Z`; `09:48Z` Gate 2 check showed only `#9058` for Conjecture 32.)
5. **Web search (`"2301.05758" OR ("Mbirika" "Question 30" "Padovan" OR "Fibonacci" OR "Perrin")`): `0` resolutions of Question 30 found.

## Coverage Limits
- `gh search issues "2301.05758"` hit GitHub HTTP 403 search rate limit at `2026-11-27T10:20:57Z` (`gh search prs`, `gh search repos`, local `trureturing` snapshot, live arXiv, Zenodo, and web search all succeeded with `0` hits for Question 30).
