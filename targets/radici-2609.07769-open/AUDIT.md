# Adversarial Audit — `targets/radici-2609.07769-open` (`arXiv:2609.07769v2`)

- **Auditor:** `@audit-1` (independent blind audit)
- **Final Verdict:** **PASS** (Pass 2 re-audit after fixing all 3 blocking defects and both precision items from Pass 1)
- **Label:** `written proof, internally audited`
- **Primary source verified:** `tools/.arxiv_cache/eprint/2609.07769.src` (`main-v32.tex`, `arXiv:2609.07769v2`, `2026-11-25`)
  - Section 7 (`main-v32.tex` L1262, L1283–1292): `thm:main` / `eq:main` ($\alpha_1 > \alpha_0$ over $\mathbb{F}_2$)
  - Section 9 (`main-v32.tex` L1494–1566, esp. L1498–1527): *Open problems* (`sec:open`) for $q \in \{3, 4, 5\}$
- **Files audited:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py` (author `verify.py` and scratch notes not read)
- **Independent verification command:** `.venv/bin/python -u targets/radici-2609.07769-open/notes/check-check-1.py` → `PASS`, `EXIT: 0`, `AST_FLOATS: []`, `AST_FLOAT_CALLS: []`

---

## Resolution of Pass 1 Blocking Defects (All Verified Fixed)

1. **Compiled section numbers & cache path (`TARGET.md`, `PROOF.md`, `notes/check-check-1.md`):**
   - Verified fixed across `TARGET.md` (L2, L15, L17, L25, L33), `PROOF.md` (L1, L5), and `notes/check-check-1.md` (L4): `thm:main` / `eq:main` cited as **Section 7**, *Open problems* (`sec:open`) cited as **Section 9**, and `/tmp/` path replaced by `tools/.arxiv_cache/eprint/2609.07769.src` (`main-v32.tex`).
2. **Lemma 5(2) corrected $N^2$ prefactors (`PROOF.md` L98, Section 4, `notes/check-check-1.py` L554–614):**
   - Verified fixed: $\frac{N}{q-1}\frac{f_q(1)}{q^D} = \kappa_q e^{\lambda_q}\frac{N(N-1)}{q^D} \le \frac{N^2 e^{q-1}}{q^D}$ (erroneous $/(q-1)$ removed) and $\frac{N}{q-1} f_q^{(M)}(Y_{\max}) \le e^{(q-1)Y_{\max}} (q-1)^{M-1}((q-1)Y_{\max}+M) N^2$ (missing factor of $N$ restored).
   - Verified all Cases 2–6 numerical bounds independently and via `check-check-1.py` (exact `Fraction` arithmetic, zero floats):
     - Case 2 (`N_0 = 27, 64, 125`): `0.002498`, `0.181919`, `0.004285`, `0.002594`, `0.007692` (all `< s0_lb_monotone(N_0) <= 11/30`).
     - Case 3 ($q=3, d=2, n \ge 3$): `0.173529 < 0.366549`.
     - Case 4 ($q=5, d=3, n \ge 3$): `0.165039 <= 0.165050 < 0.366658 <= 0.368325`.
     - Case 5 ($q=4, d=2, n = 3$): exact-coefficient error `0.170160` (independent) / `0.181733` (`check-check-1.py`, dropping negative $P_5$ excess) `<= 0.195837 < 0.207604 <= 0.207906`; ($n \ge 4$): `0.047707 <= 0.047769 < 0.199945 <= 0.202129`.
     - Case 6 ($q=5, d=2, n = 3$): combinatorial bad-triple bound `102,960` (`7200 + 42480 + 3720 + 49560`, explicitly covering $|C \cap P| \in \{0,1\}$ and all $7$-circuits; independently verified exact average $\le 74{,}220 \le 102{,}960$), `margin_coarse >= 0.041313` / `margin_shadow >= 0.050491` vs exact $5^6$-matrix MacWilliams tail `<= 0.039690` (`A_6 = 8,060,000`, `A_7 = 81,840,000`, even $|P|=6$ dropped).
     - Case 6 ($q=5, d=2, n = 4$): exact-coefficient error `0.052397` (independent) `<= 0.053757` (`PROOF.md`) / `0.057221` (`check-check-1.py`) `< 0.067099 <= 0.067115`; ($n \ge 5$): `0.014067 <= 0.014082 < 0.081753`.
3. **Lemma 3 $\sigma_2(P)$ bound (`PROOF.md` L72, L74):**
   - Verified fixed to $\sigma_2(P) \le \binom{N-5}{2}$ (justified immediately by $\mathcal{F}(P) \subseteq 2^{V \setminus L}$), while $\sigma_1(P) = N - 5$ is independently confirmed exact.
4. **Non-blocking precision items (`PROOF.md` L37, L128):**
   - L37 corrected to note $\beta_4^{\mathrm{new}} = 0$ (no $5$-circuits at $q=5, d=2$; $\beta_4^{\mathrm{new}} \le \Lambda_5(n)$ looser and valid).
   - L128 explicitly accounts for both $|C \cap P| = 0$ ($T \subset L'$, $\le 744\binom{5}{4} = 3{,}720$) and $7$-circuits (absorbed into $6\binom{20}{3} = 6{,}840$).

---

## Independent Mathematical Checks Summary
- Base cases $n = 2$ (all $q \in \{3,4,5\}$, all $2 \le d \le 2(q-1)$): verified exact via `check-check-1.py` (`alpha_0 < alpha_1` in all 15 pairs).
- Lemma 1 (Affine Dimension Lemma), Corollary 2 (exact $\mathrm{GRM}_q(d,2)^\perp$ dual enumerators: $A_6 = 24, 1920, 52{,}000$ and $A_6 = A_7 = 0$ for $\mathrm{GRM}_5(3,2)^\perp$), Lemma 4 (Normalized MacWilliams), Lemma 5(1)–(4), and Remark ($q \ge 7, d=2$, large $n$): all independently verified sound.
