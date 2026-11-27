---
source: arXiv:2201.08490v3 (Emily Gullerud, Rita Johnson, and aBa Mbirika, "Tridiagonal real symmetric matrices with a connection to Pascal's triangle and the Fibonacci sequence", Section 5.1, Conjecture 5.4 / `conj:ellipse`, lines 1171–1173)
status: reported
owner: scout-9
updated: 2026-11-27T11:20:00Z
attack_started_utc: 2026-11-27T11:00:38Z
identifiers: ["2201.08490", "2201.08490v3", "conj:ellipse", "Conjecture 5.4"]
---

# Gullerud–Johnson–Mbirika (`arXiv:2201.08490v3`): Conjecture 5.4 (`conj:ellipse`)

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2201.08490/Aug_2023_version_of_Tridiagonal_paper.tex`, lines 1171–1173)

> **Conjecture 5.4** (`\label{conj:ellipse}`). The roots of $f_{n}(\lambda) = F_{n+1}$ lie on an ellipse.

*(Note: the companion Conjecture 5.5 at lines 1179–1187 regarding unbounded real parts was already disproved in `arXiv:2510.02008v1/v2` (Davis–Farnsworth, $n \equiv 0 \pmod 4$) and `arXiv:2611.21142v1` (Oyengo, all $n \ge 1$), both of which explicitly left Conjecture 5.4 (`conj:ellipse`) open. This target is scoped strictly to Conjecture 5.4.)*

*(Numbering verified from `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}` at lines 45–48, following Question 5.1, Question 5.2, and Theorem 5.3 in Section 5.)*

## Primary Definitions (`Aug_2023_version_of_Tridiagonal_paper.tex`, Sections 1–3, lines 180–310, 750–785, 1133)

- $A_n$ is the $n \times n$ tridiagonal real symmetric matrix with $0$ on the main diagonal and $1$ on the superdiagonal and subdiagonal (`Definition 2.4` / `Section 2`, line 274).
- $f_n(\lambda) = \det(A_n - \lambda I_n)$ (`Definition 2.6`, line 309), satisfying the closed form (line 213) and recurrence (line 215):
  $$f_n(\lambda) = \sum_{i=0}^{\lfloor n/2 \rfloor} (-1)^{n+i} \binom{n-i}{i} \lambda^{n-2i}, \qquad f_n(\lambda) = -\lambda f_{n-1}(\lambda) - f_{n-2}(\lambda),$$
  with $f_0(\lambda) = 1$, $f_1(\lambda) = -\lambda$, $f_2(\lambda) = \lambda^2 - 1$, and $f_n(\lambda) = U_n(-\lambda/2)$ (line 785).
- $\{F_n\}_{n=0}^\infty = \{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \dots\}$ is the Fibonacci sequence (line 1133).

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T11:00:38Z`
- `tools/novelty_grep.py "2201.08490"`: 0 hits across `watch/snapshots/**`.
- `tools/arxiv_fetch.py abs 2201.08490` and `query`: latest version is `arXiv:2201.08490v3` (`2023-08-21`), unpublished (`journal_ref=""`, `doi=""`).
- `gh search issues "2201.08490"` (0 hits) and `gh search issues "Gullerud"` (0 hits); `gh search issues "Mbirika"` returned only unrelated targets (`mbirika-2204.12626-ques6.1`, `mbirika-2301.05758-ques30`, etc.).
- Zenodo API (`zenodo.org/api/records?q=2201.08490`): 0 hits.
- OpenAlex (`works/https://arxiv.org/abs/2201.08490` and title search): no matching journal publication or citations; `search_web` confirms Conjectures 5.4 and 5.5 remain open.
