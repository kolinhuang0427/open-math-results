# Gate 3 Novelty & Checker Receipt — `say-2611.32633-bqtisp-sublog` (`watch-5`)

- **Timestamp:** `2026-11-27T23:14:39Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** A. C. Cem Say, *"Lower space bounds for polynomial-time quantum computation"*, `arXiv:2611.32633v1` (`2026-11-24T13:54:27Z`, `[cs.CC]`), §5 (`main.tex` L1924–1928) `BQTISP` sublogarithmic hierarchy in $\omega(\log\log n)\cap o(\log n)$.

## Fresh Live Novelty Checks (`23:14:39Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2611.32633" "BQTISP" "Cem Say"`):** `0` settlements (`15` lines across `6/877` files: `arxiv_submissions.{json,md}`, `citing_papers.{json,md}`, `last_sweep_report.json`, `state.json` entries for `2611.32633v1` only).
- **arXiv API:** `2611.32633v1` (`2026-11-24T13:54:27Z`) sole version.
- **OpenAlex / OpenCitations / Zenodo:** `W7239717187` (`10.48550/arXiv.2611.32633`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search issues "2611.32633"` `0` hits; `trureturing` PRs up to `#35032` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2611.32633` and earlier `2601.16695`/`2503.21582` (`0` follow-up settlements).

## Verification on Disk & Checker Run
- **Verified files present:** `targets/say-2611.32633-bqtisp-sublog/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/say-2611.32633-bqtisp-sublog/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (`LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True`; `FAMILY_sqrt_log`, `FAMILY_three_quarter_log`, `FAMILY_log_div_loglog`, `FAMILY_loglog_mul_logloglog` PASS).
