# Independent Blind Audit — `dochtermann-2609.13361-conj7.5`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (`written proof, internally audited`; after Re-Audit #1 of `#1395` patch — initial audit was FAIL on Lemma 1 L49–51 and Corollary 2 L19, both now cleanly resolved; see §6)
- **Audited Files (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2609.13361/cyclesystem_reg.tex` (`arXiv:2609.13361v1`, confirmed latest via live arXiv query), `targets/dochtermann-2609.13361-conj7.5/TARGET.md`, `targets/dochtermann-2609.13361-conj7.5/PROOF.md`, `targets/dochtermann-2609.13361-conj7.5/notes/check-check-1.{md,py}`. Author `verify.py` and scratch notes were not read.

---

## 1. Primary-Source & Numbering Fidelity (`arXiv:2609.13361v1`)

- **Latest Version:** Live arXiv query confirms `2609.13361v1` (`2026-09-11`, Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, Yuchen Xu, *Matroids with cycle systems are regular*) is the sole version (`journal_ref: ""`, `doi: ""`).
- **Compiled Numbering & Verbatim Match (`cyclesystem_reg.tex`):** All theorem-like environments share the `[theorem]` counter per `\section` (L23–58). Parsed every environment across all 7 sections and verified verbatim matches for every citation in `TARGET.md` and `PROOF.md`:
  - Definitions 2.13 (`def:uniqueunion`, L449) & 2.14 (L459), Proposition 2.19 (`prop:del-con cs`, L504), Lemma 2.21 (`lem:circuitsys`, L531), Theorem 2.22 (`thm:components`, L538), Theorem 4.3 (`thm:cycle system binary`, L706), Lemma 6.4 (`lem:reachable to D`, L952), Definition 6.6 (L994), Proposition 6.7 (`prop:C>=3`, L1000), Example 6.8 (`ex:C>=3`, L1012), Theorem 6.9 (`thm:sufficient unique`, L1020), **Conjecture 7.4** (`conj:unique`, L1057–1059), and **Conjecture 7.5** (`conj:C>=3 ind`, L1063–1065).
- **Local Snapshot Check:** `grep -rnE "2609\.13361|dochtermann|C>=3 ind|circuit system" watch/snapshots/` hits only `tamnd__arxiv.json` bibliographic index (`0` settlement hits). Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all report PASS.

---

## 2. Blocking Defects in `PROOF.md`

### Blocking Defect 1 — Lemma 1 (`PROOF.md` L49–51) is literally false as stated for general cycle systems on disconnected binary matroids

`PROOF.md` L49–51 states:
> **Lemma 1 (Linear independence of cycle systems in binary matroids).** *Let $N$ be a binary matroid with cycle system $\mathcal{E} = \{E_1, \dots, E_g\}$. Then the indicator vectors of $E_1, \dots, E_g$ are linearly independent over $\mathbb{F}_2$ (hence form an $\mathbb{F}_2$-basis of $\mathcal{Z}(N)$).*
> *Proof.* ... Thus $E_1, \dots, E_g$ are linearly independent in $\mathcal{Z}(N)$, and since $|\mathcal{E}| = g(N) \ge \dim_{\mathbb{F}_2} \mathcal{Z}(N)$, they form a basis of $\mathcal{Z}(N)$.

In `cyclesystem_reg.tex` L266 (and `PROOF.md` L28), a **cycle** is defined as an arbitrary **union** of circuits, *not* necessarily a disjoint union of circuits. On a disconnected binary matroid $N$, a member $E_i$ of a cycle system $\mathcal{E}$ need **not** belong to the circuit space $\mathcal{Z}(N)$ (which is precisely why `cyclesystem_reg.tex` Corollary 4.4 `cor:circuit basis` L718–724 requires $M$ to be connected and first invokes `lem:circuitsys` to ensure every $C_i$ is a circuit).

**Explicit counterexample (verified computationally):** Take the graphic (hence binary) matroid $N = M(K_4 \setminus e) \oplus M(C_3)$ of corank $g = 3$, where $K_4 \setminus e$ has edges $e_0=(0,1), e_1=(1,2), e_2=(2,3), e_3=(3,0), e_4=(0,2)$ with triangles $C_1 = \{e_0, e_1, e_4\}$, $C_2 = \{e_2, e_3, e_4\}$, and $C_3 = \{e_5, e_6, e_7\}$. Set $E_1 = C_1$, $E_2 = C_2$, and $E_3 = C_3 \cup C_1 \cup C_2$ (all $8$ edges). Every $E_i$ is a union of circuits, and every nonempty unique union $\mathcal{E}_S$ contains either $C_3$ (when $3 \in S$) or one of $C_1, C_2, C_1 \triangle C_2$ (when $3 \notin S$), so $\mathcal{E} = \{E_1, E_2, E_3\}$ is a valid cycle system on $N$. Yet $E_3 \notin \mathcal{Z}(N)$ because vertices $0$ and $2$ have odd degree $3$ in $E_3 \cap E(K_4 \setminus e)$ (`xor(cols in E3) = 0b101 != 0`). Thus $\mathcal{E}$ is not contained in $\mathcal{Z}(N)$ and is not a basis of $\mathcal{Z}(N)$.

- **Required fix (`PROOF.md` L49–51):** Split/restrict Lemma 1 cleanly: (a) for any binary matroid $N$ and cycle system $\mathcal{E} = \{E_1, \dots, E_g\}$, the indicator vectors of $E_1, \dots, E_g$ are linearly independent in $\mathbb{F}_2^{E(N)}$; (b) if $\mathcal{E}$ is a **circuit system** (so every $E_i \in \mathrm{Cir}(N) \subseteq \mathcal{Z}(N)$), then $\mathcal{E}$ forms an $\mathbb{F}_2$-basis of $\mathcal{Z}(N)$. Notice every invocation of Lemma 1 in `PROOF.md` (Step 1 L87, Step 2 Case 2(3) L117, Corollary 2 L141/L143) already applies Lemma 1 exclusively to a circuit system $\mathcal{C}$, so the rest of the proof is unaffected.

### Blocking Defect 2 — Corollary 2 (`PROOF.md` L19) quantifier ambiguity under Whitney $2$-switching

`PROOF.md` L19 states:
> *...if and only if $M$ is cographic ($M \cong M(G)^*$ for a connected graph $G$ on $g + 1$ vertices with no self-loops), in which case $\mathcal{C}$ is necessarily the canonical vertex-star system $\{\delta_G(v) : v \in V(G) \setminus \{q\}\}$ for some sink vertex $q \in V(G)$ with $\delta_G(q) = D$.*

This phrasing can be read as fixing a graph realization $G$ of $M$ first and asserting that every such $\mathcal{C}$ is a vertex-star system of *that* $G$. For $2$-connected non-$3$-connected $G$, that reading is false under Whitney $2$-switching: e.g., $G_1$ on $\{0,1,2,3\}$ with edges $(0,2),(0,2),(1,2),(0,3),(0,3),(1,3)$ (vertex star sizes $4, 2, 3, 3$) and its $2$-switch $G_2$ with edges $(0,2),(0,2),(1,2),(1,3),(1,3),(0,3)$ (vertex star sizes $3, 3, 3, 3$) satisfy $M(G_1)^* = M(G_2)^*$; the vertex-star circuit system of $G_2$ satisfies $\mathcal{C}_{[3]} \in \mathrm{Cir}(M(G_1)^*)$ but is not a vertex-star system of $G_1$.

- **Required fix (`PROOF.md` L19):** Make the quantifier order unambiguous so $G$ depends on $\mathcal{C}$ (matching what L141–145 actually proves): *"if and only if $M$ is cographic; moreover, for every such circuit system $\mathcal{C}$, there exists a connected loopless graph $G$ on $g + 1$ vertices with $M \cong M(G)^*$ and a sink vertex $q \in V(G)$ such that $\mathcal{C} = \{\delta_G(v) : v \in V(G) \setminus \{q\}\}$ and $\delta_G(q) = D$."*

---

## 3. Non-Blocking Polish (Fix in the Same Patch)

- **`PROOF.md` L40 & L105:** Replace $K_C \subseteq \bigoplus_{t=1}^{j-1} E(W_t)$ with $K_C \subseteq \bigsqcup_{t=1}^{j-1} E(W_t)$ (ground-set disjoint union rather than the matroid direct-sum symbol on sets).

---

## 4. Verification of Core Proof & Independent Checker

Aside from the two statement defects in §2, every step of the proof was verified line-by-line and found **100% mathematically sound**:
- **Lemma 2 (L53–65):** Rank connectedness criterion, absence of loops/coloops in $M$ and coloops in $M/x$ for connected $M$ with $g \ge 2$, and $C \setminus \{x\} \in \mathrm{Cir}(M/x)$ for non-loop $x \in C$. **Verified.**
- **Lemma 3 (L67–77):** Parallel-connection circuit elimination $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$ via binary $\mathcal{Z}(M)$ symmetric difference. **Verified.**
- **Main Theorem (§4, L83–130):** Strong induction on $|E(M)|$, base case $g = 1$, Step 1 disconnected reduction (valid for circuit systems since every $C \in \mathcal{C}$ lies in a single component $M_j$ and $\mathcal{C}^{(j)} \subseteq \mathcal{Z}(M_j)$), Step 2 contraction at $x \in D$, Case 1 (`lem:circuitsys`), and Case 2 items 1–5 (`thm:components`, $g(W_j) \ge 1$, $D \setminus \{x\} \subseteq E(W_k)$, rank equality $r_M(E_1) = r_M(E_1 \cup \{x\}) = r(W_1) + 1$ forcing $1 \in I_1$ via $\dim_{\mathbb{F}_2}\mathcal{Z}(M|E_1) \le g(W_1) - 1$, Lemma 3 giving $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$, and $*$-deletion $\mathcal{C}'_{[g-1]} = D \triangle C_1$ forcing $C_1 \cap \mathcal{C}_{\ge 3} = \emptyset$ and $\mathcal{C}'_{\ge 3} = \mathcal{C}_{\ge 3}$). **Verified.**
- **Corollary 1 (L138, Conjecture 7.4 `conj:unique`):** Checked that every $*$-deleted element $e_t$ in `lem:reachable to D` is disjoint from every $C \in \mathcal{C}^D$, so $\mathcal{C}^D$ remains a circuit system on $M^D$ with total unique union $D \in \mathrm{Cir}(M^D)$, allowing Main Theorem + Proposition 6.7 (`prop:C>=3`). **Verified.**
- **Corollary 2 (L140–145):** Verified both directions including all $g = 1$ edge cases (single loop $U_{0,1} = M(K_2)^*$ and dipole $U_{r, r+1}$) and $g \ge 2$ ($2$-connected loopless $G$). **Verified** (under the corrected quantifier order in §2).
- **Independent Checker (`notes/check-check-1.py`):** AST-verified (`floats: []`, `float_calls: []`, `divs: []`) and executed `.venv/bin/python -u targets/dochtermann-2609.13361-conj7.5/notes/check-check-1.py` -> exit `0`, raw `PASS` (`test_necklace_stress`, `39` circuit systems across graphic/cographic matroids, $K_5$ cone Corollary 1, disconnected+coloops, Example 6.8). No changes needed to `check-check-1.py`.

---

## 5. Handoff

**FAIL** — returning to `@attack-5` and `@triage` to patch the two statement defects in `PROOF.md` (L49–51 Lemma 1; L19 Corollary 2 quantifier order; plus L40/L105 `$\bigsqcup$` tidy) and ping `@audit-3` for quick re-audit.

---

## 6. Re-Audit #1 Following `#1395` Patch (`2026-11-27T12:08Z`) — **PASS**

Re-read `targets/dochtermann-2609.13361-conj7.5/PROOF.md` in full (`160` lines):
- **Blocking Defect 1 (`PROOF.md` L49–56, Lemma 1) — RESOLVED:** Split cleanly into (1) $\mathbb{F}_2^{E(N)}$ linear independence for arbitrary cycle systems and (2) $\mathbb{F}_2$-basis of $\mathcal{Z}(N)$ for circuit systems on binary matroids, with all downstream citations updated (`L92`, `L122`, `L146`, `L148`).
- **Blocking Defect 2 (`PROOF.md` L19, Corollary 2) — RESOLVED:** Quantifier order fixed so that for every such circuit system $\mathcal{C}$, there exist a connected loopless graph $G$ on $g + 1$ vertices with edge set $E(M)$ satisfying $M = M(G)^*$ and a sink vertex $q \in V(G)$ with $\mathcal{C} = \{\delta_G(v) : v \in V(G) \setminus \{q\}\}$ and $\delta_G(q) = D$ (immune to Whitney $2$-switching).
- **Non-Blocking Polish (`PROOF.md` L40, L110) — RESOLVED:** Updated $\bigoplus \to \bigsqcup$ on ground sets.
- **Independent Verifier (`notes/check-check-1.py`, unchanged):** Previously executed (`exit 0`, raw `PASS`, zero floats, zero `/` divisions).

**Final Verdict:** **PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 freshness check (`<1h`), instructing them to mention `@coordinator` on PASS with verifier command `.venv/bin/python -u targets/dochtermann-2609.13361-conj7.5/notes/check-check-1.py` and paths `targets/dochtermann-2609.13361-conj7.5/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
