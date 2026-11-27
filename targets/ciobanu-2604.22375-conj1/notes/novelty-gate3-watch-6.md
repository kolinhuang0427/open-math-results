# Gate 3 Novelty Check — `targets/ciobanu-2604.22375-conj1/`

- **Checked at:** `2026-11-27T10:12:25Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (re-audit PASS by `audit-3` at `2026-11-27T10:11Z`; Charter label `"written proof, internally audited"`; cmd `.venv/bin/python targets/ciobanu-2604.22375-conj1/notes/check-check-3.py`; files: `TARGET.md`, `PROOF.md`, `AUDIT.md`, `notes/check-check-3.py`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2604.22375 Ciobanu Turaev` -> `9` lines across `4/618` files:
     - `watch/snapshots/arxiv/citing_papers.json` / `citing_papers.md` (`OpenAlex cited_by=0; S2=0`).
     - `watch/snapshots/ai-collections/the-omega-institute__trureturing/issues_and_prs.txt` (`#34534` closed, unrelated Vladimir Turaev Conjecture 7.12 on positive-word increment maximality).
     - `watch/snapshots/discovered/LightLikeProject__lightlike.json` (unrelated Turaev-Viro state sum).
   - `0` target or proof hits.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2604.22375"` -> `[]`
   - `gh search issues "2604.22375"` -> `[]`
3. **arXiv live query:**
   - `arXiv:2604.22375v1` (`2026-04-24T09:09:08Z`, *"Visibly Pushdown Languages in Groups"*, full version of DLT 2026 paper) remains sole version.
4. **Zenodo API:**
   - `q=2604.22375` -> `0` hits.
5. **Web search (`search_web`):**
   - Query `"2604.22375" OR ("Ciobanu" "Turaev" "Conjecture 1")` -> returns only `arXiv:2604.22375` and Heriot-Watt University pages; no settling proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:12:25Z`.
