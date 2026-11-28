# Blind Adversarial Audit — `targets/kern-2611.32927-oolcs-11connected/`

- **Auditor:** `@audit-1` (`auto`)
- **Primary Source Verified:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (LATIN 2026 full version), `tools/.arxiv_cache/eprint/2611.32927.src` (`main-arxiv.tex`, **Section 5** `sections/conclusion.tex` L5, `sections/preliminaries.tex` L4–19, `sections/stcon.tex` L215–224).
- **Files Audited (blind — author `verify.py` and scratch `notes/` not read):**
  - `targets/kern-2611.32927-oolcs-11connected/TARGET.md`
  - `targets/kern-2611.32927-oolcs-11connected/PROOF.md`
  - `targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.md`
  - `targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.py`
- **Verdict:** **PASS** (**Label:** `"written proof, internally audited"`).

---

## 1. Statement & Citation Fidelity

- Compiled section numbering verified via `main-arxiv.tex` L38–42: `sections/conclusion.tex` is **Section 5**, matching `TARGET.md` L3.
- `TARGET.md` L14 quotes `sections/conclusion.tex` L5 verbatim; `TARGET.md` L18–20 quotes the definitions of `\wlcs{}` and `\oolcs{}` (`sections/stcon.tex` L215–224, including distinct terminals $a \neq b \in V(\widehat{G})$ and arbitrary real weights $w : \mathcal{S}(\widehat{G}) \times \mathbb{N}_{\ge 0} \to \mathbb{R}$) verbatim.

---

## 2. Mathematical & Computational Audit

- **Main Result (YES — polynomial-time algorithm for full `WLCS` and hence `OOLCS` on $\{1,1\}$-bounded connected switches):**
  1. **Normalization & weight shifting (§1):** Shifting each switch $s$ by $m_s = \min_{i \in [|s|]} w(s, i)$ yields equivalent non-negative shifted costs $c(e) \ge 0$ against $\lambda' = \lambda - \sum_s m_s$. Every $\{1,1\}$-bounded connected switch has either $1$ edge (static cost $0$ or optional edge of cost $w'(s,\text{edge}) > 0$) or $2$ distinct edges sharing a unique center vertex $z_s$ ($P_3$-switch). Crucially, no two edges of the same switch are vertex-disjoint. (Edge-less switches, if any, have their minimum weight absorbed into $\lambda'$ and contribute no edges.)
  2. **Claim 1 (Simple class-valid $a$--$b$ path characterization, §2):** Both directions verified airtight. Because every switch has at most $2$ edges and any two edges of the same switch share its center $z_s$, a simple $a$--$b$ path uses at most one edge per switch iff it uses at most one edge from each incident switch class $C_{v, s}$ at every vertex $v$ (including at terminals $a, b$, where degree $1$ enforces this automatically).
  3. **Claim 2 (Exact reduction to minimum-weight perfect matching on $G^*$, §3):** Both directions verified airtight. Every half-edge vertex $e_v$ has neighbors $\{e_u, c_{v,s}\}$, forcing $W^*(M) = \sum_{e \in E_M} c(e)$ exactly (with half-edge weight $\frac{1}{2} c(e)$, or integer-doubled $c(e)$ against $2\lambda'$). Hub capacities $|H_a| = |H_b| = 1$ and $|H_v| = 2$ ($v \notin \{a,b\}$) enforce $\deg_{E_M}(a) = \deg_{E_M}(b) = 1$, $\deg_{E_M}(v) \in \{0, 2\}$ for $v \notin \{a,b\}$, and $|E_M \cap C_{v,s}| \le 1$, eliminating non-simple walk bypasses and decomposing $(V(\widehat{G}), E_M)$ into one simple class-valid $a$--$b$ path $P$ plus vertex-disjoint cycles (which drop with non-increasing weight because $c(e) \ge 0$).
  4. **Size & complexity bounds:** Verified exact — with $n' \le \min(n, 2m)$ active vertices and $\le 2m$ non-empty classes $(v, s)$, $|V^*| \le 2m + (2n' - 2) + 4m \le 2n + 6m$ (and $\le 10m$) and $|E^*| \le m + (n' - 2) + 2m + 4m + 2m \le 9m + n$ (and $\le 11m$), giving $O(|V^*|(|E^*| + |V^*|\log|V^*|)) = O(m^2 \log m)$ via Edmonds'/Gabow's minimum-weight perfect matching on $G^*$.
- **Independent Verifier Execution:**
  - Command: `.venv/bin/python -u targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.py`
  - AST audit: `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: [311, 313, 316]` (`pathlib.Path` joins only — zero floating-point arithmetic).
  - Exit code `0`, output `SIZE_WITNESS (n=3, m=2): |V*|=16, |E*|=17`, `WLCS_11CONNECTED_EXACT: checked=40, yes=16, no=24, trap=5`, `PASS`.

---

## 3. Handoff
**PASS** — handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 live freshness check (`< 1h`) and `@coordinator` reporting.
