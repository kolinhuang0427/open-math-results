# Adversarial Audit Report: `targets/oeis-A386251/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T23:00Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (specifically, an explicit infinite family of 4-segment counterexamples for $n = m^2 - 30$, $m \ge 92$ verified by exact integer computation, paired with an internally audited elementary proof that every 3-segment closed walk has length $\ge 4m + 2$). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/oeis-A386251/notes/check-check-3.py` (authored by `check-3` strictly from live OEIS `A386251` and `COUNTEREXAMPLE.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly): `A386251` (revision 22, `2025-08-06T00:07:55-04:00`) and sibling `A385525` (revision 32, `2025-08-06T00:08:46-04:00`).
- `targets/oeis-A386251/TARGET.md`
- `targets/oeis-A386251/COUNTEREXAMPLE.md`
- `targets/oeis-A386251/notes/check-check-3.md` and `notes/check-check-3.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,3,5,6}.md`), plus direct live checks of `the-omega-institute/trureturing#27151`, `aliromman/math`, Zenodo API, GitHub search, and `tools/novelty_grep.py`.

Author scratch notes (`notes/explore*.py`, `notes/find_4seg_counterexample.py`, `notes/check_small_n_and_verify.py`) and the finder's `verify.py` were **not** read.

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against live OEIS `A386251` (rev 22, Charles L. Hohn, `2025-08-06T00:07:55-04:00`) and cross-referenced `A385525` (rev 32):
- **Name:** *"Consider the graph whose vertices are the points of the n-dimensional cubic lattice with points connected by all integer-length diagonals that traverse all n dimensions and do not intersect intermediate points. a(n) is the total length of the shortest possible closed walk in this graph via noncongruent diagonals."*
- **Comment (conjecture):** *"It is provable that all such walks must be even in total length. It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks."*
- **Definition checks against `A386251` examples and `A385525`:**
  1. **"traverse all $n$ dimensions"** $\iff v_i \neq 0$ for every coordinate $1 \le i \le n$ (confirmed by all examples for $n = 2, 3, 4$).
  2. **"do not intersect intermediate points"** $\iff$ primitive lattice vector $\gcd(|v_1|, \dots, |v_n|) = 1$ (confirmed by Comment 2 *"primitive Pythagorean triangles"* and all examples).
  3. **"noncongruent diagonals"** $\iff$ pairwise distinct multisets of coordinate magnitudes $\{|v_1|, \dots, |v_n|\}$ (i.e., distinct orbits under the cubic lattice symmetry group $B_n$), **not** pairwise distinct lengths: explicitly confirmed by `A386251` Example `a(3) = 28` using two diagonals of equal length `9` (`[-7, 4, 4]` and `[8, -4, 1]`), and by Comment 4 (*"Adding a constraint that the diagonal segments must all have the same length gives A385525"*).
- Zero quantifier, hypothesis, edge-case, or definition drift between `A386251`, `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-3.py`.

---

## 3. Adversarial Audit of `COUNTEREXAMPLE.md`

### 3.1 Section 1 (Explicit 4-Segment Witness for $n = m^2 - 30$, $m \ge 92$)
Checked every coordinate, column sum, squared norm, primitivity, and distinctness condition by hand and via exact computation:
- For $m \ge 92$, $n = m^2 - 30 \ge 8434$, so the tail has $n - 10 \ge 8424 \ge 1$ coordinates $(1, 1, -1, -1)^T$.
- All 6 distinct column types sum to $0$: $(-2-4+1+5)=0$, $(-2-2+3+1)=0$, $(2-2-1+1)=0$, $(2-1-2+1)=0$, $(2-1+1-2)=0$, $(1+1-1-1)=0$, giving $v^{(1)} + v^{(2)} + v^{(3)} + v^{(4)} = 0$.
- Every coordinate belongs to $\{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5\}$, so every $v^{(j)}_i \neq 0$.
- Coordinate $i = 11$ of each $v^{(j)}$ is $\pm 1$, so $\gcd(v^{(j)}_1, \dots, v^{(j)}_n) = 1$ for every $j \in \{1,2,3,4\}$.
- Squared Euclidean norms: each vector has excess $\sum_{i=1}^{10} ((v^{(j)}_i)^2 - 1)$ equal to:
  - $v^{(1)}$: $10(4 - 1) = 30$;
  - $v^{(2)}$: $(16 - 1) + 5(4 - 1) = 30$;
  - $v^{(3)}$: $3(9 - 1) + 2(4 - 1) = 30$;
  - $v^{(4)}$: $(25 - 1) + 2(4 - 1) = 30$.
  Hence $\|v^{(j)}\|_2^2 = n + 30 = m^2$ and $\|v^{(j)}\|_2 = m$ for all $j = 1, 2, 3, 4$, total length $4m$ ($368$ at $m = 92, n = 8434$).
- Multisets of coordinate magnitudes $> 1$ are $\{2^{10}\}, \{2^5, 4\}, \{2^2, 3^3\}, \{2^2, 5\}$, pairwise distinct, hence pairwise noncongruent under $B_n$.
- **Geometric non-degeneracy check (auditor addition):** On coordinates $(1, 2, 5)$, the $3 \times 3$ matrix of $(v^{(1)}, v^{(2)}, v^{(3)})$ is $\begin{pmatrix}-2 & -2 & 2 \\ -4 & -2 & -2 \\ 1 & 3 & -1\end{pmatrix}$ with determinant $-24 \neq 0$, so the four vertices $0, v^{(1)}, v^{(1)}+v^{(2)}, v^{(1)}+v^{(2)}+v^{(3)}$ are affinely independent (span a non-degenerate 3-simplex in $\mathbb{R}^n$). Thus the walk is not merely a closed walk, but a simple, non-self-intersecting 4-cycle in $\mathbb{R}^n$.

### 3.2 Section 2 (Proof That Every 3-Segment Closed Walk Has Length $\ge 4m + 2$ for $m \ge 92$)
Audited all five steps adversarially, checking all boundary and equality cases:
1. **$L_j \ge m$:** Every valid diagonal has $\|v\|_2^2 \ge n = m^2 - 30$. For $m \ge 92$ (indeed $m \ge 16$), $(m-1)^2 = m^2 - 2m + 1 \le m^2 - 183 < m^2 - 30 = n \le L_j^2$, so integer $L_j \ge m$.
2. **Parity ($L_1 + L_2 + L_3$ even):** $u_i + v_i + w_i = 0 \implies u_i^2 + v_i^2 + w_i^2 = 2(u_i^2 + u_i v_i + v_i^2) \equiv 0 \pmod 2$; summing over $i$ gives $L_1^2 + L_2^2 + L_3^2 \equiv L_1 + L_2 + L_3 \equiv 0 \pmod 2$.
3. **$L_1^2 + L_2^2 + L_3^2 \ge 6n = 6m^2 - 180$:** For each $i$, $u_i, v_i, w_i \in \mathbb{Z} \setminus \{0\}$ with $u_i + v_i + w_i = 0$ cannot all be odd (sum of three odd integers is odd), hence cannot all lie in $\{\pm 1\}$; thus at least one has $|x| \ge 2$ and the other two have $|x| \ge 1$, giving $u_i^2 + v_i^2 + w_i^2 \ge 4 + 1 + 1 = 6$.
4. **Strict triangle inequality $L_3 < L_1 + L_2$:** By Cauchy–Schwarz, $\|u + v\|_2 = \|u\|_2 + \|v\|_2$ with $u, v \neq 0$ holds iff $v = \lambda u$ for some $\lambda \in \mathbb{R}_{>0}$. Since $u, v \in \mathbb{Z}^n$ are primitive ($\gcd = 1$), writing $\lambda = p/q$ in lowest terms forces $q \mid \gcd(u) = 1$ and $p \mid \gcd(v) = 1$, hence $\lambda = 1$ and $u = v$ — contradicting both noncongruence of $u, v$ and primitivity of $w = -2u$.
5. **Contradiction for $L_1 + L_2 + L_3 \le 4m$:** Ordering $m \le L_1 \le L_2 \le L_3$ and setting $L_1 = m+a$, $L_2 = m+b$, $L_3 = 2m-d$ with $0 \le a \le b$:
   - $L_1 + L_2 + L_3 \le 4m \iff d \ge a + b \ge 0$;
   - $L_3 < L_1 + L_2 \iff d + a + b > 0$, ruling out $d = 0$ (since $d = 0 \implies a = b = 0$), so $d \ge 1$;
   - $L_3 \ge L_2 \iff d \le m - b \le m$.
   - If $d = m$: $b = 0 \implies a = 0$, giving $(m, m, m)$ and $3m^2 < 6m^2 - 180$ (for $m \ge 8$).
   - If $1 \le d \le m - 1$: $m^2 + (m+d)^2 - (m+a)^2 - (m+b)^2 = 2m(d-a-b) + (d^2 - a^2 - b^2) \ge 2ab \ge 0$, so
     $$L_1^2 + L_2^2 + L_3^2 \le m^2 + (m+d)^2 + (2m-d)^2 = 6m^2 - 2d(m-d) \le 6m^2 - 2(m-1) \le 6m^2 - 182 < 6m^2 - 180 = 6n$$
     for all $m \ge 92$ (since $d(m-d) - (m-1) = (d-1)(m-1-d) \ge 0$).
   - Equality cases $L_1 = L_2$ ($a = b$) and $L_2 = L_3$ ($d = m - b$) and strict inequality $L_1+L_2+L_3 < 4m$ are all validly covered without gap.
- **Exactness of $a(m^2 - 30) = 4m$:** 1-segment walks are impossible ($v \neq 0$); 2-segment walks force $v^{(2)} = -v^{(1)}$ (congruent); every 3-segment walk has length $\ge 4m + 2$; every $k$-segment walk with $k \ge 4$ has length $\ge k m \ge 4m$. Hence $a(m^2 - 30) = 4m$ and is never achieved by a 3-segment walk for any $m \ge 92$.

### 3.3 Independent Verifier Re-run
Re-executed `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A386251/notes/check-check-3.py` (exit code `0`):
```text
4-cycle witnesses PASS: verified full n-dim vectors for m=92..110 (n=8434..12070).
3-segment lower bound (>= 4m+2) PASS: exact triple exhaustion for m=92..120 (sharp at m=91).
PASS
```

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A386251` (rev 22, `2025-08-06T00:07:55-04:00`) still explicitly states the 3-segment conjecture as open.
- Gate 2 receipts (`notes/novelty-gate2-watch-{1,3,5,6}.md`) all passed with no `CONTESTED.md`.
- Direct auditor verification confirmed:
  - `the-omega-institute/trureturing#27151` targets Charles L. Hohn's unrelated 2D bilateral-symmetry conjecture on `A386671` (and is only an open preregistration).
  - `aliromman/math` (all PRs/issues), `KnowledgeSense/math`, Zenodo (`total: 0`), `tools/novelty_grep.py` (333 files), GitHub issues/code, and web search contain no prior refutation of `A386251`.
- **Gate 3 live pre-report re-check (all PASS within 1 hour of report, no `CONTESTED.md`; `watch-3` relieved `watch-1` per board #397):**
  - `targets/oeis-A386251/notes/novelty-gate3-watch-3.md` (`2026-11-26T23:16:07Z`, PASS)
  - `targets/oeis-A386251/notes/novelty-gate3-watch-5.md` (`2026-11-26T23:13:09Z`, PASS)
  - `targets/oeis-A386251/notes/novelty-gate3-watch-6.md` (`2026-11-26T23:07:13Z`, PASS)
