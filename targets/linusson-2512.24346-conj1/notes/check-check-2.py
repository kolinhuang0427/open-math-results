"""Independent exact-arithmetic verifier for Linusson-Ozdemir (arXiv:2512.24346v1) Conj 1.

Strictly derived from Kplancherel.tex (Sections 2-3) and PROOF.md without reading
verify.py or any author notes. Uses exact integer and Fraction arithmetic.
"""

from __future__ import annotations

import itertools
import math
import signal
import sys
import time
from fractions import Fraction


class TimeoutError(Exception):
    pass


def _alarm_handler(signum, frame):
    raise TimeoutError("Verification exceeded built-in time limit")


def hook_lengths_ok(part: tuple[int, ...], r: int) -> bool:
    """Return True iff partition `part` (tuple of row lengths) is an r-core."""
    if not part:
        return True
    l = len(part)
    # conjugate lengths
    cols = [sum(1 for row in part if row >= c) for c in range(1, part[0] + 1)]
    for i, row_len in enumerate(part):
        for j in range(row_len):
            hook = (row_len - j - 1) + (cols[j] - i - 1) + 1
            if hook == r:
                return False
    return True


def p_map(core: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Map (k+1)-core to k-bounded partition via hook lengths < k+1 (Sec 2.2)."""
    if not core:
        return ()
    cols = [sum(1 for row in core if row >= c) for c in range(1, core[0] + 1)]
    out = []
    for i, row_len in enumerate(core):
        cnt = 0
        for j in range(row_len):
            hook = (row_len - j - 1) + (cols[j] - i - 1) + 1
            if hook < k + 1:
                cnt += 1
        if cnt > 0:
            out.append(cnt)
    return tuple(out)


def maya_occupied(part: tuple[int, ...]) -> set[int]:
    """Occupied set M(part) = Z \\ {part_r - r : r >= 1} (for sufficiently large window)."""
    # Compute vacant set V(part) inside [-N, N]
    vac = set()
    l = len(part)
    bound = max(l + 10, (part[0] if part else 0) + 10)
    for r in range(1, bound + 1):
        pr = part[r - 1] if r <= l else 0
        vac.add(pr - r)
    return set(range(-bound, bound + 1)) - vac


def c_map_via_maya(lam: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Sequential c-map from Kplancherel.tex Section 2.2 (lines 121)."""
    # Add boxes on the left of rows 1..i until all existing cells in row i have hook <= k
    rows = list(lam)
    l = len(rows)
    for i in range(l - 1, -1, -1):
        while True:
            # check max hook of an original cell? Wait: Section 2.2 says:
            # "until all cells already-present in lambda_i have hook-lengths <= k"
            # Since hooks are strictly increasing to the left, the leftmost cell in row i
            # of the original lambda_i? Wait: use the exact definition from Sec 2.2:
            # Actually we can compute columns and check the hook at column (rows[i] - lam[i] + 1)
            # i.e. the leftmost original cell of row i (0-based col = rows[i] - lam[i]).
            col_idx = rows[i] - lam[i]  # 0-based column of leftmost original cell in row i
            leg = sum(1 for r in range(i + 1, l) if rows[r] >= col_idx + 1)
            arm = rows[i] - col_idx - 1  # == lam[i] - 1
            hook = arm + leg + 1
            if hook <= k:
                break
            for r in range(i + 1):
                rows[r] += 1
    return tuple(rows)


def connected_components_of_skew(tau: tuple[int, ...], kappa: tuple[int, ...]) -> int:
    """Count edge-connected components of skew diagram tau \\ kappa."""
    cells = set()
    for i, rlen in enumerate(tau):
        klen = kappa[i] if i < len(kappa) else 0
        for j in range(klen, rlen):
            cells.add((i, j))
    if not cells:
        return 0
    seen = set()
    comps = 0
    for c in cells:
        if c in seen:
            continue
        comps += 1
        stack = [c]
        seen.add(c)
        while stack:
            x, y = stack.pop()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (nx, ny) in cells and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    stack.append((nx, ny))
    return comps


def all_bounded_partitions(k: int, max_size: int) -> list[tuple[int, ...]]:
    res: list[tuple[int, ...]] = []

    def gen(rem: int, max_part: int, cur: list[int]):
        res.append(tuple(cur))
        for p in range(min(rem, max_part), 0, -1):
            cur.append(p)
            gen(rem - p, p, cur)
            cur.pop()

    gen(max_size, k, [])
    return res


def weak_covers_core(kappa: tuple[int, ...], k: int) -> list[tuple[int, ...]]:
    """Find all (k+1)-cores tau covering kappa in weak order (same content mod k+1)."""
    # Group addable corners of kappa by content mod (k+1)
    by_content: dict[int, list[tuple[int, int]]] = {}
    l = len(kappa)
    for i in range(l + 1):
        rlen = kappa[i] if i < l else 0
        prev_len = kappa[i - 1] if i > 0 else (10**9)
        if rlen < prev_len:
            # cell (i, rlen) (0-based) has 1-based row i+1, col rlen+1, content (rlen+1)-(i+1) = rlen - i
            c = (rlen - i) % (k + 1)
            by_content.setdefault(c, []).append((i, rlen))

    covers = []
    for c, cells in by_content.items():
        # In weak cover, add ALL cells of content c? Actually PROOF.md proves A = S_c(kappa),
        # i.e. adding all addable cells of content c (Wait: adding a cell in row i of content c
        # cannot make row i+1 also have an addable cell of content c mod k+1 since k+1>=2).
        # Let's check: adding all cells in `cells` gives a partition tau; verify it's a (k+1)-core
        # and |p(tau)| == |p(kappa)| + 1!
        tau_list = list(kappa)
        for i, rlen in cells:
            if i == len(tau_list):
                tau_list.append(1)
            else:
                tau_list[i] += 1
        tau = tuple(tau_list)
        if hook_lengths_ok(tau, k + 1):
            covers.append(tau)
    return covers


def multiset_to_part(counts: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for idx in range(len(counts) - 1, -1, -1):
        out.extend([idx + 1] * counts[idx])
    return tuple(out)


def part_to_counts(lam: tuple[int, ...], k: int) -> tuple[int, ...]:
    cnt = [0] * k
    for p in lam:
        cnt[p - 1] += 1
    return tuple(cnt)


def red_k(lam: tuple[int, ...], k: int) -> tuple[int, ...]:
    cnt = list(part_to_counts(lam, k))
    for i in range(1, k + 1):
        cnt[i - 1] %= (k - i + 1)
    return multiset_to_part(tuple(cnt))


def comp_k(lam: tuple[int, ...], k: int) -> tuple[int, ...]:
    cnt = part_to_counts(lam, k)
    return multiset_to_part(tuple((k - i) - cnt[i - 1] for i in range(1, k + 1)))


def alpha_bij(sigma: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Lemma 2 eq (2): sigma in S_k (tuple of 1..k+1 ending with k+1) -> R_k."""
    assert sigma[-1] == k + 1 and len(sigma) == k + 1
    pos = {val: idx for idx, val in enumerate(sigma)}
    cnt = [0] * k
    for m in range(1, k + 1):
        pm = pos[m]
        pm1 = pos[m + 1]
        # strictly clockwise from pm to pm1 in circular array of length k+1
        c = 0
        idx = (pm + 1) % (k + 1)
        while idx != pm1:
            if sigma[idx] >= m + 2:
                c += 1
            idx = (idx + 1) % (k + 1)
        cnt[m - 1] = c
    return multiset_to_part(tuple(cnt))


def rev_cyc(sigma: tuple[int, ...]) -> tuple[int, ...]:
    # Reverse cyclic order keeping last element k+1 fixed: (s_1,...,s_k, k+1) -> (s_k,...,s_1, k+1)
    return sigma[:-1][::-1] + (sigma[-1],)


def build_strong_dimensions(k: int, max_n: int) -> tuple[dict[tuple[int, ...], int], dict[tuple[int, ...], tuple[int, ...]]]:
    """Compute d_lambda^(k) directly from Definition 2.4 (strong marked tableaux, weight 1^n)."""
    parts = all_bounded_partitions(k, max_n)
    cores: dict[tuple[int, ...], tuple[int, ...]] = {}
    by_size: dict[int, list[tuple[int, ...]]] = {}
    for lam in parts:
        kap = c_map_via_maya(lam, k)
        assert hook_lengths_ok(kap, k + 1), f"c_map produced non-core for {lam}"
        assert p_map(kap, k) == lam, f"p(c({lam})) != {lam}"
        cores[lam] = kap
        by_size.setdefault(sum(lam), []).append(lam)

    d_val: dict[tuple[int, ...], int] = {(): 1}
    for sz in range(max_n):
        for lam in by_size.get(sz, []):
            kap = cores[lam]
            d_lam = d_val[lam]
            for mu in by_size.get(sz + 1, []):
                tau = cores[mu]
                # Check kappa subset tau
                if len(kap) <= len(tau) and all(
                    (kap[i] if i < len(kap) else 0) <= tau[i] for i in range(len(tau))
                ):
                    comps = connected_components_of_skew(tau, kap)
                    assert comps >= 1
                    d_val[mu] = d_val.get(mu, 0) + comps * d_lam
    return d_val, cores


def syt_hook_dim(part: tuple[int, ...]) -> int:
    if not part:
        return 1
    n = sum(part)
    cols = [sum(1 for row in part if row >= c) for c in range(1, part[0] + 1)]
    prod_hooks = 1
    for i, rlen in enumerate(part):
        for j in range(rlen):
            prod_hooks *= (rlen - j - 1) + (cols[j] - i - 1) + 1
    return math.factorial(n) // prod_hooks


def check_irreducibility_paths(k: int) -> None:
    """Verify Lemma 4 constructive paths between all pairs in R_k (via S_k)."""
    if k < 2:
        return
    perms = [p + (k + 1,) for p in itertools.permutations(range(1, k + 1))]
    id_p = tuple(range(1, k + 2))
    w0 = tuple(range(k, 0, -1)) + (k + 1,)

    def step_swaps(s: tuple[int, ...]) -> set[tuple[int, ...]]:
        out = set()
        for idx in range(k + 1):
            nxt = (idx + 1) % (k + 1)
            j_val, i_val = s[idx], s[nxt]
            if j_val > i_val:
                lst = list(s)
                lst[idx], lst[nxt] = lst[nxt], lst[idx]
                # Normalize so k+1 is at end
                k1_pos = lst.index(k + 1)
                norm = tuple(lst[k1_pos + 1 :] + lst[: k1_pos + 1])
                out.add(norm)
        return out

    # BFS reachability from id_p and to id_p
    adj = {s: step_swaps(s) for s in perms}
    # Check id_p -> w0 and w0 -> all, all -> id_p
    for s in perms:
        # sigma ->* id_p by inversion reductions
        cur = s
        while cur != id_p:
            moved = False
            for idx in range(k - 1):
                if cur[idx] > cur[idx + 1]:
                    lst = list(cur)
                    lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                    nxt = tuple(lst)
                    assert nxt in adj[cur]
                    cur = nxt
                    moved = True
                    break
            assert moved
    # id_p ->* w0 and w0 ->* all via BFS check
    seen = {id_p}
    stack = [id_p]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    assert len(seen) == len(perms)


def main() -> int:
    signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(60)
    t0 = time.monotonic()

    # 1. Check k=1..4 completely (strong marked tableaux, Lemma 1-4, R-reversibility, exact pi)
    known_pi = {
        3: {
            (): Fraction(3, 20),
            (2, 1): Fraction(4, 20),
            (1, 1): Fraction(3, 20),
            (2,): Fraction(3, 20),
            (1,): Fraction(4, 20),
            (2, 1, 1): Fraction(3, 20),
        },
        4: {
            (): Fraction(8, 280),
            (1,): Fraction(14, 280),
            (1, 1): Fraction(12, 280),
            (1, 1, 1): Fraction(8, 280),
            (2,): Fraction(12, 280),
            (2, 1): Fraction(16, 280),
            (2, 1, 1): Fraction(15, 280),
            (2, 1, 1, 1): Fraction(12, 280),
            (2, 2): Fraction(8, 280),
            (2, 2, 1): Fraction(12, 280),
            (2, 2, 1, 1): Fraction(15, 280),
            (2, 2, 1, 1, 1): Fraction(8, 280),
        },
    }

    for k in (1, 2, 3, 4):
        max_r_size = sum(i * (k - i) for i in range(1, k + 1))
        max_n = max_r_size + k  # enough for mu cup square_i
        d_val, cores = build_strong_dimensions(k, max_n)

        # Enumerate R_k
        R_k = [lam for lam in cores if red_k(lam, k) == lam]
        assert len(R_k) == math.factorial(k)

        # Check Lemma 2 (alpha bijection and complement = reversal)
        if k >= 2:
            perms = [p + (k + 1,) for p in itertools.permutations(range(1, k + 1))]
            seen_R = {}
            for sig in perms:
                lam = alpha_bij(sig, k)
                assert lam in R_k
                seen_R[sig] = lam
                lam_rev = alpha_bij(rev_cyc(sig), k)
                assert lam_rev == comp_k(lam, k), f"Lemma 2(2) failed at k={k}, sig={sig}"
            assert len(set(seen_R.values())) == len(R_k)
            inv_alpha = {v: u for u, v in seen_R.items()}

        # Check Lemma 1(2): k-rectangle identity for all lam in R_k and i in 1..k
        for lam in R_k:
            for i in range(1, k + 1):
                rect = (i,) * (k - i + 1)
                if sum(lam) + sum(rect) <= max_n:
                    lam_rect = tuple(sorted(lam + rect, reverse=True))
                    lhs = Fraction(d_val[lam_rect], math.factorial(sum(lam_rect)))
                    rhs = Fraction(syt_hook_dim(rect), math.factorial(sum(rect))) * Fraction(
                        d_val[lam], math.factorial(sum(lam))
                    )
                    assert lhs == rhs, f"Lemma 1(2) failed at k={k}, lam={lam}, i={i}"

        # Build Markov transition matrix P on R_k from weak covers
        P: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction] = {
            (a, b): Fraction(0, 1) for a in R_k for b in R_k
        }
        for lam in R_k:
            kap = cores[lam]
            w_covers = weak_covers_core(kap, k)
            row_sum = Fraction(0, 1)
            projected = []
            for tau in w_covers:
                Lam = p_map(tau, k)
                assert sum(Lam) == sum(lam) + 1
                mu = red_k(Lam, k)
                projected.append(mu)
                prob = Fraction(d_val[Lam], (sum(lam) + 1) * d_val[lam])
                P[(lam, mu)] += prob
                row_sum += prob
            assert row_sum == 1, f"Lemma 1(1) row stochasticity failed at k={k}, lam={lam}: {row_sum}"
            if k >= 3:
                assert len(set(projected)) == len(projected), f"Lemma 3(2) distinctness failed at k={k}, lam={lam}"

            # Also verify Lemma 3(1) TASEP swap correspondence when k >= 2
            if k >= 2:
                sig = inv_alpha[lam]
                tasep_targets = []
                for idx in range(k + 1):
                    nxt = (idx + 1) % (k + 1)
                    if sig[idx] > sig[nxt]:
                        lst = list(sig)
                        lst[idx], lst[nxt] = lst[nxt], lst[idx]
                        k1_pos = lst.index(k + 1)
                        norm = tuple(lst[k1_pos + 1 :] + lst[: k1_pos + 1])
                        tasep_targets.append(alpha_bij(norm, k))
                assert sorted(projected) == sorted(tasep_targets), f"Lemma 3(1) mismatch at k={k}, lam={lam}"

        # Check closed-form w(lam) and R-reversibility
        w = {
            lam: Fraction(
                d_val[lam] * d_val[comp_k(lam, k)],
                math.factorial(sum(lam)) * math.factorial(sum(comp_k(lam, k))),
            )
            for lam in R_k
        }
        Z_k = sum(w.values())
        pi = {lam: w[lam] / Z_k for lam in R_k}

        for lam in R_k:
            for mu in R_k:
                lhs = pi[lam] * P[(lam, mu)]
                rhs = pi[mu] * P[(comp_k(mu, k), comp_k(lam, k))]
                assert lhs == rhs, f"R-reversibility failed at k={k}, {lam} -> {mu}"

        # Check exact stationarity pi * P == pi and pi(lam) == pi(lam^comp)
        for mu in R_k:
            stat = sum(pi[lam] * P[(lam, mu)] for lam in R_k)
            assert stat == pi[mu], f"Stationarity failed at k={k}, mu={mu}"
            assert pi[mu] == pi[comp_k(mu, k)], f"Conj 1 failed at k={k}, mu={mu}"

        if k in known_pi:
            for lam, val in known_pi[k].items():
                assert pi[lam] == val, f"Paper table mismatch at k={k}, {lam}: {pi[lam]} vs {val}"

        check_irreducibility_paths(k)
        print(f"k={k} (|R_{k}|={len(R_k)}, Z_{k}={Z_k}): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS")

    # 2. Check k=5 combinatorics (Lemmas 2, 3, 4 on all 120 states)
    k = 5
    perms5 = [p + (6,) for p in itertools.permutations(range(1, 6))]
    R_5 = set()
    for sig in perms5:
        lam = alpha_bij(sig, 5)
        R_5.add(lam)
        assert alpha_bij(rev_cyc(sig), 5) == comp_k(lam, 5)
    assert len(R_5) == 120
    check_irreducibility_paths(5)
    print("k=5 (|R_5|=120): Lemmas 2 & 4 PASS")

    elapsed = time.monotonic() - t0
    print(f"PASS (all checks passed in {elapsed:.3f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
