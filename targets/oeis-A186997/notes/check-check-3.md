# Independent Check Report: `oeis-A186997`

- **Checker:** `@check-3`
- **Verdict:** **PASS**
- **Primary Source:** Live OEIS `A186997` (rev. 85, `https://oeis.org/search?q=id:A186997&fmt=json`).
- **Gate 2 Watch Status:** Pending `@watch-1 @watch-5 @watch-6` (requested in `#638`).

## 1. Primary-Source Fidelity Check

- **Verbatim match:** `TARGET.md` L13–18 quotes the `NAME` (`G.f. satisfies: A(x) = 1 + x*A(x)^3 + x^2*A(x)^4.`) and Peter Bala's `COMMENTS` (Aug 02 2016: both 2-adic valuation conjectures checked up to $n=100$) verbatim from live OEIS `A186997` rev. 85.

## 2. Proof Audit & Independent Mechanical Verification

- Checked `PROOF.md` Steps 1–4 line by line:
  - **Step 1:** $W(x) := x A(x^2)$ satisfies $W(x)(1 - W(x)^2) = x(1 + W(x)^4)$ in $\mathbb{Z}[[x]]$; Lagrange Inversion yields $(2k+1) a(k) = [z^k]\left((1-z) + \frac{2z}{1-z}\right)^{2k+1} = \sum_{j=0}^k t_j$ with $t_j = (-1)^{k-j} 2^j \binom{2k+1}{j} \binom{2k+1-2j}{k-j}$ (since $2k+1-2j \ge 1$ for $0 \le j \le k$, and $j > k$ has no $z^k$ term).
  - **Step 2:** Legendre/Kummer identities $v_2(C_m) = s_2(m+1) - 1$, $v_2\binom{2k+1-2j}{k-j} = s_2(k+1-j) - 1$, and $s_2(k+1-j) \ge s_2(k+1) - s_2(j)$ are exact.
  - **Step 3 ($k = 2m+1, m \ge 0$):** $v_2(t_0) = v_2(C_{2m+1}) = v_2(C_m)$, $v_2(t_1) = 1 + v_2(m+1) + v_2(C_k) > v_2(t_0)$, and for $j \ge 2$, $v_2(t_j) \ge v_2(C_m) + v_2(j!) \ge v_2(C_m) + 1 > v_2(t_0)$.
  - **Step 4 ($k = 2m, m \ge 2$):** $t_0 + t_1 = -k\binom{2k+1}{k}$ has $v_2(t_0 + t_1) = 3 + v_2(C_{m-2}) = s_2(m) + r - 1$ ($r = v_2(m) + 2 \ge 2$). Case A ($2 \le j \le 2^r - 1 < 4m$): $v_2\binom{4m}{i} = r - v_2(i)$ for $1 \le i \le 2^r - 1$ gives $v_2\binom{4m+1}{j} = r - \max(v_2(j), v_2(j-1))$ and $j - s_2(j) - v \ge 0$, so $v_2(t_j) \ge s_2(m) + r > v_2(t_0 + t_1)$. Case B ($j \ge 2^r$): $j - s_2(j) \ge 2^r - 1 \ge r + 1 > r - 1$, so $v_2(t_j) \ge s_2(m) + r + 1 > v_2(t_0 + t_1)$.
- Wrote and executed independent exact-integer verifier [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A186997/notes/check-check-3.py) (AST `FLOAT_COUNT: 0`):
  1. `[1/4]` Computed $a(0)\dots a(250)$ directly from $A(x) = 1 + x A(x)^3 + x^2 A(x)^4$ and matched OEIS rev. 85 opening terms.
  2. `[2/4]` Verified $(2k+1)a(k) = \sum_{j=0}^k t_j$, every $v_2(t_j)$ formula, and $s_2$ subadditivity for all $0 \le k \le 250$.
  3. `[3/4]` Verified $j - s_2(j) - \max(v_2(j), v_2(j-1)) \ge 0$ ($2 \le j \le 1000$) and all Step 3/Step 4 $v_2$ inequalities + Bala's conjectures up to $k = 250$ ($m \le 124$, past $n = 100$).
  4. `[4/4]` Verified $W(x)(1 - W(x)^2) = x(1 + W(x)^4) \pmod{x^{60}}$.

### Raw Verifier Output

Command: `.venv/bin/python -u targets/oeis-A186997/notes/check-check-3.py` (exit code `0`):
```text
[1/4] Computing A(x) directly from A(x) = 1 + x*A^3 + x^2*A^4 up to k=250...
[2/4] Verifying Step 1 Lagrange inversion sum (2k+1)*a(k) = sum_j t_j and W(x) identity...
[3/4] Verifying Step 3 (odd k = 2m+1) & Step 4 (even k = 2m) ultrametric domination...
[4/4] Verifying symbolic power series identity W(x)*(1 - W(x)^2) = x*(1 + W(x)^4) mod x^60...
PASS
```
