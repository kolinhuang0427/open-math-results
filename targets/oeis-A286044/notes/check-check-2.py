#!/usr/bin/env python3
"""Independent exact verifier for targets/oeis-A286044/
(OEIS A286044: Velin Yanev Feb 16 2026 conjecture a(n) = b(b(n-2)) - b(b(n-3)) for n > 3).

Strictly derived from live OEIS definitions (A286044 rev 8, A010060 rev 619,
A003160 rev 61, A003159 rev 238) and verifies all intermediate claims of PROOF.md
using exact integer arithmetic.
"""

from __future__ import annotations

import signal
import time


def timeout_handler(signum, frame):
    raise TimeoutError("Verification exceeded 60s alarm")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(60)


OEIS_A286044_PREFIX = [
    0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,
    0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,
    0,0,1,0,0,0,
]

OEIS_A003160_PREFIX = [
    1,1,1,2,3,4,4,4,5,5,5,6,6,6,7,8,9,9,9,10,11,12,12,12,13,14,15,15,15,16,16,16,17,
    17,17,18,19,20,20,20,21,21,21,22,22,22,23,
]


def thue_morse(k: int) -> int:
    return k.bit_count() & 1


def v2(k: int) -> int:
    assert k >= 1
    return (k & -k).bit_length() - 1


def run_checks(N_LIMIT: int = 120_000) -> None:
    t0 = time.monotonic()

    # 1. Build Thue-Morse A010060 and apply literal {011 -> 0} left-to-right transform
    # To guarantee at least N_LIMIT terms of A286044 and cover MAX_INT, build > 2 * N_LIMIT + 250 bits of A010060.
    MAX_INT = 2 * N_LIMIT + 200
    M_TM = MAX_INT + 10
    t = [thue_morse(k) for k in range(M_TM)]
    a_seq = [0]  # 1-indexed dummy
    i = 0
    while i + 2 < M_TM:
        if t[i] == 0 and t[i + 1] == 1 and t[i + 2] == 1:
            assert i % 2 == 0, f"Expected 011 only at even index, found at {i}"
            if i + 3 < M_TM:
                assert t[i + 3] == 0, f"Expected t[{i+3}] == 0 after 011"
            a_seq.append(0)
            i += 3
        else:
            a_seq.append(t[i])
            i += 1
    assert len(a_seq) - 1 >= N_LIMIT
    assert a_seq[1 : 1 + len(OEIS_A286044_PREFIX)] == OEIS_A286044_PREFIX
    print(f"[OEIS A286044 prefix + literal 011->0] PASS ({len(OEIS_A286044_PREFIX)} OEIS terms, computed {len(a_seq)-1} terms)")

    # 2. Build V = A003159 (1-indexed) and V_bar directly from v2 parity
    # Need v(N_LIMIT + 2) so build V up to at least 2 * N_LIMIT + 200
    v_seq = [0]  # 1-indexed: v_seq[n] = v(n)
    vbar_seq = [0]
    pi_V = [0] * (MAX_INT + 1)
    pi_Vbar = [0] * (MAX_INT + 1)
    for k in range(1, MAX_INT + 1):
        if (v2(k) & 1) == 0:
            v_seq.append(k)
            pi_V[k] = pi_V[k - 1] + 1
            pi_Vbar[k] = pi_Vbar[k - 1]
        else:
            vbar_seq.append(k)
            pi_V[k] = pi_V[k - 1]
            pi_Vbar[k] = pi_Vbar[k - 1] + 1
    assert len(v_seq) - 1 >= N_LIMIT + 10

    # Fact 1 & Fact 2 checks
    for idx in range(1, len(vbar_seq)):
        assert vbar_seq[idx] == 2 * v_seq[idx], f"Fact 1 failed at idx={idx}"
    for N in range(0, MAX_INT + 1):
        assert pi_Vbar[N] == pi_V[N // 2]
        assert pi_V[N] + pi_V[N // 2] == N
    for j in range(0, MAX_INT):
        diff = 1 if (t[j + 1] != t[j]) else 0 if j + 1 < M_TM else None
        if diff is not None:
            in_V = 1 if ((v2(j + 1) & 1) == 0) else 0
            assert diff == in_V, f"Fact 2 failed at j={j}"
    print(f"[Section 1 Fact 1 & Fact 2] PASS up to {MAX_INT}")

    # 3. Section 2 checks: positions of 1s in A286044 and even elements of V
    m = 0
    for n in range(1, N_LIMIT + 1):
        v_even = 1 if (v_seq[n] % 2 == 0) else 0
        assert a_seq[n] == v_even, f"Sec 2 indicator failed at n={n}: a={a_seq[n]}, v({n})={v_seq[n]}"
        if a_seq[n] == 1:
            m += 1
            assert n == 2 * v_seq[m] + m, f"m-th 1 position failed at m={m}: n={n}"
            assert v_seq[n] == 4 * v_seq[m], f"m-th even element of V failed at m={m}"
    print(f"[Section 2 indicator & 2v(m)+m positions] PASS for 1<=n<={N_LIMIT} ({m} surviving 1s)")

    # 4. Build A003160 b(n) directly from defining recurrence and verify Section 3 closed form
    b_seq = [0] * (N_LIMIT + 5)
    b_seq[1] = 1
    b_seq[2] = 1
    for n in range(3, N_LIMIT + 5):
        b_seq[n] = n - b_seq[b_seq[n - 1]] - b_seq[b_seq[n - 2]]
    assert b_seq[1 : 1 + len(OEIS_A003160_PREFIX)] == OEIS_A003160_PREFIX

    for n in range(1, N_LIMIT + 5):
        g_n = v_seq[n + 1] - (n + 1)
        assert b_seq[n] == g_n, f"Section 3 closed form failed at n={n}: b={b_seq[n]}, g={g_n}"
        assert g_n == pi_Vbar[v_seq[n + 1]]
        if n >= 2:
            assert b_seq[n] - b_seq[n - 1] in (0, 1)

    # Check level sets I_y = [y + 2*b(y-1), y + 2*b(y)] (with b(0)=0)
    max_y = b_seq[N_LIMIT]
    for y in range(1, max_y):
        lo = y + 2 * b_seq[y - 1]
        hi = y + 2 * b_seq[y]
        assert hi - lo + 1 in (1, 3)
        for n in range(lo, hi + 1):
            assert b_seq[n] == y, f"Level set I_{y} failed at n={n}"
        if lo > 1:
            assert b_seq[lo - 1] == y - 1
        assert b_seq[hi + 1] == y + 1
    print(f"[Section 3 A003160 recurrence, prefix, closed form & I_y blocks] PASS for 1<=n<={N_LIMIT+4}")

    # 5. Main Theorem & Section 4 double-difference check for ALL 4 <= n <= N_LIMIT
    for n in range(4, N_LIMIT + 1):
        rhs = b_seq[b_seq[n - 2]] - b_seq[b_seq[n - 3]]
        assert rhs == a_seq[n], f"Yanev conjecture FAILS at n={n}: a={a_seq[n]}, rhs={rhs}"
        assert rhs == (1 if v_seq[n] % 2 == 0 else 0)

    dt = time.monotonic() - t0
    print(f"[Main Theorem: a(n) = b(b(n-2)) - b(b(n-3))] PASS for ALL 4<=n<={N_LIMIT}")
    print(f"PASS (all independent checks passed in {dt:.3f}s)")


if __name__ == "__main__":
    run_checks(120_000)
