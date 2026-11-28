"""Exact integer verifier for the counterexample to Mora et al. (arXiv:2112.08768v1)."""


def l1_dist(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1]) + abs(u[2] - v[2])


def build_witness(n1, n2, n3):
    verts = [(x, y, z) for x in range(n1) for y in range(n2) for z in range(n3)]
    frame = {
        (x, y, z)
        for (x, y, z) in verts
        if (1 if x == 0 or x == n1 - 1 else 0)
        + (1 if y == 0 or y == n2 - 1 else 0)
        + (1 if z == 0 or z == n3 - 1 else 0)
        >= 2
    }
    extra = {
        (0, 1, 1),
        (n1 - 1, 1, 1),
        (1, 0, 1),
        (1, n2 - 1, 1),
        (1, 1, 0),
        (1, 1, n3 - 1),
    }
    return verts, frame | extra


def verify_case(n1, n2, n3, k, expected_size):
    am = 2 * (n1 + n2 + n3) - 8
    aM = min(n1 * (n2 + n3 - 2), n2 * (n1 + n3 - 2), n3 * (n1 + n2 - 2))
    assert am <= k < aM, f"k={k} not in [{am}, {aM})"

    conjectured = min(
        4 * k - 2 * am + 4,
        n1 * n2 * n3 - (n1 - 2) * (n2 - 2) * (n3 - 2),
    )
    verts, S = build_witness(n1, n2, n3)
    assert len(S) == expected_size, f"Expected size {expected_size}, got {len(S)}"
    assert len(S) < conjectured, f"|S|={len(S)} is not < conjectured {conjectured}"

    S_list = sorted(S)
    min_resolved = len(S_list)
    for i in range(len(verts)):
        u = verts[i]
        for j in range(i + 1, len(verts)):
            v = verts[j]
            resolved = 0
            for w in S_list:
                if l1_dist(w, u) != l1_dist(w, v):
                    resolved += 1
            if resolved < min_resolved:
                min_resolved = resolved
            assert resolved >= k + 1, (
                f"Grid ({n1},{n2},{n3}), pair {u} vs {v} only resolved by "
                f"{resolved} < {k + 1} vertices"
            )
    return len(S_list), conjectured, min_resolved


def main():
    cases = [
        (3, 3, 4, 13, 30),
        (3, 3, 5, 15, 34),
        (3, 4, 4, 15, 34),
        (4, 4, 4, 17, 38),
    ]
    for n1, n2, n3, k, exp_sz in cases:
        sz, conj, min_res = verify_case(n1, n2, n3, k, exp_sz)
        print(
            f"Verified counterexample P_{n1} x P_{n2} x P_{n3}, k={k}: "
            f"|S|={sz} < conjectured {conj}, min resolved={min_res} >= {k+1}"
        )
    print("PASS")


if __name__ == "__main__":
    main()
