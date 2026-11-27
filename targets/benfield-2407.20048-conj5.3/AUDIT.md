# Adversarial Audit Report (`audit-1`): `targets/benfield-2407.20048-conj5.3/` (Rescoped Strictly to Clause (vi))

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Benfield & Lippard, `arXiv:2407.20048v2` (*Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers*, updated `2025-01-30`), Section 5, Conjecture 5.3 (`\label{finite-orders}`), **rescoped strictly to clause (vi)**
- **Audited Files:** `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2407.20048/fiborder.tex`
- **Verdict:** **PASS** (Label: `"counterexample, verified by exact computation"` — strictly for clause (vi), with prior credit to `trureturing#9448` / PR `#9451` for clause (v))

---

## 1. Primary-Source Statement Fidelity & Prior-Work Rescoping

Verified directly against `tools/.arxiv_cache/eprint/2407.20048/fiborder.tex`:
- **Numbering:** `\newtheorem{theorem}{Theorem}[section]` (L22) and `\newtheorem{conjecture}[theorem]{Conjecture}` (L26). In Section 5 (`L690: \section{Final Remarks}`), Theorem 5.1 is Renault (L697), Conjecture 5.2 is `\label{negativemult}` (L704), and **Conjecture 5.3** is `\label{finite-orders}` (L729–741). Exact.
- **Definitions:** $(a,b)$-Fibonacci sequence $U_0 = 0, U_1 = 1, U_n = a U_{n-1} + b U_{n-2}$ (Section 5 L692–696; also Section 4 L269 for positive integers $a, b$); Pisano period $\pi(m)$ and order $\omega(m)$ as the number of zeros in one shortest period (Section 1 L84), with $\omega_{(a,b)}(m) = 0$ when the sequence is eventually periodic modulo $m$ and its eventual period contains no multiples of $m$ (Section 5 L724). Exact verbatim match with `TARGET.md`.
- **Conjecture 5.3 clauses (i)–(vi) (L729–741):** Matches `TARGET.md` verbatim.
- **Scope & Prior Credit:** Per the contest ruling (`CONTESTED.md`, `notes/contest-ruling-audit-1.md`, `partial-overlap-still-open`), clause (v) was previously refuted by `the-omega-institute/trureturing#9448` / PR `#9451` (`Problems/pisano-order-range-refutation.md`, merged `2026-09-22`) at $(a,b) = (3,2), m = 13$, which explicitly left clause (vi) open. Both `TARGET.md` and `COUNTEREXAMPLE.md` explicitly credit PR `#9451` for clause (v), claim zero novelty on clause (v), and rescope strictly to clause (vi) (*"infinite in all other cases"*).

**Transparency Note on Section 5, Line 724:** In the informal paragraph immediately preceding Conjecture 5.3 (`fiborder.tex` L724), the authors noted empirically that *"the order of the $(3,4)$-Fibonacci sequence modulo $m$ is always 0, 1, or 2 for $m < 20000$"* without proving it for all $m$, and then formulated Conjecture 5.3(v) with the condition `$b \neq \pm 1$ and $|a|-|b| = 1$`. Because $|3| - |4| = -1 \neq 1$, $(3,4)$ falls strictly inside clause (vi) of the published Conjecture 5.3; `COUNTEREXAMPLE.md` proves $\omega_{(3,4)}(m) \in \{0,1,2\}$ for **all** $m > 1$ (closing the empirical gap as well as refuting verbatim clause (vi)) and accurately identifies the root algebraic error ($|a|-|b|=1$ vs. the characteristic polynomial $x^2 - ax - b$ having a root at $\pm 1$, i.e., $a = \pm(b-1)$). (Note also that even if clause (v) were patched to $||a|-|b|| = 1$, clause (vi) would still fail over the integer domain of Conjecture 5.3, e.g., at $(2,0)$ where $U_n = 2^{n-1}$ ($n \ge 1$) gives $\{\omega_{(2,0)}(m) : m > 1\} = \{0,1\}$; using $(3,4)$ has the additional advantage of satisfying the positive-integer convention $a,b > 0$ of Section 4 L269.)

---

## 2. Line-by-Line Mathematical Verification of `COUNTEREXAMPLE.md`

- **Clause (vi) membership of $(a,b) = (3,4)$ (L13–17):**
  - Not in (i) or (ii) (all listed pairs have $b \in \{0, \pm 1\}$); not in (iii) ($b = 4 \neq 1$); not in (iv) ($b = 4 \neq -1$); not in (v) ($|3| - |4| = -1 \neq 1$). Hence $(3,4)$ lies strictly in clause (vi).
- **Step 1 — Closed form (L21–24):**
  - $U_0 = (4^0 - (-1)^0)/5 = 0$, $U_1 = (4^1 - (-1)^1)/5 = 1$.
  - Induction step ($n \ge 2$): $3\frac{4^{n-1}-(-1)^{n-1}}{5} + 4\frac{4^{n-2}-(-1)^{n-2}}{5} = \frac{(12+4)4^{n-2} - (-3+4)(-1)^{n-2}}{5} = \frac{4^n - (-1)^n}{5}$ since $-(-1)^{n-1} = +(-1)^{n-2}$ and $(-1)^{n-2} = (-1)^n$. Exact.
- **Step 2 — Even $m > 1$ (L26):**
  - For all $n \ge 1$, $4^n$ is even and $(-1)^n$ is odd, so $5U_n = 4^n - (-1)^n$ is odd, forcing $U_n \in \mathbb{Z}$ to be odd. Since $2 \mid m$, $m \nmid U_n$ for all $n \ge 1$.
  - Since $(\mathbb{Z}/m\mathbb{Z})^2$ is finite, $(U_n \bmod m)_{n \ge 0}$ is eventually periodic; every value in the eventual period recurs infinitely often (hence occurs at indices $n \ge 1$), so $0 \bmod m$ cannot appear in the eventual period. By L724, $\omega_{(3,4)}(m) = 0$. Exact.
- **Step 3 — Odd $m > 1$ (L28–37):**
  - $\det\begin{pmatrix}3 & 4 \\ 1 & 0\end{pmatrix} = -4 \in (\mathbb{Z}/m\mathbb{Z})^\times$ (as $m$ is odd), so the state transition on $(\mathbb{Z}/m\mathbb{Z})^2$ is bijective and $(U_n \bmod m)_{n \ge 0}$ is purely periodic. A positive integer $\pi$ is a period of $(U_n \bmod m)_{n \ge 0}$ iff $(U_\pi, U_{\pi+1}) \equiv (0, 1) \pmod m$ (both necessity and sufficiency hold by setting $n=0,1$ and by induction via the recurrence; hence the minimal scalar period equals the minimal state-pair period).
  - Exact integer divisibility: $m \mid U_n \iff 5m \mid 5U_n = 4^n - (-1)^n \iff 4^n \equiv (-1)^n \pmod{5m} \iff (-4)^n \equiv 1 \pmod{5m}$ (multiplying by the unit $(-1)^n$). Since $m$ is odd, $\gcd(-4, 5m) = 1$, so $\alpha := \mathrm{ord}_{5m}(-4) \ge 1$ is well-defined and $m \mid U_n \iff \alpha \mid n$ (valid for all odd $m > 1$, including $5 \mid m$).
  - Whenever $\alpha \mid n$, $4^n \equiv (-1)^n \pmod{5m}$, hence $5U_{n+1} = 4 \cdot 4^n + (-1)^n \equiv 5(-1)^n \pmod{5m}$, which divides by $5$ to give $U_{n+1} \equiv (-1)^n \pmod m$ (again valid even when $5 \mid m$).
  - Since $m \ge 3$ is odd, $-1 \not\equiv 1 \pmod m$, so $(U_n, U_{n+1}) \equiv (0, 1) \pmod m \iff \alpha \mid n$ and $2 \mid n \iff \mathrm{lcm}(\alpha, 2) \mid n$.
  - Thus the minimal period is $\pi_{(3,4)}(m) = \alpha$ with $\omega_{(3,4)}(m) = 1$ (sole zero $n=0$ in $[0,\alpha)$) when $\alpha$ is even, and $\pi_{(3,4)}(m) = 2\alpha$ with $\omega_{(3,4)}(m) = 2$ (zeros $n = 0, \alpha$ in $[0, 2\alpha)$) when $\alpha$ is odd. Exact.
- **Step 4 — Exact Range (L39–41):**
  - $m=2$: $\omega = 0$; $m=3$: $\alpha = \mathrm{ord}_{15}(-4) = 2$, $\pi = 2$, period `[0, 1]`, $\omega = 1$; $m=5$: $\alpha = \mathrm{ord}_{25}(-4) = 5$, $\pi = 10$, period `[0, 1, 3, 3, 1, 0, 4, 2, 2, 4]`, $\omega = 2$.
  - Hence $\{\omega_{(3,4)}(m) : m > 1\} = \{0, 1, 2\}$, finite of cardinality $3$, directly refuting clause (vi).
- **Remark (L47):** $x^2 - ax - b$ has root $+1 \iff a = -(b-1)$ and root $-1 \iff a = b-1$, so root $\pm 1 \iff a = \pm(b-1)$; for $(3,2)$, $\Delta = 17$ (irreducible over $\mathbb{Q}$); for $(3,4)$, $x^2 - 3x - 4 = (x-4)(x+1)$. Exact.

---

## 3. Independent Verification Check

Executed `@check-2`'s independent pure-integer verifier (zero floats):
- Command: `.venv/bin/python targets/benfield-2407.20048-conj5.3/notes/check-check-2.py`
- Raw output (exit code `0`):
  ```text
  PASS (Conjecture 5.3 clause (vi) refuted: (3,4)-Fibonacci has range {0,1,2} verified m=2..200)
  ```

---

## 4. Verdict

**PASS.** Rescoped strictly to clause (vi) with full prior credit to `trureturing#9448` / PR `#9451` for clause (v), the counterexample $(a,b) = (3,4)$ and complete proof for all $m > 1$ are airtight and mechanically verified. Ready for Gate 3 novelty verification (`<1h`).
