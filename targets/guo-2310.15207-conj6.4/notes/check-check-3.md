# Check Report — `guo-2310.15207-conj6.4` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** `tools/.arxiv_cache/eprint/2310.15207v1.src` (`qLucas.tex`, Victor J. W. Guo, `arXiv:2310.15207v1`, Oct 23, 2023): Section 6 (`Open problems and concluding remarks`), lines 748–760 (`\label{conj:3}`, `\label{conj:4}`), and Section 2 lines 277–283 (`\label{lem:3}`, `\label{eq:lem3}`).
- **`TARGET.md` check:** Every quantifier ($n \equiv 1 \pmod 4$, $n > 1$, positive integers $r > s$), $q$-shifted factorial convention $(a;q)_m$, modulus $\Phi_{n^s}(q)^2$, Conjecture 6.4 (`\label{conj:4}`), Conjecture 6.3 (`\label{conj:3}`), and Lemma 2.3 (`\label{lem:3}`) match `qLucas.tex` verbatim.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–124:
  - **Section 1 (Setup & Telescoping):** Linearization $1 - q^{a+KN} \equiv (1-q^a)(1 + K\frac{q^a}{1-q^a}z) \pmod{\Phi_N(q)^2}$ ($z = 1-q^N$, $z^2 \equiv 0$) and pairing identity $\frac{q^a}{1-q^a} + \frac{q^{N-a}}{1-q^{N-a}} \equiv -1 \pmod{\Phi_N(q)}$ ($1 \le a < N$) are exact. Coprimality + one-step invariance $T(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$ for all $r \ge s+1$ implies the full $r > s$ congruence.
  - **Section 2 (Conjecture 6.4):** Verified coprimality of $R_4(n,s;q)$ to $\Phi_N(q)$ (Step 2.1), exact cancellation of $n$-multiples in $T_4(n,r;q)$ (Step 2.2, Eq. (3)), block decomposition & $\Delta Q_4(a)$ sign alternation (Step 2.3, Eq. (4)), and pairing cancellation modulo $\Phi_N(q)$ using $N \equiv N/n \equiv 1 \pmod 4$ (Step 2.4).
  - **Section 3 (Conjecture 6.3):** Verified coprimality of $R_3(n,s;q)$ to $\Phi_N(q)$ for both $s=1$ ($[n]$ cancels $1-q^n$ in $(q^5;q^4)$) and $s \ge 2$ ($1-q^N$ cancels between $(q^{5n};q^{4n})$ and $(q^5;q^4)$) (Step 3.1), exact $n$-multiple cancellation in $T_3(n,r;q)$ (Step 3.2, Eq. (5)), and $\Delta Q_3(a) = \pm 2$ mod $4$ pairing cancellation (Step 3.3, Eq. (6)).

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/guo-2310.15207-conj6.4/notes/check-check-3.py) (exact `SymPy` `ZZ[q]` polynomial and cyclotomic arithmetic, `FLOAT_COUNT: 0`).
- Checks performed:
  1. Eq. (2) modulo $\Phi_N(q)$ for $N \in \{5, 9, 13, 25\}$ and all $1 \le a < N$.
  2. $\Delta Q_4(a)$ (Eq. 4), $\Delta Q_3(a)$ (Eq. 6), and pairing sum vanishing for $n \in \{5, 9, 13, 17, 21, 25\}$, $s \in \{1, 2\}$.
  3. Step 2.2 & 3.2 exact exponent-multiset cancellation for $(n,r) \in \{(5,2), (9,2), (13,2)\}$.
  4. Direct verification of Conjecture 6.4 and Conjecture 6.3 modulo $\Phi_{n^s}(q)^2$ (with exact $\Phi_{n^s}(q)$-coprimality check on reduced denominators) for $(n,r,s) \in \{(5,2,1), (5,3,1), (5,3,2), (9,2,1), (13,2,1)\}$ (covering prime, composite $n=9$, and higher $s=2$ modulus $\Phi_{25}(q)^2$).
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```
