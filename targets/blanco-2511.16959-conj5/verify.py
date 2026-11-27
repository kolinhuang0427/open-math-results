#!/usr/bin/env python3
"""Exact verification script for PROOF.md of targets/blanco-2511.16959-conj5/.

Verifies with exact arithmetic (no floating point):
1. All algebraic permutation identities used in Lemmas 2.1 and 2.2 (right-to-left composition).
2. Upper bound & forest/bipartition non-generation proof (Section 1) exhaustively for all
   2 <= k < m < n <= 12 via exact Schreier-Sims group orders.
3. Exact Dirichlet-prime construction (Section 2) for k = 2..15:
   - Constructs Q, valid residue R mod Q, and an explicit prime n == R (mod Q) with n > k^2 + 2.
   - Verifies gcd(a, n - k) = 1, odd parity of r_n, fixed-point & support bounds on r_k,
     and exact BFS transitivity of <r_n, r_m, r_k> on {1..n} for every m in M_k(n).
   - For k in {2, 3, 5} (where the Dirichlet prime n <= 31), additionally verifies by exact
     Schreier-Sims that |<r_n, r_m, r_k>| == n! for every m in M_k(n) and |F_k(n)| equals
     the exact conjectured maximum (k + 1 for k even, (k + 1)/2 for k odd).
4. Exact small-degree attainment check for k = 2..10 via exact Schreier-Sims.

Prints PASS on complete success, FAIL otherwise.
"""
import math
import signal
import sys
from collections import deque
from sympy import isprime
from sympy.combinatorics import Permutation, PermutationGroup


def _timeout(signum, frame):
    print("FAIL: timeout exceeded")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout)
signal.alarm(60)


def prefix_rev_list(n: int, i: int) -> list[int]:
    """Return 0-indexed image list of prefix reversal r_i on {0, ..., n-1}."""
    p = list(range(n))
    p[:i] = reversed(p[:i])
    return p


def prefix_rev_perm(n: int, i: int) -> Permutation:
    return Permutation(prefix_rev_list(n, i))


def compose_rtl(sigma: list[int], pi: list[int]) -> list[int]:
    """Right-to-left composition (sigma * pi)(x) = sigma(pi(x))."""
    return [sigma[pi[x]] for x in range(len(sigma))]


def inverse_list(p: list[int]) -> list[int]:
    inv = [0] * len(p)
    for i, v in enumerate(p):
        inv[v] = i
    return inv


def verify_commutator_and_3cycle_lemmas():
    """Verify Lemma 2.1 (single-overlap commutator) and Lemma 2.2 (3-cycle generation identities)."""
    # Test Lemma 2.2 identities on {0,1,2,3,4,5} with a=0, b=1, z1=2, z2=3, x=2, y=3, z=4
    def cyc3(n, u, v, w):
        p = list(range(n))
        p[u], p[v], p[w] = v, w, u
        return p

    a, b, z1, z2, z3 = 0, 1, 2, 3, 4
    c_abz1 = cyc3(6, a, b, z1)
    c_abz2 = cyc3(6, a, b, z2)
    # Identity 1: (a b z1)(a b z2)^{-1} == (a z2 z1)
    assert compose_rtl(c_abz1, inverse_list(c_abz2)) == cyc3(6, a, z2, z1)
    # Identity 2: (a b z1)^{-1}(a b z2) == (b z2 z1)
    assert compose_rtl(inverse_list(c_abz1), c_abz2) == cyc3(6, b, z2, z1)
    # Identity 3: (a x y)^{-1}(a y z)(a x y) == (x z y)
    c_axy = cyc3(6, a, z1, z2)
    c_ayz = cyc3(6, a, z2, z3)
    assert compose_rtl(inverse_list(c_axy), compose_rtl(c_ayz, c_axy)) == cyc3(6, z1, z3, z2)

    # Test Lemma 2.1: single-overlap commutator [g, g'] = g g' g^{-1} (g')^{-1} == (a g(a) g'(a))
    # Take g = (0 1 2)(3 4) (supp {0,1,2,3,4}) and g' = (0 5 6 7) (supp {0,5,6,7}), overlap {0}
    g = [1, 2, 0, 4, 3, 5, 6, 7]
    gp = [5, 1, 2, 3, 4, 6, 7, 0]
    comm = compose_rtl(g, compose_rtl(gp, compose_rtl(inverse_list(g), inverse_list(gp))))
    assert comm == cyc3(8, 0, g[0], gp[0])
    # Also test overlap of two involutions (e.g. prefix-reversal-like)
    g2 = [1, 0, 3, 2, 4, 5]   # supp {0,1,2,3}
    gp2 = [4, 1, 2, 3, 0, 5]  # supp {0,4}, overlap {0}
    comm2 = compose_rtl(g2, compose_rtl(gp2, compose_rtl(inverse_list(g2), inverse_list(gp2))))
    assert comm2 == cyc3(6, 0, g2[0], gp2[0])


def verify_forest_bipartition_proof(n: int, m: int, k: int):
    """Verify the exact graph H = (V, E_m U E_k) and quotient Q proof of Proposition 1.1."""
    # Build edges of E_m and E_k (0-indexed vertices 0..n-1)
    edges_m = [(x, m - 1 - x) for x in range(m // 2)]
    edges_k = [(x, k - 1 - x) for x in range(k // 2)]
    assert set(edges_m).isdisjoint(set(edges_k))

    # Connected components of H
    adj_h = [[] for _ in range(n)]
    for u, v in edges_m + edges_k:
        adj_h[u].append(v)
        adj_h[v].append(u)
    comp = [-1] * n
    cid = 0
    for start in range(n):
        if comp[start] == -1:
            q = deque([start])
            comp[start] = cid
            while q:
                u = q.popleft()
                for w in adj_h[u]:
                    if comp[w] == -1:
                        comp[w] = cid
                        q.append(w)
            cid += 1
    # H must be acyclic -> exact component count n - floor(m/2) - floor(k/2)
    assert cid == n - (m // 2) - (k // 2)

    # Build quotient multigraph Q on 0..cid-1 with floor(n/2) edges from E_n
    adj_q = [[] for _ in range(cid)]
    for x in range(n // 2):
        cu, cv = comp[x], comp[n - 1 - x]
        adj_q[cu].append(cv)
        adj_q[cv].append(cu)

    # Check connectivity of Q
    color = [-1] * cid
    q = deque([0])
    color[0] = 0
    bipartite = True
    while q:
        u = q.popleft()
        for w in adj_q[u]:
            if color[w] == -1:
                color[w] = 1 - color[u]
                q.append(w)
            elif color[w] == color[u]:
                bipartite = False
    connected = all(c != -1 for c in color)

    if n % 2 == 1 and m + k < n - 1:
        assert not connected
    elif n % 2 == 0 and m + k < n:
        if connected:
            assert cid == (n // 2) + 1
            assert bipartite
            A = {v for v in range(n) if color[comp[v]] == 0}
            B = {v for v in range(n) if color[comp[v]] == 1}
            assert len(A) == n // 2 and len(B) == n // 2
            rm = prefix_rev_list(n, m)
            rk = prefix_rev_list(n, k)
            rn = prefix_rev_list(n, n)
            assert {rm[v] for v in A} == A and {rk[v] for v in A} == A
            assert {rn[v] for v in A} == B and {rn[v] for v in B} == A


def is_sym_n(n: int, m: int, k: int) -> bool:
    G = PermutationGroup(prefix_rev_perm(n, n), prefix_rev_perm(n, m), prefix_rev_perm(n, k))
    return G.order() == math.factorial(n)


def is_transitive_bfs(n: int, m: int, k: int) -> bool:
    rn = prefix_rev_list(n, n)
    rm = prefix_rev_list(n, m)
    rk = prefix_rev_list(n, k)
    seen = [False] * n
    q = deque([0])
    seen[0] = True
    cnt = 1
    while q:
        u = q.popleft()
        for v in (rn[u], rm[u], rk[u]):
            if not seen[v]:
                seen[v] = True
                cnt += 1
                q.append(v)
    return cnt == n


def verify_upper_bound_exhaustive(max_n: int = 12):
    for n in range(4, max_n + 1):
        for k in range(2, n - 1):
            Fk = []
            for m in range(k + 1, n):
                if (n % 2 == 0 and m + k < n) or (n % 2 == 1 and m + k < n - 1):
                    verify_forest_bipartition_proof(n, m, k)
                gen = is_sym_n(n, m, k)
                if gen:
                    if n % 2 == 0:
                        assert m + k >= n
                    else:
                        assert m + k >= n - 1
                    if k % 2 == 1:
                        assert m % 2 == 0
                    Fk.append(m)
            bound = k + 1 if k % 2 == 0 else (k + 1) // 2
            assert len(Fk) <= bound, f"Upper bound failed at k={k}, n={n}: Fk={Fk}"


def find_dirichlet_prime(k: int) -> tuple[int, int, int]:
    """Construct Q, valid R mod Q, and smallest prime n == R (mod Q) with n > k^2 + 2."""
    odd_primes = [q for q in range(3, k + 2) if isprime(q)]
    Q = 4
    for q in odd_primes:
        Q *= q
    # Build R via CRT: R == 3 (mod 4), R == r_q (mod q) with r_q not in {0, k mod q}
    R = 3
    mod = 4
    for q in odd_primes:
        for rq in range(1, q):
            if rq != (k % q):
                # Lift R mod mod and rq mod q
                inv_mod = pow(mod, -1, q)
                t = ((rq - R) * inv_mod) % q
                R = R + mod * t
                mod *= q
                break
    assert mod == Q
    assert R % 4 == 3
    assert math.gcd(R, Q) == 1
    for q in odd_primes:
        assert R % q != 0 and (R - k) % q != 0

    # Find smallest prime n == R (mod Q) with n > k^2 + 2
    min_n = k * k + 3
    start = R
    if start < min_n:
        step = (min_n - start + Q - 1) // Q
        start += step * Q
    n = start
    while not isprime(n):
        n += Q
    return Q, R, n


def verify_dirichlet_construction():
    for k in range(2, 16):
        Q, R, n = find_dirichlet_prime(k)
        assert isprime(n) and n % Q == R and n > k * k + 2
        assert (n // 2) % 2 == 1  # r_n is an odd permutation
        supp_rk = 2 * (k // 2)
        assert supp_rk >= 2 and n - k >= 2
        assert (supp_rk - 1) ** 2 + 1 < n
        b = n - k
        if k % 2 == 0:
            a_list = list(range(1, k + 2))
            expected_size = k + 1
        else:
            a_list = list(range(1, k + 1, 2))
            expected_size = (k + 1) // 2
        assert len(a_list) == expected_size

        for a in a_list:
            m = n - a
            assert k < m < n
            assert math.gcd(a, b) == 1
            # Verify r_m r_n(y) == y - a for y in [a+1, n] (0-indexed: y in [a, n-1])
            rn = prefix_rev_list(n, n)
            rm = prefix_rev_list(n, m)
            rk = prefix_rev_list(n, k)
            for y in range(a, n):
                assert rm[rn[y]] == y - a
            # Verify r_n r_k(x) == x + b for x in [1, k] (0-indexed: x in [0, k-1])
            for x in range(k):
                assert rn[rk[x]] == x + b
            assert is_transitive_bfs(n, m, k)

        # For k in {2, 3, 5} (Dirichlet prime n <= 31), also confirm full Sym_n via exact Schreier-Sims
        if n <= 31:
            for a in a_list:
                assert is_sym_n(n, n - a, k), f"Failed Sym_n at k={k}, n={n}, a={a}"
            # Also confirm no other m in [n - k - 1, n - 1] generates Sym_n
            found = [m for m in range(n - k - 1, n) if is_sym_n(n, m, k)]
            assert found == sorted(n - a for a in a_list)
            assert len(found) == expected_size


def verify_small_equality_attainment():
    """Confirm equality is achieved at small degrees for k = 2..10 via exact Schreier-Sims."""
    witnesses = {
        2: 7,
        3: 7,
        4: 11,
        5: 19,
        6: 17,
        7: 23,
        8: 19,
        9: 31,
        10: 23,
    }
    for k, n in witnesses.items():
        expected = k + 1 if k % 2 == 0 else (k + 1) // 2
        Fk = [m for m in range(n - k - 1, n) if is_sym_n(n, m, k)]
        assert len(Fk) == expected, f"Expected {expected} at k={k}, n={n}, got {len(Fk)}"


def main():
    verify_commutator_and_3cycle_lemmas()
    verify_upper_bound_exhaustive(max_n=12)
    verify_dirichlet_construction()
    verify_small_equality_attainment()
    print("PASS")


if __name__ == "__main__":
    main()
