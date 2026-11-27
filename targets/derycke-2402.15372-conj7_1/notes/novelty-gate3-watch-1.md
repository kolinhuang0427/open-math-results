# Gate 3 Novelty Receipt (`watch-1`): `targets/derycke-2402.15372-conj7_1/`

- **Checked UTC:** `2026-11-27T10:08Z`
- **Target:** Henri Derycke, Mark Dukes, and Yvan Le Borgne, *"The sandpile model on the complete split graph: $q,t$-Schröder polynomials, sawtooth polyominoes, and a cycle lemma"*, `arXiv:2402.15372v3` (`2025-12-19`), Section 6, **Conjecture 6.1** (`\label{conj:ITCCTIsymmetry}`, directory slug `derycke-2402.15372-conj7_1`)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-2` PASS `2026-11-27T10:08Z`), cmd `.venv/bin/python targets/derycke-2402.15372-conj7_1/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2402.15372 ITCCTIsymmetry` at `10:08Z`):** Only `watch/snapshots/arxiv/citing_papers.{json,md}` and `last_sweep_report.json` (`OpenAlex cited_by=3; S2=4`: `2506.23237`, `2409.11811`, `2401.06488`, `2207.01997`, all checked in `notes/novelty-derycke-lit.md` / `#276`, none resolving Conjecture 6.1); `0` hits in `1337isnot1337/solved-conjectures` (`09:50:27Z` rebuild), `trureturing`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2402.15372` at `10:08Z`):** `2402.15372v3` (`2025-12-19T21:03:09Z`) remains latest.
3. **Live GitHub (`gh search issues "2402.15372"` & `gh search prs "2402.15372"` at `10:08Z`):** `0` hits (`[]`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2402.15372&size=5` at `10:08Z`):** `0` hits (`total: 0`).
