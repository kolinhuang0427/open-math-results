# Gate 3 Novelty Receipt — `targets/cai-2610.02047-plog-reg/` (`watch-1`)

- **Target:** `targets/cai-2610.02047-plog-reg/` (*Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth*, Shaowei Cai and Ziqun Li, `arXiv:2610.02047v1` [`cs.CC`], §8 lines 4025–4031: FPT-sized regular resolution refutations parameterized by partially log-weighted incidence treewidth $\mathrm{tw}_{\mathrm{plog}}^*(F)$)
- **Checked At (UTC):** `2026-11-27T21:52:08Z`–`2026-11-27T21:52:24Z` (extending Gate 2 at `21:31:01Z`)
- **Verdict:** **PASS** (novel; `0` prior resolutions found)

## Exact Checks Run & Observed Results

1. **Snapshot grep (from Gate 2, `855` files):** `0/855` snapshot hits (`0` settlements).
2. **GitHub PRs / Issues / Code Search (`21:52:08Z`):**
   - `gh search prs "2610.02047"` -> `[]`
   - `gh search issues "2610.02047"` -> `2` unrelated (`trureturing#25977` Yuhao Han `2611.01890`, `j15marti/pnp#3`)
   - `gh search code '"partially log-weighted"'` -> `[]`
3. **Live `1337isnot1337/solved-conjectures` HEADs (`21:52:08Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `d3afc6a36d0d14219077ff770f7c33488b76bd76` (*"Audit the original one-sided conjecture and preserve the scope distinction (#1092)"*) — unrelated.
4. **arXiv / Zenodo / ECCC / Web Search (`21:52:08Z`–`21:52:18Z`):**
   - arXiv API (`id_list=2610.02047`): sole version `2610.02047v1` (`2026-10-01T16:56:03Z`).
   - Zenodo API (`q=2610.02047`): `0` hits.
   - `search_web` (incl. `site:eccc.weizmann.ac.il`): returns only `arXiv:2610.02047v1` / ResearchGate entry for `2610.02047v1`; `0` follow-up resolutions of regular resolution FPT-size parameterized by $\mathrm{tw}_{\mathrm{plog}}^*(F)$.
5. **Independent Check Execution (`#2066`):**
   - Command: `.venv/bin/python -u targets/cai-2610.02047-plog-reg/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `JOIN_COUNTEREXAMPLE: L165_fails=True, corrected_regular_ok=True, len=6`
     - `COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS`
     - `AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS`
     - `PASS`
