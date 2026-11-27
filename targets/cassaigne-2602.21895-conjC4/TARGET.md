source: https://arxiv.org/abs/2602.21895v1 (Julien Cassaigne, Bastián Espinoza, Michel Rigo, Manon Stipulanti, "Symbols frequencies in the Thue--Morse word in base 3/2 and related conjectures", Section 1.4 Conjecture (C_4), citing F. M. Dekking, and Section 7 Concluding remarks)
status: reported
owner: scout2-6
updated: 2026-11-27T03:58:00Z
identifiers: ["2602.21895", "2602.21895v1", "Cassaigne", "Espinoza", "Rigo", "Stipulanti", "Dekking", "A357448", "t_{3/2}", "Thue--Morse word in base 3/2", "C_4"]

# Cassaigne–Espinoza–Rigo–Stipulanti (2026) — Dekking Conjecture `(C_4)` for Factor Frequencies in $\mathbf{t}'$ and $\mathbf{t}_{3/2}$

- **Started:** 2026-11-27T03:41:45Z

## Exact Statement
From Julien Cassaigne, Bastián Espinoza, Michel Rigo, and Manon Stipulanti, *Symbols frequencies in the Thue--Morse word in base $3/2$ and related conjectures*, arXiv:2602.21895v1 (25 Feb 2026), Sections 1.3–1.4 and Section 7 (`merge_version.tex`, lines 362–417, 431–446, 485–496, 515, 2090–2121):

Let $\mathbf{t}_{3/2} = (t_n)_{n \ge 0} \in \{{\tt 0}, {\tt 1}\}^\mathbb{N}$ be the Thue--Morse word in base $3/2$, uniquely defined by $t_0 = {\tt 0}$ and the relations (eq. `eq:t32relations`):
$$t_{3n} = t_{3n+1} = t_{2n}, \qquad t_{3n+2} = 1 - t_{2n+1} \quad (\forall n \ge 0),$$
and let $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`A357448`, `lem:morphic_image`), where $\varphi({\tt 0}) = {\tt 010}$ and $\varphi({\tt 1}) = {\tt 101}$.

> **Conjecture $(C_4)$ (Dekking [DekTM], restated in Section 1.4, line 493, and Section 7, lines 2090–2121).**
> 1. Frequencies of all finite words $w \in \{{\tt 0}, {\tt 1}\}^*$ occurring in $\mathbf{t}'$ (and similarly in $\mathbf{t}_{3/2}$) exist.
> 2. Every word $w$ and its reversal $\widetilde{w}$ have the same frequency.

Note: Theorem `thm:existence_freqs_iff_mun_exist` in `2602.21895v1` settled $(C_4)$ **for single-letter symbols ($|w|=1$)** by proving $\mu_n(a,k) = 2^{-n-1}$ for all $n \ge 0, a \in \{{\tt 0}, {\tt 1}\}, k \in \mathbb{Z}$. All factor lengths $|w| \ge 2$ (including the explicit values $\text{freq}_{\mathbf{t}_{3/2}}({\tt 00}) = \text{freq}_{\mathbf{t}_{3/2}}({\tt 11}) = 3/10$, $\text{freq}_{\mathbf{t}_{3/2}}({\tt 01}) = \text{freq}_{\mathbf{t}_{3/2}}({\tt 10}) = 2/10$, and $\text{freq}_{\mathbf{t}'}({\tt 01}) = 4/10$ noted experimentally in Section 7, lines 2116–2121) and reversal symmetry of factor frequencies remain open.

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T03:47:30Z
- **Local `novelty_grep.py`:** `.venv/bin/python tools/novelty_grep.py "2602.21895" "Espinoza" "Stipulanti" "A357448" "t_{3/2}"` across 470 files in `watch/snapshots/**` returned 0 hits for `2602.21895`, `Espinoza`, `Stipulanti`, `A357448`, `t_{3/2}` (4 unrelated hits for `3/2` in `ArtificialZeng__AI-Has-Taste`).
- **arXiv:** `arxiv_fetch.py query --id-list 2602.21895` confirms `2602.21895v1` (2026-02-25) is the sole version; query `abs:2602.21895 OR abs:A357448` returned 0 citing preprints.
- **GitHub (`gh search code` across required repos):**
  - `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`: 0 hits.
  - `the-omega-institute/trureturing*`: 1 hit in `the-omega-institute/trureturing/Problems/dekking-keane-2022-two-block-thue-morse-frequency.md`, which settles ONLY single-letter frequency $1/2$ for a *different* 2-block substitution (`arXiv:2202.13548v1`) and explicitly states *"Frequencies of longer factors remain open."*
- **Zenodo:** `https://zenodo.org/api/records?q=2602.21895` returned 0 hits.
- **`search_web`:** Returned `2602.21895v1` itself and OEIS `A357448` (citing conjectured block frequencies `00: 1/10`, `01: 4/10`). No proof of factor frequencies for $|w| \ge 2$ or reversal-symmetry of frequencies found.
- **What was not covered:** Papers/repos not indexed by arXiv API, Zenodo, GitHub code search, Google web search, or `watch/snapshots/**` as of 2026-11-27T03:47Z.
- **Verdict:** Open for $|w| \ge 2$ and reversal-invariance of factor frequencies (passes Gate 1).
