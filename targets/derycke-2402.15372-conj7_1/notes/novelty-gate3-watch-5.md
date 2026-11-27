# Gate 3 Novelty Receipt — targets/derycke-2402.15372-conj7_1 (watch-5)

- **Checked UTC:** 2026-11-27T10:08:35Z (with 09:43Z full inspection of all 4 S2 citing preprints)
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2402.15372 ITCCTIsymmetry`):** matched only `watch/snapshots/arxiv/*` (own sweep entry `OpenAlex cited_by=3; S2=4` listing `2506.23237`, `2409.11811`, `2401.06488`, `2207.01997`, all inspected in Gate 2 with 0 resolution of `conj:ITCCTIsymmetry`); `0` solution hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'abs:"2402.15372"'`):** `0` entries (prior `09:43Z` check confirmed `2402.15372v3` latest version and `search_web` found `0` solutions).
3. **Live Zenodo & OpenAlex (`2402.15372`):** Zenodo `0` hits; OpenAlex `cited_by=3` (unchanged).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `2402.15372` in indexed metadata/abstracts are not covered.
