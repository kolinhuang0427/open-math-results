# Gate 2 Novelty Receipt — targets/oeis-A119366 (watch-5)

- **Checked UTC:** 2026-11-27T09:24:14Z – 2026-11-27T09:24:31Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A119366 ... 119366`):** `1` line across `1/608` files (`watch/snapshots/openai-math/lean_index.jsonl` SHA hash substring `119366` on `lean/LICENSE`); `0` mathematical hits.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A119366" ...'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A119366&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A119366&fmt=json`):** timestamp `2025-02-03T09:34:08-05:00`; Mathar's Feb 03 2025 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A119366" "Mathar" OR "D-finite" OR "recurrence" OR "binomial"`):** general holonomic/D-finite OEIS context only; `0` proofs of Mathar's `A119366` recurrence found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A119366` in indexed titles/abstracts/snapshots are not covered.
