# Independent Check Report: `campbell-2509.16034-conj1` (`check-1`, Re-Confirmed Post-Rescope)

- **Checked at (UTC):** `2026-11-27T01:24:05Z` (supersedes prior check `2026-11-26T23:52:27Z`)
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity for rescoped Open Problems `(c1)` and `(c2)`, prior-art crediting per `notes/contest-ruling-audit-3.md`, and independent exact verification of Lemma 1, Theorem 1, $8$-state $2$-kernel closure, and Theorem 2)

## 1. Primary-Source Fidelity Check (Post-Rescope)

- **Primary source:** `arXiv:2509.16034v1` (`tools/.arxiv_cache/eprint/2509.16034/ReducedComplexityV85.tex`, *INTEGERS* 26 (2026), #A34; sole arXiv version):
  - Section 1 definitions (lines 75–113): $\mathrm{red}(w)$, $\rho_{\mathbf{x}}^{\mathrm{ab},\mathrm{red}}(n)$, and 1-indexed Thue–Morse $\mathbf{t}_n = s_2(n-1) \bmod 2$.
  - Section 2.1 (lines 180–348): Theorem 1 (`\ref{tm_red}`, including $\rho_{\mathbf{t}}^{\mathrm{red}}(n) = 2(M_n - m_n + 1)$ and its $2$-regularity), Lemma 2 (`\ref{tm_max_min}`, $n \ge 2$), and Lemma 3 (`\ref{tm_mod4}`, $n \ge 1$).
  - Section 3 Conclusion (lines 675–699): Open Problems `(c1)` (explicit sign of $\rho(4n+2) - \rho(4n)$ in the nonzero case, lines 691–694) and `(c2)` (explicit recursion for $\rho(4n)$ and full recursion for $\rho(n)$, lines 680–682, 695–696).
- **Rescope check against `notes/contest-ruling-audit-3.md`:**
  - `TARGET.md` and `PROOF.md` now claim **strictly** `(c1)` and `(c2)` (plus $2$-regularity of $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$) and explicitly credit `the-omega-institute/trureturing` (Sept 2026, commits `832f82f782` & `96baee8682`) for prior settlement of the odd recurrence, eq. (11) `displayconjecture`, and non-$k$-automaticity. Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from `ReducedComplexityV85.tex` definitions and `PROOF.md`, without reading `verify.py` or author scratch `notes/`.
- **Verifier script:** `targets/campbell-2509.16034-conj1/notes/check-check-1.py` (exact integer and rational `Fraction` arithmetic plus direct factor enumeration).
- **Verified claims:**
  1. **Direct factor enumeration ($1 \le n \le 120$):** Built Thue–Morse prefix of length $4096$, directly enumerated $\mathrm{red}(w)$ abelian equivalence classes and $[m_n, M_n]$, matched `(numericalproblem)` prefix `(2, 3, 3, 4, 3, 5, 4, 5, 3, 4, 5, 6, 4, 6, 5, 4, 3, 5, 4)`, verified Lemma 2/3 ($1 \le n \le 4999$) and Lemma 1 closed form ($1 \le n \le 20{,}000$).
  2. **Theorem 1 (`(c2)` explicit recursion & $2$-regularity):** Verified $\rho(2n+1)=\rho(n+1)$ ($0 \le n \le 9999$), $\rho(4n)$ and $\rho(4n+2)$ ($1 \le n \le 4999$), $(a_k, b_k)$ mod-2 recurrences ($j \ge 2$), exact $8$-state $2$-kernel closure of $(a'_k, b'_k) = (a_{k+1}, b_{k+1})$ for all $k \ge 0$, and exact linear combination $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n) = \frac{3}{4}\rho_{\mathbf{t}}^{\mathrm{red}}(n) + \frac{(-1)^{m_n} + (-1)^{M_n}}{4}$ ($1 \le n \le 20{,}000$).
  3. **Theorem 2 (`(c1)` exact sign formula):** Verified $\rho(4n+2)-\rho(4n) = b_{n+1}-a_{n+1} = \frac{(-1)^{m_{n+1}}-(-1)^{M_{n+1}}}{2}$ and nonzero sign formula $2b_{n+1}-1 = (-1)^{1-b_{n+1}}$ for all $1 \le n \le 4999$.

### Command & Raw Output

```bash
.venv/bin/python -u targets/campbell-2509.16034-conj1/notes/check-check-1.py
```

```text
Direct factor enumeration (1<=n<=120), paper prefix (1..19), Lemma 2/3, & Theorem 1 (1<=n<=20000): OK
2-kernel sizes: alpha=9, beta=10, alpha_{k+1}=8, beta_{k+1}=8
Rescoped Theorem 1 (odd/4n/4n+2 recurrences, 8-state 2-kernel, 2-regularity, unboundedness): OK
Rescoped Theorem 2 (exact sign, nonzero formula 2b_{n+1}-1, strong induction 1<=n<=4999): OK
PASS
```
