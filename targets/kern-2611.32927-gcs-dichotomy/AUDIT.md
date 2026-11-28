# Blind Adversarial Audit — `targets/kern-2611.32927-gcs-dichotomy/`

- **Auditor:** `@audit-1` (`auto`)
- **Primary Source Verified:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (LATIN 2026 full version), `tools/.arxiv_cache/eprint/2611.32927.src` (`main-arxiv.tex`, `sections/introduction.tex`, `sections/preliminaries.tex` L4–19, `sections/stcon.tex` L147–175, **Section 4** `sections/gcon.tex` L1–116).
- **Files Audited (blind — author `verify.py` and scratch `notes/` not read):**
  - `targets/kern-2611.32927-gcs-dichotomy/TARGET.md`
  - `targets/kern-2611.32927-gcs-dichotomy/COUNTEREXAMPLE.md`
  - `targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.md`
  - `targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py`
- **Verdict:** **PASS** (re-audit after `#2010` / `#2017` fix; **Label:** `"written proof, internally audited"`).

---

## 1. Statement & Citation Fidelity

- Compiled section numbering verified via `main-arxiv.tex` L38–42: `sections/gcon.tex` is **Section 4**, matching `TARGET.md` L3.
- `TARGET.md` L14 & L16 quote `sections/gcon.tex` L21 (matroid switch definition) and L116 (`Global-Con Switching` dichotomy conjecture) verbatim.
- All cited theorem labels (`thm:dichotomy-lcs`, `thm:gcs-21-npc`, `thm:gcs-matroid-switches`, `thm:wgcs-matroid`) and 0-indexed position conventions (`[n] = \{0, \dots, n-1\}`) match `arXiv:2611.32927v1` verbatim.

---

## 2. Resolution of Prior FAIL Finding (`#2010`) & Full Audit Summary

- **Fix verified (`#2017`):** The erroneous parenthetical `{2,1,1}`-bounded remark previously on L27 has been removed cleanly from `COUNTEREXAMPLE.md`.
- **All three counterexamples to the `GCS` matroid-switch dichotomy conjecture verified airtight:**
  1. **$\Pi_1$ (all $\{2,1\}$-bounded $K_3$-shaped switches, L9–25):** Forced to $|s|=2$, $\{|s[0]|, |s[1]|\}=\{2,1\}$, $s[0]\cap s[1]=\emptyset$; every switch fails matroid augmentation ($A=\{uw\}, B=\{uv,vw\}$); `GCS` is solvable in $O(n+m)$ time by fixing every switch to its dominant size-$2$ position.
  2. **$\Pi_2$ (all isomorphic copies of paw-graph $L_{3,1} \cong K_4 - \{bc, cx\}$ switch $s_2$, L29–40):** Incomparable component partitions $\{\{a,x,b\},\{c\}\}$ vs $\{\{a,x,c\},\{b\}\}$; fails matroid augmentation ($A=\{ax,ac\}, B=\{ax,xb,ab\}$); exact component-preserving reduction to static-edge switch $s^{\mathrm{st}}=(\{a_s x_s\})$ plus $\{1,1\}$-bounded switch $s'=(\{a_s b_s\},\{a_s c_s\})$ yields $O(n^2 m \log n)$ for `GCS` (`thm:gcs-matroid-switches`, $T=O(1)$) and $\mathsf{P}$ for `WGCS` (`thm:wgcs-matroid`), valid under arbitrary vertex/edge sharing across switches.
  3. **$\Pi_3$ (all isomorphic copies of $K_4$-shaped acyclic spanning-tree switch $s_3$, L44–50):** Fails matroid augmentation ($A=\{ab,bc\}, B=\{ac,bd,da\}$); trivial $O(n+m)$ algorithm since both positions span $\{a,b,c,d\}$.
- **Independent Verifier Execution (re-run after patch):**
  - Command: `.venv/bin/python -u targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py`
  - AST audit: `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: [120]` (`pathlib.Path` joins only — zero floating-point arithmetic).
  - Exit code `0`, output `Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS`, `PASS`.

---

## 3. Handoff
**PASS** — handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 live freshness check (`< 1h`) and `@coordinator` reporting.
