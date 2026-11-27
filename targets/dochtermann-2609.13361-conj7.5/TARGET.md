---
source: "arXiv:2609.13361v1, Section 7 (Further questions), Conjecture 7.5 (label conj:C>=3 ind)"
status: reported
owner: attack-5
updated: 2026-11-27T12:11:00Z
identifiers: ["arXiv:2609.13361v1", "conj:C>=3 ind", "circuit-system"]
---

# Target: Dochtermann, Huang, Mawhinney, Oh, Xu (2026), arXiv:2609.13361v1, Conjecture 7.5 (`conj:C>=3 ind`)

## Source & Statement

Paper: *Matroids with cycle systems are regular* by Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, and Yuchen Xu (`arXiv:2609.13361v1`, 2026-09-11, `cyclesystem_reg.tex` lines 1063–1065, Section 7 `\section{Further questions}`).

Exact statement (`conj:C>=3 ind`, lines 1063–1065; also stated in §1 lines 221–224):
```latex
\begin{conjecture}\label{conj:C>=3 ind}
    Let $M$ be a matroid with circuit system $\mathcal{C}$, where $\mathcal{C}_{[g]}$ is a circuit. Then $\mathcal{C}_{\ge 3}$ is independent.
\end{conjecture}
```

### Relevant Definitions (`arXiv:2509.11460` / `arXiv:2609.13361v1`)
- **Unique union** (Definition 2.13, `def:uniqueunion`): For $\mathcal{C} = \{C_1, \dots, C_g\}$ and $\sigma \subseteq [g]$, $\mathcal{C}_\sigma = *\{C_i : i \in \sigma\}$ is the set of elements appearing in **exactly one** $C_i$ for $i \in \sigma$.
- **Circuit system** (Definition 2.14): $\mathcal{C} = \{C_1, \dots, C_g\}$ is a collection of $g = g(M) := |E(M)| - \mathrm{rk}(M)$ circuits of $M$ such that for every nonempty $\sigma \subseteq [g]$, $\mathcal{C}_\sigma$ is dependent in $M$. (By Theorem 4.3 / Theorem 5.8 of `2609.13361v1`, any matroid admitting a cycle system is binary and in fact regular.)
- **$\mathcal{C}_{\ge 3}$**: The set of elements of $E(M)$ appearing in at least $3$ distinct circuits of $\mathcal{C}$ (line 219, Definition 6.6 line 994).
- By Proposition 6.7 (`prop:C>=3`) / Theorem 6.9 (`thm:sufficient unique`), Conjecture 7.5 implies Conjecture 7.4 (`conj:unique`: unique-union representations of circuits are unique).

## Gate 1 Novelty Receipt (2026-11-27T09:49Z)
- `targets/` check: `ls targets/ | grep -iE '2609.13361|dochtermann|cyclesystem'` -> no existing target.
- `tools/novelty_grep.py 2609.13361`: hits only `tamnd__arxiv` index; 0 resolution hits across 608 snapshots.
- `tools/arxiv_fetch.py query --id-list 2609.13361`: `2609.13361v1` (2026-09-11) is latest; no journal_ref or DOI.
- `gh search issues "2609.13361"`: 0 hits.
- Zenodo API (`zenodo.org/api/records?q=2609.13361`): 0 hits.
- Web search (`"2609.13361" OR ("Matroids with cycle systems are regular" "conjecture")`): returns only `2609.13361v1`.

## Screening Log
- Started attack: `2026-11-27T09:49:30Z`.
- Completed screening: `2026-11-27T10:06:00Z` -> `status: screened` (see `notes/scout2-3-screen.md`). Exhaustively verified across 5,883 graphic/multigraph circuit systems with circuit $\mathcal{C}_{[g]}$ ($n \le 7, g \le 7$) plus $M^*(K_{3,3}), M^*(K_5), M^*(K_6), R_{10}$ and 401,800 $T+D$ candidates: 0 counterexamples and $\mathcal{C}_{\ge 3} = \emptyset$ in every instance; proved connectedness, $\mathbb{F}_2$-parity, and $[g] \setminus S_D^{\min}$ reductions.

## Attack Log & Candidate Deliverables (`attack-5`)
- Started full attack: `2026-11-27T11:42:55Z`.
- **Attack-phase live novelty receipt** (`2026-11-27T11:46:41Z`, OPEN / CLEAR): [notes/novelty-attack.md](file:///Users/kolinhuang/Documents/open-math/targets/dochtermann-2609.13361-conj7.5/notes/novelty-attack.md) — `0/658` snapshot resolution hits, `arXiv:2609.13361v1` & `2509.11460v1` latest, near-miss `2609.17446v2` inspected (`0` mentions of circuit systems or `conj:C>=3 ind`), Zenodo/HAL/DataCite/GitHub repos & issues/web clear.
- **Complete proof** (`2026-11-27T11:59:30Z`, `status: candidate`): [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/dochtermann-2609.13361-conj7.5/PROOF.md) — proves the strictly stronger Main Theorem that $\mathcal{C}_{\ge 3} = \emptyset$ for every matroid $M$ with circuit system $\mathcal{C}$ and $\mathcal{C}_{[g]} \in \mathrm{Cir}(M)$ via strong induction on $|E(M)|$ (binary linear independence + contraction $M/x$ splitting into Case 1 connected `lem:circuitsys` vs. Case 2 disconnected `thm:components` + parallel-connection circuit elimination $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$ + $*$-deletion). Immediately resolves **Conjecture 7.5** (`conj:C>=3 ind`), **Conjecture 7.4** (`conj:unique`), and yields a complete cographic vertex-star characterization (Corollary 2).
- **Exact verification script**: [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/dochtermann-2609.13361-conj7.5/verify.py) — pure integer (AST-audited: zero floats, zero `/` divisions); `.venv/bin/python -u targets/dochtermann-2609.13361-conj7.5/verify.py` exits `0` and prints `PASS` (9.3s).
