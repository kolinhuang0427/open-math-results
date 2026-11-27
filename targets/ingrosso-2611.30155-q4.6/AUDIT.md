# Independent Adversarial Audit: `targets/ingrosso-2611.30155-q4.6/`

- **Auditor:** `@audit-1`
- **Target:** E. Ingrosso, M. Trombetti, and A. Zitouni, *Groups with dual classes of subgroups*, `arXiv:2611.30155v1` (confirmed sole version live on `arxiv.org/abs/2611.30155` as of 2026-11-27), Section 4 Question 4.6 (`pronormali_arxiv.tex` L784–786, referring to Theorem 4.5 `\label{sip}`, L772–774).
- **Candidate Artifacts Inspected (blind):** Primary source `tools/.arxiv_cache/eprint/2611.30155/pronormali_arxiv.tex`, `TARGET.md`, `PROOF.md`, `notes/check-check-1.py`, `notes/check-check-1.md`.
- **Verdict:** **PASS** (verification label: `"written proof, internally audited"`).

---

## 1. Primary-Source Fidelity & Compiled Numbering — PASS

Verified verbatim against `tools/.arxiv_cache/eprint/2611.30155/pronormali_arxiv.tex` (`\numberwithin{theo}{section}`, shared `[theo]` counter across `theo`, `prop`, `lem`, `defi`, `cor`, `rem`, `ex`, `quest`):
- **Theorem 3.1 (`\label{pgroups}`, §3, L359–365):** Characterizes non-abelian locally finite $p$-groups whose subgroups are normal or contained in the norm; $M_{16}$ ($p = 2, o(a) = 8, o(x) = 2, B = 1, |G'| = 2$, $8 \ge 4/2 \cdot 2 = 4$) is indeed of type (2).
- **Theorem 4.5 (`\label{sip}`, §4, L772–774):** Let $G$ be a locally graded group whose subgroups are pronormal or contained in the pro-norm. If $H$ is a subnormal subgroup of $G$, then $H$ has defect at most $7$.
- **Question 4.6 (§4, L784–786):** *What is the smallest possible defect of subnormality in the statement of Theorem 4.5?*
- **Definitions verified verbatim:** pronormal subgroup and pronormalizing element (L178), pro-norm $N_{\mathrm{pro}}(G) = \bigcap_{K \le G} P_G(K)$ (L190, L225; crucially treated only as a subset, not assumed to be a subgroup), locally graded group (L219).

---

## 2. Mathematical Audit — PASS (Answer: **$2$**)

1. **Lemma 1 ($P_G(H) = N_G(H)$ for every subnormal subgroup $H \le G$ in any group $G$, `PROOF.md` L23–31):**
   - $N_G(H) \subseteq P_G(H)$ via $u = 1$.
   - Conversely, if $y \in P_G(H)$ with $H^y = H^u$, $u \in J := \langle H, H^y \rangle$, and $H = H_0 \trianglelefteq \dots \trianglelefteq H_d = G$, then $J_i := J \cap H_i$ gives $H = J_0 \trianglelefteq \dots \trianglelefteq J_d = J$. If $H^y \neq H$, then $J \neq H$ (else $u \in H \implies H^y = H^u = H$), so taking minimal $r \ge 1$ with $J_r = J$ yields $H \le J_{r-1} \trianglelefteq J$ with $J_{r-1} < J$; since $u \in J$, $H^y = H^u \le (J_{r-1})^u = J_{r-1}$, forcing $J = \langle H, H^y \rangle \le J_{r-1} < J$, contradiction. Valid in arbitrary (including infinite) groups. **Airtight.**
2. **Lemma 2 ($N_{\mathrm{pro}}(G)$ is closed under $G$-conjugation, L33–37):**
   - For $y \in N_{\mathrm{pro}}(G)$, $g \in G$, and $K \le G$, $y \in P_G(K^{g^{-1}})$ gives $u \in \langle K^{g^{-1}}, K^{g^{-1}y} \rangle$ with $K^{g^{-1}y} = K^{g^{-1}u}$. Conjugating by $g$ under right conjugation ($x^g = g^{-1}xg$) gives $K^{y^g} = K^{u^g}$ with $u^g \in \langle K, K^{y^g} \rangle$, so $y^g \in P_G(K)$ for all $K \le G$, hence $y^g \in N_{\mathrm{pro}}(G)$. **Airtight.**
3. **Sharp Upper Bound ($\mathrm{defect} \le 2$, L39–43):**
   - Case 1 ($H$ pronormal): $G = P_G(H) = N_G(H)$ by Lemma 1, so $H \trianglelefteq G$ (defect $\le 1$).
   - Case 2 ($H$ not pronormal): by hypothesis $H \subseteq N_{\mathrm{pro}}(G)$, so by Lemma 2 every conjugate $h^g$ ($h \in H, g \in G$) lies in $N_{\mathrm{pro}}(G) \subseteq P_G(H) = N_G(H)$ (Lemma 1). Since $N_G(H)$ is a subgroup of $G$ containing all generators $\{h^g\}$ of $H^G$, $H^G \le N_G(H)$, hence $H \trianglelefteq H^G \trianglelefteq G$ (defect $\le 2$). Holds for *every* group $G$ satisfying the dual subgroup condition, without even needing local gradedness or subgroupness of $N_{\mathrm{pro}}(G)$. **Airtight.**
4. **Tightness ($\mathrm{defect} = 2$ achieved by $M_{16}$, L47–57):**
   - $M_{16} = \langle a, x \mid a^8 = x^2 = 1,\, x^{-1}ax = a^5 \rangle$ has order $16$ ($5^2 \equiv 1 \pmod 8$), hence is finite and locally graded.
   - Verified directly: $M_{16}' = \langle a^4 \rangle \le Z(M_{16})$, so every subgroup containing $a^4$ is normal (hence pronormal); $(xa^j)^2 = a^{6j}$ implies the only non-trivial subgroups avoiding $a^4$ are $\langle x \rangle$ and $\langle xa^4 \rangle$; $x^{-1} a^j x = a^{5j} \in \langle a^j \rangle$ and $x^{-1}(xa^j)x = (xa^j)a^{4j} \in \langle xa^j \rangle$ (trivial for even $j$, equals $(xa^j)^5$ for odd $j$), so $x, xa^4 \in N(M_{16}) \subseteq N_{\mathrm{pro}}(M_{16})$.
   - For $H = \langle x \rangle$, $a^{-1}xa = xa^4 \notin H$ (not normal, defect $> 1$) while $H \trianglelefteq \langle x, a^4 \rangle \trianglelefteq M_{16}$ (exact defect $2$). **Airtight.**

---

## 3. Independent Mechanical Verification (`notes/check-check-1.py`) — PASS

- **AST & exactness audit:** `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: []` (pure integer group-table & subgroup-lattice BFS arithmetic).
- **Execution:** `.venv/bin/python -u targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py` exited `0`, raw output:
  - `M_16 (|G|=16, #subs=11, |N|=8, |N_pro|=8, hyp=True, max_defect=2): OK`
  - `D_8 (|G|=8, #subs=10, |N|=2, |N_pro|=2, hyp=False, max_defect=2): OK`
  - `S_3 x S_3 (|G|=36, #subs=60, |N|=1, |N_pro|=18, hyp=True, max_defect=2): OK`
  - `M_16 x| C_3 (|G|=48, #subs=36, |N|=4, |N_pro|=24, hyp=True, max_defect=2): OK`
  - `PASS`

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (`"written proof, internally audited"`).
- Gate 2 novelty passed (`#1682` `watch-6`, `#1683` `watch-1`, `#1684` `watch-5`). Ready for Gate 3 freshness (`<1h`) and Coordinator reporting.
