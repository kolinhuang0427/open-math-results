---
source: arXiv:2512.08168v2
status: reported
owner: attack-2
updated: 2026-11-27T05:29:30Z
identifiers:
  - arXiv:2512.08168v2
  - conj:union-intersection
---

# Conjecture 1.3 (`conj:union-intersection`) of Gaetz–Gao (arXiv:2512.08168v2)

**Primary Source:** Christian Gaetz and Yibo Gao, *"Billey--Postnikov posets, rationally smooth Schubert varieties, and Poincar\'e duality"*, `arXiv:2512.08168v2` (submitted 9 Dec 2025, revised 8 Jun 2026, `math.CO`), Section 1.1 (`main.tex` lines 113–116) and Section 2.1 (`main.tex` lines 194–205).

## Definitions (`main.tex` lines 192–205)

Let $(W, S)$ be a Coxeter group with length function $\ell$, Bruhat order $\le$, left descent set $D_L(u) := \{s \in S \mid \ell(su) < \ell(u)\}$, support $\mathrm{Supp}(u) := \{s \in S \mid s \le u\}$, and parabolic decomposition $w = w^J w_J$ ($w^J \in W^J$, $w_J \in W_J$).

> **Definition (`def:BP`, lines 194–201):** A parabolic decomposition $w=w^Jw_J$ is called a *Billey--Postnikov* decomposition, or *BP* decomposition, if
> $$\mathrm{Supp}(w^J)\cap J\subset D_L(w_J).$$
> In this case, we also say that $w$ is *BP at* $J$.

For any $w \in W$, $\mathrm{BP}(w) := \{J \subset S \mid w = w^J w_J \text{ is a Billey--Postnikov decomposition}\}$.

## Exact Verbatim Conjecture Statement (`main.tex` lines 113–116)

> **Conjecture (`conj:union-intersection`):** Let $W$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K, J \cup K \in \mathrm{BP}(w)$.

*(Known cases in primary source: all finite Weyl groups by Theorem 1.2, and all Coxeter groups of rank at most three by Theorem 3.7 / Section 3.3.)*

## Gate 1 Novelty Receipt

- **Checked at:** `2026-11-26T21:43:45Z`–`21:45:45Z`
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py "2512.08168" "conj:union-intersection" "BP(w)"` -> 0 hits matching `2512.08168` or `BP(w)` (`watch/snapshots/arxiv/index.md` lists Gaetz–Gao's later paper `2611.33572v1`, *Reflection subgroups and the Lookup Conjecture*, 2026-11-25, unrelated topic).
- **arXiv:** `tools/arxiv_fetch.py query "all:2512.08168 OR all:\"Billey--Postnikov poset\""` -> only `2512.08168v2` (updated 2026-06-08). `main.tex` proves `conj:union-intersection` only for finite Weyl groups and rank $\le 3$.
- **Web (`search_web`):** Query `"Billey--Postnikov posets, rationally smooth Schubert varieties" OR ("BP(w)" "Gaetz" "Gao")` -> returned only `arXiv:2512.08168` summary.
- **Near misses / what was not covered:** Follow-up papers citing `2512.08168` not indexed under the exact title/author strings or off-arXiv theses are not covered.
