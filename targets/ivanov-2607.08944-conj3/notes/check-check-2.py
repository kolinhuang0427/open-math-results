"""Independent exact-rational verifier for targets/ivanov-2607.08944-conj3.

Tests the 24-facet 13-dimensional polytope P directly against the primary-source
definition of a primitive polytope (arXiv:2607.08944v1, Section 1.3-1.4, Theorem 2 /
positive basis / unbounded spills) and enumerates all vertices via exact Fraction
linear algebra (zero floating point).
"""

from fractions import Fraction
from itertools import combinations


def rref_rank(rows: list[list[Fraction]]) -> int:
    """Exact rank over Q via Fraction Gaussian elimination."""
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    mat = [list(r) for r in rows]
    rank = 0
    for col in range(n):
        piv = None
        for r in range(rank, m):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        inv = Fraction(1, 1) / mat[rank][col]
        for c in range(col, n):
            mat[rank][c] *= inv
        for r in range(m):
            if r != rank and mat[r][col] != 0:
                factor = mat[r][col]
                for c in range(col, n):
                    mat[r][c] -= factor * mat[rank][c]
        rank += 1
    return rank


def solve_3x3(rows: list[list[Fraction]], rhs: list[Fraction]) -> tuple[Fraction, Fraction, Fraction] | None:
    """Solve 3x3 exact rational system; return None if singular."""
    mat = [list(rows[i]) + [rhs[i]] for i in range(3)]
    for col in range(3):
        piv = None
        for r in range(col, 3):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            return None
        mat[col], mat[piv] = mat[piv], mat[col]
        inv = Fraction(1, 1) / mat[col][col]
        for c in range(col, 4):
            mat[col][c] *= inv
        for r in range(3):
            if r != col and mat[r][col] != 0:
                factor = mat[r][col]
                for c in range(col, 4):
                    mat[r][c] -= factor * mat[col][c]
    return (mat[0][3], mat[1][3], mat[2][3])


def dot(u: list[Fraction], v: list[Fraction]) -> Fraction:
    return sum(a * b for a, b in zip(u, v))


def build_P() -> tuple[list[list[Fraction]], list[Fraction]]:
    """Build exact 24 halfspaces A x <= b in Q^13 from COUNTEREXAMPLE.md."""
    A: list[list[Fraction]] = []
    b: list[Fraction] = []

    def add_row(entries: dict[int, int], rhs_val: int) -> None:
        row = [Fraction(0)] * 13
        for idx, val in entries.items():
            row[idx] = Fraction(val)
        A.append(row)
        b.append(Fraction(rhs_val))

    # 4 simplex inequalities on (x1, x2, x3) = indices 0, 1, 2
    add_row({0: 1}, 100)
    add_row({1: 1}, 100)
    add_row({2: 1}, 100)
    add_row({0: -1, 1: -1, 2: -1}, 100)

    # 10 lifted pairs for y_j = index 3 + j, j = 0..9
    for j in range(10):
        add_row({3 + j: 1}, 1)
        add_row({0: 1, 1: 1, 2: -j, 3 + j: -1}, 119 + j * j)

    assert len(A) == 24
    return A, b


def main() -> None:
    A, b = build_P()

    # 1. Origin is strictly in interior of P.
    for i in range(24):
        assert b[i] > 0, f"Origin not strictly feasible on inequality {i}"

    # 2. Positive dependence among all 24 outer normals (=> 0 in int conv{a_i}, P bounded).
    # Verify outer normals span R^13 (rank 13) and sum(mu_i * a_i) == 0 with all mu_i > 0.
    assert rref_rank(A) == 13, "Outer normals do not span R^13"
    mu = [Fraction(1), Fraction(1), Fraction(56), Fraction(11)] + [Fraction(1)] * 20
    assert all(m > 0 for m in mu)
    for col in range(13):
        assert sum(mu[i] * A[i][col] for i in range(24)) == 0, f"Positive dependence fails at coord {col}"

    # 3. Primitivity: every single-facet spill is unbounded (positive basis check).
    # We compute ray directions directly: for each i, find r_i with a_i . r_i > 0 and a_m . r_i <= 0 (m != i).
    # Note: the 20 y_j-rays are +/- e_{3+j}, and for the 4 base inequalities we construct/check integer rays.
    rays: list[list[Fraction]] = [
        [Fraction(v) for v in [1, -1, 0] + [0] * 10],
        [Fraction(v) for v in [-1, 1, 0] + [0] * 10],
        [Fraction(v) for v in [-1, -1, 2] + [0] * 10],
        [Fraction(v) for v in [-10, 0, -1] + [0] * 10],
    ]
    for j in range(10):
        r_plus = [Fraction(0)] * 13
        r_plus[3 + j] = Fraction(1)
        rays.append(r_plus)
        r_minus = [Fraction(0)] * 13
        r_minus[3 + j] = Fraction(-1)
        rays.append(r_minus)

    assert len(rays) == 24
    for i in range(24):
        assert dot(A[i], rays[i]) > 0, f"Ray {i} fails strict positivity on omitted halfspace"
        for m in range(24):
            if m != i:
                assert dot(A[m], rays[i]) <= 0, f"Ray {i} violates non-positivity on halfspace {m}"

    # 4. Exact complete enumeration of vertices of projected 3-polytope P_x.
    Px_rows: list[list[Fraction]] = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(-1), Fraction(-1), Fraction(-1)],
    ]
    Px_rhs: list[Fraction] = [Fraction(100), Fraction(100), Fraction(100), Fraction(100)]
    for j in range(10):
        Px_rows.append([Fraction(1), Fraction(1), Fraction(-j)])
        Px_rhs.append(Fraction(120 + j * j))

    Px_verts: set[tuple[Fraction, Fraction, Fraction]] = set()
    for i1, i2, i3 in combinations(range(len(Px_rows)), 3):
        pt = solve_3x3([Px_rows[i1], Px_rows[i2], Px_rows[i3]], [Px_rhs[i1], Px_rhs[i2], Px_rhs[i3]])
        if pt is None:
            continue
        pt_list = list(pt)
        if all(dot(Px_rows[k], pt_list) <= Px_rhs[k] for k in range(len(Px_rows))):
            Px_verts.add(pt)

    assert len(Px_verts) == 24, f"Expected 24 vertices in P_x, got {len(Px_verts)}"

    # 5. Lift every vertex of P_x to all exact vertices of P and verify Ax <= b and rank(A_active) == 13.
    P_verts: set[tuple[Fraction, ...]] = set()
    for x1, x2, x3 in Px_verts:
        choices_per_j: list[list[Fraction]] = []
        for j in range(10):
            lo = x1 + x2 - Fraction(j) * x3 - Fraction(119 + j * j)
            hi = Fraction(1)
            assert lo <= hi
            if lo == hi:
                choices_per_j.append([hi])
            else:
                choices_per_j.append([lo, hi])

        # Cartesian product over j=0..9
        partials: list[tuple[Fraction, ...]] = [(x1, x2, x3)]
        for j in range(10):
            partials = [p + (yj,) for p in partials for yj in choices_per_j[j]]

        for v in partials:
            v_list = list(v)
            active_rows = []
            for idx in range(24):
                val = dot(A[idx], v_list)
                assert val <= b[idx], f"Feasibility violated at {v} row {idx}"
                if val == b[idx]:
                    active_rows.append(A[idx])
            assert rref_rank(active_rows) == 13, f"Active rank < 13 at {v}"
            P_verts.add(v)

    assert len(P_verts) == 8704, f"Expected 8704 vertices, got {len(P_verts)}"
    assert len(P_verts) > 2**13, "Vertex count does not exceed 2^13"

    # 6. Verify COUNTEREXAMPLE.md L63 formula (20 - m^2 - m, 100, -2*m - 1) for m = 8..0 matches P_x vertices.
    explicit_r2 = [(-52, 100, -17), (-36, 100, -15), (-22, 100, -13), (-10, 100, -11), (0, 100, -9), (8, 100, -7), (14, 100, -5), (18, 100, -3), (20, 100, -1)]
    for m_idx, pt in enumerate(reversed(explicit_r2)):
        assert pt == (20 - m_idx**2 - m_idx, 100, -2 * m_idx - 1)
        assert (Fraction(pt[0]), Fraction(pt[1]), Fraction(pt[2])) in Px_verts

    print("PASS")
    print(f"Verified 24-facet primitive 13-polytope P: 24 P_x vertices, {len(P_verts)} distinct full-rank vertices (> 2^13 = {2**13}).")


if __name__ == "__main__":
    main()
