# Check Report: `targets/mirzavaziri-2610.19249-conj1/` (`@check-1`)

- **Verdict:** **PASS** (verifier re-checked after `#1166` fixes to Part B `L467`, `L833–834`, `L896`, `L962`)
- **Primary Sources:**
  - `tools/.arxiv_cache/eprint/2610.19249/gk74-2.tex` (`arXiv:2610.19249v1`, Section 1 Conjecture 1.1 `\label{conj:GK}` L64–70; Section 4 Theorem 4.3 `\label{thm:computation}` L259, Conjecture 4.4 `\label{conj:general}` L275–281, Conjecture 4.5 `\label{conj:almost}` L283–285; Section 5 Theorem 5.1 `\label{thm:asymptotic}` L293).
  - `tools/.arxiv_cache/eprint/1301.7651/onebino6.tex` (`arXiv:1301.7651v3`, Section 7 Conjecture 7.4 `\label{conj:330n88n}` L1210–1223).
- **Verifier Script:** `targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.py` (exact Python `int` + zero-float `mpmath.iv` at `dps = 30`, built directly from primary definitions and `PROOF.md` without reading `verify.py` or author `notes/`).

## 1. Primary Source & Statement Verification
- Mathematical statements of `conj:GK` (Conjecture 1.1), `conj:general` (Conjecture 4.4), `conj:almost` (Conjecture 4.5), and Guo–Krattenthaler Conjecture 7.4 (`conj:330n88n`) verified verbatim against `gk74-2.tex` and `onebino6.tex`.
- Self-contained proofs of Propositions 1–2 (cyclotomic polynomiality, reciprocity, partition injection on $0 \le t \le 5m$) and Lemmas 1–7 + Section 7 monotonicity (4th-order Edgeworth major arc, exact trigonometric splitting, Poisson summation, $L^1$-midpoint Fourier quadrature, unimodal layer-cake bound) verified line by line.

## 2. Independent Exact & Interval Verification
Ran `.venv/bin/python -u targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.py` (`AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`, `PASS`):
- **Part A (16s):** Exact `int` polynomial verification for all `57` admissible integers $m \in \{5\} \cup \{9 \le m \le 100 : m \not\equiv 2,3 \pmod 5\}$ (covering $1 \le n \le 20$ of Conjecture 1.1), including full-degree zero-remainder and reciprocity checks on $m \in \{5,9,10,11,14,15,20,25,30,35,100\}$ and Proposition 2 $d_k(n)$ checks ($k \in \{9,10,15,25\}, n \le 150$).
- **Part B (34s):** Independent `mpmath.iv` (`dps = 30`) certification across all $\gamma = \theta m \in (0, \infty)$ at $m_0 = 101$ (`L = 3`), with full $m \ge 101$ interval bounds on $\sin(a|\varphi|/2)\sin(b|\varphi|/2)$, exact boundary term on $v'$, $2\pi\sqrt{VW}$ factor in $I_C$, and upper $V_{\mathrm{hi}, m}$ in $I_{\mathrm{B2}}$:
  - `Lemma 1`: tail sum $\le 0.04941276 < 0.5$, $\tau/m \le 4.901257 < 5$, $s_{\min} \ge 17.17524$.
  - `Lemma 2` $L^1$ constants certified on $[0, 22]$ + exponential tail on $[22, \infty)$.
  - `Regime III` $[0, 0.5]$ (`8` blocks): $\min \mathrm{Net} \ge +0.77987$.
  - `Regime IIa` $[0.5, 3.7]$ (`32` blocks, Fourier quadrature + Lemma 6(2) complementary Poisson bound): $\min \mathrm{Net} \ge +0.4183219$.
  - `Regime IIb` $[3.7, 5.5]$ (`3` slices, Lemma 5/6(1) sharper of A/B1 + Lemma 6(2) far-arc): $\min \mathrm{Net} \ge +0.02184526$.
  - `Regime I` $[5.5, \infty)$: $\mathrm{Net} \ge +0.2767805$ ($\mathrm{Maj} \ge 0.5640574$, $\mathrm{Min} \le 0.2872769$).
  - Uniformly $\mathrm{Net} = 2\pi\sqrt{VW}\mathrm{Re} I \ge +0.02184526 > 0$ for all $m \ge 101$ and $5m < t \le T_m$.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.
