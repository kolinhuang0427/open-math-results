# Adversarial Audit Report: `targets/ferrero-2511.16335-conj1.8/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T20:19Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"counterexample, verified by exact computation"` (for the explicit 12-vertex witness $C_6[2K_1] \cong \mathrm{Circ}(12, \{1,5\})$, supplemented by an internally audited analytic proof for the infinite family $C_6[r_0 K_1, \dots, r_5 K_1]$, $r_i \ge 2$). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py` (authored by `check-2` strictly from primary-source definitions, re-executed independently with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary source: `arXiv:2511.16335v1` (`tools/.arxiv_cache/eprint/2511.16335/NewFixedPropTime.tex`, entire manuscript lines 1–1393), plus direct verification of the published revised journal version in *Australasian Journal of Combinatorics*, Vol. 96(2) (2026), pp. 374–394 (revised 2 June 2026) via `notes/audit-helper-ferrero.md`.
- `targets/ferrero-2511.16335-conj1.8/TARGET.md`
- `targets/ferrero-2511.16335-conj1.8/COUNTEREXAMPLE.md`
- `targets/ferrero-2511.16335-conj1.8/notes/check-check-2.md` and `notes/check-check-2.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and our adversarial helper's literature/check report (`notes/audit-helper-ferrero.md`).

Author scratch notes (`notes/screen-*`) and the finder's `verify.py` were **not** read.

---

## 2. Primary-Source Statement & Definition Fidelity

Checked word-for-word against `NewFixedPropTime.tex` (`arXiv:2511.16335v1`) and confirmed verbatim in the June 2026 revised *Australasian Journal of Combinatorics* Vol. 96(2) PDF:

- **Graph convention (Section 1, line 307):** Simple undirected graph $G = (V(G), E(G))$, edge set consisting of 2-element subsets of $V(G)$.
- **Color change rule CCR-$\mathrm{Z}$ and propagation time (Section 1, lines 312, 319–326):** Simultaneous standard zero forcing rounds $B^{[0]} = B^{(0)} = B$, $B^{(i+1)} = \{w : \exists v \in B^{[i]} \text{ with } N_G(v) \setminus B^{[i]} = \{w\}\}$, $B^{[i+1]} = B^{[i]} \cup B^{(i+1)}$; for a forcing set $B$, $\mathrm{pt}(G, B) = \max\{p : B^{(p)} \ne \emptyset\}$.
- **Upper standard propagation time (Section 1, Definition 1.2, line 231; also line 264):** $\overline{\mathrm{PT}}(G)$ is the maximum of $\mathrm{pt}(G, B)$ over all *minimal* standard zero forcing sets $B$ of $G$. (Line 264 also notes $\overline{\mathrm{PT}}(G) = 1$ is equivalent to every proper forcing set $B \subsetneq V(G)$ having $\mathrm{pt}(G, B) = 1$.)
- **Standard fast join (Section 1, Definition 1.5, lines 275–276; Observation 4.1, lines 921–924):** A graph $G$ of order $n \ge 2$ is a *standard fast join* if $G \cong K_n$ or $G = \bigvee_{i=1}^t G_i$ where $t \ge 2$ and each $G_i \cong n_i K_1$ or $G_i \cong K_{n_i} \dot{\cup} K_{m_i}$ with $n_i, m_i \ge 2$. By Theorem 4.4 (line 973), every standard fast join satisfies $\mathrm{Z}(G) \ge n - 2$ and (when $G \not\cong K_n$) has disconnected complement $\overline{G}$.
- **Conjecture 1.8 (`\label{c:std}`, Section 1, lines 293–296):** *"Let $G$ be a connected graph. If $\overline{\mathrm{PT}}(G) = 1$, then $G$ is a standard fast join."*

No quantifier, hypothesis, edge-case, or definition drift exists between the primary source, `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-2.py`. No hidden hypothesis excludes $C_6[2K_1]$ (and Conjecture 1.8 explicitly concerns standard forcing $\overline{\mathrm{PT}}(G)$, distinct from PSD forcing Conjecture 1.7).

---

## 3. Adversarial Audit of the Explicit Counterexample and Infinite Family

### 3.1 Explicit Witness: $G = C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$

1. **Well-defined simple connected graph:** Vertex set $\mathbb{Z}/12\mathbb{Z}$, edges $\{i, i \pm 1 \bmod 12\}$ and $\{i, i \pm 5 \bmod 12\}$. Partitioning into $A_i = \{i, i+6\}$ ($i \in \mathbb{Z}/6\mathbb{Z}$) matches $C_6[2K_1]$ edge-for-edge (for $u \in \{i, i+6\}$, $\{u+1, u-5\} = \{i+1, i+7\} = A_{i+1}$ and $\{u-1, u+5\} = \{i-1, i+5\} = A_{i-1}$). Simple, 4-regular, bipartite, 12 vertices, 24 edges, Hamiltonian (hence connected).
2. **Not a standard fast join:** $G \not\cong K_{12}$ ($24 < 66$ edges). Its complement $\overline{G}$ is 7-regular on 12 vertices, hence connected (Dirac/degree condition $\delta(\overline{G}) = 7 \ge 12/2$, and directly diameter 2), so $G$ is not a nontrivial join of $t \ge 2$ nonempty graphs. Independently, $\mathrm{Z}(G) = 8 < 12 - 2 = 10$, violating the paper's own Theorem 4.4 necessary condition $\mathrm{Z}(G) \ge n - 2$.
3. **$\overline{\mathrm{PT}}(G) = 1$ (exact exhaustive computation):** Independent verifier `notes/check-check-2.py` implements Definition 1.2, Definition 1.5, and CCR-$\mathrm{Z}$ faithfully in exact integer/bitmask arithmetic (no floating point) and exhaustively evaluates all $2^{12} = 4096$ subsets of $V(G)$:
   - Total forcing sets: $361$ ($19^2$).
   - Minimal forcing sets: $144$ ($12^2$), all of cardinality $8$, so $\mathrm{Z}(G) = \overline{\mathrm{Z}}(G) = 8$ (hence minimal and minimum forcing sets coincide, eliminating any minimal-vs-minimum ambiguity).
   - Every proper forcing set $B \subsetneq V(G)$ has $\mathrm{pt}(G, B) = 1$; thus $\underline{\mathrm{PT}}(G) = \overline{\mathrm{PT}}(G) = 1$.
   - Re-execution output of `.venv/bin/python targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py` (0.378s, exit code 0): `PASS`.

### 3.2 Infinite Family Proof: $G = C_6[r_0 K_1, \dots, r_5 K_1]$ ($r_i \ge 2$)

Audited line-by-line with no gaps found:
1. **Connectedness & non-fast-join:** $C_6$ is connected and all $r_i \ge 2$, so $G$ is connected and $G \not\cong K_n$ (non-adjacent pair inside $A_0$). In $\overline{G}$, every $A_i$ is a clique and $A_i$ is completely joined to $A_j$ for $j \not\equiv i \pm 1 \pmod 6$; any non-adjacent pair $u \in A_i, v \in A_{i+1}$ has a common neighbor in $A_{i+3}$, so $\overline{G}$ is connected of diameter 2, proving $G$ is not a join and not a standard fast join.
2. **Propagation time analysis:** Let $B \subsetneq V(G)$ and $W = V(G) \setminus B \ne \emptyset$.
   - *Case 1 ($|W \cap A_i| \ge 2$):* Any two vertices in $W \cap A_i$ are independent twins with identical open neighborhood $A_{i-1} \cup A_{i+1}$, forming a standard fort (Observation 4.2(2) of the paper), so $B$ is not a forcing set.
   - *Case 2 ($|W \cap A_i| \le 1$ for all $i$):* Let $S = \{i \in \mathbb{Z}/6\mathbb{Z} : |W \cap A_i| = 1\} \ne \emptyset$ and $W \cap A_j = \{w_j\}$ for $j \in S$. Because $r_i \ge 2$, every part has $A_i \cap B \ne \emptyset$. For $u \in A_i \cap B$, $N_G(u) \cap W = (A_{i-1} \cap W) \cup (A_{i+1} \cap W)$ (disjoint since $i-1 \not\equiv i+1 \pmod 6$). Hence $w_j$ is forced in round 1 iff $j-2 \notin S$ or $j+2 \notin S$ (mod 6).
   - Partitioning $\mathbb{Z}/6\mathbb{Z}$ into $E = \{0,2,4\}$ and $O = \{1,3,5\}$, we have $\{j-2, j+2\} = E \setminus \{j\}$ for all $j \in E$ (and $O \setminus \{j\}$ for $j \in O$). Thus all of $S \cap E$ is forced in round 1 iff $E \not\subseteq S$ and none iff $E \subseteq S$, and symmetrically for $O$.
   - If $E \not\subseteq S$ and $O \not\subseteq S$, every vertex of $W$ is forced in round 1, giving $\mathrm{pt}(G, B) = 1$. Otherwise, the white set remaining after round 1 corresponds to $S' \in \{E, O, E \cup O\}$, in which every vertex of $G$ has $0$ or $2$ white neighbors in each of $E$-white and $O$-white (a standard fort); propagation stalls and $B$ is not a forcing set.
   - Consequently, $B$ is a minimal forcing set iff $S$ contains exactly 2 indices from $E$ and 2 from $O$, giving $\mathrm{Z}(G) = \overline{\mathrm{Z}}(G) = n - 4 < n$ and $\underline{\mathrm{PT}}(G) = \overline{\mathrm{PT}}(G) = 1$.
3. **Sharpness sanity checks (`audit-helper-ferrero.md`):** Exhaustive checks on $C_k[2K_1]$ ($4 \le k \le 8$) and $C_6[1,2,2,2,2,2]$ confirm $C_4[2K_1] \cong K_{4,4}$ is a fast join, $C_5[2K_1], C_7[2K_1], C_8[2K_1]$ have $\overline{\mathrm{PT}} \in \{2, 3\}$, and $C_6[1,2,2,2,2,2]$ has $\overline{\mathrm{PT}} = 2$, confirming both $k=6$ and $r_i \ge 2$ are sharp.

### 3.3 Minor Non-Blocking Observations

- The heading `## Explicit Smallest Witness` in `COUNTEREXAMPLE.md` refers to the smallest witness in the $C_6[r_0 K_1, \dots, r_5 K_1]$ ($r_i \ge 2$) family ($n = 12$). Global minimality over *all* connected graphs of order $n \le 11$ is neither proved nor claimed in the body text, and is not required to refute Conjecture 1.8.

---

## 4. Novelty Assessment (Gate 3 Clear)

- Gate 2 receipts (`novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`) all passed with no `CONTESTED.md`.
- Our adversarial helper closed the Gate 2 caveat regarding the journal version: the published revised PDF (*Australasian Journal of Combinatorics*, Vol. 96(2), 2026, pp. 374–394, revised 2 June 2026) retains Conjecture 1.8 verbatim with `cited_by_count: 0` in OpenAlex, and `the-omega-institute/trureturing#8371` closed `2026-09-16` as explicitly `terminal OPEN` with zero code/proof/counterexample artifacts.
- **Gate 3 Clear (pre-report window, `2026-11-26T20:20:58Z`–`20:21:30Z`):** All three watchers filed fresh live PASS receipts with zero `CONTESTED.md` matches: `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, and `notes/novelty-gate3-watch-6.md`. Ready for coordinator final verification.
