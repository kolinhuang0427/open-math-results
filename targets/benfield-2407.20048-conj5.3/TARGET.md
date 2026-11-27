---
source: arXiv:2407.20048v2 (Brennan Benfield and Oliver Lippard, "Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers", updated 2025-01-30, Section 5 "Final Remarks", Conjecture 5.3 / `\label{finite-orders}`, rescoped strictly to clause (vi))
status: reported
owner: scout-11
updated: 2026-11-27T09:08:46Z
identifiers: arXiv:2407.20048, arXiv:2407.20048v2, Benfield, Lippard, Pisano period, K-Fibonacci, (a,b)-Fibonacci, finite-orders, Conjecture 5.3, clause (vi), omega_{(a,b)}(m)
---

# Target: Benfield–Lippard `arXiv:2407.20048v2` Conjecture 5.3, Clause (vi) (`\label{finite-orders}`)

**Scope Note & Prior Credit (`CONTESTED.md`, `notes/contest-ruling-audit-1.md`):**
Clause (v) of Conjecture 5.3 ($b \neq \pm 1, |a| - |b| = 1 \implies \{0,1,2\}$) was previously refuted by `the-omega-institute/trureturing#9448` / PR `#9451` (`Problems/pisano-order-range-refutation.md`, merged `2026-09-22`) at $(a,b) = (3,2), m = 13$ ($\omega_{(3,2)}(13) = 3 \notin \{0,1,2\}$). No novelty is claimed on clause (v). Per the `audit-1` contest ruling (`partial-overlap-still-open`), this target is **rescoped strictly to clause (vi)** (*"infinite in all other cases"*), which PR `#9451` explicitly left open.

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2407.20048/fiborder.tex` (arXiv:2407.20048v2):

**Definition of $(a,b)$-Fibonacci sequence (Section 5 "Final Remarks", lines 692–696):**
> A general binary recurrence sequence $\mathcal{U}_{n}$ is determined by the four parameters $(a,b,c,d)$ where 
> \[
> \mathcal{U}_0=c, \qquad \mathcal{U}_1=d, \qquad \mathcal{U}_n=a\times\mathcal{U}_{n-1}+b\times\mathcal{U}_{n-2}.
> \]
> When $\mathcal{U}_0=0$ and $\mathcal{U}_1=1$, these sequences are often referred to as $(a,b)$-Fibonacci sequences.

(Note: Section 4, line 269 also writes *"for positive integers $a$ and $b$"*; our counterexample $(3,4)$ uses strictly positive integers $a, b$.)

**Definition of order $\omega_{(a,b)}(m)$ (Section 1, line 84 & Section 5, line 724):**
> The number of zeros in a Pisano period is the \textit{order} of $m$, denoted $\omega(m)$.
>
> For illustrative purposes, define the order to be zero if the sequence is eventually periodic modulo $m$ and this period contains no multiples of $m$; this appears to occur if and only if $m$ shares a common factor with either $a$ or $b$.

**Conjecture 5.3 (`\label{finite-orders}`, Section 5 "Final Remarks", lines 729–741):**
> For an $(a,b)$-Fibonacci sequence, the range of $\omega_{(a,b)}(m)$ for $m>1$ is given by
> \begin{enumerate}[label=(\roman*)]
>     \item $\{1\}$ if $(a,b) \in \{(0,1),(1,0),(-1,-1),(\pm2,-1)\}$, \\
>     \\
>     \indent \ \ or if $m=2$ and $(a,b) \in \{(-1,0),(1,-1), (0,-1)\}$,\\
>     \item \{2\} if $m>2$ and $(a,b) \in \{(-1,0),(1,-1), (0,-1)\}$,\\
>     \item $\{1,2,4\}$ if $b=1$ and $a\neq0$,\\
>     \item $\{1,2\}$ if $b=-1$ and $a\not\in\{-2,-1,0,1,2\}$,\\
>     \item $\{0,1,2\}$ if $b \neq \pm1$ and $|a|-|b| = 1$,\\
>     \item infinite in all other cases.
> \end{enumerate}

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:01:48Z`
- **Sources checked:**
  - `tools/novelty_grep.py 2407.20048 "finite-orders" "(3,2)-Fibonacci" "(3,4)-Fibonacci" "Connecting Zeros in Pisano"` (0 lines across 0/601 snapshot files).
  - `tools/novelty_grep.py Benfield Lippard`: 37 lines across 10 files (all referring to `arXiv:2404.08193v2` Waring-gap conjectures; 0 matches for `2407.20048` or Pisano orders).
  - `tools/arxiv_fetch.py query 'all:"2407.20048" OR ti:"Connecting Zeros in Pisano Periods"'`: 1 result (`2407.20048v2` itself).
  - `1337isnot1337/solved-conjectures` (`CONTENTS.md`, `issues`) and `openai/math` tree: 0 matches for `2407.20048`, `finite-orders`, or Pisano order range conjectures.
  - `search_web` for `"2407.20048"`, `"Benfield" "Lippard" "Pisano"`, and `site:github.com "2407.20048"`: no published refutation or counterexample found.
- **What was not covered:** Live `gh search code` was rate-limited (HTTP 429) at the time of check; covered instead via `watch/snapshots/` (601 files) and web search.
- **Conclusion:** Conjecture 5.3 (`\label{finite-orders}`) is OPEN in the literature.
