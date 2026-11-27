---
source: arXiv:2412.02932v1 (Peter L. Guo & Zhuowei Lin, "Schubert polynomials and patterns in permutations", Section 5.2, Conjecture 5.7 `\label{locond-3}`)
status: reported
owner: scout-8
updated: 2026-11-27T09:49:40Z
identifiers:
  - arXiv:2412.02932v1
---

# Guo–Lin (2024) — Positivity of Pattern Coefficients $d_u$ for Schubert Monomial Support $\theta_w$

## Exact Conjecture Statement (`arXiv:2412.02932v1`, `main.tex` Section 5.2, lines 1355–1368)

For a permutation $w \in S_n$, let $\theta_w$ denote the number of monomials in the Schubert polynomial $\mathfrak{S}_w(x)$ (equivalently, lattice points in its Newton polytope). Expanding
$$\theta_w = 1 + \sum_u d_u\, p_u(w),$$
where $p_u(w)$ is the number of occurrences of pattern $u$ in $w$, the coefficients $d_u$ for $u \in S_m$ are uniquely defined recursively by
$$d_u = \theta_u - 1 - \sum_{\sigma \in S_\ell,\, \ell < m} d_\sigma\, p_\sigma(u).$$

**Conjecture 5.7 (`\label{locond-3}`):**
> For any permutation $u$, we have $d_u \in \mathbb{Z}_{\geq 0}$.

(Verified in `2412.02932v1` up to $n \le 8$; see also Conjecture 5.2 `\label{conk-09}` asserting that $\beta_n = \max_{w \in S_n} \theta_w$ is attained by layered permutations, verified up to $n \le 9$.)

## Gate 1 Novelty Receipt (2026-11-27T09:43Z)
- `tools/novelty_grep.py "2412.02932"` across `watch/snapshots/**`: `0` lines across `0/606` files.
- `gh search issues "2412.02932"`: `0` issues.
- `gh search repos "2412.02932"`: `0` repositories.
- `.venv/bin/python tools/arxiv_fetch.py query '"2412.02932"'`: `0` citing/follow-up entries.
- Web search (`"2412.02932" OR "theta_w" "Schubert polynomial" "layered" "Guo" "Lin"`): only `2412.02932` itself.

## Attack Log
- Started: `2026-11-27T09:44:06Z`
- Finished: `2026-11-27T09:49:40Z`
- Outcome: `candidate` — Exhaustive C++ computation over all $409{,}113$ permutations in $\bigsqcup_{n=1}^9 S_n$ (`notes/test_du_n9.cpp`) found the unique minimal counterexample $u = 134562897 \in S_9$ with $\theta_u = 113$, $1 + \sum_{\sigma \neq u} d_\sigma p_\sigma(u) = 114$, and $d_u = -1 < 0$ ($c_u = 0$). Pure-integer `verify.py` (`PASS`, 0 floats) independently confirms via divided differences and $\mathfrak{S}_u = e_4(x_1..x_5)e_2(x_1..x_8)$.
