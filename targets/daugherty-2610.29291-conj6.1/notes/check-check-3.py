"""Independent exact-arithmetic verifier for targets/daugherty-2610.29291-conj6.1/."""

import itertools
import signal

signal.alarm(50)


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r >= c) for c in range(1, lam[0] + 1))


def dominates(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    """True iff partial sums of a >= partial sums of b (padded with 0s) and |a| == |b|."""
    if sum(a) != sum(b):
        return False
    m = max(len(a), len(b))
    sa = sb = 0
    for i in range(m):
        sa += a[i] if i < len(a) else 0
        sb += b[i] if i < len(b) else 0
        if sa < sb:
            return False
    return True


def is_wide_all_subpartitions(lam: tuple[int, ...]) -> bool:
    """Check Definition 2.2 directly: every subpartition (deleting any subset of rows) dominates its conjugate."""
    ell = len(lam)
    for mask in range(1, 1 << ell):
        sub = tuple(lam[i] for i in range(ell) if (mask >> i) & 1)
        if not dominates(sub, conjugate(sub)):
            return False
    return True


def count_latin_tableaux(lam: tuple[int, ...]) -> int:
    """Exact count LT(lam) of Latin tableaux of shape lam and type lam' directly from Definition 2.5."""
    ell = len(lam)
    width = lam[0]
    conj = conjugate(lam)
    # Build valid fillings row by row; each cell (r, c) gets val in 1..width.
    # Also verify directly that type == conj and no repeats in row or column.
    col_used = [0] * width
    row_used = [0] * ell
    rem_counts = [0] + list(conj)

    # Order cells by row (top to bottom) then col (left to right),
    # or pre-check per-row possibilities? Cell-by-cell with row/col/type bitmasks is simple and exact,
    # Wait: for row 0 (length 6) -> 6! = 720, then row 1 -> quickly pruned if we assign row by row.
    # Better: assign cell-by-cell in column-first or row-first order?
    # Note: in any Latin tableau of shape lam and type lam', row r MUST use {1..lam[r]}
    # (forced by type counts from largest symbol downward), AND let's NOT assume that shortcut—
    # instead, track rem_counts[sym] and allow any sym in 1..width not yet in row r or col c,
    # pruning only when rem_counts[sym] > number of remaining cells in rows not yet containing sym!
    cells = [(r, c) for r in range(ell) for c in range(lam[r])]
    total_cells = len(cells)

    # Precompute for each cell index: remaining occurrences of row r after this cell
    # Wait: simple row-by-row backtracking over valid row permutations using only symbols with rem_counts > 0
    # Wait: let's prove/verify during search whether row r ever uses symbol > lam[r]:
    # We don't even restrict row r to 1..lam[r]; we restrict only by type=lam', no row repeats, no col repeats!
    # Wait: if row 0 has len 6 and 6 symbols, any permutation of remaining counts uses 1..6.
    # Let's do cell-by-cell with suffix max-row-count pruning so it is 100% faithful to Def 2.5 without assumptions!
    rem_rows_after = [[0] * ell for _ in range(total_cells + 1)]
    for idx in range(total_cells - 1, -1, -1):
        r, _ = cells[idx]
        rem_rows_after[idx] = rem_rows_after[idx + 1][:]
        rem_rows_after[idx][r] += 1

    # Better yet: assign row by row, generating valid completions of row r from available symbols
    memo: dict[tuple[int, tuple[int, ...], tuple[int, ...]], int] = {}

    def backtrack_row(r: int) -> int:
        if r == ell:
            return 1
        row_len = lam[r]
        rem_row_slots = ell - r
        for s in range(1, width + 1):
            if rem_counts[s] > rem_row_slots:
                return 0
        key = (r, tuple(col_used[:row_len]), tuple(rem_counts))
        if key in memo:
            return memo[key]

        def fill_cell(c: int, used_row_mask: int) -> int:
            if c == row_len:
                return backtrack_row(r + 1)
            ans = 0
            c_mask = col_used[c]
            for s in range(1, width + 1):
                bit = 1 << s
                if rem_counts[s] > 0 and not (used_row_mask & bit) and not (c_mask & bit):
                    rem_counts[s] -= 1
                    col_used[c] |= bit
                    ans += fill_cell(c + 1, used_row_mask | bit)
                    col_used[c] ^= bit
                    rem_counts[s] += 1
            return ans

        res = fill_cell(0, 0)
        memo[key] = res
        return res

    return backtrack_row(0)


def check_pair(mu: tuple[int, ...], lam: tuple[int, ...], exp_i: int, exp_lt_mu: int, exp_lt_lam: int) -> None:
    assert len(mu) == len(lam)
    diffs = [idx for idx in range(len(lam)) if lam[idx] != mu[idx]]
    assert diffs == [exp_i - 1], f"Expected diff at row {exp_i}, got {diffs}"
    assert lam[exp_i - 1] == mu[exp_i - 1] + 1
    assert 1 <= exp_i <= len(lam) - 1
    assert is_wide_all_subpartitions(mu), f"{mu} is not wide"
    assert is_wide_all_subpartitions(lam), f"{lam} is not wide"
    lt_mu = count_latin_tableaux(mu)
    lt_lam = count_latin_tableaux(lam)
    assert lt_mu == exp_lt_mu, f"LT({mu})={lt_mu} != {exp_lt_mu}"
    assert lt_lam == exp_lt_lam, f"LT({lam})={lt_lam} != {exp_lt_lam}"
    assert lt_lam < lt_mu, f"Expected LT({lam}) < LT({mu})"
    print(f"Pair PASS: mu={mu} (wide, LT={lt_mu}) -> lam={lam} (wide, LT={lt_lam}) at i={exp_i}")


def main() -> None:
    # Paper's Example (Definition 2.5 -> Example): LT((3, 2)) == 6
    assert count_latin_tableaux((3, 2)) == 6
    # Paper's Section 5 counterexamples for bottom/top row addition:
    assert count_latin_tableaux((4, 4, 2, 1)) == 12
    assert count_latin_tableaux((4, 4, 2, 2)) == 8
    assert count_latin_tableaux((3, 2)) == 6 and count_latin_tableaux((3, 3, 2)) == 4
    assert count_latin_tableaux((4, 4, 3, 1)) == 40 and count_latin_tableaux((5, 4, 4, 3, 1)) == 32
    print("Sanity checks PASS: paper's examples (3,2), (4,4,2,1)->(4,4,2,2), (3,3,2), (4,4,3,1)->(5,4,4,3,1) match.")

    # Main counterexample + additional pairs in COUNTEREXAMPLE.md
    check_pair((6, 5, 5, 3, 2, 1), (6, 5, 5, 3, 3, 1), 5, 56, 32)
    check_pair((6, 6, 4, 3, 2, 1), (6, 6, 4, 3, 3, 1), 5, 88, 64)
    check_pair((6, 6, 5, 3, 2, 1), (6, 6, 5, 3, 3, 1), 5, 2080, 1984)
    print("PASS")


if __name__ == "__main__":
    main()
