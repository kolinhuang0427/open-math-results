source: https://arxiv.org/abs/2605.25743v3 (Section 1 Conjecture 1.1 & Section 6 Conjecture 6.5, `conj:sos` and `conj:hermite`)
status: reported
owner: attack-5
updated: 2026-11-27T08:13:00Z
identifiers: ["2605.25743", "2605.25743v3", "Riener", "Shapiro", "Hermite-matrix SOS", "conj:hermite", "conj:sos", "square-graph cone"]

# Riener–Shapiro (2026) — Hermite-Matrix & Scalar SOS Conjectures for Derivative Discriminants (`conj:hermite` / `conj:sos`)

- **Started:** 2026-11-27T03:36:51Z

## Exact Statements
From Cordian Riener and Boris Shapiro, *Discriminants of derivatives: square graphs and sums of squares*, arXiv:2605.25743v3 (submitted 2026-05-25, updated 2026-10-21), Sections 1 & 5 (`article.tex`, lines 123–126, 401–437, 1716–1730, 1983–1987):

> **Conjecture 1.1 (`conj:sos`, sum-of-squares question).** For every $n\ge 2$ and every $0\le k\le n-2$, the polynomial $\mathrm{D}_k^{(n)}$ is a sum of squares of polynomials in the differences $x_i-x_j$.

> **Conjecture 5.6 (`conj:hermite`, Hermite-matrix SOS conjecture).** For every $n\ge 2$ and $0\le k\le n-2$, the ordinary Hermite matrix of $P^{(k)}/\mathrm{lc}(P^{(k)})$ is an SOS matrix over $\mathbb{R}[x_1,\ldots,x_n]$.

Definitions (`article.tex`, lines 99–106, 401–437, 1716–1730):
- $P(t) = \prod_{i=1}^n (t - x_i)$ is the monic polynomial of degree $n$ with roots $x_1,\ldots,x_n$, and $\mathrm{D}_k^{(n)}(x_1,\ldots,x_n) := \mathrm{disc}(P^{(k)})$ for $0 \le k \le n-2$.
- Centered roots: $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$, $z_i = x_i - \bar{x}$, $p_j = \sum_{i=1}^n z_i^j$ ($j \ge 1$, $p_1 = 0$).
- Normalized terminal derivative of degree $r = n - k$:
  $$J_{n,r}(t) = \frac{r!}{n!} P^{(n-r)}(t) = \binom{n}{r}^{-1} \sum_{|S|=r} \prod_{i\in S}(t-x_i) = t^r + \sum_{j=2}^r (-1)^j \frac{\binom{r}{j}}{\binom{n}{j}} e_j t^{r-j} \quad \text{(centered)}.$$
- For a monic polynomial $f$ of degree $r$ with roots $\theta_1,\ldots,\theta_r$, $s_j(f) = \sum_{l=1}^r \theta_l^j$, and its ordinary Hermite matrix is $H(f) = (s_{i+j}(f))_{0 \le i,j \le r-1}$. An *SOS-matrix factorization* is an identity $H(f) = A^{\mathsf T} A$ with polynomial entries in $A$ (over $\mathbb{R}[x_1,\ldots,x_n]$, equivalently $\mathbb{R}[z_1,\ldots,z_n]$). By Cauchy–Binet, `conj:hermite` implies `conj:sos`.
- **Known vs. open status in `2605.25743v3`:** Both conjectures are proved for $k \in \{0, 1\}$ and $r = n-k \in \{2, 3, 4\}$ (all $n \ge r$). The remaining open cases are $2 \le k \le n-5$ ($r \ge 5$), starting at **$(n,k) = (7,2)$** ($r = 5$). Proposition 6.2 verifies `conj:hermite` in the centered outlier limit $K_r$ for $3 \le r \le 6$.

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T03:32:00Z
- **Local `novelty_grep.py`:** Searched `"2605.25743"`, `"Riener"`, `"Hermite-matrix"`, `"square-graph"` across 469 files in `watch/snapshots/**` (including `1337-solved-conjectures`, `openai-math`, `erdosproblems`, `formal`, `discovered/` covering `aliromman/math`, `the-omega-institute/trureturing*`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`): **0 hits** for all four terms. (Also checked `"Hermite matrix"` / `"Alexandersson"` / `"discriminant"`: 100 hits across 34/461 files, none mentioning Riener–Shapiro `2605.25743` or derivative Hermite-matrix SOS.)
- **arXiv:** `arxiv_fetch.py query` for `id_list=["2605.25743"]` shows `v3` (2026-10-21) is latest; `abs:"2605.25743"` returned 0 citing/mentioning arXiv papers.
- **OpenAlex / Zenodo:** OpenAlex work `W7162418932` has `cited_by_count: 0`; Zenodo API query `2605.25743 OR 2212.02496` returned 0 hits.
- **GitHub & Web:** `gh search repos "2605.25743"` returned 0 repos; `gh search code "2605.25743"` returned only corpus/wiki/paper-reader mirrors (`AlexenderSokolov/cross-theory-formal-database`, `veenrek/openwiki`, `twenhui2-afk/daily-paper-reader`), no solutions; `search_web` returned no resolution.
- **What was not covered:** Papers/repos not indexed by arXiv, OpenAlex, Zenodo, GitHub search, web search, or `watch/snapshots/**` as of 2026-11-27T03:32Z.
- **Verdict:** Open (passes Gate 1).
