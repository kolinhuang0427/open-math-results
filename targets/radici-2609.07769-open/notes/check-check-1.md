# Gate 1 Verification Report (Pass 3 — Post-Audit Sync): `targets/radici-2609.07769-open`

- **Verdict:** **PASS**
- **Target:** `arXiv:2609.07769v2` (*A Note on Binary Quadratic Systems and Their Relation to Complexity Theory*, Gabriele Radici & Massimiliano Sala, Section 9 *Open problems* `main-v32.tex` `L1494–1566`, `L1498–1527`; Section 7 `thm:main` / `eq:main` `L1283–1292`)
- **Verifier script:** `targets/radici-2609.07769-open/notes/check-check-1.py` (exact `Fraction`, integer, and finite-field linear algebra only; `AST_FLOATS: []`, `FLOAT_CALLS: []`)

## Summary of Post-Audit Fixes Verified

1. **Section Numbers & Primary Source Path (`TARGET.md`, `PROOF.md`, `check-check-1.{py,md}`):**
   - Corrected compiled section citations to **Section 7** (`thm:main` / `eq:main`, `main-v32.tex` `L1283–1292`) and **Section 9** (*Open problems* `sec:open`, `main-v32.tex` `L1494–1566`, `L1498–1527`), and removed `/tmp/` paths from `TARGET.md` in favor of `tools/.arxiv_cache/eprint/2609.07769.src` (`main-v32.tex`).
2. **Lemma 5(2) Corrected `N^2` Prefactors (`PROOF.md` `L98`, `check-check-1.py`):**
   - Fixed $\frac{N}{q-1}\frac{f_q(1)}{q^D} = \kappa_q e^{\lambda_q}\frac{N(N-1)}{q^D} \le \frac{N^2 e^{q-1}}{q^D}$ (removing erroneous $/(q-1)$) and $\frac{N}{q-1} f_q^{(M)}(Y_{\max}) \le e^{(q-1)Y_{\max}}(q-1)^{M-1}((q-1)Y_{\max}+M)N^2$ (restoring the factor of $N^2$).
   - Verified Cases 2–6 under the true $N^2$ formulas: monotone bounds for Cases 2, 3 (`<= 0.173529`), 4 (`<= 0.165039`), 5 (`n >= 4`: `<= 0.047707`), 6 (`n >= 5`: `<= 0.014067`), and exact-coefficient $(\lambda_q, \kappa_q, c_4, c_5, \mathbb{E}[Y^6])$ bounds for Case 5 (`n=3`: `<= 0.181733 < 0.207906`) and Case 6 (`n=4`: `<= 0.057221 < 0.067115`).
3. **Lemma 3 $\sigma_2(P)$ Inequality (`PROOF.md` `L72, L74`):**
   - Replaced the false equality with $\sigma_2(P) \le \binom{N-5}{2}$ (justified immediately by $\mathcal{F}(P) \subseteq 2^{V \setminus L}$).
4. **Case 6 `q=5, d=2, n=3` (`PROOF.md` `L128`, `check-check-1.py`):**
   - Verified the `102,960` combinatorial upper bound (`7200 + 42480 + 3720 + 49560`, covering $|C \cap P| = 0, 1$ and $7$-circuits), `margin_coarse >= 0.041313` / `margin_shadow >= 0.050491`, and exact $5^6$-matrix MacWilliams tail `<= 0.039690` (`A_6 = 8,060,000`, `A_7 = 81,840,000`, dropping even $|P|=6$).

## Verification Output

- `.venv/bin/python -u targets/radici-2609.07769-open/notes/check-check-1.py` -> `PASS`, `EXIT:0`, `AST_FLOATS: []`, `FLOAT_CALLS: []`.
- Gate 2 receipts verified: `watch-1` (`#2137`), `watch-5` (`#2138`), `watch-6` (`#2139`).
