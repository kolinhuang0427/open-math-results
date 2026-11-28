# Check Report: `targets/dobson-2611.13347-ising-clifford/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2611.13347v1` (`sections/5.tex` L11 Problem (3); `sections/4.tex` L32–66, L113–240; `sections/3.tex` L13–112; `sections/2.tex` L366, L420; `main.tex` L16–20)
- **Gate 2 Receipts:** `watch-1` (`#2092`), `watch-5` (`#2093`), `watch-6` (`#2094`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` reproduces `sections/5.tex` L11 Problem (3) verbatim, and `PROOF.md` cites exact section/counter numbers (`Definitions 3.1, 3.4, 3.8` at L83, `Proposition 3.7` at L101) and `(-i)^{m+1}` parity sign (L25, L41).
2. **Proof review (`PROOF.md`):** Verified Majorana algebra and weight invariance (Lemma 1.1), $\ket{0^a}$-ancilla no-go for Clifford simulation on $n \ge 3$ under both standard and arbitrary wire placements (Theorems 2.2 & 2.3), $\texttt{ISING-BRAID} \in \mathbf{L}$ and unconditional strict separations $\mathbf{LUSB} \subsetneq \mathbf{LUSC}$ and $\mathbf{PUSB} \subsetneq \mathbf{PUSC}$ (Theorems 3.1 & 3.2), and exact $1$-ancilla measurement-assisted Clifford universality + log-space equivalence $\mathbf{L}^{\texttt{ISING-MEAS-PAULI}} = \mathbf{L}^{\texttt{STAB}} = \oplus\mathbf{L}$, $\mathbf{PUSI} = \mathbf{PUSC}$, $\mathbf{LUSI} = \mathbf{LUSC}$ (Theorem 4.1 & Corollary 4.2).
3. **Independent exact $\mathbb{Q}(\zeta_{16})$ verifier (`notes/check-check-1.py`):**

```text
$ .venv/bin/python -u targets/dobson-2611.13347-ising-clifford/notes/check-check-1.py
MAJORANA_AND_NOGO: PASS
ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS
ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS
PASS
EXIT:0
AST_FLOATS: []
FLOAT_CALLS: []
```
