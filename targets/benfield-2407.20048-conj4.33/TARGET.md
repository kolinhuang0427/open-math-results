---
source: arXiv:2407.20048v2 (Brennan Benfield and Oliver Lippard, "Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers", updated 2025-01-30, Section 4.2 "K-Fibonacci Sequences for Even K", Conjecture 4.33 / `\label{even-K-exceptions}`)
status: reported
owner: scout-11
updated: 2026-11-27T09:13:31Z
identifiers: arXiv:2407.20048, arXiv:2407.20048v2, Benfield, Lippard, Pisano period, K-Fibonacci, even-K-exceptions, Conjecture 4.33, omega_K(m), alpha_K(m), pi_K(m)
---

# Target: Benfield–Lippard `arXiv:2407.20048v2` Conjecture 4.33 (`\label{even-K-exceptions}`)

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2407.20048/fiborder.tex` (arXiv:2407.20048v2):

**Definitions of $K$-Fibonacci sequence, $\pi_K(m)$, $\alpha_K(m)$, $\omega_K(m)$ (Section 4, lines 273 & 306–310; Section 1, line 84):**
> There is a well-studied category of binary recurrences where $b$ is fixed at $1$ while $a$ varies. Traditionally in this case, $a$ is swapped out for $K$, and these binary recurrences are known as $K$-Fibonacci sequences, where $F_{K,0}=0$, $F_{K,1}=1$, and $F_{K,n} = KF_{K,n-1}+F_{K,n-2}$. Because $b$ is fixed at 1, $\omega(m)=1$, 2, or 4 for all $K$. Denote the $K$-Pisano period, $K$-order, and $K$-rank of a positive integer $m$ by $\pi_K(m)$, $\omega_K(m)$, and $\alpha_K(m)$, respectively.
>
> The number of zeros in a Pisano period is the \textit{order} of $m$, denoted $\omega(m)$.
>
> $\alpha_K(m)$, or the rank, is the index of the first zero in the Pisano period modulo $m$.

**Conjecture 4.33 (`\label{even-K-exceptions}`, Section 4.2 "K-Fibonacci Sequences for Even K", lines 675–682):**
> \begin{conjecture}\label{even-K-exceptions}
>     The following portions of Theorem \ref{omega-odd-K} also apply to even $K$ for all moduli $m > 3$:
>     \begin{itemize}
>     \item $\omega_K(m)=4$ if and only if $\alpha_K(m)\equiv\pm1\pmod{4}$.\\
>     \item If $\omega_K(m)=2$, then $4\mid\pi_K(m)$ and $2\mid\alpha_K(m)$.\\
>     \item If $4\not\mid\pi_K(m)$, then $\omega_K(m)=1$.
>     \end{itemize}
> \end{conjecture}

*(Note: Conjecture 4.33 is numbered as the 33rd numbered theorem-like environment in Section 4, where `theorem` shares counter `[section]`, directly following Theorem 4.26 `\label{omega-odd-K}`, ..., Theorem 4.31 `\label{mainthm-even-K}`, Question 4.32.)*

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:12:59Z`
- **Attack started UTC:** `2026-11-27T09:13:31Z`
- **Sources checked:**
  - `ls targets/` — only `benfield-2407.20048-conj5.3` exists for `2407.20048`; no target for `even-K-exceptions` / Conjecture 4.33.
  - `.venv/bin/python tools/novelty_grep.py "even-K-exceptions" "4 \not\mid\pi_K" "2407.20048" "omega_K(m)=4"`: 0 lines across 0/607 snapshot files.
  - `.venv/bin/python tools/novelty_grep.py "BenfieldLippard" "pisano-order" "9448" "9451" "K-Fibonacci" "4 \mid \pi" "omega_K"` and direct check of `watch/snapshots/ai-collections/the-omega-institute__trureturing/files.txt` (`Problems/pisano-order-range-refutation.md` covers only Conjecture 5.3 clause (v); no file addresses Conjecture 4.33 / `even-K-exceptions`).
  - `.venv/bin/python tools/arxiv_fetch.py query 'all:"Benfield" AND all:"Pisano"'`: returns only `2407.20048v2` itself.
  - `search_web` for `"even-K-exceptions"`, `"Benfield" "Lippard" "even K" "Pisano"`, `"2407.20048"` with `"Conjecture 4"`: no published resolution of Conjecture 4.33 found.
- **What was not covered:** Live `gh search code` was avoided due to GitHub HTTP 429 rate limits; covered via `watch/snapshots/` (607–608 files) and web search.
- **Conclusion:** Conjecture 4.33 (`\label{even-K-exceptions}`) is OPEN in the literature.
