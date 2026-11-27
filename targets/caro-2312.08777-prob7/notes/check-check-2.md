# Independent Check Report (`@check-2`): `targets/caro-2312.08777-prob7/`

**Verdict:** `PASS`

## 1. Primary Source & Restatement Verification
- **Primary source:** `tools/.arxiv_cache/eprint/2312.08777/sections/section1.tex`, `section6.tex`, `section7.tex` (`arXiv:2312.08777v1`, Caro–Lauri–Mifsud–Yuster–Zarb, *Flip colouring of graphs*).
- **Match check:** `TARGET.md` quotes the $t$-neighbourhood flip graph definition (`section6.tex`) and the final Problem (`section7.tex`, unnumbered `problem*`, Problem 7 of Section 7: *"For $t \in \mathbb{N}, t \geq 2$ determine $b(t)$"*) verbatim, matching all quantifiers, positive-integer regularity conventions (`section1.tex`), and definitions.
- **`PROOF.md` review:**
  - **Lower bound ($b(t) \ge 3$):** Sound self-contained proof evaluating $e_{2,1}[v] < e_{1,1}[v]$ at $s=1$ and summing the triangle-type identity over $v \in V$ to obtain $r - b < \binom{b}{2}$, ruling out $b = 1, 2$ for all $t \ge 1$.
  - **Upper bound ($b(t) \le 3$):** Erdős–Sachs (`Theorem 6.2`) gives a finite connected $16$-regular simple graph $H$ of girth $g(H) \ge 2t + 2$; replacing vertices by $K_4$ cliques (colour $1$) and partitioning the $16$ incident edges at each vertex into four $4$-edge classes (colour $2$) yields a simple $(3,4)$-regular graph $G$. Claims 1–2 establish the exact local tree structure of $B_H(x_0, t)$ and entry-vertex decomposition $L_s = A_s \sqcup B_s$ ($1 \le s \le t$) with recurrence $A_{s+1} = 3A_s + 4B_s$, $B_{s+1} = 3A_s$ ($A_1=4, B_1=3$), proving $5 A_{s-1} \le A_s \le 6 A_{s-1}$ ($s \ge 2$) and hence $e_{1,s}[v] > e_{2,s}[v]$ for all $1 \le s \le t$.

## 2. Independent Exact Verifier (`notes/check-check-2.py`)
- **Methodology:** Zero-floating-point Python (`int` and `fractions.Fraction` only), written directly from `arXiv:2312.08777v1` and `PROOF.md`.
- **Checks performed:**
  1. Verbatim source comparison against `section1.tex`, `section6.tex`, `section7.tex`, and `TARGET.md`.
  2. Exact triangle-counting identity and inequality $T_{BBB}(v) + T_{BBR}(v) \le \binom{b}{2}$ on explicit $2$-edge-coloured regular graphs, plus algebraic elimination for $b \in \{1, 2\}$.
  3. Exact integer & `Fraction` verification of the recurrence $A_{s+1}, B_{s+1}$, invariant $5 A_{s-1} \le A_s \le 6 A_{s-1}$, and $e_{1,s}[v] > e_{2,s}[v]$ across $1 \le s \le 200$.
  4. Full explicit $K_4$-blow-up graph verification across three finite $16$-regular base graphs:
     - $t = 1$: $K_{16,16}$ ($32$ vertices, girth $4$) $\to 128$-vertex $([1],(3,4))$-flip graph (3 seeds, all $128$ vertices checked).
     - $t = 2$: $\mathrm{AG}(2,16)$ point-line incidence graph minus vertical parallel class ($512$ vertices, girth $6$) $\to 2048$-vertex $([2],(3,4))$-flip graph (2 seeds, all $2048$ vertices checked).
     - $t = 3$: symplectic generalized quadrangle $W(16)$ minus a Hopcroft–Karp $1$-factor ($8738$ vertices, girth $\ge 8$ checked on $204$ sampled vertices) $\to 34952$-vertex $([3],(3,4))$-flip graph ($203$ sampled vertices checked).
- **Run command & output:**
  ```text
  .venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py
  [PASS] Primary source arXiv:2312.08777v1 verbatim statement & definitions verified.
  [PASS] Lower bound b(t) >= 3 algebra & triangle identities verified.
  [PASS] Layer recurrence & e_{1,s} > e_{2,s} verified in exact ints for 1 <= s <= 200.
  [PASS] Explicit ([1],(3,4)) (128v), ([2],(3,4)) (2048v), and ([3],(3,4)) (34952v, sampled 203v) verified.
  PASS
  ```
  (Exit code `0`.)

## 3. Gate Status
- Gate 1: `PASS` (recorded in `TARGET.md`).
- Gate 2: `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-6.md`).
