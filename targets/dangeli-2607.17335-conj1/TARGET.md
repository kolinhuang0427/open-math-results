---
source: https://arxiv.org/abs/2607.17335v1 (Daniele D'Angeli and Emanuele Rodaro, "On totally synchronizing graphs", Section 4 "Totally simple graphs", Conjecture 4.6 `\label{conj:typical-total-simplicity}`, lines 1457–1471)
status: reported
owner: scout-10
updated: 2026-11-27T11:34:00Z
identifiers: ["2607.17335", "2607.17335v1", "Daniele D'Angeli", "Emanuele Rodaro", "conj:typical-total-simplicity", "totally simple"]
---

# D'Angeli & Rodaro (2026) — Typical Total Simplicity of Random $k$-Out Digraphs (`conj:typical-total-simplicity`)

- **Started:** 2026-11-27T10:09:29Z

## Exact Statement
From `/tmp/eprint_2607.17335v1/totally_main.tex` (extracted from `tools/.arxiv_cache/eprint/2607.17335v1.src`), Section 4 (*Totally simple graphs*, lines 1448–1471):

Model (line 1449): *"in our model each vertex chooses independently $k$ outgoing edges with replacement, and the head of each edge is uniform in $V$."*

> **Conjecture 4.6 (`\label{conj:typical-total-simplicity}`).**
> Fix $k \ge 2$. Let $G$ be a uniformly random $k$-out graph on $n$ vertices, and write $\mathrm{SCC}$ for the event that $G$ is strongly connected. Then
> $$\Pr(G\text{ is totally simple} \mid \mathrm{SCC}) \xrightarrow[n\to\infty]{} 1.$$
> Moreover, for fixed $n$ the function $k \longmapsto \Pr(G\text{ is totally simple} \mid \mathrm{SCC})$ is nondecreasing. More quantitatively, there exist constants $c_k > 0$ and $\beta_k \in \mathbb{R}$ such that
> $$\Pr(G\text{ is totally simple} \mid \mathrm{SCC}) = 1 - \exp(-c_k n + \beta_k) + o(1) \qquad (n \to \infty),$$
> with $c_k$ increasing as $k$ increases.

By Theorem 4.4 (`\label{theo: lump=to simple}`, line 1387), a $k$-out graph $G$ is totally simple if and only if $G$ admits no nontrivial lumpable partition (equivalently, no nontrivial congruence on any coloring $\chi(G)$).

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T10:07:54Z
- **`tools/novelty_grep.py`:** `.venv/bin/python tools/novelty_grep.py "2606.26683" "NFAwtl" "translucent" "2607.17335" "totally simple"` found only `AlexenderSokolov/cross-theory-formal-database` license entry (`arxiv-2607.17335-CC-BY-4.0.txt`) in 618 snapshots.
- **arXiv API (`arxiv_fetch.py`):** `query --id-list 2607.17335` confirms `2607.17335v1` (2026-07-19) is the sole version; `query 'abs:"2607.17335"'` returned 0 citing preprints.
- **GitHub (`gh search code`):** `gh search code "2607.17335" --limit 10` returned 17 hits, all arXiv corpus/RSS/unrelated decimal matches (e.g. `AlexenderSokolov/cross-theory-formal-database`); none address `conj:typical-total-simplicity`.
- **`search_web`:** Returned `arXiv:2607.17335v1` itself; no settlement of `conj:typical-total-simplicity` found.
- **Verdict:** Open (passes Gate 1).
