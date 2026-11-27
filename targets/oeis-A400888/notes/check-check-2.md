# Independent Check Report: `targets/oeis-A400888/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary sources checked:**
  - Live **OEIS `A400888`** JSON (revision 16, `2026-10-15T16:25:59-04:00`, fetched directly via `https://oeis.org/search?q=id:A400888&fmt=json`): name, 96 `DATA` terms (`2,2,1,2,2,...,1`), `COMMENT` (definition of $V(n)$, Stern vector $(p_n, q_n)$, $a(n) = \max\{m \ge 1 : u_n \equiv (0,0)^T \pmod m\}$, and surjectivity conjecture), `FORMULA` ($a(n) = \gcd(p_n - e_n, q_n + f_n)$, $a(4^j(n+1)-1) = a(n)$), and `PROGRAM` (PARI/GP `w(n)` and `a(n)`).
  - Live **OEIS `A000361`** JSON (revision 53, Oct 21, 2026, fetched via `https://oeis.org/search?q=id:A000361&fmt=json`): modular `fusc` formula $v_j = (((j p_0 - 1) \bmod q_0) + 1 - p_0) \bmod 2$.
- **Comparison with `TARGET.md` and `PROOF.md`:**
  - `TARGET.md` and `PROOF.md` match OEIS `A400888` (rev 16) and `A000361` (rev 53) verbatim with zero quantifier or domain drift.
  - Every step of `PROOF.md` (Lemmas 1–6 and Main Theorem) is verified complete and gap-free:
    - Lemma 1: $V(4n+3) = V(n)$ and exact column word $V(n(r,t)) = (0^r 1^r)^{t-1} 0^r 1^{r-1}$ from both the PARI recurrence $w(n)$ and the `A000361` modular formula ($n(r,t) = 2^{2t+r-1} - 2^{r-1} - 2$, $r \ge 2, t \ge 1$).
    - Lemma 2: exact matrix evaluation $a(n(r,t)) = r \gcd(X_t, Z_t)$, quadratic-form invariant $Q(x_t, y_t) = -r$, and Bézout identity forcing $\gcd(X_t, Z_t) \mid t((t-1)r - 2)$.
    - Lemma 3: exact witnesses for $r=1$ ($n=2$), even $r \ge 2$ ($t=1$), odd $r \not\equiv 2 \pmod 5$ ($t=2$), and odd $r \equiv 2 \pmod 5, 3 \nmid r$ ($t=3$).
    - Lemmas 4–6: parity $2 \nmid X_t$ for odd $r, t \equiv 2 \pmod 3$; algebraic norm bound $C_m(r) < 0$ ($m \in \{3r+8, 3r\}$) ruling out $p \mid \gcd(X_t, Z_t)$ for primes $p > P_0(r)$ with $(t-1)r - 2 = 2p$; order $d_q = \mathrm{ord}_{\mathbb{F}_{q^2}^\times}(\bar{\alpha}^2)$ giving $q \mid F_{2d_q}$ and $qd_q \mid t$; convergent tail $S(Y) \to 0$; and CRT + PNT in AP + Montgomery–Vaughan Brun–Titchmarsh yielding infinitely many $t$ with $\gcd(X_t, Z_t) = 1$ for every odd $r \ge 3$ divisible by $3$.

## 2. Independent Mechanical Check

Written independently from live OEIS `A400888` & `A000361` JSON and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/oeis-A400888/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/oeis-A400888/notes/check-check-2.py
  ```
- **Raw output (exit code 0):**
  ```text
  OEIS A400888 rev 16 (96 DATA terms == PARI w(n) == A000361) & Lemma 1: PASS
  Lemmas 2 & 3 (matrix eval, quadratic form, Bezout, r=1..100 != 27 mod 30): PASS
  Lemmas 4, 5 & 6 (parity, C_m(r) norm bound, d_q order, >=5 exact prime witnesses for r<=147): PASS
  PASS (all checks passed in 0.058s)
  ```

## 3. Gate 2 & Contest Status

- **Gate 2 receipts present:** `notes/novelty-gate2-watch-2.md`, `notes/novelty-gate2-watch-5.md` (both PASS).
- **Contested status:** No `CONTESTED.md` present.
