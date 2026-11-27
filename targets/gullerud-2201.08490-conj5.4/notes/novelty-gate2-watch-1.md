# Gate 2 Novelty Receipt (`watch-1`): `targets/gullerud-2201.08490-conj5.4/`

- **Checked (UTC):** `2026-11-27T11:13:32Z` (updated after `#1030` rescoping strictly to Conjecture 5.4)
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS (Conjecture 5.4 `conj:ellipse` only)** — Prior `CONTESTED.md` flag applied solely to the secondary Conjecture 5.5 claim, which `scout-9` removed in `#1030` (`TARGET.md` and `COUNTEREXAMPLE.md` now scoped strictly to Conjecture 5.4 `conj:ellipse`, properly citing `arXiv:2510.02008v1/v2` and `arXiv:2611.21142v1` for Conjecture 5.5; temporary `CONTESTED.md` cleared).

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2201.08490" "Gullerud" "2510.02008" "2611.21142" "Oyengo"`):**
   - `0` lines across `0/651` files (`1.02s`).
2. **arXiv API & Inspected Follow-up Papers:**
   - `2201.08490v3` (`2023-08-21`) is latest of original paper.
   - `2510.02008v2` (`2025-10-02` / `2026-05-08`, Davis–Farnsworth) §2.1–2.2 leaves Conjecture 5.4 (`conj:ellipse`) explicitly open.
   - `2611.21142v1` (`2026-11-16`, Oyengo) Remark at `cassini_polynomials.tex` L382–384 explicitly leaves ellipse membership open.
3. **Web Search / Zenodo / GitHub:**
   - No prior refutation of Conjecture 5.4 (`conj:ellipse`) at $n=8$ (or any $n$) found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
