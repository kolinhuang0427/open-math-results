# Check Report — `oeis-A075997` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A075997&fmt=text` (`%I A075997 #37 Jun 14 2025 09:50:29`).
- **`TARGET.md` check:** Revision (`rev. 37`), `%N` definition `a(n) = [n/2] - [n/3] + [n/4] - [n/5] + [n/6] - ...`, `%O` (`0,5`), `%S..%U` initial 80 terms ($a(0)=0$ through $a(79)=21$), and Benedict W. J. Irwin's Sep 23, 2016 `%F` conjecture match the live OEIS record verbatim.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–38:
  - Base cases $n = 0, 1$ give $0 = 0$.
  - Step 1: summation swap $\sum_{m=1}^n (-1)^m \lfloor n/m \rfloor = \sum_{k=1}^n \sum_{m=1}^{\lfloor n/k \rfloor} (-1)^m$ yields $a(n) = \sum_{k=1}^{n-1} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ even}\}}$ (since $\lfloor n/n \rfloor = 1$ is odd).
  - Step 2: since $(n+k)-(n-k) = 2k$, $r := (n+k) \bmod 2k = (n-k) \bmod 2k$, so $f(n+k,n-k)=1 \iff 2r \ge 2k \iff n \bmod 2k \in \{0,\dots,k-1\} \iff \lfloor n/k \rfloor$ is even for all $1 \le k \le n-1$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A075997/notes/check-check-3.py) (pure `int` arithmetic, `FLOAT_COUNT: 0`).
- Checked all 80 OEIS `%S..%U` terms ($n=0..79$), Step 1 parity identity, Step 2 termwise equivalence for all $1 \le k \le n-1$, and full equality $a(n) = \sum_{k=1}^{n-1} f(n+k, n-k)$ for all $n=0..200$.
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```
