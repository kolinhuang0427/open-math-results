---
source: arXiv:2603.29978v2
status: reported
owner: attack-1
updated: 2026-11-27T05:35:00Z
identifiers:
  - arXiv:2603.29978v2
  - 2603.29978
  - Ragunathan
  - Van Tuyl
  - Conjecture 6.1
  - vdw(n,k)
  - A(vdw(n,k))
  - van der Waerden simplicial complex
---

# Conjecture 6.1 (`conjecture`) of Ragunathan–Van Tuyl (arXiv:2603.29978v2)

**Primary Source:** Naveena Ragunathan and Adam Van Tuyl, *"The van der Waerden Simplicial Complex and its Lefschetz Properties"*, `arXiv:2603.29978v2` (submitted 31 Mar 2026, revised 19 Aug 2026, `math.AC`), Section 6 (`van_der_Waerden_complex_and_the_Lefschetz_Properties_final.tex` lines 1384–1393).

## Definitions (`lines 173–195, 511–529`)

- ${\tt vdw}(n,k)$ ($n > k \ge 1$) is the pure $k$-dimensional simplicial complex on vertex set $[n] = \{1,\ldots,n\}$ whose facets are the $(k+1)$-element arithmetic progressions $\{i, i+d, i+2d, \dots, i+kd\} \subseteq [n]$ ($d \ge 1$, called "arithmetic progressions of length $k$" in the paper, where $k$ is the number of jumps; lines 511–529).
- $A({\tt vdw}(n,k)) := K[x_1,\ldots,x_n]/(I_{{\tt vdw}(n,k)} + \langle x_1^2,\ldots,x_n^2\rangle)$, where $I_{{\tt vdw}(n,k)}$ is the Stanley–Reisner ideal of ${\tt vdw}(n,k)$.
- $A({\tt vdw}(n,k))$ has the *Weak Lefschetz Property* (WLP) over $K$ if for a general linear form $\ell$, multiplication $\times \ell : A_i \to A_{i+1}$ has maximal rank $\min(\dim_K A_i, \dim_K A_{i+1})$ for all $i$. (In characteristic 0, by Migliore–Miró-Roig–Nagel, it suffices to test $\ell = x_1 + \cdots + x_n$.)

## Exact Verbatim Conjecture Statement (`lines 1384–1393`)

> **Conjecture 6.1 (`conjecture`):** Suppose ${\rm char}(K) = 0$. Fix an integer $k \geq 3$.
> 1. If $k$ is odd, then there exists an $m$ such that $A({\tt vdw}(n,k))$ fails to have the WLP for $n \geq m$.
> 2. If $k$ is even, then $A({\tt vdw}(n,k))$ has the WLP for all $n > k$.

*(The paper also remarks at lines 1406–1409 that for odd $3 \le k \le 11$, the smallest failing $n$ observed was $7, 12, 15, 20, 23$.)*

## Gate 1 Novelty Receipt

- **Checked at:** `2026-11-26T23:28:30Z`–`23:29:57Z`
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py 2603.29978 Ragunathan "Van Tuyl" "vdw(n,k)" "van der Waerden simplicial"` -> 0 hits.
- **arXiv:** `.venv/bin/python tools/arxiv_fetch.py query 'all:2603.29978 OR all:"van der Waerden simplicial"'` -> only `2603.29978v2` (updated 2026-08-19).
- **Zenodo API:** `https://zenodo.org/api/records?q=%222603.29978%22+OR+%22van+der+Waerden+simplicial%22` -> 0 hits.
- **GitHub (`gh search` & `gh api`):** `gh search repos "2603.29978"` (0), `gh search code "2603.29978"` (RSS feeds / non-math LIO-SAM timestamp false positives), `gh search code "vdw(n,k)"` (`chy4pro/automath` archive brief listing it as an open arXiv entry; `inventor1975/ZTL` unrelated SAT file), `aliromman/math/contents/conjectures` (no match).
- **Web (`search_web`):** Query `"2603.29978" OR "The van der Waerden Simplicial Complex and its Lefschetz Properties" OR ("vdw(n,k)" "WLP")` -> returned only `arXiv:2603.29978` summaries.
- **Not covered:** Off-arXiv theses, papers not mentioning `2603.29978` or `vdw(n,k)`, private repositories.
