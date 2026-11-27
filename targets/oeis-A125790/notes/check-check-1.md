# Check Report — `oeis-A125790`

- Checker: `check-1`
- Checked UTC: `2026-11-27T03:48:53Z` (re-check after `PROOF.md` L21 fix)
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source: live OEIS JSON `https://oeis.org/search?q=id:A125790&fmt=json` (revision `47`, `2026-03-22T15:37:03-04:00`):
  - Definition: `T(n,k) = T(n,k-1) + T(n-1,2*k) for n>0, k>0, with T(0,n)=T(n,0)=1 for n>=0.`
  - Conjecture (`_Mikhail Kurkov_`, May 03 2025): `Conjecture: g.f. for n-th row is (Sum_{i=0..n-1} x^i Sum_{j=0..i} binomial(n+1,j)*T(n,i-j)*(-1)^j)/(1-x)^(n+1) for n > 0.`
- Comparison against `TARGET.md` and `PROOF.md` (updated L21): exact match with zero quantifier, hypothesis, edge-case, or definition drift. `PROOF.md` Step 1 L21 now correctly states $\nabla: V_n \to W_{n-1}$ between $n$-dimensional spaces with trivial kernel is an isomorphism.

## 2. Independent Mechanical Verification

- Verifier script: `targets/oeis-A125790/notes/check-check-1.py` (written strictly from live OEIS `A125790` and `PROOF.md`, without reading `verify.py`).
- Verified directly in exact integer and rational/SymPy arithmetic:
  1. OEIS recurrence matches all example rows `0 <= n <= 8`.
  2. Step 1 isomorphism $\nabla: V_n \to W_{n-1}$ ($\dim = n$, $\det \neq 0$) and unique polynomial $P_n(t) \in \mathbb{Q}[t]$ ($\deg P_n \le n$, $P_n(0)=1$, $P_n(-1)=0$) matching $T(n, k)$ for $0 \le k \le 40$ and $1 \le n \le 10$, with vanishing $(n+1)$-th backward differences for $n \le i \le 25$.
  3. Kurkov's conjectured row generating function expanded to $x^{40}$ matches $T(n, 0..40)$ for all $1 \le n \le 10$.

### Command & Raw Output

```bash
.venv/bin/python -u targets/oeis-A125790/notes/check-check-1.py
```

Raw output (exit code `0`):
```text
OEIS table (0<=n<=8), Step 1 P_n(t) & P_n(-1)=0, and backward differences (1<=n<=10): OK
Kurkov row GF verified against T(n, 0..40) for all 1 <= n <= 10: OK
Step 1 isomorphism nabla: V_n -> W_{n-1} (dim n, det != 0 for 1<=n<=10): OK
PASS
```
