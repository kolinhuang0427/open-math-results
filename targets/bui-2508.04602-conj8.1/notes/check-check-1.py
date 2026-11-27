#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Hong Duc Bui arXiv:2508.04602v1 Section 8.2 Conjecture.

Built strictly from primary source definitions and targets/bui-2508.04602-conj8.1/PROOF.md.
Uses pure integer arithmetic (zero floats).
"""

from __future__ import annotations

import itertools
import random
import sys

Point = tuple[int, int]


def orient2d(a: Point, b: Point, c: Point) -> int:
    """Exact 2x signed area of triangle (a, b, c)."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def sgn(x: int) -> int:
    return (1 if x > 0 else (-1 if x < 0 else 0))


def check_general_position_and_hull(Q_hull: list[Point], B_int: list[Point]) -> None:
    n = len(Q_hull)
    assert n >= 3 and len(B_int) == n
    all_pts = Q_hull + B_int
    assert len(set(all_pts)) == 2 * n

    # No 3 points collinear
    for i in range(2 * n):
        for j in range(i + 1, 2 * n):
            for k in range(j + 1, 2 * n):
                assert orient2d(all_pts[i], all_pts[j], all_pts[k]) != 0, "Not in general position"

    # Q_hull in strict CCW convex order, and all B_int strictly inside
    for k in range(n):
        qk = Q_hull[k]
        qk1 = Q_hull[(k + 1) % n]
        for m in range(n):
            if m != k and m != (k + 1) % n:
                assert orient2d(qk, qk1, Q_hull[m]) > 0, "Hull not strict CCW convex"
        for b in B_int:
            assert orient2d(qk, qk1, b) > 0, "Interior point not strictly inside hull"


def seg_strict_cross(a: Point, b: Point, c: Point, d: Point) -> bool:
    """True iff open segments (a, b) and (c, d) intersect at a single interior point (general position)."""
    if len({a, b, c, d}) < 4:
        return False
    o1 = orient2d(a, b, c)
    o2 = orient2d(a, b, d)
    o3 = orient2d(c, d, a)
    o4 = orient2d(c, d, b)
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


def point_in_open_triangle(p: Point, t: tuple[Point, Point, Point]) -> bool:
    a, b, c = t
    o1 = orient2d(a, b, p)
    o2 = orient2d(b, c, p)
    o3 = orient2d(c, a, p)
    return (o1 > 0 and o2 > 0 and o3 > 0) or (o1 < 0 and o2 < 0 and o3 < 0)


def triangles_intersect_nontrivially(t1: tuple[Point, Point, Point], t2: tuple[Point, Point, Point]) -> bool:
    """Exact general-position test for nontrivial intersection of two triangles T_i, T_j (i != j, B_a != B_b).

    Tests BOTH boundary crossing and vertex-in-interior containment directly,
    independently verifying Lemma 1.
    """
    # Check edge-edge crossings
    edges1 = [(t1[0], t1[1]), (t1[1], t1[2]), (t1[2], t1[0])]
    edges2 = [(t2[0], t2[1]), (t2[1], t2[2]), (t2[2], t2[0])]
    for e1 in edges1:
        for e2 in edges2:
            if seg_strict_cross(e1[0], e1[1], e2[0], e2[1]):
                return True
    # Check if any vertex of one triangle lies strictly inside the other
    for v in t1:
        if v not in t2 and point_in_open_triangle(v, t2):
            return True
    for v in t2:
        if v not in t1 and point_in_open_triangle(v, t1):
            return True
    return False


def verify_instance(Q_hull: list[Point], B_int: list[Point], label: str) -> tuple[int, int]:
    check_general_position_and_hull(Q_hull, B_int)
    n = len(Q_hull)

    # Precompute l_k(B_r) = orient2d(Q_k, Q_{k+1}, B_r) > 0
    ell = [[orient2d(Q_hull[k], Q_hull[(k + 1) % n], B_int[r]) for r in range(n)] for k in range(n)]

    # Verify Lemma 2(1)-(4)
    for k in range(n):
        assert orient2d(Q_hull[k], Q_hull[(k + 1) % n], Q_hull[k]) == 0
        assert orient2d(Q_hull[k], Q_hull[(k + 1) % n], Q_hull[(k + 1) % n]) == 0
        for m in range(n):
            val = orient2d(Q_hull[k], Q_hull[(k + 1) % n], Q_hull[m])
            if m in (k, (k + 1) % n):
                assert val == 0
            else:
                assert val > 0
        for r in range(n):
            assert ell[k][r] > 0
    for i in range(n):
        for j in range(n):
            if i != j:
                v1 = orient2d(Q_hull[j], Q_hull[(j + 1) % n], Q_hull[i])
                v2 = orient2d(Q_hull[j], Q_hull[(j + 1) % n], Q_hull[(i + 1) % n])
                assert v1 >= 0 and v2 >= 0 and (v1 + v2) > 0

    # Precompute triangle intersection cache: inter[(i, a, j, b)] -> bool for i < j, a != b
    inter = {}
    for i in range(n):
        for j in range(i + 1, n):
            for a in range(n):
                ti = (Q_hull[i], B_int[a], Q_hull[(i + 1) % n])
                for b in range(n):
                    if a == b:
                        continue
                    tj = (Q_hull[j], B_int[b], Q_hull[(j + 1) % n])
                    hit = triangles_intersect_nontrivially(ti, tj)
                    inter[(i, a, j, b)] = hit
                    if hit:
                        # Lemma 3: strict area-product decrease + post-swap non-intersection
                        assert ell[i][b] * ell[j][a] < ell[i][a] * ell[j][b], (
                            f"{label}: Lemma 3 inequality failed at (i={i},j={j},a={a},b={b})"
                        )
                        ti_sw = (Q_hull[i], B_int[b], Q_hull[(i + 1) % n])
                        tj_sw = (Q_hull[j], B_int[a], Q_hull[(j + 1) % n])
                        assert not triangles_intersect_nontrivially(ti_sw, tj_sw), (
                            f"{label}: Post-swap triangles still intersect at (i={i},j={j},a={a},b={b})"
                        )

    # Full state graph check on S_n
    perms = list(itertools.permutations(range(n)))
    phi = {}
    for p in perms:
        val = 1
        for k in range(n):
            val *= ell[k][p[k]]
        assert val > 0
        phi[p] = val

    edge_count = 0
    sink_count = 0
    for p in perms:
        out_deg = 0
        for i in range(n):
            for j in range(i + 1, n):
                if inter[(i, p[i], j, p[j])]:
                    q = list(p)
                    q[i], q[j] = q[j], q[i]
                    qt = tuple(q)
                    assert phi[qt] < phi[p], f"{label}: Phi did not strictly decrease"
                    edge_count += 1
                    out_deg += 1
        if out_deg == 0:
            sink_count += 1
    assert sink_count >= 1, f"{label}: No sink (non-intersecting matching) found!"
    return len(perms), edge_count


def make_perturbed_polygon_and_interior(n: int, seed: int, mode: str) -> tuple[list[Point], list[Point]]:
    """Construct exact integer points in general position with |CH|=n and n interior points."""
    rng = random.Random(seed)
    R = 10000
    # Use rational circle parameterization ((1-t^2)/(1+t^2), 2t/(1+t^2)) or exact integer convex hull on parabola/circle
    # Even simpler: vertices on scaled circle via exact rational points cleared to common denominator,
    # or points (x, y) around a circle rounded then strictly convexified.
    # Actually: integer points on a parabola/ellipse or convex chain:
    # Take angles via rational points (1 - t^2, 2t) scaled and cleared, wait: on unit circle x^2+y^2=1,
    # distinct points ALWAYS form a strictly convex polygon!
    # Pick n distinct integers t_1 < t_2 < ... < t_n? Better: pick rational angles around full circle:
    # For k=0..n-1, take exact rational approximation to (cos, sin) on unit circle using Pythagorean triples!
    # Specifically, for k=1..n, u_k in Q: ((1 - u_k^2)/(1 + u_k^2), 2 u_k/(1 + u_k^2)) gives points on unit circle,
    # Wait: if we pick integer slopes or just scale by 10^6 and round? Rounding can break convexity only if collinear,
    # which we avoid by large radius and explicit check!
    import math
    # Note: math.cos/sin only used to generate integer test coordinates, NOT in any verification arithmetic!
    # Wait: to avoid even importing math trig / float anywhere in check-check-1.py, generate strictly convex polygon purely in int!
    # Pure integer strictly convex n-gon: pick n distinct slopes and build vertices by summing positive-turn edge vectors,
    # or pick points on a circle of Pythagorean triples!
    # Let's use Pythagorean triples: for coprime (a_k, b_k) or just t_k = p_k / q_k,
    # point on unit circle is ((q^2 - p^2)/(q^2 + p^2), 2pq/(q^2 + p^2)).
    # To avoid huge LCM denominators, use small fractions p/q and round? No, don't use float!
    # Pure integer convex n-gon: start at (0, 0), take n edge vectors (dx_k, dy_k) in CCW order summing to (0, 0)!
    # Even simpler: place points on upper + lower convex arcs, or use exact integer circle points (x, y) on x^2+y^2 = M!
    # Wait: 5^5 = 3125 or 65 * ... has many lattice points! Even simpler:
    # Take m_1 < m_2 < ... < m_n in Z: upper hull points (m_k, -m_k^2) if n is split?
    # Let's just take k-th vector v_k = (dx_k, dy_k) and reflect/balance so sum = 0:
    # Choose angles in Q1: (dx_k, dy_k) with dy_k/dx_k strictly increasing, then negate for Q3, etc.!
    # Let's construct n edge vectors in Z^2 in strict CCW angle order whose sum is (0, 0):
    # Pick m = floor(n/2) vectors in first half-plane, and adjust! Actually for even/odd n:
    # Take half-vectors (a_1, b_1), ..., (a_r, b_r) in Q1 with 0 < b_1/a_1 < ... < b_r/a_r,
    # add their negatives (-a_1, -b_1), ... -> sums to 0! That gives 2r vectors. For odd n=2r+1, split one vector!
    r = n // 2
    vecs = []
    for k in range(1, r + 1):
        vecs.append((1000, k * 300 + rng.randint(1, 50)))
    if n % 2 == 0:
        neg = [(-dx, -dy) for dx, dy in vecs]
        all_v = vecs + neg
    else:
        # Replace first negative (-a_1, -b_1) by two vectors summing to (-a_1, -b_1) with steeper/shallower slopes
        # Wait: sum of vecs is (S_x, S_y). Take (-(S_x - u), -(S_y - v))? Easier:
        # Take n-1 vectors summing to (-dx_last, -dy_last) where last vector is in Q4!
        # Let's use r vectors in Q1 (dx > 0, dy > 0), then reflect across y-axis?
        # Even simpler: take r vectors in Q1: (100, 10*k + jitter), and (n-r) vectors in Q3/Q4 summing to -sum!
        # Any vector with dx < 0, dy < 0 has angle in (180, 270), and we just partition (-S_x, -S_y) into (n-r) vectors
        # with strictly increasing slopes!
        Sx = sum(vx for vx, _ in vecs)
        Sy = sum(vy for _, vy in vecs)
        m = n - r  # >= 2
        # Partition (-Sx, -Sy) into m vectors in Q3 with strictly increasing slopes vy/vx (since vx < 0, vy < 0,
        # CCW in Q3 means vy/vx DECREASES? Wait: (-10, -1) is angle 186 deg, (-1, -10) is angle 264 deg!
        # So in Q3, CCW order means |vy|/|vx| INCREASES, i.e. vy/vx INCREASES!).
        # Pick vx_j = -Sx // m (adjust last), and vy_j decreasing in magnitude? Wait:
        # For (-vx, -vy) in Q3, angle increases with (-vy)/(-vx) = vy/vx!
        # So make vy_j/vx_j strictly increasing: pick vx_j negative, e.g. all equal -1000, wait sum vx_j = -Sx.
        # Just scale Sx, Sy by 100! Wait: Sx = 1000*r. If m = r+1, Sx/m might not be integer, so scale vecs by m!
        vecs = [(vx * m, vy * m) for vx, vy in vecs]
        Sx *= m
        Sy *= m
        base_x = Sx // m
        base_y = Sy // m
        rem_y = Sy - base_y * m
        # Make deltas sum to 0 in y: d_j strictly increasing!
        # Wait: if vx = -base_x < 0 and vy = -(base_y + d_j) < 0, then vy/vx = (base_y + d_j)/base_x strictly increases with d_j!
        # Pick d_j = (2*j - (m - 1)) * 50 for j = 0..m-1 (sums to 0!), and absorb rem_y=0 since Sy divisible by m!
        assert Sx % m == 0 and Sy % m == 0
        neg_vecs = [(-base_x, -(base_y + (2 * j - (m - 1)) * 50)) for j in range(m)]
        all_v = vecs + neg_vecs

    # Sort all_v in strict CCW order (they already are, let's verify cross > 0 consecutively)
    hull = [(0, 0)]
    for dx, dy in all_v[:-1]:
        px, py = hull[-1]
        hull.append((px + dx, py + dy))

    # Centroid (exact integer if we scale hull by n!)
    hull = [(x * n, y * n) for x, y in hull]
    cx = sum(x for x, _ in hull) // n
    cy = sum(y for _, y in hull) // n

    # Generate n interior points as integer barycentric combinations of hull vertices
    B_int: list[Point] = []
    while len(B_int) < n:
        if mode == "clustered":
            bx = cx + rng.randint(-50, 50)
            by = cy + rng.randint(-50, 50)
        elif mode == "double_circle":
            idx = len(B_int)
            q1 = hull[idx]
            q2 = hull[(idx + 1) % n]
            mx = (q1[0] + q2[0]) // 2
            my = (q1[1] + q2[1]) // 2
            # 90% towards midpoint, 10% towards centroid + tiny jitter
            bx = (9 * mx + cx) // 10 + rng.randint(-15, 15)
            by = (9 * my + cy) // 10 + rng.randint(-15, 15)
        else:
            # random convex combination
            w = [rng.randint(1, 20) for _ in range(n)]
            sw = sum(w)
            bx = sum(w[i] * hull[i][0] for i in range(n)) // sw + rng.randint(-20, 20)
            by = sum(w[i] * hull[i][1] for i in range(n)) // sw + rng.randint(-20, 20)

        cand = (bx, by)
        # Check strictly inside and general position with existing points
        inside = all(orient2d(hull[k], hull[(k + 1) % n], cand) > 0 for k in range(n))
        if not inside:
            continue
        existing = hull + B_int
        gp = True
        for i in range(len(existing)):
            for j in range(i + 1, len(existing)):
                if orient2d(existing[i], existing[j], cand) == 0:
                    gp = False
                    break
            if not gp:
                break
        if gp:
            B_int.append(cand)
    return hull, B_int


def run_all_checks() -> None:
    total_edges = 0
    total_instances = 0
    configs = [
        (3, 10),
        (4, 10),
        (5, 8),
        (6, 4),
        (7, 2),
    ]
    modes = ("random", "clustered", "double_circle")
    for n, count in configs:
        for idx in range(count):
            mode = modes[idx % len(modes)]
            seed = n * 1000 + idx * 17 + 5
            Q_hull, B_int = make_perturbed_polygon_and_interior(n, seed, mode)
            n_perms, n_edges = verify_instance(Q_hull, B_int, f"n={n},idx={idx},mode={mode}")
            total_edges += n_edges
            total_instances += 1
        print(f"  n={n}: verified {count} full S_{n} state graphs")
    print(f"Total: {total_instances} instances, {total_edges} directed swap edges verified.")
    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
