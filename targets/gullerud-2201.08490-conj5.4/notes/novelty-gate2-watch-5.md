# Gate 2 Novelty Check — gullerud-2201.08490-conj5.4 (watch-5)

- **Checked UTC:** 2026-11-27T11:03:52Z – 2026-11-27T11:13:05Z
- **Result:** **PASS** (after scoping `TARGET.md` and `COUNTEREXAMPLE.md` strictly to **Conjecture 5.4 (`conj:ellipse`)** and dropping Conjecture 5.5 per `#1011`/`#1030`).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2201.08490 Gullerud "conj:ellipse"`
   - Result: `0` lines across `0/651` files.

2. **arXiv / Semantic Scholar / Web:**
   - `id:2201.08490`: `2201.08490v3` (`2023-08-21`), latest version on arXiv.
   - Inspected full `.tex` sources of both follow-up papers:
     - **arXiv:2510.02008v1** (Davis & Farnsworth, `2025-10-02`): explicitly *"leaves Conjecture 1(1) [= Conjecture 5.4 `conj:ellipse`] open"*.
     - **arXiv:2611.21142v1** (Oyengo, `2026-11-16`, sole S2 citation): explicitly states proving/disproving exact ellipse containment (Conjecture 5.4) *"remains open"*.
   - Zenodo live API (`2201.08490`): `0` hits.
   - Prior partial overlap on **Conjecture 5.5** (`unbounded real parts`) was removed from `TARGET.md` and `COUNTEREXAMPLE.md` in `#1030`.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live arXiv, S2 citations, Zenodo, and `search_web` returned `0` settlements of Conjecture 5.4 (`conj:ellipse`).
