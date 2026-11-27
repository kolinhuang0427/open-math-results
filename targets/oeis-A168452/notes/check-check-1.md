# Independent Check Report: `oeis-A168452`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against live OEIS A168452 (`https://oeis.org/search?q=id:A168452&fmt=text`, rev. 14, Nov 22 2024):
  - Offset `0,2`, name `Self-convolution of A005568, where A005568(n) is the product of two successive Catalan numbers C(n)*C(n+1).`
  - Mathar's Nov 22 2024 5-term recurrence in `TARGET.md` and `PROOF.md` matches the live OEIS record verbatim (`n >= 4`).

## 2. Proof & Independent Mechanical Verification
- Checked all steps of `PROOF.md`:
  - Step 1: exact ratio $b(n)/b(n-1) = 4(2n-1)(2n+1)/((n+1)(n+2))$ and ODE (1) $x^2(16x-1)B''(x) = -2 + 2(1-6x)B(x) + 4x(1-12x)B'(x)$.
  - Step 2: inductive differentiation of $y(x) = B(x)^2$ giving $D_k(x) y^{(k)} = M_k(x, B, B')$ for $k = 0 \dots 5$, exact divisibility $D_k \mid p_k$, and exact polynomial identity $\sum_{k=0}^5 q_k(x) M_k(x, B, B') = 72 - 1152x$ in $\mathbb{Z}[x, B, B']$.
  - Step 3: coefficient extraction at $[x^n]$ for $n \ge 4$ matching $C_0(n), \dots, C_4(n)$ identically in $\mathbb{Z}[n]$.
- Wrote independent exact-arithmetic verifier `targets/oeis-A168452/notes/check-check-1.py` (`sympy` + exact Python `int`, zero floats, without reading `verify.py` or notes).
- Command: `.venv/bin/python targets/oeis-A168452/notes/check-check-1.py`
- Results (`PASS`):
  - Verified Step 1 ODE identity, Step 2 inductive relations $M_0 \to M_1 \to \dots \to M_5$ in $\mathbb{Z}[x, B, B']$, $D_k \mid p_k$, and $\sum_{k=0}^5 q_k M_k = 72 - 1152x$.
  - Verified Step 3 symbolic extraction in $\mathbb{Z}[n]$ matches $C_0(n), \dots, C_4(n)$ identically.
  - Verified all 21 OEIS `%S/%T/%U` terms (`a(0)..a(20)`) and Mathar's recurrence for $4 \le n \le 60$.

## 3. Gate 2 Novelty Status
- Gate 2 pending (`watch-1`/`watch-5`/`watch-6` pinged in #294).
