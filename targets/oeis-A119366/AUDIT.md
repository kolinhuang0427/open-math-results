# Independent Blind Audit — `targets/oeis-A119366/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:27Z`
- **Verdict:** **PASS**

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against live OEIS **A119366** JSON (`https://oeis.org/search?q=id:A119366&fmt=json`, revision `7`, `2025-02-03T09:34:08-05:00`, offset `0,5`):
- **Name:** `Number of rooted planar n-trees whose number of leaves is equal to 1 modulo 3.`
- **Formula (`_Paul Barry_`, Jan 25 2007):** `a(0)=0, a(n)=sum{k=0..floor(n/3), (1/n)*C(n,3k+1)C(n,3k)},n>0;`
  - *(Agrees identically with the first OEIS formula `sum{k=0..n, if(mod(n-k,3)=1, (1/n)*C(n,k)*C(n,k+1), 0)}` via $j = n - k = 3r + 1$, matching Narayana leaf counts $\frac{1}{n}\binom{n}{j}\binom{n}{j-1}$.)*
- **Conjecture (`_R. J. Mathar_`, Feb 03 2025):**
  `Conjecture D-finite with recurrence +n*(881*n-4580)*(n-2)*(n+1)*a(n) -3*n*(612*n^3-2827*n^2-2988*n+10135)*a(n-1) +3*(-3088*n^4+42803*n^3-190361*n^2+313702*n-167988)*a(n-2) +(43042*n^4-600920*n^3+2924411*n^2-5860777*n+4115562)*a(n-3) +3*(-38600*n^4+558681*n^3-2904370*n^2+6389913*n-4965528)*a(n-4) +3*(-14776*n^4+162695*n^3-434711*n^2-415064*n+1878084)*a(n-5) -9*(n-6)*(10835*n^3-106831*n^2+290611*n-173519)*a(n-6) +54*(n-6)*(n-7)*(593*n-1429)*(2*n-13)*a(n-7)=0.`
- Every coefficient $C_0(n), \dots, C_7(n)$, offset `0`, quantifier $n \ge 7$ (all indices $n-7 \ge 0$), and $C_0(n) > 0$ for $n \ge 6$ in `TARGET.md` and `PROOF.md` match the live OEIS entry verbatim.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Step 1 — Roots-of-unity trisection & Lagrange inversion (lines 16–55):**
   - For $n \ge 1$, setting $m = 3k + 1$ with $\binom{n}{3k} = \binom{n}{n+1-m}$ and $\binom{n}{n+1} = 0$, the cube-root-of-unity filter $\frac{1}{3}\sum_{j=0}^2 \omega^{j(m-1)}$ yields $\sum_{k=0}^{\lfloor n/3 \rfloor} \binom{n}{3k+1}\binom{n}{3k} = \frac{1}{3}\sum_{j=0}^2 \omega^{-j} [t^{n+1}]((1+t)(1+\omega^j t))^n$.
   - Substituting $t = 1/u$ with $P_j(u) = (u+1)(u+\omega^j) = \omega^j + (1+\omega^j)u + u^2$ gives $[t^{n+1}]((1+t)(1+\omega^j t))^n = [u^{n-1}] P_j(u)^n$.
   - Since $P_j(0) = \omega^j \neq 0$, Lagrange inversion yields unique $u_j(x) \in x\mathbb{Q}[\omega][[x]]$ with $u_j(x) = x P_j(u_j(x))$ and $y(x) = \frac{1}{3}(u_0(x) + \omega^2 u_1(x) + \omega u_2(x))$ (including $[x^0] = 0 = a(0)$).
   - Completing the square gives $(2x u_j + x(1+\omega^j) - 1)^2 = \Delta_j(x)$ with hand-verified discriminants $\Delta_0(x) = 1 - 4x$, $\Delta_1(x) = 1 + 2\omega^2 x - 3\omega x^2$, and $\Delta_2(x) = 1 + 2\omega x - 3\omega^2 x^2$.
   - Taking the unique square root $S_j(x) \in 1 + x\mathbb{Q}[\omega][[x]]$ matches the $-1 \pmod x$ constant term: $2x u_j(x) = 1 - x(1+\omega^j) - S_j(x)$. Summing $\frac{1}{6x}\omega^{-j}$ over $j \in \{0, 1, 2\}$ (using $1+\omega+\omega^2 = 0$ and $2 + \omega^2(1+\omega) + \omega(1+\omega^2) = 2 - \omega - \omega^2 = 3$) gives eq. (1): $y(x) = -\frac{1}{2} - \frac{1}{6}(S_0/x + \omega^2 S_1/x + \omega S_2/x)$ in $\mathbb{Q}[\omega]((x))$. Airtight.
2. **Step 2 — Order-4 linear ODE for $y(x)$ (lines 57–86):**
   - Hand-checked the inductive numerator recurrence $N_0 = 1$, $N_{k+1} = 2x D N_k' - (2(k+1)D + (2k-1)x D')N_k$ for $2^k x^{k+1} D^k (S/x)^{(k)} = N_k S$ ($k = 0, 1, 2, 3, 4$) using $2 D S' = D' S$: exact.
   - Clearing $16 x^5 D^4$ yields $16 x^5 D^4 L(f) = S \sum_{k=0}^4 p_k N_k (2x D)^{4-k}$: exponents match identically.
   - Exact univariate polynomial annihilation $\sum_{k=0}^4 p_k N_k (2x D)^{4-k} = 0$ holds identically in $\mathbb{Z}[x]$ for $D = \Delta_0$ and in $\mathbb{Z}[\omega][x]$ for $D = \Delta_1$, hence also for $D = \Delta_2$ via the Galois automorphism $\omega \mapsto \omega^2$ (since $p_0, \dots, p_4 \in \mathbb{Z}[x]$). Since $16 x^5 \Delta_j^4 S_j \neq 0$ in the field $\mathbb{Q}[\omega]((x))$, $L(S_j/x) = 0$ for $j = 0, 1, 2$.
   - By $\mathbb{Q}[\omega]$-linearity applied to (1), $L(y(x)) = L(-1/2) = -\frac{1}{2}p_0(x) \in \mathbb{Z}[x]$ (since $12 \mid p_0$). Airtight.
3. **Step 3 — Coefficient extraction for $n \ge 7$ (lines 88–100):**
   - Checked exact degree intervals across $p_0, \dots, p_4$: $0 \le d - k \le 7$ throughout, so $m = n - (d - k) \ge 0$ for all $n \ge 7$. When $0 \le m < k$ (so $n - d < 0$), the falling product $\prod_{i=0}^{k-1}(m - i)$ vanishes identically, matching $[x^n](c x^d y^{(k)}(x)) = 0$.
   - Since $\deg(-\frac{1}{2}p_0) = 5 < 7$, $[x^n](-\frac{1}{2}p_0(x)) = 0$ for all $n \ge 7$. Extracted coefficients in $\mathbb{Z}[n]$ match $C_0(n), \dots, C_7(n)$ identically. Airtight.

---

## 3. Independent Verification & Gate 2 Novelty Check

- **Independent Checker Re-run (`notes/check-check-3.py`):**
  - Command: `.venv/bin/python targets/oeis-A119366/notes/check-check-3.py`
  - Exit code: `0`
  - Raw output:
    ```text
    [1/4] Barry formula matches all 27 live OEIS A119366 terms.
    [2/4] Step 1 roots-of-unity trisection and Delta_j identities verified up to x^40.
    [3/4] Step 2 exact polynomial annihilator (Delta_0, Delta_1) and order-4 ODE verified.
    [4/4] Step 3 symbolic Z[n] coefficient match and recurrence verified for 7 <= n <= 120.
    PASS
    ```
  - Pure exact `int` / $\mathbb{Z}[\omega]$ / SymPy polynomial arithmetic (zero floats); every coefficient of $p_0, \dots, p_4$ and $C_0, \dots, C_7$ in `check-check-3.py` verified to match `PROOF.md` and `TARGET.md`.
- **Gate 2 Novelty Receipts:** Verified all three receipts (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`) — all **PASS**.

---

## 4. Verdict & Handoff

**PASS** (label: `"written proof, internally audited"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.
