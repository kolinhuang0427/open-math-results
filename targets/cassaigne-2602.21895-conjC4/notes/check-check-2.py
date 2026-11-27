#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/cassaigne-2602.21895-conjC4/.

Verifies strictly from arXiv:2602.21895v1 (merge_version.tex) and PROOF.md:
  1. Prefix of t_{3/2} and t' = phi(t_{3/2}) matches paper verbatim.
  2. Lemma 1 (preimage lengths) for 2 <= L <= 50.
  3. Lemma 2 (exact desubstitution counting recurrence C_n(w,k,N) with |E|<=3L+3)
     for 2 <= L <= 5, n in {0,1,2}, N in {50, 200, 1000, 10000}.
  4. Exact rational f(w) via Fraction for all 1 <= |w| <= 9 (fixed-point eq,
     total sum == 1, prefix/suffix compatibility, reversal & complement invariance,
     Proposition 2 commutation psi_{r'}(w^R) == (psi_r(w))^R).
  5. Exact rational freq_{t'}(w) for all 1 <= |w| <= 7 (incl. L=2 exact 1/10, 2/5,
     total sum == 1, reversal & complement invariance), plus empirical check against
     t_{3/2}[0..100000) and t'[0..300000) (integer/Fraction comparison only).
"""

from __future__ import annotations

import functools
import signal
import sys
import time
from collections import Counter
from fractions import Fraction


def _alarm_handler(signum: int, frame: object) -> None:
    raise TimeoutError("Verification script exceeded 60s timeout")


# ---------------------------------------------------------------------------
# Sequence generation from eq:t32relations and lem:morphic_image
# ---------------------------------------------------------------------------

def gen_t32(length: int) -> list[int]:
    t = [0] * length
    t[0] = 0
    for n in range((length + 2) // 3):
        if 3 * n < length:
            t[3 * n] = t[2 * n]
        if 3 * n + 1 < length:
            t[3 * n + 1] = t[2 * n]
        if 3 * n + 2 < length:
            t[3 * n + 2] = 1 - t[2 * n + 1]
    return t


def gen_tprime(t32: list[int]) -> list[int]:
    out = [0] * (3 * len(t32))
    for i, b in enumerate(t32):
        if b == 0:
            out[3 * i] = 0
            out[3 * i + 1] = 1
            out[3 * i + 2] = 0
        else:
            out[3 * i] = 1
            out[3 * i + 1] = 0
            out[3 * i + 2] = 1
    return out


# ---------------------------------------------------------------------------
# Desubstitution maps S, eps, psi_r
# ---------------------------------------------------------------------------

def s_map(m: int) -> int:
    q, r = divmod(m, 3)
    return 2 * q if r < 2 else 2 * q + 1


def eps_map(m: int) -> int:
    return 1 if (m % 3 == 2) else 0


def psi_r(r: int, w: tuple[int, ...]) -> tuple[int, ...] | None:
    l_len = len(w)
    assert l_len >= 2 and r in (0, 1, 2)
    a_r = s_map(r)
    b_r = s_map(r + l_len - 1)
    u: dict[int, int] = {}
    for i in range(l_len):
        idx = s_map(r + i) - a_r
        val = w[i] ^ eps_map(r + i)
        if idx in u and u[idx] != val:
            return None
        u[idx] = val
    out_len = b_r - a_r + 1
    return tuple(u[j] for j in range(out_len))


def rev_word(w: tuple[int, ...]) -> tuple[int, ...]:
    return w[::-1]


def comp_word(w: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 - x for x in w)


# ---------------------------------------------------------------------------
# Exact rational frequencies f(w) and freq_{t'}(w)
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def f_exact(w: tuple[int, ...]) -> Fraction:
    l_len = len(w)
    if l_len == 1:
        return Fraction(1, 2)
    if l_len == 2:
        return Fraction(3, 10) if w[0] == w[1] else Fraction(1, 5)
    if l_len == 3:
        a, b, c = w
        wp = (a, 1 - b, c)
        def g(u: tuple[int, int, int]) -> Fraction:
            ua, ub, uc = u
            tot = Fraction(0)
            if ua == ub:
                tot += f_exact((ua, 1 - uc))
            if ub == uc:
                tot += f_exact((1 - ua, ub))
            return tot / 3
        return Fraction(9, 8) * (g(w) + Fraction(1, 3) * g(wp))
    tot = Fraction(0)
    for r in (0, 1, 2):
        pr = psi_r(r, w)
        if pr is not None:
            tot += f_exact(pr)
    return tot / 3


def freq_tprime_exact(w: tuple[int, ...]) -> Fraction:
    l_len = len(w)
    assert l_len >= 1
    tot = Fraction(0)
    phi = {0: (0, 1, 0), 1: (1, 0, 1)}
    for r in (0, 1, 2):
        mr = (r + l_len + 2) // 3
        # Enumerate all u in {0,1}^{mr} whose phi(u)[r:r+L] == w
        # Note each block of 3 in w forces at most 1 choice of bit in u, so we can just check directly
        # in O(mr) instead of 2^{mr}:
        # Determine required bit for each block idx b_idx in 0..mr-1
        u_req: list[int | None] = [None] * mr
        ok = True
        for i, wbit in enumerate(w):
            pos = r + i
            b_idx, offset = divmod(pos, 3)
            # phi(bit)[offset] == bit ^ (1 if offset == 1 else 0)
            needed_bit = wbit ^ (1 if offset == 1 else 0)
            if u_req[b_idx] is not None and u_req[b_idx] != needed_bit:
                ok = False
                break
            u_req[b_idx] = needed_bit
        if not ok:
            continue
        free_positions = [idx for idx, val in enumerate(u_req) if val is None]
        for mask in range(1 << len(free_positions)):
            u = list(u_req)
            for k_idx, pos in enumerate(free_positions):
                u[pos] = (mask >> k_idx) & 1
            ut = tuple(u)  # type: ignore[arg-type]
            # Verify phi(ut)[r:r+L] == w explicitly
            img = sum((phi[b] for b in ut), ())
            assert img[r:r + l_len] == w
            tot += f_exact(ut)
    return tot / 3


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def all_words(length: int) -> list[tuple[int, ...]]:
    return [tuple((mask >> (length - 1 - i)) & 1 for i in range(length)) for mask in range(1 << length)]


def verify_lemma1() -> None:
    for L in range(2, 51):
        l0 = s_map(L - 1) - s_map(0) + 1
        l1 = s_map(L) - s_map(1) + 1
        l2 = s_map(L + 1) - s_map(2) + 1
        assert l0 < L
        if L == 2:
            assert (l0, l1, l2) == (1, 2, 2)
        elif L == 3:
            assert (l0, l1, l2) == (2, 3, 2)
        else:
            assert l1 < L and l2 < L


def verify_lemma2(t32: list[int]) -> None:
    for N in (50, 200, 1000, 10000):
        n23 = (2 * N) // 3
        for n in (0, 1, 2):
            mod_n = 1 << n
            mod_n1 = 1 << (n + 1)
            qn = pow(3, -1, mod_n1)
            for L in (2, 3, 4, 5):
                # Count C_n(w, k, N) and C_{n+1}(u, k', n23) in one linear pass!
                cn_counts: dict[tuple[tuple[int, ...], int], int] = {}
                cn1_counts: dict[tuple[tuple[int, ...], int], int] = {}
                for m in range(N):
                    w = tuple(t32[m:m + L])
                    key = (w, m % mod_n)
                    cn_counts[key] = cn_counts.get(key, 0) + 1
                # Also precompute C_{n+1} for lengths in {l_0, l_1, l_2}
                lens_needed = {s_map(r + L - 1) - s_map(r) + 1 for r in (0, 1, 2)}
                for len_u in lens_needed:
                    for m in range(n23):
                        u = tuple(t32[m:m + len_u])
                        key = (u, m % mod_n1)
                        cn1_counts[key] = cn1_counts.get(key, 0) + 1

                for k in range(mod_n):
                    k0 = (2 * qn * k) % mod_n1
                    k1 = (2 * qn * k - 2 * qn) % mod_n1
                    k2 = (2 * qn * k - qn) % mod_n1
                    kr_list = (k0, k1, k2)
                    for w in all_words(L):
                        lhs = cn_counts.get((w, k), 0)
                        rhs = 0
                        for r in (0, 1, 2):
                            pr = psi_r(r, w)
                            if pr is not None:
                                rhs += cn1_counts.get((pr, kr_list[r]), 0)
                        err = abs(lhs - rhs)
                        assert err <= 3 * L + 3, f"Lemma 2 error {err} > {3*L+3}"


def verify_exact_frequencies_and_symmetries() -> None:
    # Check 1 <= L <= 9 for t_{3/2}
    prev_words_freqs: dict[tuple[int, ...], Fraction] = {}
    for L in range(1, 10):
        words = all_words(L)
        cur = {w: f_exact(w) for w in words}
        assert sum(cur.values()) == Fraction(1), f"Sum != 1 at L={L}"
        for w, fw in cur.items():
            assert Fraction(0) <= fw <= Fraction(1)
            assert cur[rev_word(w)] == fw, f"Reversal failed at {w}"
            assert cur[comp_word(w)] == fw, f"Complement failed at {w}"
            if L >= 2:
                # Fixed-point identity for all L >= 2
                fp = sum((f_exact(psi_r(r, w)) for r in (0, 1, 2) if psi_r(r, w) is not None), Fraction(0)) / 3
                assert fp == fw, f"Fixed point failed at {w}"
                # Proposition 2 commutation: psi_{r'}(w^R) == (psi_r(w))^R
                wr = rev_word(w)
                for r in (0, 1, 2):
                    rp = (2 - r - L) % 3
                    pr = psi_r(r, w)
                    prp = psi_r(rp, wr)
                    if pr is None:
                        assert prp is None
                    else:
                        assert prp == rev_word(pr)
        if L >= 2:
            # Prefix and suffix marginals
            for u, fu in prev_words_freqs.items():
                assert cur[u + (0,)] + cur[u + (1,)] == fu
                assert cur[(0,) + u] + cur[(1,) + u] == fu
        prev_words_freqs = cur

    # Check exact L=2 values
    assert f_exact((0, 0)) == Fraction(3, 10)
    assert f_exact((1, 1)) == Fraction(3, 10)
    assert f_exact((0, 1)) == Fraction(1, 5)
    assert f_exact((1, 0)) == Fraction(1, 5)

    # Check 1 <= L <= 7 for t'
    for L in range(1, 8):
        words = all_words(L)
        cur_tp = {w: freq_tprime_exact(w) for w in words}
        assert sum(cur_tp.values()) == Fraction(1), f"t' sum != 1 at L={L}"
        for w, fw in cur_tp.items():
            assert Fraction(0) <= fw <= Fraction(1)
            assert cur_tp[rev_word(w)] == fw, f"t' reversal failed at {w}"
            assert cur_tp[comp_word(w)] == fw, f"t' complement failed at {w}"
    assert freq_tprime_exact((0, 0)) == Fraction(1, 10)
    assert freq_tprime_exact((1, 1)) == Fraction(1, 10)
    assert freq_tprime_exact((0, 1)) == Fraction(2, 5)
    assert freq_tprime_exact((1, 0)) == Fraction(2, 5)


def verify_empirical(t32: list[int], tp: list[int]) -> None:
    n_emp = 100000
    for L in range(1, 6):
        cnt = Counter(tuple(t32[i:i + L]) for i in range(n_emp))
        for w in all_words(L):
            emp = Fraction(cnt[w], n_emp)
            diff = abs(emp - f_exact(w))
            assert diff < Fraction(1, 200), f"Empirical t_{{3/2}} diff {diff} at {w}"
    # Filtered nu_n(w, k, N) check for n=1,2, L=3
    for n in (1, 2):
        mod_n = 1 << n
        for k in range(mod_n):
            cnt = Counter(tuple(t32[i:i + 3]) for i in range(k, n_emp, mod_n))
            for w in all_words(3):
                nu = Fraction(mod_n * cnt[w], n_emp)
                assert abs(nu - f_exact(w)) < Fraction(1, 100)
    # Empirical check on t'[0..300000)
    n_tp = 300000
    for L in range(1, 6):
        cnt = Counter(tuple(tp[i:i + L]) for i in range(n_tp))
        for w in all_words(L):
            emp = Fraction(cnt[w], n_tp)
            assert abs(emp - freq_tprime_exact(w)) < Fraction(1, 200)


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(60)
    t0 = time.monotonic()

    t32 = gen_t32(100020)
    tp = gen_tprime(t32)
    # Verify verbatim prefixes from merge_version.tex lines 401 and 438
    assert "".join(map(str, t32[:17])) == "00111011111011011"
    assert "".join(map(str, tp[:25])) == "0100101011011010101011011"
    print("Primary-source prefixes (t_{3/2} len 17, t' len 25) match merge_version.tex verbatim: PASS")

    verify_lemma1()
    print("Lemma 1 (preimage lengths l_0, l_1, l_2 for 2 <= L <= 50): PASS")

    verify_lemma2(t32)
    print("Lemma 2 (exact desubstitution recurrence C_n(w,k,N), |E|<=3L+3 for 2<=L<=5, N<=10000): PASS")

    verify_exact_frequencies_and_symmetries()
    print("Exact Fraction frequencies & rev/comp symmetries (t_{3/2} 1<=L<=9, t' 1<=L<=7; L=2 values): PASS")

    verify_empirical(t32, tp)
    print("Empirical density agreement on t_{3/2}[0..100000) and t'[0..300000) (L<=5, filtered n<=2): PASS")

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
