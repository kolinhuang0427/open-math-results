#!/usr/bin/env python3
"""Exact-arithmetic verifier for Hong Duc Bui's acyclicity conjecture
(arXiv:2508.04602v1, Section 8.2) and the potential Phi(pi) = prod ell_k(B_{pi_k}).

Uses pure Python arbitrary-precision integer arithmetic only (no floating point).
Tests Lemma 1, Lemma 2, Lemma 3 (strict potential decrease and non-intersection
after swap), and full graph acyclicity on diverse general-position point sets
for n = 3, 4, 5, 6, 7.
"""

import itertools
import random


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def seg_proper_cross(a, b, c, d):
    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)
    return (o1 * o2 < 0) and (o3 * o4 < 0)


def pt_in_tri(p, a, b, c):
    o1 = orient(a, b, p)
    o2 = orient(b, c, p)
    o3 = orient(c, a, p)
    return (o1 > 0 and o2 > 0 and o3 > 0) or (o1 < 0 and o2 < 0 and o3 < 0)


def tris_intersect_nontrivial(q1, q2, b1, q3, q4, b2):
    """Exact general-position check for nontrivial intersection of
    triangle(q1, q2, b1) and triangle(q3, q4, b2), where q1q2 and q3q4 are
    distinct edges of CH(Q) and b1 != b2 are interior points.
    """
    for u1, v1 in ((q1, b1), (q2, b1)):
        for u2, v2 in ((q3, b2), (q4, b2)):
            if seg_proper_cross(u1, v1, u2, v2):
                return True
    return pt_in_tri(b1, q3, q4, b2) or pt_in_tri(b2, q1, q2, b1)


def is_general_position(pts):
    m = len(pts)
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if orient(pts[i], pts[j], pts[k]) == 0:
                    return False
    return True


def verify_instance(Q, B):
    n = len(Q)
    assert len(B) == n and n >= 3
    assert is_general_position(Q + B), "Point set not in general position"

    # Verify Q is in strict CCW convex hull order and every B is strictly inside CH(Q)
    for i in range(n):
        q1, q2 = Q[i], Q[(i + 1) % n]
        for j in range(n):
            val = orient(q1, q2, Q[j])
            if j == i or j == (i + 1) % n:
                assert val == 0
            else:
                assert val > 0, "Hull not strictly convex CCW"
        for r in range(n):
            assert orient(q1, q2, B[r]) > 0, "Interior point not strictly inside CH(Q)"

    # Exact integer table ell[i][r] = orient(Q[i], Q[(i+1)%n], B[r]) > 0
    ell = [[orient(Q[i], Q[(i + 1) % n], B[r]) for r in range(n)] for i in range(n)]

    # Precompute conflicts[i][a][j][b]
    conf = [[[[False] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for a in range(n):
            for j in range(i + 1, n):
                for b in range(n):
                    if a == b:
                        continue
                    hit = tris_intersect_nontrivial(
                        Q[i], Q[(i + 1) % n], B[a],
                        Q[j], Q[(j + 1) % n], B[b],
                    )
                    if hit:
                        # Lemma 3 check: ell[i][b] * ell[j][a] < ell[i][a] * ell[j][b]
                        lhs = ell[i][b] * ell[j][a]
                        rhs = ell[i][a] * ell[j][b]
                        if not (lhs < rhs):
                            print("FAIL: Lemma 3 violated!", lhs, rhs)
                            return False
                        # Post-swap non-intersection check
                        swapped_hit = tris_intersect_nontrivial(
                            Q[i], Q[(i + 1) % n], B[b],
                            Q[j], Q[(j + 1) % n], B[a],
                        )
                        if swapped_hit:
                            print("FAIL: Swapped triangles still intersect!")
                            return False
                        conf[i][a][j][b] = True

    # Verify exact potential decrease on ALL edges of G and DAG acyclicity on S_n
    perms = list(itertools.permutations(range(n)))
    perm_idx = {p: idx for idx, p in enumerate(perms)}
    phi = []
    for p in perms:
        val = 1
        for k in range(n):
            val *= ell[k][p[k]]
        phi.append(val)

    edge_count = 0
    adj = [[] for _ in range(len(perms))]
    for u, p in enumerate(perms):
        for i in range(n):
            a = p[i]
            for j in range(i + 1, n):
                b = p[j]
                if conf[i][a][j][b]:
                    q = list(p)
                    q[i], q[j] = q[j], q[i]
                    v = perm_idx[tuple(q)]
                    if not (phi[v] < phi[u]):
                        print("FAIL: Phi did not strictly decrease!", phi[v], phi[u])
                        return False
                    adj[u].append(v)
                    edge_count += 1

    # Explicit DFS cycle check on G
    state = [0] * len(perms)
    for start in range(len(perms)):
        if state[start] != 0:
            continue
        stack = [(start, 0)]
        state[start] = 1
        while stack:
            u, idx = stack[-1]
            if idx < len(adj[u]):
                stack[-1] = (u, idx + 1)
                v = adj[u][idx]
                if state[v] == 1:
                    print("FAIL: Cycle detected in G!")
                    return False
                if state[v] == 0:
                    state[v] = 1
                    stack.append((v, 0))
            else:
                state[u] = 2
                stack.pop()

    return edge_count


def make_integer_instance(n, rng, skewed=False):
    # Pick n integer points on a convex parabola / circle-like curve using exact rationals
    # Using points on unit circle parametrized by rational t: ((1-t^2)/(1+t^2), 2t/(1+t^2))
    # Clear common denominator or use integer parabola (k, k^2)?
    # Better: use distinct rational slopes t_1 < ... < t_n mapped via stereographic projection
    # scaled to exact integers!
    ts = sorted(rng.sample(range(-40, 41), n))
    # Point (1 - t^2, 2t) / (1 + t^2) -> scale by product of (1 + t^2) or just project onto integer hull:
    # Actually convex hull on a circle with integer points: use Pythagorean triples or
    # simply exact rational scale LCM? Let's use (1 - t^2) * M // (1 + t^2) isn't exact on circle,
    # instead use exact integer convex polygon via positive slope increments!
    Q = [(0, 0)]
    # Generate n strictly increasing angles via exact integer vectors (dx, dy) in Q1..Q4
    vecs = []
    # Pick n distinct slopes across 4 quadrants so sum = (0,0)? Simpler:
    # Use integer points on parabola? No, parabola isn't closed.
    # Use exact rational points on circle x = (1-t^2)/(1+t^2), y = 2t/(1+t^2) with small t in [-4,4]
    # and multiply by LCM of all (1+t^2)!
    from math import lcm
    denoms = [1 + t * t for t in ts]
    L = 1
    for d in denoms:
        L = lcm(L, d)
    Q = [((1 - t * t) * (L // (1 + t * t)), (2 * t) * (L // (1 + t * t))) for t in ts]
    if skewed:
        Q = [(x * 3, y) for x, y in Q]
    # Ensure CCW order: points on circle with increasing t go CCW around (-1, 0) except wraparound.
    # Order by atan2? No float needed! Wait: for exact integer CCW order around centroid/origin:
    # Sort by half-plane (y > 0 or (y == 0 and x > 0)) then cross product!
    from functools import cmp_to_key
    def half(p):
        return 0 if (p[1] > 0 or (p[1] == 0 and p[0] > 0)) else 1
    def cmp_ccw(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = a[0] * b[1] - a[1] * b[0]
        return -1 if c > 0 else (1 if c < 0 else 0)
    Q.sort(key=cmp_to_key(cmp_ccw))

    minx = min(p[0] for p in Q)
    maxx = max(p[0] for p in Q)
    miny = min(p[1] for p in Q)
    maxy = max(p[1] for p in Q)

    B = []
    while len(B) < n:
        cand = (rng.randint(minx + 1, maxx - 1), rng.randint(miny + 1, maxy - 1))
        if not all(orient(Q[i], Q[(i + 1) % n], cand) > 0 for i in range(n)):
            continue
        pts = Q + B
        if all(orient(pts[a], pts[b], cand) != 0 for a in range(len(pts)) for b in range(a + 1, len(pts))):
            B.append(cand)
    return Q, B


def main():
    rng = random.Random(20250806)
    total_edges = 0
    cases = 0
    for n, count in [(3, 20), (4, 20), (5, 15), (6, 10), (7, 3)]:
        for idx in range(count):
            Q, B = make_integer_instance(n, rng, skewed=(idx % 2 == 1))
            ec = verify_instance(Q, B)
            if ec is False:
                print("FAIL")
                return
            total_edges += ec
            cases += 1
    print(f"PASS (verified {cases} exact integer general-position instances for n=3..7, {total_edges} edges in G)")


if __name__ == "__main__":
    main()
