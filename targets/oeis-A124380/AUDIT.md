# Adversarial Audit Report (`audit-1`): `targets/oeis-A124380/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A124380` (rev. 39, Oct 22 2025 `08:33:40`) — Vaclav Kotesovec's Sep 18, 2024 logarithmic asymptotic conjecture $\log a(n) \sim \frac{n\log n}{2} - \frac{1+\log 2}{2} n$
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, live OEIS `A124380` rev. 39 (`fmt=text`), `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A124380` (`#39 Oct 22 2025 08:33:40`):**
  - `%O`: `0,3`; `%S/%T/%U` ($n = 0..29$) match `TARGET.md` and `notes/check-check-1.py` verbatim.
  - `%N`: `O.g.f.: A(x) = Sum_{n>=0} x^n*Product_{k=0..n} (1 + k*x).` matches `PROOF.md` L9 verbatim.
  - `%F`: `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2. - _Vaclav Kotesovec_, Sep 18 2024` matches `TARGET.md` and `PROOF.md` verbatim.
  - Establishing $\log a(n) = \frac{n\log n}{2} - \frac{1+\log 2}{2} n + O(n^{3/4}\log n)$ proves both the literal ratio equivalence $\log a(n) \sim \frac{n\log n}{2} - \frac{1+\log 2}{2} n$ and the two-term asymptotic expansion $\lim_{n\to\infty}\frac{\log a(n) - \frac{n}{2}\log n}{n} = -\frac{1+\log 2}{2}$.
- **Snapshot cross-check:** `A124380` has `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.
- **Gate 2 novelty receipts:** Present from `watch-5` (`#977`) and `watch-6` (`#980`); `@watch-1` will verify at Gate 3.

---

## 2. Line-by-Line Proof Audit — PASS

- **Section 1 (L7–12):** Since the $j=0$ factor is $1$, $\prod_{j=0}^m (1+jx) = \prod_{j=1}^m (1+jx) = \sum_{r=0}^m e_r(1,\dots,m)x^r$ (including $m=0$ with $e_0 = 1$). Extracting $[x^n]A(x)$ sets $m = n - r$ with $0 \le r \le n - r \iff 0 \le r \le \lfloor n/2 \rfloor$, giving $a(n) = \sum_{r=0}^{\lfloor n/2 \rfloor} e_r(1,\dots,n-r)$ for all $n \ge 0$.
- **Section 2 — Lemma 1 (L14–37):** Let $n \ge 4$, $k = \lfloor n/2 \rfloor \ge 2$.
  - *Lower bound:* Retaining only $r = k$ gives $e_k(1,\dots,k) = k!$ when $n = 2k$, and $e_k(1,\dots,k+1) = \sum_{j=1}^{k+1}\frac{(k+1)!}{j} > k!$ when $n = 2k+1$, so $a(n) \ge k!$ for all $n \ge 2$.
  - *Termwise upper bound:* For $r \in \{0,\dots,k\}$, $t = k - r \in \{0,\dots,k\}$, $m = n - r$: $2k \le n \le 2k+1$ yields $k + t \le m \le k + 1 + t$ and $m - r = n - 2r \ge 2t \ge 0$. Each $r$-subset product is $\le m!/(m-r)!$, so $e_r(1,\dots,m) \le \binom{m}{r}\frac{m!}{(m-r)!} = \frac{(m!)^2}{r!\,((m-r)!)^2} \le \frac{((k+1+t)!)^2}{(k-t)!\,((2t)!)^2}$.
  - At $t = 0$: $\frac{((k+1)!)^2}{k!\,(0!)^2} = (k+1)^2 k! \le (2k+1)^2 k!$.
  - For $1 \le t \le k$: $k+1+t \le 2k+1$, and $\frac{(k+1+t)!}{k!}$ has $t+1$ factors while $\frac{(k+1+t)!}{(k-t)!}$ has $2t+1$ factors (all $\le 2k+1$), giving $\frac{((k+1+t)!)^2}{(k-t)!\,k!} \le (2k+1)^{3t+2}$. From $e^M > M^M/M!$ at $M = 2t \ge 2$, $((2t)!)^2 > (2t/e)^{4t} = (16t^4/e^4)^t$, so $\frac{e_r(1,\dots,m)}{k!} \le (2k+1)^2 \bigl(\frac{(2k+1)^3 e^4}{16 t^4}\bigr)^t$. With $T = e(2k+1)^{3/4} > 0$: $t \ge T$ makes the base $< 1/16 < 1$ (giving $\le (2k+1)^2$), while $1 \le t < T$ drops $((2t)!)^2 \ge 1$ to get $\le (2k+1)^{3t+2} < (2k+1)^{3T+2}$. Summing over all $k+1$ terms yields $a(n) \le (k+1)(2k+1)^{3e(2k+1)^{3/4}+2} k!$.
- **Section 3 — Theorem (L39–53):**
  - Monotonicity of $\log x$ on $[1,\infty)$ gives $k\log k - k + 1 = \int_1^k \log x\,dx \le \log(k!) \le \int_1^{k+1}\log x\,dx = (k+1)\log(k+1) - k$ for $k \ge 2$.
  - Writing $k = \frac{n}{2} - \theta_n$ ($\theta_n \in \{0, 1/2\}$) gives $\log k = \log n - \log 2 + O(1/n)$, $(k+1)\log(k+1) - k\log k = O(\log n)$, and $\log(k!) = \frac{n\log n}{2} - \frac{1+\log 2}{2} n + O(\log n)$.
  - Taking logarithms in Lemma 1 adds an error in $[0, \log(k+1) + (3e(2k+1)^{3/4}+2)\log(2k+1)] = O(n^{3/4}\log n)$, yielding $\log a(n) = \frac{n\log n}{2} - \frac{1+\log 2}{2} n + O(n^{3/4}\log n)$, from which both $\log a(n) \sim \frac{n\log n}{2} - \frac{1+\log 2}{2} n$ and $\lim_{n\to\infty}\frac{\log a(n) - \frac{n}{2}\log n}{n} = -\frac{1+\log 2}{2}$ follow immediately.

---

## 3. Independent Exact & Interval Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A124380/notes/check-check-1.py`:
- Exit code `0`, output `PASS` (exact Python `int` + zero-float `mpmath.iv` at `dps = 30`).
- Verified exact OGF coefficients against all 30 live OEIS terms ($n = 0..29$), the Section 1 $e_r$ identity ($n = 0..160$), and all Lemma 1 & Section 3 inequalities ($n = 4..160$).
