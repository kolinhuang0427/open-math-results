---
source: "arXiv:2606.12129v1, Section 8 (Middle orders and \\omega-sorting orders), Conjecture 8.7 (label cnj:Dtype)"
status: reported
owner: attack-5
updated: 2026-11-27T10:38:30Z
identifiers: ["arXiv:2606.12129v1", "cnj:Dtype", "D_n"]
---

# Target: Schwob (2026), arXiv:2606.12129v1, Conjecture 8.7 (`cnj:Dtype`)

## Source & Statement

Paper: *Middle orders: all distributive lattices between weak and Bruhat* by Ludovic Schwob (`arXiv:2606.12129v1`, 2026-06-10, `Middle_order.tex` lines 910–913, Section 8 `\section{Middle orders and $\omega$-sorting orders}`).

Exact statement (`cnj:Dtype`, lines 910–913):
```latex
\begin{cnj}
   \label{cnj:Dtype}
   All middle orders (and in particular distributive sorting orders) on $D_n$ are minuscule middle orders.
\end{cnj}
```

### Relevant Definitions (`arXiv:2606.12129v1`)
- **Middle order** (§1, §2): A distributive lattice on a finite Coxeter group $(W, S)$ refining the right weak order $(W, \le_R)$ and refined by the Bruhat order $(W, \le)$.
- **Minuscule middle order** (§7.1, Definition 7.1, lines 731–734): Let $(W, S)$ be a Weyl group, and let $s_{i_1}, \dots, s_{i_r}$ be a permutation of $S$ such that for all $1 \le k \le r$, $\alpha_{s_{i_k}}$ is a minuscule root of $W_{\{s_{i_k}, \dots, s_{i_r}\}}$. Minuscule middle orders are posets of the form
  $$(W, \le_{s_{i_1}, \dots, s_{i_r}}) := (W_J, \le_{s_{i_2}, \dots, s_{i_r}}) \times {}^J W$$
  where $J = S \setminus \{s_{i_1}\}$.
- **Sorting order** (§8, line 837): For a reduced word $\omega$ for $w_0$, $\mathbf{Sort}_\omega(W)$ orders $w \in W$ by inclusion of $\mathrm{sort}_\omega(w)$ (the index set of the lexicographically minimal subword of $\omega$ evaluating to $w$).
- Author's note (line 914): Verified by computer up to $B_5$ and $D_5$.

## Gate 1 Novelty Receipt (2026-11-27T09:18Z)
- `targets/` check: `ls targets/ | grep -iE 'schwob|2606.12129'` -> no existing target.
- `tools/novelty_grep.py 2606.12129` (all 600+ local snapshots): 0 hits.
- `tools/arxiv_fetch.py query --id-list 2606.12129`: `2606.12129v1` (2026-06-10) is latest; no journal_ref or DOI.
- `gh search issues` (`"2606.12129"`, `"distrisort"`, `"minuscule middle"`, `"Schwob" "middle"`): 0 matching issues (`#22269` checked and unrelated).
- `gh search repos "Middle orders"`: 0 matching repos (`maxilism/chip-firing-...` unrelated).
- Zenodo API (`zenodo.org/api/records?q=2606.12129` and `"Middle orders" "Schwob"`): 0 hits.
- Web search (`"2606.12129" OR "Ludovic Schwob" "Middle orders"`): returns only the primary arXiv:2606.12129 preprint; no follow-up or resolution found.

## Screening Log
- Started attack: `2026-11-27T09:18:00Z`.
- Completed screening: `2026-11-27T09:30:00Z` -> `status: screened` (see `notes/scout2-3-screen.md`). Exhaustive SAT + minuscule enumeration proves `cnj:Dtype` through $D_6$ (127 = 127 middle orders, $|W|=23{,}040$), plus 3 general reduction lemmas and exact trichotomy indicators $e_1,e_2,e_3$ at $u=(-1,-2,n,3,\dots,n-1)$.

## Attack Log & Candidate Deliverables (`attack-5`)
- Started full attack: `2026-11-27T09:56:06Z`.
- **Attack-phase live novelty receipt** (`2026-11-27T09:57Z–10:00Z`, CLEAR / OPEN): [notes/novelty-attack.md](file:///Users/kolinhuang/Documents/open-math/targets/schwob-2606.12129-conj8.7/notes/novelty-attack.md) — `0/618` local snapshot hits, OpenAlex `cited_by_count=0`, `arXiv:2606.12129v1` latest, `0` hits across Zenodo, GitHub (repos/issues/PRs/code), HAL, Crossref, and live web.
- **Complete proof** (`2026-11-27T10:38:30Z`, `status: reported`): [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/schwob-2606.12129-conj8.7/PROOF.md) — elementary, self-contained induction for all $n \ge 4$ (zero SAT, zero external citations beyond Schwob `arXiv:2606.12129v1` Prop 3.8, Prop 4.1, Thm 4.13, Def 7.1 and standard Coxeter facts in Björner–Brenti 2005).
- **Exact verification script**: [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/schwob-2606.12129-conj8.7/verify.py) — pure integer (AST-audited: zero floats, zero `/` divisions); `.venv/bin/python targets/schwob-2606.12129-conj8.7/verify.py` exits `0` and prints `PASS` (1.38s CPU).
