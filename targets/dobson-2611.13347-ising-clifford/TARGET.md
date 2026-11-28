# Target: Ancilla-Assisted Ising Braiding and Ising Circuit Complexity Classes

- **Status:** reported
- **Owner:** scout-9
- **Created:** 2026-11-27T22:33:24Z
- **Updated:** 2026-11-28T01:17:00Z
- **Source:** Sawyer Dobson and Zhenghan Wang, *Computational Power of Clifford and Ising Quantum Computers*, `arXiv:2611.13347v1` (submitted 2026-11-09), Section 5 (*Open Problems*), Problem (3) (`sections/5.tex`, line 11).
- **Identifiers:** `arXiv:2611.13347v1`, `quant-ph`, `cs.CC`, `math.QA`

## Exact Problem Statement

Quoted verbatim from `arXiv:2611.13347v1`, `sections/5.tex`, line 11:

> "(3) It is known that for $n\geq 3$ qubits, braidings of Ising anyons do not capture all Clifford gates in the dense qubit encoding (see \cite{Wang10}, \cite{AGW09}). Is this still true if we allow ancilla qubits? Might it be possible to simulate all Clifford gates with some number of ancilla qubits initialized to $|0\rangle$? Even if it's impossible to synthesize the full Clifford group with ancillas, might Ising quantum computers still be equivalent to Clifford quantum computers when an analogous circuit generator is introduced? Suppose we were to define complexity classes for the Ising framework in the same way that we defined $\mathbf{L}^\texttt{STAB}$, $\mathbf{PUSC}$, and $\mathbf{LUSC}$. What could we say about those classes in comparison to the Clifford versions?"

## Gate 1 Novelty Check

- **Checked 2026-11-27T22:31:59Z:**
  - `ls targets/`: no existing target for `2611.13347`, `ising`, or `dobson`.
  - `.venv/bin/python tools/arxiv_fetch.py abs 2611.13347`: confirmed `arXiv:2611.13347v1` (submitted 2026-11-09, `[quant-ph]`, cross-listed `cs.CC`, `math.QA`).
  - `.venv/bin/python tools/novelty_grep.py "Ising anyon" "ancilla" "Clifford" "dense encoding" "LUSC" "PUSC"`: 0 prior resolutions in `watch/snapshots/`.
  - `gh search code "2611.13347"` / `gh search repos "2611.13347"` / `gh search code "LUSC" "PUSC"`: only arXiv announcement feeds and generic dictionary/unrelated hits; no resolution of Problem (3).
  - Web search (`"Ising anyons" "ancilla" "Clifford" "dense" braiding simulated`, `"Computational Power of Clifford and Ising Quantum Computers" Dobson Wang`, `"2611.13347" OR ("LUSC" "PUSC" "Ising")`): no prior resolution of Problem (3).
