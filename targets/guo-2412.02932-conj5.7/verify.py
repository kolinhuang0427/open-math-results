"""Exact pure-integer verifier for COUNTEREXAMPLE.md (arXiv:2412.02932v1 Conjecture 5.7)."""
import itertools
from collections import defaultdict


def div_diff(poly, i):
    """Exact integer divided difference operator partial_i on polynomial dict."""
    res = defaultdict(int)
    for exp, coeff in poly.items():
        a, b = exp[i], exp[i + 1]
        if a == b:
            continue
        lst = list(exp)
        if a > b:
            for t in range(a - b):
                lst[i] = a - 1 - t
                lst[i + 1] = b + t
                res[tuple(lst)] += coeff
        else:
            for t in range(b - a):
                lst[i] = b - 1 - t
                lst[i + 1] = a + t
                res[tuple(lst)] -= coeff
    return {k: v for k, v in res.items() if v != 0}


def schubert_poly_divdiff(w):
    """Compute Schubert polynomial S_w(x) via exact divided differences from w_0."""
    n = len(w)
    cur = list(range(n, 0, -1))
    poly = {tuple(n - 1 - i for i in range(n)): 1}
    tmp = list(w)
    swaps = []
    while tmp != cur:
        for i in range(n - 1):
            if tmp[i] < tmp[i + 1]:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                swaps.append(i)
    for i in reversed(swaps):
        poly = div_diff(poly, i)
    assert all(v > 0 for v in poly.values())
    return poly


def elem_sym_poly(k, m, n):
    """Exact e_k(x_1, ..., x_m) as a dict of length-n exponent tuples."""
    if k == 0:
        return {(0,) * n: 1}
    res = {}
    for comb in itertools.combinations(range(m), k):
        exp = [0] * n
        for idx in comb:
            exp[idx] = 1
        res[tuple(exp)] = 1
    return res


def poly_mul(p, q):
    res = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            res[tuple(a + b for a, b in zip(e1, e2))] += c1 * c2
    return {k: v for k, v in res.items() if v != 0}


def standardize(sub):
    vals = sorted(sub)
    rank = {v: r + 1 for r, v in enumerate(vals)}
    return tuple(rank[v] for v in sub)


def main():
    u = (1, 3, 4, 5, 6, 2, 8, 9, 7)
    n = len(u)

    # 1. Cross-check S_u(x) between divided differences and e_4(x_1..x_5) * e_2(x_1..x_8).
    poly_u_dd = schubert_poly_divdiff(u)
    poly_u_elem = poly_mul(elem_sym_poly(4, 5, n), elem_sym_poly(2, 8, n))
    assert poly_u_dd == poly_u_elem, "Schubert polynomial identity mismatch for u=134562897"
    assert len(poly_u_dd) == 113, f"Expected theta_u=113, got {len(poly_u_dd)}"
    assert sum(poly_u_dd.values()) == 140, f"Expected nu_u=140, got {sum(poly_u_dd.values())}"

    # 2. Check all 55 distinct patterns in u and compute exact recursive d_sigma and c_sigma.
    patterns = defaultdict(int)
    for mask in range(1, 1 << n):
        sub = [u[i] for i in range(n) if (mask >> i) & 1]
        patterns[standardize(sub)] += 1
    assert len(patterns) == 55

    d = {}
    c = {}
    thetas = {}
    nus = {}
    for sig in sorted(patterns.keys(), key=len):
        m = len(sig)
        poly = schubert_poly_divdiff(sig)
        th = len(poly)
        nu = sum(poly.values())
        thetas[sig] = th
        nus[sig] = nu
        sd = 0
        sc = 0
        for mask in range(1, (1 << m) - 1):
            sub = [sig[i] for i in range(m) if (mask >> i) & 1]
            tau = standardize(sub)
            sd += d[tau]
            sc += c[tau]
        d[sig] = th - 1 - sd
        c[sig] = nu - 1 - sc

    # 3. Verify paper benchmark 13452786 (Section 5.2: c=3, d=4) and all nonzero proper subpatterns of u.
    u8 = (1, 3, 4, 5, 2, 7, 8, 6)
    assert c[u8] == 3 and d[u8] == 4, f"Mismatch on 13452786: c={c[u8]}, d={d[u8]}"

    expected_nonzero = {
        (1, 3, 2): (2, 1, 16),
        (1, 2, 4, 5, 3): (6, 1, 11),
        (1, 3, 2, 5, 4): (7, 2, 8),
        (2, 1, 4, 5, 3): (6, 1, 4),
        (1, 3, 2, 5, 6, 4): (17, 2, 4),
        (1, 3, 4, 2, 6, 5): (13, 2, 12),
        (1, 3, 4, 2, 6, 7, 5): (36, 3, 6),
        (1, 3, 4, 5, 2, 7, 8, 6): (67, 4, 4),
    }
    nonzero_found = {
        sig: (thetas[sig], d[sig], patterns[sig])
        for sig in patterns
        if sig != u and d[sig] != 0
    }
    assert nonzero_found == expected_nonzero, f"Table mismatch: {nonzero_found}"

    # 4. Verify d_u = -1 < 0 and c_u = 0.
    assert d[u] == -1, f"Expected d_u = -1, got {d[u]}"
    assert c[u] == 0, f"Expected c_u = 0, got {c[u]}"
    print("PASS")


if __name__ == "__main__":
    main()
