# Adversarial Audit Report: `targets/oeis-A092920/`

- **Auditor:** `audit-1`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Gate 3 Status:** Pending live Gate 3 re-checks (`@watch-1`, `@watch-5`, `@watch-6`)

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A092920` (`https://oeis.org/search?q=id:A092920&fmt=json`, rev `56`, `2026-03-14T12:38:00-04:00`), plus direct StackExchange API searches of MathOverflow and Math.StackExchange (`A092920`, `strongly monotone partitions`).
- `targets/oeis-A092920/TARGET.md`
- `targets/oeis-A092920/PROOF.md`
- `targets/oeis-A092920/notes/check-check-3.md`
- `targets/oeis-A092920/notes/check-check-3.py`
- Gate 2 receipts `notes/novelty-gate2-watch-{1,5}.md` (and confirmed absence of `CONTESTED.md`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Statement Fidelity

- **Live OEIS `A092920` (rev `56`, `2026-03-14`):**
  - Name: *"Number of strongly monotone partitions of [n]."*
  - Comment: *"A partition is strongly monotone if its blocks can be written in increasing order of their least element and increasing order of their greatest element, simultaneously."*
  - Conjecture (`_Mikhail Kurkov_`, Apr 24 2023): *"Conjecture: a(n) = Sum_{k=0..2^(n-1) - 1} b(k) for n > 0 with a(0) = 1 where b(2^m*(2n+1)) = Sum_{k=0..[m > 0]*(m-1)} binomial(m-1, k)*b(2^k*n) for m >= 0, n >= 0 with b(0) = 1."*
- **Match:** `TARGET.md` and `PROOF.md` match live OEIS `A092920` rev 56 verbatim (`m = 0` uses standard $\binom{-1}{0} = 1$ giving $b(2n+1) = b(n)$, matching OEIS data `1, 1, 2, 4, 9, ...`). Zero quantifier, domain, or index drift.

---

## 3. Adversarial Line-by-Line Mathematical Audit

- **Section 1 (FIFO bijection $\Phi$ & continued fraction for $A(x)$):**
  - Verified every transition of $\Phi$ between strongly monotone partitions of $[n]$ and labeled Motzkin paths $\mathcal{M}_n$ (height $0$: $H_0$ weight $1$, $U$ weight $1$; height $h \ge 1$: $U, D$ weight $1$, $H^{(r)}$ weight $h$). Singleton $\{t\}$ cannot lie inside the span of any open block (forcing $h = 0$); closing a non-singleton block must close the oldest open block $Q[0]$ by strong monotonicity; replay on a FIFO queue recovers a unique strongly monotone partition with $\Phi \circ \Phi^{-1} = \mathrm{id}$ and $\Phi^{-1} \circ \Phi = \mathrm{id}$.
  - First-return decomposition at height $m$ gives $P_0(x) = (1 - x - x^2 P_1(x))^{-1}$ and $P_m(x) = (1 - mx - x^2 P_{m+1}(x))^{-1}$ for $m \ge 1$. With $B_m := P_{m+1}$, $A(x) = (1 - x - x^2 B_0(x))^{-1}$ and $B_m(x) = (1 - (m+1)x - x^2 B_{m+1}(x))^{-1}$ for all $m \ge 0$, matching OEIS `A092920`'s established J-fraction verbatim.
- **Section 2 (Binary-sum EGF & PDE):**
  - Splitting $r \in \{0, \ldots, 2^N - 1\}$ into even $2y$ and odd $2n+1$ gives $R_0(N) = R_1(N-1) + R_0(N-1)$ and $R_j(N) = R_{j+1}(N-1) + \sum_{k=0}^{j-1}\binom{j-1}{k} R_k(N-1)$ for all $N \ge 1, j \ge 1$.
  - Multiplying by $z^{j-1}/(j-1)!$ and summing over $j \ge 1$ yields $F_N'(z) = F_{N-1}''(z) + e^z F_{N-1}(z)$ with $F_N(0) = F_{N-1}(0) + F_{N-1}'(0)$ and $F_0(z) = e^z$.
  - Induction on $N$ proves each $F_N(z)$ is a polynomial in $u = e^z$ of degree $\le N + 1$ (since $F_{N-1}'' + u F_{N-1}$ has zero constant term in $u$ and $\mathbb{Q}[u] \hookrightarrow \mathbb{Q}[[z]]$ via $u = e^z$ is injective intertwining $\partial_z$ and $u\partial_u$).
  - Summing $H(x, u) = 1 + x\sum_{N \ge 0} F_N(u) x^N = \sum_{k \ge 0} p_k(x) u^k$ gives $p_k(x) \in x^k\mathbb{Q}[[x]]$, exact PDE $x u \partial_u^2 H + (x - 1)\partial_u H + x H = 0$, and boundary condition $(1 - x) H(x, 1) - x \partial_u H(x, 1) = 1$ (exact cancellation of $x$ verified).
- **Section 3 (Hypergeometric solution & $x$-adic continued-fraction identification):**
  - Coefficient extraction $[u^k]$ yields $p_k(x) = p_0(x)\frac{x^k}{k! \prod_{j=1}^k(1-jx)}$ in $\mathbb{Q}[[x]]$; $x$-adic convergence at $u = 1$ gives $H(x, 1) = (1 - x - x S_1(x)/S_0(x))^{-1}$ with all denominators units in $1 + x\mathbb{Q}[[x]]$.
  - Verified both identities on $c_{m, r}(x) = \frac{x^r}{r! \prod_{j=1}^r(1-(m+j)x)}$: $r c_{m,r} = \frac{x}{1-(m+1)x} c_{m+1,r-1}$ (giving $S_1(x) = \frac{x}{1-x} U_1(x)$) and $(1-(m+1)x) c_{m,r} = (1-(m+1)x) c_{m+1,r} - x r c_{m+1,r}$ for all $r \ge 0$ (both $r = 0$ and $r \ge 1$ checked explicitly).
  - Summing over $r \ge 0$ and dividing by $(1-(m+1)x) U_{m+1}(x)$ gives $C_m(x) = (1 - (m+1)x - x^2 C_{m+1}(x))^{-1}$ for $C_m = U_{m+1}/((1-(m+1)x)U_m) \in 1 + x\mathbb{Q}[[x]]$.
  - Difference $C_m - B_m \in x^2(C_{m+1} - B_{m+1})\mathbb{Q}[[x]]$ yields $C_0 - B_0 \in \bigcap_{K \ge 1} x^{2K}\mathbb{Q}[[x]] = \{0\}$, hence $H(x, 1) = (1 - x - x^2 C_0(x))^{-1} = (1 - x - x^2 B_0(x))^{-1} = A(x)$, proving $a(n) = R_0(n-1) = \sum_{k=0}^{2^{n-1}-1} b(k)$ for all $n > 0$. **No gaps.**

---

## 4. Independent Mechanical Verification & Novelty Status

- **Independent script re-execution:** Re-ran `.venv/bin/python -u /Users/kev/Documents/open-math/targets/oeis-A092920/notes/check-check-3.py`: exited with status `0`, outputting `PASS` (verified bijection for $n \le 7$, J-fraction matching all $28$ OEIS terms $n \le 27$, direct Kurkov sums for $n \le 15$, and Sections 2–3 exact formal power series identities through degree $13$).
- **Novelty status:** Live OEIS `A092920` rev `56` (`2026-03-14`) remains marked `Conjecture:`; MathOverflow and Math.StackExchange searches returned `0` hits for `A092920`; Gate 2 receipts `notes/novelty-gate2-watch-{1,5}.md` both PASS; no `CONTESTED.md`.
- **Gate 3 receipts:** Pending (requested from `@watch-1`, `@watch-5`, `@watch-6`).
