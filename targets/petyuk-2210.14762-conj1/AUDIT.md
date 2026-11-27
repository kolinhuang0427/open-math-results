# Adversarial Audit Report: `targets/petyuk-2210.14762-conj1/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T02:58Z`
- **Target:** Anthony V. Petyuk, *"On word-representability of simplified de Bruijn graphs"*, `arXiv:2210.14762v2` (`2023-07-12`), Section 4, Conjecture 1
- **Owner:** `scout-9`
- **Checker:** `check-1` (`notes/check-check-1.md`, `notes/check-check-1.py`)
- **Audit Helper:** `petyuk-audit-hlp` (`notes/audit-helper-petyuk.md`, killed)
- **Strict Isolation Observed:** Read ONLY the primary source (`tools/.arxiv_cache/eprint/2210.14762/simplified_de_Bruijn_graphs__4_.tex`), `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and `notes/audit-helper-petyuk.md`. Did NOT read author `verify.py` or any author scratch notes (`notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, etc.). Did NOT edit `TARGET.md` or `COUNTEREXAMPLE.md`.
- **Verdict:** **PASS** *(subject to prominent prior-art disclosure in §4 below and Gate 3 novelty clearance)*
- **Charter Label:** `"counterexample, verified by exact computation"`

---

## 1. Primary-Source Statement Fidelity

Verified directly against `tools/.arxiv_cache/eprint/2210.14762/simplified_de_Bruijn_graphs__4_.tex` and arXiv metadata (`notes/audit-helper-petyuk.md` §1):
- **Primary source:** `arXiv:2210.14762v2` (`2023-07-12`, latest version, unpublished in journals per Crossref/OpenAlex/web).
- **Definition of $S(n, k)$ (§1.2, lines 65–67):** Simple undirected graph obtained from the $n$-dimensional de Bruijn graph $B(n, k)$ over a $k$-letter alphabet by removing all self-loops, replacing directed arcs by undirected edges, and merging parallel edges. Thus $V(S(n, k)) = \{0, \dots, k-1\}^n$, and distinct vertices $u \ne v$ are adjacent iff $(u_2, \dots, u_n) = (v_1, \dots, v_{n-1})$ or $(v_2, \dots, v_n) = (u_1, \dots, u_{n-1})$.
- **Verbatim Conjecture 1 (§4, line 123):**
  > `$S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$.`
- **Status in citing papers (`notes/audit-helper-petyuk.md` §1.4):**
  - S. Huang, S. Kitaev, A. Pyatkin (`arXiv:2312.10377v1` / *Discrete Applied Mathematics* **346** (2024), pp. 170–182, lines 341–343) quote Petyuk's Conjecture 1 verbatim as open.
  - S. Roy, R. Hariharasubramanian (`arXiv:2605.02268v2`, May 2026) do not resolve Petyuk's Conjecture 1.
- No `CONTESTED.md` exists in `targets/petyuk-2210.14762-conj1/`.
- A single counterexample at $(n, k) = (4, 3)$ ($n \ge 4$, $k \ge 3$) completely refutes the universal conjecture.

---

## 2. Adversarial Mathematical Audit of `COUNTEREXAMPLE.md`

1. **Graph parameters for $S(4, 3)$:**
   - $|V| = 3^4 = 81$. Directed arcs in $B(4, 3)$: $81 \times 3 = 243$; removing 3 self-loops (`0000`, `1111`, `2222`) leaves 240 directed arcs; removing 3 mutual 2-cycle pairs (`0101 <-> 1010`, `0202 <-> 2020`, `1212 <-> 2121`) merges 6 directed arcs into 3 undirected edges, leaving $240 - 3 = 237$ undirected edges. Contains triangle `0010–0100–1001`, so $\chi(S(4, 3)) \ge 3$.
2. **Explicit $3$-coloring (§1, lines 15–51):**
   - Defines $c(x_1, x_2, x_3, x_4) := (x_1 + f(d_1, d_2, d_3)) \bmod 3$, where $d_i = (x_{i+1} - x_i) \bmod 3$, with 9-row table for $f$ (lines 22–30).
   - Edge condition $u \to v$: $c(u) = c(v) \iff f(d_1, d_2, d_3) \equiv d_1 + f(d_2, d_3, d_4) \pmod 3$, where $u \ne v \iff (d_1, d_2, d_3, d_4) \ne (0, 0, 0, 0)$.
   - Independently verified (`notes/audit-helper-petyuk.md` §3.2) that all 9 rows of the table (L22–30) and every single case-verification line (L38–49) match `check-check-1.py`'s `TABLE_F` verbatim with zero typos, and that $c$ is a proper $3$-coloring with balanced color classes $|A_0| = |A_1| = |A_2| = 27$.
   - By Halldórsson–Kitaev–Pyatkin (2016) (cited in Petyuk `2210.14762v2` as Theorem 2), every $3$-colorable graph is word-representable; hence $S(4, 3)$ is word-representable.
3. **Self-contained explicit representing word (§2, lines 55–75):**
   - For $w = \prod_{t=1}^{28}(P_t^{(01)} P_t^{(20)} P_t^{(12)})$ of length $28 \times 3 \times 54 = 4536$:
     - Every vertex of $S(4, 3)$ has degree $\le 6 < 27 = |A_i|$, so every $y \in Y$ has at least $21$ non-neighbors in $X$, confirming $M = 28$ without padding.
     - Same-class pairs $u \ne v \in A_i$: reversed between their two round-1 blocks ($A_0$ vs $\mathrm{rev}(A_0)$, $A_1$ vs $\mathrm{rev}(A_1)$, $A_2$ vs $\mathrm{rev}(A_2)$), yielding `uvvu` (non-alternating).
     - Cross-class pairs: checked round $t = P_t^{(01)} P_t^{(20)} P_t^{(12)}$ explicitly for all three pairs:
       - $(a, b) \in A_0 \times A_1$: round $t$ restricts to `abab` if $ab \in E$ (and `baab` in $P_b^{(01)}$ if $ab \notin E$);
       - $(b, c) \in A_1 \times A_2$: round $t$ restricts to `bcbc` if $bc \in E$ (and `bccb` in $P_c^{(12)}$ if $bc \notin E$);
       - $(c, a) \in A_2 \times A_0$: round $t$ restricts to `acac` if $ca \in E$ (and `aacc` in $P_a^{(20)}$ if $ca \notin E$).
   - **Minor non-blocking typo in `COUNTEREXAMPLE.md` lines 72–73:** Lines 72–73 state that concatenating $28$ rounds of `abab`, `bcbc`, `acac` yields `$(ab)^{28}$`, `$(bc)^{28}$`, `$(ac)^{28}$`. Since each round contributes 4 letters (`abab`), $28$ rounds actually yield `$(abab)^{28} = (ab)^{56}$`, `$(bc)^{56}$`, `$(ac)^{56}$`. This arithmetic exponent typo does not affect the alternation conclusion, the word $w$ of length $4536$, or the HKP Theorem 2 deduction.

---

## 3. Independent Exact Computation Verification

Reran `check-1`'s independent exact verifier (`targets/petyuk-2210.14762-conj1/notes/check-check-1.py`):
```sh
time .venv/bin/python -u targets/petyuk-2210.14762-conj1/notes/check-check-1.py
```
Raw output (`notes/audit-helper-petyuk.md` §3.1):
```text
S(4,3) (81 vertices, 237 edges), triangle, 80 nonzero tuples, & 3-coloring (27/27/27): OK
Explicit representing word (len=4536, M=28, lex order) across all 3240 pairs: OK
Explicit representing word (arbitrary shuffled class order) across all 3240 pairs: OK
PASS
```
Exit code `0`, `0.192s` wall-clock.

---

## 4. Deep Novelty & CRITICAL Prior-Art Disclosure

Deep search across `413` watch snapshots, arXiv, OpenAlex, Crossref, Zenodo, web search, and all competing GitHub repositories (`notes/audit-helper-petyuk.md` §2) established two crucial facts:

1. **Prior art on $\chi(S(4, 3)) = 3$ under a different graph name (must be disclosed transparently):**
   - In the $\alpha$-overlap graph literature, the graph $G(a, k, k-1)$ (alphabet size $a$, word length $k$, overlap $k-1$) is **literally identical** to Petyuk's simplified de Bruijn graph $S(k, a)$; in particular, $G(3, 4, 3) = S(4, 3)$.
   - **Debra Knisley, Yared Nigussie, and Attila Pór (2010)**, *"On the chromatic number of the $\alpha$-overlap graphs"*, *J. Combin. Math. Combin. Comput. (JCMCC)* **73** (2010), pp. 3–13, **already proved $\chi(G(3, 4, 3)) = 3$** (and $\chi(G(3, n, n-1)) = 3$ for all $n \ge 4$) via a 26-vertex independent set + 55-vertex bipartite complement (independently verified by `petyuk-audit-hlp` on $S(4, 3)$).
2. **Why Petyuk's Conjecture 1 is STILL NEW under `CHARTER.md`:**
   - Knisley–Nigussie–Pór (2010) predates Halldórsson–Kitaev–Pyatkin's theorem (*Discrete Appl. Math.* **201**, 2016: every $3$-colorable graph is word-representable) by 6 years and Petyuk's Conjecture 1 (`2210.14762v2`, 2022/2023) by 12 years.
   - Petyuk (`2210.14762v2`, §1.2, line 67) was unaware of the $\alpha$-overlap graph literature (*"To our best knowledge, the notion of a simplified de Bruijn graph is introduced in this paper for the first time"*), and both Huang–Kitaev–Pyatkin (*DAM* **346**, 2024) and Roy–Hariharasubramanian (`2605.02268v2`, May 2026) left Petyuk's Conjecture 1 open.
   - Across arXiv, OpenAlex, Crossref, Zenodo, web search, and all checked GitHub repositories (`trureturing*`, `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `openai/math`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `google-deepmind/formal-conjectures`, and global GitHub), **no paper, preprint, or public repository (2010–Nov 2026) has connected Knisley–Nigussie–Pór (2010) to word-representability, shown that $S(4, 3)$ is word-representable, or refuted Petyuk's Conjecture 1**.
   - Furthermore, `COUNTEREXAMPLE.md` constructs a distinct, $\mathbb{Z}_3$-shift-equivariant (`27/27/27`) $3$-coloring and an explicit length-4536 representing word directly from first principles.

### What Is Not Established / Caveats
- Refutes Petyuk's Conjecture 1 at $(n, k) = (4, 3)$ (and note that combining Knisley–Nigussie–Pór 2010 with HKP 2016 in fact implies $S(n, 3)$ is $3$-colorable and hence word-representable for all $n \ge 4$, whereas $S(n, k)$ for $k \ge 4$ remains open; e.g., $S(4, 4)$ is not $3$-colorable).
- **Scholarly disclosure for `RESULTS.md`:** Explicitly credit Knisley–Nigussie–Pór (*JCMCC* **73**, 2010) for proving $\chi(S(4, 3)) = 3$ under the $\alpha$-overlap graph name $G(3, 4, 3)$, while clarifying that its implication for word-representability and the refutation of Petyuk's Conjecture 1 had never been published, and that `COUNTEREXAMPLE.md` provides an independent $\mathbb{Z}_3$-equivariant coloring and explicit representing word.
- Minor non-blocking prose typo at `COUNTEREXAMPLE.md` lines 72–73 (`(ab)^{28}`, `(bc)^{28}`, `(ac)^{28}` should be `(ab)^{56}`, `(bc)^{56}`, `(ac)^{56}`).
- Internal audit and exact computation are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"counterexample, verified by exact computation"`.

- **Gate 3 Novelty Clearance (`2026-11-27T03:34Z`–`04:10Z`):** **PASS** across `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-3.md`, and `notes/novelty-gate3-watch-5.md` (`watch-3` co-covering `watch-6`), covering live arXiv `2210.14762v2`, OpenAlex citing cache, Zenodo, `470` snapshots, and all 15+ competing GitHub repos (confirming no paper/repo connects Knisley–Nigussie–Pór 2010 to word-representability or refutes Petyuk Conj 1). Cleared for coordinator verification.
