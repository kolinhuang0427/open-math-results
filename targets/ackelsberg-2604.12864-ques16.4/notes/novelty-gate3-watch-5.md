# Gate 3 Novelty Check — ackelsberg-2604.12864-ques16.4 (watch-5)

- **Checked UTC:** 2026-11-27T11:14:44Z – 2026-11-27T11:14:49Z (`<1h` before reporting)
- **Result:** **PASS** (no prior refutation or settlement of Ackelsberg–Richter `arXiv:2604.12864v1` §16.1 Question 16.4 "Kneser's theorem in $\mathbb{N}^2$" found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A135920 A369527 A369595 "2604.12864" "Question 16.4"`
   - Result: `3` lines across `2/651` files (`formal-conjectures` PR `#8236` on Question 16.9 only; `0` hits for Question 16.4).

2. **arXiv / Zenodo:**
   - `id:2604.12864`: sole version `2604.12864v1` (`2026-04-14T15:15:46Z`).
   - `abs:2604.12864`: `0` citing/matching abstracts.
   - Zenodo live API (`2604.12864`): `0` hits.

## Verification Scope
- Audit target files: `targets/ackelsberg-2604.12864-ques16.4/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live arXiv and Zenodo returned `0` settlement hits.
