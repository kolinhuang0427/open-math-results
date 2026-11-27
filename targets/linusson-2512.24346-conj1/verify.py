#!/usr/bin/env python3
"""Exact-arithmetic verification of all lemmas and Theorem 1 / Conjecture 1
(Linusson-Ozdemir, arXiv:2512.24346v1, Section 3.4, conj:complement) for k = 1..5.

Uses only exact integer and fractions.Fraction arithmetic (zero floating point).
Prints PASS if every check succeeds, otherwise FAIL with diagnostic details.
"""

from fractions import Fraction
from math import factorial, lcm
import signal
import sys
import sympy as sp


class TimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("Verification exceeded built-in time limit")


def counts_to_part(counts):
    """Convert multiplicity vector (l_1, ..., l_k) to partition tuple (weakly decreasing)."""
    res = []
    for i in range(len(counts), 0, -1):
        res.extend([i] * counts[i - 1])
    return tuple(res)


def part_to_counts(lam, k):
    c = [0] * k
    for p in lam:
        c[p - 1] += 1
    return tuple(c)


def red_k(lam, k):
    """Project a k-bounded partition onto R_k by removing k-rectangles."""
    c = list(part_to_counts(lam, k))
    for i in range(1, k + 1):
        c[i - 1] %= (k - i + 1)
    return counts_to_part(c)


def comp_part(lam, k):
    """Complement lambda^comp in R_k: l_i(lam) + l_i(lam^comp) = k - i."""
    c = part_to_counts(lam, k)
    return counts_to_part(tuple((k - i) - c[i - 1] for i in range(1, k + 1)))


def bounded_to_core(lam, k):
    """Map c: P_k -> C_{k+1} (Section 2.2 of Kplancherel.tex)."""
    if not lam:
        return ()
    rows = list(lam)
    L = len(rows)
    for i in range(L - 1, -1, -1):
        oi = lam[i]
        sub = rows[i:]
        while True:
            rl = sub[0]
            start = rl - oi
            bad = False
            for j in range(start, rl):
                ch = 0
                for r in sub:
                    if r > j:
                        ch += 1
                    else:
                        break
                if (rl - 1 - j) + ch >= k + 1:
                    bad = True
                    break
            if bad:
                for m in range(i + 1):
                    rows[m] += 1
                sub[0] += 1
            else:
                break
    return tuple(rows)


def core_to_bounded(kappa, k):
    """Map p: C_{k+1} -> P_k (number of cells in each row with hook length < k+1)."""
    res = []
    L = len(kappa)
    for i, rl in enumerate(kappa):
        cnt = 0
        for j in range(rl):
            ch = 0
            for r in range(i, L):
                if kappa[r] > j:
                    ch += 1
                else:
                    break
            h = (rl - 1 - j) + ch
            assert h != k + 1, f"Not a {k+1}-core: {kappa} has hook {k+1} at ({i},{j})"
            if h < k + 1:
                cnt += 1
        if cnt > 0:
            res.append(cnt)
    return tuple(res)


def maya_minima_and_sigma(kappa, k):
    """Compute leftmost occupied positions b_1 < ... < b_{k+1} in M(kappa) = Z \\ V(kappa)
    where V(kappa) = {kappa_r - r : r >= 1}, and the cyclic permutation sigma in S_k
    (normalized with k+1 at the end).
    """
    L = len(kappa)
    vac_nonneg = set()
    vac_all = set()
    min_val = -L - (k + 2)
    for r in range(1, L + 1):
        v = kappa[r - 1] - r
        vac_all.add(v)
        if v >= 0:
            vac_nonneg.add(v)
    for r in range(L + 1, L + k + 5):
        vac_all.add(-r)

    max_v = max(vac_all) if vac_all else -1
    # For each residue mod (k+1), find smallest x >= -L - 1 not in V(kappa)
    b_by_res = {}
    for res in range(k + 1):
        # Start below min possible occupied (-L)
        x = min_val + ((res - min_val) % (k + 1))
        while x in vac_all:
            x += k + 1
        # Verify core closure above x up to max_v + k + 1
        y = x
        while y <= max_v + k + 1:
            assert y not in vac_all, f"Core closure violated at {y} for {kappa}"
            y += k + 1
        b_by_res[res] = x

    ordered = sorted((b_by_res[res], res) for res in range(k + 1))
    b_sorted = [val for val, _ in ordered]
    # Place label p (1..k+1) at position r_p = b_p mod (k+1) on Z/(k+1)Z
    ring = [0] * (k + 1)
    for p_idx, (_, res) in enumerate(ordered, start=1):
        ring[res] = p_idx
    pos_last = ring.index(k + 1)
    sigma = tuple(ring[(pos_last + 1 + t) % (k + 1)] for t in range(k + 1))
    return b_sorted, sigma


def alpha_from_sigma(sigma, k):
    """Cyclic-arc formula (2) of Lemma 2: l_m(alpha(sigma))."""
    assert sigma[-1] == k + 1 and len(sigma) == k + 1
    counts = [0] * k
    for m in range(1, k + 1):
        idx_m = sigma.index(m)
        cnt = 0
        t = (idx_m + 1) % (k + 1)
        while sigma[t] != m + 1:
            if sigma[t] >= m + 2:
                cnt += 1
            t = (t + 1) % (k + 1)
        counts[m - 1] = cnt
    return counts_to_part(counts)


def sigma_rev(sigma):
    """Cyclic reversal keeping the last entry (k+1) fixed."""
    return tuple(reversed(sigma[:-1])) + (sigma[-1],)


def tasep_swaps(sigma, k):
    """Return list of (j, i, tau) for every legal swap (j, i) -> (i, j) with j > i."""
    res = []
    n = k + 1
    for pos in range(n):
        i = sigma[pos]
        j = sigma[(pos - 1) % n]
        if j > i:
            arr = list(sigma)
            arr[pos], arr[(pos - 1) % n] = j, i
            p_last = arr.index(n)
            tau = tuple(arr[(p_last + 1 + t) % n] for t in range(n))
            res.append((j, i, tau))
    return res


def weak_covers_from_core(kappa, k):
    """Directly enumerate weak covers kappa ->_k tau via Definition 2.1:
    all cells of tau \\ kappa have the same content mod (k+1).
    Returns list of (res_mod, tau, p(tau)).
    """
    L = len(kappa)
    # Find all addable cells of kappa, grouped by content mod (k+1)
    by_res = {}
    for r in range(L + 1):
        cur_len = kappa[r] if r < L else 0
        prev_len = kappa[r - 1] if r > 0 else cur_len + 1
        if r == 0 or cur_len < prev_len:
            # cell (r+1, cur_len+1) has 1-based content (cur_len+1)-(r+1) = cur_len - r
            c_mod = (cur_len - r) % (k + 1)
            by_res.setdefault(c_mod, []).append(r)

    covers = []
    for c_mod, rows_to_add in by_res.items():
        new_rows = list(kappa)
        for r in rows_to_add:
            if r == len(new_rows):
                new_rows.append(1)
            else:
                new_rows[r] += 1
        tau = tuple(new_rows)
        # Verify tau is a (k+1)-core
        is_core = True
        Lt = len(tau)
        for ri, rl in enumerate(tau):
            for cj in range(rl):
                ch = sum(1 for rr in range(ri, Lt) if tau[rr] > cj)
                if (rl - 1 - cj) + ch == k + 1:
                    is_core = False
                    break
            if not is_core:
                break
        if is_core:
            lam_t = core_to_bounded(tau, k)
            covers.append((c_mod, tau, lam_t))
    return covers


def connected_components_skew(outer, inner):
    cells = set()
    li = len(inner)
    for i, rl in enumerate(outer):
        start = inner[i] if i < li else 0
        for j in range(start, rl):
            cells.add((i, j))
    comp = 0
    while cells:
        comp += 1
        stack = [cells.pop()]
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (nr, nc) in cells:
                    cells.remove((nr, nc))
                    stack.append((nr, nc))
    return comp


def gen_bounded_parts(n, k, max_part=None):
    if max_part is None:
        max_part = k
    if n == 0:
        yield ()
        return
    for p in range(min(n, max_part), 0, -1):
        for rest in gen_bounded_parts(n - p, k, p):
            yield (p,) + rest


def compute_dk_strong(max_n, k):
    """Compute d_lambda^(k) for all lambda in P_k(<= max_n) directly from
    Definition 2.6 (strong marked tableaux of weight (1^n) on (k+1)-cores).
    """
    cores_by_n = {0: [((), ())]}
    d = {(): 1}
    for n in range(1, max_n + 1):
        cur = []
        prev = cores_by_n[n - 1]
        for lam in gen_bounded_parts(n, k):
            c_lam = bounded_to_core(lam, k)
            len_c = len(c_lam)
            c0 = c_lam[0]
            tot = 0
            for mu, c_mu in prev:
                if len(c_mu) <= len_c and (not c_mu or c_mu[0] <= c0):
                    if all(c_mu[i] <= c_lam[i] for i in range(len(c_mu))):
                        tot += connected_components_skew(c_lam, c_mu) * d[mu]
            d[lam] = tot
            cur.append((lam, c_lam))
        cores_by_n[n] = cur
    return d


def hook_dim(lam):
    """Standard Young tableau count d_lambda via hook-length formula (exact)."""
    n = sum(lam)
    prod = 1
    L = len(lam)
    for i, rl in enumerate(lam):
        for j in range(rl):
            ch = sum(1 for r in range(i, L) if lam[r] > j)
            prod *= (rl - 1 - j) + ch
    assert factorial(n) % prod == 0
    return factorial(n) // prod


def verify_irreducibility_paths(k, all_sigmas):
    """Verify constructive paths sigma -> id -> omega_0 -> tau of Lemma 4."""
    if k == 1:
        return
    id_s = tuple(range(1, k + 2))
    w0_s = tuple(range(k, 0, -1)) + (k + 1,)

    def legal_next(s):
        return {tau for _, _, tau in tasep_swaps(s, k)}

    # 1. sigma -> id by adjacent inversion reductions
    for s in all_sigmas:
        cur = s
        while cur != id_s:
            arr = list(cur)
            moved = False
            for p in range(k - 1):
                if arr[p] > arr[p + 1]:
                    arr[p], arr[p + 1] = arr[p + 1], arr[p]
                    nxt = tuple(arr)
                    assert nxt in legal_next(cur), f"Illegal step {cur} -> {nxt}"
                    cur = nxt
                    moved = True
                    break
            assert moved

    # 2. id -> omega_0 by explicit induction in Lemma 4
    cur = id_s
    for r in range(k - 1, 0, -1):
        expected = tuple(range(1, r + 1)) + tuple(range(k, r, -1)) + (k + 1,)
        assert cur == expected, f"Expected {expected}, got {cur}"
        # r left cyclic rotations
        for _ in range(r):
            nxt = cur[1:k] + (cur[0], k + 1)
            assert nxt in legal_next(cur), f"Illegal rotation {cur} -> {nxt}"
            cur = nxt
        # Move 1, 2, ..., r-1 left past k, ..., r+1
        for val in range(1, r):
            pos = cur.index(val)
            while pos > val - 1:
                arr = list(cur)
                assert arr[pos - 1] > arr[pos]
                arr[pos - 1], arr[pos] = arr[pos], arr[pos - 1]
                nxt = tuple(arr)
                assert nxt in legal_next(cur), f"Illegal slide {cur} -> {nxt}"
                cur = nxt
                pos -= 1
    assert cur == w0_s, f"Failed to reach w0: got {cur}"

    # 3. omega_0 -> tau for every tau
    for tau in all_sigmas:
        cur = w0_s
        for p in range(k):
            val = tau[p]
            pos = cur.index(val)
            while pos > p:
                arr = list(cur)
                assert arr[pos - 1] > arr[pos]
                arr[pos - 1], arr[pos] = arr[pos], arr[pos - 1]
                nxt = tuple(arr)
                assert nxt in legal_next(cur), f"Illegal w0->tau step {cur} -> {nxt}"
                cur = nxt
                pos -= 1
        assert cur == tau


def verify_k(k):
    # Max partition size needed:
    # - For transitions from R_k: N_k + 1 where N_k = sum_{i=1}^{k-1} i*(k-i)
    # - For k-rectangle check on all mu in R_k: up to N_k + max_i |square_i|
    #   (for k<=4 check ALL mu in R_k x all i; for k=5 check all mu+square_i appearing in transitions plus all |mu|+|sq| <= 24)
    N_k = sum(i * (k - i) for i in range(1, k))
    max_sq = max(i * (k - i + 1) for i in range(1, k + 1))
    max_n = N_k + max_sq if k <= 4 else max(N_k + 1, 22)

    dk = compute_dk_strong(max_n, k)

    # Enumerate all states in R_k
    states = []
    def gen_rk(idx, cur):
        if idx == k:
            states.append(counts_to_part(cur))
            return
        for v in range(k - idx):
            gen_rk(idx + 1, cur + [v])
    gen_rk(0, [])
    assert len(states) == factorial(k)
    st_idx = {lam: idx for idx, lam in enumerate(states)}

    # 1. Verify Lemma 2 (Maya diagram bijection, cyclic-arc formula, complement = reversal)
    lam_to_sigma = {}
    sigma_to_lam = {}
    for lam in states:
        kap = bounded_to_core(lam, k)
        assert core_to_bounded(kap, k) == lam, f"p(c({lam})) != {lam}"
        _, sig = maya_minima_and_sigma(kap, k)
        assert alpha_from_sigma(sig, k) == lam, f"alpha(sigma({lam})) != {lam}"
        lam_to_sigma[lam] = sig
        sigma_to_lam[sig] = lam
    assert len(sigma_to_lam) == factorial(k)

    for lam in states:
        sig = lam_to_sigma[lam]
        assert alpha_from_sigma(sigma_rev(sig), k) == comp_part(lam, k), (
            f"Reversal mismatch for k={k}, lam={lam}"
        )

    # 2. Verify Lemma 1(2) (k-rectangle dimension identity) on all mu in R_k with |mu|+|sq_i| <= max_n
    rect_checked = 0
    for mu in states:
        for i in range(1, k + 1):
            sq = (i,) * (k - i + 1)
            mu_sq = tuple(sorted(mu + sq, reverse=True))
            if sum(mu_sq) <= max_n:
                lhs = Fraction(dk[mu_sq], factorial(sum(mu_sq)))
                rhs = Fraction(hook_dim(sq), factorial(sum(sq))) * Fraction(dk[mu], factorial(sum(mu)))
                assert lhs == rhs, f"Rectangle identity failed for k={k}, mu={mu}, i={i}"
                rect_checked += 1

    # 3. Verify Lemma 3 (weak covers <-> TASEP swaps, drops iff j=i+1, distinctness for k>=3)
    #    and build exact transition matrix P
    n_st = len(states)
    P = [[Fraction(0) for _ in range(n_st)] for _ in range(n_st)]
    for u, lam in enumerate(states):
        kap = bounded_to_core(lam, k)
        sig = lam_to_sigma[lam]
        covers = weak_covers_from_core(kap, k)
        swaps = tasep_swaps(sig, k)
        assert len(covers) == len(swaps), f"Cover count mismatch at k={k}, lam={lam}"

        # Match each weak cover with its exact TASEP swap
        cover_by_tau_sig = {}
        for _, tau_core, Lam in covers:
            assert sum(Lam) == sum(lam) + 1
            _, tau_sig = maya_minima_and_sigma(tau_core, k)
            cover_by_tau_sig.setdefault(tau_sig, []).append(Lam)

        swap_by_tau_sig = {}
        for j, i, tau_sig in swaps:
            swap_by_tau_sig.setdefault(tau_sig, []).append((j, i))

        assert set(cover_by_tau_sig.keys()) == set(swap_by_tau_sig.keys())
        seen_mu = set()
        row_sum = Fraction(0)
        for tau_sig, Lams in cover_by_tau_sig.items():
            swap_list = swap_by_tau_sig[tau_sig]
            assert len(Lams) == len(swap_list)
            mu = sigma_to_lam[tau_sig]
            for Lam in Lams:
                assert red_k(Lam, k) == mu
                # Check drop iff j = i+1
                if Lam == mu:
                    assert any(j >= i + 2 for j, i in swap_list)
                else:
                    matched = False
                    for j, i in swap_list:
                        if j == i + 1:
                            sq = (i,) * (k - i + 1)
                            if Lam == tuple(sorted(mu + sq, reverse=True)):
                                matched = True
                                # Also check k-rectangle identity for this transition
                                lhs = Fraction(dk[Lam], factorial(sum(Lam)))
                                rhs = Fraction(hook_dim(sq), factorial(sum(sq))) * Fraction(dk[mu], factorial(sum(mu)))
                                assert lhs == rhs
                    assert matched, f"Rectangle drop mismatch for k={k}, lam={lam}, Lam={Lam}"
                prob = Fraction(dk[Lam], (sum(lam) + 1) * dk[lam])
                assert prob > 0
                P[u][st_idx[mu]] += prob
                row_sum += prob
                if k >= 3:
                    assert mu not in seen_mu, f"Multi-edge found for k={k} >= 3 at {lam} -> {mu}"
                seen_mu.add(mu)
        assert row_sum == 1, f"Row sum != 1 at k={k}, lam={lam}: {row_sum}"

    # 4. Verify Lemma 4 (constructive irreducibility paths)
    verify_irreducibility_paths(k, list(sigma_to_lam.keys()))

    # 5. Verify Theorem 1: exact R-reversibility, stationarity, uniqueness, and Conjecture 1
    w = []
    for lam in states:
        lc = comp_part(lam, k)
        w.append(Fraction(dk[lam] * dk[lc], factorial(sum(lam)) * factorial(sum(lc))))
    Z = sum(w)
    pi_formula = [val / Z for val in w]

    # Exact R-reversibility for ALL pairs (u, v)
    for u, lam in enumerate(states):
        ru = st_idx[comp_part(lam, k)]
        for v, mu in enumerate(states):
            rv = st_idx[comp_part(mu, k)]
            assert pi_formula[u] * P[u][v] == pi_formula[v] * P[rv][ru], (
                f"R-reversibility failed at k={k}, ({lam}, {mu})"
            )

    # Exact stationarity pi * P = pi
    for v in range(n_st):
        lhs = sum(pi_formula[u] * P[u][v] for u in range(n_st))
        assert lhs == pi_formula[v], f"Stationarity failed at k={k}, v={v}"

    # Verify uniqueness (nullspace of P^T - I has dimension 1) and exact match via SymPy
    if k <= 4:
        M = sp.Matrix(n_st, n_st, lambda r, c: sp.Rational(P[c][r].numerator, P[c][r].denominator) - (1 if r == c else 0))
        ns = M.nullspace()
        assert len(ns) == 1, f"Nullspace dimension != 1 for k={k}: {len(ns)}"
        vec = ns[0]
        s_vec = sum(vec)
        for u in range(n_st):
            val = vec[u] / s_vec
            assert Fraction(int(val.p), int(val.q)) == pi_formula[u]

    # Conjecture 1 check
    for u, lam in enumerate(states):
        ru = st_idx[comp_part(lam, k)]
        assert pi_formula[u] == pi_formula[ru]

    lcd = 1
    for p in pi_formula:
        lcd = lcm(lcd, p.denominator)
    print(
        f"k={k}: states={n_st}, rect_checks={rect_checked}, "
        f"Z_k={Z}, lcd={lcd}, pi(empty)={pi_formula[st_idx[()]]} -- OK"
    )


def main():
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(45)
    try:
        for k in range(1, 6):
            verify_k(k)
        print("PASS")
    except Exception as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
