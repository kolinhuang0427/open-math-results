# Gate 3 Novelty Receipt — `ziller-2310.15628-conj6.2`

- **UTC Time:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 586 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`): `0` hits for `2310.15628`, `varphi(x)/x^2`, `phi(x)/x^2`, `Ziller`.
   - `.venv/bin/python tools/novelty_grep.py 2310.15628 "varphi(x)/x^2" "phi(x)/x^2" "Ziller"` -> hits only in `plasma-ai__erdos`/`techno-optimist__erdos-frontier-atlas` (Erdős #854 Ziller–Morack table, unrelated) and `watch/snapshots/arxiv/citing_papers.*` (`arXiv:2604.19646`, Ziller's own April 2026 follow-up, directly checked in `AUDIT.md` and confirmed not to resolve Conjecture 6.2).
2. **Live GitHub (`gh search`) & Zenodo (`2026-11-27T08:48Z`):**
   - `gh search issues "2310.15628"` -> `trureturing#24177` only (Mike Klein OEIS `A349824`, unrelated).
   - `gh search code "2310.15628"` -> `ehijano/rss_fetch` (arXiv RSS mirror) and `kolinhuang0427/open-math-results` (unrelated `biswas` Gate 3 receipt); `0` competing proofs.
   - `https://zenodo.org/api/records?q=2310.15628&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues, private repositories, and arXiv papers not mentioning `2310.15628` or `Ziller` in indexed text.
