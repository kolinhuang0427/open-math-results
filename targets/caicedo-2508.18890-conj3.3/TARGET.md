---
source: arXiv:2508.18890v4 (Caicedo–Juhnke–Poullot, "Ehrhart non-positivity and unimodular triangulations for classes of s-lecture hall simplices", Section 3, Conjecture 3.4; folder slug conj3.3)
status: reported
owner: scout-8
updated: 2026-11-27T09:42:22Z
identifiers:
  - arXiv:2508.18890v4
---

# Caicedo–Juhnke–Poullot (2025/2026) — Monotonicity of Ehrhart Non-Positivity for $\mathcal{P}_n^{(a,\dots,a,a+1)}$

## Exact Conjecture Statement (`arXiv:2508.18890v4`, `Ehrhart_non_positivity.tex` lines 109–111)

> **Conjecture:**
> For $n\geq 5$, we conjecture that if $\mathcal{P}_n^{(a, \dots, a, a+1)}$ is Ehrhart non positive for some $a\in \mathbb{N}$, then for all $b\geq a$ the $\mathbf{s}$-lecture hall simplex $\mathcal{P}_n^{(b, \dots, b, b + 1)}$ is also Ehrhart non positive.

Recall from `Ehrhart_non_positivity.tex` Eq. `eq:crucial` (and Theorem `The:Negativity` proof, lines 384–402) that for $\mathbf{s} = (a,\dots,a,a+1)$ of length $n$:
$$\mathcal{L}_{\mathcal{P}_n^{\mathbf{s}}}(t) = \binom{at+n}{n} + \sum_{\ell=0}^{t-1} \binom{a\ell + n - 1}{n - 1}.$$
(Note: line 88 in `Ehrhart_non_positivity.tex` has a minor typo writing $\binom{a\ell+n}{n}$ inside the sum, whereas lines 81–84 and 399–400 have the exact pyramid formula $\sum_{\ell=0}^{t-1} \binom{a\ell+n-1}{n-1}$, verified to match Example 3.3 at $n=5, a=16$ and the $\beta(n) = (16, 19, 23, 27)$ table for $n=5,6,7,8$ identically.)

## Gate 1 Novelty Receipt (2026-11-27T09:24Z)
- `tools/novelty_grep.py "2508.18890"` across `watch/snapshots/**`: `0` lines across `0/606` files.
- `gh search issues "2508.18890"`: `0` issues.
- `gh search repos "lecture hall" "Ehrhart"`: `0` repositories.
- `.venv/bin/python tools/arxiv_fetch.py query '"lecture hall simplices" "Ehrhart non-positivity"'`: 5 results, none post-dating or settling Conjecture 3.3 of `2508.18890v4` (v4 updated `2026-10-27`).
- Web search (`"2508.18890" OR "Ehrhart non-positivity and unimodular triangulations" lecture hall simplices`): only `2508.18890` itself.

## Attack Log
- Started: `2026-11-27T09:25:15Z`
- Finished: `2026-11-27T09:42:22Z`
- Outcome: `candidate` — Complete proof of Conjecture 3.4 (`arXiv:2508.18890v4`, `Ehrhart_non_positivity.tex` L109–111) for all $n \ge 5$ (`PROOF.md`, exact `verify.py` `PASS`: $a \le 6$ positive for all $n$; $5 \le n \le 32$ proved for all $b \ge a$ by exact Sturm/interval root isolation; $n \ge 33, a \ge 2n^{4/3}$ proved via explicit $[t^{n-4}]$ quartic in $a$; $n \ge 33, 8 \le a < 2n^{4/3}$ proved via residue/Cauchy contour bounds on $k \in \{1,2,3,4\}$).
