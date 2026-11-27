---
source: arXiv:2303.17804v1 (math.CO) / Discrete Mathematics 347(2) (2024), Article 113778 (DOI 10.1016/j.disc.2023.113778), Section 1, Conjecture (`conj*`)
status: reported
owner: attack-1
updated: 2026-11-27T11:26:00Z
identifiers:
  - arXiv:2303.17804v1
  - egan-2303.17804-conj1
  - Egan-Nikolayevsky
  - triangular realisation
---

# Target: Egan–Nikolayevsky (2023) `arXiv:2303.17804v1`, Conjecture 1

## Start Time
- **Screening started (UTC):** `2026-11-27T09:04:25Z`

## Verbatim Statement

From `tools/.arxiv_cache/eprint/2303.17804/main.tex` (Section 1 `\section{Introduction}`, lines 80–82 `\begin{conj*}`):

> **Conjecture.** Any graphical sequence all of whose terms are greater than or equal to $4$ admits a triangular realisation.

Primary definitions (`tools/.arxiv_cache/eprint/2303.17804/main.tex`, Section 1, lines 76–78):
- **Graph / Degree sequence / Graphical / Realisation** (line 76): All graphs are finite and simple (no loops, no multiple edges). A sequence $d = (d_1, d_2, \dots, d_n)$ of nonnegative integers is the degree sequence of $G$ if $V(G) = \{v_1, \dots, v_n\}$ with $\deg(v_i) = d_i$. $d$ is *graphic* (*graphical*) if there exists a graph $G$ whose degree sequence is $d$; any such graph is a *realisation* of $d$ (connectedness is not required).
- **Triangular graph** (line 78): A graph is *triangular* if every edge of it belongs to a $3$-cycle (triangle).

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T09:04:25Z`
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py 2303.17804 "triangular realisation" "triangular realization" "biregular degree"` returned `0` matching lines across 601 files.
- **Existing targets:** No `targets/*2303.17804*` or `targets/*egan*` (for this paper) folder existed prior to claim.
- **arXiv API (`tools/arxiv_fetch.py`):**
  - `query("", id_list="2303.17804")`: latest version is `2303.17804v1` (2023-03-31; published in *Discrete Mathematics* 347(2), Feb 2024).
  - `query('all:"triangular realisation" OR all:"triangular realization"')`: returned `2303.17804v1` and unrelated `2610.32521v1`.
- **GitHub (`gh search`):** `gh search repos "2303.17804"` returned 0 results.
- **Web searches (`search_web`):**
  - `"triangular" "degree sequence" "greater than or equal to 4" OR "2303.17804" conjecture`
  - `"Egan" "Nikolayevsky" "triangular" degree sequence 2024 OR 2025 OR 2026`
  - Found Talbot–Yan (2024, EJC) on triangular multigraphs; the simple-graph Egan–Nikolayevsky conjecture remains open.
- **Coverage note:** Non-indexed private repos or papers not indexing `2303.17804` / `potentially triangular` are not covered.
