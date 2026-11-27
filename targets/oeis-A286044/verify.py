import signal

signal.alarm(30)


def thue_morse(n_terms: int) -> list[int]:
    return [k.bit_count() & 1 for k in range(n_terms)]


def a286044_from_tm(tm: list[int]) -> list[int]:
    # Replace every 011 by 0 in the infinite Thue-Morse prefix (drop trailing partial 011)
    s = "".join(map(str, tm))
    # Stop cleanly before the last 3 chars so prefix truncation never alters a boundary 011
    stable_prefix = s[:-3].replace("011", "0")
    return [int(c) for c in stable_prefix]


def main() -> None:
    N_TM = 200000
    tm = thue_morse(N_TM)
    a = a286044_from_tm(tm)
    M = len(a)

    # Check OEIS A286044 published initial terms (offset 1)
    expected_prefix = [
        0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,
        1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,
        0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,
    ]
    assert a[:len(expected_prefix)] == expected_prefix, "Initial A286044 mismatch"

    # Compute A003159 (vile numbers: even 2-adic valuation)
    v = [0]  # 1-indexed: v[1] = 1
    k = 1
    while len(v) <= M + 10:
        if ((k & -k).bit_length() - 1) % 2 == 0:
            v.append(k)
        k += 1

    # Verify Section 2: a[n-1] == 1 iff v[n] is even (1 <= n <= M)
    even_v_pos = [2 * v[m] + m for m in range(1, len(v)) if 2 * v[m] + m <= M]
    actual_ones = [n for n, val in enumerate(a, start=1) if val == 1]
    assert actual_ones == even_v_pos, "Position of 1s mismatch with 2*v(m)+m"
    for n in range(1, M + 1):
        assert a[n - 1] == (1 if v[n] % 2 == 0 else 0), f"A286044 vs even v(n) mismatch at n={n}"

    # Compute A003160 b(n) directly from recurrence b(1)=b(2)=1, b(n)=n-b(b(n-1))-b(b(n-2))
    b = [0] * (M + 1)
    b[1] = 1
    b[2] = 1
    for n in range(3, M + 1):
        b[n] = n - b[b[n - 1]] - b[b[n - 2]]

    # Verify Section 3: b[n] == v[n+1] - (n+1) for 1 <= n <= M
    for n in range(1, M + 1):
        assert b[n] == v[n + 1] - (n + 1), f"A003160 closed form mismatch at n={n}"

    # Verify target conjecture: a(n) == b(b(n-2)) - b(b(n-3)) for 4 <= n <= M
    for n in range(4, M + 1):
        rhs = b[b[n - 2]] - b[b[n - 3]]
        assert a[n - 1] == rhs, f"Conjecture mismatch at n={n}"

    print(
        f"PASS: verified A286044 = {{011->0}}(TM) and Yanev identity "
        f"a(n) = b(b(n-2)) - b(b(n-3)) for all 4 <= n <= {M}."
    )


if __name__ == "__main__":
    main()
