# Independent Check Report: `targets/oeis-A208425/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary sources checked:**
  - Live **OEIS `A208425`** JSON (revision 60, `2025-11-05T15:22:21-05:00`, fetched directly via `https://oeis.org/search?q=id:A208425&fmt=json`): name `"Expansion of Sum_{n>=0} (3*n)!/n!^3 * x^(2*n)/(1-x)^(3*n+1)."`, 24 `DATA` terms `1,1,7,25,151,...`, formula `a(n) = Sum_{k=0..n} C(n,k)*C(n-k,k)*C(n+k,k)`, and Zhi-Wei Sun's Nov 12, 2016 comment Conjecture (i) and (ii).
  - `google-deepmind/formal-conjectures` `FormalConjectures/OEIS/208425.lean` (SHA `6692a6604859e2615fd452aa1f41cade8b6f8dcc`, fetched via read-only `gh api`): `a`, `conjecture_1`, `conjecture_2`, `conjecture_3`.
- **Comparison with `TARGET.md` and `PROOF.md`:**
  - Both `TARGET.md` and `PROOF.md` match OEIS `A208425` (rev 60) and `208425.lean` (`conjecture_2`) verbatim, with zero quantifier or domain drift (all primes $p \equiv 1 \pmod 3$, i.e., $p = 6n + 1$, $n \ge 1$).
  - Every step of `PROOF.md` (Lemmas 1–5 and completion modulo $\Phi(X) = X^2 - X + 1$) is verified self-contained and gap-free:
    - Lemma 1: generating-function vs trinomial-sum equivalence, hockey-stick identity, $t_{2n} \equiv \binom{4n}{2n} \pmod{p^2}$ (using $2n$ even), reduction to $F(1) = 0$ in $\mathbb{F}_p$.
    - Lemma 2: harmonic congruence $H_n - H_{2n} \equiv H_{3n} \pmod p$, $[x^{p-1}]$ Laurent extraction, and $\sum_{k=0}^{p-1}\binom{2k}{k} \equiv 1 \pmod{p^2}$.
    - Lemma 3: exact $\Phi(X) \mid L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$ (monic divisor), $3$-orbit cancellation $\sum_{x \in \mathbb{F}_p} P(x)L(x) = 0$ via $\sigma(x) = 1/(1-x)$, and Wilson reduction giving Adamchuk's $\sum_{k=0}^{4n}\binom{2k}{k} \equiv 1 \pmod{p^2}$.
    - Lemma 4: $p$-integrality of $\tilde{Q}(X)$, $p Q_{4n+1}(1) \equiv \binom{4n}{2n} \pmod{p^2}$, degree bound $< 3p$, and exact polynomial identity $H(u(X)) \equiv (1 - 2X^p)\tilde{Q}(X) - \binom{4n}{2n} R(X) \pmod p$.
    - Lemma 5 & completion: exact rational telescoping in $\mathbb{Q}[X]$ and reduction modulo $\Phi(X)$ giving $\tilde{Q}(\zeta) = 0$, hence $3 F(1) = H(u(\zeta)) = 0$ in $\mathbb{F}_p$ ($p \ge 7 \implies F(1) = 0$).

## 2. Independent Mechanical Check

Written independently from live OEIS `A208425` JSON, `208425.lean`, and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/oeis-A208425/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/oeis-A208425/notes/check-check-2.py
  ```
- **Raw output (exit code 0):**
  ```text
  OEIS A208425 rev 60 definitions (GF == trinomial sum, all 24 live OEIS DATA terms): PASS
  Lemmas 1, 2, 3 (incl. full 3-orbit F_p check for p<=200, direct sum p<=250) on 45 primes p<500: PASS
  Lemmas 4 & 5 (exact Q[X] telescoping, F_p[X] ODE match, mod Phi(X) reduction) on [7, 13, 19, 31, 37, 43]: PASS
  Target conjecture_2 verified across all 80 primes p == 1 (mod 3), p < 1000: PASS
  PASS (all checks passed in 2.128s)
  ```

## 3. Gate 2 & Contest Status

- **Gate 2 receipts present:** `notes/novelty-gate2-watch-2.md`, `notes/novelty-gate2-watch-5.md` (both PASS).
- **Contested status:** No `CONTESTED.md` present.
