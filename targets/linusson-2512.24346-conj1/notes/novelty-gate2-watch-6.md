# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/linusson-2512.24346-conj1/` (Linusson–Özdemir `arXiv:2512.24346v1` §3.4 Conjecture 1 `conj:complement`: $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$ for all $\lambda \in \mathcal{R}_k$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T22:04:06Z`
- **Requested by:** `@attack-2` (board #283)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2512.24346 Linusson "conj:complement" "kcore-chain"`
   - Result: `# 0 lines across 0/265 files in 0.90s`
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "2512.24346 OR kcore-chain OR k-Plancherel" --limit 20` -> `[]`
   - `gh search code "2512.24346 OR conj:complement" --limit 15` -> `[]`
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2512.24346` -> `2512.24346v1` (`2025-12-30`) is the sole version (`22 pages`, `math.CO`/`math.PR`).
4. **Web Search (`search_web`):**
   - Query: `"2512.24346" "Linusson" OR "Ozdemir" OR "conj:complement" OR "k-Plancherel" proved`
   - Result: Only `arXiv:2512.24346v1` itself; no prior proof of `conj:complement` found.

## Near Misses
- None found. Authors (`2512.24346v1`) verified Conjecture 1 computationally for $k \le 6$ without proof.

## Not Covered
- Private repositories, paywalled publications, and unindexed offline manuscripts.
