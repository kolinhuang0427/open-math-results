"""Independent exact checker for targets/oeis-A061313/ (PROOF.md).

Written strictly from live OEIS A061313 (rev 58), A007305, A007306,
and PROOF.md, without reading verify.py or notes/screen-*.
"""

from fractions import Fraction
from math import ceil, gcd


A061313_DATA = [
    0, 1, 3, 2, 5, 4, 4, 3, 7, 6, 6, 5, 6, 5, 5, 4, 9, 8, 8, 7, 8, 7, 7, 6,
    8, 7, 7, 6, 7, 6, 6, 5, 11, 10, 10, 9, 10, 9, 9, 8, 10, 9, 9, 8, 9, 8, 8,
    7, 10, 9, 9, 8, 9, 8, 8, 7, 9, 8, 8, 7, 8, 7, 7, 6, 13, 12, 12, 11, 12,
    11, 11, 10, 12, 11, 11, 10, 11, 10, 10, 9, 12, 11, 11, 10, 11, 10, 10, 9,
    11, 10,
]

# First 33 terms of A007305 and A007306 (offset 0, from live OEIS JSON)
A007305_PREFIX = [
    0, 1, 1, 1, 2, 1, 2, 3, 3, 1, 2, 3, 3, 4, 5, 5, 4, 1, 2, 3, 3, 4, 5, 5, 4,
    5, 7, 8, 7, 7, 8, 7, 5,
]
A007306_PREFIX = [
    1, 1, 2, 3, 3, 4, 5, 5, 4, 5, 7, 8, 7, 7, 8, 7, 5, 6, 9, 11, 10, 11, 13, 12,
    9, 9, 12, 13, 11, 10, 11, 9, 6,
]


def hirzebruch_cf(x: Fraction) -> list[int]:
    """Compute canonical Hirzebruch (negative) CF [[c0; c1, ..., ck]] with ci >= 2 for i >= 1."""
    terms: list[int] = []
    cur = x
    while True:
        c = ceil(cur)
        terms.append(c)
        if cur == c:
            break
        cur = Fraction(1, 1) / (Fraction(c, 1) - cur)
    for i in range(1, len(terms)):
        assert terms[i] >= 2
    return terms


def eval_hirzebruch(terms: list[int]) -> Fraction:
    val = Fraction(terms[-1], 1)
    for c in reversed(terms[:-1]):
        val = Fraction(c, 1) - Fraction(1, 1) / val
    return val


def mat_mul(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat_inv_sl2(A: list[list[int]]) -> list[list[int]]:
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert det == 1
    return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]


def H_mat(c: int) -> list[list[int]]:
    return [[c, -1], [1, 0]]


def main() -> None:
    N = 4096

    # 1. Verify Step 2 exact 2x2 matrix identities
    L = [[1, 0], [1, 1]]
    R = [[1, 1], [0, 1]]
    J = H_mat(1)
    J_inv = mat_inv_sl2(J)
    assert mat_mul(L, J) == mat_mul(H_mat(1), H_mat(2))
    assert mat_mul(mat_mul(J_inv, L), J) == H_mat(2)
    JRJ = mat_mul(mat_mul(J_inv, R), J)
    for c in range(-5, 15):
        assert mat_mul(H_mat(c), JRJ) == H_mat(c + 1)

    # 2. Compute A061313 from OEIS recurrence up to N, compare with data & BFS shortest steps
    a = [0] * (N + 1)
    a[1] = 0
    for m in range(1, N + 1):
        if 2 * m <= N:
            a[2 * m] = a[m] + 1
        if 2 * m + 1 <= N:
            a[2 * m + 1] = a[m + 1] + 2
    assert a[1 : len(A061313_DATA) + 1] == A061313_DATA

    # Cross-check OEIS Name ("minimal steps from 1 to n by -1 or *2") via BFS for n=1..100
    from collections import deque
    dist = {1: 0}
    q = deque([1])
    while len([k for k in range(1, 101) if k in dist]) < 100:
        u = q.popleft()
        for v in (u - 1, 2 * u):
            if 1 <= v <= 2000 and v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    for n in range(1, 101):
        assert dist[n] == a[n], f"BFS mismatch at n={n}: {dist[n]} != {a[n]}"

    # 3. Build Stern-Brocot subtree r(n) directly by level-by-level mediants (PROOF.md Theorem def)
    # Also track Farey intervals M(m) for Step 1 verification
    r_fracs: list[Fraction] = [Fraction(0, 1), Fraction(1, 1)]
    sorted_list = [Fraction(0, 1), Fraction(1, 1)]
    M: dict[int, list[list[int]]] = {}
    P: dict[int, list[list[int]]] = {}

    idx_next = 2
    # Level L = 1..12 -> up to 2^12 = 4096
    for level in range(1, 13):
        new_mediants = []
        new_sorted = [sorted_list[0]]
        for j in range(len(sorted_list) - 1):
            left = sorted_list[j]
            right = sorted_list[j + 1]
            assert left.denominator * right.numerator - left.numerator * right.denominator == 1
            med = Fraction(left.numerator + right.numerator, left.denominator + right.denominator)
            assert gcd(left.numerator + right.numerator, left.denominator + right.denominator) == 1
            new_mediants.append(med)
            new_sorted.append(med)
            new_sorted.append(right)

            # Compare with Step 1 matrix M(idx_next)
            M_cur = [[right.numerator, left.numerator], [right.denominator, left.denominator]]
            M[idx_next] = M_cur
            P[idx_next] = mat_mul(M_cur, J)
            assert P[idx_next][0][0] == med.numerator and P[idx_next][1][0] == med.denominator
            if idx_next >= 4:
                parent = (idx_next + 1) // 2
                if idx_next % 2 == 1:
                    assert M[idx_next] == mat_mul(M[parent], L)
                else:
                    assert M[idx_next] == mat_mul(M[parent], R)
            idx_next += 1
        r_fracs.extend(new_mediants)
        sorted_list = new_sorted

    # Verify r_fracs against A007305 / A007306 OEIS prefix (indices 0..32)
    for idx in range(len(A007305_PREFIX)):
        assert r_fracs[idx].numerator == A007305_PREFIX[idx]
        assert r_fracs[idx].denominator == A007306_PREFIX[idx]

    # 4. Verify n = 1 boundary exception and all 2 <= n <= N Hirzebruch CF & matrix factorization
    cf1 = hirzebruch_cf(r_fracs[1])
    assert cf1 == [1] and sum(cf1) == 1 != 2 == a[1] + 2

    for n in range(2, N + 1):
        cf = hirzebruch_cf(r_fracs[n])
        assert cf[0] == 1 and eval_hirzebruch(cf) == r_fracs[n]
        assert sum(cf) == a[n] + 2, f"Sum mismatch at n={n}: {sum(cf)} != {a[n]+2}"
        # Also verify P(n) == H(c0)*H(c1)*...*H(ck)
        prod_H = [[1, 0], [0, 1]]
        for c in cf:
            prod_H = mat_mul(prod_H, H_mat(c))
        assert prod_H == P[n], f"Matrix factorization mismatch at n={n}"

    print("Step 2 SL_2(Z) identities (L, R, J, H(c)): OK")
    print("A061313 OEIS data (90 terms) & BFS minimal steps (n=1..100): OK")
    print("A007305/A007306 (33 terms) & Step 1 M(n) recursion (2<=n<=4096): OK")
    print("n=1 exception ([[1]] sum 1 != 2) & Main Theorem P(n)=prod H(c_i), sum=a(n)+2 (2<=n<=4096): OK")
    print("PASS")


if __name__ == "__main__":
    main()
