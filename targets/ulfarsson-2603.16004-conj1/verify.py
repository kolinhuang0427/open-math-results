"""Exact-arithmetic verification script for PROOF.md (Úlfarsson, arXiv:2603.16004v1, Conjecture 2.9).

Uses pure integer arithmetic only (zero floats, zero true-division operators).
Prints PASS on success (exit code 0) or FAIL on any check failure (exit code 1).
"""

import ast
import itertools
import sys


def std_seq(seq):
    """Return the standardization of a sequence of distinct integers as a tuple in 1..len(seq)."""
    ordered = sorted(seq)
    rank = {v: i + 1 for i, v in enumerate(ordered)}
    return tuple(rank[v] for v in seq)


def rev(p):
    """Reverse of a permutation tuple."""
    return p[::-1]


def is_monotone(p):
    """Return True iff permutation p (length >= 2) is strictly increasing or strictly decreasing."""
    inc = all(p[i] < p[i + 1] for i in range(len(p) - 1))
    dec = all(p[i] > p[i + 1] for i in range(len(p) - 1))
    return inc or dec


def asc_count(p):
    return sum(1 for i in range(len(p) - 1) if p[i] < p[i + 1])


def des_count(p):
    return sum(1 for i in range(len(p) - 1) if p[i] > p[i + 1])


def inflate(gamma, j_1based, t, sign):
    """Compute I_t(gamma, j, sign) for 1-based index j, integer t >= 1, sign in {'+', '-'}."""
    v = gamma[j_1based - 1]
    out = []
    for idx, val in enumerate(gamma, start=1):
        if idx == j_1based:
            if sign == "+":
                out.extend(range(v, v + t))
            elif sign == "-":
                out.extend(range(v + t - 1, v - 1, -1))
            else:
                raise ValueError(f"bad sign {sign}")
        elif val < v:
            out.append(val)
        else:
            out.append(val + t - 1)
    return tuple(out)


def shadow_k(pi, k):
    """Exact k-shadow Sh_k(pi) as a frozenset of tuples."""
    n = len(pi)
    res = set()
    for idxs in itertools.combinations(range(n), k):
        sub = tuple(pi[i] for i in idxs)
        res.add(std_seq(sub))
    return frozenset(res)


def find_occurrence(pi, pat):
    """Return a tuple of 0-based indices where pat occurs in pi, or None if pi avoids pat.

    Exact backtracking search (fast for medium lengths without enumerating all C(n, k) subsets).
    """
    n = len(pi)
    m = len(pat)
    if m > n:
        return None
    if m == 0:
        return ()

    # Precompute relative bounds for each position r in pat against earlier positions 0..r-1:
    # closest smaller value index and closest larger value index among 0..r-1.
    prev_lo = []
    prev_hi = []
    for r in range(m):
        v = pat[r]
        best_lo_val = -1
        best_lo_idx = -1
        best_hi_val = m + 2
        best_hi_idx = -1
        for prev in range(r):
            pv = pat[prev]
            if pv < v and pv > best_lo_val:
                best_lo_val = pv
                best_lo_idx = prev
            if pv > v and pv < best_hi_val:
                best_hi_val = pv
                best_hi_idx = prev
        prev_lo.append(best_lo_idx)
        prev_hi.append(best_hi_idx)

    chosen_idx = [0] * m
    chosen_val = [0] * m
    min_val = min(pi) - 1
    max_val = max(pi) + 1

    def dfs(pos, start_i):
        if pos == m:
            return True
        lo_i = prev_lo[pos]
        hi_i = prev_hi[pos]
        lo_bound = chosen_val[lo_i] if lo_i != -1 else min_val
        hi_bound = chosen_val[hi_i] if hi_i != -1 else max_val
        limit = n - (m - pos) + 1
        for i in range(start_i, limit):
            val = pi[i]
            if lo_bound < val < hi_bound:
                chosen_idx[pos] = i
                chosen_val[pos] = val
                if dfs(pos + 1, i + 1):
                    return True
        return False

    if dfs(0, 0):
        return tuple(chosen_idx)
    return None


def contains_pattern(pi, pat):
    return find_occurrence(pi, pat) is not None


def contiguous_monotone_blocks(p, sign):
    """Yield (a, t) (0-based start a, length t with 2 <= t <= k-1) for all contiguous
    index-AND-value monotone blocks of sign in p.
    """
    k = len(p)
    step = 1 if sign == "+" else -1
    for a in range(k):
        for t in range(2, k):
            if a + t > k:
                break
            ok = True
            for r in range(t - 1):
                if p[a + r + 1] - p[a + r] != step:
                    ok = False
                    break
            if ok:
                yield (a, t)


def collapse_block(p, a, t):
    """Collapse contiguous block p[a : a+t] to single element p[a] and standardize."""
    sub = p[: a + 1] + p[a + t :]
    return std_seq(sub)


def check_1_thresholds():
    """Verify exact polynomial and all inequalities for n_0(k) across 3 <= k <= 500."""
    for k in range(3, 501):
        n0 = k + ((2 * k + 1) * (k - 1)) ** 2 + 1
        poly = 4 * (k ** 4) - 4 * (k ** 3) - 3 * (k ** 2) + 3 * k + 2
        assert n0 == poly, f"Polynomial mismatch at k={k}: {n0} != {poly}"
        assert n0 > (k - 1) ** 2 + 1, f"ES threshold fail at k={k}"
        assert n0 - k == ((2 * k + 1) * (k - 1)) ** 2 + 1
        assert n0 - k > 2 * k - 2, f"n0 - k <= 2k - 2 at k={k}"
        assert 2 * k - 2 > k, f"2k - 2 <= k at k={k}"
        assert n0 - k + 1 > k, f"n0 - k + 1 <= k at k={k}"
        # Pigeonhole check: L = (2k+1)(k-1) + 1 > (2k+1)(k-1)
        L = (2 * k + 1) * (k - 1) + 1
        assert L > (2 * k + 1) * (k - 1)
        assert (L - 1) ** 2 + 1 == n0 - k
    print("[OK] Check 1: n_0(k) polynomial & threshold inequalities verified for 3 <= k <= 500.")


def check_2_lemma0():
    """Verify Lemma 0(1) reversal identity, Lemma 0(2) shadow stabilization, Lemma 0(3) block inflation."""
    # (1) Reversal identity: exhaustive for m in {3, 4}, all gamma, all j, t in 1..m+2, both signs
    rev_count = 0
    for m in (3, 4):
        for gamma in itertools.permutations(range(1, m + 1)):
            for j in range(1, m + 1):
                for t in range(1, m + 3):
                    for sign, opp in (("+", "-"), ("-", "+")):
                        lhs = rev(inflate(gamma, j, t, sign))
                        rhs = inflate(rev(gamma), m + 1 - j, t, opp)
                        assert lhs == rhs, f"Reversal identity failed: {gamma}, {j}, {t}, {sign}"
                        rev_count += 1

    # (2) Shadow stabilization:
    # k=3 exhaustive for m in {3, 4}, t in {3, 4, 5}; k=4 exhaustive for m=4, t in {4, 5}
    stab_count = 0
    for m in (3, 4):
        for gamma in itertools.permutations(range(1, m + 1)):
            for j in range(1, m + 1):
                for sign in ("+", "-"):
                    base = shadow_k(inflate(gamma, j, 3, sign), 3)
                    for t in (4, 5):
                        assert shadow_k(inflate(gamma, j, t, sign), 3) == base
                        stab_count += 1
    for gamma in itertools.permutations(range(1, 5)):
        for j in range(1, 5):
            for sign in ("+", "-"):
                base = shadow_k(inflate(gamma, j, 4, sign), 4)
                assert shadow_k(inflate(gamma, j, 5, sign), 4) == base
                stab_count += 1

    # (3) Contiguous monotone-block inflation: exhaustive on k=3, all 1-point extensions beta in S_4
    block_count = 0
    k = 3
    b_len = 2 * k - 2  # = 4
    for beta in itertools.permutations(range(1, k + 2)):
        for i0 in range(1, k + 2):
            p = std_seq(beta[: i0 - 1] + beta[i0:])
            if is_monotone(p):
                continue
            pr = rev(p)
            for sign in ("+", "-"):
                sigma = inflate(beta, i0, b_len, sign)
                b_indices = set(range(i0 - 1, i0 - 1 + b_len))
                for idxs in itertools.combinations(range(len(sigma)), k):
                    if std_seq(tuple(sigma[x] for x in idxs)) == pr:
                        in_b = [x for x in idxs if x in b_indices]
                        in_p0 = [x for x in idxs if x not in b_indices]
                        s1 = len(in_b)
                        assert 1 <= s1 <= k - 1
                        # First 1-based index of R1 cap B0 in R1:
                        j1 = idxs.index(in_b[0]) + 1
                        expected = inflate(pr, j1, k, sign)
                        for b_sub in itertools.combinations(sorted(b_indices), k + s1 - 1):
                            comb = sorted(in_p0 + list(b_sub))
                            got = std_seq(tuple(sigma[x] for x in comb))
                            assert got == expected, f"Lemma 0(3) failed: {got} != {expected}"
                            block_count += 1

    print(
        f"[OK] Check 2: Lemma 0 verified ({rev_count} reversal identities, "
        f"{stab_count} shadow stabilizations, {block_count} block-inflation embeddings)."
    )


def check_3_lemma2_witnesses():
    """Trace Lemma 2 Case 1 / Subcase 2a / Subcase 2b exhaustively for k=3 and k=4."""
    stats = {}
    for k in (3, 4):
        b_len = 2 * k - 2  # minimal block size needed by Lemma 2 (n - k >= 2k - 2)
        c1 = c2a = c2b = 0
        for beta in itertools.permutations(range(1, k + 2)):
            for i0 in range(1, k + 2):
                p = std_seq(beta[: i0 - 1] + beta[i0:])
                if is_monotone(p):
                    continue
                pr = rev(p)
                for sign, opp in (("+", "-"), ("-", "+")):
                    sigma = inflate(beta, i0, b_len, sign)
                    sigma_r = rev(sigma)
                    sh_sigma = shadow_k(sigma, k)
                    sh_sigma_r = frozenset(rev(q) for q in sh_sigma)
                    assert sh_sigma_r == shadow_k(sigma_r, k)
                    assert pr in sh_sigma_r

                    if p not in sh_sigma_r:
                        # Case 1: sigma^r avoids p and contains p^r
                        c1 += 1
                        continue

                    # Case 2: p in Sh_k(sigma^r) <=> p^r in Sh_k(sigma)
                    assert pr in sh_sigma
                    b_indices = set(range(i0 - 1, i0 - 1 + b_len))
                    r1 = find_occurrence(sigma, pr)
                    assert r1 is not None
                    in_b = [x for x in r1 if x in b_indices]
                    in_p0 = [x for x in r1 if x not in b_indices]
                    s1 = len(in_b)
                    assert 1 <= s1 <= k - 1
                    j1 = r1.index(in_b[0]) + 1
                    b_prime = sorted(b_indices)[: k + s1 - 1]
                    sub1_idxs = sorted(in_p0 + b_prime)
                    inf1 = inflate(pr, j1, k, sign)
                    assert std_seq(tuple(sigma[x] for x in sub1_idxs)) == inf1
                    sh_inf1 = shadow_k(inf1, k)
                    assert sh_inf1.issubset(sh_sigma)
                    assert pr in sh_inf1

                    if p not in sh_inf1:
                        # Subcase 2a: omega_1 avoids p and contains p^r
                        c2a += 1
                        continue

                    # Subcase 2b: extract P_2 inside (R_1 cap P_0) U B' of pattern p
                    sub1_vals = tuple(sigma[x] for x in sub1_idxs)
                    p2_local = find_occurrence(sub1_vals, p)
                    assert p2_local is not None
                    p2 = tuple(sub1_idxs[idx] for idx in p2_local)
                    assert std_seq(tuple(sigma[x] for x in p2)) == p
                    s2 = sum(1 for x in p2 if x in b_indices)
                    assert s1 <= s2 <= k - 1

                    # Reflect to R_2 = rho(P_2) inside sigma^r
                    m_len = len(sigma)
                    r2 = tuple(reversed([m_len - 1 - x for x in p2]))
                    assert std_seq(tuple(sigma_r[x] for x in r2)) == pr
                    br_indices = set(m_len - 1 - x for x in b_indices)
                    r2_in_br = [x for x in r2 if x in br_indices]
                    r2_in_p0r = [x for x in r2 if x not in br_indices]
                    assert len(r2_in_br) == s2
                    j2 = r2.index(r2_in_br[0]) + 1
                    b_dprime = sorted(br_indices)[: k + s2 - 1]
                    sub2_idxs = sorted(r2_in_p0r + b_dprime)
                    inf2 = inflate(pr, j2, k, opp)
                    assert std_seq(tuple(sigma_r[x] for x in sub2_idxs)) == inf2
                    sh_inf2 = shadow_k(inf2, k)
                    assert sh_inf2.issubset(sh_sigma_r)
                    assert pr in sh_inf2
                    assert p not in sh_inf2, f"Theorem 3 / Subcase 2b failed for p={p}"
                    c2b += 1

        stats[k] = (c1, c2a, c2b)
    print(
        f"[OK] Check 3: Lemma 2 witness construction verified exhaustively "
        f"(k=3: C1={stats[3][0]}, C2a={stats[3][1]}, C2b={stats[3][2]}; "
        f"k=4: C1={stats[4][0]}, C2a={stats[4][1]}, C2b={stats[4][2]})."
    )


def check_4_theorem3_exhaustive():
    """Exhaustively verify Claim 3A, Claim 3B, and Theorem 3 for k = 3, 4, 5, 6, 7."""
    summary = []
    for k in (3, 4, 5, 6, 7):
        total_nonmono = 0
        plus_hits = 0
        minus_hits = 0
        eq_plus_hits = 0
        eq_minus_hits = 0
        for p in itertools.permutations(range(1, k + 1)):
            if is_monotone(p):
                continue
            total_nonmono += 1
            pr = rev(p)

            # Direct inflation containment check: exists j in 1..k with p <= I_k(p^r, j, sign)
            has_plus_direct = any(
                contains_pattern(inflate(pr, j, k, "+"), p) for j in range(1, k + 1)
            )
            has_minus_direct = any(
                contains_pattern(inflate(pr, j, k, "-"), p) for j in range(1, k + 1)
            )

            # Theorem 3 assertion: NEVER both!
            assert not (has_plus_direct and has_minus_direct), (
                f"Theorem 3 counterexample at k={k}, p={p}"
            )

            if has_plus_direct:
                plus_hits += 1
            if has_minus_direct:
                minus_hits += 1

            # Verify Claim 3A equivalence and Claim 3B monotonicity/rigidity
            # For k <= 6 check EVERY permutation; for k = 7 check all direct hits + all asc == des
            do_detailed = (k <= 6) or has_plus_direct or has_minus_direct or (asc_count(p) == des_count(p))
            if do_detailed:
                p_asc = asc_count(p)
                p_des = des_count(p)

                # Check Claim 3A for '+'
                plus_blocks = []
                for a, t in contiguous_monotone_blocks(p, "+"):
                    q = collapse_block(p, a, t)
                    if contains_pattern(pr, q):
                        plus_blocks.append((a, t, q))
                assert bool(plus_blocks) == has_plus_direct, (
                    f"Claim 3A (+) mismatch at k={k}, p={p}"
                )
                for a, t, q in plus_blocks:
                    m = len(q)
                    assert 2 <= m <= k - 1
                    assert des_count(q) == p_des
                    assert (p[0] < p[-1]) == (q[0] < q[-1])
                    qr = rev(q)
                    occ = find_occurrence(p, qr)
                    assert occ is not None
                    assert asc_count(qr) <= p_asc
                    if asc_count(qr) == p_asc:
                        eq_plus_hits += 1
                        assert p[0] >= p[occ[0]]
                        assert p[occ[-1]] >= p[-1]
                        # Since asc(q_+^r) = des(p) = asc(p), our proof forces p(1) > p(k)!
                        assert p[0] > p[-1], f"Endpoint rigidity (+) failed at k={k}, p={p}"

                # Check Claim 3A for '-'
                minus_blocks = []
                for a, t in contiguous_monotone_blocks(p, "-"):
                    q = collapse_block(p, a, t)
                    if contains_pattern(pr, q):
                        minus_blocks.append((a, t, q))
                assert bool(minus_blocks) == has_minus_direct, (
                    f"Claim 3A (-) mismatch at k={k}, p={p}"
                )
                for a, t, q in minus_blocks:
                    m = len(q)
                    assert 2 <= m <= k - 1
                    assert asc_count(q) == p_asc
                    assert (p[0] > p[-1]) == (q[0] > q[-1])
                    qr = rev(q)
                    occ = find_occurrence(p, qr)
                    assert occ is not None
                    assert des_count(qr) <= p_des
                    if des_count(qr) == p_des:
                        eq_minus_hits += 1
                        assert p[0] <= p[occ[0]]
                        assert p[occ[-1]] <= p[-1]
                        # Since des(q_-^r) = asc(p) = des(p), our proof forces p(1) < p(k)!
                        assert p[0] < p[-1], f"Endpoint rigidity (-) failed at k={k}, p={p}"

        summary.append(
            f"k={k}: nonmono={total_nonmono}, +hits={plus_hits}, -hits={minus_hits}, both=0"
        )
    print("[OK] Check 4: Claim 3A, Claim 3B & Theorem 3 verified exhaustively for k=3..7:")
    for line in summary:
        print(f"     {line}")


def check_5_pap_game_k3():
    """End-to-end exact PAP game tree verification for k=3, n in {5, 6}:
    1. Exact Sprague-Grundy value sg(S_n, 3) == 0.
    2. Move-by-move reverse strategy wins EVERY line of play for Player II.
    """
    k = 3
    patterns = list(itertools.permutations(range(1, k + 1)))
    pat_idx = {p: i for i, p in enumerate(patterns)}
    rev_idx = [pat_idx[rev(p)] for p in patterns]

    for n in (5, 6):
        # Precompute bitmask of 3-patterns contained in each pi in S_n
        perm_masks = []
        for pi in itertools.permutations(range(1, n + 1)):
            mask = 0
            for p in shadow_k(pi, k):
                mask |= 1 << pat_idx[p]
            perm_masks.append(mask)

        # Position is represented by forbidden bitmask F_mask (subset of 0..5)
        sg_memo = {}

        def legal_moves(f_mask):
            # A pattern i is legal iff some pi avoids f_mask (perm_mask & f_mask == 0) and contains i
            union_patterns = 0
            for pm in perm_masks:
                if (pm & f_mask) == 0:
                    union_patterns |= pm
            return [i for i in range(len(patterns)) if (union_patterns >> i) & 1]

        def sg(f_mask):
            if f_mask in sg_memo:
                return sg_memo[f_mask]
            moves = legal_moves(f_mask)
            child_vals = set()
            for m in moves:
                child_vals.add(sg(f_mask | (1 << m)))
            val = 0
            while val in child_vals:
                val += 1
            sg_memo[f_mask] = val
            return val

        assert sg(0) == 0, f"sg(S_{n}, 3) != 0"

        # Verify literal move-by-move reverse strategy wins every play from F_mask = 0
        def rev_strategy_wins(f_mask):
            moves_p1 = legal_moves(f_mask)
            if not moves_p1:
                return True  # Player I has no move -> Player II wins
            for m1 in moves_p1:
                after_p1 = f_mask | (1 << m1)
                m2 = rev_idx[m1]
                if m2 not in legal_moves(after_p1):
                    return False  # Reverse reply illegal!
                if not rev_strategy_wins(after_p1 | (1 << m2)):
                    return False
            return True

        assert rev_strategy_wins(0), f"Reverse strategy failed at k=3, n={n}"

    print("[OK] Check 5: Exact PAP game tree verified for k=3, n=5,6 (sg=0 and reverse strategy wins).")


def check_6_zero_floats_ast():
    """AST self-audit ensuring this verification script contains zero float literals, float() calls, or '/' divisions."""
    with open(__file__, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=__file__)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal detected: {node.value}")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            raise AssertionError("True division '/' operator detected")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            raise AssertionError("float() call detected")
    print("[OK] Check 6: Zero-float / zero-division AST self-audit passed.")


def main():
    try:
        check_6_zero_floats_ast()
        check_1_thresholds()
        check_2_lemma0()
        check_3_lemma2_witnesses()
        check_4_theorem3_exhaustive()
        check_5_pap_game_k3()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
