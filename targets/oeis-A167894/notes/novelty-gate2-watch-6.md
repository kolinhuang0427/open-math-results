# Gate 2 Novelty Check — targets/oeis-A167894/ (watch-6)

- **UTC Timestamp:** `2026-11-27T10:55:21Z`
- **Target:** `targets/oeis-A167894/` (`status: candidate`, `owner: scout-5`) — Sergei N. Gladkovskii (Nov 19 2013) continued fraction conjecture $Q(0)$ where $Q(k) = 1 + kx - (k+1)x/Q(k+1)$ for $1 / \sum_{k \ge 0} k! x^k$.
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py A167894 "167894"`
   - Result: `# 0 lines across 0/635 files in 1.46s` (incl. `zenodo-23112421-oeis-ids.md`, `ai-village-graffiti-verification.md`, Sweep 4 `discovered/`).
   - Cross-reference check `A003319` (`2 - 1/\sum k! x^k`): `0` matches in `635` snapshot files; `insorrowmeow/oeis-sequence-proofs` lists only `Pisot-A048625.ru.txt` for Gladkovskii (`0` matches on `A167894`/`A003319`).
2. **Live OEIS (`A167894` rev `83`, `2026-01-02T20:45:39-05:00` & cross-ref `A003319` rev `462`):**
   - `A167894` still explicitly lists `G.f.: conjecture: Q(0), where Q(k) = 1 + k*x - (k+1)*x/Q(k+1).` without proof.
   - **Near-miss disclosure:** `A003319` (`2 - A167894`) includes Peter Bala's May 23 2017 entry `1 + x/(1 + x - 2*x/(1 + 2*x - 3*x/(1 + 3*x - ...)))`, which equals `2 - Q(0)`, also stated as a bare formula without proof.
3. **Zenodo API (`https://zenodo.org/api/records?q=%22A167894%22&size=5`):** `zenodo_hits: 0`.
4. **arXiv API (`all:A167894`):** `<opensearch:totalResults>0</opensearch:totalResults>`.
5. **GitHub Search (`gh search repos "A167894"`, `gh search issues "A167894"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear; no paper proving Gladkovskii's `Q(k)` continued fraction for `1/\sum k! x^k`.

## Coverage Limits
- `gh search code` not run after `0` repo/issue/local-snapshot hits under rate-limit budget; `A003319` OEIS links (Hopf algebra / divergent series references) checked at formula/title level only.
