#!/usr/bin/env python3
"""Independent exact-integer verifier for Guo-Lin (arXiv:2412.02932v1) Section 5.2 Conjecture 5.7.

Written directly from main.tex definitions (L275-292, L1336-1368) without reading verify.py or notes/.
Pure integer arithmetic (zero floats).
"""

from __future__ import annotations

from itertools import combinations, permutations
import sys


def partial_i(poly: dict[tuple[int, ...], int], i: int) -> dict[tuple[int, ...], int]:
    """Divided difference operator partial_i(f) = (f(x) - f(x)|_{x_i <-> x_{i+1}}) / (x_i - x_{i+1})."""
    out: dict[tuple[int, ...], int] = {}
    for exp, coeff in poly.items():
        a, b = exp[i], exp[i + 1]
        if a == b:
            continue
        if a > b:
            for k in range(a - b):
                ne = list(exp)
                ne[i] = a - 1 - k
                ne[i + 1] = b + k
                t = tuple(ne)
                out[t] = out.get(t, 0) + coeff
        else:
            for k in range(b - a):
                ne = list(exp)
                ne[i] = b - 1 - k
                ne[i + 1] = a + k
                t = tuple(ne)
                out[t] = out.get(t, 0) - coeff
    return {k: v for k, v in out.items() if v != 0}


def schubert_poly(w: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    """Compute S_w(x) via top-down divided differences from S_{w_0}(x) = x_1^{n-1}...x_{n-1}^1."""
    n = len(w)
    cur = list(w)
    ops: list[int] = []
    while True:
        found = -1
        for i in range(n - 2, -1, -1):
            if cur[i] < cur[i + 1]:
                found = i
                break
        if found == -1:
            break
        ops.append(found)
        cur[found], cur[found + 1] = cur[found + 1], cur[found]
    poly: dict[tuple[int, ...], int] = {tuple(n - 1 - k for k in range(n)): 1}
    for i in reversed(ops):
        poly = partial_i(poly, i)
    assert all(c > 0 for c in poly.values()), f"Negative Schubert coefficient for {w}"
    return poly


def standardize(seq: tuple[int, ...]) -> tuple[int, ...]:
    vals = sorted(seq)
    rank = {v: idx + 1 for idx, v in enumerate(vals)}
    return tuple(rank[v] for v in seq)


def pattern_counts_in(w: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    """Exact counts p_sigma(w) over ALL proper nonempty subsequences (1 <= |sigma| < len(w))."""
    n = len(w)
    counts: dict[tuple[int, ...], int] = {}
    for m in range(1, n):
        for idxs in combinations(range(n), m):
            pat = standardize(tuple(w[i] for i in idxs))
            counts[pat] = counts.get(pat, 0) + 1
    return counts


def compute_theta_nu_all_Sn(max_n: int) -> tuple[dict[tuple[int, ...], int], dict[tuple[int, ...], int]]:
    """Compute S_w for all w in S_n (1 <= n <= max_n) via downward BFS from w_0."""
    theta: dict[tuple[int, ...], int] = {}
    nu: dict[tuple[int, ...], int] = {}
    for n in range(1, max_n + 1):
        w0 = tuple(range(n, 0, -1))
        polys: dict[tuple[int, ...], dict[tuple[int, ...], int]] = {w0: {tuple(n - 1 - k for k in range(n)): 1}}
        queue = [w0]
        while queue:
            nxt_queue = []
            for cur in queue:
                p_cur = polys[cur]
                for i in range(n - 1):
                    if cur[i] > cur[i + 1]:
                        nxt_l = list(cur)
                        nxt_l[i], nxt_l[i + 1] = nxt_l[i + 1], nxt_l[i]
                        nxt = tuple(nxt_l)
                        if nxt not in polys:
                            polys[nxt] = partial_i(p_cur, i)
                            assert all(c > 0 for c in polys[nxt].values())
                            nxt_queue.append(nxt)
            queue = nxt_queue
        assert len(polys) == len(list(permutations(range(1, n + 1))))
        for w, pol in polys.items():
            theta[w] = len(pol)
            nu[w] = sum(pol.values())
    return theta, nu


def main() -> int:
    print("[1/3] Checking all permutations in S_1..S_6 (Table 3 + S_6 nonnegativity)...", flush=True)
    theta, nu = compute_theta_nu_all_Sn(6)
    d_vals: dict[tuple[int, ...], int] = {}
    c_vals: dict[tuple[int, ...], int] = {}
    for n in range(1, 7):
        for w in permutations(range(1, n + 1)):
            pcounts = pattern_counts_in(w)
            d_vals[w] = theta[w] - 1 - sum(d_vals[sig] * cnt for sig, cnt in pcounts.items())
            c_vals[w] = nu[w] - 1 - sum(c_vals[sig] * cnt for sig, cnt in pcounts.items())
            assert d_vals[w] >= 0 and c_vals[w] >= 0

    # Verify Guo-Lin Table 3 (\label{tab-mdu}, main.tex L1391-1403) exact nonzero (c_u, d_u) for m <= 5
    expected_table3 = {
        (1, 3, 2): (1, 1),
        (1, 4, 3, 2): (1, 1),
        (1, 2, 4, 5, 3): (1, 1),
        (1, 2, 5, 3, 4): (1, 1),
        (1, 2, 5, 4, 3): (5, 4),
        (1, 3, 2, 5, 4): (3, 2),
        (1, 3, 5, 2, 4): (3, 2),
        (1, 3, 5, 4, 2): (4, 3),
        (1, 4, 2, 5, 3): (3, 3),
        (1, 4, 3, 5, 2): (1, 1),
        (1, 4, 5, 2, 3): (1, 1),
        (1, 4, 5, 3, 2): (1, 1),
        (1, 5, 2, 4, 3): (4, 4),
        (1, 5, 3, 2, 4): (1, 1),
        (1, 5, 3, 4, 2): (2, 2),
        (1, 5, 4, 2, 3): (1, 1),
        (1, 5, 4, 3, 2): (3, 3),
        (2, 1, 4, 5, 3): (1, 1),
        (2, 1, 5, 3, 4): (1, 1),
        (2, 1, 5, 4, 3): (5, 4),
        (2, 4, 1, 5, 3): (1, 1),
        (2, 5, 1, 4, 3): (2, 2),
        (3, 1, 5, 2, 4): (1, 1),
        (3, 1, 5, 4, 2): (2, 2),
        (3, 5, 1, 4, 2): (1, 1),
    }
    nonzero_m5 = {w: (c_vals[w], d_vals[w]) for n in range(1, 6) for w in permutations(range(1, n + 1)) if c_vals[w] > 0 or d_vals[w] > 0}
    assert nonzero_m5 == expected_table3, f"Table 3 mismatch: {nonzero_m5}"
    # Verify S_6 remark (main.tex L1375-1377)
    assert (d_vals[(1, 3, 6, 2, 4, 5)], c_vals[(1, 3, 6, 2, 4, 5)]) == (0, 1)
    assert (d_vals[(1, 4, 6, 2, 3, 5)], c_vals[(1, 4, 6, 2, 3, 5)]) == (0, 1)

    print("[2/3] Computing downward pattern closure of u = (1,3,4,5,6,2,8,9,7)...", flush=True)
    u = (1, 3, 4, 5, 6, 2, 8, 9, 7)
    closure: set[tuple[int, ...]] = {u}
    bfs = [u]
    while bfs:
        cur = bfs.pop()
        for pat in pattern_counts_in(cur):
            if pat not in closure:
                closure.add(pat)
                bfs.append(pat)

    # Sort closure by length ascending so all proper subpatterns are evaluated before u
    for w in sorted(closure, key=len):
        if w not in theta:
            pol = schubert_poly(w)
            theta[w] = len(pol)
            nu[w] = sum(pol.values())
        if w not in d_vals:
            pcounts = pattern_counts_in(w)
            d_vals[w] = theta[w] - 1 - sum(d_vals[sig] * cnt for sig, cnt in pcounts.items())
            c_vals[w] = nu[w] - 1 - sum(c_vals[sig] * cnt for sig, cnt in pcounts.items())

    print("[3/3] Checking exact counterexample values and subpattern table...", flush=True)
    u_pcounts = pattern_counts_in(u)
    assert len(u_pcounts) == 54
    assert theta[u] == 113
    assert nu[u] == 140
    assert d_vals[u] == -1
    assert c_vals[u] == 0

    nonzero_u_subs = {sig: (theta[sig], d_vals[sig], cnt, d_vals[sig] * cnt) for sig, cnt in u_pcounts.items() if d_vals[sig] != 0}
    expected_subs = {
        (1, 3, 2): (2, 1, 16, 16),
        (1, 2, 4, 5, 3): (6, 1, 11, 11),
        (1, 3, 2, 5, 4): (7, 2, 8, 16),
        (2, 1, 4, 5, 3): (6, 1, 4, 4),
        (1, 3, 2, 5, 6, 4): (17, 2, 4, 8),
        (1, 3, 4, 2, 6, 5): (13, 2, 12, 24),
        (1, 3, 4, 2, 6, 7, 5): (36, 3, 6, 18),
        (1, 3, 4, 5, 2, 7, 8, 6): (67, 4, 4, 16),
    }
    assert nonzero_u_subs == expected_subs, f"Subpattern table mismatch: {nonzero_u_subs}"
    assert (c_vals[(1, 3, 4, 5, 2, 7, 8, 6)], d_vals[(1, 3, 4, 5, 2, 7, 8, 6)]) == (3, 4)
    assert 1 + sum(d_vals[sig] * cnt for sig, cnt in u_pcounts.items()) == 114
    print(f"Counterexample u={u}: theta_u={theta[u]}, sum_sub=114, d_u={d_vals[u]} < 0")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
