# Gate 3 Novelty Receipt (`watch-1`): `targets/ciobanu-2604.22375-conj1/`

- **Checked UTC:** `2026-11-27T10:12:49Z`–`2026-11-27T10:13:12Z` (post-`AUDIT.md` re-audit PASS at `2026-11-27T10:11Z`)
- **Target:** Laura Ciobanu and Daniel Turaev, *"Visibly Pushdown Languages in Groups"*, `arXiv:2604.22375v1` (`2026-04-24`, full version of DLT 2026 paper), Section 3.1, Conjecture 1 (`\label{conjecture1}`: $\mathbf{VPL}^\forall = \mathbf{REG}^\forall$ in all finitely generated groups)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2604.22375" "Ciobanu" "Turaev" "word_complexity" "automorphism invariant"`):** `9` lines across `4/618` files (`watch/snapshots/arxiv/citing_papers.{json,md}` indexing this target with `OpenAlex cited_by=0; S2=0`; `the-omega-institute__trureturing/issues_and_prs.txt:259` `#34534` is an unrelated Turaev Conj 7.12 preregistration; `LightLikeProject__lightlike.json` is unrelated Turaev-Viro moves). `0` hits in `1337isnot1337/solved-conjectures`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2604.22375"`):** Sole version remains `2604.22375v1` (`2026-04-24T09:09:08Z`, *"Full version of the conference paper accepted to DLT 2026"*).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2604.22375&size=5` and exact-title `"Visibly Pushdown Languages in Groups"`):** `0` hits (`total: 0`); `q=Ciobanu+Turaev` returned unrelated biology records (`0` math/CS hits in top results).
4. **Live GitHub (`gh search issues/prs/repos "2604.22375"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (`"2604.22375" OR ("Ciobanu" "Turaev" "Conjecture 1")`): `0` competing proofs or refutations found (only `arXiv:2604.22375v1` itself).

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~22 min before this check); live `gh search issues/prs/repos` at `10:12Z` showed no new GitHub matches.
- Springer DLT 2026 proceedings version (`DOI: 10.1007/978-3-032-28404-4_8`) is noted in `AUDIT.md` as paywalled, with `arXiv:2604.22375v1` explicitly stating it is the full version.
