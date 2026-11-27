"""Independent exact-arithmetic verifier for targets/oeis-A394511/."""

from collections import deque
import signal

signal.alarm(50)

Cell = tuple[str, int, int]


def neighbors(cell: Cell) -> list[Cell]:
    kind, x, y = cell
    if kind == "O":
        return [
            ("O", x + 1, y),
            ("O", x - 1, y),
            ("O", x, y + 1),
            ("O", x, y - 1),
            ("S", x, y),
            ("S", x - 1, y),
            ("S", x, y - 1),
            ("S", x - 1, y - 1),
        ]
    assert kind == "S"
    return [
        ("O", x, y),
        ("O", x + 1, y),
        ("O", x, y + 1),
        ("O", x + 1, y + 1),
    ]


def is_connected(cells: set[Cell]) -> bool:
    if not cells:
        return True
    start = next(iter(cells))
    seen = {start}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nb in neighbors(cur):
            if nb in cells and nb not in seen:
                seen.add(nb)
                q.append(nb)
    return len(seen) == len(cells)


def corona(H: set[Cell]) -> set[Cell]:
    C: set[Cell] = set()
    for cell in H:
        for nb in neighbors(cell):
            if nb not in H:
                C.add(nb)
    return C


def check_hole_and_shell(H: set[Cell], S: set[Cell], R_bound: int, C_bound: int) -> None:
    assert not (H & S), "H and S must be disjoint"
    assert is_connected(H), "H must be connected"
    assert corona(H) <= S, "S must contain corona C(H)"
    assert is_connected(S), "S must be connected"

    # Check exterior connectedness inside a generous bounding box covering H union S + 3-cell margin
    box: set[Cell] = set()
    for x in range(-4, R_bound + 4):
        for y in range(-4, C_bound + 4):
            box.add(("O", x, y))
            box.add(("S", x, y))
    ext = box - (H | S)
    assert ("O", -4, -4) in ext
    assert is_connected(ext), "Exterior inside bounding box must be connected"

    # Also verify every cell on the boundary layer outside H union S connects to the infinite exterior
    # (Wait: since H union S is contained in [-1, R_bound] x [-1, C_bound], every cell outside that rectangle
    # is connected in the full infinite graph to (-4, -4).)
    for c in H | S:
        _, cx, cy = c
        assert -2 <= cx <= R_bound + 1 and -2 <= cy <= C_bound + 1


def build_HRC(R: int, C: int) -> set[Cell]:
    H: set[Cell] = set()
    for x in range(R):
        for y in range(C):
            H.add(("O", x, y))
    for i in range(R - 1):
        for j in range(C - 1):
            H.add(("S", i, j))
    for i in range(R - 1):
        H.add(("S", i, -1))
        H.add(("S", i, C - 1))
    for j in range(C - 1):
        H.add(("S", -1, j))
        H.add(("S", R - 1, j))
    return H


def exley_formula(n: int) -> int:
    assert n >= 6
    return 2 * ((n + 17 + 4) // 5)


def main() -> None:
    # Sanity check edge-adjacency symmetry on a local patch
    for x in range(-2, 3):
        for y in range(-2, 3):
            for kind in ("O", "S"):
                c = (kind, x, y)
                for nb in neighbors(c):
                    assert c in neighbors(nb)

    # Check all H(R, C) for 2 <= R, C <= 10
    for R in range(2, 11):
        for C in range(2, 11):
            H = build_HRC(R, C)
            n = 2 * R * C + R + C - 3
            assert len(H) == n
            S = corona(H)
            assert len(S) == 2 * R + 2 * C + 4
            check_hole_and_shell(H, S, R, C)
    print("Grid Family PASS: H(R,C) and corona S=C(H(R,C)) verified for all 2 <= R, C <= 10.")

    # Explicit counterexamples cited in COUNTEREXAMPLE.md
    H35 = build_HRC(3, 5)
    S35 = corona(H35)
    assert len(H35) == 35 and len(S35) == 20 < exley_formula(35) == 22
    check_hole_and_shell(H35, S35, 3, 5)

    # Removing corner octagon O(0,0) from H(3,5) -> n=34, |S|=20 < 22
    H34 = H35 - {("O", 0, 0)}
    S34 = corona(H34)
    assert len(H34) == 34 and len(S34) == 20 < exley_formula(34) == 22
    check_hole_and_shell(H34, S34, 3, 5)

    # R=C=4 -> n=37, |S|=20 < 22
    H44 = build_HRC(4, 4)
    S44 = corona(H44)
    assert len(H44) == 37 and len(S44) == 20 < exley_formula(37) == 22
    check_hole_and_shell(H44, S44, 4, 4)

    # Infinite family R=C=k >= 4 inequality check (for k=4..1000)
    for k in range(4, 1001):
        nk = 2 * k * k + 2 * k - 3
        sk = 4 * k + 4
        assert sk < exley_formula(nk)

    # Recurrence check: a(20) = 16 from OEIS Data, so recurrence would force a(35) = 22 > 20
    oeis_data = [4, 8, 8, 8, 8, 10, 10, 10, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16]
    assert oeis_data[19] == 16  # a(20) in 1-indexed data
    assert oeis_data[19] + 3 * 2 == 22 > len(S35)

    print("Counterexamples PASS: (3,5) [n=35, |S|=20<22], n=34 [|S|=20<22], (4,4) [n=37, |S|=20<22], k=4..1000.")
    print("PASS")


if __name__ == "__main__":
    main()
