# Independent Check Report: `targets/teheux-2611.12469-q3/`

- **Checker:** `@check-3`
- **Target:** `targets/teheux-2611.12469-q3/TARGET.md` (`arXiv:2611.12469v1`, Section 8, Question 8.4(3), `\label{q:correspondence}`)
- **Proof checked:** `targets/teheux-2611.12469-q3/PROOF.md` (answer: **YES**)
- **Gate 2 Watch:** **PASS** (`watch-5` `#1507`, `watch-1` `#1508`, `watch-6` `#1509`)

## 1. Primary Source Verification

- **arXiv version check:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2611.12469` confirms `2611.12469v1` is the sole arXiv version (`published: 2026-11-09T14:19:48Z`).
- **Cached TeX:** `tools/.arxiv_cache/eprint/2611.12469v1/Notes_definability_pocset.tex` (3,216 lines).
- **Statement match (`L3066-3085`, `q:correspondence` item 3):**
  > *"Does every universal sentence that holds in a median algebra $\mathrm{alg}{A}$ hold in $\hat{\mathrm{alg}{A}}$, that is, does every finite subalgebra of $\hat{\mathrm{alg}{A}}$ embed into $\mathrm{alg}{A}$?"*
  Matches `TARGET.md` verbatim.
- **Paper citation checks in `PROOF.md`:** All cited numbers/labels verified against `Notes_definability_pocset.tex`: `Definition 2.1` (`def:median`), `Definition 2.2` (`def:convex`), `Theorem 2.4` (`prop:med-axioms`), `Definition 2.5` (`def:poc`), `Theorem 3.4` (`thm:dualities`), `Corollary 4.6` (`prop:profinite`), `Lemma 7.1` (`lem:cube-lift`), `Example 7.2` (`ex:rho-k`), `Corollary 7.6` (`cor:rank-transfer`), and `Example 8.1` (`ex:rho-k-correspondent`).

## 2. Proof Audit Summary

- **Equivalence:** Follows from local finiteness of $\mathsf{M}$ (`|B| <= 2^{2^n}`) and the finite-subalgebra-forbidding universal sentences $\varphi_{\mathbf{B}}$ (`Example 7.2`).
- **Case 1 ($\mathrm{rank}(\mathbf{A}) = \infty$):** `Theorem 2.4` embeds $\mathbf{B} \hookrightarrow \mathbf{2}^d$, and infinite rank gives $\mathbf{2}^n \hookrightarrow \mathbf{A}$ for $n \ge d$; $0$-padding preserves coordinatewise median.
- **Case 2 ($\mathrm{rank}(\mathbf{A}) = r < \infty$):**
  - **Lemma 1 (Transversality bound):** Helly property for convex sets and `Lemma 7.1` give $\le r$ pairwise transverse elements in $\mathbf{X} \setminus \{0, 1\}$.
  - **Lemmas 2–3:** Finite boundary $|A_U \setminus \{0\}| \le r$, $|B_U| = |A_U| \le r + 1$, and open local upward cone $W_{t,U} \ni t$ with $W_{t,U} \cap U \subseteq t^\uparrow$ (trivial $W_{0,U} = X$ at $t=0$).
  - **Steps 0–3 (Symmetric clopen retraction $\pi$):** Pointwise clopen separation on $\mathbf{X} \subseteq \mathbf{2}^A$ gives $C_{s,t}$ and clopen down-sets $H_y = e_{\mathbf{A}}(a)^c$ whose intersection defines $t^\downarrow$, making Step 1's compactness cover over $F_t$ valid. Bottom-up induction with $\Omega_{t,U}$ ensures $t^\downarrow \cap \overline{U} \subseteq \Omega_{t,U}$, yielding Claims (I)–(II), clopen ultrafilter pullbacks $\widetilde{U} = \pi^{-1}(U)$, and the median embedding $U \mapsto a_U \in \mathbf{A}$ via `Theorem 3.4(1)`.
- **Remark:** Verified $P = (\mathbb{N} \cup \{\infty\}) \times \{0, 1\}$ is a Priestley space where $\mathcal{U}(P)$ has the nontrivial complemented pair $\{(\infty, 0), (\infty, 1)\}$ / $\mathbb{N} \times \{0, 1\}$, whereas $\mathrm{ClopUp}(P)$ has none.

## 3. Exact Mechanical Verification (`check-check-3.py`)

Command:
```sh
.venv/bin/python -u targets/teheux-2611.12469-q3/notes/check-check-3.py && .venv/bin/python -c "import ast; tree = ast.parse(open('targets/teheux-2611.12469-q3/notes/check-check-3.py').read()); floats = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]; calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'float']; print('FLOAT_COUNT:', len(floats), 'FLOAT_CALLS:', len(calls))"
```

Exact output:
```text
Part 1 (finite median/poc duality, Helly, Lemma 1, Remark 7.5): OK
Part 2 (X2: single non-clopen A_U={r<t}): |B|=1, all Lemmas 2-3 & Steps 0-3 & embedding B->A2 OK
Part 2 (X2: 2 non-clopen generators): |B|=2, all Lemmas 2-3 & Steps 0-3 & embedding B->A2 OK
Part 2 (X2: 4-gen mixed non-clopen/clopen B): |B|=5, all Lemmas 2-3 & Steps 0-3 & embedding B->A2 OK
Part 3 (0 in A_U on omega*, embedded U -> 4, V -> 0): OK
Part 4 (Remark Priestley space (N U {inf}) x {0,1} counterexample): OK
PASS
FLOAT_COUNT: 0 FLOAT_CALLS: 0
```

Verdict: **PASS**.
