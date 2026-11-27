"""Independent exact-arithmetic verifier for targets/oeis-A092920/."""

from fractions import Fraction
import itertools
from math import comb
import signal

signal.alarm(50)

OEIS_A092920 = [
    1, 1, 2, 4, 9, 22, 58, 164, 496, 1601, 5502, 20075, 77531, 315947, 1354279,
    6087421, 28611385, 140239297, 715116827, 3785445032, 20760746393,
    117759236340, 689745339984, 4165874930885, 25911148634728,
    165775085602106, 1089773992530717, 7353740136527305,
]


def set_partitions(n: int) -> list[list[list[int]]]:
    if n == 0:
        return [[]]
    res: list[list[list[int]]] = []
    for p in set_partitions(n - 1):
        for i in range(len(p)):
            np = [b[:] for b in p]
            np[i].append(n)
            res.append(np)
        res.append([b[:] for b in p] + [[n]])
    return res


def is_strongly_monotone(part: list[list[int]]) -> bool:
    ordered = sorted(part, key=lambda b: b[0])
    maxs = [b[-1] for b in ordered]
    return all(maxs[i] < maxs[i + 1] for i in range(len(maxs) - 1))


def phi_bijection(n: int, part: list[list[int]]) -> tuple[tuple[str, int], ...]:
    """Bijection from strongly monotone partitions of [n] to labeled Motzkin paths M_n."""
    by_elem = {}
    for b in part:
        bs = sorted(b)
        for x in bs:
            by_elem[x] = bs
    Q: list[list[int]] = []
    path = []
    for t in range(1, n + 1):
        b = by_elem[t]
        if len(b) == 1:
            assert not Q
            path.append(("H0", 0))
        elif t == b[0]:
            Q.append(b)
            path.append(("U", 0))
        elif t == b[-1]:
            assert Q and Q[0] == b
            Q.pop(0)
            path.append(("D", 0))
        else:
            r = Q.index(b) + 1
            path.append(("H", r))
    assert not Q
    return tuple(path)


def phi_inverse(path: tuple[tuple[str, int], ...]) -> list[list[int]]:
    Q: list[list[int]] = []
    closed: list[list[int]] = []
    for idx, (step, r) in enumerate(path, start=1):
        if step == "H0":
            assert not Q
            closed.append([idx])
        elif step == "U":
            Q.append([idx])
        elif step == "D":
            b = Q.pop(0)
            b.append(idx)
            closed.append(b)
        elif step == "H":
            Q[r - 1].append(idx)
        else:
            raise AssertionError(step)
    assert not Q
    return sorted(closed, key=lambda b: b[0])


def count_labeled_motzkin(n: int) -> int:
    dp = {0: 1}
    for _ in range(n):
        nxt: dict[int, int] = {}
        for h, cnt in dp.items():
            if h == 0:
                nxt[0] = nxt.get(0, 0) + cnt
                nxt[1] = nxt.get(1, 0) + cnt
            else:
                nxt[h + 1] = nxt.get(h + 1, 0) + cnt
                nxt[h - 1] = nxt.get(h - 1, 0) + cnt
                nxt[h] = nxt.get(h, 0) + h * cnt
        dp = nxt
    return dp.get(0, 0)


def compute_b(limit: int) -> list[int]:
    b = [0] * (limit + 1)
    b[0] = 1
    for r in range(1, limit + 1):
        m = 0
        t = r
        while t % 2 == 0:
            t //= 2
            m += 1
        n = (t - 1) // 2
        if m == 0:
            b[r] = b[n]
        else:
            b[r] = sum(comb(m - 1, k) * b[(1 << k) * n] for k in range(m))
    return b


def series_inv(p: list[Fraction]) -> list[Fraction]:
    """Inverse of formal power series p with p[0] != 0."""
    deg = len(p)
    q = [Fraction(0)] * deg
    q[0] = Fraction(1) / p[0]
    for k in range(1, deg):
        s = sum(p[i] * q[k - i] for i in range(1, k + 1))
        q[k] = -s * q[0]
    return q


def series_mul(a: list[Fraction], b: list[Fraction], deg: int) -> list[Fraction]:
    res = [Fraction(0)] * deg
    for i in range(min(len(a), deg)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), deg - i)):
            res[i + j] += a[i] * b[j]
    return res


def series_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [x + y for x, y in zip(a, b)]


def check_section1_and_kurkov_values() -> list[Fraction]:
    # Brute force strongly monotone partitions & bijection for n=0..7
    for n in range(8):
        parts = [sorted(p, key=lambda b: b[0]) for p in set_partitions(n) if is_strongly_monotone(p)]
        assert len(parts) == OEIS_A092920[n]
        assert count_labeled_motzkin(n) == OEIS_A092920[n]
        seen_paths = set()
        for p in parts:
            path = phi_bijection(n, p)
            assert phi_inverse(path) == p
            seen_paths.add(path)
        assert len(seen_paths) == len(parts)

    # Continued fraction B_m(x) and A(x) up to degree 27
    DEG = 28
    # Compute B_m(x) backwards from m = DEG down to 0
    B_cur = [Fraction(1)] + [Fraction(0)] * (DEG - 1)
    for m in range(DEG, -1, -1):
        # B_m = 1 / (1 - (m+1)x - x^2 B_{m+1})
        denom = [Fraction(1), Fraction(-(m + 1))] + [-c for c in B_cur[: DEG - 2]]
        B_cur = series_inv(denom)
        if m == 0:
            B0 = B_cur
    # A = 1 / (1 - x - x^2 B_0)
    denom_A = [Fraction(1), Fraction(-1)] + [-c for c in B0[: DEG - 2]]
    A = series_inv(denom_A)
    assert [int(A[n]) for n in range(DEG)] == OEIS_A092920

    # Compute b(0..2^14 - 1) and verify a(1..15) == sum_{k=0}^{2^{n-1}-1} b(k)
    b = compute_b((1 << 14) - 1)
    for n in range(1, 16):
        s = sum(b[: 1 << (n - 1)])
        assert s == OEIS_A092920[n]

    print("Section 1 & Data PASS: bijection (n<=7), continued fraction (n<=27), and Kurkov b(k) sum (n<=15) verified.")
    return A


def check_sections2_and_3(A: list[Fraction]) -> None:
    N_MAX = 12
    b = compute_b(1 << 18)

    # Compute R_j(N) = sum_{r=0}^{2^N-1} b(2^j * r) directly for N=0..8, j=0..10
    R = {}
    for N in range(9):
        for j in range(11):
            R[(N, j)] = sum(b[(1 << j) * r] for r in range(1 << N))
    for j in range(11):
        assert R[(0, j)] == 1
    for N in range(1, 9):
        assert R[(N, 0)] == R[(N - 1, 1)] + R[(N - 1, 0)]
        for j in range(1, 10):
            assert R[(N, j)] == R[(N - 1, j + 1)] + sum(comb(j - 1, k) * R[(N - 1, k)] for k in range(j))

    # Build exact F_N(u) as Laurent/polynomial in u = e^z using differential recurrence:
    # F_0(u) = u; F_N'(z) = u d/du F_N = (u d/du)^2 F_{N-1} + u F_{N-1}
    # If F_{N-1}(u) = sum_{k=0}^N c_k u^k, then u d/du F_N = sum_{k>=1} (k^2 c_k + c_{k-1}) u^k,
    # so for k >= 1, [u^k] F_N = (k^2 c_k + c_{k-1}) / k, and [u^0] F_N = F_N(0) - sum_{k>=1} [u^k] F_N.
    F: list[list[Fraction]] = [[Fraction(0), Fraction(1)]]  # F_0(u) = u
    for N in range(1, N_MAX + 1):
        prev = F[-1]
        # F_N(0) = F_{N-1}(0) + F_{N-1}'(0) = sum_k c_k + sum_k k c_k = sum_k (k+1) c_k
        fn_0 = sum((k + 1) * c for k, c in enumerate(prev))
        nxt = [Fraction(0)] * (N + 2)
        for k in range(1, N + 2):
            ck = prev[k] if k < len(prev) else Fraction(0)
            ck_m1 = prev[k - 1] if k - 1 < len(prev) else Fraction(0)
            nxt[k] = (k * k * ck + ck_m1) / k
        nxt[0] = fn_0 - sum(nxt[1:])
        F.append(nxt)
        # Verify R_j(N) == sum_k c_k k^j for small N, j
        if N <= 8:
            for j in range(10):
                val = sum(c * (k ** j) for k, c in enumerate(nxt))
                assert val == R[(N, j)]

    # Build H(x, u) = 1 + sum_{N=0}^{N_MAX} F_N(u) x^{N+1} up to x^{N_MAX+1}
    DEG_X = N_MAX + 2
    MAX_U = N_MAX + 2
    p: list[list[Fraction]] = [[Fraction(0)] * DEG_X for _ in range(MAX_U)]
    p[0][0] = Fraction(1)
    for N in range(N_MAX + 1):
        for k, c in enumerate(F[N]):
            p[k][N + 1] = c
        # Check p_k(x) in x^k Q[[x]]? Note k <= N+1 => lowest x-deg is at least max(0, k-1)! Wait:
        # Wait: F_N has u-deg N+1, multiplied by x^{N+1}, so p_k(x) has [x^m] only for m >= k! Exact!
    for k in range(MAX_U):
        assert all(p[k][m] == 0 for m in range(min(k, DEG_X)))

    # Check PDE: x u H_uu + (x - 1) H_u + x H == 0, i.e. for each k >= 0:
    # (k+1)((k+1)x - 1) p_{k+1}(x) + x p_k(x) == 0 mod x^{DEG_X}
    for k in range(MAX_U - 1):
        term1 = series_mul(p[k + 1], [Fraction(-(k + 1)), Fraction((k + 1) ** 2)], DEG_X)
        term2 = [Fraction(0)] + p[k][: DEG_X - 1]
        assert series_add(term1, term2) == [Fraction(0)] * DEG_X

    # Check boundary condition (1-x)H(x,1) - x d_u H(x,1) == 1
    H1 = [sum(p[k][d] for k in range(MAX_U)) for d in range(DEG_X)]
    Hu1 = [sum(k * p[k][d] for k in range(MAX_U)) for d in range(DEG_X)]
    lhs = series_add(
        series_mul(H1, [Fraction(1), Fraction(-1)], DEG_X),
        [Fraction(0)] + [-c for c in Hu1[: DEG_X - 1]],
    )
    assert lhs == [Fraction(1)] + [Fraction(0)] * (DEG_X - 1)

    # Section 3: U_m(x), C_m(x), and H(x, 1) == A(x)
    def build_U(m: int, deg: int) -> list[Fraction]:
        U = [Fraction(0)] * deg
        fact = 1
        for r in range(deg):
            if r > 0:
                fact *= r
            # prod_{j=1}^r (1 - (m+j)x)
            den = [Fraction(1)] + [Fraction(0)] * (deg - 1)
            for j in range(1, r + 1):
                den = series_mul(den, [Fraction(1), Fraction(-(m + j))], deg)
            inv_den = series_inv(den)
            term = [Fraction(0)] * r + [inv_den[t] / fact for t in range(deg - r)]
            U = series_add(U, term)
        return U

    U0 = build_U(0, DEG_X)
    U1 = build_U(1, DEG_X)
    U2 = build_U(2, DEG_X)
    S1_from_U1 = series_mul([Fraction(0), Fraction(1)], series_mul(U1, series_inv([Fraction(1), Fraction(-1)] + [Fraction(0)] * (DEG_X - 2)), DEG_X), DEG_X)
    # Compare S1 directly vs H(x,1)
    C0 = series_mul(U1, series_inv(series_mul([Fraction(1), Fraction(-1)] + [Fraction(0)] * (DEG_X - 2), U0, DEG_X)), DEG_X)
    C1 = series_mul(U2, series_inv(series_mul([Fraction(1), Fraction(-2)] + [Fraction(0)] * (DEG_X - 2), U1, DEG_X)), DEG_X)
    # Check C_0(x) = 1 / (1 - x - x^2 C_1(x))
    rhs_C0 = series_inv(series_add([Fraction(1), Fraction(-1)] + [Fraction(0)] * (DEG_X - 2), [Fraction(0), Fraction(0)] + [-c for c in C1[: DEG_X - 2]]))
    assert C0 == rhs_C0
    # Check S1_from_U1 / (x U0) == C0
    assert S1_from_U1[0] == 0
    assert series_mul(S1_from_U1[1:] + [Fraction(0)], series_inv(U0), DEG_X - 1) == C0[:-1]
    assert H1 == A[:DEG_X]

    print(f"Sections 2 & 3 PASS: R_j(N), F_N PDE, boundary cond, U_m / C_m CF identity, and H(x,1)==A(x) verified to deg {DEG_X-1}.")


def main() -> None:
    A = check_section1_and_kurkov_values()
    check_sections2_and_3(A)
    print("PASS")


if __name__ == "__main__":
    main()
