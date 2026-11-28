# Check Report: `targets/cai-2610.02047-plog-reg/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2610.02047v1` (`main.tex` Section 8 L4025–4031; Section 3 `Preliminaries` L1000–1153; `lem:plog-decomposition-size` L1324–1338; `lem:mres-to-res` L1641, L4269–4392; helper lemmas L1697–1754, L2338–2343)
- **Gate 2 Receipts:** `watch-1` (`#2033`), `watch-6` (`#2034`), `watch-5` (`#2035`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` reproduces `arXiv:2610.02047v1` Section 8 (`main.tex`, lines 4025–4031) verbatim, and `PROOF.md` L7 cites `Section 3` (`Preliminaries`).
2. **Proof review (`PROOF.md`) & `AUDIT.md` Re-Audit 1 fixes:**
   - Verified `L136` draft parenthetical removed, `L138–140` & `L193–195` geometric-series bounds ($2^{w+2} + 1$ and $(w+2)\cdot 2^{3w+5} = 2^{O(w)}$), and `L155` tautological $R_j$ equivalence ($\ell_j \in G$ or $\neg\ell_u \in G$ for some $u > j$).
3. **Independent exact-arithmetic verifier (`notes/check-check-1.py`):**
   - Fixed the 3 recursion slices (`L486`, `L640`, `L689`) and added both the $|W|=2$ `intro_v` regression test and the 27/27 clause-path 3-clause join test (`|elim_list| >= 2`, shared external literal in $d_{t_0}^{\mathrm{ext}}$).

```text
$ .venv/bin/python -u targets/cai-2610.02047-plog-reg/notes/check-check-1.py
JOIN_COUNTEREXAMPLE: L165_fails=True, corrected_regular_ok=True, len=6
COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS
AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS
PASS
PLOG_EXIT:0
PLOG_AST_FLOATS: []
PLOG_FLOAT_CALLS: []
```
