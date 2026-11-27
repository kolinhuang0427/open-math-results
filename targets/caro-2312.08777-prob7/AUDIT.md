# Blind Independent Audit Report — `targets/caro-2312.08777-prob7/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2312.08777/{flip_graphs.tex,sections/section1.tex,sections/section6.tex,sections/section7.tex}`, `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-2.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *"Flip colouring of graphs"*, `arXiv:2312.08777v1` (`2023-12-14`, verified sole arXiv version via live `tools/arxiv_fetch.py query --id-list 2312.08777 --no-cache`; published in *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 6 (`sections/section6.tex`) & Section 7 final Problem (`sections/section7.tex` L44–49, 7th `\begin{problem*}`).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all blocking and minor fixes from initial FAIL `#1822` were cleanly applied in `PROOF.md`; publication label: **"written proof, internally audited"**).

---

## 1. Primary Source & Statement Fidelity Check

Verified verbatim against `tools/.arxiv_cache/eprint/2312.08777/`:
- **Notation & regularity conventions (`sections/section1.tex` L14–35, `sections/section6.tex` L5–22):** Finite simple graphs; strictly increasing positive integer sequence $(a_1, \dots, a_k)$ (so $1 \le b < r$); $N_t[v] = \{u \in V(G) : d_G(u, v) \le t\}$; $e_{j, s}[v] = |E(j) \cap E(N_s[v])|$; $([t], (a_1, \dots, a_k))$-flip graph requires $\deg_j(v) = a_j$ and $e_{j, s}[v] < e_{i, s}[v]$ for all $v \in V(G)$, $1 \le i < j \le k$, $1 \le s \le t$. Matches `TARGET.md` L14–18 verbatim.
- **Erdős–Sachs citation (`sections/section6.tex` L89–91):** `\begin{theorem}\label{ErdosSachs}` is **Theorem 6.2** (after Theorem 6.1 `CayleyTFlip` at L40), matching `PROOF.md` L41 verbatim.
- **Open problem (`sections/section7.tex` L44–49):** 7th `\begin{problem*}`: *"In particular, define $b(t) = \min\{b : ([t], (b, r))\text{-flip graph exists}\}$. Observe that for $t \ge 2$, the proof of Theorem \ref{CayleyTFlip} gives $b(t) \le 2^{t+1} - 1$. **Problem.** For $t \in \mathbb{N}, t \ge 2$ determine $b(t)$."* Matches `TARGET.md` L22–26 verbatim.
- **`TARGET.md` fidelity:** **PASS** (zero defects).

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Section 1 (L11–31) — Lower Bound $b(t) \ge 3$:** Core double-counting proof is **SOUND** ($e_{1,1}[v] = b + e_B(v)$, $e_{2,1}[v] = r + e_R(v)$, global triangle-type identities $2\sum_v T_{RRB}(v) = \sum_v T_{BRR}(v)$ and $2\sum_v T_{BBR}(v) = \sum_v T_{BRB}(v)$, yielding $\sum_v (e_B(v) - e_R(v)) \le \sum_v (T_{BBB}(v) + T_{BBR}(v)) \le |V|\binom{b}{2}$, hence $r - b < \binom{b}{2} \implies b + 1 \le r \le \binom{b+1}{2} - 1$, impossible for $b \in \{1, 2\}$).
  - **BLOCKING DEFECT (`PROOF.md` L19):** L19 writes:
    > *(treating $BRR = RBR$ and $BBR = BRB$ as the same type)*
    Under the definition in L19 ($X, Y$ are the two edges incident to $v$ and $Z$ is the edge opposite $v$), swapping the two incident edges identifies $BRR = RBR$ and **$BRB = RBB$** — NOT $BBR = BRB$! Indeed, $T_{BBR}(v)$ (incident $B, B$, opposite $R$) and $T_{BRB}(v)$ (incident $B, R$, opposite $B$) are distinct types in L20–22 satisfying $2\sum_v T_{BBR}(v) = \sum_v T_{BRB}(v)$. Fix to `(treating $BRR = RBR$ and $BRB = RBB$ as the same type)`.
- **Section 2.1 (L37–50) — Base Graph & $K_4$-Blow-Up:** **SOUND.** Erdős–Sachs (Theorem 6.2) guarantees a finite connected $16$-regular simple graph $H$ with $g(H) \ge 2t + 2$; replacing vertices by blue $K_4$ cliques $C_x$ and lifting each $xy \in E(H)$ via 4-edge partitions $E_x(1), \dots, E_x(4)$ produces a finite connected simple graph $G$ with $E(1) \cap E(2) = \emptyset$ and $(\deg_1, \deg_2) = (3, 4)$ at every vertex.
- **Section 2.2 (L52–67) — Claims 1 & 2:** **SOUND.**
  - Claim 1: $g(H) \ge 2t + 2$ guarantees $T_{x_0} = H[B_H(x_0, t)]$ is an induced tree (any non-BFS edge inside $B_H(x_0, t)$ would close a cycle of length $\le 2t + 1 < g(H)$), and every length-$\le t$ path in $G$ from $v$ projects into $T_{x_0}$.
  - Claim 2: Uniqueness of the bridge $p(x)x$ in the induced tree $T_{x_0}$ forces every length-$\le t$ path to $u \in C_x$ ($x \ne x_0$) to cross $e_x$ through $x^*$, yielding $d_G(v, u) = d_G(v, x^*) + \mathbf{1}_{u \ne x^*}$ and $d_G(v, x^*) = d_G(v, (p(x), i_x)) + 1$. Consequently, for $1 \le s \le t$, $C_x$ contributes either all $6$ blue edges (iff $x^* \in N_{s-1}[v]$) or $0$ blue edges (if $d_G(v, x^*) \ge s$) to $G[N_s[v]]$, and the red edges of $G[N_s[v]]$ are precisely the lifts $e_x$ with $(p(x), i_x) \in N_{s-1}[v]$ and $x^* \in N_s[v]$.
- **Section 2.3 (L68–103) — Layer Recurrence & Induction:** **SOUND.**
  - Verified exact layer counts $A_1 = 4, B_1 = 3$, $A_{s+1} = 3 A_s + 4 B_s$, $B_{s+1} = 3 A_s$ ($1 \le s \le t - 1$), exact edge increments $e_{1, s+1}[v] - e_{1, s}[v] = 6 A_s$, $e_{2, s+1}[v] - e_{2, s}[v] = 3 A_s + 4 B_s$, base cases $e_{1,1}[v] = 6 > 4 = e_{2,1}[v]$ and $e_{1,2}[v] = 30 > 28 = e_{2,2}[v]$, and inductive invariant $5 A_{s-1} \le A_s \le 6 A_{s-1}$ giving $\Delta e_1 - \Delta e_2 = 3 A_s - 12 A_{s-1} \ge 3 A_{s-1} > 0$ for all $2 \le s \le t - 1$.
  - **Minor polish (non-blocking, fix alongside L19):**
    - L74: remove scratch phrasing `"Wait: "` and `"!"` (`Notice that every vertex $u \in L_s$ ... lie in $B_H(x_0, t) = V(T_{x_0})$.`).
    - L93–95: restrict `for all $s \ge 2$` / `($s \ge 2$)` to `for all $2 \le s \le t$` / `($2 \le s \le t - 1$)` to match the domain $1 \le s \le t$ of $A_s, B_s$.

---

## 3. Independent Verifier Audit (`notes/check-check-2.py`)

- Re-executed `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py`: exited `0`, raw stdout:
  - `[PASS] Primary source arXiv:2312.08777v1 verbatim statement & definitions verified.`
  - `[PASS] Lower bound b(t) >= 3 algebra & triangle identities verified.`
  - `[PASS] Layer recurrence & e_{1,s} > e_{2,s} verified in exact ints for 1 <= s <= 200.`
  - `[PASS] Explicit ([1],(3,4)) (128v), ([2],(3,4)) (2048v), and ([3],(3,4)) (34952v, sampled 203v) verified.`
  - `PASS`
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Verified file MD5s at initial audit:
  - `TARGET.md`: `ba0f83276f2a31423f32ac58db3e99a1`
  - `PROOF.md`: `7444a1c11e293acf0a8e4d3fc61df6e9`
  - `notes/check-check-2.md`: `9044782377b9bcdac92bc3e7d0e557ff`
  - `notes/check-check-2.py`: `2917a3247218e4fc6e2f8ed23d5d92dc`
- Verifier logic inspected line-by-line (L1–532): **PASS** (no changes needed to `check-check-2.{md,py}`).

---

## 4. Gate 2 Novelty Status

- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`2026-11-27T17:58Z`–`17:59Z`, `0/760` snapshot hits, `2312.08777v1` sole arXiv version, all citing preprints `2401.02315`, `2403.04401`, `2507.14473`, `2602.23517`, `2609.37978` verified unrelated to $b(t)$ for $t \ge 2$, GH/Zenodo/HexagonMath/Papex/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

Following `@scout-9` (`#1827`), `@audit-2` re-verified the patched `PROOF.md` verbatim on disk and re-executed the independent verifier:

1. **Blocking Defect resolved (`PROOF.md` L19):** Updated to `(treating $BRR = RBR$ and $BRB = RBB$ as the same type)`, matching the triangle-type definitions and global double-count in L20–22.
2. **Minor polish resolved (`PROOF.md` L74 & L93–95):** Removed `"Wait: "` / `"!"` at L74, and restricted the inductive invariant to `for all $2 \le s \le t$` / `($2 \le s \le t - 1$)`.
3. **Final independent re-run by `@audit-2`:**
   - Command: `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py` -> exit `0`, raw stdout:
     - `[PASS] Primary source arXiv:2312.08777v1 verbatim statement & definitions verified.`
     - `[PASS] Lower bound b(t) >= 3 algebra & triangle identities verified.`
     - `[PASS] Layer recurrence & e_{1,s} > e_{2,s} verified in exact ints for 1 <= s <= 200.`
     - `[PASS] Explicit ([1],(3,4)) (128v), ([2],(3,4)) (2048v), and ([3],(3,4)) (34952v, sampled 203v) verified.`
     - `PASS`
   - AST zero-float check: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
   - Verified file MD5s: `TARGET.md` `ba0f83276f2a31423f32ac58db3e99a1`, `PROOF.md` `79c57f3637da49d023ab368abbf1e1cd`, `notes/check-check-2.md` `9044782377b9bcdac92bc3e7d0e557ff`, `notes/check-check-2.py` `2917a3247218e4fc6e2f8ed23d5d92dc`.

**Final Verdict: PASS** (publication label: **"written proof, internally audited"**). Handing off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`) prior to coordinator reporting.
