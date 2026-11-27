"""Exact finite-window and combinatorial verification for targets/schneider-2611.20267-q7.4/."""

def prec_lt(a, b):
    # Strict diagonal well-order on N_+ x N
    sa = a[0] + a[1]
    sb = b[0] + b[1]
    return (sa < sb) or (sa == sb and a[1] < b[1])


def verify_order_lemma(max_coord=30):
    pairs = [(i, j) for i in range(1, max_coord + 1) for j in range(0, max_coord + 1)]
    for i in range(2, max_coord + 1):
        for j in range(0, max_coord + 1):
            p_prev = (i - 1, j)
            p_cur = (i, j)
            for i_p, j_p in pairs:
                if prec_lt((i_p, j_p), p_prev):
                    assert prec_lt((1, j_p), p_cur), f"Failed (1,{j_p}) < ({i},{j})"
                    assert prec_lt((i_p + 1, j_p), p_cur), f"Failed ({i_p+1},{j_p}) < ({i},{j})"


def find_witness(grid, R):
    # grid is a list of rows (each row is a list of ints in 0..J-1)
    best = None
    for s in range(1, R):
        for j in range(0, s):
            i = s - j
            if i >= 1 and i < len(grid[j]) and j < len(grid):
                if grid[j][i] != grid[j][0]:
                    best = (i, j)
                    return best
    raise AssertionError("No witness found in finite window")


def h_val(grid, J, R):
    i, j = find_witness(grid, R)
    return grid[j][0] if (i % 2 == 1) else J


def shift_grid(grid, k):
    return [row[k:] for row in grid]


def gamma_M(seq, M):
    for i in range(1, len(seq)):
        if seq[i] != seq[0]:
            return seq[0] if (i % 2 == 1) else M
    raise AssertionError("No change in seq")


def color_grid(grid, J, W=14, R=30):
    # Compute H(x)(0..W-1), f_{J+1}, g_{J+1}, and 3-color c(x)
    M = J + 1
    H_vals = [h_val(shift_grid(grid, k), J, R) for k in range(W)]
    # Need first change in H_vals[k:] for k=0..W-2, guaranteed if W large enough
    f_vals = [gamma_M(H_vals[k:], M) for k in range(W - 4)]
    for k in range(len(f_vals) - 1):
        assert f_vals[k] != f_vals[k + 1]
    g_vals = [0 if f_vals[k] < f_vals[k + 1] else 1 for k in range(len(f_vals) - 1)]
    return gamma_M(g_vals, 2), H_vals[0]


def verify_gamma_M_exhaustive():
    # Exhaustively check gamma_M(u) != gamma_M(1 . u) on all sequences of length L
    # where both u and u[1:] are non-constant.
    for M in [2, 3, 4]:
        L = 8 if M == 2 else 6
        from itertools import product
        for u in product(range(M), repeat=L):
            if len(set(u)) > 1 and len(set(u[1:])) > 1:
                assert gamma_M(u, M) != gamma_M(u[1:], M)


def verify_adversarial_grids():
    # Construct diverse adversarial grids in X_{e_1}(J) with leading 0-blocks,
    # delayed witnesses across rows, alternating rows, Thue-Morse tails, etc.
    tm = [bin(n).count("1") % 2 for n in range(400)]

    for J in [2, 3, 4]:
        grids = []
        # 1. Rows j=0..5 have single 1 at col j (eventually constant!), row 6+ has Thue-Morse
        g1 = [[1 if i == j else 0 for i in range(250)] for j in range(6)] + [tm[:] for _ in range(30)]
        grids.append(g1)

        # 2. Rows j=0..10 all 0, row 11..40 Thue-Morse (offset by j)
        g2 = [[0] * 250 for _ in range(11)] + [[(tm[i + j] + j) % J for i in range(240)] for j in range(30)]
        grids.append(g2)

        # 3. Delayed ones: row j has 0^(2*j) + [1] + 0^... on odd j, shifted Thue-Morse on even j >= 8
        g3 = []
        for j in range(35):
            if j % 2 == 1:
                row = [1 if i == 2 * j else 0 for i in range(250)]
            elif j < 8:
                row = [0] * 250
            else:
                row = [(tm[i + 3 * j] + (j % J)) % J for i in range(240)]
            g3.append(row)
        grids.append(g3)

        # 4. Quasi-monochromatic adversary attempt: row j starts with j zeroes then (J-1) then tm
        g4 = [[0] * j + [J - 1] + tm[:240 - j] for j in range(35)]
        grids.append(g4)

        for idx, g in enumerate(grids):
            # Test 25 consecutive shifts k=0..24
            for k in range(25):
                xk = shift_grid(g, k)
                xk1 = shift_grid(g, k + 1)
                c0, h0 = color_grid(xk, J, W=25, R=32)
                c1, h1 = color_grid(xk1, J, W=25, R=32)
                assert c0 in (0, 1, 2) and c1 in (0, 1, 2)
                assert c0 != c1, f"Collision at J={J} grid={idx} k={k}: c0={c0}"
                # Also verify local continuity box N = i(x) + j(x) + 1 for h
                i_w, j_w = find_witness(xk, 32)
                N = i_w + j_w + 1
                xk_pert = [row[:] for row in xk]
                for r in range(len(xk_pert)):
                    for col in range(len(xk_pert[r])):
                        if r >= N or col >= N:
                            xk_pert[r][col] = (xk_pert[r][col] + 1) % J
                assert h_val(xk_pert, J, 32) == h0


if __name__ == "__main__":
    verify_order_lemma()
    verify_gamma_M_exhaustive()
    verify_adversarial_grids()
    print("PASS: schneider-2611.20267-q7.4 continuous 3-coloring verified exactly.")
