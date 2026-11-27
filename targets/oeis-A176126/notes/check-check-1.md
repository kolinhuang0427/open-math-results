# Independent Check Report — `oeis-A176126`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A176126`](https://oeis.org/search?q=id:A176126&fmt=text) (`#18 Aug 27 2022 03:13:41`, offset `0,4`) and [`A127276`](https://oeis.org/search?q=id:A127276&fmt=text) (`#33 Nov 25 2026 15:43:26`).
- **Verbatim match:** `TARGET.md` L18–22 matches live OEIS `A176126` `%N`, `%C` (`-1/0, -1/1, 1/3, ...`), and Mathar's Dec 12 2010 `%F` `Conjecture:` verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A176126/notes/check-check-1.py` (`int`, `Fraction`, and SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Lemma 1 (`A127276(n) = 2^n - n(n+1)2^{n-2}$):**
   - Verified `A127275` series expansion $\frac{\sqrt{1-4x}-x}{1-4x}$ matches $b_0 = 1$, $b_m = \binom{2m}{m} - 4^{m-1}$ ($1 \le m \le 18$).
   - Verified $P_k(t(z)) = z^k + z^{-k}$, $P_k(4) = 2$, $P_k(0) = 2(-1)^k$ ($k \ge 1$), and directly checked $M_n = C_n - \frac{1}{4}vv^T + \frac{1}{4}e_0 e_0^T$, $P C_n P^T = \mathrm{diag}(1, 2, \dots, 2)$, $v^T C_n^{-1} v = e_0^T C_n^{-1} e_0 = 2n+1$, $v^T C_n^{-1} e_0 = (-1)^n$, and $\det(M_n) = 2^n - n(n+1)2^{n-2}$ for $n = 0..8$.
2. **Reduced numerator, g.f., and 9-term recurrence (`n <= 150`):**
   - Verified exact `Fraction(-A127276(n), A001788(n)).numerator` equals the mod-$4$ piecewise closed form for $1 \le n \le 150$, matching live OEIS `%S` (`0..79`) and `%C` (`1..12`) verbatim.
   - Verified $a(n) - 3a(n-4) + 3a(n-8) - a(n-12) = 0$ ($12 \le n \le 150$), exact polynomial identities for $N(x)$, $-(1+x)^3 N(x) = P(x)$, $(1-x^4)^3 = -(x-1)^3(x+1)^3(x^2+1)^3$, $D(x) = (x-1)^3(x^2+1)^3$, formal convolution $D(x)A(x) = N(x)$ mod $x^{151}$, SymPy series match up to $x^{20}$, and Mathar's 9-term recurrence for $9 \le n \le 150$.

## 3. Gate 2 Status

Gate 2 PASS receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`.
