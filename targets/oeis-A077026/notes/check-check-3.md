# Check Report — `oeis-A077026` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A077026&fmt=text` (`%I A077026 #14 Sep 27 2016 06:14:53`).
- **`TARGET.md` check:** Revision (`rev. 14`), `%N` definition `a(n) = Sum_{k=1..n} floor(n/k + 1)-floor(n/k + 1/2)`, `%O` (`1,2`), `%S..%U` initial 73 terms ($a(1)=1$ through $a(73)=48$), and Benedict W. J. Irwin's Sep 22, 2016 `%F` conjecture match the live OEIS record verbatim.

## Proof / Counterexample Verification (`COUNTEREXAMPLE.md`)
- Audited `COUNTEREXAMPLE.md` lines 1–39:
  - Minimal counterexample $n = 1$: $a(1) = 1 \ne S(1) = 0$ (empty sum); $n = 2$: $a(2) = 2 \ne S(2) = 1$.
  - Universal refutation & discrepancy proof: reindexing $d = n - k \in \{1,\dots,n-1\}$ gives $n \equiv k \pmod d$, so $1 - f(n,k) = \mathbf{1}_{\{2(n \bmod d) < d\}}$, which matches the $d$-th term of $a(n)$ identically for $1 \le d \le n-1$, while $d = n$ contributes $\lfloor 2 \rfloor - \lfloor 3/2 \rfloor = 1$. Hence $S(n) = a(n) - 1$ for every $n \ge 1$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A077026/notes/check-check-3.py) (pure `int` arithmetic using exact integer division, `FLOAT_COUNT: 0`).
- Checked all 73 OEIS `%S..%U` terms ($n=1..73$), explicit counterexamples $n=1,2$, termwise congruence correspondence, and $S(n) = a(n) - 1$ for all $n=1..200$.
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```
