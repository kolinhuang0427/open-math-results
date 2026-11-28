# Independent Check Report: `targets/mora-2112.08768-conj/`

- **Checker:** `@check-3`
- **Target:** `targets/mora-2112.08768-conj/TARGET.md` (`arXiv:2112.08768v1` / *Mediterr. J. Math.* **19** (2022), art. 188, Section 3, Conjecture 21)
- **Counterexample checked:** `targets/mora-2112.08768-conj/COUNTEREXAMPLE.md` (answer: **FALSE**; explicit $30$-vertex $14$-resolving set on $P_3 \Box P_3 \Box P_4$ refuting conjectured $\dim_{14} = 32$)
- **Gate 2 Watch:** **PASS** (`watch-1` `#1857`, `watch-6` `#1859`, `watch-5` `#1862`)

## 1. Primary Source Verification

- **arXiv version check:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2112.08768` confirms `2112.08768v1` is the sole arXiv version (`published: 2021-12-16T10:26:03Z`, `doi: 10.1007/s00009-022-02096-1`).
- **Cached TeX:** `tools/.arxiv_cache/eprint/2112.08768v1/FaultTolerantMD-3DGrids-arxiv.tex` (1,123 lines).
- **Statement & definition match (`FaultTolerantMD-3DGrids-arxiv.tex` L195–204, L249–261, L635–644, L901–911):**
  - $(k+1)$-resolving set: every pair of distinct vertices $x, y \in V$ has $d(z, x) \neq d(z, y)$ for at least $k+1$ vertices $z \in S$.
  - $P_{n_1} \Box P_{n_2} \Box P_{n_3}$ ($n_i \ge 2$, $k \ge 2$) has vertices $\{0,\dots,n_1-1\} \times \{0,\dots,n_2-1\} \times \{0,\dots,n_3-1\}$ and graph distance $\sum_{i=1}^3 |x_i - y_i|$.
  - $\alpha_m(n_1,n_2,n_3) = 2(n_1+n_2+n_3)-8$ and $\alpha_M(n_1,n_2,n_3) = \min\{n_1(n_2+n_3-2), n_2(n_1+n_3-2), n_3(n_1+n_2-2)\}$.
  - Conjecture (L901–911): if $\alpha_m \le k < \alpha_M$, then $\dim_{k+1}(P_{n_1}\Box P_{n_2}\Box P_{n_3}) = \min\{4k - 2\alpha_m + 4,\, n_1 n_2 n_3 - (n_1-2)(n_2-2)(n_3-2)\}$.
  Matches `TARGET.md` verbatim.

## 2. Counterexample Verification

- For $(n_1, n_2, n_3, k) = (3, 3, 4, 13)$: $\alpha_m = 12 \le 13 < 15 = \alpha_M$, conjectured value $= \min(32, 34) = 32$.
- Explicit set $S = F_{\mathrm{edge}} \cup F_{\mathrm{int}} = V \setminus M$ has $|S| = 30$ and resolves every pair $\{u, v\} \in \binom{V}{2}$ by at least $14$ vertices (minimum $14$, attained at $(0,0,1), (0,1,0)$), proving $\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30 < 32$.
- Exhaustive verification also confirms the same construction $S$ of size $2\alpha_m + 6 < 4k - 2\alpha_m + 4$ gives $(k+1)$-resolving counterexamples at $(3,3,5,15)$ ($34 < 36$), $(3,4,4,15)$ ($34 < 36$), and $(4,4,4,17)$ ($38 < 40$).

## 3. Exact Mechanical Verification (`check-check-3.py`)

Command:
```sh
.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py && .venv/bin/python -c "import ast; tree = ast.parse(open('targets/mora-2112.08768-conj/notes/check-check-3.py').read()); floats = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]; calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'float']; print('FLOAT_COUNT:', len(floats), 'FLOAT_CALLS:', len(calls))"
```

Exact output:
```text
BFS == L1 distance on P_3 x P_3 x P_4: OK
(3,3,4,13): alpha_m=12 <= 13 < alpha_M=15, |S|=30 < conj=32, min_res=14 >= 14 (min pair ((0, 0, 1), (0, 1, 0))): OK
(3, 3, 5, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK
(3, 4, 4, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK
(4, 4, 4, 17): alpha_m=16 <= 17 < alpha_M=24, |S|=38 < conj=40, min_res=18 >= 18: OK
PASS
FLOAT_COUNT: 0 FLOAT_CALLS: 0
```

Verdict: **PASS**.
