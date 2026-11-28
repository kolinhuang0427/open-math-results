# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/say-2611.32633-bqtisp-sublog/`

- **Target:** A. C. Cem Say, *Lower space bounds for polynomial-time quantum computation*, `arXiv:2611.32633v1` (`2026-11-24`), **Section 5** (*Concluding remarks*, `main.tex` L1924–1928): whether the $\mathsf{BQTISP}(n^{O(1)}, o(s(n))) \subsetneq \mathsf{BQTISP}(n^{O(1)}, O(s(n)))$ sublogarithmic space hierarchy extends to general $s(n) \in \omega(\log\log n) \cap o(\log n)$ (**YES** for every monotone, doubling-smooth, log-constructible $s(n)$; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T23:14:33Z` – `2026-11-27T23:15:08Z`
- **Verdict:** **PASS — OPEN** (no competing or prior resolution of the Section 5 general sublogarithmic $\mathsf{BQTISP}$ hierarchy question found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `877` files across `958` cataloged repos, post-Sweep 29) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32633" "say-2611.32633" "BQTISP" "BPTISP" "Cem Say" "quantum space hierarchy" --max-per-file 0 --max-total 30` -> `15` lines across `6/877` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},citing_papers.{json,md},last_sweep_report.json,state.json}` entries for `2611.32633v1` `OpenAlex cited_by=0; S2=0` only).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T23:14:40Z`–`23:15:04Z`):**
   - `gh search code` for `"2611.32633"`, `"BQTISP"`, and `repo:the-omega-institute/trureturing BQTISP` -> `[]` (`0` hits on all three).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo & Web (`2026-11-27T23:01Z`–`23:15:08Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2611.32633` or `bqtisp`.
   - `https://export.arxiv.org/api/query?id_list=2611.32633` -> `2611.32633v1` sole version (`[cs.CC]`).
   - `https://hexagonmath.org/api/v1/works` (`1,692` works; `q=2611.32633`, `q=BQTISP` -> `total=0`), `papex.org` (`20` records, checked Sweep 29 `23:01Z` -> `0`), `Zenodo` (`"2611.32633"` -> `0`), `search_web` returns only `arXiv:2611.32633v1` and mirrors (`researchgate.net`, `theory.report`, `themoonlight.io`) of the preprint itself.
4. **Independent Verifier Verification (`@audit-2` PASS `#2119`):**
   - Executed `.venv/bin/python -u targets/say-2611.32633-bqtisp-sublog/notes/check-check-1.py` -> exited `0` (`LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True`, `FAMILY_sqrt_log` / `three_quarter_log` / `log_div_loglog` / `loglog_mul_logloglog: PASS`, `PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach).
