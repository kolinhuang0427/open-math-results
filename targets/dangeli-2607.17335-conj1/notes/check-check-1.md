# Check Report: `targets/dangeli-2607.17335-conj1/` (`@check-1`)

- **Verdict:** **PASS** (re-checked after `#1162` & `#1184` fixes to `COUNTEREXAMPLE.md` L92/L105/L125 and `notes/check-check-1.py`)
- **Primary Source:** `/tmp/eprint_2607_check/totally_main.tex` (extracted from `tools/.arxiv_cache/eprint/2607.17335v1.src`): Section 2 (L216–240), Section 4 (`\section{Totally simple graphs}`, L1355; Theorem 4.4 `\label{theo: lump=to simple}`, L1386; Conjecture 4.6 `\label{conj:typical-total-simplicity}`, L1457–1471; $k$-out model L1449).
- **Verifier Script:** `targets/dangeli-2607.17335-conj1/notes/check-check-1.py` (zero-float exact `int`/`Fraction`/SymPy + `mpmath.iv` `dps=30`, built directly from primary definitions without reading `verify.py` or author `notes/`).

## 1. Primary Source & Citation Verification
- `TARGET.md` and `COUNTEREXAMPLE.md` match `totally_main.tex` Section 4, Theorem 4.4 (`theo: lump=to simple`), and Conjecture 4.6 (`conj:typical-total-simplicity`) verbatim (`TARGET.md` has opening `---`, no remaining `Section 8` references).

## 2. Independent Verification Summary (`notes/check-check-1.py`)
Ran `.venv/bin/python -u targets/dangeli-2607.17335-conj1/notes/check-check-1.py` (`AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`, `PASS`):
- `PASS` Lemma 1 (twin-pair SCC examples `n = 3..6`), Section 2 ($T(m,k)$, $F(m,k,t)$ identities and brute-force $\mathrm{SCC}_n \subseteq \mathcal{E}_n$ for `n = 2..4`), Lemma 2 constants ($\lambda$, $\rho_\delta$, $2c_{\mathrm{loc}}$, $C_{\mathrm{up}} = 0.38$, $c_{\mathrm{low}} = 0.34$), exact $c_{\mathrm{scc}}(s, M)$ (`s = 1..4`).
- `PASS` All Case 1a, 1b (`s = 3..4` exact, `5..0.02n` RHS `< 7 \times 10^{-6} < 10^{-4}`, `0.02n..n/2` explicit $r=\lambda$ internally / $r_s$ externally tail `< 10^{-60}`), 2a, 2b (`0.02n..n/2` explicit `6500` ratio check `< 2 \times 10^{-10}` & `< 2 \times 10^{-40}`) bounds in `mpmath.iv` (`dps=30`), including symbolic derivative check for $R(\alpha, p)$ and uniform interval bounds on $f_{\mathrm{sink}}(\alpha) \le -0.05$, $f_{\mathrm{mid}}(p) \le -0.70$, $R(\alpha, p) \le -0.30$ on $(0, 1/2]\times[0,1]$ (with exact `2*(1-p)ln(1-p)` term), $R(\alpha, p) \le -0.60$ on $(0, 0.10]\times[0,1]$: grand failure probability sum $\le 0.6055 < 0.64$.
- `PASS` Section 5 first/second moments and overlaps ($|P_1 \cap P_2|=1$, disjoint $t=2,3$, main $t=4$): $\mathbb{E}_n[Z] \ge 0.20$, $\mathbb{E}_n[N^2] < 1.166 \le 1.20$, Paley–Zygmund bound $\ge 1/30$.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.
