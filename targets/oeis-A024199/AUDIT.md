# Blind Audit Report: `targets/oeis-A024199/` (`@audit-2`)

**Verdict: PASS**

---

## 1. Primary Source & Statement Fidelity

- **Primary source verified live:** `https://oeis.org/search?q=id:A024199&fmt=json` (OEIS `A024199`, **revision 80**, `2026-06-28T15:47:50-04:00`).
- **Verbatim check against `TARGET.md`:**
  - `NAME`: `a(n) = (2n-1)!! * Sum_{k=0..n-1}(-1)^k/(2k+1).` — exact match.
  - `OFFSET`: `0,3` — exact match.
  - `DATA`: all 21 terms `a(0) = 0` through `a(20) = 247199273204273879989500` — exact match.
  - `FORMULA` (Peter Bala, Nov 15 2016):
    > `Conjecture: a(n) = 1/2*Sum_{k = 0..2*n-1} (-1)^(n-k+1)*k!*(2*n - 2*k - 3)!!, where the double factorial of an odd integer (positive or negative) may be defined in terms of the gamma function as (2*N - 1)!! = 2^((N+1)/2)*Gamma(N/2 + 1)/sqrt(Pi).`
    > `E.g.f. 1/2*arcsin(2*x)/sqrt(1 - 2*x) = x + 2*x^2/2! + 13*x^3/3! + 76*x^4/4! + ....`
    — exact match.
- **Convention note check (`TARGET.md` L30, `PROOF.md` L10–12):** Bala's parenthetical remark writes `(2*N - 1)!! = 2^((N+1)/2)*Gamma(N/2 + 1)/sqrt(Pi)`, conflating the odd integer $M = 2N-1$ with $N$ in the standard Gamma continuation $M!! = 2^{(M+1)/2}\Gamma(M/2+1)/\sqrt{\pi} = 2^N\Gamma(N+1/2)/\sqrt{\pi}$. Both `TARGET.md` and `PROOF.md` document this cleanly and use the standard odd double factorial $(2m-1)!! = 2^m\Gamma(m+1/2)/\sqrt{\pi}$ for all $m \in \mathbb{Z}$. Note also that at $n = 0$ both the `NAME` sum and Bala's sum (`k = 0..-1`) are empty ($0 = 0$), and Theorem 1 proves all $n \ge 1$.

---

## 2. Line-by-Line Proof Verification (`PROOF.md`)

- **Section 1 & Lemma 1 (L5–20):**
  - $(2m-1)!! = 2^m\Gamma(m+1/2)/\sqrt{\pi}$ gives $\prod_{j=1}^m (2j-1)$ for $m \ge 1$, $1$ for $m = 0$, and $(-1)^r/(2r-1)!!$ for $m = -r \le -1$ ($r \ge 1$).
  - Lemma 1 ($(2m-1)(2m-3)!! = (2m-1)!!$ for all $m \in \mathbb{Z}$) follows directly from $\Gamma(m+1/2) = (m-1/2)\Gamma(m-1/2)$ and is also verified across all four piecewise regimes ($m \ge 2$, $m = 1$, $m = 0$, $m = -r \le -1$).
  - *Harmless editorial note (non-blocking):* L12 parenthetically says *"where we interpret $(-1)!! = 1$ in the denominator for $r = 1$"*; at $r = 1$ the denominator in $(-1)^r/(2r-1)!!$ is actually $1!! = 1$ (already covered by the $m \ge 1$ branch), not $(-1)!!$. The formula on L11, the displayed values $(-3)!! = -1$ and $(-5)!! = 1/3$, and every step of Lemma 1 and Theorems 1–2 are completely unaffected and exact.
- **Section 2 & Lemma 2 (L22–28):** $a(n) - (2n-1)a(n-1) = (-1)^{n-1}(2n-3)!!$ for all $n \ge 1$ (with $a(0) = 0$) is verified directly for $n = 1$ ($1 - 0 = (-1)^0(-1)!!$) and for $n \ge 2$ via $(2n-1)!! = (2n-1)(2n-3)!!$. **PASS.**
- **Section 3 & Theorem 1 (L30–71):**
  - Base case $n = 1$: $T(1,0) = 1$, $T(1,1) = (-1)(-1) = 1$, $b(1) = 1 = a(1)$.
  - Inductive step ($n \ge 2$, $0 \le k \le 2n-3$): both row-shift identities $T(n, k) = -(2n-2k-3)T(n-1, k)$ (via Lemma 1 with $m = n-k-1$) and $T(n, k+1) = (k+1)T(n-1, k)$ are exact; combining with $(2n-2k-3) + 2(k+1) = 2n-1$ yields $T(n, k) - (2n-1)T(n-1, k) = 2(T(n, k) - T(n, k+1))$.
  - Summing $k = 0, \dots, 2n-3$ and adding $T(n, 2n-2) + T(n, 2n-1)$ gives $2b(n) - 2(2n-1)b(n-1) = 2T(n, 0) - T(n, 2n-2) + T(n, 2n-1)$.
  - Boundary evaluations for $n \ge 2$: $T(n, 0) = (-1)^{n-1}(2n-3)!!$, $T(n, 2n-2) = \frac{(2n-2)!}{(2n-3)!!} = 2^{n-1}(n-1)!$, and $T(n, 2n-1) = \frac{(2n-1)!}{(2n-1)!!} = 2^{n-1}(n-1)! = T(n, 2n-2)$, giving exact cancellation and $b(n) - (2n-1)b(n-1) = (-1)^{n-1}(2n-3)!!$. By induction and Lemma 2, $b(n) = a(n)$ for all $n \ge 1$. **PASS.**
- **Section 4 & Theorem 2 (L73–84):** Multiplying Lemma 2 by $x^{n-1}/(n-1)!$ and summing over $n \ge 1$ yields $(1-2x)Y'(x) - Y(x) = \sum_{m \ge 0} (-1)^m \frac{(2m-1)!!}{m!} x^m = \sum_{m \ge 0} \binom{-1/2}{m}(2x)^m = (1+2x)^{-1/2}$ in $\mathbb{Q}[[x]]$ with $Y(0) = 0$. Multiplying by the unit $(1-2x)^{-1/2}$ gives $\frac{d}{dx}((1-2x)^{1/2}Y(x)) = (1-4x^2)^{-1/2} = \frac{d}{dx}(\frac{1}{2}\arcsin(2x))$, so $Y(x) = \frac{\arcsin(2x)}{2\sqrt{1-2x}}$ in $\mathbb{Q}[[x]]$. **PASS.**

---

## 3. Independent Verification & Gate 2 Novelty

- **Checker script:** Re-ran `.venv/bin/python -u targets/oeis-A024199/notes/check-check-3.py` — `exit 0`, raw output `PASS`, AST `FLOAT_CONSTANTS: 0` (exact `int`/`Fraction` arithmetic verifying OEIS `DATA`, Sloane recurrence, Lemma 1 on $[-40, 40]$, Lemma 2 & Theorem 1 on $[1, 50]$, and Theorem 2 ODE & series identity mod $x^{41}$).
- **Zenodo & Gate 2 receipts:** Independently verified `0` hits for `A024199` in `watch/snapshots/zenodo-23112421-oeis-ids.md`; all three Gate 2 receipts (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`) PASS.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.
