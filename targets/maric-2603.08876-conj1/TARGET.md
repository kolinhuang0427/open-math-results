source: arXiv:2603.08876v1 (Nevena Marić, "Hierarchical threshold structure in Max-Cut with geometric edge weights", 2026-03-09)
status: reported
owner: attack-6
updated: 2026-11-27T11:48:00Z
identifiers: 2603.08876, 2603.08876v1, Maric, LexiCut, Max-Cut, geometric edge weights, isolated cuts, conj:global

## Exact Statement (arXiv:2603.08876v1, Section 5, Conjecture 5.1, `\label{conj:global}` [Global Optimality])

> **Conjecture (Global Optimality).** For $n \geq 7$ and $r \in (r_k(n), r_{k-1}(n))$, the $k$-isolated cut $C_k$ achieves the maximum weight among all $2^{n-1}$ cuts.

*(Definitions in Section 2: For $r > 1$, the $i$-th edge in lexicographic order of $K_n$ has weight $w_i = r^{N-i}$, where $N = \binom{n}{2}$. For a cut $S \subseteq \{1,\dots,n\}$ with $1 \in S$, $W^n(S;r) = \sum_{1 \le a < b \le n,\, \mathbf{1}_S(a) \ne \mathbf{1}_S(b)} r^{\binom{n-a+1}{2} - (b-a)}$. The $k$-isolated cut is $C_k = \{1,\dots,k\} \mid \{k+1,\dots,n\}$, and $r_k(n)$ is the unique root in $(1,2)$ of $W^n(C_k; r) = W^n(C_{k+1}; r)$, with $r_0(n) := 2$ and $r_{\lfloor n/2 \rfloor}(n) := 1$.)*

## Gate 1 Novelty Receipt
- **UTC timestamp:** 2026-11-26T22:54:09Z
- **Local snapshots (`tools/novelty_grep.py`):** `2603.08876`, `"LexiCut"`, `"isolated cuts"` returned 0 matches across `watch/snapshots/**`; `"Maric"` matched only unrelated `C. R. Marić` irrationality series and `Marica-Schönheim` in Mathlib.
- **GitHub & `trureturing` (`gh api`):** `search/issues?q=2603.08876`, `search/repositories?q=2603.08876`, `search/code?q=repo:the-omega-institute/trureturing+2603.08876`, and `search/commits?...` all returned `0`. `search/issues?q="isolated+cuts"+Max-Cut` returned 19 unrelated hits (top 10 checked, all software PRs/issues).
- **Web search (`search_web`):** Query `"2603.08876" OR "Hierarchical threshold structure in Max-Cut with geometric edge weights" proved OR disproved OR counterexample` returned only the original March 2026 preprint; conjecture remains open.
