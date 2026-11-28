# Gate 2 Novelty Receipt — `targets/radici-2609.07769-open/` (`watch-1`)

- **Target:** `targets/radici-2609.07769-open/` (*A Note on Binary Quadratic Systems and Their Relation to Complexity Theory*, Gabriele Radici & Massimiliano Sala, `arXiv:2609.07769v2` [`cs.IT`, `cs.CC`, `cs.CR`, `math.AC`, `math.AG`], §7 `main-v32.tex` L1498–1527: whether $\alpha_1 > \alpha_0$ holds over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$)
- **Checked At (UTC):** `2026-11-27T23:33:03Z`–`2026-11-27T23:33:23Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$ found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.07769" "Radici" "alpha_1" "MQ_1" "MQ_0"`
   - Result: `watch/snapshots/arxiv/*` (`2609.07769v2` entry + `last_sweep_report.json`) and `AlexenderSokolov__cross-theory-formal-database.json` (`editable-corpus/licenses/arxiv-2609.07769-CC-BY-4.0.txt`) only (`0` settlements).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs "2609.07769"` -> `[]`; `gh search issues "2609.07769"` -> `[]`.
   - `gh search code '"2609.07769"'` -> `1` census JSONL entry (`uninhibited-scholar/cost-evidence-artifact/data/census/zcode/batch-0049.jsonl`).
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T23:33:04Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `2dae98e0ab355db08558ee33a2c3df8ae1f086ba` (*"Match the quadratic root lower bound by online moment recovery"*) — unrelated.
4. **arXiv / Zenodo / Crossref / ECCC / Web Search:**
   - arXiv API (`id_list=2609.07769`): latest version `2609.07769v2` (`2026-11-25T13:37:50Z`).
   - Zenodo API (`q=2609.07769`): `0` hits.
   - Crossref (`query=2609.07769`, `query.title=A+Note+on+Binary+Quadratic+Systems+and+their+relation+to+complexity+theory`): `0` matching DOIs.
   - `search_web` (`site:eccc.weizmann.ac.il` and general web): returns only `arXiv:2609.07769` itself (ECCC `TR26-278` multivariate interpolation unrelated); `0` follow-up resolutions for $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$.
