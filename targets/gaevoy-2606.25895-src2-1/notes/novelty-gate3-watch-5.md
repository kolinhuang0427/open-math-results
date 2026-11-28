# Gate 3 Novelty & Checker Receipt — `gaevoy-2606.25895-src2-1` (`watch-5`)

- **Timestamp:** `2026-11-27T19:48:55Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Nikita Gaevoy, *"The Power of Small Symmetries"*, `arXiv:2606.25895v1` / MFCS 2026 `DOI:10.4230/LIPIcs.MFCS.2026.97`, §§ 2 & 6 ($\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs. $\mathrm{Res}$).

## Fresh Live Novelty Checks (`19:48:55Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2606.25895" "Gaevoy" "SRC-II" "SRCII"`):** `0 lines across 0/826 files`.
- **arXiv API:** `2606.25895v1` (`2026-06-24T14:41:30Z`) sole version.
- **OpenAlex & OpenCitations:** `W7166252852` (`10.4230/LIPIcs.MFCS.2026.97`) `cited_by_count: 0`; OpenCitations `200 []`.
- **Zenodo:** `q=2606.25895` -> `0` hits.
- **GitHub & `trureturing`:** `gh search issues/prs "2606.25895"` `0` hits; `trureturing` PRs up to `#34959` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2606.25895` and MFCS 2026 Dagstuhl/LIPIcs abstract; no follow-up settlement.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/gaevoy-2606.25895-src2-1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
- **Command:** `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py`
- **Result:** Exit `0` — `PASS` (primary source quotes/macros/numbering, Lemma 1 exact integer/rational bounds $2\le n\le 40$, strict `1-SRC-II` Cook–Reckhow checker, Theorem 5 proofs $K_2\dots M_{20}$, `Res` unfolding + Lemma 2 restriction, $H_3$ 4-cycle simulation, and Lemma 3 expansion verified).
