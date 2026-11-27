import math
import signal
from fractions import Fraction

signal.alarm(30)


def count_smp_dp(max_n: int) -> list[int]:
    """Compute a(n) for n=0..max_n via the proved weighted-Motzkin transfer."""
    res = [1]
    dp = [1] + [0] * (max_n + 2)
    for n in range(1, max_n + 1):
        ndp = [0] * (max_n + 3)
        for h in range(n + 1):
            w = 1 if h == 0 else h
            val = w * dp[h]
            if h > 0:
                val += dp[h - 1]
            val += dp[h + 1]
            ndp[h] = val
        dp = ndp
        res.append(dp[0])
    return res


def poly_mul(a: list[Fraction], b: list[Fraction], deg: int) -> list[Fraction]:
    out = [Fraction(0)] * deg
    for i in range(deg):
        if a[i] == 0:
            continue
        for j in range(deg - i):
            out[i + j] += a[i] * b[j]
    return out


def poly_inv(a: list[Fraction], deg: int) -> list[Fraction]:
    inv0 = Fraction(1) / a[0]
    b = [Fraction(0)] * deg
    b[0] = inv0
    for i in range(1, deg):
        b[i] = -sum(a[j] * b[i - j] for j in range(1, i + 1)) * inv0
    return b


def main() -> None:
    # 1. Verify bijection against brute-force strongly monotone partitions for n = 0..8
    def is_smp(part: list[list[int]]) -> bool:
        s = sorted(part, key=lambda blk: blk[0])
        maxs = [max(blk) for blk in s]
        return all(maxs[i] < maxs[i + 1] for i in range(len(maxs) - 1))

    def gen_parts(n: int):
        if n == 0:
            yield []
            return
        def rec(k: int, cur: list[list[int]]):
            if k > n:
                yield [list(blk) for blk in cur]
                return
            for i in range(len(cur)):
                cur[i].append(k)
                yield from rec(k + 1, cur)
                cur[i].pop()
            cur.append([k])
            yield from rec(k + 1, cur)
            cur.pop()
        yield from rec(1, [])

    a_motz = count_smp_dp(27)
    for n in range(0, 9):
        cnt = sum(1 for p in gen_parts(n) if is_smp(p))
        assert cnt == a_motz[n], f"Bijection check failed at n={n}"

    # Check against all 28 published OEIS A092920 terms (n = 0..27)
    oeis_data = [
        1, 1, 2, 4, 9, 22, 58, 164, 496, 1601, 5502, 20075, 77531, 315947,
        1354279, 6087421, 28611385, 140239297, 715116827, 3785445032,
        20760746393, 117759236340, 689745339984, 4165874930885,
        25911148634728, 165775085602106, 1089773992530717, 7353740136527305,
    ]
    assert a_motz == oeis_data, "Motzkin DP mismatch with OEIS A092920 data"

    # 2. Compute b(k) directly from Kurkov's definition for 0 <= k < 2^19 and check n = 1..20
    N_BITS = 19
    L = 1 << N_BITS
    b = [0] * L
    b[0] = 1
    for x in range(1, L):
        m = (x & -x).bit_length() - 1
        n_odd = x >> (m + 1)
        if m == 0:
            b[x] = b[n_odd]
        else:
            b[x] = sum(math.comb(m - 1, k) * b[(1 << k) * n_odd] for k in range(m))

    for n in range(1, N_BITS + 2):
        s = sum(b[: 1 << (n - 1)])
        assert s == a_motz[n], f"Direct sum mismatch at n={n}"

    # 3. Verify Section 2 & 3 exact series identities up to x^28
    DEG = 29
    # Compute H(x, 1) from S0, S1
    S0 = [Fraction(0)] * DEG
    S1 = [Fraction(0)] * DEG
    term = [Fraction(0)] * DEG
    term[0] = Fraction(1)
    S0[0] = Fraction(1)
    for k in range(1, DEG):
        shifted = [Fraction(0)] + [term[i] / k for i in range(DEG - 1)]
        new_term = [Fraction(0)] * DEG
        for i in range(DEG):
            new_term[i] = shifted[i] + (k * new_term[i - 1] if i > 0 else 0)
        term = new_term
        for i in range(DEG):
            S0[i] += term[i]
            S1[i] += k * term[i]

    # (1 - x) * S0 - x * S1
    denom = [S0[i] - (S0[i - 1] + S1[i - 1] if i > 0 else 0) for i in range(DEG)]
    H_at_1 = poly_mul(S0, poly_inv(denom, DEG), DEG)
    assert [int(c) for c in H_at_1[:28]] == oeis_data, "H(x, 1) mismatch with A092920"

    print("PASS: verified SMP bijection (n=0..8), direct b(k) sum (n=1..20), and H(x,1)=A(x) series (n=0..27).")


if __name__ == "__main__":
    main()
