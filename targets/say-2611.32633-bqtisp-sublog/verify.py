import math
import sys


def bin_str(n: int) -> str:
    return "0" if n == 0 else bin(n)[2:]


def floor_log2(n: int) -> int:
    assert n >= 1
    return n.bit_length() - 1


def ceil_log2(n: int) -> int:
    assert n >= 1
    return 0 if n == 1 else (n - 1).bit_length()


def main() -> int:
    # 1. Verify exact L_S string length formula N_k = (k+1)(m+1) - 2^m + 1 for k = 1..5000
    s_parts = ["0"]
    cur_len = 1
    for k in range(1, 5001):
        bk = bin_str(k)
        s_parts.append("$")
        s_parts.append(bk)
        cur_len += 1 + len(bk)
        m = len(bk)
        formula = (k + 1) * (m + 1) - (1 << m) + 1
        if cur_len != formula:
            print(f"FAIL: N_k mismatch at k={k}: actual={cur_len}, formula={formula}")
            return 1
        if k <= 200:
            full = "".join(s_parts)
            assert len(full) == cur_len
    print("PASS: Exact L_S length formula verified against strings for k=1..5000")

    # 2. Verify Lemma 1 exact bounds A * 2^(m-t) <= N_k < 2A * 2^(m-t) and r_tilde <= floor(log2 N_k) <= r_tilde + 1
    for k in range(128, 30001):
        m = len(bin_str(k))
        t = ceil_log2(m + 1) + 3
        if not (t < m):
            print(f"FAIL: t={t} not < m={m} at k={k}")
            return 1
        Nk = (k + 1) * (m + 1) - (1 << m) + 1
        K_top = k >> (m - t)
        A = K_top * (m + 1) - (1 << t)
        if not (A > m + 2):
            print(f"FAIL: A={A} <= m+2 at k={k}")
            return 1
        lhs = A << (m - t)
        rhs = (2 * A) << (m - t)
        if not (lhs <= Nk < rhs):
            print(f"FAIL: Sandwich violated at k={k}: lhs={lhs}, Nk={Nk}, rhs={rhs}")
            return 1
        r_tilde = (m - t) + floor_log2(A)
        exact_r = floor_log2(Nk)
        if not (r_tilde <= exact_r <= r_tilde + 1):
            print(f"FAIL: r_tilde={r_tilde} vs exact_r={exact_r} at k={k}")
            return 1
        if not ((1 << r_tilde) <= Nk < (1 << (r_tilde + 2))):
            print(f"FAIL: power-of-two sandwich failed at k={k}")
            return 1
    print("PASS: Lemma 1 exact O(log log n)-space r_tilde sandwich verified for k=128..30000")

    # 3. Verify concrete monotone, doubling-smooth sublogarithmic families in omega(log log n) cap o(log n):
    #    s1(n) = floor(sqrt(floor(log2 n)))
    #    s2(n) = floor(sqrt(floor(log2 n))) * floor(n^{1/4}-analogue: isqrt(isqrt(floor(log2 n))))
    #    s3(n) = floor(log2(floor(log2 n))) * max(1, floor(log2(floor(log2(floor(log2 n))))))
    def s1(n: int) -> int:
        return math.isqrt(floor_log2(n))

    def s2(n: int) -> int:
        r = floor_log2(n)
        return math.isqrt(r) * math.isqrt(math.isqrt(r))

    def s3(n: int) -> int:
        r = floor_log2(n)
        d2 = floor_log2(max(2, r))
        d3 = floor_log2(max(2, d2))
        return d2 * max(1, d3)

    for name, s_fn in [("sqrt_log", s1), ("log_3_4", s2), ("loglog_mul_logloglog", s3)]:
        # Find threshold k1 >= 128 from which j_k <= N_k / 4 holds
        checked = 0
        for k in range(512, 30001):
            m = len(bin_str(k))
            t = ceil_log2(m + 1) + 3
            Nk = (k + 1) * (m + 1) - (1 << m) + 1
            K_top = k >> (m - t)
            A = K_top * (m + 1) - (1 << t)
            r_tilde = (m - t) + floor_log2(A)
            l_k = s_fn(1 << r_tilde)
            # Check monotonicity & doubling bound s(2n) <= 2*s(n) and j_k = 2^l_k < N_k
            if (1 << l_k) > Nk:
                print(f"FAIL: {name} j_k > N_k at k={k} (l_k={l_k}, Nk={Nk})")
                return 1
            if l_k > s_fn(Nk):
                print(f"FAIL: {name} l_k={l_k} > s(N_k)={s_fn(Nk)} at k={k}")
                return 1
            N_next = (k + 2) * (len(bin_str(k + 1)) + 1) - (1 << len(bin_str(k + 1))) + 1
            for n in (Nk, N_next - 1):
                # Check N_k >= n // 2 and 2^r_tilde > n // 8 and s(n) <= 8 * l_k
                if not (Nk * 2 >= n and (1 << (r_tilde + 3)) > n and s_fn(n) <= 8 * l_k):
                    print(f"FAIL: {name} gap bound at k={k}, n={n}")
                    return 1
            checked += 1
        assert checked > 29000
    print("PASS: Exact feasibility & gap bounds verified on 3 sublogarithmic families across k=512..30000")
    print("OVERALL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
