"""Independent exact-arithmetic verifier for targets/ziller-2310.15628-conj6.2/."""

from fractions import Fraction
from math import gcd
import signal

signal.alarm(50)


def totient_sieve(n_max: int) -> tuple[list[int], list[int]]:
    phi = list(range(n_max + 1))
    spf = list(range(n_max + 1))
    for i in range(2, n_max + 1):
        if spf[i] == i:
            phi[i] = i - 1
            for j in range(2 * i, n_max + 1, i):
                if spf[j] == j:
                    spf[j] = i
                phi[j] = (phi[j] // i) * (i - 1)
    return phi, spf


def factorize(n: int, spf: list[int]) -> dict[int, int]:
    fac: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        fac[p] = e
    return fac


def vp_rat(num: int, den: int, p: int) -> int:
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def main() -> None:
    N = 200_000
    phi, spf = totient_sieve(N)

    # 1. Exact injectivity of phi(x)/x^2 and x^2/phi(x) on 1 <= x <= N
    seen: set[tuple[int, int]] = set()
    for x in range(1, N + 1):
        num = phi[x]
        den = x * x
        g = gcd(num, den)
        key = (num // g, den // g)
        assert key not in seen, f"Collision at x={x}"
        seen.add(key)
    assert len(seen) == N
    print(f"Injectivity PASS: all {N} reduced fractions phi(x)/x^2 (1 <= x <= {N}) are pairwise distinct.")

    # 2. Verify PROOF.md product formula and largest-prime p-adic valuation formula on 1 <= n <= 10000
    for n in range(1, 10_001):
        fac = factorize(n, spf)
        prod_val = Fraction(1, 1)
        for q, eq in fac.items():
            prod_val *= Fraction(q - 1, q ** (eq + 1))
        direct = Fraction(phi[n], n * n)
        assert prod_val == direct

        if n > 1:
            p = max(fac)
            eq = fac[p]
            assert vp_rat(direct.numerator, direct.denominator, p) == -(eq + 1)
            # For any prime r > p (check next prime up to p+20), v_r(f(n)) == 0
            r = p + 1
            while r <= 10_000 and spf[r] != r:
                r += 1
            if r <= 10_000:
                assert vp_rat(direct.numerator, direct.denominator, r) == 0

    # 3. Verify multiplicativity reduction f(p^e * x0) = f(p^e) * f(x0) and v_p invariance
    for x in range(2, 200):
        for y in range(x + 1, 201):
            p = max(max(factorize(x, spf)), max(factorize(y, spf)))
            fx = Fraction(phi[x], x * x)
            fy = Fraction(phi[y], y * y)
            vx = vp_rat(fx.numerator, fx.denominator, p)
            vy = vp_rat(fy.numerator, fy.denominator, p)
            ex = 0
            tx = x
            while tx % p == 0:
                tx //= p
                ex += 1
            ey = 0
            ty = y
            while ty % p == 0:
                ty //= p
                ey += 1
            assert vx == (0 if ex == 0 else -(ex + 1))
            assert vy == (0 if ey == 0 else -(ey + 1))
            if ex != ey:
                assert vx != vy and fx != fy
            else:
                e = ex
                assert e >= 1
                fpe = Fraction(p - 1, p ** (e + 1))
                assert fx == fpe * Fraction(phi[tx], tx * tx)
                assert fy == fpe * Fraction(phi[ty], ty * ty)
                assert tx * ty < x * y

    print("Proof Lemma & Descent PASS: product formula, v_p(f(n)) == -(e+1), and p^e-descent verified.")
    print("PASS")


if __name__ == "__main__":
    main()
