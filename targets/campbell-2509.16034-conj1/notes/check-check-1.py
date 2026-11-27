"""Independent exact checker for targets/campbell-2509.16034-conj1/ (PROOF.md).

Written strictly from arXiv:2509.16034v1 (ReducedComplexityV85.tex) and PROOF.md,
without reading verify.py or notes/.
"""

from collections import deque
from fractions import Fraction


def tm_bit_1idx(k: int) -> int:
    """1-indexed Thue-Morse bit t_k = s_2(k - 1) mod 2."""
    assert k >= 1
    return (k - 1).bit_count() & 1


def red_word(w: str) -> str:
    if not w:
        return ""
    out = [w[0]]
    for ch in w[1:]:
        if ch != out[-1]:
            out.append(ch)
    return "".join(out)


def alternations(w: str) -> int:
    return sum(1 for i in range(len(w) - 1) if w[i] != w[i + 1])


def test_direct_factors() -> tuple[list[int], list[int], list[int]]:
    # Build t[1..4096] (prefix of length 4096 contains all factors up to length ~200)
    L_tm = 4096
    t_str = "".join(str(tm_bit_1idx(k)) for k in range(1, L_tm + 1))

    # Compute m_n, M_n via Lemma 2 (for comparison)
    N = 20000
    m = [0] * (N + 1)
    M = [0] * (N + 1)
    m[1], M[1] = 0, 0
    m[2], M[2] = 0, 1
    m[3], M[3] = 1, 2
    for n in range(4, N + 1):
        if n % 2 == 0:
            j = n // 2
            m[n] = 2 * j - 1 - M[j + 1]
            M[n] = 2 * j - 1 - m[j]
        else:
            j = (n - 1) // 2
            m[n] = 2 * j - M[j + 1]
            M[n] = 2 * j - m[j + 1]

    # Check Lemma 3 (tm_mod4) against Lemma 2 for 1 <= n <= 4999
    for n in range(1, 5000):
        assert m[4 * n] == 2 * n - 1 + m[n + 1]
        assert M[4 * n] == 2 * n + M[n + 1]
        assert m[4 * n + 2] == 2 * n + m[n + 1]
        assert M[4 * n + 2] == 2 * n + 1 + M[n + 1]

    # Direct factor enumeration for n = 1..120
    direct_rho = [0] * 121
    for n in range(1, 121):
        ab_classes = set()
        alts = []
        for start in range(L_tm - n + 1):
            w = t_str[start : start + n]
            rw = red_word(w)
            ab_classes.add((len(rw), rw.count("0"), rw.count("1")))
            alts.append(len(rw) - 1)
        assert min(alts) == m[n] and max(alts) == M[n], f"min/max alt mismatch at n={n}"
        direct_rho[n] = len(ab_classes)

    # Check eq. (numericalproblem) from paper lines 667: (2, 3, 3, 4, 3, 5, 4, 5, 3, 4, 5, 6, 4, 6, 5, 4, 3, 5, 4)
    paper_prefix = [2, 3, 3, 4, 3, 5, 4, 5, 3, 4, 5, 6, 4, 6, 5, 4, 3, 5, 4]
    assert direct_rho[1 : len(paper_prefix) + 1] == paper_prefix

    # Compute rho from Theorem 1 up to N = 20000 and verify exact equality with direct_rho for 1..120
    rho = [0] * (N + 1)
    for n in range(1, N + 1):
        s_sum = sum(1 + (r % 2) for r in range(m[n] + 1, M[n] + 2))
        closed_num = 3 * (M[n] - m[n] + 1) * 2 + ((-1) ** m[n] + (-1) ** M[n])
        assert closed_num % 4 == 0
        closed = closed_num // 4
        assert s_sum == closed
        rho[n] = s_sum
        if n <= 120:
            assert rho[n] == direct_rho[n], f"Theorem 1 mismatch at n={n}"

    print("Direct factor enumeration (1<=n<=120), paper prefix (1..19), Lemma 2/3, & Theorem 1 (1<=n<=20000): OK")
    return m, M, rho


def test_theorem2_and_2kernel(m: list[int], M: list[int], rho: list[int]) -> None:
    N = len(rho) - 1
    # Theorem 2(1): rho(2n+1) == rho(n+1) for n >= 0
    for n in range(0, (N - 1) // 2 + 1):
        assert rho[2 * n + 1] == rho[n + 1]

    # Theorem 2(2): rho(4n) and rho(4n+2) for n >= 1
    for n in range(1, (N - 2) // 4 + 1):
        assert rho[4 * n] == rho[n + 1] + 1 + (m[n + 1] % 2)
        assert rho[4 * n + 2] == rho[n + 1] + 1 + (M[n + 1] % 2)

    # Theorem 2(3): alpha_k, beta_k recurrences & 2-kernel closure
    alpha = [m[k] % 2 for k in range(N + 1)]
    beta = [M[k] % 2 for k in range(N + 1)]
    assert (alpha[1], beta[1]) == (0, 0)
    assert (alpha[2], beta[2]) == (0, 1)
    assert (alpha[3], beta[3]) == (1, 0)
    for j in range(2, N // 2):
        assert alpha[2 * j] == 1 - beta[j + 1]
        assert beta[2 * j] == 1 - alpha[j]
        assert alpha[2 * j + 1] == beta[j + 1]
        assert beta[2 * j + 1] == alpha[j + 1]

    # Verify exact 2-kernel sizes claimed in PROOF.md line 59 (1-indexed subsequences vs shifted x_k = alpha_{k+1})
    # For a 1-indexed sequence seq[1..N], 2-kernel elements are seq[2^e * k + r] for k >= 1 (or k >= 0 for shifted).
    # Let's check 1-indexed k >= 1 (truncated to first M_chk terms) AND 0-indexed shifted!
    def kernel_size_1idx(seq: list[int], M_chk: int = 200) -> int:
        # 2-kernel over { (2^e, r) : 0 <= r < 2^e } on k >= 1
        seen: set[tuple[int, ...]] = set()
        queue = deque([(1, 0)])
        visited_params = {(1, 0)}
        while queue:
            p2, r = queue.popleft()
            vec = tuple(seq[p2 * k + r] for k in range(1, M_chk + 1))
            if vec in seen:
                continue
            seen.add(vec)
            for b in (0, 1):
                np2, nr = 2 * p2, r + b * p2
                if np2 * M_chk + nr <= N and (np2, nr) not in visited_params:
                    visited_params.add((np2, nr))
                    queue.append((np2, nr))
        return len(seen)

    def kernel_size_shifted(seq: list[int], M_chk: int = 200) -> int:
        # x_k = seq[k + 1] for k >= 0 (or k >= 1): check both!
        # Using k >= 0: x_0 = seq[1], x_k = seq[k+1]
        seen: set[tuple[int, ...]] = set()
        queue = deque([(1, 0)])
        visited_params = {(1, 0)}
        while queue:
            p2, r = queue.popleft()
            vec = tuple(seq[p2 * k + r + 1] for k in range(0, M_chk))
            if vec in seen:
                continue
            seen.add(vec)
            for b in (0, 1):
                np2, nr = 2 * p2, r + b * p2
                if np2 * M_chk + nr + 1 <= N and (np2, nr) not in visited_params:
                    visited_params.add((np2, nr))
                    queue.append((np2, nr))
        return len(seen)

    ka = kernel_size_1idx(alpha)
    kb = kernel_size_1idx(beta)
    kxa = kernel_size_shifted(alpha)
    kxb = kernel_size_shifted(beta)
    print(f"2-kernel sizes: alpha={ka}, beta={kb}, alpha_{{k+1}}={kxa}, beta_{{k+1}}={kxb}")
    assert ka == 9 and kb == 10 and kxa == 8 and kxb == 8

    # Verify exact 8-state transition closure of shifted a'_k = alpha[k+1], b'_k = beta[k+1] for ALL k >= 0
    ap = [alpha[k + 1] for k in range(N)]
    bp = [beta[k + 1] for k in range(N)]
    for k in range(0, (N - 3) // 2):
        assert ap[2 * k] == bp[k]
        assert bp[2 * k] == ap[k]
        assert ap[2 * k + 1] == 1 - bp[k + 1]
        assert bp[2 * k + 1] == 1 - ap[k]
        assert ap[2 * k + 2] == bp[k + 1]
        assert bp[2 * k + 2] == ap[k + 1]

    # Verify Theorem 1(3) exact linear combination with rho_red(n) = 2(M_n - m_n + 1)
    for n in range(1, N + 1):
        rho_red_n = 2 * (M[n] - m[n] + 1)
        rhs = Fraction(3, 4) * rho_red_n + Fraction((-1) ** m[n] + (-1) ** M[n], 4)
        assert rhs == rho[n]

    # Also verify Theorem 2(4) unbounded sequence n_j = (4 + 2*4^j)/3
    n_j = 2
    for j in range(8):
        if n_j > N:
            break
        assert (4 + 2 * (4**j)) // 3 == n_j
        assert rho[n_j] >= 3 + j
        n_j = 4 * (n_j - 1)
    print("Rescoped Theorem 1 (odd/4n/4n+2 recurrences, 8-state 2-kernel, 2-regularity, unboundedness): OK")


def test_theorem3_sign_and_induction(m: list[int], M: list[int], rho: list[int]) -> None:
    N = len(rho) - 1
    max_n = (N - 2) // 4
    # Rescoped Theorem 2(1) and 2(2): exact signed difference & nonzero sign formula
    for n in range(1, max_n + 1):
        diff = rho[4 * n + 2] - rho[4 * n]
        an1 = m[n + 1] % 2
        bn1 = M[n + 1] % 2
        assert diff == bn1 - an1
        assert diff == ((-1) ** m[n + 1] - (-1) ** M[n + 1]) // 2
        assert diff in (-1, 0, 1)
        t_n1 = tm_bit_1idx(n + 1)
        t_3n1 = tm_bit_1idx(3 * n + 1)
        assert abs(diff) == (0 if t_n1 == t_3n1 else 1)
        if diff != 0:
            assert an1 == 1 - bn1
            assert diff == 2 * bn1 - 1 == (-1) ** (1 - bn1)

    # Strong induction verification for k = 1..max_n+1
    d = [0] * (max_n + 2)
    f = [0] * (max_n + 2)
    for k in range(1, max_n + 2):
        d[k] = (M[k] - m[k]) % 2
        f[k] = tm_bit_1idx(k) ^ tm_bit_1idx(3 * k - 2)
        assert d[k] == f[k]
        if k >= 4:
            if k % 2 == 1:
                j = (k - 1) // 2
                assert d[k] == d[j + 1] and f[k] == f[j + 1]
            elif k % 4 == 0:
                i = k // 4
                assert d[k] == (1 ^ d[i + 1]) and f[k] == (1 ^ f[i + 1])
                # Verify v_2(3i) == v_2(i) identity in PROOF.md lines 95-96
                v_i = (i & -i).bit_length() - 1
                v_3i = ((3 * i) & -(3 * i)).bit_length() - 1
                assert v_i == v_3i
                assert (tm_bit_1idx(i + 1) ^ tm_bit_1idx(i)) == ((1 + v_i) & 1)
                assert (tm_bit_1idx(3 * i + 1) ^ tm_bit_1idx(3 * i)) == ((1 + v_3i) & 1)
            else:
                assert k % 4 == 2
                i = (k - 2) // 4
                assert d[k] == (1 ^ d[i + 1]) and f[k] == (1 ^ f[i + 1])
    print(f"Rescoped Theorem 2 (exact sign, nonzero formula 2b_{{n+1}}-1, strong induction 1<=n<={max_n}): OK")


def main() -> None:
    m, M, rho = test_direct_factors()
    test_theorem2_and_2kernel(m, M, rho)
    test_theorem3_sign_and_induction(m, M, rho)
    print("PASS")


if __name__ == "__main__":
    main()
