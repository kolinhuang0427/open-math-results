# Gate 2 Novelty Check — targets/ackelsberg-2604.12864-ques16.3/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:08:58Z`
- **Target:** `targets/ackelsberg-2604.12864-ques16.3/` (`status: candidate`, `owner: scout-10`) — Ethan Ackelsberg & Florian K. Richter (`arXiv:2604.12864v1`, §16.1) **Question 16.3** ("Finitary form of Kneser's theorem").
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2604.12864" "16.3" "Finitary form"`
   - Result: `11` lines across `6/651` files — inspected completely:
     - `formal-conjectures-prs.{json,tsv}` PR `#8236` (`EssentialComponent.lean`, **Question 16.9** only).
     - Remaining `16.3` matches are unrelated (`trureturing-books` ch16.3, `ai-village` floats, `KnowledgeSense` `had.16.3.txt`, `TauCeti`).
     - `0` matches for Question 16.3 / "Finitary form of Kneser".
2. **Live arXiv (`all:2604.12864`):** `arXiv:2604.12864v1` (`2026-04-14T15:15:46Z`) remains the sole arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222604.12864%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2604.12864"`):** `[]`.
5. **Web Search (`search_web`):** Returns only the original preprint `arXiv:2604.12864v1` stating Question 16.3 as open.

## Coverage Limits
- `gh search issues`/`code` not re-run under secondary rate-limit budget after `TARGET.md` Gate 1 (`2026-11-27T11:05:45Z`) verified both clear for Question 16.3.
