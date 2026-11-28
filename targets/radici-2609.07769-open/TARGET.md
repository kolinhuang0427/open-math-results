---
title: "Radici-Sala Open Problem: alpha_1 > alpha_0 over F_3, F_4, F_5 (arXiv:2609.07769v2, §9)"
source: "arXiv:2609.07769v2"
status: reported
owner: scout-9
started_utc: 2026-11-27T19:25:49Z
updated_utc: 2026-11-28T00:31:00Z
identifiers:
  - "arXiv:2609.07769v2"
  - "MQ_0"
  - "MQ_1"
  - "alpha_1 - alpha_0"
---

# Radici–Sala Open Problem: $\alpha_1 > \alpha_0$ over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$ (`arXiv:2609.07769v2`, §9)

- **Source:** Gabriele Radici & Massimiliano Sala, *A Note on Binary Quadratic Systems and Their Relation to Complexity Theory*, `arXiv:2609.07769v2` (`2026-11-25`), Section 9 (*Open problems*, `main-v32.tex` L1494–1566, esp. L1498–1527), referencing Theorem `thm:main` / inequality `eq:main` (Section 7, `main-v32.tex` L1283–1292).
- **Status:** `reported` (complete proof settled for all $q \in \{3,4,5\}$, $n \ge 2$, $2 \le d \le n(q-1)$ in `PROOF.md` + `verify.py`)
- **Owner:** `scout-9`
- **Started UTC:** `2026-11-27T19:25:49Z`
- **Updated UTC:** `2026-11-28T00:31:00Z`

## Exact Quoted Statement

From `tools/.arxiv_cache/eprint/2609.07769.src` (`main-v32.tex`), Section 7 (`main-v32.tex` L1283–1292) & Section 9 (`main-v32.tex` L1498–1527):

> **Theorem (`thm:main`):** Let $n\ge 2$ and $2\le d\le n$. Then
> $$\Bigl(1-\frac{2}{5N^{2}}\Bigr)\frac{\alpha_1}{N} \le \alpha_1-\alpha_0 \le \frac{\alpha_1}{N},$$
> with equality in the upperbound if and only if $d = n$.
> In particular, the following inequality holds:
> $$\alpha_1 > \alpha_0 \qquad (\text{eq:main})$$

> **Section 9 (`main-v32.tex` L1498–1527):**
> "The first natural question that comes to mind after seeing Theorem \ref{thm:main} is whether there is anything special about the binary field. Any attempt to generalise will start from the following experimental observations.
> Fix a prime power $q$, let $V=(\mathbb{F}_q)^{\,n}$, $N=q^n$, and let $Q_{q,d}$ be the space of functions $V\to\mathbb{F}_q$ of total degree at most $d$, written in reduced form with all exponents at most $q-1$; put $D_q=\dim Q_{q,d}$ and let $\alpha_k(q,n,d)$ be the number of square systems of $n$ such functions having exactly $k$ zeros in $V$, out of $q^{\,nD_q}$.
> Exact enumeration of all $q^{\,2D_q}$ systems at $n=2$, $d=2$ gives ... so that $\alpha_0(7,2,2)-\alpha_1(7,2,2)=146\,358\,624>0$, and thus \eqref{eq:main} fails over $\mathbb{F}_7$ (and we think it is more evident with larger fields).
> The remaining possibilities are $q=3, q=4, q=5$, which we present as open problems."

## Gate 1 Novelty Receipt (`2026-11-27T19:25Z`)

- `targets/`: `0` existing folders matching `07769` or `radici`.
- `tools/novelty_grep.py "2609.07769" "Radici" "alpha_0"` across 811 files: only arXiv sweep indexing `2609.07769v2` (`0` settlements).
- GitHub (`gh search prs/issues "2609.07769"`): `0` matches.
- arXiv `--no-cache` (`tools/arxiv_fetch.py abs 2609.07769 --no-cache`): `2609.07769v2` (`2026-11-25`) latest.
- Web search (`"2609.07769" OR "A Note on Binary Quadratic Systems" Radici Sala "F_3" OR "F_4" OR "F_5"`): clear (`0` follow-up settlements).
