# Check Report: `targets/kern-2611.32927-gcs-dichotomy/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2611.32927v1` (`sections/gcon.tex` L19–27, L111–116, Section 4; `sections/preliminaries.tex` L13–19; `sections/stcon.tex` L149)
- **Gate 2 Receipts:** `watch-1` (`#1989`), `watch-6` (`#1990`), `watch-5` (`#1991`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` cites Section 4 (`sections/gcon.tex`, L116) and matches the primary definition of matroid switches (`gcon.tex`, L21–22) and the dichotomy conjecture (`gcon.tex`, L116) verbatim.
2. **Counterexample review (`COUNTEREXAMPLE.md`):**
   - Verified $\Pi_1$ ($\{2,1\}$-bounded $K_3$-shaped switches, plus L27 remark on $\{2,1,1\}$-bounded repetition), $\Pi_2$ (L35 corrected to paw graph $L_{3,1} \cong K_4 - \{bc, cx\}$, incomparable partitions, non-matroid, matroid-switch reduction), and $\Pi_3$ ($\{3,3\}$-bounded spanning-tree $K_4$-shaped switches).
3. **Independent exact-arithmetic verifier (`notes/check-check-1.py`):**

```text
$ .venv/bin/python -u targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py
Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS
PASS
EXIT:0
AST_FLOATS: []
FLOAT_CALLS: []
```
