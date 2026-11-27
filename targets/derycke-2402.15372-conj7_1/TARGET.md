---
source: arXiv:2402.15372v3 (Section 6, Conjecture 6.1 / conj:ITCCTIsymmetry)
status: reported
owner: attack-3
updated: 2026-11-27T09:42:00Z
identifiers: ["2402.15372", "2402.15372v3", "Derycke", "Dukes", "Le Borgne", "CTI", "ITC", "ITCCTIsymmetry", "complete split graph", "sawtooth polyominoes"]
---

# Derycke–Dukes–Le Borgne (arXiv:2402.15372v3): Conjecture 6.1 (`conj:ITCCTIsymmetry`)

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2402.15372/qtss1.tex`, lines 946–958, 1016–1020, 1044–1055, and 2659–2669)

On the complete split graph $S_{n,d}$ (with clique $V = \{v_1,\ldots,v_n\}$ plus sink $s=v_0$, and independent set $W = \{w_1,\ldots,w_d\}$), $\mathcal{R}_{\mathrm{dec}}(S_{n,d})$ (`\ClassOneParams{n}{d}`) is the set of sorted recurrent sandpile configurations $c = (a_1,\ldots,a_n; b_1,\ldots,b_d)$ with $a_1 \ge \cdots \ge a_n$ and $b_1 \ge \cdots \ge b_d$.
For $c \in \mathcal{R}_{\mathrm{dec}}(S_{n,d})$, $\mathrm{level}(c) = \mathrm{height}(c) - \bigl(\binom{n+d}{2} - \binom{d}{2}\bigr)$, and:
\[
\mathfrak{F}_{n,d}^{\mathrm{CTI}}(q,t) := \sum_{c \in \mathcal{R}_{\mathrm{dec}}(S_{n,d})} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{CTI}}(c)-(n+d)},
\qquad
\mathfrak{F}_{n,d}^{\mathrm{ITC}}(q,t) := \sum_{c \in \mathcal{R}_{\mathrm{dec}}(S_{n,d})} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{ITC}}(c)-(n+d)}.
\]

> `\begin{conjecture}\label{conj:ITCCTIsymmetry}`
> `$\displaystyle \notrepoly_{n,d}^{CTI}(q,t) = \notrepoly_{n,d}^{ITC}(q,t).$`
> `\end{conjecture}`

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T09:05:00Z`
- `tools/novelty_grep.py` (queries: `2402.15372`, `Derycke`, `ITC`, `CTI`): 0 hits across 601 files in `watch/snapshots/**`.
- `gh search issues` (`"2402.15372"`, `"Derycke"`, `"sawtooth polyominoes"`): 0 matching issues.
- Zenodo API (`2402.15372 OR sawtooth polyominoes OR CTI ITC`): 0 matching records.
- `search_web` (`"sandpile model on the complete split graph" "CTI" "ITC"`): returns only arXiv:2402.15372 itself. No resolution found.

## Screening Log

- Attack started UTC: `2026-11-27T09:05:00Z`
