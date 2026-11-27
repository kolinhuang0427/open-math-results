---
source: "Ján Mináč, Tung T. Nguyen, and Nguyễn Duy Tân, 'Isomorphic gcd-graphs over polynomial rings', arXiv:2411.01768v2 (JAust_isomorphic_gcd_revised.tex), Section 5.2, Remark 5.14 (\\label{rem:same_degree}, L1095–1099)"
status: reported
owner: scout-11
created: 2026-11-27T10:27:46Z
updated: 2026-11-27T10:32:00Z
identifiers:
  - arXiv:2411.01768v2
  - "Remark 5.14 (rem:same_degree)"
  - gcd-graphs
  - polynomial rings
---

# Target: `minac-2411.01768-rem5.14`

- **Source:** Ján Mináč, Tung T. Nguyen, and Nguyễn Duy Tân, *"Isomorphic gcd-graphs over polynomial rings"*, `arXiv:2411.01768v2` (`JAust_isomorphic_gcd_revised.tex`, to appear in *The Journal of the Australian Mathematical Society*), Section 5 (*Isomorphic gcd-graphs*), Subsection 5.2, **Remark 5.14** (`\label{rem:same_degree}`, L1095–1099).

## Definitions (quoted from `arXiv:2411.01768v2`, Section 1, L268–278 & Section 2, L317)

> Let $A$ be a principal ideal domain and $n \in A$ which is not a unit. Suppose further that the ring $A/n$ is finite. Let $\mathrm{Div}(n)$ be the set of divisors of $n$ (defined up to associates) and $D \subset \mathrm{Div}(n)$ such that $n \not\in D.$ The gcd-graph $G_n(D)$ is the graph equipped with the following data:
> 1. The vertex set of $G_n(D)$ is $A/n.$
> 2. Two vertices $a, b \in A/n$ are adjacent if and only if $\gcd(a-b, n) \in D.$
>
> In other words, $G_n(D)$ is the Cayley graph on $A/n$ with the generating set $S_D = \{h \in A/n \mid \gcd(h, n) \in D\}$.

For $A = \mathbb{F}_q[x]$ and monic $f \in \mathbb{F}_q[x]$, $\mathrm{Div}(f)$ is the set of monic divisors of $f$ (`L317`).

## Verbatim Open Question (`arXiv:2411.01768v2`, Section 5.2, Remark 5.14, L1095–1099)

> **Remark 5.14** (`\label{rem:same_degree}`). A conjecture of So \cite[Conjecture 7.3]{so2006integral} says that if $n$ is an integer and $D_1, D_2$ are two distinct subsets of $\mathrm{Div}(n)$, then the two gcd-graphs over $\mathbb{Z}$, $G_n(D_1)$ and $G_n(D_2)$ are not isomorphic.
>
> As we have shown, this conjecture is not true if we consider gcd-graphs over $\mathbb{F}_q[x].$ We remark, however, that our constructions of isomorphic gcd-graphs of the form $G_{f}(D)$ where $f$ is fixed are based on a crucial fact that $f$ has two irreducible factors of the same degree. This could happen over $\mathbb{F}_q[x]$ but not over $\mathbb{Z}.$ As a result, we wonder whether So's conjecture still holds for the family $G_{f}(D)$ under the additional assumption that irreducible factors of $f$ have different degrees.

## Gate 1 Novelty Check Receipt (`2026-11-27T10:27Z`)

- `targets/` check: no existing `minac*`, `nguyen*`, or `2411.01768*` folder.
- `.venv/bin/python tools/novelty_grep.py "2411.01768" "2409.01929" "2611.15026" "rem:same_degree" "So's conjecture"`: `0` hits answering Remark 5.14 (`2611.15026v2` studies matrix rings $M_n(\mathbb{F}_q)$, not $\mathbb{F}_q[x]$; `2409.01929` is the authors' preceding `minavc2024gcd` paper).
- Semantic Scholar citing-paper check for `arXiv:2411.01768` (`citationCount = 4`: `2503.04086`, `2508.10348`, `2605.11445`, `2609.30407`) + `.src` grep of `2503.04086`, `2508.10348`, `2609.30407`: none address Remark 5.14 or distinct-degree polynomials over $\mathbb{F}_q[x]$.
- `tools/arxiv_fetch.py abs 2411.01768` + `search_web`: `2411.01768v2` (`2026-08-03`) is the latest version; Remark 5.14 remains open.
- Verdict: OPEN, clear to attack.
