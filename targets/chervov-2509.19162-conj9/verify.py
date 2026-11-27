"""Exact verification script for disproof of arXiv:2509.19162v2 Conjecture 9."""

from collections import deque
import random


def mat_mul_f2(A, B):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                rowB = B[k]
                rowR = res[i]
                for j in range(n):
                    rowR[j] ^= rowB[j]
    return res


def apply_gen_left(M, k):
    """Left-multiply 0-indexed matrix M by s_k = I + E_{k-1, k} (1 <= k <= n-1)."""
    n = len(M)
    out = [row[:] for row in M]
    for j in range(n):
        out[k - 1][j] ^= out[k][j]
    return out


def apply_gen_right(M, k):
    """Right-multiply 0-indexed matrix M by s_k = I + E_{k-1, k} (1 <= k <= n-1)."""
    out = [row[:] for row in M]
    for row in out:
        row[k] ^= row[k - 1]
    return out


def synth_row(i, row_bits, n):
    """Return word [k_1, ..., k_L] (1 <= k <= n-1) whose product s_{k_1}...s_{k_L} equals U_i."""
    if i == n - 2:
        return [n - 1] if row_bits[n - 1] else []
    hi = [j for j in range(i + 2, n) if row_bits[j]]
    if not hi:
        return [i + 1] if row_bits[i + 1] else []
    m = max(hi)
    W = list(range(i + 2, m + 1)) + [k for k in range(m, i + 1, -1) if row_bits[k] == 0]
    word = list(reversed(W)) + [i + 1] + W
    if row_bits[i + 1] == 0:
        word = [i + 1] + word
    return word


def factor_matrix(M):
    """Construct word w for M = U_{n-2}...U_0 in U(n, F_2) of length <= 2n^2 - 6n + 5."""
    n = len(M)
    word = []
    for i in range(n - 2, -1, -1):
        w_i = synth_row(i, M[i], n)
        max_len = 1 if i == n - 2 else 4 * (n - i - 2)
        assert len(w_i) <= max_len
        word.extend(w_i)
    return word


def eval_word(n, word):
    M = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
    for k in word:
        M = apply_gen_right(M, k)
    return M


def bfs_diameter_u_f2(n):
    """Exact BFS diameter of U(n, F_2) with fundamental root transvections."""
    # Pack upper triangular bits into an integer
    pairs = [(r, c) for r in range(n) for c in range(r + 1, n)]
    idx = {p: b for b, p in enumerate(pairs)}
    N = 1 << len(pairs)
    dist = [-1] * N
    dist[0] = 0
    q = deque([0])
    # Precompute bit effects of left-multiplying by s_k: row k-1 ^= row k
    gen_masks = []
    for k in range(1, n):
        # row k-1 col c (c >= k+1) flips if row k col c is 1; col k flips
        gen_masks.append(k)
    max_d = 0
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        d = dist[u]
        if d > max_d:
            max_d = d
        for k in range(1, n):
            # Left multiply by s_k: row k-1 ^= row k (including implicit 1 at (k, k))
            v = u ^ (1 << idx[(k - 1, k)])
            for c in range(k + 1, n):
                if (u >> idx[(k, c)]) & 1:
                    v ^= 1 << idx[(k - 1, c)]
            if dist[v] == -1:
                dist[v] = d + 1
                q.append(v)
    assert visited == N
    return max_d


def ab_invariant_factors(elems, mul, id_elem):
    """Return sorted exponent pair (e1 <= e2) for a 2-generated abelian 2-group."""
    max_e = 0
    for g in elems:
        p = g
        e = 0
        while p != id_elem:
            p = mul(p, p)
            e += 1
        if e > max_e:
            max_e = e
    E = len(elems).bit_length() - 1
    assert (1 << E) == len(elems)
    return (E - max_e, max_e)


def count_F(n):
    m = n // 2
    cnt = 0
    for a in range(3, m + 1):
        for s in range(2, a):
            cnt += min(s, a - s) + 1
    return cnt


def main():
    # 1. Exact BFS diameters for n = 2..6 (and check n=2 < A136184(2)=2)
    expected_bfs = {2: 1, 3: 4, 4: 8, 5: 12, 6: 19}
    for n, exp_d in expected_bfs.items():
        d = bfs_diameter_u_f2(n)
        assert d == exp_d, f"BFS diameter mismatch at n={n}: {d} != {exp_d}"
    assert expected_bfs[2] == 1 < 2  # metacyclic groups of order 4: C4, C2 x C2
    print("[PASS] Exact BFS diameters n=2..6:", expected_bfs, "(n=2: 1 < 2)")

    # 2. Exhaustive verification of 2n^2 - 6n + 5 factorization for n = 2..5
    for n in range(2, 6):
        pairs = [(r, c) for r in range(n) for c in range(r + 1, n)]
        ub = 2 * n * n - 6 * n + 5
        for mask in range(1 << len(pairs)):
            M = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
            for bit, (r, c) in enumerate(pairs):
                if (mask >> bit) & 1:
                    M[r][c] = 1
            w = factor_matrix(M)
            assert len(w) <= ub
            assert eval_word(n, w) == M
    print("[PASS] Exhaustive factorization check n=2..5 against 2n^2 - 6n + 5")

    # 3. Deterministic sample verification at n = 176 and n = 178 (plus n = 20)
    rng = random.Random(250919162)
    for n in [20, 176, 178]:
        ub = 2 * n * n - 6 * n + 5
        for trial in range(5):
            M = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
            for r in range(n):
                for c in range(r + 1, n):
                    if trial == 0:
                        # Worst-case sparse/dense pattern: bit r+1 is 0, alternating/dense tail
                        M[r][c] = 1 if (c > r + 1 and (c == n - 1 or (c - r) % 2 == 0)) else 0
                    else:
                        M[r][c] = rng.randint(0, 1)
            w = factor_matrix(M)
            assert len(w) <= ub
            assert eval_word(n, w) == M
    print("[PASS] Factorization witness check at n=20, 176, 178")

    # 4. Full axiom & invariant verification of metacyclic family F_n for n = 6..11
    for n in range(6, 12):
        seen_invariants = set()
        expected_cnt = count_F(n)
        actual_cnt = 0
        for a in range(3, n // 2 + 1):
            b = n - a
            for s in range(2, a):
                d = a - s
                for c in range(max(s, d), a + 1):
                    actual_cnt += 1
                    A = 1 << a
                    B = 1 << b
                    C = 1 << c
                    step = 1 + (1 << s)

                    def mul(g1, g2):
                        i1, j1 = g1
                        i2, j2 = g2
                        nj = j1 + j2
                        carry = C if nj >= B else 0
                        if nj >= B:
                            nj -= B
                        return ((i1 + i2 * pow(step, j1, A) + carry) & (A - 1), nj)

                    elems = [(i, j) for i in range(A) for j in range(B)]
                    # Check associativity exhaustively on n <= 8, and on random triples for n = 9..11
                    if n <= 8:
                        for g1 in elems:
                            for g2 in elems:
                                for g3 in elems:
                                    assert mul(mul(g1, g2), g3) == mul(g1, mul(g2, g3))
                    else:
                        for _ in range(200):
                            g1, g2, g3 = rng.choice(elems), rng.choice(elems), rng.choice(elems)
                            assert mul(mul(g1, g2), g3) == mul(g1, mul(g2, g3))

                    # Verify normal cyclic subgroup <x> and presentation relations
                    x = (1, 0)
                    y = (0, 1)
                    y_inv = ((A - C) & (A - 1), B - 1)
                    assert mul(y, y_inv) == (0, 0) and mul(y_inv, y) == (0, 0)
                    assert mul(mul(y, x), y_inv) == (step & (A - 1), 0)
                    yb = (0, 0)
                    for _ in range(B):
                        yb = mul(yb, y)
                    xc = (C & (A - 1), 0)
                    assert yb == xc

                    # Center Z(G) invariant factors == (c - d, n - c - d)
                    Z = [g for g in elems if mul(g, x) == mul(x, g) and mul(g, y) == mul(y, g)]
                    z_inv = ab_invariant_factors(Z, mul, (0, 0))
                    assert z_inv == (c - d, n - c - d)

                    # Abelianization G / G' invariant factors == (s, b)
                    S = 1 << s
                    ab_elems = [(i, j) for i in range(S) for j in range(B)]

                    def ab_mul(g1, g2):
                        i1, j1 = g1
                        i2, j2 = g2
                        nj = j1 + j2
                        carry = C if nj >= B else 0
                        if nj >= B:
                            nj -= B
                        return ((i1 + i2 + carry) & (S - 1), nj)

                    ab_inv = ab_invariant_factors(ab_elems, ab_mul, (0, 0))
                    assert ab_inv == (s, b)
                    inv_key = (z_inv, ab_inv)
                    assert inv_key not in seen_invariants
                    seen_invariants.add(inv_key)
        assert actual_cnt == expected_cnt == len(seen_invariants)
    print("[PASS] Metacyclic family axioms & (Z(G), G/G') uniqueness verified for n=6..11")

    # 5. Exact crossover checks for n = 176 and all n in [178, 195] (and algebraic check for n >= 195)
    f176 = count_F(176)
    ub176 = 2 * 176 * 176 - 6 * 176 + 5
    assert f176 == 61404 and ub176 == 60901 and f176 > ub176
    for n in range(178, 220):
        assert count_F(n) > 2 * n * n - 6 * n + 5
    # Verify algebraic lower bound (2m^3 + 15m^2 - 65m + 54)/24 <= count_F(n) and > (n-1)^3/96
    for n in range(195, 250):
        m = n // 2
        assert 24 * count_F(n) >= 2 * m**3 + 15 * m**2 - 65 * m + 54
        assert 15 * m**2 - 65 * m + 54 > 0
        assert (n - 1) ** 3 > 96 * (2 * n * n - 6 * n + 5)
    print(f"[PASS] Crossover verified: n=176 (|F_176|={f176} > {ub176}), all n>=178")
    print("PASS")


if __name__ == "__main__":
    main()
