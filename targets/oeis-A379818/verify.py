import math
import signal

signal.alarm(30)

OEIS_A379818 = [
    1,1,4,1,10,4,10,1,22,10,28,4,49,10,22,1,46,22,64,10,118,28,64,4,190,49,
    118,10,190,22,46,1,94,46,136,22,256,64,148,10,424,118,292,28,478,64,136,
    4,661,190,478,49,796,118,256,10,1177,190,424,22,661,46
]

OEIS_A025480_PREFIX = [
    0,0,1,0,2,1,3,0,4,2,5,1,6,3,7,0,8,4,9,2,10,5,11,1,12,6,13,3,14,7,15,0,
    16,8,17,4,18,9,19,2,20,10,21,5,22,11,23,1
]


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def compute_A025480(N: int):
    b = [0] * (N + 1)
    for r in range(1, N + 1):
        if r % 2 == 0:
            b[r] = r // 2
        else:
            b[r] = b[r // 2]
    return b


def compute_A379818(N: int):
    b = compute_A025480(N)
    a = [0] * (N + 1)
    a[0] = 1
    for i in range(1, N + 1):
        if i % 2 == 1:
            n = (i - 1) // 2
            a[i] = a[n]
        else:
            n = i // 2
            f_n = v2(n)
            p2 = 1 << f_n
            a[i] = a[n] + a[n - p2] + a[2 * n - p2] + a[b[n - 1]]
    return a, b


def main():
    N = 20000
    a, b = compute_A379818(N)

    # 1. Exact check against OEIS data
    assert b[:len(OEIS_A025480_PREFIX)] == OEIS_A025480_PREFIX
    assert a[:len(OEIS_A379818)] == OEIS_A379818

    # 2. Verify Lemma: b[2^r * (2k+1) - 1] == k for all r, k with index <= N
    for idx in range(1, N + 1):
        r = v2(idx)
        k = ((idx >> r) - 1) // 2
        assert b[idx - 1] == k

    # 3. Verify Conjectured Formula for all n = 2^m * (2k+1) in 1..N
    for n in range(1, N + 1):
        m = v2(n)
        k = ((n >> m) - 1) // 2
        rhs = sum(
            (math.comb(m + 2, j + 1) - math.comb(m, j)) * a[(1 << j) * k]
            for j in range(m + 1)
        )
        assert a[n] == rhs, f"Mismatch at n={n} (m={m}, k={k}): {a[n]} != {rhs}"

    print(f"PASS: OEIS A379818 (62 terms) & A025480 (48 terms) matched verbatim; "
          f"Lemma and conjectured formula verified exactly for all 1 <= n <= {N}.")


if __name__ == "__main__":
    main()
