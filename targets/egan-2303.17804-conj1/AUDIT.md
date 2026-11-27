# Blind Audit Report: `targets/egan-2303.17804-conj1/` (`@audit-2`)

**Verdict: FAIL (4 localized proof defects in `PROOF.md`; primary-source fidelity, Theorems 1, 2, 4, Main Theorem architecture, and `check-check-2.py` PASS)**

The overall proof architecture — Lemma 1, Theorem 1 (Small-Slack), Theorem 2 ($d_1 = n - 2$), Theorem 3 (Low-Tail $d_4 \le 5$), Lemma 2 ($K_2$-peeling), Theorem 4 ($b_{\min} \in \{4, 5\}$), Theorem 5 ($b_{\min} \ge 6$ dual peeling), and the strong-induction Main Theorem — is structurally sound and solves Egan–Nikolayevsky's conjecture. However, line-by-line adversarial verification uncovered **4 concrete localized proof defects** in `PROOF.md` (false intermediate lower bounds in Theorem 3 Part 2, a missing tie-breaking justification in Theorem 5 Step 1 Subcase 1a, an arithmetic off-by-1 error in Theorem 5 Step 2, and strict-vs-weak inequality errors in Theorem 5 Step 3 / Lemma 2 Case 1) that must be patched before Gate 3 / reporting.

---

## 1. Primary Source & Statement Fidelity

- **Live arXiv query:** `arXiv:2303.17804v1` (Benjamin Egan and Yuri Nikolayevsky, *"On triangular biregular degree sequences"*, published in *Discrete Mathematics* 347(2) (2024), Article 113778, DOI `10.1016/j.disc.2023.113778`) is the sole version on arXiv.
- **Verbatim TeX verification (`tools/.arxiv_cache/eprint/2303.17804/main.tex`, Section 1, L76–82):**
  - `\begin{conj*}` (L80–82): *"Any graphical sequence all of whose terms are greater than or equal to $4$ admits a triangular realisation."*
  - Definitions (L76–78): finite simple graphs (no loops, no multiple edges; connectedness not required), triangular iff every edge belongs to a $3$-cycle.
  - `TARGET.md` and `PROOF.md` match `main.tex` verbatim.

---

## 2. Blocking Defects in `PROOF.md` (Must Fix)

### Defect 1: False intermediate $\mathrm{RHS}_k$ lower bounds in Theorem 3 Part 2 (`PROOF.md` L162–169)
The Erdős–Gallai verification for $h$ on $U$ assumes only the $\le \ell - 2$ touched vertices of $N_1$ can fall below $3$, overlooking that **$v_2$ and $v_3$** are also reduced by $\ge 2$ and can drop to $1$ or $2$ and land in the tail $\{h_{k+1}, \dots, h_{d_1}\}$. Consequently, four displayed intermediate lower bounds fail on valid graphical sequences $d$:
1. **L163 ($k = 2, \ell \ge 2$):** Claims $\mathrm{RHS}_2 \ge 2 + 2(d_1 - 4) + 2(1) = 2 d_1 - 4$. **Fails** at $d = (6, 4, 4, 4^6)$ ($w=2, q=6, p=0$, cost $(2,2,2)$): $h = (3, 3, 3, 1, 1, 1)$ gives $\mathrm{RHS}_2 = 2 + 2 + 1 + 1 + 1 = 7 < 8 = 2(6) - 4$ (and at $d = (8, 4, 4, 4^8)$: $h = (3^5, 1^3)$, $\mathrm{RHS}_2 = 11 < 12$).
2. **L165 ($k = 3, \ell = 1$):** Claims $\mathrm{RHS}_3 = 6 + 3(d_1 - 3) = 3 d_1 - 3$. **Fails** at $d = (6, 5, 5, 5^6, 4^3)$ ($w=5, q=3, p=6$, cost $(2)$): $h = (4, 4, 4, 4, 4, 2)$ has $h(v_2) = 2$ in the tail, giving $\mathrm{RHS}_3 = 6 + 3 + 3 + 2 = 14 < 15 = 3(6) - 3$ (similarly for every $(d_1, 5, 5, 5^{d_1}, 4^3)$ with $d_1 \ge 6$). Also note L162 ($k=2, \ell=1$) should state the one-phrase reason $h(v_2) \ge 2$ (in Row 9, $p \ge 5 \implies d_2 \ge d_4 = 5 \implies h(v_2) = d_2 - 3 \ge 2$).
3. **L166 ($k = 3, \ell \ge 2$):** Claims $\mathrm{RHS}_3 \ge 6 + 3(d_1 - 5) + 2(1) = 3 d_1 - 7$ and (for $d_1 = 6, \ell \le 3$) $\mathrm{RHS}_3 \ge 13$. **Fails** at $d = (6, 4, 4, 4^6)$ ($h = (3,3,3,1,1,1)$, $\mathrm{RHS}_3 = 9 < 11 < 13$) and $d = (6, 5, 5, 5^4, 4^2)$ ($h = (4,4,4,2,2,2)$, $\mathrm{RHS}_3 = 12 < 13$).
4. **L168 ($k = 4, \ell = 1$) & L169 ($k = 4, \ell \ge 2, d_1 \ge 7$):**
   - L168's justification *"0 vertices of $N_1$ are touched (all $\ge 3$), so $\mathrm{RHS}_4 \ge 12 + 3(d_1 - 4)$"* ignores $h(v_2) = 2 < 3$ when $d_2 = 5$ (the inequality $\mathrm{EG}_4(h) \ge 0$ still holds because $d_2 = 5$ forces $h_i \le 4$ for all $i$, and Row 9 has $q \le 4$ with $q_W = 3$ so at most one vertex of $N_1$ has $h = 3$, leaving $\ge d_1 - 3$ vertices with $h = 4$).
   - L169 claims $\mathrm{RHS}_4 \ge 12 + 3(d_1 - 6) + 2(1) = 3 d_1 - 4$, which **fails** at $d = (7, 5, 4, 4^7)$ ($h = (3^4, 2, 1, 1)$, $\mathrm{RHS}_4 = 16 < 17$) and $d = (8, 4, 4, 4^8)$ ($h = (3^5, 1^3)$, $\mathrm{RHS}_4 = 18 < 20$).

*(In all these cases $\mathrm{EG}_k(h) \ge 0$ still holds cleanly because whenever $h(v_2)$ or $h(v_3)$ drops below $3$, $d_2$ or $d_3$ is $\le 5$ and $h_1, h_2$ are bounded by $4$ instead of $d_1 - 3$. Rewrite L161–174 cleanly by accounting for $h(v_2), h(v_3) \in \{1, 2\}$ — e.g., splitting by $d_3 \le 5$ vs $d_3 \ge 6$ — and verify every displayed inequality against all valid $(d_1, d_2, d_3, p, q)$.)*

### Defect 2: Missing $D_2$-tie-breaking step in Theorem 5 Step 1, Subcase 1a (`PROOF.md` L272–275)
- L272 infers $m_2 + q_2 \le 3$ from $c^{(2)}_{s_2 + 1} - c^{(2)}_{r_2 + 1} \ge m_2$ and the weak inequality `(4)` ($c^{(2)}_{s_2 + 1} - c^{(2)}_{r_2 + q_2} \le 2$). That inference is **invalid** from `(4)` alone: if $c^{(2)}_{r_2 + 1} = b_2 + 1$ and $b_2$ has multiplicity $\ge 4$, then $c^{(2)}_{r_2 + 2} = c^{(2)}_{r_2 + 3} = b_2$ is not strictly decreasing after $r_2 + 1$, so `(4)` allows $m_2 = 1, q_2 \ge 3$ ($m_2 + q_2 \ge 4$).
- **Fix:** Invoke the $D_2$-tie-breaking rule already assumed in Lemma 2(2): since $r_2 + q_2 \in K'_2 \cap U_2$ beats $s_2 + 1 \in I'_2 \cap D_2$, we have the **strict** inequality $t_2 = c^{(2)}_{r_2 + q_2} > c^{(2)}_{s_2 + 1} - 2$, i.e. $c^{(2)}_{s_2 + 1} - c^{(2)}_{r_2 + q_2} \le 1$. Combined with $1 \le m_2 \le c^{(2)}_{s_2 + 1} - c^{(2)}_{r_2 + 1} \le c^{(2)}_{s_2 + 1} - c^{(2)}_{r_2 + q_2} \le 1$, this immediately forces $m_2 = 1$ and $c^{(2)}_{r_2 + q_2} = c^{(2)}_{r_2 + 1} > b_2$, hence $q_2 = 1$ (eliminating $(1, 2)$ and $(2, 1)$ altogether and leaving only $(1, 1)$!).

### Defect 3: Arithmetic off-by-1 error in Theorem 5 Step 2 (`PROOF.md` L306–308, L312–313)
- L306 writes `(p_2 - 1) - (c^{(2)}_i - 2) = (b_2 - c^{(2)}_i) + (u + 1)`. Since $p_2 := b_2 - 1 + u$ (L302), the exact identity is
  $$(p_2 - 1) - (c^{(2)}_i - 2) = p_2 + 1 - c^{(2)}_i = (b_2 - c^{(2)}_i) + u$$
  (not $+ (u + 1)$).
- **Fix:** Replace $(u + 1)$ with $u$ in L306, L307, L308, L312, L313:
  - L308 ($L \le 3$): $(k^* - L) u \ge 2 \cdot 5 = 10 \implies b_2 - c^{(2)}_{k^*} \le t_{\mathrm{out}} - 9 \implies c^{(2)}_{k^*} \ge N_\ge + 8 \ge N_\ge + 1$.
  - L313 ($4 \le L < k^*$): $(k^* - L) u \ge 1 \cdot 5 = 5 \implies b_2 - c^{(2)}_{k^*} \le t_{\mathrm{out}} - 10 \implies c^{(2)}_{k^*} \ge N_\ge + 9 \ge N_\ge + 1$.
  The target lower bound $c^{(2)}_{k^*} \ge N_\ge + 1$ holds intact.

### Defect 4: Strict-vs-weak inequality slips in Theorem 5 Step 3 (L321, L328) and Lemma 2(2) Case 1 (L198)
1. **L321 (Theorem 5 Step 3, Case A):** Claims *"Every entry in $P_1 = \{1, \dots, p_1\}$ of $c^{(1)}$ has $c^{(1)}_i > k_1 \ge k^* + 1$, i.e. $c^{(1)}_i \ge k^* + 2$"*. For $i \in K'_1 \cap U_1$, `(4)` only guarantees $c^{(1)}_i \ge t_1 \ge k_1$ (not strictly $> k_1$). **Fix:** Note explicitly that if $k_1 \ge k^* + 2$ then $c^{(1)}_i \ge t_1 \ge k_1 \ge k^* + 2$; and if $k_1 = k^* + 1$ then $D_1$-tie-breaking + `(7)` gives $c^{(1)}_i \ge t_1 > c^{(1)}_{s_1 + 1} - 2 \ge (k^* + 3) - 2 = k^* + 1 \implies c^{(1)}_i \ge k^* + 2$. Thus every $i \in P_1$ indeed satisfies $c^{(1)}_i \ge k^* + 2$, so $p_1 \le p_\ge$.
2. **L328 (Theorem 5 Step 3, Case B):** Claims *"every $i \in \{L_0 + 1, \dots, p_1\}$ of $c^{(1)}$ has $c^{(1)}_i > k_1 \ge L_0$"*. Again, for $i \in K'_1 \cap U_1$ we only have $c^{(1)}_i \ge k_1 \ge L_0$ (which still gives $\min(c^{(1)}_i, L_0) = L_0$). **Fix:** Change `> k_1` to `\ge k_1`.
3. **L198 (Lemma 2(2) Case 1):** Claims *"if $k \ge b$, then $c_k = d'_k \ge k \ge b$"*. When $c_r - 2 < c_k$, the $k$-th largest entry $d'_k$ of $d'$ is strictly smaller than $c_k$ (e.g., $c = (10^5, 9^2, \dots), b = 6, k = 6$ gives $d'_6 = 8 < 9 = c_6$). **Fix:** Change `c_k = d'_k` to `c_k \ge d'_k` (since $k \in K' \cap U \implies c_k \ge \min_{i \in K'} d'_i = d'_k \ge k \ge b$).

---

## 3. Sections Independently Audited & Verified Sound (PASS)

- **Section 1 (Eq. (1), Lemma 1):** Verified line-by-line. **PASS.**
- **Section 2 (Theorem 1 Small-Slack & Theorem 2 $d_1 = n - 2$):** Every edge case (including $k=4, a=2$ in Thm 1(c)(1), $y \in I_\le$/$I_>$ in Thm 1(c)(2), $a=0,1,2$ switches/3-trade in Thm 1(c)(3), and `(O1)`/`(O2)` Cases 1–2 in Thm 2) verified airtight. **PASS.**
- **Section 3 (Theorem 3 Part 1 bases $n=5..11$, $n\ge 12$ peeling, Part 2 graphicality criterion & all 11 rows of $W$–$U$ table):** All 11 rows, chord lists, and peeling intervals verified exact. **PASS** (pending Defect 1 fix on L162–169).
- **Section 4 (Lemma 2(1), Lemma 2(2) Case 2 & Eq. (2)–(3), Identities (I1)/(I2)/(I2'), Theorem 4, Theorem 5 Step 1 Subcases 1b–1c & Step 3 Case B L329–333):** All algebra and cases verified airtight (pending Defects 2–4 fixes on L198, L272–275, L306–313, L321, L328).
- **Section 5 (Main Theorem strong induction):** Verified exhaustive and non-circular. **PASS.**

---

## 4. Independent Checker & Gate 2 Verification

- Re-ran `.venv/bin/python -u targets/egan-2303.17804-conj1/notes/check-check-2.py`: `exit 0`, AST `FLOAT_CONSTANTS: 0`, raw `PASS` (exhaustively built & verified $7,188$ explicit simple triangular graphs for $n=5..11$, $21,794$ coverage at $n=12$, adversarial large-$n$ up to $n=144$, and Lemma 2 exact identities).
- Gate 2 novelty receipts verified (`notes/novelty-gate2-watch-{1,5,6}.md`): all 3 PASS.

**Action required:** `@attack-1` to patch Defects 1–4 in `PROOF.md` (and verify every intermediate bound in Theorem 3 Part 2), then ping `@audit-2` for rapid re-audit.

---

## 5. Re-Audit Verdict (`audit-2`, `2026-11-27T11:18Z`) — **PASS**

Verified `@attack-1`'s patched `targets/egan-2303.17804-conj1/PROOF.md` (`#1052`) against all 4 blocking defects from §3:

1. **Defect 1 (Theorem 3 Part 2, L159–193):** Rewritten cleanly using the exact universal lower bounds $\mathrm{RHS}_2 \ge 2d_1 - 2 - n_1$, $\mathrm{RHS}_3 \ge 3d_1 - 3 - L_3$, $\mathrm{RHS}_4 \ge 3d_1 - L_3$ and trivial bounds $\mathrm{RHS}_2 \ge d_1$, $\mathrm{RHS}_3 \ge d_1 + 3$, $\mathrm{RHS}_4 \ge d_1 + 8$, split cleanly into Regimes I, II, IIIa, IIIb, IIIc. Independently verified every intermediate inequality exhaustively in Python across all `24,585` valid $(d_1, w, q, d_2, d_3)$ instances for $6 \le d_1 \le 20$ (`0` violations) and verified every linear/asymptotic inequality algebraically for all $d_1 \ge 6$.
2. **Defect 2 (Eq. (4) L233–234 & Theorem 5 Subcase 1a L290–292):** Tightened (4) via $D$-tie-breaking ($c_{s+1} - 1 \le t_0$), which directly forces $m_2 = 1$ and $c^{(2)}_{r_2+q_2} = c^{(2)}_{r_2+1} > b_2 \implies q_2 = 1$, yielding $\mathrm{EG}_{k_2}(d^{(2)}) - \mathrm{EG}_{k_2}(d) = -1 \implies \mathrm{EG}_{k_2}(d^{(2)}) \ge 5 > 0$. Airtight.
3. **Defect 3 (Theorem 5 Step 2 L322–329):** Fixed $(p_2 - 1) - (c^{(2)}_i - 2) = (b_2 - c^{(2)}_i) + u$, yielding $c^{(2)}_{k^*} \ge N_\ge + 8 \ge N_\ge + 1$ ($L \le 3$) and $c^{(2)}_{k^*} \ge N_\ge + 9 \ge N_\ge + 1$ ($4 \le L < k^*$). Airtight.
4. **Defect 4 (L216, L337, L344):** Fixed Lemma 2(2) Case 1 (`c_k \ge \min_{i \in K'} d'_i = d'_k \ge k \ge b`), Theorem 5 Step 3 Case A (invoking $D_1$-tie-breaking in (4) + (7) at $k_1 = k^* + 1$ to obtain $t_1 \ge c^{(1)}_{s_1+1} - 1 \ge k^* + 2$), and Case B (`c^{(1)}_i \ge k_1 \ge L_0`). Airtight.

**Final Audit Verdict:** **PASS.** Handing off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check.
