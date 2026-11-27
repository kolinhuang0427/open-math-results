# Adversarial Audit Report: `targets/oeis-A061313/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T23:59Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (with exact-arithmetic verification of all $\mathrm{SL}_2(\mathbb{Z})$ matrix identities, BFS minimal steps for $n = 1..100$, Stern–Brocot enumeration and canonical Hirzebruch continued fractions for $n = 1..4096$). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/oeis-A061313/notes/check-check-1.py` (authored by `check-1` strictly from live OEIS `A061313`, `A007305`, `A007306` and `PROOF.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly): `A061313` (revision 58, `2026-11-01T16:49:49-05:00`), `A007305` (revision 117), `A007306` (revision 342), and companion `A008687` (revision 66).
- `targets/oeis-A061313/TARGET.md`
- `targets/oeis-A061313/PROOF.md`
- `targets/oeis-A061313/notes/check-check-1.md` and `notes/check-check-1.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`), plus direct arXiv queries (`1812.00170`, `2312.12953`, negative continued fraction + Farey/Stern–Brocot queries) and web searches.

The author's `verify.py` and `notes/explore.py` were **not** read.

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against live OEIS `A061313` (rev 58, `2026-11-01`), `A007305` (rev 117), `A007306` (rev 342), and `A008687` (rev 66):
- **Name (`A061313`, offset `1,3`):** *"Minimal number of steps to get from 1 to n by (a) subtracting 1 or (b) multiplying by 2."*
- **Formula (`A061313`):** `a(2n) = a(n)+1; a(2n+1) = a(n+1)+2; a(1) = 0.`
  - *(Auditor completeness check: reversing operations to reach $1$ from $n$ via $+1$ or $/2$ when even, any path from even $2n$ that starts with $2r \ge 2$ additions before its first $/2$ reaches $n + r$ in $2r + 1$ steps, whereas $/2$ followed by $r$ additions reaches $n + r$ in $r + 1 < 2r + 1$ steps; hence $/2$ is strictly optimal at every even $2n$, giving $a(2n) = a(n) + 1$ and $a(2n+1) = 1 + a(2n+2) = a(n+1) + 2$ for all $n \ge 1$.)*
- **Comment (`A061313`):** *"Conjecture: a(n)+2 is the sum of the terms of the Hirzebruch (negative) continued fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n). - _Andrei Zabolotskii_, Apr 17 2020"*
- **`A007305`/`A007306`:** Numerators and denominators of the Farey / Stern–Brocot subtree on $[0, 1]$, starting $r(0) = 0/1$, $r(1) = 1/1$, and level $L \ge 1$ mediants at indices $n \in \{2^{L-1}+1, \dots, 2^L\}$. Exact match with `PROOF.md`.
- **Boundary at $n = 1$:** Because `A061313` has offset `1`, the literal conjecture includes $n = 1$, where $r(1) = 1/1$ has unique canonical Hirzebruch continued fraction $[[1]]$ (sum $1 \neq 2 = a(1) + 2$; moreover, no 2-term integer negative continued fraction $c_0 - 1/c_1 = 1$ has $c_0 + c_1 = 2$). `PROOF.md` transparently establishes both the universal theorem for all $n \ge 2$ and the sole boundary exception at $n = 1$.

---

## 3. Adversarial Audit of `PROOF.md`

### 3.1 Step 1 (Stern–Brocot Tree Index Recursion for $m \ge 2$)
- Encoding each Farey ancestor interval $[a_m/b_m, c_m/d_m] \subseteq [0, 1]$ ($b_m c_m - a_m d_m = 1$) by $M(m) = \begin{pmatrix} c_m & a_m \\ d_m & b_m \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z})$ gives $M(2) = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ and $r(2) = 1/2$.
- At level $L - 1 \ge 1$, the $j$-th index is $m = 2^{L-2} + j$ ($1 \le j \le 2^{L-2}$); splitting its interval by $r(m)$ produces the $(2j-1)$-th and $(2j)$-th intervals at level $L$, with indices $2^{L-1} + (2j - 1) = 2m - 1$ and $2^{L-1} + 2j = 2m$, and matrices $M(2m-1) = M(m) L$ and $M(2m) = M(m) R$.
- Since $\det M(2) = \det L = \det R = 1$, $\det M(m) = 1$ for all $m \ge 2$, guaranteeing $\gcd(a_m + c_m, b_m + d_m) = 1$ and positivity of both numerator and denominator.

### 3.2 Step 2 (Conjugation to Hirzebruch Matrices)
- Checked $H(c) = \begin{pmatrix} c & -1 \\ 1 & 0 \end{pmatrix}$: by induction on $k \ge 0$, for $c_0 \ge 1$ and $c_1, \dots, c_k \ge 2$, the first column $(p, q)^T$ of $H(c_0) H(c_1) \cdots H(c_k)$ satisfies $p > 0, q > 0$, $\gcd(p, q) = 1$, and $p/q = [[c_0; c_1, \dots, c_k]]$ (with $p > q > 0$ preserved whenever $c_0 \ge 2$).
- Checked uniqueness of the canonical expansion: since $c_1, \dots, c_k \ge 2$, backward induction gives $x_k = c_k \ge 2 > 1$ and $x_i = c_i - 1/x_{i+1} \in (c_i - 1, c_i)$ for all $0 \le i < k$, forcing $c_i = \lceil x_i \rceil$ uniquely at every step.
- Checked all three $2 \times 2$ matrix identities by hand (and exact script):
  1. $P(2) = M(2) J = \begin{pmatrix} 1 & -1 \\ 2 & -1 \end{pmatrix} = H(1) H(2)$;
  2. $J^{-1} L J = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} = H(2)$;
  3. $J^{-1} R J = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$ and $H(c)(J^{-1} R J) = H(c + 1)$ for all $c \in \mathbb{Z}$.
- First column of $P(m) = M(m) J$ is $M(m)\binom{1}{1} = \binom{a_m + c_m}{b_m + d_m}$, representing $r(m)$ in lowest terms.

### 3.3 Step 3 (Structural Induction on $n \ge 2$ and Recurrence Match)
- Every $n \ge 3$ is either $2m - 1$ ($m = (n+1)/2 \in [2, n-1]$) or $2m$ ($m = n/2 \in [2, n-1]$), so strong induction from $n = 2$ covers all $n \ge 2$.
- Since $k \ge 1$ in $P(m) = H(1) H(c_1) \cdots H(c_k)$ ($c_i \ge 2$), $P(2m-1) = P(m) H(2)$ appends $c_{k+1} = 2 \ge 2$, and $P(2m) = P(m)(J^{-1} R J) = H(1) \cdots H(c_{k-1}) H(c_k + 1)$ increments the final entry $c_k \mapsto c_k + 1 \ge 3$ without touching $H(1)$.
- Thus $S(n) = 1 + \sum_{i=1}^k c_i$ satisfies $S(2) = 3$, $S(2m-1) = S(m) + 2$, $S(2m) = S(m) + 1$ ($m \ge 2$), matching $T(n) := a(n) + 2$ ($T(2) = a(1) + 1 + 2 = 3$, $T(2m) = T(m) + 1$, $T(2m-1) = a(2(m-1)+1) + 2 = a(m) + 4 = T(m) + 2$ for $m \ge 2$).
- Also verified the companion Remark on `A008687`: length $L(n) = k + 1$ satisfies $L(2) = 2$, $L(2m-1) = L(m)+1$, $L(2m) = L(m)$, matching $\mathrm{A008687}(n) + 1$ for all $n \ge 2$ with the same $n = 1$ boundary ($2 \neq 1$).

### 3.4 Independent Verifier Re-run
Re-executed `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A061313/notes/check-check-1.py` (exit code `0`):
```text
Step 2 SL_2(Z) identities (L, R, J, H(c)): OK
A061313 OEIS data (90 terms) & BFS minimal steps (n=1..100): OK
A007305/A007306 (33 terms) & Step 1 M(n) recursion (2<=n<=4096): OK
n=1 exception ([[1]] sum 1 != 2) & Main Theorem P(n)=prod H(c_i), sum=a(n)+2 (2<=n<=4096): OK
PASS
```

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A061313` (rev 58, `2026-11-01`) and companion `A008687` (rev 66) still explicitly mark Zabolotskii's April 17, 2020 comments as `Conjecture:`.
- While the correspondence between regular and Hirzebruch–Jung (negative) continued fractions and Farey/$2\times 2$ matrix factorizations is classical (Hirzebruch 1973, Riemenschneider 1974, Morier-Genoud–Ovsienko `1812.00170`, Short–van Son–Zabolotskii `2312.12953`), no published proof or public repository resolution of Zabolotskii's `A061313` conjecture (linking `A061313(n) + 2` to the Hirzebruch continued fraction sum of `A007305(n)/A007306(n)` and characterizing $n = 1$ as the sole exception) was found.
- Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) all passed with no `CONTESTED.md`; direct auditor spot-checks of `facebookresearch/atlas-lean` and `rainwangphy/aftd-platform` also found 0 hits.
- **Gate 3 live pre-report re-check (all PASS within 1 hour of report, no `CONTESTED.md`; `watch-3` relieved `watch-1` per board #494):**
  - `targets/oeis-A061313/notes/novelty-gate3-watch-3.md` (`2026-11-27T00:25:29Z`, PASS)
  - `targets/oeis-A061313/notes/novelty-gate3-watch-5.md` (`2026-11-27T00:08:52Z`, PASS)
  - `targets/oeis-A061313/notes/novelty-gate3-watch-6.md` (`2026-11-27T00:21:13Z`, PASS)
