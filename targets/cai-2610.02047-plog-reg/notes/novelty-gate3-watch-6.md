# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/cai-2610.02047-plog-reg/`

- **Target:** Shaowei Cai and Ziqun Li, *Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth*, `arXiv:2610.02047v1` (`2026-10-01`), Section 8 (`main.tex` L4025–4031): whether every unsatisfiable CNF formula has an FPT-sized regular resolution refutation parameterized by partially log-weighted incidence treewidth $\mathrm{tw}_{\mathrm{plog}}^*(F)$ (**YES** — length $\le k^2(n+m)2^{O(w\log(w+2))} \le (n+m)^3 2^{O(w\log(w+2))}$; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T21:52:09Z` – `2026-11-27T21:52:32Z`
- **Verdict:** **PASS — OPEN** (no competing or prior resolution of the Section 8 $\mathrm{tw}_{\mathrm{plog}}^*(F)$ regular-resolution question found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `863` files across `944` cataloged repos, post-Sweep 26) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2610.02047" "cai-2610.02047" "tw_plog" "partially log-weighted" "plog-resolution" --max-per-file 0 --max-total 30` -> `3` lines across `2/863` files (`watch/snapshots/arxiv/citing_papers.{json,md}` recording `OpenAlex cited_by=0; S2=0`).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:52:10Z`–`21:52:30Z`):**
   - `gh search code '"2610.02047"'` -> `jtraverso/erdos-81-chordal-clique-partitions` (`PUBLICATION_RECEIPT.json` citing unrelated `aixiv.online/abs/2610.02047`).
   - `gh search code` for `"plog-resolution"`, `"regular resolution" "treewidth" "2610.02047"`, and `repo:the-omega-institute/trureturing 2610.02047` -> `[]` (`0` hits on all three).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo & Web (`2026-11-27T21:46Z`–`21:52:32Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2610.02047`, `plog`, or `regular resolution`.
   - `https://export.arxiv.org/api/query?id_list=2610.02047` -> `2610.02047v1` sole version (`2026-10-01`).
   - `https://hexagonmath.org/api/v1/works` (`1,692` works, checked Sweep 26; `q=2610.02047`, `q=plog-resolution` -> `total=0`), `papex.org` (`20` records, checked Sweep 26 `21:46Z` -> `0`), `Zenodo` (`0`), `search_web` returns only `arXiv:2610.02047` itself.
4. **Independent Verifier Verification (`@audit-2` PASS `#2066`):**
   - Executed `.venv/bin/python -u targets/cai-2610.02047-plog-reg/notes/check-check-1.py` -> exited `0` (`JOIN_COUNTEREXAMPLE: L165_fails=True, corrected_regular_ok=True, len=6`, `COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS`, `AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS`, `PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach).
