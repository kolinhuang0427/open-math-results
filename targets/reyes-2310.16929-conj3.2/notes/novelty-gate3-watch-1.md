# Gate 3 Novelty Receipt (`watch-1`): `targets/reyes-2310.16929-conj3.2/`

- **Checked UTC:** `2026-11-27T10:13:45Z`–`2026-11-27T10:14:15Z` (post-`AUDIT.md` PASS at `2026-11-27T10:13Z`)
- **Target:** M. A. Reyes, C. Dalfó, and M. A. Fiol, *"On the spectra and spectral radii of token graphs"*, `arXiv:2310.16929v1` (`2023-10-25`, *Bol. Soc. Mat. Mex.* 30 (2024), Art. 11), Section 3, Conjecture 3.2 (`\label{conjec-creix-alfa}`, refuted by $G = C_6$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "2310.16929" "Reyes" ...`):** Only existing `the-omega-institute/trureturing` files (`Library/Eigenstructure/reyes2023tokenspectra.md`, `Problems/reyes-dalfo-fiol-2024-new-laplacian-layer-maxima.md`, which refutes Conjecture 3.3 on $\rho_k$ maxima only) plus unrelated `Reyes` entries (`dalfofiolreyes2026threequarters`, `reyesbustos2026twophotonrabi`, `rickyjreyes/PVNP`, Girondo–Reyes-Monsalve hyperbolic packings). `0` settlements of Conjecture 3.2 across `618` snapshot files.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "...,2310.16929,..."`):** Sole version remains `2310.16929v1` (`2023-10-25T18:52:24Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2310.16929&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs "2310.16929"`):** `0` issues, `0` PRs.
5. **Web search (`"2310.16929" OR ("Reyes" "Conjecture 3.2" "Shannon capacity")`): `0` refutations or settlements of Conjecture 3.2 found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~23 min before this check); live `gh search issues/prs` at `10:13Z` showed no new GitHub matches.
