# Independent Check Report: `targets/benfield-2407.20048-conj5.3` (Rescoped Clause (vi))

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/benfield-2407.20048-conj5.3/notes/check-check-2.py`

## 1. Primary Source Fidelity & Rescoping
Checked against `arXiv:2407.20048v2` (`fiborder.tex`, lines 84, 269, 692–696, 724, 729–741):
- Definition of $(a,b)$-Fibonacci sequence (`U_0=0, U_1=1, U_n = a U_{n-1} + b U_{n-2}`) and order $\omega_{(a,b)}(m)$ (including $\omega=0$ when the eventual period mod $m$ contains no multiples of $m$) match `TARGET.md` verbatim.
- Conjecture 5.3 (`\label{finite-orders}`) parts (i)–(vi) match `TARGET.md` verbatim, and both `TARGET.md` and `COUNTEREXAMPLE.md` are rescoped strictly to clause (vi) (*"infinite in all other cases"*) with explicit prior credit to `the-omega-institute/trureturing#9448` / PR `#9451` for clause (v).

## 2. Independent Exact Mechanical Verification
Command:
```sh
.venv/bin/python targets/benfield-2407.20048-conj5.3/notes/check-check-2.py
```
Output:
```
PASS (Conjecture 5.3 clause (vi) refuted: (3,4)-Fibonacci has range {0,1,2} verified m=2..200)
```
All checks use pure exact integer modular state-tracking (zero floating point):
- **Clause (vi) membership of $(a,b) = (3,4)$:** Verified $(3,4)$ is excluded from (i)–(v) ($b = 4 \notin \{0,\pm 1\}$, $|3|-|4| = -1 \neq 1$).
- **Closed form:** $U_n = (4^n - (-1)^n)/5$ verified against the recurrence for $0 \le n \le 60$.
- **Exhaustive modular check ($2 \le m \le 200$):** Confirms $\omega_{(3,4)}(m) = 0$ for all even $m$, and for all odd $m > 1$, $\pi_{(3,4)}(m) = \alpha = \mathrm{ord}_{5m}(-4)$ with $\omega = 1$ when $\alpha$ is even and $\pi_{(3,4)}(m) = 2\alpha$ with $\omega = 2$ when $\alpha$ is odd. Explicit values $\omega_{(3,4)}(2)=0$, $\omega_{(3,4)}(3)=1$ (period `[0,1]`), and $\omega_{(3,4)}(5)=2$ (period `[0,1,3,3,1,0,4,2,2,4]`) verified.
