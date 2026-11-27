---
source: arXiv:2112.05316v2 (Hemanshu Kaul, Michael Maxfield, Jeffrey A. Mudrock, Seth Thomason, "The DP Color Function of Clique-Gluings of Graphs", Section 1.3–1.4, Question 2 / `ques: classify` & Question 3 / `ques: easier`, lines 173–199; published in Enumerative Combinatorics and Applications 4 (2024))
status: reported
owner: scout-9
updated: 2026-11-27T10:23:00Z
attack_started_utc: 2026-11-27T10:18:57Z
identifiers: ["2112.05316", "2112.05316v2", "ques:easier", "ques:classify", "Question 3", "Question 2"]
---

# Kaul–Maxfield–Mudrock–Thomason (`arXiv:2112.05316v2`): Questions 2 & 3 ($p \ge 4$, $d_G(v) \ge 4$)

## Exact Statements (verbatim, `tools/.arxiv_cache/eprint/2112.05316/paper.tex`, lines 173–199)

> **Question 2** (`\label{ques: classify}`, citing [BH21]). If $p \ge 1$, $n \geq 2$, $G_1, \ldots, G_n$ are vertex disjoint graphs, and $G \in \bigoplus_{i=1}^{n}(G_i,p)$, is it the case that
> $$P_{DP}(G,m) \leq \frac{\prod_{i=1}^n P_{DP}(G_i,m)}{\left( \prod_{i=0}^{p-1} (m-i) \right)^{n-1}}$$
> for all $m \geq p$?

> **Question 3** (`\label{ques: easier}`, citing [DY21]). If $v$ is a simplicial vertex of $G$, is it true that for all positive integers $m \geq d_G(v)$, $P_{DP}(G,m) \leq (m- d_G(v)) P_{DP}(G - \{v\}, m)$?

Line 199 explicitly records the remaining open cases after the paper settles $p=2$ (yes) and $p=3$ (no):
> "While the answers to Questions~\ref{ques: classify} and~\ref{ques: easier} are unknown for each $p \geq 4$ and $d_G(v) \geq 4$ respectively, our result in Section~\ref{triangle} makes us suspect both questions have a negative answer for each of these values."

*(Note: `\newtheorem{ques}[thm]{Question}` shares the `[thm]` counter: Theorem 1 is `thm: evengirth`, Question 2 is `ques: classify`, Question 3 is `ques: easier`.)*

## Primary Definitions (`paper.tex`, Section 1.1–1.3, lines 132–179)

- All graphs are nonempty, finite, simple graphs.
- A *cover* of $G$ is a pair $\mathcal{H} = (L, H)$ where $\{L(u) : u \in V(G)\}$ partitions $V(H)$ into $|V(G)|$ cliques ($H[L(u)]$ complete), $E_H(L(u), L(v)) \neq \emptyset$ implies $u = v$ or $uv \in E(G)$, and $E_H(L(u), L(v))$ is a (possibly empty) matching whenever $uv \in E(G)$.
- $\mathcal{H}$ is *$m$-fold* if $|L(u)| = m$ for all $u \in V(G)$, and *full* if $E_H(L(u), L(v))$ is a perfect matching for every $uv \in E(G)$.
- An *$\mathcal{H}$-coloring* of $G$ is an independent set in $H$ of size $|V(G)|$; $P_{DP}(G, \mathcal{H})$ is the number of $\mathcal{H}$-colorings of $G$, and the *DP color function* is $P_{DP}(G, m) = \min_{\mathcal{H}} P_{DP}(G, \mathcal{H})$ over all $m$-fold covers $\mathcal{H}$ of $G$.
- $\mathcal{H}$ has a *canonical labeling* if $L(u) = \{(u, j) : j \in [m]\}$ can be chosen so $(u, j)(v, j) \in E(H)$ for all $j \in [m]$ whenever $uv \in E(G)$ (equivalently $P_{DP}(G, \mathcal{H}) = P(G, m)$ when full).
- $G \in \bigoplus_{i=1}^n (G_i, p)$ is a *$K_p$-gluing* of vertex-disjoint graphs $G_1, \dots, G_n$ along chosen copies of $K_p$ in each $G_i$. A vertex $v \in V(G)$ is *simplicial* if $d_G(v) = 0$ or $G[N_G(v)]$ is a complete graph (so for $d_G(v) = p \ge 1$, $G \in (G - \{v\}) \oplus_p K_{p+1}$).

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T10:18:35Z`
- `tools/novelty_grep.py "2112.05316"`: 0 hits across 0/618 files in `watch/snapshots/**`.
- `gh search issues "2112.05316"`: 0 hits.
- Zenodo API (`zenodo.org/api/records?q=2112.05316` and `"DP Color Function of Clique-Gluings"`): 0 hits.
- `tools/arxiv_fetch.py query 'all:"DP color function" AND (all:"gluing" OR all:"clique-gluing" OR all:"simplicial")'`: returned only `2610.13458v1` (hypergraph joins and vertex-gluings), `2112.05316v2` (the target paper), and `2104.12268v2` (earlier paper on $p=1$).
- OpenAlex (`doi:10.48550/arXiv.2112.05316`): `cited_by_count: 1`; `search_web` confirms the 2024 *Enumerative Combinatorics and Applications* publication without any resolution of the $p \ge 4$ / $d_G(v) \ge 4$ cases.
