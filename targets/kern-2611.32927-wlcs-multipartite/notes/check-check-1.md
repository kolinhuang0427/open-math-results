# Check Report: `targets/kern-2611.32927-wlcs-multipartite/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2611.32927v1` (`sections/conclusion.tex` L5, Section 5; `sections/preliminaries.tex` L13–19; `sections/stcon.tex` L147–188, L215–224)
- **Gate 2 Receipts:** `watch-1` (`#1996`), `watch-5` (`#1994`), `watch-6` (`#1995`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` L3 cites Section 5 (`sections/conclusion.tex` L5), and `TARGET.md` L14 & L18 match `sections/conclusion.tex` L5 and `sections/stcon.tex` L215–221 verbatim.
2. **Proof review (`PROOF.md`):** Verified polynomial-time NP-hardness reduction from $\{1^\star\}$-bounded $(K_2+K_2)$-shaped `LCS` (Theorem `thm:dichotomy-lcs`, `stcon.tex` L149, L184–186) to $\{1^\star\}$-bounded $K_{2,2}$-shaped `WLCS` with $\{0,1\}$-weights and $\lambda = 0$. Empty positions are dropped by monotonicity of $a$--$b$ connectivity and duplicate positions deduplicated in $O(|\widehat{G}|)$ time, yielding exact bijection $c(s) = c'(\tilde{s}) \in \{0,1\}$.
3. **Independent exact-arithmetic verifier (`notes/check-check-1.py`):**

```text
$ .venv/bin/python -u targets/kern-2611.32927-wlcs-multipartite/notes/check-check-1.py
REDUCTION_EXACT: checked=120, yes=48, no=72, lam1_false_positives=24
PASS
EXIT:0
AST_FLOATS: []
FLOAT_CALLS: []
```
