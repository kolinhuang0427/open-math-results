# Gate 2 Novelty Receipt — `targets/cai-2610.02047-plog-reg/` (`watch-1`)

- **Target:** `targets/cai-2610.02047-plog-reg/` (*Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth*, Shaowei Cai and Ziqun Li, `arXiv:2610.02047v1` [`cs.CC`], §8 lines 4025–4031: FPT-sized regular resolution refutations parameterized by partially log-weighted incidence treewidth $\mathrm{tw}_{\mathrm{plog}}^*(F)$)
- **Checked At (UTC):** `2026-11-27T21:31:01Z`–`2026-11-27T21:31:26Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions of regular resolution FPT-size parameterized by $\mathrm{tw}_{\mathrm{plog}}^*(F)$ found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.02047" "tw_plog" "partially log-weighted" "Short Resolution Refutations"`
   - Result: `0` lines across `0/855` files (`0` settlements or competing snapshots).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs "2610.02047"` -> `[]`; `gh search prs '"Short Resolution Refutations"'` -> `[]`.
   - `gh search issues "2610.02047"` -> `2` unrelated issues (`trureturing#25977` Yuhao Han `2611.01890`, `j15marti/pnp#3`); `gh search issues '"Short Resolution Refutations"'` -> `[]`.
   - `gh search code '"2610.02047"'` -> `1` unrelated bibliography reference (`jtraverso/erdos-81-chordal-clique-partitions/publication/aixiv/PUBLICATION_RECEIPT.json`); `gh search code '"partially log-weighted"'` -> `[]`.
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T21:31:01Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `fce596932e0bf104eff9da1b91f9da2027a851d7` (*"Prove countable pair self-rainbows by tree fusion (#1087)"*) — unrelated.
4. **arXiv / Zenodo / Crossref / ECCC / Web Search:**
   - arXiv API (`id_list=2610.02047`): sole version `2610.02047v1` (`2026-10-01T16:56:03Z`).
   - Zenodo API (`q=2610.02047`): `0` hits.
   - Crossref (`query=2610.02047`, `query.title=Short+Resolution+Refutations+for+CNFs+with+Bounded+Weighted+Incidence+Treewidth`): `0` matching DOIs.
   - `search_web` on `eccc.weizmann.ac.il` (`"regular resolution" "treewidth" OR "plog" OR "2610.02047"`): returned `TR26-332` (*Resolution Is Automatable on Tseitin Formulas*, Itsykson & Smirnov, primal treewidth) — unrelated; `0` matches on $\mathrm{tw}_{\mathrm{plog}}^*(F)$.
   - `search_web` (`"2610.02047" ...`, `"Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth" ...`): returns only `arXiv:2610.02047v1` and `emergentmind.com` digest of `2610.02047v1` itself; `0` follow-up proofs for regular resolution under $\mathrm{tw}_{\mathrm{plog}}^*(F)$.
