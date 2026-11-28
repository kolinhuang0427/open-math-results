# Gate 2 Novelty Receipt — `targets/dobson-2611.13347-ising-clifford/` (`watch-1`)

- **Target:** `targets/dobson-2611.13347-ising-clifford/` (*Computational Power of Clifford and Ising Quantum Computers*, Sawyer Dobson and Zhenghan Wang, `arXiv:2611.13347v1` [`quant-ph`, `cs.CC`, `math.QA`], §5 `sections/5.tex` L11 Problem (3): ancilla-assisted Ising braiding vs Clifford, `PUSB`/`LUSB` vs `PUSC`/`LUSC`)
- **Checked At (UTC):** `2026-11-27T22:36:41Z`–`2026-11-27T22:37:08Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions of §5 Problem (3) found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.13347" "Ising anyon" "LUSC" "PUSC" "Computational Power of Clifford and Ising"`
   - Result: `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` entries announcing `2611.13347v1` itself (plus unrelated substring hits on `LUSC`/`luschny` and statistical-mechanics Ising files; `0` settlements).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs/issues "2611.13347"` -> `[]`; `gh search prs/issues '"Computational Power of Clifford and Ising"'` -> `[]`.
   - `gh search code '"2611.13347"'` -> `8` hits across `4` automated arXiv digest/inbox repos (`meat-daemon-404/pat-hot`, `LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `drmithileshkumar/quantumresearchcenter`, `Quantum-Research-Center/quantumresearchcenter`).
   - `gh search code '"PUSB" "LUSB"'` -> `[]`; `gh search code '"LUSC" "Ising"'` -> `[]`.
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T22:36:41Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `f3baa56462fe09d56940e4f131cd2ea2254b0134` (*"Exclude low fractional chromatic number and force edge expansion of extremizers"*) — unrelated.
4. **arXiv / Zenodo / Crossref / ECCC / Web Search:**
   - arXiv API (`id_list=2611.13347`): sole version `2611.13347v1` (`2026-11-09T23:19:02Z`).
   - Zenodo API (`q=2611.13347`): `0` hits.
   - Crossref (`query=2611.13347`, `query.title=Computational+Power+of+Clifford+and+Ising+Quantum+Computers`): `0` matching DOIs.
   - `search_web` (`site:eccc.weizmann.ac.il` and general web): returns only `arXiv:2611.13347v1` / ResearchGate entry for Dobson & Wang (`2611.13347v1`) itself; `0` ECCC matches and `0` follow-up papers settling §5 Problem (3).
