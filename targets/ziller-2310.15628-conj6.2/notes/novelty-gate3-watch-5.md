# Gate 3 Novelty Receipt (`watch-5`, refreshed) — `targets/ziller-2310.15628-conj6.2/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/ziller-2310.15628-conj6.2/`)
- **Target Scope:** Mario Ziller, `arXiv:2310.15628v2` (`2026-04-15T17:18:47Z`), Section 6 Conjecture 6.2 (distinctness of $\varphi(x)/x^2$ for $x \in \mathbb{N}$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py 2310.15628 Ziller 'phi(x)/x^2' --max-per-file 3 --max-total 15`: `11` lines across `5/586` files (`plasma-ai__erdos` and `erdos-frontier-atlas` are Ziller–Morack on Erdős #854; `watch/snapshots/arxiv/` records only citing paper `arXiv:2604.19646v1`).
2. **arXiv 7-category snapshot & OpenAlex/S2 citing sweep (`watch/snapshots/arxiv/`):**
   - 1,000 recent arXiv entries: `0` matches resolving `2310.15628` Conjecture 6.2.
   - OpenAlex (`cited_by=1`): only citing paper `arXiv:2604.19646v1` (Mario Ziller, `2026-04-21`, *"Pseudometrics and preorders on sets of integer sequences induced by arithmetic functions functions"*); abstract verified directly via `tools/arxiv_fetch.py`, does not resolve Conjecture 6.2.
3. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `id_list=['2310.15628']`: confirms `2310.15628v2` (`2026-04-15T17:18:47Z`) remains the latest version.
   - `abs:"2310.15628" OR ...`: `total: 0`.
4. **Live OEIS JSON:**
   - `A373318`: rev `9`, `2024-06-01T04:03:07-04:00` (unchanged).
   - `A373319`: rev `15`, `2025-09-10T17:43:39-04:00` (unchanged).
5. **Web search (`search_web`):**
   - `"2310.15628" "Ziller"`: returns only `2310.15628` itself, no resolution.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, OpenAlex, web search, or `watch/snapshots/**`.
