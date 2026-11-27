# Gate 2 Novelty Check — targets/ackelsberg-2604.12864-ques16.4/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:07:36Z`
- **Target:** `targets/ackelsberg-2604.12864-ques16.4/` (`status: candidate`, `owner: scout-10`) — Ethan Ackelsberg & Florian K. Richter (`arXiv:2604.12864v1`, §16.1) **Question 16.4** ("Kneser's theorem in $\mathbb{N}^2$").
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2604.12864" "16.4" "Ackelsberg"`
   - Result: `21` lines across `10/651` files — inspected completely:
     - `plasma-ai/erdos`: references Ackelsberg–Richter `2604.12864` on Erdős #335 inverse theorem.
     - `formal-conjectures-prs.{json,tsv}` PR `#8236`: addresses **Question 16.9** (`d`-essential components), NOT Question 16.4.
     - Remaining `"16.4"` hits are floats/unrelated chapters (`trureturing-books`, `ai-village`, `Fuglede`, `KVZ`).
2. **Live arXiv (`all:2604.12864`):**
   - `http://arxiv.org/abs/2604.12864v1` (`2026-04-14T15:15:46Z`) remains the sole arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222604.12864%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2604.12864"`):** `[]`.
5. **Web Search (`search_web`):** Only `arXiv:2604.12864v1` itself and Erdős #335 summaries; Question 16.4 remains open.

## Coverage Limits
- `gh search issues`/`code` not re-run under secondary rate-limit budget after `TARGET.md` Gate 1 (`2026-11-27T11:02:42Z`) checked both and found `0` Question 16.4 results.
