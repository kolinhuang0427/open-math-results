# Gate 2 Novelty Check — guo-2310.15207-conj6.8 (watch-5)

- **Checked UTC:** 2026-11-27T11:01:06Z – 2026-11-27T11:01:24Z
- **Result:** **PASS** (no prior proof or settlement of Victor J. W. Guo `arXiv:2310.15207v1` / *RACSAM* 119 (2025) §6 Conjecture 6.8 `conj:8` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2310.15207 "Conjecture 6.8" "conj:8"`
   - Result: `0` lines across `0/636` snapshot files.

2. **arXiv / Semantic Scholar citing papers:**
   - `id:2310.15207`: sole version `2310.15207v1` (`2023-10-23`, published as *RACSAM* `10.1007/s13398-025-01762-9`, 2025).
   - `abs:2310.15207`: `0` citing/matching abstracts.
   - All 3 S2 citing works of `10.1007/s13398-025-01762-9` previously identified (`arXiv:2608.13818` `.tex` explicitly checked for `6.8`/`conj:8`/`2310.15207` -> `[]`; plus `10.1007/s00025-026-02719-z` and `10.1007/s13398-025-01816-y` inspected via Springer abstracts) are distinct from Conjecture 6.8.

3. **Zenodo / Web:**
   - Zenodo live API (`2310.15207`): `0` hits.
   - `search_web` (`"2310.15207" "Conjecture 6.8" OR "6.8" "Guo" "Phi_n(q)^2" proved`): confirms Conjecture 6.8 remains an open conjecture from Section 6 of `2310.15207`.

## Coverage Limits
- Local snapshot coverage reflects `636` files; Springer paywalled PDFs for `10.1007/s00025-026-02719-z` and `10.1007/s13398-025-01816-y` checked via title/abstract, and full `.tex` checked for `2608.13818`.
