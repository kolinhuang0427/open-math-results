# Gate 3 Novelty Check — gullerud-2201.08490-conj5.4 (watch-5)

- **Checked UTC:** 2026-11-27T11:18:08Z – 2026-11-27T11:18:19Z (`<1h` before reporting)
- **Result:** **PASS** for **Conjecture 5.4 (`conj:ellipse`)** (no prior proof or counterexample establishing failure of exact ellipse containment at $n=8$ found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A271061 A271060 A271062 2201.08490 "conj:ellipse"`
   - Result: `0` lines across `0/651` snapshot files.

2. **arXiv / Zenodo:**
   - `id:2201.08490`: latest version `2201.08490v3` (`2023-08-21T19:49:41Z`).
   - `abs:2201.08490`: `0` citing/matching abstracts.
   - Follow-up papers `arXiv:2510.02008v1` (Davis–Farnsworth) and `arXiv:2611.21142v1` (Oyengo, sole S2 citation) were inspected in Gate 2: both explicitly leave Conjecture 5.4 (`conj:ellipse`) open (and are cited in `TARGET.md` / `COUNTEREXAMPLE.md`, which are scoped strictly to Conjecture 5.4).
   - Zenodo live API (`2201.08490`): `0` hits.

## Verification Scope
- Audit target files: `targets/gullerud-2201.08490-conj5.4/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live arXiv and Zenodo returned `0` settlements of Conjecture 5.4 (`conj:ellipse`).
