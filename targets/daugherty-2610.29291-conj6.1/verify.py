#!/usr/bin/env python3
"""Independent exact verifier for counterexample to Daugherty et al. (2026) Conjecture 6.1."""

import itertools


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x >= i) for i in range(1, lam[0] + 1))


def dominates(a, b):
    L = max(len(a), len(b))
    sa = sb = 0
    for i in range(L):
        sa += a[i] if i < len(a) else 0
        sb += b[i] if i < len(b) else 0
        if sa < sb:
            return False
    return True


def is_wide_all_subpartitions(lam):
    """Check Definition 2.2 literally: every subpartition (deleting any subset of rows) dominates its conjugate."""
    L = len(lam)
    for r in range(1, L + 1):
        for idxs in itertools.combinations(range(L), r):
            sub = tuple(lam[i] for i in idxs)
            if not dominates(sub, conjugate(sub)):
                return False, sub
    return True, None


def exact_lt_from_definition(lam):
    """Count Latin tableaux of shape lam and type lam' directly from Definition 2.5."""
    L = len(lam)
    k = lam[0]
    conj = conjugate(lam)
    # Type lam': symbol s (1..k) appears exactly conj[s-1] times.
    # To enumerate quickly directly from Definition 2.5 without assuming row contents:
    # Fill cell-by-cell from row 0 to L-1, pruning only when remaining cells in rows/cols cannot satisfy type.
    # Actually, since each row r has length lam[r] and we know Lemma 1 forces row r to be {1..lam[r]},
    # let's verify BOTH:
    # (a) pure Definition 2.5 backtracking (pruned only by row-uniqueness, col-uniqueness, remaining symbol counts,
    #     and impossibility when a symbol s has rem_mult[s] > number of remaining rows that don't yet have s);
    # (b) explicit verification of every produced tableau against Definition 2.5.
    cells = [(r, c) for r in range(L) for c in range(lam[r])]
    grid = [[0] * rlen for rlen in lam]
    row_used = [set() for _ in range(L)]
    col_used = [set() for _ in range(k)]
    rem = {s: conj[s - 1] for s in range(1, k + 1)}
    tableaux = []

    # Precompute remaining cells in row r after cell idx
    def bt(idx):
        if idx == len(cells):
            # Verify Definition 2.5 literally on grid
            counts = {s: 0 for s in range(1, k + 1)}
            for r in range(L):
                assert len(grid[r]) == lam[r]
                assert len(set(grid[r])) == lam[r], "Row repeat"
                for c, val in enumerate(grid[r]):
                    assert 1 <= val <= k
                    counts[val] += 1
            for c in range(k):
                col_vals = [grid[r][c] for r in range(L) if c < lam[r]]
                assert len(col_vals) == len(set(col_vals)), "Col repeat"
            for s in range(1, k + 1):
                assert counts[s] == conj[s - 1], "Type mismatch"
            tableaux.append(tuple(tuple(row) for row in grid))
            return

        r, c = cells[idx]
        # Necessary pruning: if row r has `rem_in_row` cells left (including this one),
        # and some symbol s must appear in `rem[s]` distinct rows among remaining rows,
        # actually simple pruning:
        # For each symbol s with rem[s] > 0: how many rows r' >= r can still take s?
        # Row r has (lam[r] - c) cells left; rows r' > r each can take at most 1 copy of s.
        for s in range(1, k + 1):
            if rem[s] == 0 or s in row_used[r] or s in col_used[c]:
                continue
            grid[r][c] = s
            row_used[r].add(s)
            col_used[c].add(s)
            rem[s] -= 1
            # Check feasibility for all symbols s2:
            # max remaining rows that can host s2 is (1 if (s2 not in row_used[r] and c+1 < lam[r]) else 0) + (L - 1 - r)
            # Tighter: number of rows r' > r with (lam[r'] > 0) = L - 1 - r
            feasible = True
            avail_rows_after_r = L - 1 - r
            has_room_in_r = (c + 1 < lam[r])
            for s2 in range(1, k + 1):
                if rem[s2] > avail_rows_after_r + (1 if (has_room_in_r and s2 not in row_used[r]) else 0):
                    feasible = False
                    break
            if feasible:
                bt(idx + 1)
            rem[s] += 1
            col_used[c].remove(s)
            row_used[r].remove(s)

    bt(0)
    assert len(tableaux) == len(set(tableaux))
    return tableaux


def main():
    mu = (6, 5, 5, 3, 2, 1)
    lam = (6, 5, 5, 3, 3, 1)

    # 1. Structural conditions of Conjecture 6.1
    assert len(mu) == len(lam) == 6
    i = 4  # 0-indexed row 4 = 1-indexed row 5 in [1..5] = [ell(lam)-1]
    assert 1 <= i + 1 <= len(lam) - 1
    assert lam[i] == mu[i] + 1
    assert all(lam[j] == mu[j] for j in range(len(lam)) if j != i)
    assert all(mu[j] >= mu[j + 1] > 0 for j in range(len(mu) - 1))
    assert all(lam[j] >= lam[j + 1] > 0 for j in range(len(lam) - 1))

    # 2. Check wideness of both mu and lam across ALL 2^6 - 1 subpartitions
    ok_mu, bad_mu = is_wide_all_subpartitions(mu)
    ok_lam, bad_lam = is_wide_all_subpartitions(lam)
    if not ok_mu or not ok_lam:
        print(f"FAIL: wideness failed: mu={ok_mu} ({bad_mu}), lam={ok_lam} ({bad_lam})")
        return 1

    # 3. Enumerate all Latin tableaux from Definition 2.5
    tabs_mu = exact_lt_from_definition(mu)
    tabs_lam = exact_lt_from_definition(lam)
    print(f"mu  = {mu}: wide=True, LT(mu)  = {len(tabs_mu)}")
    print(f"lam = {lam}: wide=True, LT(lam) = {len(tabs_lam)}")
    if len(tabs_mu) != 56 or len(tabs_lam) != 32:
        print("FAIL: unexpected tableau counts")
        return 1
    if not (len(tabs_lam) < len(tabs_mu)):
        print("FAIL: LT(lam) >= LT(mu)")
        return 1

    print("Sample tableau of mu:", tabs_mu[0])
    print("Sample tableau of lam:", tabs_lam[0])
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
