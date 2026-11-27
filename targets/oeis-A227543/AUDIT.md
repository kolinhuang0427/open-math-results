# Adversarial Audit Report (`audit-1`): `targets/oeis-A227543/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A227543` (rev. 113, Oct 03 2026 `19:42:30`) — Mikhail Kurkov's Sep 26, 2024 Stieltjes continued-fraction triangle conjecture $b(n) = P(n, n)$ for arbitrary $f(m)$ (specializing to $f(m) = q^m$ for `A227543`)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, live OEIS `A227543` rev. 113 (`fmt=text`), `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A227543` (`#113 Oct 03 2026 19:42:30`):**
  - `%N`: `Triangle defined by g.f. A(x,q) such that: A(x,q) = 1 + x*A(q*x,q)*A(x,q), as read by terms k=0..n*(n-1)/2 in rows n>=0.` — verbatim match.
  - `%F`: `Conjecture: b(n) = P(n, n) where b(n) is an integer sequence with g.f. B(x) = 1/(1 - f(0)*x/(1 - f(1)*x/(1 - f(2)*x/(1 - f(3)*x/(1 - f(4)*x/(1 -...)))))), P(n, k) = P(n-1, k) + f(n-k)*P(n, k-1) for 0 < k <= n with P(n, k) = 0 for k > n, P(n, 0) = 1 for n >= 0 and where f(n) is an arbitrary function. In fact for this sequence we have f(n) = q^n. - _Mikhail Kurkov_, Sep 26 2024` — verbatim match.
  - `%S/%T/%U` (all 93 terms, rows $n = 0..8$) match `notes/check-check-2.py` verbatim.
- **Snapshot cross-check:** `A227543` has `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.
- **Gate 2 novelty receipts:** Present from `watch-1` (`#1057`), `watch-5` (`#1041`), `watch-6` (`#1044`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Step 1 (Well-definedness & uniqueness of $B_m(x)$ in $R[[x]]$, L22–28):**
  - Over any commutative ring $R$ with $1$, every $1 - f(m) x B_{m+1}^{(N)}(x)$ has constant term $1$ and is a unit in $R[[x]]$.
  - Backward induction from $m = N+1$ ($B_{N+1}^{(N+1)} \equiv 1 = B_{N+1}^{(N)} \pmod{x^1}$) shows $B_m^{(N+1)}(x) \equiv B_m^{(N)}(x) \pmod{x^{N-m+2}}$ for all $0 \le m \le N+1$. Thus $B_m(x) = \lim_{N \to \infty} B_m^{(N)}(x) \in 1 + xR[[x]]$ exists $x$-adically, is uniquely determined by degree-by-degree induction on $[x^k]$, and satisfies $B_m(x) - 1 = f(m) x B_m(x) B_{m+1}(x)$ for all $m \ge 0$.
- **Step 2 (Diagonal product generating functions, L30–34):**
  - Setting $\widetilde{R}_{-1}(x) = 1$ and $\widetilde{R}_d(x) = \prod_{j=0}^d B_j(x) \in 1 + xR[[x]]$ ($d \ge 0$), we have $\widetilde{R}_d = \widetilde{R}_{d-1} B_d$ and $\widetilde{R}_{d+1} = \widetilde{R}_{d-1} B_d B_{d+1}$ for all $d \ge 0$. Multiplying $B_d - 1 = f(d) x B_d B_{d+1}$ by $\widetilde{R}_{d-1}$ yields $\widetilde{R}_d(x) - \widetilde{R}_{d-1}(x) = f(d) x \widetilde{R}_{d+1}(x)$ for all $d \ge 0$.
- **Step 3 (Coefficient extraction & identification with $P(n, k)$, L36–59):**
  - With $\widetilde{Q}(d, k) = [x^k]\widetilde{R}_d(x)$, we have $\widetilde{Q}(d, 0) = 1$ ($d \ge -1$), $\widetilde{Q}(-1, k) = 0$ ($k \ge 1$), and $\widetilde{Q}(d, k) = \widetilde{Q}(d-1, k) + f(d)\widetilde{Q}(d+1, k-1)$ ($d \ge 0, k \ge 1$).
  - Defining $\widetilde{P}(n, k) = \widetilde{Q}(n-k, k)$ for $0 \le k \le n$ and $0$ for $k > n$ reproduces all boundary conditions ($k = 0$ and $k > n$) and Kurkov's recurrence for all $0 < k \le n$ (explicitly checking both $k < n$ and $k = n$, where $\widetilde{P}(n-1, n) = 0 = \widetilde{Q}(-1, n)$, and $k - 1 < n$).
  - Well-founded induction on $k \ge 0$ (and inner induction on $n \ge k$) gives $P(n, k) = \widetilde{P}(n, k)$ for all $n, k \ge 0$, whence $P(n, n) = \widetilde{Q}(0, n) = [x^n]B_0(x) = b(n)$ for all $n \ge 0$.
- **Step 4 (Specialization to OEIS `A227543`, L61–64):**
  - Setting $R = \mathbb{Z}[q]$ and $f(m) = q^m$: the unique $x$-adic fixed point $A(x, q) \in 1 + x\mathbb{Z}[q][[x]]$ of $A(x, q) = 1 + x A(qx, q) A(x, q)$ satisfies $A(q^m x, q) = (1 - q^m x A(q^{m+1} x, q))^{-1}$ for all $m \ge 0$, forcing $B_m(x) = A(q^m x, q)$ and $[x^n]A(x, q) = b(n) = P(n, n)$ for all $n \ge 0$.

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A227543/notes/check-check-2.py`:
- Exit code `0`, output `PASS` (zero floats; pure exact sparse integer polynomials in $\mathbb{Z}[f_0,\dots,f_9]$ and $\mathbb{Z}[q]$).
- Independently verified Steps 1–3 universally in $\mathbb{Z}[f_0,\dots,f_9][[x]] \bmod x^{10}$, the $f(m)=q^m$ specialization through $n = 12$, all 93 live OEIS `A227543` terms (rows $0..8$), and four diverse integer specializations through $n = 20$.
