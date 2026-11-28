"""Independent exact verifier for targets/radici-2609.07769-open (ZERO FLOATS)."""

from __future__ import annotations

import itertools
import math
import pathlib
import tarfile
from fractions import Fraction


def float_free_frac(x: Fraction, prec: int = 6) -> str:
    sign = "-" if x < 0 else ""
    ax = abs(x)
    scale = 10 ** prec
    scaled = (ax.numerator * scale) // ax.denominator
    ip = scaled // scale
    fp = scaled % scale
    return f"{sign}{ip}.{fp:0{prec}d}"


# ---------------------------------------------------------------------------
# 1. Finite fields F_q and exact GRM_q(d, n) linear algebra
# ---------------------------------------------------------------------------

def make_field(q: int):
    if q == 4:
        add = [[i ^ j for j in range(4)] for i in range(4)]
        mul = [
            [0, 0, 0, 0],
            [0, 1, 2, 3],
            [0, 2, 3, 1],
            [0, 3, 1, 2],
        ]
        inv = [0, 1, 3, 2]
        return add, mul, inv
    add = [[(i + j) % q for j in range(q)] for i in range(q)]
    mul = [[(i * j) % q for j in range(q)] for i in range(q)]
    inv = [0] + [pow(i, q - 2, q) for i in range(1, q)]
    return add, mul, inv


def rank_fq(rows: list[list[int]], ncols: int, q: int, field) -> int:
    _, mul, inv = field
    mat = [list(r) for r in rows]
    rk = 0
    for c in range(ncols):
        piv = -1
        for r in range(rk, len(mat)):
            if mat[r][c] != 0:
                piv = r
                break
        if piv == -1:
            continue
        mat[rk], mat[piv] = mat[piv], mat[rk]
        inv_p = inv[mat[rk][c]]
        piv_row = mat[rk]
        for j in range(c, ncols):
            piv_row[j] = mul[piv_row[j]][inv_p]
        for r in range(rk + 1, len(mat)):
            factor = mat[r][c]
            if factor != 0:
                row = mat[r]
                for j in range(c, ncols):
                    sub = mul[factor][piv_row[j]]
                    if q == 4:
                        row[j] ^= sub
                    else:
                        row[j] = (row[j] - sub) % q
        rk += 1
    return rk


def reduced_monomials(n: int, q: int, d: int) -> list[tuple[int, ...]]:
    return [exps for exps in itertools.product(range(q), repeat=n) if sum(exps) <= d]


def eval_matrix(n: int, q: int, d: int, field) -> tuple[list[tuple[int, ...]], list[list[int]]]:
    _, mul, _ = field
    pts = list(itertools.product(range(q), repeat=n))
    mons = reduced_monomials(n, q, d)
    pows = [[1] for _ in range(q)]
    for x in range(q):
        for _ in range(1, q):
            pows[x].append(mul[pows[x][-1]][x])
    rows = []
    for pt in pts:
        row = []
        for exps in mons:
            val = 1
            for coord, e in zip(pt, exps):
                val = mul[val][pows[coord][e]]
            row.append(val)
        rows.append(row)
    return pts, rows


# ---------------------------------------------------------------------------
# 2. Exact base cases n = 2 for q in {3, 4, 5}, 2 <= d <= 2(q - 1)
# ---------------------------------------------------------------------------

def verify_base_n2_q3_q4() -> None:
    for q in (3, 4):
        field = make_field(q)
        N = q * q
        for d in range(2, 2 * (q - 1) + 1):
            _, rows = eval_matrix(2, q, d, field)
            D = len(rows[0])
            # Enumerate all 2^N subsets (exact bitmask rank via incremental Gaussian elimination)
            chi_m = 0
            chi_c = 0
            for mask in range(1 << N):
                sub = [rows[i] for i in range(N) if (mask >> i) & 1]
                rk = rank_fq(sub, D, q, field)
                sgn = -1 if (mask.bit_count() & 1) else 1
                chi_m += sgn * (N ** (D - rk))
                if not (mask & 1):
                    rk0 = rank_fq([rows[0]] + sub, D, q, field)
                    chi_c += sgn * (N ** (D - rk0))
            alpha0 = chi_m
            alpha1 = N * chi_c
            assert alpha1 > alpha0, f"n=2 failed for q={q}, d={d}: alpha1={alpha1} <= alpha0={alpha0}"
            if d == 2:
                if q == 3:
                    assert (alpha0, alpha1) == (184184, 206712)
                else:
                    assert (alpha0, alpha1) == (6012645, 6242400)
            print(f"BASE_N2 (q={q}, d={d}): alpha_0={alpha0} < alpha_1={alpha1}")


def agl2_f5_orbits_up_to_12() -> list[tuple[int, int]]:
    """
    Enumerate ALL AGL_2(F_5) orbits of subsets S subset F_5^2 of size 0 <= k <= 12.
    Returns list of (rep_mask, orbit_size).
    """
    pts = [(x, y) for x in range(5) for y in range(5)]
    pt_idx = {p: i for i, p in enumerate(pts)}

    # Precompute all 12,000 affine maps sending (0,0),(1,0),(0,1) -> non-collinear triple (a,b,c)
    triple_maps: dict[tuple[int, int, int], list[int]] = {}
    for a in range(25):
        ax, ay = pts[a]
        for b in range(25):
            if b == a:
                continue
            bx, by = pts[b]
            ux, uy = (bx - ax) % 5, (by - ay) % 5
            for c in range(25):
                cx, cy = pts[c]
                vx, vy = (cx - ax) % 5, (cy - ay) % 5
                if (ux * vy - uy * vx) % 5 == 0:
                    continue
                perm = [0] * 25
                for idx, (x, y) in enumerate(pts):
                    nx = (ax + ux * x + vx * y) % 5
                    ny = (ay + uy * x + vy * y) % 5
                    perm[idx] = pt_idx[(nx, ny)]
                triple_maps[(a, b, c)] = perm

    # Also precompute the 30 lines as bitmasks for fast collinearity check
    line_masks: list[int] = []
    seen_l = set()
    for a in range(25):
        ax, ay = pts[a]
        for b in range(a + 1, 25):
            dx, dy = (pts[b][0] - ax) % 5, (pts[b][1] - ay) % 5
            lm = 0
            for t in range(5):
                lm |= 1 << pt_idx[((ax + t * dx) % 5, (ay + t * dy) % 5)]
            if lm not in seen_l:
                seen_l.add(lm)
                line_masks.append(lm)
    assert len(line_masks) == 30

    # For fast canonicalization of a mask containing a non-collinear triple:
    # Sort vertices by (sum over lines containing v of |line \cap S|, etc.), pick top vertex a,
    # Wait: even simpler! To guarantee deterministic canonical rep without missing symmetries,
    # we compute the minimum image over ALL `perm` that send the MINIMUM-degree-pair triple?
    # Wait: we can score every point v in S by tuple (sorted counts of other points on each of the 6 lines through v),
    # take the points with the lexicographically SMALLEST (or rarest) signature,
    # then for each triple (a,b,c) with a in min-tier, b in min-tier-for-pairs, c non-collinear, invert!
    # Even simpler and 100% bug-proof: given ANY S with a non-collinear triple,
    # pick ONLY triples (a,b,c) where a achieves the minimum point-signature among S,
    # b achieves the minimum point-signature among S\{a}, and c achieves the minimum
    # point-signature among S \ line(a,b)! Wait: if S is symmetric (say 12 pts, all same sig),
    # there could still be many triples; how many symmetries can S have? At most ~24..120,
    # and we only need ONE canonical rep per orbit! Wait: to compare against known orbits,
    # taking min over ALL valid (a,b,c) in the invariant-minimal tier IS 100% invariant-exact!
    pt_lines = [[] for _ in range(25)]
    for lm in line_masks:
        for v in range(25):
            if (lm >> v) & 1:
                pt_lines[v].append(lm)

    # Precompute collinearity lookup for triples
    collinear_pair_line = [[0] * 25 for _ in range(25)]
    for lm in line_masks:
        vs = [v for v in range(25) if (lm >> v) & 1]
        for u in vs:
            for v in vs:
                if u != v:
                    collinear_pair_line[u][v] = lm

    def apply_inv_map(mask: int, a: int, b: int, c: int) -> int:
        # triple_maps[(a,b,c)] maps canonical -> mask! Wait: we want the inverse map sending (a,b,c) -> (0,1,5)
        # Better: precompute inv_perm for each (a,b,c)!
        pass

    # Precompute inverse permutations sending (a,b,c) -> (0=(0,0), 5=(1,0), 1=(0,1))
    # Notice in triple_maps above, (0,0)=0, (1,0)=5, (0,1)=1!
    inv_triple_maps: dict[tuple[int, int, int], list[int]] = {}
    for key, perm in triple_maps.items():
        inv_p = [0] * 25
        for src, dst in enumerate(perm):
            inv_p[dst] = src
        inv_triple_maps[key] = inv_p

    def canonical_noncollinear(mask: int) -> int:
        vs = [v for v in range(25) if (mask >> v) & 1]
        sigs = {}
        for v in vs:
            counts = sorted(((lm & mask).bit_count() for lm in pt_lines[v]), reverse=True)
            sigs[v] = tuple(counts)
        min_sig = min(sigs.values())
        a_cands = [v for v in vs if sigs[v] == min_sig]
        best = (1 << 26)
        for a in a_cands:
            rem1 = [v for v in vs if v != a]
            # Refine b by pair line size + sig
            b_scores = {
                v: (sigs[v], (collinear_pair_line[a][v] & mask).bit_count())
                for v in rem1
            }
            min_bs = min(b_scores.values())
            b_cands = [v for v in rem1 if b_scores[v] == min_bs]
            for b in b_cands:
                ab_line = collinear_pair_line[a][b]
                rem2 = [v for v in vs if not ((ab_line >> v) & 1)]
                if not rem2:
                    continue
                c_scores = {
                    v: (
                        sigs[v],
                        (collinear_pair_line[a][v] & mask).bit_count(),
                        (collinear_pair_line[b][v] & mask).bit_count(),
                    )
                    for v in rem2
                }
                min_cs = min(c_scores.values())
                for c in rem2:
                    if c_scores[c] != min_cs:
                        continue
                    inv_p = inv_triple_maps[(a, b, c)]
                    new_m = 0
                    for v in vs:
                        new_m |= 1 << inv_p[v]
                    if new_m < best:
                        best = new_m
        assert best < (1 << 26)
        return best

    # Collinear orbits of size k <= 5 are trivial: one orbit per size k!
    all_orbits: list[tuple[int, int]] = []
    # k = 0, 1, 2
    all_orbits.append((0, 1))
    all_orbits.append((1 << 0, 25))
    all_orbits.append(((1 << 0) | (1 << 1), 300))

    # For k = 3..12, maintain collinear orbit (if k <= 5) + non-collinear orbits
    #Wait: we compute exact orbit size from generator transitions? Better:
    # From each orbit (rep, size) at level k-1, each extension x in V\S gives a weighted edge of weight size/k!
    # Wait: summing weight size(S') over incoming transitions and dividing by k gives exact size(S)!
    # Let's verify sum of orbit sizes at every level k equals C(25, k)!
    #Wait: at level k=2, rep = {(0,0),(0,1)} has size 300.
    cur_level: dict[int, int] = {(1 << 0) | (1 << 1): 300}
    line0 = line_masks[0]  # line {(0,0),(0,1),(0,2),(0,3),(0,4)} = {0,1,2,3,4}

    for k in range(3, 13):
        next_weights: dict[int, int] = {}
        for rep, orb_sz in cur_level.items():
            for x in range(25):
                if (rep >> x) & 1:
                    continue
                cand = rep | (1 << x)
                # Check if cand is collinear (all points in a single line)
                is_col = False
                if k <= 5:
                    for lm in line_masks:
                        if (cand & lm) == cand:
                            is_col = True
                            break
                if is_col:
                    # Canonical collinear rep: first k points of line0 (indices 0..k-1)
                    canon = (1 << k) - 1
                else:
                    canon = canonical_noncollinear(cand)
                next_weights[canon] = next_weights.get(canon, 0) + orb_sz
        cur_level = {}
        tot = 0
        for canon, wsum in next_weights.items():
            assert wsum % k == 0
            osz = wsum // k
            cur_level[canon] = osz
            tot += osz
            all_orbits.append((canon, osz))
        assert tot == math.comb(25, k), f"Orbit size sum mismatch at k={k}: {tot} != {math.comb(25, k)}"
    return all_orbits


def verify_base_n2_q5() -> None:
    q = 5
    N = 25
    field = make_field(q)
    orbits = agl2_f5_orbits_up_to_12()
    all_mask = (1 << N) - 1
    for d in range(2, 9):
        _, rows = eval_matrix(2, q, d, field)
        D = len(rows[0])
        if d == 8:
            # Boundary d = 2*(5-1) = 8: coloop case
            alpha0 = (N - 1) ** N
            alpha1 = N * ((N - 1) ** (N - 1))
            assert alpha1 > alpha0
            print(f"BASE_N2 (q=5, d=8): coloop alpha_1 - alpha_0 = {(N-1)**(N-1)} > 0")
            continue
        chi_m = 0
        chi_c = 0
        for rep, osz in orbits:
            k = rep.bit_count()
            # 1. Evaluate rep (size k <= 12)
            sub = [rows[i] for i in range(N) if (rep >> i) & 1]
            rk = rank_fq(sub, D, q, field)
            sgn = -1 if (k & 1) else 1
            chi_m += sgn * osz * (N ** (D - rk))
            # Contribution of sets of size k containing 0:
            # By AGL_2(F_5) transitivity, fraction k/N of the orbit contains 0!
            # Wait: for chi_c = sum_{T subset V\{0}} (-1)^|T| N^{D - r(T \cup {0})},
            # put S = T \cup {0} (|S| = k >= 1, |T| = k-1). Then (-1)^|T| = -(-1)^|S| = -sgn!
            if k >= 1:
                assert (osz * k) % N == 0
                cnt_0 = (osz * k) // N
                chi_c += (-sgn) * cnt_0 * (N ** (D - rk))

            # 2. Evaluate complement V \ rep (size 25 - k >= 13)
            comp = all_mask ^ rep
            kc = N - k
            sub_c = [rows[i] for i in range(N) if (comp >> i) & 1]
            rk_c = rank_fq(sub_c, D, q, field)
            sgn_c = -1 if (kc & 1) else 1
            chi_m += sgn_c * osz * (N ** (D - rk_c))
            assert (osz * kc) % N == 0
            cnt_c0 = (osz * kc) // N
            chi_c += (-sgn_c) * cnt_c0 * (N ** (D - rk_c))

        alpha0 = chi_m
        alpha1 = N * chi_c
        assert alpha1 > alpha0, f"n=2 q=5 failed for d={d}: alpha1={alpha1} <= alpha0={alpha0}"
        if d == 2:
            assert (alpha0, alpha1) == (88849944, 88998000)
        print(f"BASE_N2 (q=5, d={d}): alpha_0={alpha0} < alpha_1={alpha1}")


# ---------------------------------------------------------------------------
# 3. Exact Rational Lemma 5 & Monotone Error / Margin Bounds (Cases 2-6)
# ---------------------------------------------------------------------------

def exp_rational_upper(x: Fraction, terms: int = 24) -> Fraction:
    """Exact rational upper bound on exp(x) for 0 <= x <= 6 using Taylor remainder <= x^m/m! * 1/(1 - x/(m+1))."""
    assert 0 <= x <= 10
    s = Fraction(1)
    term = Fraction(1)
    for k in range(1, terms):
        term = term * x / k
        s += term
    last = term * x / terms
    rem = last * Fraction(terms + 1, terms + 1 - x)
    return s + rem


def macwilliams_moments(q: int, N: int, max_m: int = 8) -> tuple[list[list[Fraction]], dict[tuple[int, int], Fraction]]:
    """
    Compute exact E_{u in F_q^N}[Y^r] for r=0..max_m and exact polynomial coefficients
    alpha_{r, w} of A_w(C) in E_{c in C^perp}[Y^r].
    Recall: W_C(1, x) = |C^perp|^{-1} sum_{c in C^perp} (1+(q-1)x)^{N-wt(c)} (1-x)^{wt(c)} = sum_w A_w(C) x^w.
    On the other hand, wt(c) = (q-1)N/q * (1 - Y_c).
    And on F_q^N, Y = (1/N) sum_{i=1}^N Z_i where Z_i = 1 (prob 1/q) or -1/(q-1) (prob (q-1)/q)!
    Notice Z_i in F_q^N has E[Z_i^m] = (1 + (q-1) * (-1/(q-1))^m) / q!
    Wait: for exact MacWilliams coefficients alpha_{r,w} of A_w(C) in E[Y^r]:
    Since (1 + (q-1)x)^N ( (1-x)/(1+(q-1)x) )^{wt(c)} = ...
    Write x = (e^t - 1) / (1 + (q-1) e^t)? Wait: even simpler!
    In Krawtchouk / exponential generating function:
    Take u = t / N:
    Let g(x) := (1 + (q-1)x) / (1 - x) => ln g(x) = q x + O(x^2).
    Actually, directly invert by expanding (1 + (q-1)x)^{N-w} (1-x)^w? No, in E_{c in C^perp}[Y_c^r]:
    Notice for ANY linear code C, E_{c in C^perp}[exp(t * Y_c)] is determined by W_C(1, x):
    Let (1 - x) / (1 + (q-1) x) = exp(-q t / ((q-1) N)), i.e.:
    Set z := exp(-q t / ((q-1) N)). Then (1-x)/(1+(q-1)x) = z => x = (1 - z) / (1 + (q-1) z)!
    Then:
      (1 + (q-1)x)^N * z^{wt(c)} = (q / (1 + (q-1) z))^N * exp(-t + t * Y_c) !
    Wait: check that!!
    wt(c) = (q-1)N/q * (1 - Y_c) => z^{wt(c)} = exp(-t(1 - Y_c)) = e^{-t} e^{t Y_c}!
    And 1 + (q-1)x = 1 + (q-1)(1-z)/(1+(q-1)z) = q / (1 + (q-1)z)!
    THEREFORE, as formal power series in t:
    E_{c in C^perp}[e^{t Y_c}] = e^t * ((1 + (q-1) z) / q)^N * W_C(1, (1-z)/(1+(q-1)z))!
    Wait: checking coefficients of t^r * r! gives E_{c in C^perp}[Y_c^r] EXACTLY as a linear combination of A_w(C)!!
    Let's compute BOTH:
    1) E_{F_q^N}[Y^r] (setting A_0=1, all A_w=0 for w>=1), AND
    2) alpha_{r, w} for w = 1..max_m!
    """
    # Compute power series in t up to degree max_m
    def mul_poly(p1: list[Fraction], p2: list[Fraction]) -> list[Fraction]:
        out = [Fraction(0)] * (max_m + 1)
        for i, a in enumerate(p1):
            if a == 0:
                continue
            for j, b in enumerate(p2):
                if i + j <= max_m:
                    out[i + j] += a * b
        return out

    def exp_series(coeff_t: Fraction) -> list[Fraction]:
        # exp(coeff_t * t) truncated to max_m
        s = [Fraction(0)] * (max_m + 1)
        pw = Fraction(1)
        fact = 1
        for k in range(max_m + 1):
            if k > 0:
                pw *= coeff_t
                fact *= k
            s[k] = pw / fact
        return s

    def pow_poly(p: list[Fraction], k: int) -> list[Fraction]:
        res = [Fraction(0)] * (max_m + 1)
        res[0] = Fraction(1)
        base = p
        exp = k
        while exp > 0:
            if exp & 1:
                res = mul_poly(res, base)
            exp >>= 1
            if exp:
                base = mul_poly(base, base)
        return res

    # z(t) = exp(-q / ((q-1)*N) * t)
    z = exp_series(Fraction(-q, (q - 1) * N))
    # num = 1 - z, den = 1 + (q-1) z
    num = [Fraction(1 if k == 0 else 0) - z[k] for k in range(max_m + 1)]
    den = [Fraction(1 if k == 0 else 0) + (q - 1) * z[k] for k in range(max_m + 1)]
    # den / q:
    den_over_q = [c / q for c in den]
    # Invert den_over_q = 1 + eps (since z[0]=1 => den[0]=q => den_over_q[0]=1!):
    inv_den_q = [Fraction(0)] * (max_m + 1)
    inv_den_q[0] = Fraction(1)
    for k in range(1, max_m + 1):
        val = Fraction(0)
        for j in range(1, k + 1):
            val -= den_over_q[j] * inv_den_q[k - j]
        inv_den_q[k] = val
    # x(t) = (1 - z) / (q * den_over_q) = (num / q) * inv_den_q
    x_t = mul_poly([c / q for c in num], inv_den_q)
    # prefactor = e^t * (den_over_q)^N
    et = exp_series(Fraction(1))
    pref = mul_poly(et, pow_poly(den_over_q, N))

    # For w = 0..max_m: series for A_w contribution is pref * x(t)^w!
    alpha: dict[tuple[int, int], Fraction] = {}
    facts = [math.factorial(r) for r in range(max_m + 1)]
    for w in range(max_m + 1):
        ser = mul_poly(pref, pow_poly(x_t, w))
        for r in range(max_m + 1):
            alpha[(r, w)] = ser[r] * facts[r]
    return alpha


def monotone_moment_poly_bound(q: int, N: int, M: int) -> Fraction:
    """
    Exact rational upper bound from PROOF.md Lemma 5(3):
    Write Y = (1/N) sum Z_i on F_q^N.
    For each integer partition of M into parts >= 2 (since E[Z_i]=0!),
    compute count of ordered k-tuples of distinct indices * prod E[Z_1^{r_j}],
    Wait: Lemma 5(3) replaces N(N-1)...(N-k+1) by N^k in N^{M/2} E[Y^M], giving a polynomial in 1/N
    with positive coefficients? Wait: N(N-1)...(N-k+1) / N^{M/2} = N^{k - M/2} * prod_{j=0}^{k-1}(1 - j/N) <= N^{k - M/2}!
    Since M is even and every part >= 2, k <= M/2, so N^{k - M/2} = N^{-(M/2 - k)} IS a negative power of N!
    """
    # Generate all partitions of M into parts >= 2
    def partitions(rem: int, min_p: int):
        if rem == 0:
            yield ()
            return
        for p in range(min_p, rem + 1):
            for rest in partitions(rem - p, p):
                yield (p,) + rest

    # E[Z^r] = (1 + (q-1) * (-1/(q-1))^r) / q
    def ez(r: int) -> Fraction:
        return (Fraction(1) + Fraction(q - 1) * (Fraction(-1, q - 1) ** r)) / q

    bound_scaled = Fraction(0)  # upper bound on N^{M/2} E[Y^M]
    for part in partitions(M, 2):
        # Number of set partitions of {1..M} with block sizes `part`:
        # M! / (prod r_j! * prod (mult_m!))
        mults: dict[int, int] = {}
        denom = 1
        for r in part:
            mults[r] = mults.get(r, 0) + 1
            denom *= math.factorial(r)
        for c in mults.values():
            denom *= math.factorial(c)
        ways = math.factorial(M) // denom
        prod_ez = Fraction(1)
        for r in part:
            prod_ez *= ez(r)
        assert prod_ez > 0
        k = len(part)
        # Replacing N(N-1)...(N-k+1) by N^k gives ways * prod_ez * N^{k - M//2}
        bound_scaled += ways * prod_ez * (Fraction(1, N) ** (M // 2 - k))
    return bound_scaled / (Fraction(N) ** (M // 2))


def verify_lemma5_and_cases2_to_6() -> list[str]:
    failures: list[str] = []

    # First check Lemma 5(4) coefficients on q in {3, 4, 5}
    for q in (3, 4, 5):
        N = q ** 3
        alpha = macwilliams_moments(q, N, 6)
        assert alpha[(4, 4)] == Fraction(24, ((q - 1) ** 4) * (N ** 4))
        assert alpha[(5, 5)] == Fraction(120, ((q - 1) ** 5) * (N ** 5))
        assert alpha[(6, 6)] == Fraction(720, ((q - 1) ** 6) * (N ** 6))
        assert alpha[(5, 4)] == Fraction(240 * (q - 2), ((q - 1) ** 5) * (N ** 5))
        for r in range(1, 7):
            for w in range(r + 1, 7):
                assert alpha[(r, w)] == 0

        # Check c_4 * alpha_{4,4}, c_5 * alpha_{5,5}, c_5 * alpha_{5,4} with lambda_q <= q-1, kappa_q <= 1
        # f_q(Y) = kappa_q (q-1)(NY - 1) sum_{m>=0} (lambda_q Y)^m / m!
        # Coeff c_r of Y^r in f_q(Y):
        # kappa_q (q-1) [ N * lambda_q^{r-1}/(r-1)! - lambda_q^r / r! ] <= (q-1) * N * (q-1)^{r-1} / (r-1)!?
        # Wait: since lambda_q <= q-1 and kappa_q <= 1, is c_r <= N (q-1)^r / (r-1)! ?
        # YES! Wait: if N >= q-1 (here N >= 27), is (q-1)^r * [N/(r-1)! - (q-1)/r!] increasing in lambda_q?
        # Derivative wrt lambda_q of (N lambda^{r-1}/(r-1)! - lambda^r/r!) = N lambda^{r-2}/(r-2)! - lambda^{r-1}/(r-1)!
        # = lambda^{r-2}/(r-2)! * (N - lambda/(r-1)) > 0 since lambda <= q-1 <= 4 < 27 <= N!
        # So c_r <= (q-1) * [N (q-1)^{r-1}/(r-1)! - (q-1)^r/r!] <= N (q-1)^r / (r-1)!
        c4_ub = Fraction(N * ((q - 1) ** 4), math.factorial(3))
        c5_ub = Fraction(N * ((q - 1) ** 5), math.factorial(4))
        assert c4_ub * alpha[(4, 4)] == Fraction(4, N ** 3)
        assert c5_ub * alpha[(5, 5)] == Fraction(5, N ** 4)
        assert c5_ub * alpha[(5, 4)] == Fraction(10 * (q - 2), N ** 4)
    print("LEMMA5_COEFFS: Exact MacWilliams moment coefficients & c4/c5 bounds verified")

    # Compute exact polynomial-bound error term at N_0 for each case in PROOF.md Section 4
    def eval_taylor_error_monotone(q: int, N: int, D: int, M: int, y_max: Fraction, extra_codewords_term: Fraction = Fraction(0)) -> Fraction:
        """
        True Lemma 5(2) monotone error bound:
        - N/(q-1) * f_q(1)/q^D <= N^2 * e^{q-1} / q^D  (NO /(q-1)!)
        - N/(q-1) * f_q^{(M)}(Y_max) <= e^{(q-1)Y_max} * (q-1)^{M-1} * ((q-1)Y_max + M) * N^2
        """
        e_q1 = exp_rational_upper(Fraction(q - 1))
        e_qy = exp_rational_upper((q - 1) * y_max)
        zero_cw_term = Fraction(N * N) * e_q1 / (Fraction(q) ** D)
        fq_M_scaled = e_qy * ((q - 1) ** (M - 1)) * ((q - 1) * y_max + M) * (N * N)
        ey_m = monotone_moment_poly_bound(q, N, M) + extra_codewords_term
        rem_term = fq_M_scaled / math.factorial(M) * ey_m
        return zero_cw_term + rem_term

    def eval_taylor_error_exact_m6(
        q: int, N: int, D: int, y_max: Fraction, a4: int, a5: int, a6: int
    ) -> Fraction:
        """
        Exact-coefficient (lambda_q, kappa_q, c_4, c_5, E[Y^6]) error bound for M = 6:
        used for Case 5 (q=4,d=2,n=3) and Case 6 (q=5,d=2,n=4).
        """
        # ln((N+q-1)/(N-1)): z = q / (2N + q - 2)
        z = Fraction(q, 2 * N + q - 2)
        ln_lb = Fraction(0)
        for k in range(1, 13, 2):
            ln_lb += Fraction(2) * (z ** k) / k
        ln_ub = ln_lb + Fraction(2) * (z ** 13) / 13 / (1 - z * z)
        lam_lb = Fraction((q - 1) * N, q) * ln_lb
        lam_ub = Fraction((q - 1) * N, q) * ln_ub
        # kappa_q = N/(N-1) * (1 + (q-1)/N)^{N-1} * e^{-lam_q}
        e_lam_lb = Fraction(1)
        tk = Fraction(1)
        for k in range(1, 22):
            tk = tk * lam_lb / k
            e_lam_lb += tk
        kap_ub = Fraction(N, N - 1) * (Fraction(N + q - 1, N) ** (N - 1)) / e_lam_lb
        assert kap_ub <= 1

        e_lam_ub = exp_rational_upper(lam_ub, terms=24)
        e_ly_ub = exp_rational_upper(lam_ub * y_max, terms=24)
        # c=0 term: N/(q-1) * f_q(1)/q^D = kap_q * e^{lam_q} * N(N-1) / q^D
        zero_cw = kap_ub * e_lam_ub * N * (N - 1) / (Fraction(q) ** D)
        # f_q^{(6)}(Y_max) * N/(q-1) = kap_q * N * lam_q^5 * (lam_q(N Y_max - 1) + 6N) * e^{lam_q Y_max}
        fq6_scaled = kap_ub * N * (lam_ub ** 5) * (lam_ub * (N * y_max - 1) + 6 * N) * e_ly_ub
        # Exact E_{F_q^N}[Y^6] via MacWilliams at A_w = 0, plus A_4, A_5, A_6
        al = macwilliams_moments(q, N, 6)
        ey6 = al[(6, 0)] + al[(6, 4)] * a4 + al[(6, 5)] * a5 + al[(6, 6)] * a6 - Fraction(1, q ** D)
        rem_6 = fq6_scaled / math.factorial(6) * ey6

        # Exact P_5 excess: N/(q-1) * sum_{w in {4,5}} A_w * (sum_{r=w}^5 c_r alpha_{r,w} - w N^{-(w-1)})
        # Note c_r = kap_q * (q-1) * (N lam^{r-1}/(r-1)! - lam^r / r!)
        # For r=4,5, let's upper-bound using kap_ub, lam_ub/lam_lb cleanly:
        c4_ub = kap_ub * (q - 1) * (N * (lam_ub ** 3) / 6 - (lam_lb ** 4) / 24)
        c5_ub = kap_ub * (q - 1) * (N * (lam_ub ** 4) / 24 - (lam_lb ** 5) / 120)
        ex4 = c4_ub * al[(4, 4)] + c5_ub * al[(5, 4)] - Fraction(4, N ** 3)
        ex5 = c5_ub * al[(5, 5)] - Fraction(5, N ** 4)
        p5_ex = Fraction(N, q - 1) * (
            (a4 * ex4 if ex4 > 0 else Fraction(0))
            + (a5 * ex5 if ex5 > 0 else Fraction(0))
        )
        return zero_cw + rem_6 + p5_ex

    # Check S_0/N^{D-1} at N = 27, 64, 125
    for N0 in (27, 64, 125):
        s0 = (
            Fraction(1)
            - Fraction(N0 - 1, N0)
            + Fraction(math.comb(N0 - 1, 2), N0 ** 2)
            - Fraction(math.comb(N0 - 1, 3), N0 ** 3)
            + Fraction(4 * N0 + 5, 5 * (N0 ** 5)) * math.comb(N0 - 1, 4)
        )
        assert s0 >= Fraction(11, 30), f"S0({N0})={float_free_frac(s0)} < 11/30"

    # Case 2: Zero-codeword monotone regimes
    # D(q, d, n): dim Q_{q, d}. For q=3, d=3, n=3: C(3+3,3) - 3 = 20 - 3 = 17? Wait: max exponent q-1=2 -> 3 vars:
    # sum e_i <= 3 with e_i <= 2: all except x_i^3 (3 monomials) -> 20 - 3 = 17.
    # For q=4, d=3, n=3: all <=3, no e_i >= 4 -> C(6,3) = 20.
    # For q=5, d=4, n=3: all <=4 -> C(7,3) = 35.
    case2_specs = [
        ("q=3,d>=3", 3, 27, 17, 8, Fraction(1), Fraction(2498, 1000000)),
        ("q=4,d=3", 4, 64, 20, 6, Fraction(2, 3), Fraction(181919, 1000000)),
        ("q=4,d>=4", 4, 64, 35, 8, Fraction(1), Fraction(4285, 1000000)),
        ("q=5,d=4", 5, 125, 35, 8, Fraction(3, 4), Fraction(2594, 1000000)),
        ("q=5,d>=5", 5, 125, 56, 8, Fraction(1), Fraction(7692, 1000000)),
    ]
    for label, q, N0, D0, M, ym, claimed_ub in case2_specs:
        err = eval_taylor_error_monotone(q, N0, D0, M, ym)
        print(f"CASE2 ({label}, N0={N0}): error <= {float_free_frac(err)} (PROOF {float_free_frac(claimed_ub)})")
        assert err < Fraction(11, 30)

    # Case 3: q=3, d=2, n>=3 (M=6, Y_max=1/2, N0=27, D=10, A_6 <= N^3/18)
    err_c3 = eval_taylor_error_monotone(3, 27, 10, 6, Fraction(1, 2), extra_codewords_term=Fraction(5, 8 * (27 ** 3)))
    print(f"CASE3 (q=3,d=2,n>=3): error <= {float_free_frac(err_c3)} (PROOF 0.173529)")
    assert err_c3 < Fraction(11, 30)

    # Case 4: q=5, d=3, n>=3 (M=6, Y_max=1/2, N0=125, D=20, A_5 = N(N-1)/5)
    # WAIT: check broken 5-circuits in S_0(125)/N^{D-1}!
    # Exact S_0(125) when excluding broken 5-circuits (lines not through 0: (125-1)*120/20 = 744) and mu_4=31:
    sig4_q5d3 = math.comb(124, 4) - 31 - 744
    s0_q5d3 = (
        Fraction(1)
        - Fraction(124, 125)
        + Fraction(math.comb(124, 2), 125 ** 2)
        - Fraction(math.comb(124, 3), 125 ** 3)
        + Fraction(4 * 125 + 5, 5 * (125 ** 5)) * sig4_q5d3
    )
    # Notice s0_q5d3 vs 11/30!
    alpha_125 = macwilliams_moments(5, 125, 6)
    a5_val = (125 * 124) // 5
    # In E[R_6], A_5 enters E[Y^6] via alpha_{6,5} * A_5! Wait: is alpha_{6,5} positive? Let's use exact alpha_{6,5}!
    extra_c4 = alpha_125[(6, 5)] * a5_val
    # And wait: what about P_5 excess for A_5? Remember PROOF.md L29 subtracted Phi_{>= 6}, so 5 A_5 / N^4 is NOT subtracted by Phi_{>= 6}?!
    # CHECK THAT CAREFULLY!!
    # In L96, PROOF.md computed c_5 * alpha_{5,5} <= 5 / N^4 (from - 5 A_5 / N^4)!
    # Wait: for q=5, d=3, L64 says: every 5-circuit has |P|=4 (EVEN!), so |P|=4 drops out of Phi_{>=6} (only odd |P| >= 5 enter Phi_{>=6}, which starts at w=6)!
    # Therefore in L82: E[f_5(Y_c)] = sum_{w >= 5} w A_w N^{-(w-1)}, so N/(q-1) * (E[f_5] - 5 A_5 / N^4) = N^2/(q-1) Phi_{>=6}!!
    # Subtracting 5 A_5 / N^4 cancels c_5 alpha_{5,5} A_5 <= 5 A_5 / N^4 (actually f_5^{(5)} > 0 => c_5 > 0, and c_5 alpha_{5,5} <= 5/N^4 => excess <= 0!)
    # So only alpha_{6,5} * A_5 enters R_6!
    assert alpha_125[(6, 5)] > 0
    err_c4 = eval_taylor_error_monotone(5, 125, 20, 6, Fraction(1, 2), extra_codewords_term=extra_c4)
    print(f"CASE4 (q=5,d=3,n>=3): S0_exact={float_free_frac(s0_q5d3)} vs 11/30={float_free_frac(Fraction(11,30))}, error <= {float_free_frac(err_c4)} (PROOF 0.165050)")
    assert err_c4 < s0_q5d3
    if s0_q5d3 < Fraction(11, 30):
        print(f"  NOTE: for q=5,d=3,n=3, true S0={float_free_frac(s0_q5d3)} slightly < 11/30 due to 744 broken 5-circuits!")

    # Case 5: q=4, d=2, n=3 (N=64, D=10) & n>=4 (N=256, D=15)
    # Exact sigma_3, sigma_4 for n=3: lines_0 = 21, lines_not_0 = 315.
    # For each P on a line L through 0 (|P|=3): sigma_1(P) = 60, sigma_2(P) = C(60,2), W(P) <= 1 - 60/64 + C(60,2)/64^2
    wp_ub_64 = Fraction(1) - Fraction(60, 64) + Fraction(math.comb(60, 2), 64 ** 2)
    loss_j3_64 = Fraction(21, 64) * wp_ub_64
    # Exact S0 for q=4, d=2, n=3 (recompute exact bad4 count = 20160? Wait: earlier exact_sig4=575505)
    # Wait: let's check both L32 S0 and true exact S0!
    field4 = make_field(4)
    pts4, _ = eval_matrix(3, 4, 2, field4)
    add4, mul4, _ = field4
    seen_l4 = set()
    for a in range(64):
        for b in range(a + 1, 64):
            diff = tuple(add4[pts4[b][c]][pts4[a][c]] for c in range(3))
            lp = tuple(sorted(pts4.index(tuple(add4[pts4[a][c]][mul4[t][diff[c]]] for c in range(3))) for t in range(4)))
            seen_l4.add(lp)
    bad3_4 = {(tuple(x for x in lp if x != 0) if 0 in lp else lp[1:]) for lp in seen_l4}
    bad4_4 = {tuple(sorted(b3 + (x,))) for b3 in bad3_4 for x in range(1, 64) if x not in b3}
    for lp in seen_l4:
        if 0 not in lp:
            bad4_4.add(lp)
    sig3_64 = math.comb(63, 3) - len(bad3_4)
    sig4_64 = math.comb(63, 4) - len(bad4_4)
    s0_64 = (
        Fraction(1) - Fraction(63, 64) + Fraction(math.comb(63, 2), 64 ** 2)
        - Fraction(sig3_64, 64 ** 3) + Fraction(4 * 64 + 5, 5 * (64 ** 5)) * sig4_64
    )
    margin_64 = s0_64 - loss_j3_64
    # Exact-coefficient error for q=4, d=2, n=3:
    # A_4 = 64*63/4 = 1008, A_5 = 0, A_6 = 1920 * Pi_4(3) where Pi_4(3) = 64*63*60/(16*15*12) = 84 => A_6 = 161280
    pi4_3 = (64 * 63 * 60) // (16 * 15 * 12)
    a6_64 = 1920 * pi4_3
    err_64 = eval_taylor_error_exact_m6(4, 64, 10, Fraction(1, 3), 1008, 0, a6_64)
    print(f"CASE5 (q=4,d=2,n=3): margin_exact={float_free_frac(margin_64)} (claimed 0.207604) vs exact-coeff err<={float_free_frac(err_64)}")
    assert margin_64 > err_64

    # Check q=4, d=2, n>=4 (N0=256, D=15)
    # Wait: check margin for n >= 4 (N=256): what is S0_exact - loss_j3 for N=256?
    # Wait: for q=4, d=2, any n: A_4 = N(N-1)/4, lines_0 = (N-1)/3, lines_not_0 = N(N-1)/12 - (N-1)/3 = (N-1)(N-4)/12.
    # Lower bound on sigma_4^(0): >= C(N-1, 4) - (lines_0 + lines_not_0) * (N-4) = C(N-1,4) - (N(N-1)/12)*(N-4).
    # Wait: is EVERY bad 4-set either a 4-line not through 0, or bad3 union {x}? Yes (since A_5 = 0!).
    # Number of 4-lines not through 0 is (N-1)(N-4)/12 (each ALREADY contains a bad3!), so ALL bad4 sets are covered by bad3 union {x}!
    lines_tot_256 = (256 * 255) // 12
    sig3_256 = math.comb(255, 3) - lines_tot_256
    sig4_256_lb = math.comb(255, 4) - lines_tot_256 * (256 - 4)
    s0_256 = (
        Fraction(1) - Fraction(255, 256) + Fraction(math.comb(255, 2), 256 ** 2)
        - Fraction(sig3_256, 256 ** 3) + Fraction(4 * 256 + 5, 5 * (256 ** 5)) * sig4_256_lb
    )
    wp_ub_256 = Fraction(1) - Fraction(252, 256) + Fraction(math.comb(252, 2), 256 ** 2)
    margin_256 = s0_256 - Fraction(255 // 3, 256) * wp_ub_256
    # Monotone error bound for q=4, d=2, n>=4:
    # A_4/N^3 <= 1/4, A_6/N^6 <= 2/(3 N^3):
    # Wait: P_5 excess <= N/3 * 20/N^4 * N(N-1)/4 = 5(N-1)/(3 N^2) <= 5/(3 N) = 5/768
    alpha_256 = macwilliams_moments(4, 256, 6)
    a4_256 = (256 * 255) // 4
    a6_256 = (2 * (256 ** 3)) // 3
    err_256 = (
        eval_taylor_error_monotone(4, 256, 15, 6, Fraction(1, 3),
            extra_codewords_term=alpha_256[(6, 4)] * a4_256 + alpha_256[(6, 6)] * a6_256)
        + Fraction(256, 3) * Fraction(20 * a4_256, 256 ** 4)
    )
    print(f"CASE5 (q=4,d=2,n>=4): margin>={float_free_frac(margin_256)} (PROOF 0.199945) vs err<={float_free_frac(err_256)} (PROOF 0.047769)")
    assert margin_256 > err_256

    # Case 6: q=5, d=2, n=3 (N=125, D=10), n=4 (N=625), n>=5 (N=3125)
    # Compute EXACT sigma_3^(0), sigma_4^(0) for q=5, d=2, n=3 (N=125)
    # Using the line-grouped order L_1 < ... < L_31 on F_5^3 \ {0}:
    # 0 is index 0; lines through 0 each get 4 consecutive indices: L_i = {4i-3, 4i-2, 4i-1, 4i}.
    pts5 = [(x, y, z) for x in range(5) for y in range(5) for z in range(5)]
    non0_ordered = []
    seen_0lines = set()
    lines_through_0 = []
    for x, y, z in pts5:
        if (x, y, z) == (0, 0, 0):
            continue
        # Canonicalize direction by first nonzero coord == 1
        dvec = (x, y, z)
        for c in dvec:
            if c != 0:
                inv_c = pow(c, 3, 5)
                dvec = tuple((v * inv_c) % 5 for v in dvec)
                break
        if dvec not in seen_0lines:
            seen_0lines.add(dvec)
            lpts = [tuple((t * v) % 5 for v in dvec) for t in range(1, 5)]
            lines_through_0.append(lpts)
            non0_ordered.extend(lpts)
    assert len(lines_through_0) == 31 and len(non0_ordered) == 124
    v_list = [(0, 0, 0)] + non0_ordered
    v_idx5 = {p: i for i, p in enumerate(v_list)}

    # Collect all 775 5-point lines in F_5^3
    all_lines5 = set()
    for a in range(125):
        pa = v_list[a]
        for b in range(a + 1, 125):
            pb = v_list[b]
            dv = tuple((pb[c] - pa[c]) % 5 for c in range(3))
            lp = tuple(sorted(v_idx5[tuple((pa[c] + t * dv[c]) % 5 for c in range(3))] for t in range(5)))
            all_lines5.add(lp)
    assert len(all_lines5) == 775

    # Exact bad 3-sets in V\{0} for Fix_0(overline{T_0}):
    # On line L through 0 (0 + 4 pts): EVERY 3-subset of L\{0} has 0 in cl(S) => 31*4 = 124 bad 3-sets.
    # On line L not through 0 (5 pts, sorted p0<p1<p2<p3<p4): EVERY 3-subset of {p1,p2,p3,p4} has p0 active => 744*4 = 2976 bad 3-sets.
    bad3_5 = set()
    bad4_5 = set()
    for lp in all_lines5:
        if 0 in lp:
            rem = [x for x in lp if x != 0]
            for trip in itertools.combinations(rem, 3):
                bad3_5.add(trip)
            bad4_5.add(tuple(rem))  # 4-set L\{0} has 0 in cl(S)
        else:
            rem = lp[1:]
            for trip in itertools.combinations(rem, 3):
                bad3_5.add(trip)
            bad4_5.add(rem)
            for quad in itertools.combinations(lp, 4):
                bad4_5.add(quad)  # dependent 4-circuit
    for b3 in bad3_5:
        b3s = set(b3)
        for x in range(1, 125):
            if x not in b3s:
                bad4_5.add(tuple(sorted(b3 + (x,))))
    sig3_125 = math.comb(124, 3) - len(bad3_5)
    sig4_125 = math.comb(124, 4) - len(bad4_5)
    s0_125 = (
        Fraction(1) - Fraction(124, 125) + Fraction(math.comb(124, 2), 125 ** 2)
        - Fraction(sig3_125, 125 ** 3) + Fraction(4 * 125 + 5, 5 * (125 ** 5)) * sig4_125
    )

    # Also compute exact average sigma_3(P) for the 93 sets P in P_0^(3) \cap Fix_1(T_0)!
    # A 3-subset P of L\{0} is in Fix_1(T_0) iff min(L\{0}) in P (3 per line => 93 sets).
    # For each P, how many triples T in V\L fail P \sqcup T \in Fix_1(T_0)?
    # Check PROOF.md L123 claimed bound: avg sigma_3(P) >= C(120, 3) - 99240
    # Wait: let's check both exact L123 margin (using 93/125 * W(P)) AND exact 8-weight enumerator of GRM_5(2,3)!
    w_p3_avg_ub = (
        Fraction(1)
        - Fraction(120, 125)
        + Fraction(math.comb(120, 2), 125 ** 2)
        - Fraction(math.comb(120, 3) - 99240, 125 ** 3)
        + Fraction(4 * 125 + 5, 5 * (125 ** 5)) * math.comb(120, 4)
    )
    loss_j3_125 = Fraction(93, 125) * w_p3_avg_ub
    # Wait: for |P|=5 in P_0^(5): 52000 * Pi_5(3) * 6 / (4 * 125) = 52000 * 31*30/(25*24) * ...?
    # Let's compute exact Pi_5(3): 125*124*120 / (25*24*20) = 155!
    # Wait: how many 6-circuits through 0? 6 * A_6 / (4 * 125), where A_6 = 52000 * 155 = 8,060,000 -> mu_5 = 6 * 8060000 / 500 = 96,720?
    # Wait: notice in PROOF.md L123: W(P) <= 1 - 100/125 + C(119,2)/125^2 = 10146/15625!
    # Let's compute exact weight enumerator of GRM_5(2,3) by enumerating all 5^6 quadratic forms!
    # For each quadratic form Q(x,y,z), tabulate values over all 125 points, subtract affine form a*x+b*y+c*z+d (625 shifts)!
    # Wait: for each fixed (a,b,c) (125 linear parts), count frequency of constant values Q(p) - L(p) in F_5!
    # The weight of Q - L - d is 125 - freq[d]! That checks all 5^10 codewords in ~0.5s!
    # Even faster: precompute vectors for 125 linear forms and 6 quadratic monomials over F_5^3:
    q_vecs = []
    for fn in (
        lambda x, y, z: (x * x) % 5,
        lambda x, y, z: (y * y) % 5,
        lambda x, y, z: (z * z) % 5,
        lambda x, y, z: (x * y) % 5,
        lambda x, y, z: (x * z) % 5,
        lambda x, y, z: (y * z) % 5,
    ):
        q_vecs.append([fn(x, y, z) for x, y, z in v_list])
    l_vecs = [
        [((a * x + b * y + c * z) % 5) for x, y, z in v_list]
        for a in range(5) for b in range(5) for c in range(5)
    ]
    # Pack 125 coords or use fast integer loop in C? Wait: 15,625 * 125 = 1,953,125 iter of 125 elements = 2.4e8 ops in Python (~15s).
    # Too slow in pure Python? Wait: we only need E[Y^8] or full weight dist! Notice by symmetry under GL_3(F_5) on symmetric 3x3 matrices,
    # there are ONLY ~14 orbits of quadratic forms in 3 variables over F_5 (rank 0,1,2,3 x square/nonsquare disc)!
    # Let's classify all 15,625 symmetric 3x3 matrices over F_5 by equivalence or compute exact wt dist on orbit reps!
    # Actually: over F_5, a quadratic form Q(x) + L(x) + d is equivalent under AGL_3(F_5) to one of ONLY a tiny handful of canonical forms!
    # Wait: we can group the 15,625 quadratic forms by GL_3(F_5) orbits OR count wt via exact quadratic character / Gauss sums (trivial in 0.01s!),
    # OR just run a quick GL_3(F_5) orbit reducer! Actually, let's check how fast quadratic-form weight distribution is by exact rank/discriminant formula over F_5!
    # In F_5^3 (odd q=5), every quadratic form Q(x) is GL_3-equivalent to sum_{i=1}^r c_i x_i^2 (r in {0,1,2,3}, c_i in {1, 2}):
    # For each canonical Q_0(x), count how many 3x3 symmetric matrices lie in its orbit, or even simpler:
    # A 3x3 symmetric matrix M has rank r and determinant/discriminant -> ONLY 7 isomorphism classes of Q(x):
    # r=0 (1 form); r=1: x^2 or 2x^2; r=2: x^2-y^2 (split, 2 lines), x^2-2y^2 (nonsplit, 1 pt); r=3: x^2+y^2+z^2 (det=1, square) or 2(x^2+y^2+z^2) (det=2, nonsquare)!
    # Wait: for each of the 15,625 matrices [[a, d/2, e/2], [d/2, b, f/2], [e/2, f/2, c]] in F_5, we find its exact rank & square-class of det in O(1) ops (15,625 iterations -> 0.05s in Python!!),
    # and we only evaluate the 125 affine shifts on the 7 canonical representatives (7 * 125 * 125 = 100k ops -> 0.02s)!!
    # Let's check: does L(x) depend on Q? Under GL_3(F_5), ANY Q(x) + L(x) transforms by the SAME linear change of vars to Q_canon(x') + L'(x'), ranging over ALL L' as L ranges over all 125 linear forms!
    # YES!! Because L' ranges bijectively over all linear forms! That is 100% exact and runs in 0.05 seconds!
    sym_counts = {}
    # Represent 3x3 sym matrix for a*x^2 + b*y^2 + c*z^2 + d*xy + e*xz + f*yz
    # Over F_5, 1/2 = 3 (mod 5).
    field5 = make_field(5)
    # Canonical reps:
    canon_forms = {
        (0, 0): lambda x, y, z: 0,
        (1, 1): lambda x, y, z: (x * x) % 5,
        (1, 2): lambda x, y, z: (2 * x * x) % 5,
        (2, 1): lambda x, y, z: (x * x + y * y) % 5,        # -1 is a square in F_5, so x^2+y^2 = x^2 - (2y)^2 (split, det=1 square)
        (2, 2): lambda x, y, z: (x * x + 2 * y * y) % 5,    # det=2 (nonsquare)
        (3, 1): lambda x, y, z: (x * x + y * y + z * z) % 5,# det=1 (square)
        (3, 2): lambda x, y, z: (x * x + y * y + 2 * z * z) % 5, # det=2 (nonsquare)
    }
    def sq_class(val: int) -> int:
        val %= 5
        assert val != 0
        return 1 if val in (1, 4) else 2

    def classify_sym3(a, b, c, d, e, f) -> tuple[int, int]:
        # Matrix M = [[a, 3d, 3e], [3d, b, 3f], [3e, 3f, c]] mod 5
        m = [[a, (3 * d) % 5, (3 * e) % 5], [(3 * d) % 5, b, (3 * f) % 5], [(3 * e) % 5, (3 * f) % 5, c]]
        # Diagonalize by congruence (symmetric Gaussian elimination!)
        rk = 0
        prod_diag = 1
        for i in range(3):
            if m[i][i] == 0:
                swapped = False
                for j in range(i + 1, 3):
                    if m[j][j] != 0:
                        m[i], m[j] = m[j], m[i]
                        for r in range(3):
                            m[r][i], m[r][j] = m[r][j], m[r][i]
                        swapped = True
                        break
                if not swapped:
                    # Find off-diagonal m[i][j] != 0 or m[j][k] != 0
                    found_off = False
                    for j in range(i, 3):
                        for k in range(j + 1, 3):
                            if m[j][k] != 0:
                                # Bring j,k to i,i+1? Easier: add row k to row j (so m[j][j] becomes 2*m[j][k] != 0!)
                                for r in range(3):
                                    m[j][r] = (m[j][r] + m[k][r]) % 5
                                for r in range(3):
                                    m[r][j] = (m[r][j] + m[r][k]) % 5
                                if j != i:
                                    m[i], m[j] = m[j], m[i]
                                    for r in range(3):
                                        m[r][i], m[r][j] = m[r][j], m[r][i]
                                found_off = True
                                break
                        if found_off:
                            break
                    if not found_off:
                        break
            piv = m[i][i]
            rk += 1
            prod_diag = (prod_diag * piv) % 5
            inv_p = pow(piv, 3, 5)
            for j in range(i + 1, 3):
                if m[j][i] != 0:
                    fac = (m[j][i] * inv_p) % 5
                    for r in range(3):
                        m[j][r] = (m[j][r] - fac * m[i][r]) % 5
                    for r in range(3):
                        m[r][j] = (m[r][j] - fac * m[r][i]) % 5
        return (0, 0) if rk == 0 else (rk, sq_class(prod_diag))

    for a, b, c, d, e, f in itertools.product(range(5), repeat=6):
        cls = classify_sym3(a, b, c, d, e, f)
        sym_counts[cls] = sym_counts.get(cls, 0) + 1
    assert sum(sym_counts.values()) == 15625

    wt_dist_grm5_2_3: dict[int, int] = {}
    for cls, cnt in sym_counts.items():
        qfn = canon_forms[cls]
        q_vals = [qfn(x, y, z) for x, y, z in v_list]
        for lv in l_vecs:
            freqs = [0, 0, 0, 0, 0]
            for idx in range(125):
                freqs[(q_vals[idx] + lv[idx]) % 5] += 1
            for d_const in range(5):
                w = 125 - freqs[d_const]
                wt_dist_grm5_2_3[w] = wt_dist_grm5_2_3.get(w, 0) + cnt
    assert sum(wt_dist_grm5_2_3.values()) == 5 ** 10

    # Exact E[f_5(Y_c)] and exact Phi_{>= 6} using W(P) <= 10146/15625 on |P|=5!
    # Actually let's check both exact E_{C^perp}[Y_c^8] from wt_dist_grm5_2_3 AND exact N/(q-1) * error!
    ey8_125 = Fraction(0)
    sum_w_phi = Fraction(0)
    # Wait: wt_dist_grm5_2_3 gives A_w(C^perp)!!
    # By L82: E_{c in C^perp}[f_5(Y_c)] = sum_{w=1}^{125} w A_w(C) N^{-(w-1)} = N Phi(C)!
    #Wait: E_{c in C^perp}[f_5(Y_c)] gives ALL w >= 4!
    # Let's subtract A_4, A_5, and separate A_6!
    # Wait: N^2/(q-1) * Phi_{>=6}(C) = N^2/(q-1) * 6 A_6 N^{-6} + N^2/(q-1) * Phi_{>=7}(C)!
    # Even better: Phi(C) = sum_{w>=4} w A_w N^{-w}, and A_4 = 125*124 = 15500, A_5 = 125*124/5 = 3100, A_6 = 52000*155 = 8060000!
    # Wait: in PROOF.md L123: mu_5 = 6 A_6 / (4*125) = 96720? Wait: A_6(n=3) = 52000 * 155 = 8,060,000 ->
    # Check: 125^2 / 4 * (6 * A_6 / 125^6) * (10146 / 15625) is ONLY for |P|=5!
    # Wait: how does PROOF.md bound w >= 7 using Y_c^8?
    # Write E[f_5(Y_c)] = E[P_7(Y_c)] + E[R_8(Y_c)]!
    # From exact wt_dist_grm5_2_3, compute exact E[Y_c^r] for r = 1..8!
    # Wait: E[P_7(Y_c)] - sum_{w=4}^7 w A_w N^{-(w-1)} (actually A_7 = ?):
    # Wait: by MacWilliams, E[P_7(Y_c)] cancels w=4..7 up to tiny positive residue c_r alpha_{r,w}, AND E[R_8(Y_c)] uses exact ey8_125!
    ey_pow = [Fraction(0)] * 9
    for w_perp, mult_c in wt_dist_grm5_2_3.items():
        y_c = Fraction(1) - Fraction(5 * w_perp, 4 * 125)
        pw = Fraction(1)
        for r in range(9):
            ey_pow[r] += mult_c * pw
            pw *= y_c
    for r in range(9):
        ey_pow[r] /= (5 ** 10)
    # Also compute exact E_{C^perp}[f_5(Y_c)] - 4 A_4/125^3 - 5 A_5/125^4 - 6 A_6/125^5 (wait: we can literally get exact A_6, A_7 via Krawtchouk or use Taylor R_8!)
    # Check exact R_8 error bound with W(P) <= 10146/15625 on |P|=5:
    e_4_ub = exp_rational_upper(Fraction(4))
    e_1_ub = exp_rational_upper(Fraction(1))  # (q-1)*Y_max = 4 * (1/4) = 1!
    # Note: for n=3, N=125, D=10: zero_cw = 125^2/4 * e^4 / 5^10!
    zero_cw_125 = Fraction(125 * 125, 4) * e_4_ub / (5 ** 10)
    # R_8 term: N/(q-1) * f_5^{(8)}(1/4) / 8! * ey_pow[8]
    # f_5^{(8)}(1/4) <= 4 * 4^7 * (4*(1/4) + 8) * 125 * e^1 = 4^8 * 9 * 125 * e
    r8_125 = Fraction(125, 4) * Fraction(4 * (4 ** 7) * 9 * 125, math.factorial(8)) * e_1_ub * ey_pow[8]
    # Wait: in E[f_5(Y_c)], let's check exact Phi_{>=8} + |P|=5 loss!
    # With MacWilliams P_7:
    # Actually we ALREADY KNOW exact wt_dist_grm5_2_3, so E_{c in C^perp}[f_5(Y_c)] IS KNOWN TO ARBITRARY PRECISION!
    # Let's compute exact E[f_5(Y_c)] using Taylor expansion of order 14 on EVERY Y_c (exact rational!) just to check!
    # Wait: exact Phi(C) = (1/125) * E[f_5(Y_c)] = sum_{w>=4} w A_w 125^{-w}!
    # And we can compute exact A_4, A_5, A_6, A_7 of C = GRM_5(2,3)^perp directly from ey_pow[0..7] if we want, OR via R_8!
    # Wait: let's check R_8 + P_7 excess for w=4,5,6,7 + |P|=5!
    # Wait: why did PROOF.md have A_7? Even better: in F_5^3 for d=2, what IS A_7?
    # Wait: mu_5 = 6 A_6 / (4 * 125) contributes <= mu_5 / 125^3 * (10146 / 15625) = 6 * 8060000 / (4 * 125^4) * (10146/15625)!
    w5_loss_125 = Fraction(6 * 8060000, 4 * (125 ** 4)) * Fraction(10146, 15625)
    # And what about P_7 excess + R_8 for w >= 8 (and w=7)?
    # Using exact N=125 MacWilliams alpha_{r,w} up to r=8, let's check what err_125 is:
    alpha_125_8 = macwilliams_moments(5, 125, 8)
    # Wait: we can also just compute exact E[f_5(Y_c)] with 16-term Taylor (error < 10^{-14}!), subtract exact 4*A_4/125^3 + 5*A_5/125^4 + 6*A_6/125^5,
    # and compare directly with `w5_loss_125` + `error_w7_and_ge8`!
    e_f5_ub = Fraction(0)
    # Using exact lam_125 <= 4, kappa_125 <= 1, OR exact exp rational Taylor for f_5(Y_c):
    # Wait: f_5(Y) = kappa_5 (q-1)(NY-1) e^{lam_5 Y} and E[f_5(Y_c)] = sum w A_w N^{-(w-1)}!
    # Wait: in (4) of Lemma 5: E[P_7(Y)]! Let's check exact sum of c_r * E[Y_c^r] for r=0..7 using lam_125 upper/lower!
    # Actually simplest exact bound on Phi_{>=8}(C) from R_8 + P_7:
    # Since A_4=15500, A_5=3100, A_6=8060000 (let's compute A_7 from MacWilliams on wt_dist!),
    # Wait: we CAN compute exact A_4, A_5, A_6, A_7 of C directly from wt_dist_grm5_2_3 in 1 line using MacWilliams:
    # W_C(1, x) = (1 / 5^10) * sum_{w} A_w(C^perp) (1 + 4x)^{125-w} (1-x)^w mod x^8!
    # That gives EXACT A_0..A_7 of C in 0.01 seconds!!
    def mul_trunc(a, b, deg):
        out = [0] * (deg + 1)
        for i, av in enumerate(a):
            if not av: continue
            for j, bv in enumerate(b):
                if i + j <= deg:
                    out[i + j] += av * bv
        return out
    def pow_trunc(base, exp, deg):
        res = [0] * (deg + 1)
        res[0] = 1
        b = list(base)
        while exp:
            if exp & 1:
                res = mul_trunc(res, b, deg)
            exp >>= 1
            if exp:
                b = mul_trunc(b, b, deg)
        return res
    p_plus4 = [pow_trunc([1, 4], k, 7) for k in range(126)]
    p_minus1 = [pow_trunc([1, -1], k, 7) for k in range(126)]
    wc_coeff = [0] * 8
    for w_perp, mult_c in wt_dist_grm5_2_3.items():
        prod_p = mul_trunc(p_plus4[125 - w_perp], p_minus1[w_perp], 7)
        for j in range(8):
            wc_coeff[j] += mult_c * prod_p[j]
    A_dual = [c // (5 ** 10) for c in wc_coeff]
    assert A_dual[0] == 1 and A_dual[4] == 15500 and A_dual[5] == 3100 and A_dual[6] == 8060000
    print(f"EXACT GRM_5(2,3)^perp A_0..7 = {A_dual}")
    # Wait: A_dual[7] gives exact w=7 too (even though |P|=6 is EVEN, A_7 enters Phi_{>=6} in L29, wait:
    # PROOF.md L29 wrote: w_0 = 6 even, and j >= w_0 - 1 odd => j >= 5 odd, so w=7 (j=6 even) doesn't even enter Phi!
    # Still, checking w >= 8 (and even including w=7!):
    # Let's check exact E_{C^perp}[f_5(Y_c)] - (4 A_4/N^3 + 5 A_5/N^4 + 6 A_6/N^5 + 7 A_7/N^6):
    # First get tight rational bounds on lam_125 and kappa_125:
    # lam_125 = (4*125/5) * ln(129/124) = 100 * ln((129/124)):
    # z = 5 / 253. ln(129/124) in [2*(z + z^3/3), 2*(z + z^3/3 + z^5/5/(1-z^2))]
    z125 = Fraction(5, 253)
    ln_lb = 2 * (z125 + (z125 ** 3) / 3 + (z125 ** 5) / 5)
    ln_ub = ln_lb + 2 * (z125 ** 7) / 7 / (1 - z125 * z125)
    lam_lb, lam_ub = 100 * ln_lb, 100 * ln_ub
    # kappa_125 = 125/124 * (129/125)^{124} * e^{-lam_125} <= 1 (by Lemma 5(1), actually check exact value!)
    # Even simpler: compute P_7(Y) with kappa <= 1 and check! Or compute exact sum of w A_w N^{-(w-1)} for w >= 8
    # by exact E_{c in C^perp}[f_5(Y_c)] using Taylor up to order 12:
    # R_12 remainder <= f_5^{(12)}(1/4)/12! * E[Y^{12}] + f_5(1)/5^{10} < 10^{-8}!
    # Let's compute exact E[f_5(Y_c)] using order-10 Taylor (valid upper bound!):
    # Wait: kappa_125 <= 1 and lam_125 in [lam_lb, lam_ub] -> for each r <= 9, max over lam in [lam_lb, lam_ub]?
    # No, f_5(Y) = kappa_5 (q-1)(NY-1) e^{lam_5 Y} has exact sign at Y_c! For r=8 we ALREADY know exact ey_pow[8]:
    # Wait: look at zero_cw_125 + r8_125 with ey_pow[8]: let's print both r8_125 and w5_loss_125 + P_7 excess!
    # P_7(Y) for kappa_125 <= 1:
    # Actually let's compute exact R_8 using ey_pow[8] + P_7 excess (from A_4..7)!
    # In P_7(Y) = sum_{r=0}^7 c_r Y^r, remember E[Y^r] = E_0[Y^r] + sum_{w=4}^7 alpha_{r,w} A_w (alpha_{r,w}=0 for w>r),
    # and sum_{r=0}^7 c_r E_0[Y^r] = - sum_{r>=8} c_r E_0[Y^r] < 0 (since c_r > 0 for r>=2 and E_0[Y^r] > 0)!
    # Wait: is E[P_7(Y)] - sum_{w=4}^7 w A_w N^{-(w-1)} simply sum_{w=4}^7 A_w (sum_{r=w}^7 c_r alpha_{r,w} - w N^{-(w-1)})?!
    # CHECK THAT! Since E[Y^r] = E_0[Y^r] + sum_{w<=r} alpha_{r,w} A_w, and E[P_7] = sum_{r<=7} c_r E_0[Y^r] + ...,
    # and E_0[f_5(Y)] = 0 => sum_{r<=7} c_r E_0[Y^r] = - sum_{r>=8} c_r E_0[Y^r] <= 0!!
    # So the ONLY positive excess from P_7 comes from sum_{w=4}^7 A_w * (sum_{r=w}^7 c_r alpha_{r,w} - w N^{-(w-1)})!
    # Let's evaluate that exact sum using c_r <= N (q-1)^r / (r-1)! (and wait: check exact sign of sum_{r=w}^7 c_r alpha_{r,w} - w N^{-(w-1)} for r=4..7!):
    #Wait: for r=w, c_w alpha_{w,w} <= w N^{-(w-1)}, so the residual is ONLY r = w+1 .. 7 (i.e. O(1/N^w) smaller!!)!
    c_ub = [Fraction(0)] * 8
    for r in range(2, 8):
        # exact c_r <= (q-1)*[N*lam_ub^{r-1}/(r-1)! - lam_lb^r/r!]
        c_ub[r] = 4 * (Fraction(125) * (lam_ub ** (r - 1)) / math.factorial(r - 1) - (lam_lb ** r) / math.factorial(r))
    # Even tighter: we ALSO have c_4 >= ..., wait: for w=4,5,6,7, alpha_{r,w} can have mixed signs? Let's check alpha_{r,w} signs!
    p7_res = Fraction(0)
    for w in (4, 5, 6, 7):
        s_w = Fraction(0)
        for r in range(w, 8):
            # Take max(c_ub[r] * alpha, c_lb * alpha)
            c_lb_r = 4 * Fraction(125 * 124, 125) # dummy? Let's just use c_ub if alpha>0, 0 if alpha<0 (since c_r > 0 for r>=2!)
            val = c_ub[r] * alpha_125_8[(r, w)] if alpha_125_8[(r, w)] >= 0 else Fraction(0)
            s_w += val
        diff_w = s_w - Fraction(w, 125 ** (w - 1))
        if diff_w > 0:
            p7_res += A_dual[w] * diff_w
    # Exact rational upper bound on N/(q-1)*(E[f_5] - 4A4/N^3 - 5A5/N^4 - 6A6/N^5 - 7A7/N^6) + w6_loss:
    # Using M=14 Taylor bound in exact rational arithmetic (no floats!):
    # 1) E[P_{13}(Y_c)] - sum_{w=4}^7 w A_w N^{-(w-1)} <= sum_{w=4}^7 A_w * max(0, sum_{r=w}^{13} c_ub[r]*alpha_{r,w} - w N^{-(w-1)})
    # Wait: even simpler, directly bound E_{C^perp}[f_5(Y_c)] by order-14 Taylor for EACH weight w_perp in wt_dist_grm5_2_3!
    # Check: for EVERY Y in [-1/4, 1], f_5(Y) = kappa_5 * 4 * (125Y - 1) * exp(lam_5 * Y).
    # Notice kappa_5 <= 125/124 * (129/125)^124 * exp(-lam_lb), and we can bound exp(lam * Y) on EVERY point Y
    # via Taylor order 16 (remainder <= |lam*Y|^16 / 16! * e^4 / ... < 10^{-12})!
    # Let's compute exact rational upper bound on kappa_5 and exp(lam * Y_c) for each weight w_perp!
    e_lam_lb = Fraction(0)
    pw_l = Fraction(1)
    fact_k = 1
    for k in range(18):
        if k > 0:
            pw_l *= -lam_lb
            fact_k *= k
        e_lam_lb += pw_l / fact_k
    # For alternating Taylor of exp(-lam_lb) at odd k=17, truncated at odd term gives LOWER bound? Wait:
    # Even simpler: exp(-lam_lb) = 1 / exp(lam_lb), and exp(lam_lb) >= sum_{k=0}^{20} lam_lb^k / k!
    e_pos_lb = Fraction(1)
    t_k = Fraction(1)
    for k in range(1, 22):
        t_k = t_k * lam_lb / k
        e_pos_lb += t_k
    kap_ub = Fraction(125, 124) * (Fraction(129, 125) ** 124) / e_pos_lb
    assert kap_ub <= 1

    # For each Y_c: 4*(125 Y_c - 1) * exp(lam * Y_c)
    # If Y_c > 1/125 (sign > 0): upper bound uses lam_ub and exp_rational_upper(lam_ub * Y_c).
    # If Y_c <= 1/125 (sign <= 0): Wait: for Y_c < 0, exp(lam * Y_c) >= 1 / exp_rational_upper(-lam_ub * Y_c) (since 4*(125 Y_c - 1) < 0, we want LOWER bound on exp(lam * Y_c)!).
    ef_ub_125 = Fraction(0)
    for w_perp, mult_c in wt_dist_grm5_2_3.items():
        y_c = Fraction(1) - Fraction(5 * w_perp, 500)
        lin = 4 * (125 * y_c - 1)
        if lin >= 0:
            # Note: since kap_ub * lin >= 0 and lam_ub * y_c in [0, 4]:
            exp_val = exp_rational_upper(lam_ub * y_c, terms=22)
            term = kap_ub * lin * exp_val
        else:
            # lin < 0, wait: what is lower bound on exp(lam * y_c) = 1 / exp(-lam * y_c)?
            # Upper bound on exp(-lam * y_c) uses lam_ub (since -y_c > 0)! Wait: for lin < 0,
            # smaller kappa or smaller exp gives LESS negative (LARGER) value!
            # We need LOWER bound on kappa_5 >= 125/124 * (129/125)^124 / exp_rational_upper(lam_ub, 24)
            # AND LOWER bound on exp(lam * y_c) = 1 / exp_rational_upper(lam_ub * (-y_c), 22)!
            # Notice at w_perp = 100 (Y_c = 0): lin = -4, exp(0) = 1 exact!
            exp_neg_ub = exp_rational_upper(lam_ub * (-y_c), terms=22) if y_c < 0 else Fraction(1)
            kap_lb = Fraction(125, 124) * (Fraction(129, 125) ** 124) / exp_rational_upper(lam_ub, terms=24)
            term = kap_lb * lin / exp_neg_ub
        ef_ub_125 += mult_c * term
    ef_ub_125 /= (5 ** 10)
    tail_ge8_125 = Fraction(125, 4) * (
        ef_ub_125
        - Fraction(4 * A_dual[4], 125 ** 3)
        - Fraction(5 * A_dual[5], 125 ** 4)
        - Fraction(6 * A_dual[6], 125 ** 5)
        - Fraction(7 * A_dual[7], 125 ** 6)
    )
    err_125_exact_tail = w5_loss_125 + tail_ge8_125

    wp3_avg_r4 = (
        Fraction(1)
        - Fraction(120, 125)
        + Fraction(math.comb(120, 2), 125 ** 2)
        - Fraction(math.comb(120, 3) - 102960, 125 ** 3)
        + Fraction(math.comb(120, 4), 125 ** 4)
    )
    wp3_avg_shadow = (
        Fraction(1)
        - Fraction(120, 125)
        + Fraction(math.comb(120, 2), 125 ** 2)
        - Fraction(3 * 125 + 8, 4 * (125 ** 4)) * (math.comb(120, 3) - 102960)
    )
    # Using L36 S_0 lower bound (with beta4_new <= Lambda_5(3) = 775) OR exact s0_125:
    s0_125_l36 = (
        Fraction(1) - Fraction(124, 125) + Fraction(math.comb(124, 2), 125 ** 2)
        - Fraction(math.comb(124, 3), 125 ** 3)
        + Fraction(4 * 125 + 5, 5 * (125 ** 5)) * (math.comb(124, 4) - 775)
    )
    margin_125_coarse = s0_125_l36 - Fraction(93, 125) * wp3_avg_r4
    margin_125_shadow = s0_125_l36 - Fraction(93, 125) * wp3_avg_shadow
    print(
        f"CASE6 (q=5,d=2,n=3): S0_L36={float_free_frac(s0_125_l36)}, "
        f"margin_coarse>={float_free_frac(margin_125_coarse)} (claimed 0.041313), "
        f"margin_shadow>={float_free_frac(margin_125_shadow)} (claimed 0.050491), "
        f"err_exact_tail<={float_free_frac(err_125_exact_tail)} (claimed 0.039690)"
    )
    assert err_125_exact_tail < margin_125_coarse < margin_125_shadow

    # Also check Case 6 n=4 (N=625, D=15) and n>=5 (N=3125, D=21) with L36 S0 + coarse & shadow margins!
    for n_c, D_c, claimed_coarse, claimed_shadow, claimed_e in [
        (4, 15, "0.067099", "0.071402", "0.053757"),
        (5, 21, "0.081753", "0.082621", "0.014082"),
    ]:
        Nc = 5 ** n_c
        lines_tot = (Nc * (Nc - 1)) // 20
        s0_c = (
            Fraction(1) - Fraction(Nc - 1, Nc) + Fraction(math.comb(Nc - 1, 2), Nc ** 2)
            - Fraction(math.comb(Nc - 1, 3), Nc ** 3)
            + Fraction(4 * Nc + 5, 5 * (Nc ** 5)) * (math.comb(Nc - 1, 4) - lines_tot)
        )
        wp3_ub_coarse = (
            Fraction(1) - Fraction(Nc - 5, Nc) + Fraction(math.comb(Nc - 5, 2), Nc ** 2)
            - (Fraction(math.comb(Nc - 5, 3)) - Fraction(29, 2) * (Nc ** 2)) / (Nc ** 3)
            + Fraction(math.comb(Nc - 5, 4), Nc ** 4)
        )
        wp3_ub_shadow = (
            Fraction(1) - Fraction(Nc - 5, Nc) + Fraction(math.comb(Nc - 5, 2), Nc ** 2)
            - Fraction(3 * Nc + 8, 4 * (Nc ** 4)) * (Fraction(math.comb(Nc - 5, 3)) - Fraction(29, 2) * (Nc ** 2))
        )
        mu3_c = (3 * (Nc - 1)) // 4
        margin_coarse = s0_c - Fraction(mu3_c, Nc) * wp3_ub_coarse
        margin_shadow = s0_c - Fraction(mu3_c, Nc) * wp3_ub_shadow
        a4_c = Nc * (Nc - 1)
        a5_c = (Nc * (Nc - 1)) // 5
        a6_c = 52000 * ((Nc * (Nc - 1) * (Nc - 5)) // (25 * 24 * 20))
        if n_c == 4:
            err_c = eval_taylor_error_exact_m6(5, Nc, D_c, Fraction(1, 4), a4_c, a5_c, a6_c)
        else:
            al_c = macwilliams_moments(5, Nc, 6)
            extra_c = al_c[(6, 4)] * a4_c + al_c[(6, 5)] * a5_c + al_c[(6, 6)] * a6_c
            p5_ex_c = Fraction(Nc, 4) * (Fraction(10 * (5 - 2), Nc ** 4) * a4_c)
            err_c = eval_taylor_error_monotone(5, Nc, D_c, 6, Fraction(1, 4), extra_codewords_term=extra_c) + p5_ex_c
        print(
            f"CASE6 (q=5,d=2,n={n_c}): coarse>={float_free_frac(margin_coarse)} (claimed {claimed_coarse}), "
            f"shadow>={float_free_frac(margin_shadow)} (claimed {claimed_shadow}), "
            f"err<={float_free_frac(err_c)} (claimed {claimed_e})"
        )
        assert margin_coarse > err_c and margin_shadow > err_c

    return failures


def check_sources_and_proof_audit() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2609.07769.src"
    tdir = root / "targets" / "radici-2609.07769-open"
    target_md = (tdir / "TARGET.md").read_text(encoding="utf-8")
    proof_md = (tdir / "PROOF.md").read_text(encoding="utf-8")

    quote = "The remaining possibilities are"
    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        if quote not in target_md:
            failures.append("TARGET.md quote missing")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            tex = tf.extractfile("main-v32.tex").read().decode("utf-8")
        if quote not in target_md or quote not in tex:
            failures.append("TARGET.md quote mismatch with main-v32.tex")
    if "/tmp/" in target_md or "§7" in target_md or "Section 7" not in target_md or "Section 9" not in target_md:
        failures.append("TARGET.md section numbers or /tmp/ path not fixed (expect Section 7 thm:main, Section 9 Open problems)")
    if "§7" in proof_md or "Section 9" not in proof_md:
        failures.append("PROOF.md still references §7 instead of Section 9")

    if "we subtract $\\mu_3$ from $\\sigma_3^{(0)}$" in proof_md:
        failures.append("Stale false L32 sigma_3/sigma_4 formula still present in PROOF.md")
    if "\\beta_4^{\\mathrm{new}}" not in proof_md or "\\sigma_4(P) \\le \\frac{117}{4}\\sigma_3(P)" not in proof_md:
        failures.append("Expected L35-37 and L128 fixes missing in PROOF.md")
    if "\\frac{N^2}{q-1}\\frac{e^{q-1}}{q^D}" in proof_md or "+ M) N." in proof_md:
        failures.append("Stale false Lemma 5(2) bounds still present in PROOF.md")
    if "\\sigma_2(P) = \\binom{N-5}{2}" in proof_md:
        failures.append("Stale false Lemma 3 sigma_2(P) equality still present in PROOF.md")
    return failures


def main() -> int:
    failures: list[str] = []
    verify_base_n2_q3_q4()
    verify_base_n2_q5()
    failures.extend(verify_lemma5_and_cases2_to_6())
    failures.extend(check_sources_and_proof_audit())
    if failures:
        for f in failures:
            print("ERROR:", f)
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
