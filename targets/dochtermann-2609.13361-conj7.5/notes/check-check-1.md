# Independent Check Report — `dochtermann-2609.13361-conj7.5`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, and Yuchen Xu, *Matroids with cycle systems are regular*, `arXiv:2609.13361v1` (`tools/.arxiv_cache/eprint/2609.13361/cyclesystem_reg.tex`).
- **Exact numbering & verbatim match:**
  - Section 7 (`\section{Further questions}`, L1030): **Conjecture 7.4** (`\label{conj:unique}`, L1057–1059) and **Conjecture 7.5** (`\label{conj:C>=3 ind}`, L1063–1065; preceded by Questions 7.1–7.3 at L1036–1052) match `TARGET.md` and `PROOF.md` verbatim.
  - All invoked results match `cyclesystem_reg.tex` verbatim in numbering and hypotheses: Definitions 2.13–2.14 (L449–479), Proposition 2.19 (`prop:del-con cs`, L504–518), Lemma 2.21 (`lem:circuitsys`, L531–534), Theorem 2.22 (`thm:components`, L538–543), Theorem 4.3 (`thm:cycle system binary`, L706), Lemma 6.4 (`lem:reachable to D`, L952–970), Definition 6.6 (L994–996), Proposition 6.7 (`prop:C>=3`, L1000–1008), Example 6.8 (`ex:C>=3`, L1012–1016).
  - Checked Corollary 1 carefully: `lem:reachable to D` preserves disjointness of $\mathcal{C}^D \subseteq \mathcal{C}$ from all $*$-deleted elements $\{e_1, \dots, e_m\}$, so when $\mathcal{C}$ is a circuit system, $\mathcal{C}^D$ remains a **circuit system** on $M^D$ with total unique union $D \in \mathrm{Cir}(M^D)$, avoiding any gap when invoking the Main Theorem + Proposition 6.7.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/dochtermann-2609.13361-conj7.5/notes/check-check-1.py` (pure-integer $\mathbb{F}_2$ bitmask linear algebra, `AST_FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: []`, exit code `0`, `PASS`):

1. **Necklace Case-2 stress test (`PROOF.md` §4 Remark):** On the 6-vertex, 9-edge planar necklace graph ($g = 4$, $\mathcal{C}_{[4]} = D \in \mathrm{Cir}(M)$), verified $M / x$ has 2 connected components for **every** $x \in D$, checked Lemma 2 rank equalities $r_M(E_1) = r_M(E_1 \cup \{x\}) = r(W_1) + 1$, `thm:components` block alignment $D \setminus \{x\} \subseteq E(W_k)$ & $C_1 \subseteq E(W_1) \cup \{x\}$, Lemma 3 circuit $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$, $*$-deletion $\mathcal{C}'_{[3]} = D \triangle C_1$, Corollary 1 (`conj:unique`), and Corollary 2 reconstruction.
2. **Graphic, cographic, disconnected, and necessity checks:**
   - Verified `39` circuit systems across $M(K_4)$ and cographic matroids $M(G)^*$ ($K_4^*, K_{2,3}^*, W_4^*, K_{3,3}^*, K_5^*$, including exhaustive enumeration over all circuit systems of $K_4^*$ and $K_{2,3}^*$): every step of Case 1 / Case 2 reduction, $\mathcal{C}_{\ge 3} = \emptyset$, Corollary 1 uniqueness, and Corollary 2 graph reconstruction $M = M(G)^*$ verified exact.
   - Verified Corollary 1 on the cone system of $M(K_5)$ (where $\mathcal{C}_{[6]} \notin \mathrm{Cir}(M(K_5))$), Step 1 disconnected reduction on $M(K_4) \oplus U_{1,1}^2$ (with coloops), and `Example 6.8` ($U_{1,6}$ necessity counterexample when $\mathcal{C}_{[g]} \notin \mathrm{Cir}$).

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-6.md` (`PASS`).
