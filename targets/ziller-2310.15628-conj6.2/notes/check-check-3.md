# Independent Check Report: targets/ziller-2310.15628-conj6.2/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2310.15628v2` (`2026-04-15T17:18:47Z`, latest version of 2), *"Orders and partitions of integers induced by arithmetic functions"* by Mario Ziller, cached TeX files `tools/.arxiv_cache/eprint/2310.15628/Ziller_2023_v2.tex`, `Examples.tex`, and `Conclusions.tex`.
- **Exact definitions & conjecture match:**
  - `Ziller_2023_v2.tex` lines 28–30 (`\newtheorem{defi}{Definition}[section]`, `\newtheorem{conj}[defi]{Conjecture}`) and line 116 ($\mathbb{N}$ denotes the positive integers $\{1, 2, 3, \dots\}$).
  - `Examples.tex` line 296: $\varphi(x) = |\{k \in \mathbb{N} \le x : k \perp x\}| = x \prod_{p \mid x} (1 - \frac{1}{p})$.
  - `Conclusions.tex` lines 2–4 (`\stepcounter{section}`, Section 6 *"Concluding remarks"*) and lines 89–91 (**Conjecture 6.2**):
    > All function values of ${\displaystyle\frac{\varphi(x)}{x^2}}$ for $x\in\mathbb{N}$ are pairwise distinct.
  - Line 98 of `Conclusions.tex` explicitly notes the equivalence for the reciprocal $x^2/\varphi(x)$.
- **Fidelity:** `TARGET.md` and `PROOF.md` match `arXiv:2310.15628v2` verbatim with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical & Mathematical Check

- Independently wrote `targets/ziller-2310.15628-conj6.2/notes/check-check-3.py` (strictly without reading `verify.py`), verifying using exact integer and `fractions.Fraction` arithmetic:
  1. **Direct injectivity:** Sieved $\varphi(x)$ for $1 \le x \le 200{,}000$ and confirmed all $200{,}000$ reduced rational fractions $\varphi(x)/x^2$ are pairwise distinct.
  2. **Proof formulas (`1 <= n <= 10,000`):** Verified $\varphi(n)/n^2 = \prod_{q \mid n} \frac{q-1}{q^{e_q+1}}$, $v_p(\varphi(n)/n^2) = -(e_p + 1)$ for the largest prime $p \mid n$, and $v_r(\varphi(n)/n^2) = 0$ for primes $r > p$.
  3. **Minimal-counterexample descent (`2 <= x < y <= 200`):** Verified $v_p(f(x)) \neq v_p(f(y))$ whenever $v_p(x) \neq v_p(y)$ at $p = \max\{q \text{ prime} : q \mid xy\}$, and verified exact multiplicative cancellation $f(p^e x_0) = f(p^e) f(x_0)$ with $x_0 y_0 < xy$ whenever $v_p(x) = v_p(y) = e \ge 1$.

- **Command run:**
```bash
.venv/bin/python -u targets/ziller-2310.15628-conj6.2/notes/check-check-3.py
```

- **Raw output:**
```text
Injectivity PASS: all 200000 reduced fractions phi(x)/x^2 (1 <= x <= 200000) are pairwise distinct.
Proof Lemma & Descent PASS: product formula, v_p(f(n)) == -(e+1), and p^e-descent verified.
PASS
```
