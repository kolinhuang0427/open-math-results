# Adversarial Audit Report (`audit-1`): `targets/oeis-A400812/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A400812` (rev. 50, Nov 10 2026) — Boris K. Horvat's four conjectures on star triples in level-$n$ Spectre supertiles (plus `A400813`/`A400814` generating functions)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, live OEIS `A400812`/`A400813`/`A400814`/`A057080`/`A099919`, and primary source Smith–Myers–Kaplan–Goodman-Strauss `arXiv:2305.17743` (`00_macros.tex`, `02_construction.tex`, `04_hexagons.tex`, `05_hexsubst.tex`, `fig_hexsubsts.tex`, `0A_appendix.tex`)
- **Verdict:** **PASS** *(Re-audit after `#975` & `#992` patches; all 4 issues from the initial FAIL audit are fully resolved and verified.)*

---

## 1. Primary-Source & Computation Verification — PASS
- Live OEIS `A400812` (rev. 50), `A400813` (rev. 19), `A400814` (rev. 19), `A057080` (rev. 81), `A099919` (rev. 68) match `TARGET.md` and `PROOF.md` verbatim (`0` hits in `zenodo-23112421-oeis-ids.md`).
- Marked hexagon labels (`00_macros.tex`), $S_8/S_9$ supertile substitutions (`fig_hexsubsts.tex`), and Spectre/Mystic geometry (`02_construction.tex`, `05_hexsubst.tex`) match `arXiv:2305.17743`.
- Independent exact-arithmetic verifier `.venv/bin/python -u targets/oeis-A400812/notes/check-check-2.py` passed cleanly (exit `0`, zero floating point). Independent adversarial checks on $\Delta_3/\Delta_4$ confirmed all numerical claims and the validity of the repaired induction/geometry steps below.
- Gate 2 novelty receipts clear (`watch-1` `#761`, `watch-5` `#784`, `watch-6` `#764`).

---

## 2. Required Fixes in `PROOF.md` (and 1 Print Typo in `check-check-2`)

### Issue 1 (Blocking Logic Gap — `PROOF.md` L53, Lemma 3.1): Non-sequitur in the $\max\deg_{\partial X_n} \le 2$ proof
L53 argues:
> *"each macro-corner or piece-junction vertex along $\partial X_n$ has hexagon degree $\le 2$ inside $X_1$ (hence inside $X_n$ because every child side at level $\ge 1$ has length $\ge 2$, preventing three child corners from collapsing onto one another)."*

Child side length $\ge 2$ only prevents **three children** from meeting at a boundary vertex; by itself it does **not** rule out two children meeting at a boundary vertex where one child's macro-corner already has degree $2$ inside that child (which would produce a degree-$3$ boundary vertex).

**Fix:** Prove part (1) and part (2) **jointly** by induction via period-2 corner stabilization:
- Every macro-corner of $X_n$ and every newly formed piece-junction vertex along $\partial X_n$ has corner tuple (and hence level-0 hexagon degree) uniquely determined by the level-$(n-1)$ macro-corners $\mathrm{corners}(n-1)$ and the $X_1$ boundary template (specifically, either a single child macro-corner when two consecutive edges belong to the same child, or the concatenation of two child macro-corners when two children meet).
- Direct verification for $n = 0, 1, 2, 3, 4, 5$ establishes $\max\deg_{\partial X_n} \le 2$ AND $\mathrm{corners}(4) = \mathrm{corners}(2)$, $\mathrm{corners}(5) = \mathrm{corners}(3)$ (and that every child macro-corner participating in an interior 3-child macro-vertex of $X_1$ has degree $1$).
- By induction on $n \ge 4$, $\mathrm{corners}(n) = \mathrm{corners}(n-2)$ holds for all $n \ge 4$, so every newly formed boundary vertex (and macro-corner) at level $n$ has the exact same tuple—hence degree $\le 2$—as at level $n-2$, while older boundary vertices inherit degree $\le 2$ from level $n-1$.

### Issue 2 (Blocking Logic Gap — `PROOF.md` L57, Lemma 3.2): Missing inductive closure of $S_\Gamma$ for $n \ge 2$
L57 argues:
> *"$\Gamma$ occurs on a boundary side of $X_1$ only on labels in $\{\alpha^-, \beta^-, \gamma^+, \zeta^-, \delta^+\}$, never on any of the opposite labels $\{\alpha^+, \beta^+, \gamma^-, \zeta^+, \delta^-\}$ (`verify.py`); since each $X_1$ has only one $\Gamma$ child, by induction on $n$ two $\Gamma$ hexagons never meet along an edge or vertex in any $X_n$."*

Checking only where the single child $\Gamma$ sits on $\partial X_1$ only handles $n \le 2$: at $n \ge 2$, a level-$(n-1)$ child $Y_{n-1}$ contains level-0 $\Gamma$ hexagons on its sides with labels in $S_\Gamma := \{\alpha^-, \beta^-, \gamma^+, \zeta^-, \delta^+\}$, and if any child side with label in $S_\Gamma$ appeared on a parent macro-side outside $S_\Gamma$, a level-0 $\Gamma$ would leak onto $\overline{S_\Gamma}$ at level $n$.

**Fix:** Explicitly state and use the exact closure property of $S_\Gamma$ (verified directly on `fig_hexsubsts.tex`):
1. In $X_1$, child $\Gamma$ touches $\partial X_1$ only along macro-sides with labels in $S_\Gamma$ (and only at macro-corners shared by two $S_\Gamma$ sides, never at any endpoint of a side outside $S_\Gamma$).
2. Every parent macro-side of $X_1$ whose label is **not** in $S_\Gamma$ decomposes exclusively into child sides whose labels are **not** in $S_\Gamma$ (indeed, child sides in $S_\Gamma$ appear only on parent macro-sides in $S_\Gamma$: $\alpha^- \to \{\beta^-\}$, $\beta^- \to \{\alpha^-\}$, $\gamma^+ \to \{\beta^-\}$, $\zeta^- \to \{\alpha^-\}$, $\delta^+ \to \{\alpha^-, \beta^-\}$, and on none of the other 10 labels).
3. By induction on $n \ge 1$, no level-0 $\Gamma$ hexagon touches any macro-side of $X_n$ outside $S_\Gamma$ (including endpoints). Since $S_\Gamma \cap \overline{S_\Gamma} = \emptyset$, whenever two children $Y_n, Z_n$ meet along an interior seam of $X_{n+1}$ (opposite labels $\ell \leftrightarrow \overline{\ell}$), at most one side contains a level-0 $\Gamma$; combined with every element of $\mathcal{V}_{45}$ containing at most one $\Gamma$, no two $\Gamma$ hexagons ever share an edge or vertex in any $X_n$.

### Issue 3 (Blocking Geometric Gap — `PROOF.md` L65, Theorem 3.3): 4-hexagon geometric pinch at the $\Sigma$–$\Gamma$ spur
L65 claims:
> *"Each marked hexagon contains at most one even tile, so $P$ must lie on three distinct marked hexagons of $X_n$. By Lemma 3.1, no point of $\partial X_n$ touches more than $2$ hexagons, and along any 2-hexagon interior edge (including the $\Sigma$–$\Gamma$ spur, where $\Sigma \cup \Gamma$ has only 2 even tiles) at most $2$ even tiles meet. Hence $P$ lies on an interior 3-hexagon vertex of $X_n$, which belongs to $\mathcal{V}_{45}$ by Lemma 3.2."*

Because $\Sigma$ has a zero-thickness spur (`W_{11} -- W_{11}+\zeta_{12}^5 -- W_{11}+\zeta_{12}^5+\zeta_{12}^3`), its $\delta^+$ side (glued to $\Gamma$'s $\delta^-$ side) passes right through $\Sigma$'s corner 1 ($W_{11}$, between $\zeta^+$ and $\beta^+$). Consequently, **four** marked hexagons ($\Sigma, \Delta, \Gamma$, and the $\beta^-$ neighbor $X$) meet geometrically at $W_{11}$ (63 such 4-hexagon geometric points occur in $\Delta_3$!). Without addressing this, one must rule out a 3-even-tile triple at $W_{11}$ using $\Gamma$'s even tile instead of the 3-hexagon vertex $(\Sigma, \Delta, X) \in \mathcal{V}_{45}$.

**Fix:** Note explicitly that in $\Gamma = W \cup B$, the entire $\delta^-$ boundary segment (`B_{13}, B_0, \dots, B_5`) lies strictly on $\Gamma$'s **odd** Spectre $B$, disjoint from $\Gamma$'s **even** Spectre $W$ (which meets $B$ only along `B_7..B_{11} = W_5..W_1`). Therefore $\Gamma$'s even tile NEVER touches the $\Sigma$–$\Gamma$ spur or $W_{11}$: at every 4-hexagon pinch $W_{11}$, the even Spectres touching $W_{11}$ are **exclusively** the three even tiles of the interior 3-hexagon vertex $(\Sigma, \Delta, X) \in \mathcal{V}_{45}$ (and similarly at the spur tip `SIGMA_SPUR`, $\Sigma$'s even tile does not reach the tip, and on $\partial X_n$ at most 2 even tiles meet even at a spur base). Thus every geometric point $P$ touched by 3 even Spectres corresponds to a unique interior 3-hexagon vertex in $\mathcal{V}_{45}$ whose 3 hexagons supply those exact 3 even Spectres. (Also note there are $3$ $L$-configs and $1$ $S$-config in $\mathcal{V}_{45}$, leaving $41$ non-star configs.)

### Issue 4 (Minor Polish — `PROOF.md` L5, L75, L97 & `check-check-2.{py,md}`)
1. **Section 4 L75:** State explicitly the 1-to-1 child-side alignment property across all 134 compatible seams in $\mathcal{S}$ (for every opposite-labeled pair $((Y,s_1),(Z,s_2))$, the child decompositions of $(Y_1, s_1)$ and $\mathrm{rev}(Z_1, s_2)$ have equal length and match opposite-labeled child sides 1-to-1, so glued child seams align 1-to-1 for all $n \ge 0$), and note that tile chirality also has period 2 ($n \bmod 2$).
2. **Section 1 L5 & Section 5 L97:** Clarify in L5 that the OEIS `A400812` level-$n$ supertile starts from a single Spectre (any of the 8 non-$\Gamma$ marked tiles, all yielding identical star-triple counts, distinct from the Mystic supertile $\Gamma_n$), and replace the internal code identifier `SUPERTILE_DEFS` on L97 with `fig:supertiles` (`fig_hexsubsts.tex`).
3. **Checker print typo (`check-check-2.py` L699 & `check-check-2.md` L10):** Fix `40/45` to `41/45` (`3 + 1 + 41 = 45`).

---

## 3. Verified Sound Sections (No Issues Found)
- **Section 2:** Marked hexagon labels, $\mathbb{Z}[\zeta_{12}]$ coordinates of $W$, $\Gamma_0$, and $\Sigma$, and edge-to-edge non-overlapping gluing of all 134 seams in $\mathcal{S}$.
- **Section 4 (Krylov & Rational GFs):** 143-dim transfer matrix $A$, 60-dim reachable subspace $A_r$, minimal annihilating polynomial $q(z) = z(z-1)(z^2-62z+1)(z^2-18z+1)$ of $A_r^2$ on $e_X^T$, degree $\le 6$ numerator argument for $(1-y)Q_{\text{rev}}(y)\sum_{m\ge 0} T(X_{2m+2})y^m$, exact rational GFs $G_L, G_S, G$, and order-5 recurrence.
- **Section 5:** Tile-count matrix $M_{\text{tile}} = \bigl(\begin{smallmatrix}1&6\\1&7\end{smallmatrix}\bigr)$, `A057080`–Fibonacci/`A099919` GF identity, and asymptotic limit $4 - \sqrt{15}$.

---

## 4. Re-Audit Verification (`#975`, `#992`) — PASS

Re-read the patched `PROOF.md`, `notes/check-check-2.md`, and `notes/check-check-2.py`, and re-executed `.venv/bin/python -u targets/oeis-A400812/notes/check-check-2.py`:
1. **Issue 1 (`PROOF.md` Lemma 3.1):** Resolved cleanly via joint induction on $n$ with period-2 corner stabilization ($\mathrm{corners}(4)=\mathrm{corners}(2)$, $\mathrm{corners}(5)=\mathrm{corners}(3)$, $\max\deg_{\partial X_n} \le 2$ for $0 \le n \le 5$, and every child macro-corner at an interior 3-child macro-vertex of $X_1$ has degree $1$).
2. **Issue 2 (`PROOF.md` Lemma 3.2):** Resolved cleanly via the explicit inductive closure of $S_\Gamma = \{\alpha^-, \beta^-, \gamma^+, \zeta^-, \delta^+\}$ (child $\Gamma$ touches $\partial X_1$ only on $S_\Gamma$ sides/corners, and every parent macro-side outside $S_\Gamma$ decomposes solely into child sides outside $S_\Gamma$, preventing level-0 $\Gamma$ leakage onto $\overline{S_\Gamma}$ for all $n \ge 1$).
3. **Issue 3 (`PROOF.md` Theorem 3.3):** Resolved cleanly by explicitly handling the 4-hexagon geometric pinch at $\Sigma$'s corner $W_{11}$ ($\Gamma$'s entire $\delta^-$ segment lies strictly on odd tile $B$, disjoint from $\Gamma$'s even tile $W$, so $\Gamma$'s even tile never touches the $\Sigma$–$\Gamma$ spur or $W_{11}$; every geometric 3-even-tile point corresponds uniquely to an interior 3-hexagon vertex in $\mathcal{V}_{45}$, with $3$ $L$-configs, $1$ $S$-config, and $41$ non-star configs).
4. **Issue 4 (Polish & Checker):** Resolved cleanly — Section 4 states 1-to-1 child-side alignment across all 134 seams in $\mathcal{S}$ and period-2 chirality; Section 1 clarifies single-Spectre initialization vs $\Gamma_n$; Section 5 cites `fig:supertiles` (`fig_hexsubsts.tex`) instead of internal code identifiers; `check-check-2.py` L699 & `check-check-2.md` L10 updated to `41/45`.
5. **Re-run of Independent Verifier:** `.venv/bin/python -u targets/oeis-A400812/notes/check-check-2.py` exited `0`, `PASS` (printing `3 L-configs (R_L^2 = 10+5*sqrt(3)), 1 S-config (R_S^2 = 10+3*sqrt(3)), 41/45 have 0 star triples` and passing all 11 exact checks).
6. **Zenodo OEIS snapshot cross-check:** Confirmed `A400812`, `A400813`, `A400814` have `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.

**Final Verdict:** **PASS**. Ready for Gate 3 novelty verification.
