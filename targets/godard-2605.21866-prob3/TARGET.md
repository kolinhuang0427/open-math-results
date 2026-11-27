---
source: https://arxiv.org/abs/2605.21866v1
status: reported
owner: attack-3
updated: 2026-11-27T09:13:30Z
identifiers:
  - 2605.21866
  - arxiv:2605.21866v1
  - godard-2605.21866-prob3
  - Godard
  - Lucas Reis
  - prob3
---

# Godard–Reis (2026), Problem 5.3 (Connectedness threshold $s(n)$ for $\Gamma(Q_b, V)$)

**Primary source:** Jean Godard and Lucas Reis, *Graphs from quadratic forms and vector spaces over finite fields*, [arXiv:2605.21866v1](https://arxiv.org/abs/2605.21866v1) (2026-05-21), Section 5 ("Conclusions and open problems"), Problem 5.3 (3rd problem in Section 5, lines 363–368 of `godard-reis.tex`).

## Verbatim Statement

From `tools/.arxiv_cache/eprint/2605.21866/godard-reis.tex` (v1, Definition 1.1 at line 100, line 114, and Problem 5.3 at lines 363–368):

> Let $q$ be an odd prime power, $n \ge 4$, $Q_b(X, Y) := X^2 + bXY + Y^2$ with $b \in \mathbb{F}_{q^n}^*$, and let $V \subsetneq \mathbb{F}_{q^n}$ be a proper $\mathbb{F}_q$-vector subspace. $\Gamma(Q_b, V)$ is the undirected graph with vertex set $\mathbb{F}_{q^n}$ and edges $(x, y)$ ($x \neq y$) iff $Q_b(x, y) \in V$.
>
> **Problem 5.3:** For each integer $n \ge 4$, find the smallest integer $s(n)$ with the following property: if $q$ is large and $\#V \ge q^{s(n)}$, then $\Gamma(Q_b, V)$ is connected for every $b \in \mathbb{F}_{q^n}^*$.
>
> Theorem \ref{thm:diam} and Remark \ref{rem:disc} provide the bounds $s(n) \le 3n/4$ and, for $n$ even, $s(n) > n/2$. In particular, we obtain $s(4) = 3$, $s(6) \in \{4, 5\}$, $s(8) \in \{5, 6\}$ and $s(10) \in \{6, 7\}$.

(Note: Theorem \ref{thm:diam} yields $\#V \ge q^{3n/4}$, so $s(n) \le \lceil 3n/4 \rceil$, giving $8$ at $n=10$ rather than $7$, though $s(n) \le \lfloor 2n/3 \rfloor + 1$ immediately improves the general upper bound to $2n/3$ and yields $s(10) \le 7$, $s(7) \le 5$.)

## Gate 1 Novelty Receipt

- **Checked at (UTC):** 2026-11-27T21:37:00Z (note system clock/UTC output `date -u` was `2026-11-27`, let's verify exact UTC string from step 878).
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py 2606.28849 2605.21866 2603.08510` -> 0 hits across 413 files.
- **arXiv check:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2605.21866` -> `2605.21866v1` (2026-05-21) is the sole version.
- **Web search (`search_web`):** `"2605.21866" OR "Graphs from quadratic forms and vector spaces over finite fields" "Godard" "Reis"` -> only `2605.21866v1` itself.
- **GitHub read-only checks (`gh search code`):** `2605.21866` hits only mirrors/indexes (`cross-theory-formal-database`, `proximityprize`, `openwiki`, `rss_fetch`); `trureturing` and `aliromman/math` -> 0 hits.
- **What was not covered:** Literature published after May 2026 not indexed by arXiv, web search, or GitHub.
