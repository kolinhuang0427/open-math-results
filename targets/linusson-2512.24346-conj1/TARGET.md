---
source: https://arxiv.org/abs/2512.24346v1 (Section 3.4, Conjecture 1 / label conj:complement)
status: reported
owner: attack-2
updated: 2026-11-26T23:58:00Z
identifiers: 2512.24346, linusson, ozdemir, k-Plancherel, TASEP, symmetry of complements, finite k-chain
---

# Linusson–Özdemir (2025) — Symmetry of Complements in the Finite $k$-Chain (Conjecture 1)

## Verbatim Statement
From `arXiv:2512.24346v1` (`Kplancherel.tex`, Section 3.4, lines 641–645):
> For a $\lambda\in\mathcal{R}_k$, let $\lambda^{\mathrm{comp}}\in\mathcal{R}_k$ be such that 
> $\lambda \cup \lambda^{\mathrm{comp}} = (k-1,(k-2)^2,\ldots,i^{k-i},\ldots,2^{k-2},1^{k-1})$, that is $l_i(\lambda)+l_i(\lambda^{\mathrm{comp}})=k-i$.
>  \begin{conjecture} \label{conj:complement}\textnormal{(Symmetry of complements)}
>    For all $\lambda\in\mathcal{R}_k$, $\pi(\lambda)=\pi(\lambda^{\mathrm{comp}}).$
> \end{conjecture}

*(Also tracking sibling conjectures in Section 3.4 & Section 4 on the same finite $k$-chain: `conj:lcd` $\pi(\lambda) = A_\lambda / M_k$ with $M_k = \prod_{j=1}^k \binom{2j}{j}$, `conj:minimum`, and `conj:rho` $\rho_i = 1/\binom{k+2}{3}$.)*

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-26T20:50:00Z
- **Sources checked:**
  - `tools/novelty_grep.py 2512.24346 "Linusson" "Plancherel"` across all `watch/snapshots/**` (0 hits).
  - `search_web`: `"2512.24346" OR "The k-Plancherel measure and a Finite Markov Chain" ("proved" OR "disproved" OR "counterexample")`
  - arXiv abs + eprint via `tools/arxiv_fetch.py`: `2512.24346v1` (30 Dec 2025).
- **Near misses:** None found. Authors verified computationally for $k \le 6$.
- **Not covered:** Citations to `2512.24346` after Dec 2025 outside `search_web` and `watch/snapshots/`.
