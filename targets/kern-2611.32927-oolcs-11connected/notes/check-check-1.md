# Check Report: `targets/kern-2611.32927-oolcs-11connected/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2611.32927v1` (`sections/conclusion.tex` L5, Section 5; `sections/preliminaries.tex` L13–21; `sections/stcon.tex` L215–224)
- **Gate 2 Receipts:** `watch-1` (`#2002`), `watch-5` (`#2000`), `watch-6` (`#2001`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` cites Section 5 (`sections/conclusion.tex` L5), and `TARGET.md` L14 & L18–20 match `sections/conclusion.tex` L5 and `sections/stcon.tex` L215–224 verbatim.
2. **Proof review (`PROOF.md`):** Verified weight-shifting normalization, class-valid simple $a$--$b$ path characterization (Claim 1), and reduction to minimum-weight perfect matching on $G^*$ (Claim 2), with consistent bounds $|V^*| \le 2n + 6m$, $|E^*| \le 9m + n$ (L7 & L54) and consistent half-edge weights $W^*(e_v c_{v,s}) = \frac{1}{2} c(e)$ (L41, L46, L52).
3. **Independent exact-arithmetic verifier (`notes/check-check-1.py`):**

```text
$ .venv/bin/python -u targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.py
SIZE_WITNESS (n=3, m=2): |V*|=16, |E*|=17
WLCS_11CONNECTED_EXACT: checked=40, yes=16, no=24, trap=5
PASS
EXIT:0
AST_FLOATS: []
FLOAT_CALLS: []
```
