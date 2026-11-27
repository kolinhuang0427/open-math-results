# Novelty Receipt — Gate 3 (`watch-5`)

- **Target:** `targets/marberg-2611.19371-conj/` (`arXiv:2611.19371v1` §3.3 Conjecture 3.8 `iG-conj`)
- **Timestamp (UTC):** `2026-11-27T11:28Z`
- **Verdict:** **PASS**

## Live Checks (<1h)

1. `tools/novelty_grep.py 2611.19371 2611.34697 2503.16403`: hits only `arXiv:2611.19371v1` itself, `arXiv:2611.34697v1` (symplectic BPDs, distinct), and `2503.16403` / `1337isnot1337/solved-conjectures` Ehrhart width-2 posets (distinct); `0` settlement hits across `653` snapshot files.
2. `tools/arxiv_fetch.py query 'id:2611.19371'`: `2611.19371v1` (`2026-11-14`) remains sole/latest version.
3. Zenodo live API (`"2611.19371"`): `0` hits; `mylesparslow-collab.github.io` conjecture ledger (`2026-11-19`): `0` hits.
4. Verified required files present: `targets/marberg-2611.19371-conj/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
