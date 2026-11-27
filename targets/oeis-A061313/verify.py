import math
import signal
from fractions import Fraction

signal.alarm(30)

OEIS_A061313 = [
    0,1,3,2,5,4,4,3,7,6,6,5,6,5,5,4,9,8,8,7,8,7,7,6,8,7,7,6,7,6,6,5,11,10,10,
    9,10,9,9,8,10,9,9,8,9,8,8,7,10,9,9,8,9,8,8,7,9,8,8,7,8,7,7,6,13,12,12,11,
    12,11,11,10,12,11,11,10,11,10,10,9,12,11,11,10,11,10,10,9,11,10
]  # offset 1: a(1)..a(90)

OEIS_A007305 = [0,1,1,1,2,1,2,3,3,1,2,3,3,4,5,5,4,1,2,3,3,4,5,5,4,5,7,8,7,7,8,7,5]
OEIS_A007306 = [1,1,2,3,3,4,5,5,4,5,7,8,7,7,8,7,5,6,9,11,10,11,13,12,9,9,12,13,11,10,11,9,6]


def compute_A061313(N: int):
    a = [0] * (N + 1)
    a[1] = 0
    for i in range(2, N + 1):
        if i % 2 == 0:
            a[i] = a[i // 2] + 1
        else:
            a[i] = a[(i + 1) // 2] + 2
    return a


def build_stern_brocot(N: int):
    sb = [(0, 1), (1, 1)]
    cur = [(0, 1), (1, 1)]
    while len(sb) <= N:
        nxt = [cur[0]]
        for i in range(len(cur) - 1):
            p1, q1 = cur[i]
            p2, q2 = cur[i + 1]
            med = (p1 + p2, q1 + q2)
            sb.append(med)
            nxt.append(med)
            nxt.append(cur[i + 1])
        cur = nxt
    return sb[: N + 1]


def hirzebruch_cf(p: int, q: int):
    terms = []
    x = Fraction(p, q)
    while True:
        c = math.ceil(x)
        terms.append(c)
        rem = c - x
        if rem == 0:
            break
        x = 1 / rem
    return terms


def eval_hirzebruch(terms):
    val = Fraction(terms[-1])
    for c in reversed(terms[:-1]):
        val = c - Fraction(1, val)
    return val


def mat_mul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def H(c):
    return ((c, -1), (1, 0))


def main():
    N = 10000
    a = compute_A061313(N)
    sb = build_stern_brocot(N)

    # 1. Exact check against OEIS data
    assert a[1 : 1 + len(OEIS_A061313)] == OEIS_A061313
    assert [sb[i][0] for i in range(len(OEIS_A007305))] == OEIS_A007305
    assert [sb[i][1] for i in range(len(OEIS_A007306))] == OEIS_A007306

    # 2. Verify SL_2 conjugation identities
    L = ((1, 0), (1, 1))
    R = ((1, 1), (0, 1))
    J = H(1)
    J_inv = ((0, 1), (-1, 1))
    assert mat_mul(J_inv, mat_mul(L, J)) == H(2)
    J_inv_R_J = mat_mul(J_inv, mat_mul(R, J))
    for c in range(2, 20):
        assert mat_mul(H(c), J_inv_R_J) == H(c + 1)

    # 3. Verify n = 1 boundary
    assert hirzebruch_cf(*sb[1]) == [1]
    assert sum(hirzebruch_cf(*sb[1])) == 1 and a[1] + 2 == 2

    # 4. Verify Main Theorem for all 2 <= n <= N
    for n in range(2, N + 1):
        p, q = sb[n]
        terms = hirzebruch_cf(p, q)
        assert terms[0] == 1 and all(c >= 2 for c in terms[1:])
        assert eval_hirzebruch(terms) == Fraction(p, q)
        assert sum(terms) == a[n] + 2, f"Mismatch at n={n}: {sum(terms)} != {a[n] + 2}"

    print(f"PASS: OEIS A061313 (90 terms), A007305/A007306 (33 terms) matched; "
          f"SL2 identities and Hirzebruch CF sum == a(n)+2 verified for all 2 <= n <= {N} (with n=1 boundary noted).")


if __name__ == "__main__":
    main()
