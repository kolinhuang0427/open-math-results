# Independent Check Report: `targets/dris-2202.08116-conj5.1/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2202.08116v1` (Jose Arnaldo Bebita Dris, *"A new approach to odd perfect numbers via GCDs"*, confirmed latest version via `tools/arxiv_fetch.py query --id-list 2202.08116`), TeX file `tools/.arxiv_cache/eprint/2202.08116/main.tex`.
- **Exact section/lines verified:**
  - Section 5 (`\section{On the equation $H = I$}\label{Sec5}`), lines 386–391:
    `\begin{conjecture}\label{AsymptoticDensity2}`
    "The asymptotic density $\mathscr{A}$ of positive integers $m$ with $\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))$ satisfies $\mathscr{A} = 0$."
  - Abstract (lines 57–59): $\mathscr{A} = \{m : \gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))\}$.
  - Section 5 table (lines 348–359): counts of solutions up to $10, 10^2, 10^3, 10^4$ are $10, 99, 974, 9561$.
- **Comparison with `TARGET.md` and `PROOF.md`:** Verbatim match with `main.tex`; zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical & Lemma Check

Written independently from the primary-source definitions and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/dris-2202.08116-conj5.1/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python targets/dris-2202.08116-conj5.1/notes/check-check-2.py
  ```
- **Raw output:**
  ```text
  Primary-source table counts verified up to 10000: {10: 10, 100: 99, 1000: 974, 10000: 9561}
  Lemma 1 verified on m <= 10000 (137 excluded integers all satisfy m not in A)
  Lemma 2 exact period check k=1 (M_1=49): d(E_1) = 43/49
  Lemma 2 exact period check k=2 (M_2=8281): d(E_2) = 6751/8281
  Lemma 3 exact CRT check on Q_7(23) (N_P=256036): E[f]=95817/256036, Var(f)=19874323827/65554433296, d(B~)=61911/64009
  Lemma 3 Chebyshev bound verified in exact Fraction DP (13 primes, E=108280528334352935238267890681/92568222856376731590410384100, P(<=1) <= Var/(E-1)^2 <= E/(E-1)^2)
  PASS (all exact checks passed in 0.440s)
  ```

## 3. Summary of Checked Steps

1. **Lemma 1:** Verified unique distinct roots $r_p, s_p \in \{2, \dots, p-2\}$ of $u^2 + u + 1 \equiv 0 \pmod p$ for all primes $p \equiv 1 \pmod 6$ up to $200$, and verified on all $m \le 10^4$ that $p \parallel m$ with $\ge 2$ primes $q \in \mathcal{Q}_p$ satisfying $q \parallel m$ forces $m \notin A$ (137 hits).
2. **Lemma 2:** Verified covering $A \cap [1, 10^4] \subseteq E_k \cup \bigcup_{i=1}^k B_i$ for $k=1,2,3$ and exact CRT densities over full periods $M_1 = 49$ and $M_2 = 8281$.
3. **Lemma 3 & Conclusion:** Verified exact CRT independence, moments $\mathbb{E}[f_P] = S(P)$ and $\mathrm{Var}(f_P) = \sum \alpha_q(1-\alpha_q) \le S(P)$ over all $N_P = 256036$ integers for $\mathcal{Q}_7(23)$, exact Chebyshev bound $\mathbb{P}(f_P \le 1) \le \mathrm{Var}/(\mathbb{E}-1)^2 \le \mathbb{E}/(\mathbb{E}-1)^2$ via exact `Fraction` DP, and $(p-1)/p^2 \ge 1/(2p)$ for all $p \equiv 1 \pmod 6$ up to $200$.
