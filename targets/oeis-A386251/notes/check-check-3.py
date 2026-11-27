"""Independent exact-arithmetic verifier for targets/oeis-A386251/.

Written strictly from OEIS A386251 (rev 22) and COUNTEREXAMPLE.md,
without reading the author's verify.py or notes/.
Uses exact integer arithmetic only (no floating point).
"""

from __future__ import annotations

import math
import signal
from collections import Counter


def timeout_handler(signum, frame):
    raise TimeoutError("check-check-3.py exceeded 50s timeout")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(50)


def build_4cycle(m: int) -> list[list[int]]:
    n = m * m - 30
    assert m >= 92 and n >= 8434
    cols_10 = [
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
    vecs = [[], [], [], []]
    for c in cols_10:
        for j in range(4):
            vecs[j].append(c[j])
    tail = (1, 1, -1, -1)
    for _ in range(n - 10):
        for j in range(4):
            vecs[j].append(tail[j])
    return vecs


def verify_4cycle(m: int) -> None:
    n = m * m - 30
    vecs = build_4cycle(m)
    assert all(len(v) == n for v in vecs)

    # 1. Closed walk and simple 4-cycle
    for i in range(n):
        assert sum(vecs[j][i] for j in range(4)) == 0
    p0 = tuple([0] * n)
    p1 = tuple(vecs[0])
    p2 = tuple(vecs[0][i] + vecs[1][i] for i in range(n))
    p3 = tuple(vecs[0][i] + vecs[1][i] + vecs[2][i] for i in range(n))
    assert len({p0, p1, p2, p3}) == 4

    # 2. All nonzero entries
    for v in vecs:
        assert all(x != 0 for x in v)

    # 3. Primitive (gcd == 1)
    for v in vecs:
        g = 0
        for x in v:
            g = math.gcd(g, abs(x))
        assert g == 1

    # 4. Exact Euclidean norm == m
    for v in vecs:
        assert sum(x * x for x in v) == m * m

    # 5. Pairwise noncongruent (distinct magnitude multisets)
    sigs = [frozenset(Counter(abs(x) for x in v).items()) for v in vecs]
    assert len(set(sigs)) == 4


def verify_3segment_lower_bound(m: int) -> None:
    n = m * m - 30
    # Verify algebraic minimum of sum L_i over all valid integer triples (L1, L2, L3)
    # with L_i >= m, L3 < L1 + L2, L1+L2+L3 even, and L1^2+L2^2+L3^2 >= 6n.
    # For L1 <= L2 <= L3 and L1+L2+L3 <= 4m, L3 <= 2m - 1.
    for L1 in range(m, (4 * m) // 3 + 1):
        for L2 in range(L1, 2 * m + 1):
            for L3 in range(L2, min(L1 + L2 - 1, 4 * m - L1 - L2) + 1):
                if (L1 + L2 + L3) % 2 != 0:
                    continue
                assert L1 * L1 + L2 * L2 + L3 * L3 < 6 * n, (
                    f"Unexpected 3-segment length triple {(L1, L2, L3)} at m={m}, n={n}"
                )


def main() -> None:
    # Check explicit full-coordinate 4-cycles for m = 92..110
    for m in range(92, 111):
        verify_4cycle(m)
    print("4-cycle witnesses PASS: verified full n-dim vectors for m=92..110 (n=8434..12070).")

    # Check exact 3-segment impossibility for <= 4m across m = 92..120
    for m in range(92, 121):
        verify_3segment_lower_bound(m)
    # Check sharpness at m = 91: (91, 92, 181) satisfies 91^2+92^2+181^2 = 6*(91^2-30)
    assert 91**2 + 92**2 + 181**2 == 6 * (91**2 - 30)
    print("3-segment lower bound (>= 4m+2) PASS: exact triple exhaustion for m=92..120 (sharp at m=91).")
    print("PASS")


if __name__ == "__main__":
    main()
