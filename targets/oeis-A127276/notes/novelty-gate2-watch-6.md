# Gate 2 Novelty Check — targets/oeis-A127276/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:17:13Z`
- **Target:** `targets/oeis-A127276/` (`status: candidate`, `owner: scout-5`) — R. J. Mathar (Dec 11 2010) conjectured closed form $a(n) = 2^n - n(n+1)2^{n-2}$ and g.f. $-(4x-1)(x-1)/(2x-1)^3$ for the Hankel transform of `A127275` (`(\sqrt{1-4x}-x)/(1-4x)`).
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results
1. **Local Snapshot Index (`tools/novelty_grep.py A127276 "127276"`):** `2` false-positive sha256 substring matches (`...12727606e...`) in `trureturing-source-theories`; `0` target hits across `651` snapshots (incl. `zenodo-23112421`, `zenodo-23114921`, Sweep 5).
2. **Live OEIS (`A127276` JSON):** `oeis_rev: 33`, `time: 2026-11-25T15:43:26-05:00` — Mathar's `Conjectured g.f.` remains open.
3. **Zenodo API (`"A127276"`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A127276`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos/issues "A127276"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear; no paper proving Mathar's `A127276` Hankel transform conjecture.

## Coverage Limits
- `gh search code` not re-run under rate-limit budget after `TARGET.md` Gate 1 checked `gh search code` = `0`.
