"""Exact zero-float verification for targets/caro-2312.08777-prob7 (b(t) = 3)."""

def verify_lower_bound() -> None:
    """Verify b + 1 <= r <= binom(b + 1, 2) - 1 has no solution for b in {1, 2}."""
    for b in (1, 2):
        upper = ((b + 1) * b) // 2 - 1
        assert upper < b + 1, f"Unexpected solution for b={b}: upper={upper}"
    assert ((3 + 1) * 3) // 2 - 1 >= 4


def verify_recurrence(max_t: int = 50) -> None:
    """Verify the exact integer recurrence and inductive bounds up to s = max_t."""
    A = {1: 4}
    B = {1: 3}
    e1 = {1: 6}
    e2 = {1: 4}
    assert e1[1] > e2[1]
    for s in range(1, max_t):
        e1[s + 1] = e1[s] + 6 * A[s]
        e2[s + 1] = e2[s] + 3 * A[s] + 4 * B[s]
        A[s + 1] = 3 * A[s] + 4 * B[s]
        B[s + 1] = 3 * A[s]
        assert e1[s + 1] > e2[s + 1], f"Flip condition failed at s={s+1}"
        if s >= 2:
            assert 5 * A[s - 1] <= A[s] <= 6 * A[s - 1]
            assert (e1[s + 1] - e1[s]) - (e2[s + 1] - e2[s]) >= 3 * A[s - 1] > 0


def mul_gf16(a: int, b: int) -> int:
    """Multiply in GF(16) = F_2[x] / (x^4 + x + 1) with integer bitmasks."""
    res = 0
    for i in range(4):
        if (b >> i) & 1:
            t = a
            for _ in range(i):
                t <<= 1
                if t & 16:
                    t ^= 0b10011
            res ^= t
    return res


def verify_explicit_t2_graph() -> None:
    """Construct an explicit 2048-vertex ([2], (3, 4))-flip graph via AG(2, 16) and verify all vertices."""
    pts = [(x, y) for x in range(16) for y in range(16)]
    lines = [(m, c) for m in range(16) for c in range(16)]
    adj_h = [[] for _ in range(512)]
    for xi, (x, y) in enumerate(pts):
        for mi, (m, c) in enumerate(lines):
            if (mul_gf16(m, x) ^ c) == y:
                adj_h[xi].append(256 + mi)
                adj_h[256 + mi].append(xi)

    # Verify H is simple, 16-regular, and girth >= 6 (no 4-cycles since bipartite => no odd cycles).
    for u in range(512):
        assert len(adj_h[u]) == 16
        assert len(set(adj_h[u])) == 16
        assert u not in adj_h[u]
    # Check no C_4 in H: any two points share <= 1 common line.
    for u in range(256):
        s_u = set(adj_h[u])
        for v in range(u + 1, 256):
            assert len(s_u.intersection(adj_h[v])) <= 1

    adj_blue = [[] for _ in range(2048)]
    adj_red = [[] for _ in range(2048)]
    for u in range(512):
        base = 4 * u
        for i in range(4):
            for j in range(4):
                if i != j:
                    adj_blue[base + i].append(base + j)

    port_cnt = [0] * 512
    for u in range(512):
        for v in adj_h[u]:
            if u < v:
                pu = port_cnt[u] // 4
                port_cnt[u] += 1
                pv = port_cnt[v] // 4
                port_cnt[v] += 1
                gu = 4 * u + pu
                gv = 4 * v + pv
                adj_red[gu].append(gv)
                adj_red[gv].append(gu)

    for v in range(2048):
        assert len(adj_blue[v]) == 3
        assert len(adj_red[v]) == 4
        assert not set(adj_blue[v]).intersection(adj_red[v])

    for v in range(2048):
        dist = {v: 0}
        queue = [v]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            if dist[u] == 2:
                continue
            for w in adj_blue[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    queue.append(w)
            for w in adj_red[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        n1 = {u for u, d in dist.items() if d <= 1}
        n2 = set(dist.keys())
        e1_1 = sum(1 for u in n1 for w in adj_blue[u] if w in n1) // 2
        e2_1 = sum(1 for u in n1 for w in adj_red[u] if w in n1) // 2
        e1_2 = sum(1 for u in n2 for w in adj_blue[u] if w in n2) // 2
        e2_2 = sum(1 for u in n2 for w in adj_red[u] if w in n2) // 2
        assert (e1_1, e2_1) == (6, 4)
        assert (e1_2, e2_2) == (30, 28)


if __name__ == "__main__":
    verify_lower_bound()
    verify_recurrence()
    verify_explicit_t2_graph()
    print("PASS")
