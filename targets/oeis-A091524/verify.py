import math
import signal

signal.alarm(30)


def floor_sqrt2(k: int) -> int:
    """Exact floor(k * sqrt(2)) for integer k >= 0."""
    return math.isqrt(2 * k * k)


def floor_div_sqrt2(k: int) -> int:
    """Exact floor(k / sqrt(2)) for integer k >= 0."""
    return math.isqrt((k * k) // 2)


def main() -> None:
    N = 10000

    # 1. Exact Beatty partition B1 = A003152, B2 = A003151
    B1 = [k + floor_div_sqrt2(k) for k in range(1, N + 1)]
    B2 = [k + floor_sqrt2(k) for k in range(1, N + 1)]
    pos_to_k = {}
    for k, m in enumerate(B1, start=1):
        if m <= N:
            assert m not in pos_to_k
            pos_to_k[m] = ("B1", k)
    for k, m in enumerate(B2, start=1):
        if m <= N:
            assert m not in pos_to_k
            pos_to_k[m] = ("B2", k)
    assert len(pos_to_k) == N, "Beatty partition failed"

    # 2. Check Graham-Pollak recurrence u_1 = m, u_{r+1} = floor(sqrt(2)*(u_r + 1/2))
    #    using exact integer arithmetic: floor((2u+1)/sqrt(2)) = isqrt((2u+1)^2 // 2)
    #    against closed form u_r = floor(tau_m * (2^((r-1)/2) + 2^((r-2)/2)))
    #    and verify first 40 binary bits of {k*sqrt(2)} for m = 1..500.
    for m in range(1, 501):
        kind, k = pos_to_k[m]
        u = [0, m]
        for _ in range(85):
            u.append(math.isqrt(((2 * u[-1] + 1) ** 2) // 2))

        for r in range(1, 84):
            if kind == "B1":
                # tau_m = k: x_r = k*(2^((r-1)/2) + 2^((r-2)/2))
                if r % 2 == 1:
                    j = (r - 1) // 2
                    p2 = 1 << j
                    expected = (k * p2) + floor_div_sqrt2(k * p2)
                else:
                    j = r // 2
                    p2 = 1 << (j - 1)
                    expected = (k * p2) + floor_sqrt2(k * p2)
            else:
                # tau_m = k*sqrt(2)
                if r % 2 == 1:
                    j = (r - 1) // 2
                    p2 = 1 << j
                    expected = (k * p2) + floor_sqrt2(k * p2)
                else:
                    j = r // 2
                    p2 = 1 << j
                    expected = (k * p2) + floor_sqrt2((k * p2) // 2)
            assert u[r] == expected, f"tau_m formula failed at m={m}, r={r}"

        # Check binary bits d_j = u_{2j+2} - 2*u_{2j} == floor(2^j*k*sqrt(2)) - 2*floor(2^(j-1)*k*sqrt(2))
        for j in range(1, 41):
            d_j = u[2 * j + 2] - 2 * u[2 * j]
            bit_k = floor_sqrt2((1 << j) * k) - 2 * floor_sqrt2((1 << (j - 1)) * k)
            assert d_j == bit_k and d_j in (0, 1), f"Bit mismatch at m={m}, j={j}"

    # 3. Verify OEIS A091524 initial 75 terms
    oeis_a091524 = [
        1,1,2,2,3,4,3,5,4,6,7,5,8,6,9,7,10,11,8,12,9,13,14,10,15,11,16,12,17,
        18,13,19,14,20,21,15,22,16,23,24,17,25,18,26,19,27,28,20,29,21,30,31,
        22,32,23,33,24,34,35,25,36,26,37,38,27,39,28,40,41,29,42,30,43,31,44,
    ]
    for n, val in enumerate(oeis_a091524, start=1):
        assert pos_to_k[n][1] == val, f"A091524 prefix mismatch at n={n}"

    # 4. Compute A028982 = sorted {j^2} U {2*j^2} and A006337 = floor((n+1)*sqrt(2)) - floor(n*sqrt(2))
    T = sorted([j * j for j in range(1, N + 5)] + [2 * j * j for j in range(1, N + 5)])
    for n in range(1, N + 1):
        a_n = pos_to_k[n][1]
        c_n = T[n - 1]  # A028982(n)
        f_n = floor_sqrt2(n + 1) - floor_sqrt2(n)  # A006337(n)
        assert f_n in (1, 2)
        assert c_n % f_n == 0
        assert c_n // f_n == a_n * a_n, f"Ratio mismatch at n={n}: {c_n}/{f_n} vs {a_n}^2"

    print(f"PASS: verified Graham-Pollak tau_m formula & bits (m=1..500) and a(n)^2 = A028982(n)/A006337(n) for all 1 <= n <= {N}.")


if __name__ == "__main__":
    main()
