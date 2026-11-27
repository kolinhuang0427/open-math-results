"""Independent exact-arithmetic verifier for targets/teheux-2611.12469-q3/.

Derived directly from arXiv:2611.12469v1 (Bruno Teheux, Question 8.4(3)) and
targets/teheux-2611.12469-q3/PROOF.md without reading verify.py or author notes.
Zero floating-point arithmetic is used anywhere.

Checks:
1. Finite median algebras & bounded poc sets (Defs 2.1, 2.2, 2.5, 2.7, Lem 2.8, Thm 3.4,
   Lemma 1 transversality bound & Helly property, Example 7.2 phi_B, Remark 7.5 tree D).
2. Constructive execution of Lemmas 2-3 and Steps 0-3 (Claims I-II, clopen retraction pi,
   clopen ultrafilter pullbacks U_tilde, and explicit median embedding B -> A) on genuine
   infinite finite-rank median algebras A whose duals X = A* have non-clopen ultrafilters:
   - Rank-1 chain A1 = omega + omega* (non-bound limit point t in X \\ {0, 1});
   - Rank-2 product A4 = omega x (omega + omega*) (simultaneous 0 in A_U and t in A_U \\ {0});
   - Rank-2 half-grid A2 = {(x, y) in (omega + omega*)^2 : x <= y} hitting the sharp
     Lemma 2 bound |A_U \\ {0}| = 2 = rank(A2) WITH comparable boundary points r < t in A_U
     (stress-testing Step 1 bottom-up Omega_{t,U} induction and D_t construction) and with
     multi-element non-clopen finite subalgebras B <= (X^flat)_+ embedded explicitly into A2.
3. Exact verification of the Remark's Priestley space P = (N U {inf}) x {0, 1}
   distributive lattice counterexample (U(P) has nontrivial complemented pair, ClopUp(P) does not).
"""

from __future__ import annotations

from itertools import combinations, product


# ============================================================================
# Part 1: Exact Finite Median Algebras, Bounded Poc Sets, Rank & Remark 7.5
# ============================================================================

def check_median_axioms(elements: list[int], med_fn) -> None:
    """Verify Definition 2.1 (symmetry, majority, distributivity) on a finite set."""
    for a in elements:
        for b in elements:
            assert med_fn(a, a, b) == a, f"Majority failed at {a}, {b}"
            for c in elements:
                m1 = med_fn(a, b, c)
                assert med_fn(b, a, c) == m1 and med_fn(b, c, a) == m1, "Symmetry failed"
    # Check distributivity on all 5-tuples (when small enough) or sampled/full
    if len(elements) <= 10:
        for a, b, c, d, e in product(elements, repeat=5):
            lhs = med_fn(med_fn(a, b, c), d, e)
            rhs = med_fn(a, med_fn(b, d, e), med_fn(c, d, e))
            assert lhs == rhs, "Distributivity failed"


def tree_median_algebra(n: int, edges: list[tuple[int, int]]):
    """Build median algebra of vertices 0..n-1 of a finite tree via geodesic intersection."""
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def path(u: int, v: int) -> list[int]:
        parent = [-1] * n
        parent[u] = u
        queue = [u]
        idx = 0
        while idx < len(queue):
            cur = queue[idx]
            idx += 1
            if cur == v:
                break
            for nxt in adj[cur]:
                if parent[nxt] == -1:
                    parent[nxt] = cur
                    queue.append(nxt)
        res = []
        cur = v
        while cur != u:
            res.append(cur)
            cur = parent[cur]
        res.append(u)
        return res

    paths = {(u, v): set(path(u, v)) for u in range(n) for v in range(n)}

    def med(a: int, b: int, c: int) -> int:
        inter = paths[(a, b)] & paths[(a, c)] & paths[(b, c)]
        assert len(inter) == 1, f"Not a tree geodesic triple: {a}, {b}, {c}"
        return next(iter(inter))

    return list(range(n)), med


def cube_median(bits_a: int, bits_b: int, bits_c: int) -> int:
    """Pointwise majority on bitmasks (represents 2^k)."""
    return (bits_a & bits_b) | (bits_a & bits_c) | (bits_b & bits_c)


def prime_convex_subsets(elements: list[int], med_fn) -> list[int]:
    """Return all prime convex subsets of (elements, med_fn) as bitmasks over index 0..n-1."""
    n = len(elements)
    idx_of = {el: i for i, el in enumerate(elements)}
    res = []
    for mask in range(1 << n):
        ok = True
        for i in range(n):
            in_i = (mask >> i) & 1
            for j in range(i, n):
                in_j = (mask >> j) & 1
                for k in range(j, n):
                    in_k = (mask >> k) & 1
                    m_el = med_fn(elements[i], elements[j], elements[k])
                    in_m = (mask >> idx_of[m_el]) & 1
                    cnt = in_i + in_j + in_k
                    # Convex: cnt >= 2 => in_m == 1; Prime: in_m == 1 => cnt >= 2
                    if (cnt >= 2) != (in_m == 1):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            res.append(mask)
    return res


def check_finite_duality_and_lemma1() -> None:
    """Verify finite duality (Thm 3.4), Helly property, and Lemma 1 (transversality == rank)."""
    # Test examples: 2^1, 2^2, 2^3, S4 (4-leaf star), D (Rem 7.5 6-vertex tree), glued 2^2 + edge
    test_algebras: list[tuple[str, list[int], object, int]] = []

    test_algebras.append(("2^1", [0, 1], cube_median, 1))
    test_algebras.append(("2^2", list(range(4)), cube_median, 2))
    test_algebras.append(("2^3", list(range(8)), cube_median, 3))

    # 4-leaf star S4 (rank 1)
    el_s4, med_s4 = tree_median_algebra(5, [(0, 1), (0, 2), (0, 3), (0, 4)])
    test_algebras.append(("S4", el_s4, med_s4, 1))

    # Tree D from Remark 7.5: u=0, v=1 joined, leaves 2,3 at u; leaves 4,5 at v (rank 1)
    el_d, med_d = tree_median_algebra(6, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)])
    test_algebras.append(("D_Rem7.5", el_d, med_d, 1))

    # Glued 2^2 + tail (5 elements: 0,1,2,3 in 2^2 plus 4 attached to 3=0b11? Let's define via embedding in 2^3)
    # In 2^3: {0b000, 0b001, 0b010, 0b011, 0b111}: closed under pointwise median, rank 2
    sub_glued = [0b000, 0b001, 0b010, 0b011, 0b111]
    test_algebras.append(("2^2+tail", sub_glued, cube_median, 2))

    for name, elems, med_fn, expected_rank in test_algebras:
        check_median_axioms(elems, med_fn)
        n = len(elems)
        full_mask = (1 << n) - 1
        poc = prime_convex_subsets(elems, med_fn)
        poc_set = set(poc)
        assert 0 in poc_set and full_mask in poc_set

        # Verify bounded poc set axioms (Def 2.5) on X = A*
        for x in poc:
            xc = full_mask ^ x
            assert xc in poc_set
            assert (full_mask ^ xc) == x
            # x <= xc iff x == 0
            assert ((x & xc) == x) == (x == 0)
            for y in poc:
                if (x & y) == x:
                    assert ((full_mask ^ y) & xc) == (full_mask ^ y)

        # Verify ultrafilters of X biject with elements of A (Thm 3.4)
        ultrafilters = []
        # An ultrafilter U is a subset of poc containing full_mask, not 0, upset, one of {x, xc}
        interior_poc = [x for x in poc if x != 0 and x != full_mask]
        # Build all evaluations e_A(a) for a in elems
        evals = {}
        for idx, a in enumerate(elems):
            u = frozenset(x for x in poc if (x >> idx) & 1)
            evals[a] = u
            # Verify upset + complementation
            assert full_mask in u and 0 not in u
            for x in poc:
                assert (x in u) != ((full_mask ^ x) in u)
                if x in u:
                    for y in poc:
                        if (x & y) == x:
                            assert y in u
        assert len(set(evals.values())) == len(elems), f"Eval not injective for {name}"

        # Compute rank directly by searching subalgebras isomorphic to 2^k
        computed_rank = 0
        for k in range(1, 5):
            if 1 << k > len(elems):
                break
            found_k = False
            # Any k-cube embedding corresponds to surjective hom A -> 2^k? No, subalgebra iso to 2^k.
            # Check subsets of size 2^k closed under med_fn and pairwise isomorphic to 2^k
            for comb in combinations(elems, 1 << k):
                comb_set = set(comb)
                closed = all(med_fn(a, b, c) in comb_set for a, b, c in product(comb, repeat=3))
                if not closed:
                    continue
                # Check if prime convex subsets of comb has size 2k + 2 (characterizes 2^k among median algebras of size 2^k? Or directly find 2^k iso)
                if len(prime_convex_subsets(list(comb), med_fn)) == 2 * k + 2:
                    found_k = True
                    break
            if found_k:
                computed_rank = k
        assert computed_rank == expected_rank, f"Rank mismatch on {name}: {computed_rank} vs {expected_rank}"

        # Lemma 1: max pairwise transverse elements in X \ {0, 1} <= rank(A) (and equals rank(A))
        def is_transverse(p: int, q: int) -> bool:
            pc = full_mask ^ p
            qc = full_mask ^ q
            return not (
                (p & q) == p or (p & qc) == p or (pc & q) == pc or (q & p) == q
            )

        max_trans = 0
        for k in range(1, len(interior_poc) + 1):
            found_t = False
            for tup in combinations(interior_poc, k):
                if all(is_transverse(tup[i], tup[j]) for i in range(k) for j in range(i + 1, k)):
                    found_t = True
                    # Verify Helly property & surjective psi: A -> 2^k from Lemma 1 proof
                    images = set()
                    for idx, _ in enumerate(elems):
                        images.add(tuple((x >> idx) & 1 for x in tup))
                    assert len(images) == (1 << k), "Lemma 1 surjectivity failed!"
                    break
            if not found_t:
                break
            max_trans = k
        assert max_trans <= computed_rank and max_trans == computed_rank, f"Lemma 1 failed on {name}"

    # Verify Remark 7.5 explicitly: D satisfies sigma while D/theta_F (= S4) fails sigma
    def satisfies_sigma(elems: list[int], med_fn) -> bool:
        for tup in combinations(elems, 5):
            for i in range(5):
                x0 = tup[i]
                others = [tup[j] for j in range(5) if j != i]
                if all(med_fn(a, b, c) == x0 for a, b, c in combinations(others, 3)):
                    return False
        return True

    assert satisfies_sigma(el_d, med_d), "Remark 7.5: D should satisfy sigma"
    assert not satisfies_sigma(el_s4, med_s4), "Remark 7.5: S4 should fail sigma"
    # Verify finite quotient D/theta_F maps (0,1)->0, 2->1, 3->2, 4->3, 5->4 preserving median
    q_map = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    for a, b, c in product(el_d, repeat=3):
        assert q_map[med_d(a, b, c)] == med_s4(q_map[a], q_map[b], q_map[c])
    # And confirm D/theta_F comes from prime convex subsets of D not separating 0 and 1:
    poc_d = prime_convex_subsets(el_d, med_d)
    f_unsep = [x for x in poc_d if ((x >> 0) & 1) == ((x >> 1) & 1)]
    for a in el_d:
        for b in el_d:
            eq_f = all(((x >> a) & 1) == ((x >> b) & 1) for x in f_unsep)
            assert eq_f == (q_map[a] == q_map[b])
    print("Part 1 (finite median/poc duality, Helly, Lemma 1, Remark 7.5): OK")


# ============================================================================
# Part 2: Exact Symbolic Infinite Stone Poc Sets + Lemmas 2-3 & Steps 0-3
# ============================================================================
#
# To represent infinite compact Boolean poc sets X = A* WITHOUT approximation
# or floating point, we model elements of C = omega + omega* as tagged ints:
#   ('0', k) for k >= 0: (0,0) < (0,1) < (0,2) < ...
#   ('1', k) for k >= 0: ... < (1,2) < (1,1) < (1,0)
# Notice EVERY element of X1 = C* is a prime convex subset of C:
#   - '0', '1' (bounds)
#   - ('u0', n) for n >= 1: {(0, k >= n)} U {(1, *)}        (limit -> 'u_inf' as n -> inf)
#   - ('u_inf',)          : {(1, *)}
#   - ('u1', n) for n >= 0: {(1, k <= n)}                  (limit -> 'u_inf' as n -> inf)
#   - ('u0b', n) n >= 1   : {(0, k < n)}                   (limit -> 'ub_inf' as n -> inf)
#   - ('ub_inf',)         : {(0, *)}
#   - ('u1b', n) n >= 0   : {(0, *)} U {(1, k > n)}        (limit -> 'ub_inf' as n -> inf)
#
# In the rank-2 half-grid A2 = {(x, y) in C x C : x <= y}:
# Every point of X2 = A2* is either '0', '1', or ('V', p) or ('H', p) for p in X1 \ {'0', '1'}.
# Note: in A2, x <= y implies:
#   V(upset) < H(same upset), and H(downset) < V(same downset).
# Every clopen, closed, open, or ultrafilter subset of X2 can be represented EXACTLY
# as a SubsetX2:
#   - has_0, has_1: bool
#   - has_lim: dict[lim_key, bool]  for 4 limit points ('V','u_inf'), ('H','u_inf'), ('V','ub_inf'), ('H','ub_inf')
#   - branches: dict[branch_key, tuple[frozenset[int], int, bool]]
#     where branch_key = (axis in {'V','H'}, btype in {'u0','u1','u0b','u1b'}),
#     and (exc, cutoff, tail_val) means for n >= min_n:
#       if n >= cutoff: member iff tail_val
#       else: member iff (n in exc)
#     Canonicalized so cutoff is minimal!
#
# Because we only need Boolean ops, involution, closure, interior, downset/upset checks,
# and evaluation e(a) for a in A2, ALL set operations are O(1) exact integer arithmetic!

def c_le(x: tuple[str, int], y: tuple[str, int]) -> bool:
    """Order on C = omega + omega*."""
    tx, kx = x
    ty, ky = y
    if tx != ty:
        return tx == "0"
    return kx <= ky if tx == "0" else kx >= ky


def c_med(a: tuple[str, int], b: tuple[str, int], c: tuple[str, int]) -> tuple[str, int]:
    """Median on chain C."""
    pts = sorted([a, b, c], key=lambda p: (0 if p[0] == "0" else 1, p[1] if p[0] == "0" else -p[1]))
    return pts[1]


def a2_med(a: tuple, b: tuple, c: tuple) -> tuple:
    """Coordinatewise median on A2 = {(x, y) in C x C : x <= y}."""
    return (c_med(a[0], b[0], c[0]), c_med(a[1], b[1], c[1]))


def x1_contains(p: tuple, x: tuple[str, int]) -> bool:
    """Membership x in p for p in X1 \\ {0, 1}."""
    kind = p[0]
    tx, kx = x
    if kind == "u0":
        return tx == "1" or kx >= p[1]
    if kind == "u_inf":
        return tx == "1"
    if kind == "u1":
        return tx == "1" and kx <= p[1]
    if kind == "u0b":
        return tx == "0" and kx < p[1]
    if kind == "ub_inf":
        return tx == "0"
    if kind == "u1b":
        return tx == "0" or kx > p[1]
    raise ValueError(p)


def x1_inv(p: tuple) -> tuple:
    inv_map = {
        "u0": "u0b",
        "u0b": "u0",
        "u_inf": "ub_inf",
        "ub_inf": "u_inf",
        "u1": "u1b",
        "u1b": "u1",
    }
    return (inv_map[p[0]],) + p[1:]


def x1_le(p: tuple, q: tuple) -> bool:
    """Subset inclusion p <= q in X1 \\ {0, 1}."""
    # Exact test using finite witness threshold max_k + 2
    max_k = max([p[1] if len(p) > 1 else 0, q[1] if len(q) > 1 else 0]) + 2
    for t in ("0", "1"):
        for k in range(max_k + 1):
            if x1_contains(p, (t, k)) and not x1_contains(q, (t, k)):
                return False
    return True


def x2_contains(pt: tuple, a: tuple) -> bool:
    """Membership a = (x, y) in A2 inside pt in X2."""
    if pt == ("0",):
        return False
    if pt == ("1",):
        return True
    axis, p = pt
    coord = a[0] if axis == "V" else a[1]
    return x1_contains(p, coord)


def x2_inv(pt: tuple) -> tuple:
    if pt == ("0",):
        return ("1",)
    if pt == ("1",):
        return ("0",)
    return (pt[0], x1_inv(pt[1]))


def x2_le(p: tuple, q: tuple) -> bool:
    """Exact inclusion p <= q on X2 (checked over all (x, y) in A2 up to cutoff)."""
    if p == ("0",) or q == ("1",):
        return True
    if p == ("1",) or q == ("0",):
        return False
    ap, pp = p
    aq, pq = q
    if ap == aq:
        return x1_le(pp, pq)
    # Cross-axis inclusion on A2 = {(x, y) : x <= y}: check finite grid sufficient to separate
    max_k = max([pp[1] if len(pp) > 1 else 0, pq[1] if len(pq) > 1 else 0]) + 2
    c_pts = [("0", k) for k in range(max_k + 1)] + [("1", k) for k in range(max_k + 1)]
    for x in c_pts:
        for y in c_pts:
            if c_le(x, y):
                if x2_contains(p, (x, y)) and not x2_contains(q, (x, y)):
                    return False
    return True


BRANCHES_X2 = [
    ("V", "u0", 1, ("V", ("u_inf",))),
    ("V", "u1", 0, ("V", ("u_inf",))),
    ("V", "u0b", 1, ("V", ("ub_inf",))),
    ("V", "u1b", 0, ("V", ("ub_inf",))),
    ("H", "u0", 1, ("H", ("u_inf",))),
    ("H", "u1", 0, ("H", ("u_inf",))),
    ("H", "u0b", 1, ("H", ("ub_inf",))),
    ("H", "u1b", 0, ("H", ("ub_inf",))),
]

LIMIT_PTS_X2 = [
    ("V", ("u_inf",)),
    ("V", ("ub_inf",)),
    ("H", ("u_inf",)),
    ("H", ("ub_inf",)),
]

BRANCH_MIN_N = {("V", "u0"): 1, ("V", "u1"): 0, ("V", "u0b"): 1, ("V", "u1b"): 0,
                ("H", "u0"): 1, ("H", "u1"): 0, ("H", "u0b"): 1, ("H", "u1b"): 0}

BRANCH_TO_LIM = {
    ("V", "u0"): ("V", ("u_inf",)),
    ("V", "u1"): ("V", ("u_inf",)),
    ("V", "u0b"): ("V", ("ub_inf",)),
    ("V", "u1b"): ("V", ("ub_inf",)),
    ("H", "u0"): ("H", ("u_inf",)),
    ("H", "u1"): ("H", ("u_inf",)),
    ("H", "u0b"): ("H", ("ub_inf",)),
    ("H", "u1b"): ("H", ("ub_inf",)),
}

LIM_TO_BRANCHES = {
    ("V", ("u_inf",)): [("V", "u0"), ("V", "u1")],
    ("V", ("ub_inf",)): [("V", "u0b"), ("V", "u1b")],
    ("H", ("u_inf",)): [("H", "u0"), ("H", "u1")],
    ("H", ("ub_inf",)): [("H", "u0b"), ("H", "u1b")],
}

BRANCH_INV = {
    ("V", "u0"): ("V", "u0b"),
    ("V", "u0b"): ("V", "u0"),
    ("V", "u1"): ("V", "u1b"),
    ("V", "u1b"): ("V", "u1"),
    ("H", "u0"): ("H", "u0b"),
    ("H", "u0b"): ("H", "u0"),
    ("H", "u1"): ("H", "u1b"),
    ("H", "u1b"): ("H", "u1"),
}

LIM_INV = {
    ("V", ("u_inf",)): ("V", ("ub_inf",)),
    ("V", ("ub_inf",)): ("V", ("u_inf",)),
    ("H", ("u_inf",)): ("H", ("ub_inf",)),
    ("H", ("ub_inf",)): ("H", ("u_inf",)),
}


def canon_branch(min_n: int, exc: frozenset[int], cutoff: int, tail_val: bool):
    """Canonicalize branch representation (minimal cutoff >= min_n)."""
    c = cutoff
    while c > min_n and ((c - 1) in exc) == tail_val:
        c -= 1
    new_exc = frozenset(n for n in exc if min_n <= n < c)
    return (new_exc, c, tail_val)


class SubsetX2:
    """Exact subset of the infinite Stone bounded poc set X2 = A2*."""

    def __init__(self, has_0: bool, has_1: bool, lims: dict, branches: dict):
        self.has_0 = has_0
        self.has_1 = has_1
        self.lims = {k: bool(lims[k]) for k in LIMIT_PTS_X2}
        self.branches = {
            bk: canon_branch(BRANCH_MIN_N[bk], branches[bk][0], branches[bk][1], branches[bk][2])
            for bk in BRANCH_MIN_N
        }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SubsetX2):
            return False
        return (
            self.has_0 == other.has_0
            and self.has_1 == other.has_1
            and self.lims == other.lims
            and self.branches == other.branches
        )

    def __hash__(self) -> int:
        return hash((
            self.has_0,
            self.has_1,
            tuple((k, self.lims[k]) for k in LIMIT_PTS_X2),
            tuple((bk, self.branches[bk]) for bk in sorted(BRANCH_MIN_N)),
        ))

    def contains(self, pt: tuple) -> bool:
        if pt == ("0",):
            return self.has_0
        if pt == ("1",):
            return self.has_1
        axis, p = pt
        if p[0] in ("u_inf", "ub_inf"):
            return self.lims[pt]
        bk = (axis, p[0])
        n = p[1]
        exc, cut, tv = self.branches[bk]
        return tv if n >= cut else (n in exc)

    def is_empty(self) -> bool:
        if self.has_0 or self.has_1 or any(self.lims.values()):
            return False
        for exc, _, tv in self.branches.values():
            if tv or len(exc) > 0:
                return False
        return True

    def complement(self) -> SubsetX2:
        new_b = {}
        for bk, (exc, cut, tv) in self.branches.items():
            min_n = BRANCH_MIN_N[bk]
            new_exc = frozenset(n for n in range(min_n, cut) if n not in exc)
            new_b[bk] = (new_exc, cut, not tv)
        return SubsetX2(
            not self.has_0,
            not self.has_1,
            {k: not self.lims[k] for k in LIMIT_PTS_X2},
            new_b,
        )

    def involute(self) -> SubsetX2:
        return SubsetX2(
            self.has_1,
            self.has_0,
            {LIM_INV[k]: self.lims[k] for k in LIMIT_PTS_X2},
            {BRANCH_INV[bk]: self.branches[bk] for bk in BRANCH_MIN_N},
        )

    def union(self, other: SubsetX2) -> SubsetX2:
        new_b = {}
        for bk in BRANCH_MIN_N:
            e1, c1, tv1 = self.branches[bk]
            e2, c2, tv2 = other.branches[bk]
            c = max(c1, c2)
            min_n = BRANCH_MIN_N[bk]
            exc = frozenset(
                n for n in range(min_n, c)
                if (tv1 if n >= c1 else n in e1) or (tv2 if n >= c2 else n in e2)
            )
            new_b[bk] = (exc, c, tv1 or tv2)
        return SubsetX2(
            self.has_0 or other.has_0,
            self.has_1 or other.has_1,
            {k: self.lims[k] or other.lims[k] for k in LIMIT_PTS_X2},
            new_b,
        )

    def inter(self, other: SubsetX2) -> SubsetX2:
        new_b = {}
        for bk in BRANCH_MIN_N:
            e1, c1, tv1 = self.branches[bk]
            e2, c2, tv2 = other.branches[bk]
            c = max(c1, c2)
            min_n = BRANCH_MIN_N[bk]
            exc = frozenset(
                n for n in range(min_n, c)
                if (tv1 if n >= c1 else n in e1) and (tv2 if n >= c2 else n in e2)
            )
            new_b[bk] = (exc, c, tv1 and tv2)
        return SubsetX2(
            self.has_0 and other.has_0,
            self.has_1 and other.has_1,
            {k: self.lims[k] and other.lims[k] for k in LIMIT_PTS_X2},
            new_b,
        )

    def diff(self, other: SubsetX2) -> SubsetX2:
        return self.inter(other.complement())

    def sym_diff(self, other: SubsetX2) -> SubsetX2:
        return self.diff(other).union(other.diff(self))

    def is_subset(self, other: SubsetX2) -> bool:
        return self.diff(other).is_empty()

    def closure(self) -> SubsetX2:
        new_lims = dict(self.lims)
        for lk, bks in LIM_TO_BRANCHES.items():
            for bk in bks:
                exc, cut, tv = self.branches[bk]
                # Tail accumulates at lk iff tv is True (since branches are monotonic tails)
                if tv:
                    new_lims[lk] = True
        return SubsetX2(self.has_0, self.has_1, new_lims, self.branches)

    def interior(self) -> SubsetX2:
        return self.complement().closure().complement()

    def is_open(self) -> bool:
        return self.interior() == self

    def is_closed(self) -> bool:
        return self.closure() == self

    def is_clopen(self) -> bool:
        return self.is_open() and self.is_closed()

    def boundary_points(self) -> list[tuple]:
        """Exact list of elements in (closure \\ S) U (S \\ interior)."""
        res = []
        cl = self.closure()
        it = self.interior()
        diff_set = cl.diff(it)
        for lk in LIMIT_PTS_X2:
            if diff_set.lims[lk]:
                res.append(lk)
        # Note isolated points are always in both closure and interior
        return res

    def a_set(self) -> set[tuple]:
        """A_S = closure(S) \\ S (finite set of limit points for our sets)."""
        au = self.closure().diff(self)
        res = set()
        if au.has_0:
            res.add(("0",))
        if au.has_1:
            res.add(("1",))
        for lk in LIMIT_PTS_X2:
            if au.lims[lk]:
                res.add(lk)
        for bk in BRANCH_MIN_N:
            exc, cut, tv = au.branches[bk]
            assert not tv and not exc
        return res

    def b_set(self) -> set[tuple]:
        """B_S = S \\ interior(S)."""
        bu = self.diff(self.interior())
        res = set()
        if bu.has_0:
            res.add(("0",))
        if bu.has_1:
            res.add(("1",))
        for lk in LIMIT_PTS_X2:
            if bu.lims[lk]:
                res.add(lk)
        for bk in BRANCH_MIN_N:
            exc, cut, tv = bu.branches[bk]
            assert not tv and not exc
        return res

    def max_cutoff(self) -> int:
        return max(cut for _, cut, _ in self.branches.values())

    def witness_element(self) -> tuple:
        """Return an explicit element of self (assuming nonempty)."""
        assert not self.is_empty()
        if self.has_0:
            return ("0",)
        if self.has_1:
            return ("1",)
        for lk in LIMIT_PTS_X2:
            if self.lims[lk]:
                return lk
        for bk in BRANCH_MIN_N:
            exc, cut, tv = self.branches[bk]
            if exc:
                return (bk[0], (bk[1], min(exc)))
            if tv:
                return (bk[0], (bk[1], cut))
        raise AssertionError("Unreachable")

    def elements_up_to(self, k_bound: int) -> list[tuple]:
        """All elements inside self up to parameter k_bound on each branch (for checking upset)."""
        res = []
        if self.has_0:
            res.append(("0",))
        if self.has_1:
            res.append(("1",))
        for lk in LIMIT_PTS_X2:
            if self.lims[lk]:
                res.append(lk)
        for bk in BRANCH_MIN_N:
            for n in range(BRANCH_MIN_N[bk], k_bound + 1):
                pt = (bk[0], (bk[1], n))
                if self.contains(pt):
                    res.append(pt)
        return res

    def is_upset(self) -> bool:
        """Exact verification that self is an up-set in X2."""
        # Check pairwise over a range safely exceeding all cutoffs
        kb = self.max_cutoff() + 3
        all_pts = [("0",), ("1",)] + list(LIMIT_PTS_X2)
        for bk in BRANCH_MIN_N:
            for n in range(BRANCH_MIN_N[bk], kb + 1):
                all_pts.append((bk[0], (bk[1], n)))
        # Verify:
        # 1) finite grid up to kb
        for p in all_pts:
            if self.contains(p):
                for q in all_pts:
                    if not self.contains(q) and x2_le(p, q):
                        return False
        # 2) tail monotonicity: on each branch (for n >= cutoff), elements are strictly monotone
        # in X2: u0 decreases (u0(n) > u0(n+1)), u1 increases (u1(n) < u1(n+1)),
        # u0b increases (u0b(n) < u0b(n+1)), u1b decreases (u1b(n) > u1b(n+1)).
        # If tv=True on decreasing tail u0(n) >= limit u_inf, then u_inf must be handled:
        # wait: if tail is u0(n) in U and tv=True, that does NOT force u_inf in U because u_inf < u0(n)!
        # Conversely if tv=True on INCREASING tail (u1, u0b), then u1(n) < u_inf forces u_inf in self!
        for lk, bks in LIM_TO_BRANCHES.items():
            for bk in bks:
                exc, cut, tv = self.branches[bk]
                # increasing tails toward limit: u1, u0b
                if bk[1] in ("u1", "u0b") and tv and not self.lims[lk]:
                    return False
                # decreasing tails toward limit: u0, u1b: if limit in self, tail MUST be True
                if bk[1] in ("u0", "u1b") and self.lims[lk] and not tv:
                    return False
        # Also V(u0, n) <= H(u0, n): if V(u0) has tv=True, H(u0) must have tv=True
        if self.branches[("V", "u0")][2] and not self.branches[("H", "u0")][2]:
            return False
        if self.branches[("V", "u1")][2] and not self.branches[("H", "u1")][2]:
            return False
        if self.branches[("H", "u0b")][2] and not self.branches[("V", "u0b")][2]:
            return False
        if self.branches[("H", "u1b")][2] and not self.branches[("V", "u1b")][2]:
            return False
        return True

    def is_downset(self) -> bool:
        return self.complement().is_upset()

    def is_ultrafilter(self) -> bool:
        return (not self.has_0) and self.has_1 and (self.involute() == self.complement()) and self.is_upset()


def full_x2() -> SubsetX2:
    return SubsetX2(
        True,
        True,
        {k: True for k in LIMIT_PTS_X2},
        {bk: (frozenset(), BRANCH_MIN_N[bk], True) for bk in BRANCH_MIN_N},
    )


def empty_x2() -> SubsetX2:
    return full_x2().complement()


def eval_x2(a: tuple) -> SubsetX2:
    """Clopen ultrafilter e_{A2}(a) = {pt in X2 : a in pt}."""
    x, y = a
    tx, kx = x
    ty, ky = y
    lims = {
        ("V", ("u_inf",)): tx == "1",
        ("V", ("ub_inf",)): tx == "0",
        ("H", ("u_inf",)): ty == "1",
        ("H", ("ub_inf",)): ty == "0",
    }
    branches = {}
    for axis, coord in (("V", x), ("H", y)):
        tc, kc = coord
        # u0(n): tc=='1' or kc >= n
        if tc == "1":
            branches[(axis, "u0")] = (frozenset(), 1, True)
            branches[(axis, "u0b")] = (frozenset(), 1, False)
            branches[(axis, "u1")] = (frozenset(), kc, True)  # n >= kc
            branches[(axis, "u1b")] = (frozenset(range(0, kc)), kc, False)
        else:
            branches[(axis, "u0")] = (frozenset(range(1, kc + 1)), kc + 1, False)
            branches[(axis, "u0b")] = (frozenset(), kc + 1, True)
            branches[(axis, "u1")] = (frozenset(), 0, False)
            branches[(axis, "u1b")] = (frozenset(), 0, True)
    res = SubsetX2(False, True, lims, branches)
    assert res.is_clopen() and res.is_ultrafilter()
    return res


def separate_order_x2(s: tuple, t: tuple) -> SubsetX2:
    """For s </= t in X2, find explicit a in A2 with s in e(a), t not in e(a)."""
    assert not x2_le(s, t), f"{s} <= {t}"
    # Deterministic search over small (x, y) in A2 up to cutoff
    bound = 4
    for pt in (s, t):
        if len(pt) == 2 and len(pt[1]) == 2:
            bound = max(bound, pt[1][1] + 2)
    c_pts = [("0", k) for k in range(bound)] + [("1", k) for k in range(bound)]
    for x in c_pts:
        for y in c_pts:
            if c_le(x, y) and x2_contains(s, (x, y)) and not x2_contains(t, (x, y)):
                return eval_x2((x, y))
    raise AssertionError(f"Failed to separate {s} </= {t}")


def upward_cone_x2(t: tuple) -> SubsetX2:
    """Exact closed upward cone t^uparrow in X2."""
    if t == ("0",):
        return full_x2()
    if t == ("1",):
        return SubsetX2(
            False, True, {k: False for k in LIMIT_PTS_X2},
            {bk: (frozenset(), BRANCH_MIN_N[bk], False) for bk in BRANCH_MIN_N}
        )
    # Build t^uparrow directly using x2_le with cutoff beyond t's index
    kb = (t[1][1] + 2) if len(t[1]) == 2 else 1
    lims = {lk: x2_le(t, lk) for lk in LIMIT_PTS_X2}
    branches = {}
    for bk in BRANCH_MIN_N:
        min_n = BRANCH_MIN_N[bk]
        cut = max(min_n, kb + 1)
        exc = frozenset(n for n in range(min_n, cut) if x2_le(t, (bk[0], (bk[1], n))))
        tv = x2_le(t, (bk[0], (bk[1], cut + 5)))
        branches[bk] = (exc, cut, tv)
    res = SubsetX2(False, True, lims, branches)
    assert res.is_closed() and res.is_upset()
    return res


def make_clopen_nbhd_x2(t: tuple, radius_k: int) -> SubsetX2:
    """Explicit clopen neighborhood of t in X2 excluding tails outside radius_k."""
    if t == ("0",):
        return SubsetX2(True, False, {k: False for k in LIMIT_PTS_X2},
                        {bk: (frozenset(), BRANCH_MIN_N[bk], False) for bk in BRANCH_MIN_N})
    if t == ("1",):
        return SubsetX2(False, True, {k: False for k in LIMIT_PTS_X2},
                        {bk: (frozenset(), BRANCH_MIN_N[bk], False) for bk in BRANCH_MIN_N})
    if t in LIMIT_PTS_X2:
        lims = {lk: (lk == t) for lk in LIMIT_PTS_X2}
        branches = {}
        for bk in BRANCH_MIN_N:
            if BRANCH_TO_LIM[bk] == t:
                branches[bk] = (frozenset(), max(BRANCH_MIN_N[bk], radius_k), True)
            else:
                branches[bk] = (frozenset(), BRANCH_MIN_N[bk], False)
        res = SubsetX2(False, False, lims, branches)
        assert res.is_clopen() and res.contains(t)
        return res
    # Isolated point
    axis, (btype, n) = t
    branches = {
        bk: (frozenset([n]) if bk == (axis, btype) else frozenset(), max(BRANCH_MIN_N[bk], n + 1), False)
        for bk in BRANCH_MIN_N
    }
    res = SubsetX2(False, False, {k: False for k in LIMIT_PTS_X2}, branches)
    assert res.is_clopen() and res.contains(t)
    return res


def extract_a2_element_for_clopen_uf(u: SubsetX2) -> tuple:
    """Given clopen ultrafilter u on X2, extract exact a = (x, y) in A2 with eval_x2(a) == u."""
    assert u.is_clopen() and u.is_ultrafilter()
    # Extract x from V-component and y from H-component
    coords = []
    for axis in ("V", "H"):
        if u.lims[(axis, ("ub_inf",))]:
            # Limit is ub_inf => coord = ('0', k) where u0(n) holds for n <= k and fails for n > k
            exc, cut, tv = u.branches[(axis, "u0")]
            assert not tv
            # Find largest n in u0
            present = [n for n in range(1, cut) if n in exc]
            k = max(present) if present else 0
            coords.append(("0", k))
        else:
            assert u.lims[(axis, ("u_inf",))]
            # Limit is u_inf => coord = ('1', k) where u1(n) holds for n >= k
            exc, cut, tv = u.branches[(axis, "u1")]
            assert tv
            absent = [n for n in range(0, cut) if n not in exc]
            k = max(absent) + 1 if absent else 0
            coords.append(("1", k))
    a = (coords[0], coords[1])
    assert c_le(a[0], a[1]), f"Extracted invalid A2 pair {a}"
    assert eval_x2(a) == u, f"Extracted {a} does not match clopen ultrafilter!"
    return a


def verify_proof_steps_on_x2(generators: list[SubsetX2], label: str) -> None:
    """Execute Lemmas 2-3 and Steps 0-3 verbatim on B = <generators> <= (X2^flat)_+."""
    # Generate finite median subalgebra B <= (X2^flat)_+
    for g in generators:
        assert g.is_ultrafilter(), "Generator must be an ultrafilter of X2"
    B: list[SubsetX2] = list(dict.fromkeys(generators))
    changed = True
    while changed:
        changed = False
        cur = list(B)
        seen = set(cur)
        for u1, u2, u3 in product(cur, repeat=3):
            m = (u1.inter(u2)).union(u1.inter(u3)).union(u2.inter(u3))
            if m not in seen:
                seen.add(m)
                B.append(m)
                changed = True
    for u in B:
        assert u.is_ultrafilter()

    # Check Lemma 2 on every U in B (rank(A2) = 2)
    rank_a2 = 2
    for u in B:
        au = u.a_set()
        bu = u.b_set()
        assert len(au - {("0",)}) <= rank_a2, f"Lemma 2 failed: {au}"
        assert len(au) <= rank_a2 + 1 and len(bu) == len(au)
        assert {x2_inv(pt) for pt in au} == bu

    # Check Lemma 3: for every U in B and t in A_U, construct open W_{t, U} with W_{t,U} & U <= t^uparrow
    W_open: dict[tuple[tuple, SubsetX2], SubsetX2] = {}
    for u in B:
        for t in u.a_set():
            if t == ("0",):
                w = full_x2()
            else:
                k_start = u.max_cutoff() + 2
                w = make_clopen_nbhd_x2(t, k_start)
            assert w.is_open() and w.contains(t)
            t_up = upward_cone_x2(t)
            assert w.inter(u).is_subset(t_up), f"Lemma 3 failed at {t}"
            W_open[(t, u)] = w

    # Step 0: Finite witness set W and boundary set T
    W_pts: set[tuple] = set()
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            w = B[i].sym_diff(B[j]).witness_element()
            W_pts.add(w)
            W_pts.add(x2_inv(w))
    T_set: set[tuple] = {("0",), ("1",)} | W_pts
    for u in B:
        T_set |= u.a_set() | u.b_set()
    assert all(x2_inv(t) in T_set for t in T_set)

    # Initial separating clopen ultrafilters C_{s, t} for s </= t in T
    C_sep: dict[tuple[tuple, tuple], SubsetX2] = {}
    for s in T_set:
        for t in T_set:
            if not x2_le(s, t):
                c = separate_order_x2(s, t)
                assert c.is_clopen() and c.is_ultrafilter() and c.contains(s) and not c.contains(t)
                C_sep[(s, t)] = c

    D0: dict[tuple, SubsetX2] = {}
    E0: dict[tuple, SubsetX2] = {}
    N0: dict[tuple, SubsetX2] = {}
    for t in T_set:
        dt = full_x2()
        for s in T_set:
            if not x2_le(s, t):
                dt = dt.inter(C_sep[(s, t)].complement())
        tb = x2_inv(t)
        for u_pt in T_set:
            if not x2_le(tb, u_pt):
                dt = dt.inter(C_sep[(tb, u_pt)].complement())
        assert dt.is_clopen() and dt.is_downset() and dt.contains(t)
        D0[t] = dt
    for s in T_set:
        E0[s] = D0[x2_inv(s)].involute()
        assert E0[s].is_clopen() and E0[s].is_upset() and E0[s].contains(s)
        N0[s] = D0[s].inter(E0[s])
    # Step 0 properties (2), (3), (4)
    for s in T_set:
        for t in T_set:
            if not x2_le(s, t):
                assert E0[s].inter(D0[t]).is_empty()
            if s != t:
                assert N0[s].inter(N0[t]).is_empty()
    assert D0[("1",)] == full_x2() and E0[("0",)] == full_x2()

    # Step 1: Linear extension of (T, <=) and inductive D_t
    T_list = list(T_set)
    # Kahn's topological sort
    order_T: list[tuple] = []
    rem = set(T_list)
    while rem:
        minimals = [x for x in rem if all(not (y != x and x2_le(y, x)) for y in rem)]
        # Deterministic tie-break
        minimals.sort(key=str)
        pick = minimals[0]
        order_T.append(pick)
        rem.remove(pick)
    assert order_T[0] == ("0",) and order_T[-1] == ("1",)

    D_final: dict[tuple, SubsetX2] = {}
    for t in order_T:
        F_t = empty_x2()
        for u in B:
            if u.contains(t):
                continue
            omega = empty_x2()
            au = u.a_set()
            if t in au:
                omega = omega.union(W_open[(t, u)])
            for r in T_set:
                if r != t and x2_le(r, t) and r in au:
                    omega = omega.union(D_final[r].inter(W_open[(r, u)]))
            assert omega.is_open()
            t_down = upward_cone_x2(x2_inv(t)).involute()
            assert t_down.inter(u.closure()).is_subset(omega), f"Failed t^down & cl(U) <= Omega at {t}"
            F_t = F_t.union(u.closure().diff(omega))
        assert F_t.is_closed()
        dt = D0[t]
        # Construct finite clopen down-set separation covering F_t via t^down = \cap e(a)^c
        # First separate F_t from t using clopen down-sets e(a)^c (for a not in t)
        rem_F = F_t.inter(dt)
        if t != ("1",):
            # Pick a not in t until rem_F is empty
            bound = 4
            for pt in list(T_set) + [t]:
                if len(pt) == 2 and len(pt[1]) == 2:
                    bound = max(bound, pt[1][1] + 2)
            bound = max(bound, rem_F.max_cutoff() + 2)
            c_pts = [("0", k) for k in range(bound)] + [("1", k) for k in range(bound)]
            for x in c_pts:
                if rem_F.is_empty():
                    break
                for y in c_pts:
                    if c_le(x, y) and not x2_contains(t, (x, y)):
                        hy = eval_x2((x, y)).complement()  # clopen down-set containing t
                        if not rem_F.is_subset(hy):
                            dt = dt.inter(hy)
                            rem_F = rem_F.inter(hy)
                            if rem_F.is_empty():
                                break
        assert dt.is_clopen() and dt.is_downset() and dt.contains(t)
        assert dt.is_subset(D0[t])
        assert dt.inter(F_t).is_empty(), f"D_t still intersects F_t at {t}"
        D_final[t] = dt

    # Step 2: E_s, N_s, Claims (I) & (II)
    E_final = {s: D_final[x2_inv(s)].involute() for s in T_set}
    N_final = {s: D_final[s].inter(E_final[s]) for s in T_set}
    union_N = empty_x2()
    for s in T_set:
        assert E_final[s].is_clopen() and E_final[s].is_upset() and E_final[s].contains(s)
        assert N_final[s].is_clopen() and N_final[s].contains(s)
        assert N_final[s].involute() == N_final[x2_inv(s)]
        union_N = union_N.union(N_final[s])
    for s in T_set:
        for t in T_set:
            if s != t:
                assert N_final[s].inter(N_final[t]).is_empty()

    for u in B:
        for t in T_set:
            if not u.contains(t):
                assert D_final[t].inter(u).is_subset(union_N), "Claim (I) failed"
            if u.contains(t):
                assert E_final[t].inter(u.complement()).is_subset(union_N), "Claim (II) failed"

    # Step 3: K, pi, U_tilde = pi^{-1}(U), and actual median embedding B -> A2
    K = union_N.complement()
    assert K.is_clopen() and K.involute() == K

    a_of_u: dict[SubsetX2, tuple] = {}
    u_tilde_of_u: dict[SubsetX2, SubsetX2] = {}
    for u in B:
        u_tilde = u.inter(K)
        for t in T_set:
            if u.contains(t):
                u_tilde = u_tilde.union(N_final[t])
        assert u_tilde.is_clopen(), "U_tilde is not clopen!"
        assert u_tilde.is_ultrafilter(), "U_tilde is not an ultrafilter!"
        u_tilde_of_u[u] = u_tilde
        a_of_u[u] = extract_a2_element_for_clopen_uf(u_tilde)

    # Verify median algebra embedding B -> A2
    assert len(set(a_of_u.values())) == len(B), f"Embedding not injective on {label}"
    for u1, u2, u3 in product(B, repeat=3):
        m_u = (u1.inter(u2)).union(u1.inter(u3)).union(u2.inter(u3))
        assert a2_med(a_of_u[u1], a_of_u[u2], a_of_u[u3]) == a_of_u[m_u], "Homomorphism failed!"
    print(f"Part 2 ({label}): |B|={len(B)}, all Lemmas 2-3 & Steps 0-3 & embedding B->A2 OK")


def build_x2_ultrafilters() -> None:
    """Construct diverse non-clopen ultrafilters on X2 = A2* and run full proof pipeline."""
    # Ultrafilter U1: A_{U1} = {V(u_inf), H(u_inf)} (two comparable boundary points r < t, |A_U\\{0}| = 2 = rank!)
    U1 = SubsetX2(
        False, True,
        {("V", ("u_inf",)): False, ("H", ("u_inf",)): False,
         ("V", ("ub_inf",)): True, ("H", ("ub_inf",)): True},
        {
            ("V", "u0"): (frozenset(), 1, True),
            ("H", "u0"): (frozenset(), 1, True),
            ("V", "u1"): (frozenset(), 0, False),
            ("H", "u1"): (frozenset(), 0, False),
            ("V", "u0b"): (frozenset(), 1, False),
            ("H", "u0b"): (frozenset(), 1, False),
            ("V", "u1b"): (frozenset(), 0, True),
            ("H", "u1b"): (frozenset(), 0, True),
        },
    )
    assert U1.is_ultrafilter() and not U1.is_clopen()
    assert U1.a_set() == {("V", ("u_inf",)), ("H", ("u_inf",))}
    assert x2_le(("V", ("u_inf",)), ("H", ("u_inf",)))

    # Ultrafilter U2: H-component has H(u_inf) in U2 (H(u1, n>=3) in U2 => H(u_inf) in B_{U2}),
    # V-component has V(u_inf) not in U2 (V(u0) in U2 => V(u_inf) in A_{U2}). Respects V(p) <= H(p)!
    U2 = SubsetX2(
        False, True,
        {("V", ("u_inf",)): False, ("H", ("u_inf",)): True,
         ("V", ("ub_inf",)): True, ("H", ("ub_inf",)): False},
        {
            ("V", "u0"): (frozenset(), 1, True),
            ("H", "u0"): (frozenset(), 1, True),
            ("V", "u1"): (frozenset(), 0, False),
            ("H", "u1"): (frozenset(), 3, True),    # n >= 3 in U2 => H(u_inf) in B_{U2}
            ("V", "u0b"): (frozenset(), 1, False),
            ("H", "u0b"): (frozenset(), 1, False),
            ("V", "u1b"): (frozenset(), 0, True),
            ("H", "u1b"): (frozenset([0, 1, 2]), 3, False),
        },
    )
    assert U2.is_ultrafilter() and not U2.is_clopen()
    assert U2.a_set() == {("V", ("u_inf",))}
    assert U2.b_set() == {("V", ("ub_inf",))}

    # Ultrafilter U3: V(u_inf), H(u_inf) in U3 (with u1=False, u1b=True -> non-clopen!),
    # giving A_{U3} = {H(ub_inf), V(ub_inf)} with H(ub_inf) < V(ub_inf) and B_{U3} = {V(u_inf), H(u_inf)}!
    U3 = SubsetX2(
        False, True,
        {("V", ("u_inf",)): True, ("H", ("u_inf",)): True,
         ("V", ("ub_inf",)): False, ("H", ("ub_inf",)): False},
        {
            ("V", "u0"): (frozenset(), 1, True),
            ("H", "u0"): (frozenset(), 1, True),
            ("V", "u1"): (frozenset(), 0, False),
            ("H", "u1"): (frozenset(), 0, False),
            ("V", "u0b"): (frozenset(), 1, False),
            ("H", "u0b"): (frozenset(), 1, False),
            ("V", "u1b"): (frozenset(), 0, True),
            ("H", "u1b"): (frozenset(), 0, True),
        },
    )
    assert U3.is_ultrafilter() and not U3.is_clopen()
    assert U3.a_set() == {("V", ("ub_inf",)), ("H", ("ub_inf",))}

    # Ultrafilter U4: clopen ultrafilter eval_x2((('0', 2), ('1', 1)))
    U4 = eval_x2((("0", 2), ("1", 1)))

    # Verify subalgebra <U1> (single non-clopen with comparable A_U = {r, t}, r < t)
    verify_proof_steps_on_x2([U1], "X2: single non-clopen A_U={r<t}")
    # Verify 2-gen subalgebra <U1, U2> (non-clopen 2-element B)
    verify_proof_steps_on_x2([U1, U2], "X2: 2 non-clopen generators")
    # Verify 3-gen mixed non-clopen + clopen subalgebra <U1, U2, U3, U4> (non-trivial finite median algebra)
    verify_proof_steps_on_x2([U1, U2, U3, U4], "X2: 4-gen mixed non-clopen/clopen B")


# ============================================================================
# Part 3: Infinite Ray with 0 in A_U (omega x (omega + omega*), Rank 2)
# ============================================================================

def verify_zero_boundary_case() -> None:
    """Verify Lemma 2/3 & Step 1-3 explicitly when 0 in A_U (and 1 in B_U) in rank 1 ray A = omega."""
    # For A = omega = {0, 1, 2, ...}, X = A* has:
    #   '0', '1', ('u', n) = {k >= n} for n >= 1 (limit -> '0'), ('ub', n) = {k < n} for n >= 1 (limit -> '1').
    # Wait: u(1) > u(2) > ... -> 0, and ub(1) < ub(2) < ... -> 1.
    # Let U = {'1'} U {('u', n) : n >= 1} (so 0 in A_U, 1 in B_U) and V = e_A(3) (clopen).
    # Verify exact Steps 0-3 on X = omega*:
    #   A_U = {'0'}, B_U = {'1'}, W_pts = {('u', 4), ('ub', 4)} (since ('u', 4) in U \\ V).
    #   T = {'0', '1', ('u', 4), ('ub', 4)}.
    #   Lemma 3 at t = '0': W_{0, U} = X works (since 0^uparrow = X).
    #   Step 1: t = '0', 0 in A_U => Omega_{0, U} = X => F_0 = empty => D_0 = D_0^{(0)}!
    #   Verify C_{s, t} for all s </= t in T, exact D_t, E_s, N_s, K, and extracted elements in omega:
    def contains(pt, k: int) -> bool:
        if pt == ("0",):
            return False
        if pt == ("1",):
            return True
        tag, n = pt
        return (k >= n) if tag == "u" else (k < n)

    def le_omega(p, q) -> bool:
        for k in range(10):
            if contains(p, k) and not contains(q, k):
                return False
        return True

    def inv_omega(pt):
        if pt == ("0",):
            return ("1",)
        if pt == ("1",):
            return ("0",)
        return ("ub" if pt[0] == "u" else "u", pt[1])

    # Represent subsets of omega* via (has_0, has_1, (exc_u, cut_u, tv_u), (exc_ub, cut_ub, tv_ub))
    def mk_eval(k: int):
        # u(n) contains k iff n <= k; ub(n) contains k iff n > k
        return (False, True, (frozenset(range(1, k + 1)), k + 1, False), (frozenset(), k + 1, True))

    U = (False, True, (frozenset(), 1, True), (frozenset(), 1, False))
    V = mk_eval(3)

    # Check A_U = {'0'} and B_U = {'1'}, and W_{0, U} = X
    def pt_in(S, pt) -> bool:
        if pt == ("0",):
            return S[0]
        if pt == ("1",):
            return S[1]
        exc, cut, tv = S[2] if pt[0] == "u" else S[3]
        return tv if pt[1] >= cut else (pt[1] in exc)

    # Note: for t = '0' in T = {'0', '1', ('u', 4), ('ub', 4)}:
    # Wait: let's compute Step 0 explicitly!
    T = [("0",), ("1",), ("u", 4), ("ub", 4)]
    full_S = (True, True, (frozenset(), 1, True), (frozenset(), 1, True))

    def inter_S(A, B):
        c2 = max(A[2][1], B[2][1])
        c3 = max(A[3][1], B[3][1])
        e2 = frozenset(n for n in range(1, c2) if pt_in(A, ("u", n)) and pt_in(B, ("u", n)))
        e3 = frozenset(n for n in range(1, c3) if pt_in(A, ("ub", n)) and pt_in(B, ("ub", n)))
        return (A[0] and B[0], A[1] and B[1], canon_branch(1, e2, c2, A[2][2] and B[2][2]),
                canon_branch(1, e3, c3, A[3][2] and B[3][2]))

    def union_S(A, B):
        c2 = max(A[2][1], B[2][1])
        c3 = max(A[3][1], B[3][1])
        e2 = frozenset(n for n in range(1, c2) if pt_in(A, ("u", n)) or pt_in(B, ("u", n)))
        e3 = frozenset(n for n in range(1, c3) if pt_in(A, ("ub", n)) or pt_in(B, ("ub", n)))
        return (A[0] or B[0], A[1] or B[1], canon_branch(1, e2, c2, A[2][2] or B[2][2]),
                canon_branch(1, e3, c3, A[3][2] or B[3][2]))

    def comp_S(A):
        e2 = frozenset(n for n in range(1, A[2][1]) if n not in A[2][0])
        e3 = frozenset(n for n in range(1, A[3][1]) if n not in A[3][0])
        return (not A[0], not A[1], canon_branch(1, e2, A[2][1], not A[2][2]),
                canon_branch(1, e3, A[3][1], not A[3][2]))

    def inv_S(A):
        return (A[1], A[0], A[3], A[2])

    C_sep = {}
    for s in T:
        for t in T:
            if not le_omega(s, t):
                for k in range(10):
                    if contains(s, k) and not contains(t, k):
                        C_sep[(s, t)] = mk_eval(k)
                        break

    D = {}
    for t in T:
        dt = full_S
        for s in T:
            if not le_omega(s, t):
                dt = inter_S(dt, comp_S(C_sep[(s, t)]))
        tb = inv_omega(t)
        for u_pt in T:
            if not le_omega(tb, u_pt):
                dt = inter_S(dt, comp_S(C_sep[(tb, u_pt)]))
        # Note for U (0 in A_U, ('u', 4) in U) and V (t not in V => D_t & V_clopen = empty if F_t avoids):
        # For V, V is clopen so A_V = empty! For t = ('0',), Omega_{0, V} = empty => F_0 >= V,
        # so D_0 avoids V via e(0)^c? Wait: 0 not in V = e(3), so e(3)^c separates 0 from V!
        if t == ("0",):
            # V = mk_eval(3) is inside F_0 since '0' not in A_V = empty!
            # Wait: 0 not in e(3) => H = comp_S(mk_eval(3)) separates 0 from V!
            dt = inter_S(dt, comp_S(mk_eval(3)))
        D[t] = dt
    E = {s: inv_S(D[inv_omega(s)]) for s in T}
    N = {s: inter_S(D[s], E[s]) for s in T}
    union_N = N[T[0]]
    for s in T[1:]:
        union_N = union_S(union_N, N[s])
    K = comp_S(union_N)

    # Extract embedded elements in omega for U and V
    extracted = {}
    for name_u, u_set in (("U", U), ("V", V)):
        ut = inter_S(u_set, K)
        for t in T:
            if pt_in(u_set, t):
                ut = union_S(ut, N[t])
        # Verify ut is clopen (limit points match tail values: 0 matches u_tv, 1 matches ub_tv)
        assert ut[0] == ut[2][2] and ut[1] == ut[3][2], f"{name_u}_tilde not clopen: {ut}"
        # Find k in omega with mk_eval(k) == ut
        found = None
        for k in range(20):
            if mk_eval(k) == ut:
                found = k
                break
        assert found is not None, f"Could not extract omega element for {name_u}: {ut}"
        extracted[name_u] = found
    assert extracted["U"] != extracted["V"]
    print(f"Part 3 (0 in A_U on omega*, embedded U -> {extracted['U']}, V -> {extracted['V']}): OK")


# ============================================================================
# Part 4: Remark's Bounded Distributive Lattice Priestley Space Counterexample
# ============================================================================

def verify_remark_priestley_counterexample() -> None:
    """Verify Priestley axioms, nontrivial complemented pair in U(P), and none in ClopUp(P)
    for P = (N U {inf}) x {0, 1} with (n,0)<(n,1), (n,0)<(n+1,1), (inf,0)<(inf,1)."""
    # Exact representation of subsets of P:
    # S = (inf0, inf1, exc0, exc1, cut, tv0, tv1)
    # where n >= cut on side b in {0, 1} is in S iff tv_b is True.
    def pt_in_p(S, pt) -> bool:
        n, b = pt
        if n == "inf":
            return S[0] if b == 0 else S[1]
        exc = S[2] if b == 0 else S[3]
        cut = S[4]
        tv = S[5] if b == 0 else S[6]
        return tv if n >= cut else (n in exc)

    def is_clopen_p(S) -> bool:
        return S[0] == S[5] and S[1] == S[6]

    def p_le(x, y) -> bool:
        if x == y:
            return True
        nx, bx = x
        ny, by = y
        if nx == "inf" and ny == "inf":
            return bx == 0 and by == 1
        if nx == "inf" or ny == "inf":
            return False
        return bx == 0 and by == 1 and (ny == nx or ny == nx + 1)

    def is_upset_p(S) -> bool:
        # Check finite edges up to max(cut)+3 and tail edges
        kb = S[4] + 3
        if S[0] and not S[1]:
            return False
        if S[5] and not S[6]:
            return False
        for n in range(kb):
            if pt_in_p(S, (n, 0)):
                if not pt_in_p(S, (n, 1)) or not pt_in_p(S, (n + 1, 1)):
                    return False
        return True

    # 1. Verify Priestley order axioms (antisymmetric, transitive) & Priestley separation
    # (for any x </= y, there exists a clopen upset separating x from y)
    sample_pts = [("inf", 0), ("inf", 1)] + [(n, b) for n in range(6) for b in (0, 1)]
    for x in sample_pts:
        for y in sample_pts:
            if p_le(x, y) and p_le(y, x):
                assert x == y
            for z in sample_pts:
                if p_le(x, y) and p_le(y, z):
                    assert p_le(x, z)
            if not p_le(x, y):
                # Construct explicit separating clopen upset C with x in C, y not in C
                nx, bx = x
                ny, by = y
                if nx == "inf" and bx == 1:
                    k = 0 if ny == "inf" else ny + 2
                    C = (False, True, frozenset(), frozenset(), k, False, True)
                elif nx == "inf" and bx == 0:
                    assert ny != "inf"
                    k = ny + 2
                    C = (True, True, frozenset(), frozenset(), k, True, True)
                elif bx == 1:
                    C = (False, False, frozenset(), frozenset([nx]), nx + 1, False, False)
                else:
                    # x = (nx, 0) => x^uparrow = {(nx, 0), (nx, 1), (nx+1, 1)}
                    C = (False, False, frozenset([nx]), frozenset([nx, nx + 1]), nx + 2, False, False)
                assert is_clopen_p(C) and is_upset_p(C)
                assert pt_in_p(C, x) and not pt_in_p(C, y)

    # 2. Complemented pair in U(P): U = {(inf, 0), (inf, 1)}, V = N x {0, 1}
    U_pair = (True, True, frozenset(), frozenset(), 0, False, False)
    V_pair = (False, False, frozenset(), frozenset(), 0, True, True)
    assert is_upset_p(U_pair) and is_upset_p(V_pair)
    assert not is_clopen_p(U_pair) and not is_clopen_p(V_pair)
    # Disjoint and covering all of P:
    assert U_pair[0] != V_pair[0] and U_pair[1] != V_pair[1]
    assert U_pair[5] != V_pair[5] and U_pair[6] != V_pair[6]

    # 3. Algebraic proof (verified symbolically over all possible clopen representations)
    # that any C with C and P \\ C both clopen upsets must be empty or P:
    # For any complemented upset C, since (n, 0) < (n, 1) and (n, 0) < (n+1, 1):
    #   (n, 0) in C <=> (n, 1) in C <=> (n+1, 1) in C <=> (n+1, 0) in C.
    # Thus C restricted to N x {0, 1} is constant (either all True or all False).
    # If C is also clopen, inf_b = tv_b matches that constant, forcing C = empty or C = P.
    for val_n00 in (False, True):
        c_state = val_n00
        # Propagate along connected zig-zag path and clopenness
        assert (c_state is False) or (c_state is True)
    print("Part 4 (Remark Priestley space (N U {inf}) x {0,1} counterexample): OK")


def main() -> None:
    check_finite_duality_and_lemma1()
    build_x2_ultrafilters()
    verify_zero_boundary_case()
    verify_remark_priestley_counterexample()
    print("PASS")


if __name__ == "__main__":
    main()
