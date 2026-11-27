# Independent Check Report: targets/oeis-A394511/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - Live OEIS JSON API for `A394511` (revision `47`, `2026-06-06T04:04:55-04:00`, offset `1,1`).
- **Exact statement match:**
  - **Name:** `Minimum number of cells in a connected enclosing shell of an n-cell connected hole on the truncated-square (4.8.8) Archimedean tiling.`
  - **Data (`offset 1`):** `4,8,8,8,8,10,10,10,12,12,12,12,12,14,14,14,14,14,16,16,16,16,16`
  - **Comment:** `The 4.8.8 (truncated square) tiling has regular squares and octagons in a 1:1 ratio, symmetry group p4mm. For a connected n-cell hole H, the corona C(H) is the set of cells edge-adjacent to H but not in H. An enclosing shell S is a connected superset of C(H), disjoint from H, with the cells outside H union S also connected. a(n) is the minimum |S|.`
  - **Conjecture:** `Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole, |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6, equivalently a(n) = a(n - 5) + 2 for n >= 11. - _Peter Exley_, Jun 05 2026`
- **Fidelity:** `TARGET.md` and `COUNTEREXAMPLE.md` match live OEIS `A394511` rev 47 verbatim, and the edge-adjacency graph $G_{4.8.8}$ faithfully captures exact shared polygon edges of the regular `4.8.8` tiling.

## 2. Independent Mechanical Check

- Independently wrote `targets/oeis-A394511/notes/check-check-3.py` (strictly without reading `verify.py` or `notes/*`), verifying on the exact `4.8.8` edge-adjacency graph:
  1. Symmetry of the adjacency graph and connectedness of $H(R, C)$, $S(R, C) = C(H(R, C))$, and the exterior complement inside a bounding box containing $[-4, R+3] \times [-4, C+3]$ for all $2 \le R, C \le 10$, matching $|H(R, C)| = 2RC + R + C - 3$ and $|S(R, C)| = 2R + 2C + 4$.
  2. Explicit counterexamples:
     - $H(3, 5)$: $n = 35$, $|S| = 20 < 22 = 2\lceil (35 + 17)/5 \rceil$ (also refuting $a(n) = a(n-5) + 2$ from $a(20) = 16$).
     - $H(3, 5) \setminus \{\mathrm{O}(0,0)\}$: $n = 34$, valid connected corona/shell of size $20 < 22$ (verified directly that $\mathrm{O}(0,0)$ enters $C(H)$ while corner square $\mathrm{S}(-1,-1)$ leaves $C(H)$, preserving $|S|=20$, connectedness of $S$, and connectedness of the exterior).
     - $H(4, 4)$: $n = 37$, $|S| = 20 < 22$.
  3. Infinite family inequality $4k + 4 < 2\lceil (2k^2 + 2k + 14)/5 \rceil$ verified for all $4 \le k \le 1000$.

- **Command run:**
```bash
.venv/bin/python -u targets/oeis-A394511/notes/check-check-3.py
```

- **Raw output:**
```text
Grid Family PASS: H(R,C) and corona S=C(H(R,C)) verified for all 2 <= R, C <= 10.
Counterexamples PASS: (3,5) [n=35, |S|=20<22], n=34 [|S|=20<22], (4,4) [n=37, |S|=20<22], k=4..1000.
PASS
```
