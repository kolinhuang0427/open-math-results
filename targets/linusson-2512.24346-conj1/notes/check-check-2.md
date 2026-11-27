# Independent Check Report: `targets/linusson-2512.24346-conj1/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2512.24346v1` (Svante Linusson and Alperen Özdemir, *"The $k$-Plancherel Measure and a Finite Markov Chain"*, 2025-12-30, confirmed latest version via `tools/arxiv_fetch.py query --id-list 2512.24346`), TeX file `tools/.arxiv_cache/eprint/2512.24346/Kplancherel.tex`.
- **Exact sections/lines verified:**
  - Section 2.2–2.4 (`Kplancherel.tex` lines 113–238): $(k+1)$-cores $\mathcal{C}_{k+1}$, $\mathfrak{p}, \mathfrak{c}$, weak cover $\kappa \to_k \tau$, strong marked tableaux (`def:tab`), $d_\lambda^{(k)} = [x_1\cdots x_n] s_\lambda^{(k)} = \mathbf{K}_{\lambda, (1^n)}^{(k)}$.
  - Section 3.2–3.3 (`Kplancherel.tex` lines 281–312): Pieri rule, $k$-rectangle $\square_i = (i^{k-i+1})$, $k$-rectangle property $s_{\square_i} s_\lambda^{(k)} = s_{\lambda \cup \square_i}^{(k)}$, state space $\mathcal{R}_k$, transition matrix $P(\lambda, \mu)$, stationary distribution $\pi$.
  - Section 3.4 (`Kplancherel.tex` lines 641–645): `conj:complement` (Symmetry of complements): "For all $\lambda \in \mathcal{R}_k$, $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$", where $l_i(\lambda) + l_i(\lambda^{\mathrm{comp}}) = k - i$.
  - Paper's $k=3$ diagram (`fig:k=3`, lines 560–565) and $k=4$ table (lines 657–668).
- **Comparison with `TARGET.md` and `PROOF.md`:** Exact verbatim match on statement and definitions; zero quantifier, hypothesis, edge-case (including $k=1$ and the $k=2$ merged cover $(1) \to \emptyset$), or definition drift. (`PROOF.md` also accurately notes the typo on line 517 of `Kplancherel.tex` writing $\lambda^{\omega_k}$ instead of $\lambda^{\mathrm{comp}}$.)

## 2. Independent Mechanical & Lemma Check

Written independently from `Kplancherel.tex` and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/linusson-2512.24346-conj1/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/linusson-2512.24346-conj1/notes/check-check-2.py
  ```
- **Raw output:**
  ```text
  k=1 (|R_1|=1, Z_1=1): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
  k=2 (|R_2|=2, Z_2=2): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
  k=3 (|R_3|=6, Z_3=5/3): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
  k=4 (|R_4|=24, Z_4=35/432): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
  k=5 (|R_5|=120): Lemmas 2 & 4 PASS
  PASS (all checks passed in 0.023s)
  ```

## 3. Summary of Verified Lemmas & Identities

1. **Lemma 1:** Verified $d_\lambda^{(k)}$ directly from strong marked tableaux (`def:tab`), Pieri row-stochasticity $\sum_\mu P(\lambda, \mu) = 1$, and exact $k$-rectangle dimension identity $\frac{d_{\lambda \cup \square_i}^{(k)}}{|\lambda \cup \square_i|!} = \frac{d_{\square_i}}{|\square_i|!} \frac{d_\lambda^{(k)}}{|\lambda|!}$ for all $\lambda \in \mathcal{R}_k, i \in [k]$ ($k=1..4$).
2. **Lemma 2:** Verified the Maya-diagram / cyclic-arc bijection $\alpha: S_k \to \mathcal{R}_k$ and $\alpha(\sigma^{\mathrm{rev}}) = \alpha(\sigma)^{\mathrm{comp}}$ exhaustively for $k=2..5$ (up to 120 states).
3. **Lemma 3 & 4:** Verified TASEP swap correspondence for all weak covers, distinctness of projections for $k \ge 3$ (and $k=2$ merge), and irreducibility for $k=2..5$.
4. **Theorem 1 & Corollary 2:** Verified exact $R$-reversibility $\pi(\lambda) P(\lambda, \mu) = \pi(\mu) P(R(\mu), R(\lambda))$, exact stationarity $\pi P = \pi$, exact agreement with the paper's $k=3$ and $k=4$ stationary tables, and $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$ for $k=1..4$.
