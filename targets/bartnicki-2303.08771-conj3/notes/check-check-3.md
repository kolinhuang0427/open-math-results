# Independent Check Report (`check-3`): `targets/bartnicki-2303.08771-conj3/`

## 1. Primary-Source Fidelity Check
Checked directly against `arXiv:2303.08771v1` (`tools/.arxiv_cache/eprint/2303.08771/Zlamasy_III_11.tex`, Section 1 lines 86–101 and Section 5 lines 248–252):
- **Definitions (lines 86, 98–101, 248):** *woody* = every color class is a forest; *broken cycle* = $C - e$ for a cycle $C$ and $e \in E(C)$; *strongly woody* = no monochromatic broken cycle (equivalently woody in $G/e$ for every $e \in E(G)$); $\zeta(G)$ = minimum colors in a strongly woody coloring; $\mathrm{col}(G)$ = least $r$ with a vertex ordering of max back-degree $r - 1$.
- **Conjecture 3 (Section 5, lines 250–252):** `Every graph $G$ satisfies $\zeta(G)\leqslant \col(G)$.`
- **Result:** `TARGET.md` and `COUNTEREXAMPLE.md` match the primary source verbatim.

## 2. Independent Mechanical Verification
Written solely from primary-source definitions in `Zlamasy_III_11.tex` and the graph/6-coloring in `COUNTEREXAMPLE.md`, without consulting `verify.py` or any other check scripts (pure Python `int` arithmetic, zero floats):
- Script: `targets/bartnicki-2303.08771-conj3/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/bartnicki-2303.08771-conj3/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/4] Verified col(G) = 5 (explicit ordering + all 511 induced subgraphs).
[2/4] Verified explicit 6-coloring is a strongly woody partition via all 24 contractions.
[3/4] Enumerated all 3292 strongly woody color classes (verified against G/e).
[4/4] Exhaustive exact-cover search proved zeta(G) > 5 and zeta(G) = 6.
PASS
```
Summary:
- Verified $G$ has $9$ vertices, $24$ edges, and $\mathrm{col}(G) = 5$ both via the explicit ordering $(0,\dots,8)$ and exhaustively over all $511$ nonempty induced subgraphs.
- Verified the explicit $6$-coloring partitions $E(G)$ and each color class stays acyclic in $G/e$ for all $24$ edge contractions.
- Enumerated all $3292$ strongly woody color classes (each independently verified against all $24$ edge contractions $G/e$) and proved exhaustively via exact cover that no strongly woody $5$-coloring exists, establishing $\zeta(G) = 6 > 5 = \mathrm{col}(G)$. (Claims 1–5 of `COUNTEREXAMPLE.md` also hold cleanly.)

## 3. Verdict
- **PASS** (`Gate 2` PASS receipts present: `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
