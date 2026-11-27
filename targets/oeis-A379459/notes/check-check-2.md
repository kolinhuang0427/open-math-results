# Blind Check Report — `targets/oeis-A379459/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty: PASS per `watch-1` `#1286`, `watch-5` `#1319`, `watch-6` `#1309`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary sources checked:** Live OEIS JSON for [A379459](https://oeis.org/A379459) (`rev. 4`, offset `0,1`), [A379460](https://oeis.org/A379460) (`rev. 4`, offset `0,3`), and [A006351](https://oeis.org/A006351) (`rev. 195`, offset `1,2`).
- **`TARGET.md` comparison:** Matches verbatim across all three entries (`A379459` `NAME` & `Conjecture: A(n,0) = A006351(n+2).`, `A379460` `NAME` & `Conjecture: A(n,0) = A006351(n+1).`, `A006351` `NAME`, e.g.f. reversion of $2\log(1+x)-x$, and Mikhail Kurkov's Jan 16 2025 conjecture `a(n) = A379459(n-2,0) = A379460(n-1,0) for n > 1 with a(1) = 1`).

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/oeis-A379459/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A379459/notes/check-check-2.py) (zero floating-point arithmetic; pure-Python `int` and `fractions.Fraction` formal power series in $\mathbb{Q}[[x]]$, $\mathbb{Q}[[y]]$, $\mathbb{Q}[[x,y]]$).
- **Command & result:** `.venv/bin/python -u targets/oeis-A379459/notes/check-check-2.py` exited with code `0` (`PASS`):
  1. `Live OEIS arrays`: verified $A_{459}$ and $A_{460}$ recurrences match all 45 live `A379459` `DATA` terms and all 55 live `A379460` `DATA` terms.
  2. `A006351 reversion & ODEs`: verified compositional inverse $B(x)$ of $2\ln(1+t)-t$ matches all 20 live `A006351` `DATA` terms and satisfies $B' = (1+B)/(1-B)$ and $B'' = 2(1+B)/(1-B)^3 \pmod{x^{19}}$.
  3. `Section 1 operator equivalence`: verified $H_n(y)$ and $\widetilde{W}_n(y) = (1-y)P_n(y)$ operator recursions and $\widetilde{W}_n(y) = H_{n-1}(y)$ ($n=1..11$), plus $A_{460}(n,0) = A_{459}(n-1,0)$ ($n=1..16$).
  4. `Section 2 transport PDE`: verified $\eta(x,y) \in \mathbb{Q}[[x,y]]$ solving $2\ln(1+\eta)-\eta = 2\ln(1+y)-y+x$ satisfies $\partial_x\eta = \frac{1+y}{1-y}\partial_y\eta$ and $W(x,y) = \frac{2(1+\eta)}{(1-\eta)^3} = \frac{1+y}{1-y}G(x,y)$ through total degree $12$, and $A_{459}(n,0) = \mathrm{A006351}(n+2)$, $A_{460}(n,0) = \mathrm{A006351}(n+1)$ for $n=0..16$.
