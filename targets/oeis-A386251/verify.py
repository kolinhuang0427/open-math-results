import math
import signal
from collections import Counter

signal.alarm(30)


def build_4seg_witness(m: int):
    """Return (n, [v1, v2, v3, v4]) for n = m^2 - 30."""
    n = m * m - 30
    assert n >= 11
    prefix_cols = [
        (-2, -4, 1, 5),
        (-2, -2, 3, 1),
        (-2, -2, 3, 1),
        (-2, -2, 3, 1),
        (2, -2, -1, 1),
        (2, -2, -1, 1),
        (2, -1, -2, 1),
        (2, -1, -2, 1),
        (2, -1, 1, -2),
        (2, -1, 1, -2),
    ]
    pad_cols = [(1, 1, -1, -1)] * (n - len(prefix_cols))
    cols = prefix_cols + pad_cols
    vecs = [[col[j] for col in cols] for j in range(4)]
    return n, vecs


def verify_witness(m: int):
    n, vecs = build_4seg_witness(m)
    assert len(vecs) == 4
    for v in vecs:
        assert len(v) == n
        # All coordinates nonzero
        assert all(x != 0 for x in v)
        # Primitive (no intermediate lattice points)
        assert math.gcd(*v) == 1
        # Integer Euclidean length == m
        sq = sum(x * x for x in v)
        assert sq == m * m

    # Closed walk: sum == 0 in every coordinate
    for i in range(n):
        assert sum(vecs[j][i] for j in range(4)) == 0

    # Simple cycle check: all 4 partial sums distinct
    p0 = tuple([0] * 10)
    p1 = tuple(vecs[0][:10])
    p2 = tuple(vecs[0][i] + vecs[1][i] for i in range(10))
    p3 = tuple(vecs[0][i] + vecs[1][i] + vecs[2][i] for i in range(10))
    assert len({p0, p1, p2, p3}) == 4

    # Noncongruent diagonals: distinct sorted |v_i| multisets
    shapes = [tuple(sorted(abs(x) for x in v)) for v in vecs]
    assert len(set(shapes)) == 4

    # Check exact 3-segment lower bound at this (m, n):
    # Exhaustively verify no integer triple (L1, L2, L3) with Lmin <= L1 <= L2 <= L3
    # and L1 + L2 + L3 <= 4*m satisfies strict triangle inequality, parity, and sum of squares >= 6n.
    Lmin = math.isqrt(n - 1) + 1
    assert Lmin == m
    for S in range(3 * Lmin, 4 * m + 1):
        if S % 2 != 0:
            continue
        for L1 in range(Lmin, S // 3 + 1):
            for L2 in range(L1, (S - L1) // 2 + 1):
                L3 = S - L1 - L2
                if L3 >= L1 + L2:
                    continue  # equality forces u = v (congruent)
                assert L1 * L1 + L2 * L2 + L3 * L3 < 6 * n, (
                    f"Unexpected candidate at m={m}: {(L1, L2, L3)}"
                )

    return n, 4 * m


def main():
    # Verify smallest guaranteed counterexample m = 92 (n = 8434) and a range m = 92..110
    n0, tot0 = verify_witness(92)
    assert n0 == 8434 and tot0 == 368
    for m in range(93, 111):
        verify_witness(m)
    print(f"PASS: explicit 4-segment witness of length {tot0} verified at n={n0} (m=92) "
          f"and all m=92..110; exhaustive check confirms every 3-segment walk has length >= 4m+2.")


if __name__ == "__main__":
    main()
