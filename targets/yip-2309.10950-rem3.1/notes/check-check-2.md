# Independent Check Report: `targets/yip-2309.10950-rem3.1/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2309.10950v2` (Chi Hoi Yip, *"Restricted sumsets in multiplicative subgroups"*, published in *Canad. J. Math.* 78 (2026), 594–618, DOI `10.4153/S0008414X24000920`, confirmed latest arXiv version via `tools/arxiv_fetch.py query --id-list 2309.10950`), TeX file `tools/.arxiv_cache/eprint/2309.10950/main.tex`.
- **Exact sections/lines verified:**
  - Section 1, Theorem 1.7 (`\label{thm:VLM}`, lines 105–107): "Let $d \geq 3$. Let $q \equiv 1 \pmod d$ be an odd prime power and a square. If $A \subset \mathbb{F}_q$ such that $A\hat{+}A \subset S_d \cup \{0\}$, then $|A| \leq \sqrt{q}$, with the equality holds if and only if $d \mid (\sqrt{q}+1)$ and $A=\alpha \mathbb{F}_{\sqrt{q}}$, where $\alpha \in S_d$."
  - Section 3.2, Remark 3.3 (`\begin{rem}`, lines 405–407): "Our analysis cannot handle the case $d=2$. In fact, there is $A \subset \mathbb{F}_9$ with size $4$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_9) \cup \{0\}$, and there are $15$ different $A \subset \mathbb{F}_{25}$ with size $5$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_{25}) \cup \{0\}$. Nevertheless, we conjecture that when $q$ is an odd square and $q \geq 49$, the statement of Theorem~\ref{thm:VLM} also extends to the case $d=2$."
- **Comparison with `TARGET.md` and `PROOF.md`:** Verbatim match; zero quantifier, hypothesis, edge-case (including odd prime powers $r = p^s$ in characteristic 3 and $2 \mid (\sqrt{q}+1)$ holding automatically for odd $\sqrt{q}$), or definition drift.

## 2. Independent Mechanical & Finite-Field Check

Written independently from `main.tex` and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/yip-2309.10950-rem3.1/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/yip-2309.10950-rem3.1/notes/check-check-2.py
  ```
- **Raw output:**
  ```text
  F_25 non-coset size-5 clique Lemma 2.2 & 2.3 check: PASS ([(0, 1), (0, 4), (1, 0), (3, 1), (3, 4)])
  r=7 (q=49) norm circles, S(theta), and explicit witnesses: PASS
  r=9 (q=81) norm circles, S(theta), and ALL 8 z^10=-1 witnesses: PASS
  r=11 (q=121) norm circles, Claim 2.4, eq (4), Hasse bound: PASS
  Case 1 M^2 = qI - J check on F_25, F_49: PASS
  PASS (all checks passed in 0.693s)
  ```

## 3. Summary of Verified Lemmas & Boundary Cases

1. **Case 1:** Verified $M \mathbf{1} = 0$ and $M^2 = q I - J$ directly over $\mathbb{F}_{25}$ and $\mathbb{F}_{49}$.
2. **Case 2 Steps 1–2 (Lemmas 2.2 & 2.3):** Verified Lagrange interpolation identity (1), $\deg H_k \le (r-1)/2$, exact evaluations $H_k(b^r)$, $Q_k \equiv 0$, and rational parametrization $b = V(b^r)/U(b^r)$ with $\max(\deg U, \deg V) = 1$ on an explicit $q=25$ non-coset size-5 clique.
3. **Case 2 Step 3 (Subcases 3B(ii)–(iii)):** Verified Fact 1–2, Claim 2.4, identity (4), exact $|C \cap N_2|$ formulas, and Hasse bound across all $(c, \lambda)$ circles in $\mathbb{F}_{49}, \mathbb{F}_{81}, \mathbb{F}_{121}$. Confirmed the explicit witnesses $b_1 = 4+u, b_2 = 2+3u$ for both $r=7$ circles and all 8 $z \in \mathbb{F}_{81} \setminus \mathbb{F}_9$ ($z^{10}=-1$) witnesses $b_1 = 1+z, b_2 = 1+z^3$ for $r=9$ satisfy $b_1, b_2 \in C \cap N_2$ with $b_1 + b_2 \in N_2$.
