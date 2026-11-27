# Independent Check Report: `dawsey-2107.14284-conj5.1`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2107.14284v2/main.tex` (`arXiv:2107.14284v2`, Section 5, `Conjecture 5.1`, lines 1083–1086; definitions at lines 113, 126, 1053).
- `TARGET.md` and `PROOF.md` match the primary source verbatim: $\mathbb{N} = \{1, 2, \dots\}$, $\mathbb{P} = \{p_1 < p_2 < \cdots\}$, $\mathrm{idx}(p_k) = k$, $f \colon \mathbb{N} \to \mathbb{C}$, $L_f = \lim_{N \to \infty} \frac{1}{N} \sum_{k=1}^N f(k)$, and the limit $\lim_{s \to 1^+} \frac{\sum_{p \in \mathbb{P}} f(\mathrm{idx}(p)) p^{-s}}{\sum_{p \in \mathbb{P}} p^{-s}} = L_f$ (with the ordered Dirichlet series $\lim_{M \to \infty} \sum_{k=1}^M f(k) p_k^{-s}$ explicitly proved to converge for all real $s > 1$, which accommodates unbounded $f$ whose Cesàro mean exists).

## 2. Proof & Independent Mechanical Verification
- Checked all analytic steps in `PROOF.md`:
  - Summation by parts (Step 1) handles $N = 1$ with $S_0 = 0$, $p_M \ge M$, $|S_M| \le CM \implies |S_M p_M^{-s}| \le C M^{1-s} \to 0$ for $s > 1$, and $\sum_{k=1}^\infty |S_k|(p_k^{-s} - p_{k+1}^{-s}) \le C P(s) < \infty$.
  - Step 2 identity and error bound $\le \frac{C_K}{P(s)} + \frac{\eta}{2}$ hold for all $s > 1$ (since $0 < p_k^{-s} - p_{k+1}^{-s} < p_k^{-s} < p_k^{-1}$ for $k \ge 1, s > 1$), and $P(s) \to +\infty$ as $s \to 1^+$ by Euler's theorem $\sum p_k^{-1} = \infty$.
- Wrote independent exact-arithmetic verifier `targets/dawsey-2107.14284-conj5.1/notes/check-check-1.py` (exact `int` / `Fraction` / integer root enclosures, zero floating point, without reading `verify.py` or author notes).
- Command: `.venv/bin/python targets/dawsey-2107.14284-conj5.1/notes/check-check-1.py`
- Results (`PASS`):
  - Checked $p_k \ge k$ for first $1200$ primes ($p_1 = 2, \dots, p_{1200} = 9733$).
  - Verified Step 1 summation-by-parts identity, telescoping bound, and Step 2 Abel-difference identity in exact $\mathbb{Q}[i]$ arithmetic at $s = 2, 3$ across 4 test functions: $f(k) = (-1)^k$, complex periodic $i^k + (2 - 3i)$, unbounded square-supported $f(m^2) = m$, and unbounded oscillating $S_k = (-1)^k \lfloor\sqrt{k}\rfloor$.
  - Verified exact rational root enclosures for $p_k^{-101/100}$ ($k = 1 \dots 1000$): $P(101/100) > 2.3826 > 2.1$, Step 2 proved error bound $< 0.6271 < 2/3$, and direct Abel-bounded ratio $\le 0.112678 < 2/3$.

## 3. Gate 2 Novelty Status
- Gate 2 passed (`notes/novelty-gate2-watch-1.md` and `notes/novelty-gate2-watch-4.md`). Ready for blind audit.
