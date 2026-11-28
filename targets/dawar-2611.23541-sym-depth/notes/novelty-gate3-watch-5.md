# Gate 3 Novelty & Checker Receipt — `dawar-2611.23541-sym-depth` (`watch-5`)

- **Timestamp:** `2026-11-27T20:56:44Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *"Depth Hierarchies for Symmetric Algebraic Circuits"*, `arXiv:2611.23541v1` (`2026-11-17T21:49:23Z`, `submitted to STOC 2027`), §1.2 depth-3/4 symmetric reduction.

## Fresh Live Novelty Checks (`20:56:44Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2611.23541" "Dwivedi" "Seppelt" "symVP" "symVAC" "symVBP"`):** `0` settlements (`20` lines across `7/849` files: `arxiv_submissions.{json,md}`, `state.json`, `discovered/{CATALOG.md,catalog.json,tseppelt__lax-symmetric-depth-reduction.json}` [author Lean repo `Lax461425` of `2611.23541v1` only], and unrelated `Rattan & Seppelt (2023)` / `Srashti Dwivedi`).
- **arXiv API:** `2611.23541v1` (`2026-11-17T21:49:23Z`) sole version.
- **OpenAlex / OpenCitations / Zenodo:** `W7236732928` (`10.48550/arXiv.2611.23541`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search issues/prs "2611.23541"` `0` hits; `trureturing` PRs up to `#34981` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2611.23541` itself; no follow-up settlement.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/dawar-2611.23541-sym-depth/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/dawar-2611.23541-sym-depth/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (Theorems 1–2 thresholds & Lemma 1 $S_n$ generation; Lemma 2 balanced 2-level decomposition + normalised pruning $d=1\dots 100$ incl. non-squares; Theorem 3 depth-4 circuit & $\Gamma_n$-invariance $P_4,P_5$; Theorem 4 Fischer + truncated exp + $\mathbb{Q}[t]/(\mu)$ interpolation descent).
