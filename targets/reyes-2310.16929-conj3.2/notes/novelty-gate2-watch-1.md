# Gate 2 Novelty Receipt (`watch-1`): `targets/reyes-2310.16929-conj3.2/`

- **Checked UTC:** `2026-11-27T09:58Z`
- **Target:** M. A. Reyes, C. Dalfó, and M. A. Fiol, *"On the spectra and spectral radii of token graphs"*, `arXiv:2310.16929v1` (`2023-10-25`, *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11, `DOI:10.1007/s40590-023-00583-3`), Section 3, Conjecture 3.2 (`\label{conjec-creix-alfa}`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2310.16929 Reyes`):**
   - `the-omega-institute/trureturing` has `Library/Eigenstructure/reyes2023tokenspectra.md` and `Problems/reyes-dalfo-fiol-2024-new-laplacian-layer-maxima.md` (which refutes Conjecture 3.3 on $\rho_k$ maxima only and explicitly leaves Conjecture 3.2 on $\alpha_k$ minima open); other `Reyes` hits are unrelated papers (`three-quarter-conjecture-24`, `two-photon-rabi`, `PVNP`).
   - `0` hits settling Conjecture 3.2 across `618` files (including `1337isnot1337/solved-conjectures` rebuilt `09:50:27Z`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2310.16929`):** `2310.16929v1` (`2023-10-25T18:52:24Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2310.16929&size=5`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues "2310.16929"` & `gh search prs "2310.16929"`):** `0` hits (`[]`).
5. **Web search (`"2310.16929" OR ("Reyes" "3.2" "eigenvalue" OR "graph" "adjacency")`): `0` refutations of Conjecture 3.2 found.
