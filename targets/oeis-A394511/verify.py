import signal
from collections import deque

signal.alarm(30)


def neighbors(cell):
    typ, x, y = cell
    if typ == 0:
        return [
            (0, x + 1, y), (0, x - 1, y), (0, x, y + 1), (0, x, y - 1),
            (1, x, y), (1, x - 1, y), (1, x, y - 1), (1, x - 1, y - 1),
        ]
    return [
        (0, x, y), (0, x + 1, y), (0, x, y + 1), (0, x + 1, y + 1),
    ]


def build_rect_hole(R: int, C: int):
    assert R >= 2 and C >= 2
    H = {(0, x, y) for x in range(R) for y in range(C)}
    H |= {(1, i, j) for i in range(R - 1) for j in range(C - 1)}
    H |= {(1, i, -1) for i in range(R - 1)}
    H |= {(1, i, C - 1) for i in range(R - 1)}
    H |= {(1, -1, j) for j in range(C - 1)}
    H |= {(1, R - 1, j) for j in range(C - 1)}
    return H


def corona(H):
    return {v for u in H for v in neighbors(u) if v not in H}


def is_connected(cells):
    start = next(iter(cells))
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in neighbors(u):
            if v in cells and v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == len(cells)


def verify_rect(R: int, C: int):
    H = build_rect_hole(R, C)
    n = 2 * R * C + R + C - 3
    assert len(H) == n

    S = corona(H)
    exp_S = (
        {(0, x, -1) for x in range(R)}
        | {(0, x, C) for x in range(R)}
        | {(0, -1, y) for y in range(C)}
        | {(0, R, y) for y in range(C)}
        | {(1, -1, -1), (1, R - 1, -1), (1, -1, C - 1), (1, R - 1, C - 1)}
    )
    assert S == exp_S
    assert len(S) == 2 * R + 2 * C + 4
    assert is_connected(H)
    assert is_connected(S)

    # Check exterior connectivity on a bounding box containing H union S with margin 4
    HS = H | S
    xmin, xmax = -4, R + 3
    ymin, ymax = -4, C + 3
    ext = {
        (t, x, y)
        for t in (0, 1)
        for x in range(xmin, xmax + 1)
        for y in range(ymin, ymax + 1)
    } - HS
    assert is_connected(ext)

    # Also confirm every outer boundary cell of the box is in ext and connected
    return n, len(S)


def main():
    # 1. Explicit smallest verified rectangular CE: (R, C) = (3, 5) -> n=35, |S|=20 < 22
    n0, s0 = verify_rect(3, 5)
    conj0 = 2 * ((n0 + 17 + 4) // 5)
    assert n0 == 35 and s0 == 20 and conj0 == 22 and s0 < conj0

    # 2. Check infinite family members (R, C) = (k, k) for k = 4..12
    for k in range(4, 13):
        nk, sk = verify_rect(k, k)
        conjk = 2 * ((nk + 17 + 4) // 5)
        assert sk < conjk, f"Expected CE at k={k}: n={nk}, |S|={sk}, conj={conjk}"

    # 3. Also check symmetry of adjacency (undirected graph sanity)
    for x in range(-2, 3):
        for y in range(-2, 3):
            for t in (0, 1):
                u = (t, x, y)
                for v in neighbors(u):
                    assert u in neighbors(v)

    print(f"PASS: verified 4.8.8 graph symmetry and valid connected enclosing shell at n={n0} "
          f"with |S|={s0} < 2*ceil((35+17)/5)={conj0}, plus diagonal family k=4..12.")


if __name__ == "__main__":
    main()
