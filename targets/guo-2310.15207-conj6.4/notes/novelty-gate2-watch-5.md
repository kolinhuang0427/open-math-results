# Gate 2 Novelty Check — guo-2310.15207-conj6.4 (watch-5)

- **Checked UTC:** 2026-11-27T10:50:03Z – 2026-11-27T10:52:53Z
- **Result:** **PASS** (no prior proof or settlement of Victor J. W. Guo `arXiv:2310.15207v1` / *RACSAM* 119 (2025) §6 Conjectures 6.3 & 6.4 found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2310.15207 "Conjecture 6.4" "conj:4" "Phi_{n^s}" "q-supercongruence"`
   - Result: `22` lines across `16/635` files (all unrelated `Conjecture 6.4` / `Guo-Schlosser` matches; `0` hits for `2310.15207` or `Phi_{n^s}`).

2. **arXiv / Crossref / Semantic Scholar citations:**
   - `id:2310.15207`: sole version `2310.15207v1` (`2023-10-23`, published as *RACSAM* `10.1007/s13398-025-01762-9`, 2025).
   - `abs:2310.15207`: `0` citing/matching abstracts.
   - S2 citations of `10.1007/s13398-025-01762-9` / `ARXIV:2310.15207` (`3` citing papers checked):
     - `arXiv:2608.13818` (Wei & Wang, 2026): inspected full `.tex` (`26,658` chars) — ${}_6\phi_5$ summation formula, `0` hits for `2310.15207`, `6.3`, `6.4`, or `Phi_{n^s}`.
     - `10.1007/s00025-026-02719-z` (Guo & Zhu, 2026): inspected Springer abstract — $(6k+1)\frac{(1/2)_k (1/4)_k^2}{k!^3} 4^k$ Dwork-type supercongruences, distinct from Conjectures 6.3–6.4.
     - `10.1007/s13398-025-01816-y` (He & Wang, 2025): inspected Springer abstract — Gasper Karlsson–Minton summation generalizing Deines et al., distinct from Conjectures 6.3–6.4.

3. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2310.15207`): `0` hits.
   - `gh search issues "2310.15207"` & `gh search repos "2310.15207"`: `0` matches.
   - `search_web`: confirms Conjectures 6.3 & 6.4 were posed as open problems in `2310.15207` with no subsequent published resolution found.

## Coverage Limits
- Local snapshot coverage reflects `635` files; S2 citing-paper abstracts (and full `.tex` for `2608.13818`) were inspected, though full PDFs behind Springer paywalls for `10.1007/s00025-026-02719-z` and `10.1007/s13398-025-01816-y` were checked via title/abstract.
