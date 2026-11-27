# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A187430/`

- **Checked UTC:** `2026-11-27T10:12:49Z`–`2026-11-27T10:13:12Z`
- **Target:** OEIS `A187430` (rev. 55) — Benedict W. J. Irwin (Jan 13 2017) Conjecture: $1 + \sum_{n\ge 0} a(n)(-1)^n x^{n+1}/(1-x)^{2n+2} = C(x)$, the Catalan numbers `A000108` g.f.
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A187430" "Benedict W. J. Irwin" "187430"`):** `0` lines across `0/618` files (no matches in `1337isnot1337/solved-conjectures`, `trureturing*`, `openai/math`, `formal-conjectures`, or `watch/snapshots/discovered/`).
2. **Zenodo `23112421` OEIS index (`grep -n "A187430" watch/snapshots/zenodo-23112421-oeis-ids.md`):** No match.
3. **Live OEIS (`https://oeis.org/search?q=id:A187430&fmt=json`):** `number: 187430`, `revision: 55` (`time: 2024-01-17T09:35:29-05:00`), `FORMULA` still lists `Conjecture: 1 + Sum_{n>=0} a(n)*(-1)^n x^(n+1)/(1-x)^(2*n+2) = C(x)... - _Benedict W. J. Irwin_, Jan 13 2017` with no proof note.
4. **Live Zenodo API (`q=A187430`, `q="Benedict W. J. Irwin" OR "187430"`):** `A187430` returned `0` hits; `"Benedict W. J. Irwin" OR "187430"` returned `4` unrelated records (only OEIS paper `23316730` concerns `A005867`, not `A187430`).
5. **Live GitHub (`gh search issues/prs/repos "A187430"`):** `0` issues, `0` PRs, `0` repos.
6. **Web search (`"A187430" "Irwin" OR "Catalan" OR "proved"`):** Only points to OEIS `A187430` (still marked `Conjecture`) and `arXiv:1609.06473` (basketball walks / knight's paths); `0` proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~22 min before this check); live `gh search` at `10:12Z` found no GitHub hits.
