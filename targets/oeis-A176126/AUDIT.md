# Adversarial Audit Report (`audit-1`): `targets/oeis-A176126/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A176126` (rev. 18, Aug 27 2022) — R. J. Mathar's Dec 12, 2010 generating function $\frac{(x^4-x^3+3x^2-x+1)(x^4-x^3-2x^2-x+1)}{(x-1)^3(x^2+1)^3}$ and 9-term linear recurrence ($n \ge 9$) for the numerator of $-A127276(n)/A001788(n)$
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, live OEIS `A176126` rev. 18, `A127276` rev. 33, `A127275` rev. 18, and `A001788` rev. 270 (`fmt=text`), `watch/snapshots/**`
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A176126` (`#18 Aug 27 2022 03:13:41`):**
  - `%O`: `0,4`; all 80 `DATA` terms ($n = 0..79$) match `notes/check-check-1.py` verbatim.
  - `%N`: `Numerator of -A127276(n)/A001788(n).`, `%C` initial fraction sequence (`-1/0, -1/1, 1/3, ...`), and Mathar's Dec 12, 2010 `%F` `Conjecture:` match `TARGET.md` and `PROOF.md` verbatim.
- **Auxiliary live OEIS definitions verified verbatim:** `A127276` (`#33`), `A127275` (`#18`), and `A001788` (`#270`, `a(n) = n*(n+1)*2^(n-2)`, `a(0) = 0`).
- **Snapshot cross-check & Gate 2:** `0` snapshot hits across `watch/snapshots/**`; Gate 2 PASS receipts from `watch-1` (`#1146`) and `watch-5` (`#1144`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Section 1 (Self-contained Lemma 1: $A127276(n) = 2^n - n(n+1)2^{n-2}$, L17–32):**
  - Rank-2 perturbation $M_n = C_n - \frac{1}{4}vv^T + \frac{1}{4}e_0e_0^T$, monic Laurent–Chebyshev polynomials $P_k(t(z)) = z^k + z^{-k}$, diagonalization $P C_n P^T = \mathrm{diag}(1,2,\dots,2)$, quadratic forms $v^T C_n^{-1} v = e_0^T C_n^{-1} e_0 = 2n+1$, $v^T C_n^{-1} e_0 = (-1)^n$, and Weinstein–Aronszajn determinant yield $A127276(n) = 2^n - n(n+1)2^{n-2}$ unconditionally for all $n \ge 0$.
- **Section 2 (Mod-4 reduced numerator, L36–46):**
  - At $n = 0$: $-1/0 \implies a(0) = -1 = \frac{0\cdot 1 - 4}{4}$.
  - For $n \ge 1$: $A001788(n) = n(n+1)2^{n-2} > 0$ gives $-\frac{A127276(n)}{A001788(n)} = \frac{n(n+1)-4}{n(n+1)}$ with $\gcd(n(n+1)-4, n(n+1)) = \gcd(n(n+1), 4) = 4$ if $n \equiv 0, 3 \pmod 4$ and $2$ if $n \equiv 1, 2 \pmod 4$. Dividing by the gcd preserves positive denominators and yields $a(n) = \frac{n(n+1)-4}{4}$ ($n \equiv 0, 3 \pmod 4$) and $\frac{n(n+1)-4}{2}$ ($n \equiv 1, 2 \pmod 4$) for all $n \ge 0$ (including $a(1) = -1$).
- **Section 3 (Generating function & 9-term recurrence, L50–69):**
  - Each residue class $a(4m+r)$ ($r \in \{0,1,2,3\}$) is quadratic in $m \ge 0$, so $(1-x^4)^3 A(x) = P(x) \in \mathbb{Z}[x]$ has degree $\le 11$, determined explicitly from $a(0..11)$.
  - Exact polynomial identity $P(x) = -(1+x)^3 N(x)$ and $(1-x^4)^3 = -(x-1)^3(x+1)^3(x^2+1)^3$; cancelling the unit $-(1+x)^3 \in \mathbb{Z}[[x]]^\times$ yields $A(x) = N(x)/((x-1)^3(x^2+1)^3)$.
  - Expanding $D(x) = (x-1)^3(x^2+1)^3$ and extracting $[x^n]$ ($n \ge 9 > \deg N = 8$) establishes Mathar's 9-term recurrence for all $n \ge 9$.

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A176126/notes/check-check-1.py`:
- Exit code `0`, output `PASS` (zero floats; exact `int`, `Fraction`, and SymPy arithmetic).
- Verified Lemma 1 ($n = 0..8$), exact `Fraction` reductions matching all 80 live OEIS `A176126` terms and all 12 `%C` fractions, all polynomial identities, formal convolution $D(x)A(x) = N(x)$ through $x^{150}$, and Mathar's 9-term recurrence for $9 \le n \le 150$.
