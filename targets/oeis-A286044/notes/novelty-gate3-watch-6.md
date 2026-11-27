# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A286044/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (no competing proof found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A286044" "286044" "A138252"` -> 1 hit (`watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/files.txt:718: conjectures/phase0/A286044.txt`, unproved phase0 listing); `0` hits in `discovered/`, `1337-solved-conjectures/`, `openai-math/`, `formal/`, or `arxiv/`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]`.
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]`.
3. **Web search (`search_web`):**
   - Query: `"A286044" "Velin Yanev" OR "b(b(n - 2)) - b(b(n - 3))" "A003160"` -> surfaces only OEIS `A286044`, `A003160`, `A003159`, `A003157`; no proof found.

## Coverage Limits
- Live `gh search code` returned `HTTP 429` (shared rate limit); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues` and `search_web`.
