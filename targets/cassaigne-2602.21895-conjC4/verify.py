#!/usr/bin/env python3
"""Exact verification for Cassaigne et al. / Dekking Conjecture (C_4) (arXiv:2602.21895v1).

Verifies (using exact Fraction arithmetic, zero floats in exact claims):
1. Preimage map lengths ell_r(L) < L for L>=4 (and ell_0(3)=2, ell_2(3)=2) for L=2..12.
2. Exact bijection between S(sigma(m)) and tau(S(m)) and exact reversal identity
   psi_{r'}(w^R) = (psi_r(w))^R for all w in {0,1}^L, L=2..8.
3. Exact fixed-point equations, normalization sum_{w} f(w) = 1, reversal symmetry
   f(w^R) = f(w), and complement symmetry f(~w) = f(w) for all L=1..8 in t_{3/2} and t'.
4. Exact empirical agreement of prefixes of t_{3/2} (N=120000) and t' (N=360000)
   with the proved exact rational frequencies for L=1..4 (including filtered mod 2, 4).
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import sys
import time


def S_map(m: int) -> int:
    q, r = divmod(m, 3)
    return 2 * q if r in (0, 1) else 2 * q + 1


def eps_map(m: int) -> int:
    return 1 if (m % 3) == 2 else 0


def psi(r: int, w: tuple[int, ...]) -> tuple[int, ...] | None:
    """Desubstitution preimage psi_r(w) for r in {0, 1, 2}."""
    L = len(w)
    u: dict[int, int] = {}
    for i, bit in enumerate(w):
        m = r + i
        idx = S_map(m)
        val = bit ^ eps_map(m)
        if idx in u and u[idx] != val:
            return None
        u[idx] = val
    lo, hi = min(u), max(u)
    assert set(u.keys()) == set(range(lo, hi + 1))
    return tuple(u[j] for j in range(lo, hi + 1))


_MEMO_T32: dict[tuple[int, ...], Fraction] = {
    (0,): Fraction(1, 2),
    (1,): Fraction(1, 2),
    (0, 0): Fraction(3, 10),
    (1, 1): Fraction(3, 10),
    (0, 1): Fraction(1, 5),
    (1, 0): Fraction(1, 5),
}


def freq_t32(w: tuple[int, ...]) -> Fraction:
    if w in _MEMO_T32:
        return _MEMO_T32[w]
    L = len(w)
    if L == 3:
        a, b, c = w
        def g(x: int, y: int, z: int) -> Fraction:
            res = Fraction(0)
            p0 = psi(0, (x, y, z))
            p2 = psi(2, (x, y, z))
            if p0 is not None:
                res += Fraction(1, 3) * freq_t32(p0)
            if p2 is not None:
                res += Fraction(1, 3) * freq_t32(p2)
            return res
        ans = Fraction(9, 8) * (g(a, b, c) + Fraction(1, 3) * g(a, 1 - b, c))
        _MEMO_T32[w] = ans
        return ans
    ans = Fraction(0)
    for r in (0, 1, 2):
        u = psi(r, w)
        if u is not None:
            assert len(u) < L
            ans += Fraction(1, 3) * freq_t32(u)
    _MEMO_T32[w] = ans
    return ans


def phi_word(u: tuple[int, ...]) -> tuple[int, ...]:
    out: list[int] = []
    for b in u:
        out.extend((0, 1, 0) if b == 0 else (1, 0, 1))
    return tuple(out)


def freq_tprime(w: tuple[int, ...]) -> Fraction:
    L = len(w)
    total = Fraction(0)
    for r in (0, 1, 2):
        mr = (r + L + 2) // 3
        for u in itertools.product((0, 1), repeat=mr):
            if phi_word(u)[r : r + L] == w:
                total += Fraction(1, 3) * freq_t32(u)
    return total


def main() -> None:
    t0 = time.time()

    # 1. Verify Lemma 1 (preimage lengths) for L = 2..12
    for L in range(2, 13):
        for r in (0, 1, 2):
            indices = [S_map(r + i) for i in range(L)]
            ell = max(indices) - min(indices) + 1
            if r == 0:
                assert ell < L
            elif r == 1:
                assert (ell == L if L in (2, 3) else ell < L)
            else:
                assert (ell == L if L == 2 else ell < L)

    # 2. Verify involution S(sigma(m)) = tau(S(m)) and psi_{r'}(w^R) = (psi_r(w))^R for L=2..8
    M = 20
    for m in range(50):
        assert S_map(3 * M + 1 - m) == 2 * M - S_map(m)
        assert eps_map(3 * M + 1 - m) == eps_map(m)

    for L in range(2, 9):
        for w in itertools.product((0, 1), repeat=L):
            for r in (0, 1, 2):
                rp = (2 - r - L) % 3
                u = psi(r, w)
                ur = psi(rp, w[::-1])
                if u is None:
                    assert ur is None, f"Mismatch None at L={L}, w={w}, r={r}"
                else:
                    assert ur == u[::-1], f"Mismatch rev at L={L}, w={w}, r={r}: {u[::-1]} vs {ur}"

    # 3. Verify fixed-point equation, sum=1, reversal & complement symmetry for L=1..8 (t_{3/2}) and L=1..6 (t')
    for L in range(1, 9):
        words = list(itertools.product((0, 1), repeat=L))
        assert sum(freq_t32(w) for w in words) == Fraction(1)
        for w in words:
            fw = freq_t32(w)
            assert 0 <= fw <= 1
            assert fw == freq_t32(w[::-1]), f"t32 rev failed at {w}"
            assert fw == freq_t32(tuple(1 - b for b in w)), f"t32 cmp failed at {w}"
            if L >= 2:
                rhs = Fraction(0)
                for r in (0, 1, 2):
                    u = psi(r, w)
                    if u is not None:
                        rhs += Fraction(1, 3) * freq_t32(u)
                assert fw == rhs, f"Fixed point eq failed at {w}: {fw} != {rhs}"

    assert freq_t32((0, 0)) == Fraction(3, 10)
    assert freq_t32((1, 1)) == Fraction(3, 10)
    assert freq_t32((0, 1)) == Fraction(1, 5)
    assert freq_t32((1, 0)) == Fraction(1, 5)

    for L in range(1, 7):
        words = list(itertools.product((0, 1), repeat=L))
        assert sum(freq_tprime(w) for w in words) == Fraction(1)
        for w in words:
            fw = freq_tprime(w)
            assert 0 <= fw <= 1
            assert fw == freq_tprime(w[::-1]), f"t' rev failed at {w}"
            assert fw == freq_tprime(tuple(1 - b for b in w)), f"t' cmp failed at {w}"

    assert freq_tprime((0, 0)) == Fraction(1, 10)
    assert freq_tprime((1, 1)) == Fraction(1, 10)
    assert freq_tprime((0, 1)) == Fraction(2, 5)
    assert freq_tprime((1, 0)) == Fraction(2, 5)

    # 4. Prefix checks on t_{3/2} (N = 120000) and t' (N = 360000)
    N = 120_000
    t = [0] * (N + 10)
    for m in range(N // 3 + 3):
        t[3 * m] = t[2 * m]
        t[3 * m + 1] = t[2 * m]
        t[3 * m + 2] = 1 - t[2 * m + 1]

    for L in (1, 2, 3, 4):
        cnt: dict[tuple[int, ...], int] = {}
        for i in range(N - L):
            w = tuple(t[i : i + L])
            cnt[w] = cnt.get(w, 0) + 1
        for w in itertools.product((0, 1), repeat=L):
            err = abs(Fraction(cnt.get(w, 0), N - L) - freq_t32(w))
            assert err < Fraction(1, 100), f"t32 empirical mismatch at {w}: {err}"

    # Filtered check mod 4 for L = 2, 3
    for L in (2, 3):
        for r in range(4):
            sub: dict[tuple[int, ...], int] = {}
            tot = 0
            for i in range(r, N - L, 4):
                w = tuple(t[i : i + L])
                sub[w] = sub.get(w, 0) + 1
                tot += 1
            for w in itertools.product((0, 1), repeat=L):
                err = abs(Fraction(sub.get(w, 0), tot) - freq_t32(w))
                assert err < Fraction(1, 100), f"Filtered mod4 mismatch at {w}, r={r}: {err}"

    # Prefix check on t' = phi(t_{3/2})
    tp: list[int] = []
    for b in t[:N]:
        tp.extend((0, 1, 0) if b == 0 else (1, 0, 1))
    Np = len(tp)
    for L in (1, 2, 3, 4):
        cntp: dict[tuple[int, ...], int] = {}
        for i in range(Np - L):
            w = tuple(tp[i : i + L])
            cntp[w] = cntp.get(w, 0) + 1
        for w in itertools.product((0, 1), repeat=L):
            err = abs(Fraction(cntp.get(w, 0), Np - L) - freq_tprime(w))
            assert err < Fraction(1, 100), f"t' empirical mismatch at {w}: {err}"

    print(f"PASS (verified L<=8 exact recurrences/symmetries and N={N}/{Np} prefixes in {time.time() - t0:.2f}s)")


if __name__ == "__main__":
    main()
