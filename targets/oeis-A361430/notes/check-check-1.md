# Check Report: `targets/oeis-A361430/` (`@check-1`)

- **Verdict:** **PASS**
- **Primary Source:** Live OEIS records `A361430` (rev. 41, Jul 05 2026), `A298826` (rev. 125, Jun 10 2025), `A298825` (rev. 29), `A298674` (rev. 38), `A306653`.
- **Verifier Script:** `targets/oeis-A361430/notes/check-check-1.py` (pure exact Python `int`, zero floats, built directly from OEIS primary definitions without reading `verify.py` or author `notes/`).

## 1. Primary Source & Statement Verification
- Checked `TARGET.md` and `PROOF.md` against live OEIS (`fmt=text`):
  - `A361430` (`%N` multiplicative $a(p^e) = e - 1$, `%F` Conjecture `a(n) = abs(A298826(n))`, `%S` $n=1..87$) matches verbatim.
  - `A298826` (`%N` $A298825(n)/n$, `%F` Oudra's Nov 19 2019 conjecture, Kotesovec's Mar 12 2023 conjecture, Schulte's Jun 09 2025 conjecture, `%S` $n=1..108$) matches verbatim.
  - Primary matrix definition (`A298674` / `A298824` / `A298825` / `A298826`) $T(u,v) = \sum_{d \mid \gcd(u,v)} \mu(d)d$ and $c(n) = \frac{1}{n}\sum_{m=1}^n \sum_{k \mid n} T(n/k,m) T(k,m+2)$ verified.

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python -u targets/oeis-A361430/notes/check-check-1.py` (exit code `0`, `PASS`):
- Primary matrix definition matches OEIS `A298826` `%S` ($n = 1..108$) and `A361430` `%S` ($n = 1..87$) identically, and verifies $n = 1..150$.
- CRT convolution $c = \tau * b$ verified against `A306653` `%S` ($n = 1..28$) and coprime multiplicativity of $b$ ($u, v \le 34, uv \le 300$).
- Schulte's formula $c(p^e) = (-1)^p(e-1)$, Kotesovec's $|c(n)| = \mathrm{A361430}(n)$, and Oudra's formula $(-1)^{n+1}\sum_{d \mid n}\mu(d)\tau(d)\tau(n/d)$ verified against primary $c(n)$ for $n = 1..150$, mutually for $n = 1..2000$, and for prime powers $b(p^e)$ ($p \in \{2,3,5,7,11,13\}$, $e \le 11$).

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.
