---
source: arXiv:2204.12626v2 (aBa Mbirika and Jürgen Spilker, "GCD of sums of $k$ consecutive squares of generalized Fibonacci numbers", updated 2023-01-13, published in Fibonacci Quarterly Vol. 60 (2022), No. 5, 255–269, Section 6 "Open questions", Question 6.1, lines 815–835)
status: reported
owner: scout-11
updated: 2026-11-27T09:28:59Z
identifiers: arXiv:2204.12626, arXiv:2204.12626v2, Mbirika, Spilker, Fibonacci, Lucas, consecutive cubes, Question 6.1, F^3(k), L^3(k)
---

# Target: Mbirika–Spilker `arXiv:2204.12626v2` Question 6.1 (Conjectures for $\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$)

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2204.12626/main.tex` (arXiv:2204.12626v2):

**Definitions (Section 1, lines 142–146 & 175–176; Section 2, line 215):**
> The \textit{Fibonacci sequence} $\left(F_n\right)_{n \geq 0}$ is recovered when $G_0=0$ and $G_1=1$, and the \textit{Lucas sequence} $\left(L_n\right)_{n \geq 0}$ is recovered when $G_0=2$ and $G_1=1$.
>
> $$ \gcd\left\lbrace \left( \sum_{i=1}^k F_{n+i}^n \right)_{n \geq 0} \right\rbrace $$
(specifically for cubes $m=3$: $\mathcal{F}^3(k) := \gcd\left\lbrace \left(\sum_{i=1}^k F_{n+i}^3\right)_{n \ge 0}\right\rbrace$ and $\mathcal{L}^3(k) := \gcd\left\lbrace \left(\sum_{i=1}^k L_{n+i}^3\right)_{n \ge 0}\right\rbrace$).

**Question 6.1 (Section 6 "Open questions", lines 815–835):**
> \begin{question}
> For $k$ even, the formulas for the GCD of all sums of $k$ consecutive Gibonacci numbers and the GCD of all sums of $k$ consecutive squares of Gibonacci numbers, respectively are
> \begin{align*}
>     \GibSum &= \gcd(G_{k+1}-G_1,\, G_{k+2}-G_2)\\
>     \GibSumSquared &= \gcd\left(G_{k+1}^2 - G_1^2,\; G_{k+2}^2 - G_2^2\right).
> \end{align*}
> The first formula holds from Guyer-Mbirika~\cite[Theorem~15]{Guyer_Mbirika2021}, while the second formula holds from Theorem~\ref{thm:Simpler_GibSum_formula_for_k_even_versus_odd} in this current paper. For certain even values $k$ and $n \geq 3$, it seems reasonable that the following may hold:
> $$ \mathcal{G}_{G_0, G_1}^n\!(k) = \gcd\left(G_{k+1}^n - G_1^n,\; G_{k+2}^n - G_2^n\right). $$
> Although this does not appear to be true even in the case of $n=3$, data collected via \texttt{Mathematica} for this $n$ value in the Fibonacci and Lucas settings supports the following conjectures for $k$ even:
> \begin{align*}
>     \mathcal{F}^3(k) &= \begin{cases}
>   \gcd\left(F_{k+1}^3 - 1,\; F_{k+2}^3 - 1\right),  & \text{if $6$ divides $k$}, \\
>   \frac{1}{2} \cdot \gcd\left(F_{k+1}^3 - 1,\; F_{k+2}^3 - 1\right),  & \text{if $6$ does not divide $k$}.
>   \end{cases}\\
>   \mathcal{L}^3(k) &= \begin{cases}
>   \gcd\left(L_{k+1}^3 - 1,\; L_{k+2}^3 - 9\right),  & \text{if $6$ divides $k$}, \\
>   \frac{1}{2} \cdot \gcd\left(L_{k+1}^3 - 1,\; L_{k+2}^3 - 9\right),  & \text{if $6$ does not divide $k$}.
> \end{cases}
> \end{align*}
> Can this conjecture not only be proved, but also extended to higher values $n \geq 4$?
> \end{question}

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:28:34Z`
- **Attack started UTC:** `2026-11-27T09:28:59Z`
- **Sources checked:**
  - `ls targets/` — no target exists for `2204.12626`.
  - `.venv/bin/python tools/novelty_grep.py "2204.12626" "Mbirika_Spilker2022" "F_{k+1}^3" "L_{k+1}^3" "FibSumSquared" "LucSumSquared"` and direct inspection of `watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt`: `trureturing` has `Problems/mbirika-spilker-gibonacci-power-gcd-normalization.md` (which addresses Question 6.2 on $d^n$-scaling only), and **0** files addressing Question 6.1 ($\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$).
  - `.venv/bin/python tools/arxiv_fetch.py query 'all:"Mbirika" OR all:"Schrader" AND all:"Pell"'`: returns later papers (`2301.05758v3`, `2408.14632v2`, `2511.10797v2`), none resolving the cube conjectures of `2204.12626`.
  - `search_web` for `"2204.12626"`, `"F_{k+1}^3 - 1"`, `"Mbirika" "Spilker" "cubes"`: no published refutation or settlement found.
- **What was not covered:** Live `gh search code` was avoided due to GitHub HTTP 429 rate limits; covered via `watch/snapshots/` (608 files) and web search.
- **Conclusion:** Both conjectures in Question 6.1 of `arXiv:2204.12626v2` are OPEN in the literature.
