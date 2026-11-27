# Adversarial Audit Report (`audit-1`): `targets/hardt-2412.06976-conj7.5/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Andrew Hardt & David Wallach, `arXiv:2412.06976v2` (*When do Schubert polynomial products stabilize?*), Section 8, **Conjecture 8.5** (Conjecture 7.5 in `v1`; lines 1603–1607 of `schubert-paper.tex`)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and primary source `tools/.arxiv_cache/eprint/2412.06976/schubert-paper.tex` (`2412.06976v2`, updated `2025-01-24`)
- **Verdict:** **PASS** *(Re-audit after `#1092` patch; all 3 issues from the initial FAIL audit are fully resolved and verified.)*

---

## 1. Primary-Source & Citation Audit — PASS
- Verified verbatim against `arXiv:2412.06976v2` (`schubert-paper.tex`, 32 pp., latest version on arXiv API):
  - Conjecture statement (`TARGET.md` L11–14) matches `schubert-paper.tex` L1603–1607 (normalizing the source's duplicate phrase `be the composition be composition` and writing `\overline` for `\overleftarrow`).
  - All numbered citations in `TARGET.md` and `PROOF.md` match compiled `v2` numbering exactly: `Definition 2.2` (L324), `Definition 3.4` (L431), `Definition 3.13` (L562), `Section 4.3, Proposition 4.21` (L807), `Section 8, Eq. (34)` (L1531–1537), `Definition 8.1` (L1563), `Proposition 8.2` (L1576), `Proposition 8.3` (L1584), `Remark 8.4` (L1598–1599), `Conjecture 8.5` (L1605), `eq:nabla-xi-olR-action` (L800), and `eq:key-stabilization` (L1572).
  - Independent checker `.venv/bin/python -u targets/hardt-2412.06976-conj7.5/notes/check-check-1.py` ran cleanly (exit `0`, all `PASS`, pure integer/`Fraction` arithmetic).
  - Gate 2 novelty receipts clear (`watch-1` `#762`, `watch-5` `#782`, `watch-6` `#755`).

---

## 2. Required Fixes in `PROOF.md`

### Issue 1 (Blocking Math Bug — `PROOF.md` L77, Lemma 3(3)): False $q > m$ claims in the $i < t = m$ subcase
Under the shared branch **"Otherwise ($t < m$ or $i < t = m$)"**, L77 asserts:
> *"Moreover, if $q > m$, then $\lambda_m < k$ (for $\lambda_m = k$ forces $t=m$ and $q=m+k$) and ($*$) for $r=m$ forces $w(m) < k$, so $w(m+1) < w(m) < k = w(q)$, whence $q \ge m+2$ and replacing $k$ by $k+1$ at $q \ge m+2$ preserves the strict increase $u(m+1) < u(m+2) < \dots$ as well as $u(m) > u(m+1)$."*

and later in the same line:
> *"if $q > m$ then $w(j) < w(m) < k$ for $m < j \le s_w$ and $w(j) > w(m)$ for $j > s_w$ (and $u(q)=k+1 > u(m)$), so again $s_u = s_w$."*

This breaks completely in the **$i < t = m$** subcase (which is explicitly inside this branch and has $\lambda_m = k$ and $q = m + k = s_w > m$):
1. $\lambda_m < k$ is **false** ($\lambda_m = k$).
2. $w(m) < k$ is **false** (in fact $w(m) \ge k + 2$, as L78 itself states).
3. $q \ge m + 2$ is **false** when $k = 1$ (e.g., $\lambda = (1, 1)$ has $w = 231, m = 2, i = 1, t = 2, q = 3 = m + 1$).
4. $u(q) = k + 1 > u(m)$ is **false** (in fact $u(q) = k + 1 < w(m) = u(m)$, which is why $s_u = m + k = s_w$!).
5. In addition, even when $t < m$ and $q > m$, preserving $u(q) < u(q+1)$ requires noting that $w(q+1) \ge k + 2$ (because $w(i) = k + 1$ lies at $i \le t < m < q$).

**Fix:** Split the $q > m$ justification on L77 cleanly into two cases:
- **$i < t = m$:** $\lambda_m = k$, $w(m+1..m+k) = (1, \dots, k)$, $q = m + k = s_w$, and since $w(i) = k + 1$ with $i < m$, we have $w(m) \ge k + 2$ and $w(m+k+1) \ge k + 2$. Replacing $w(m+k) = k$ by $k + 1$ preserves $u(m+1) < u(m+2) < \dots$ (giving $1, \dots, k-1, k+1 < u(m+k+1)$), $u(m) = w(m) \ge k + 2 > k + 1 = u(m+k) \ge u(m+1)$, and $s_u = m + k = s_w$ (since $u(j) \le k+1 < u(m)$ for $m < j \le m+k$ and $u(j) = w(j) > u(m)$ for $j > m+k$).
- **$t < m$ and $q > m$:** $\lambda_m < k$, so ($*$) for $r = m$ forces $w(m) < k$ (otherwise $k \in \{1, \dots, \lambda_m\}$), giving $w(m+1) < w(m) < k = w(q)$ and hence $q \ge m + 2$; also $w(q+1) \ge k + 2$ (as $w(i) = k + 1$ with $i < m < q$), preserving $u(m+1) < u(m+2) < \dots$, $u(m) > u(m+1)$, and $s_u = s_w$ (since $u(q) = k + 1 > w(m) = u(m)$).

### Issue 2 (Justification Gap — `PROOF.md` L45, Lemma 2): $\beta_{i+k} = \beta_{i+k+1}$ case
L45 states that $\pi_j(\kappa_\beta) = \kappa_\beta$ for $\beta_j \le \beta_{j+1}$ *"follows from $\kappa_\beta = \pi_{u(\beta)} x^\lambda$ and $\pi_j^2 = \pi_j$"*. While true for $\beta_j < \beta_{j+1}$ (where $s_j$ is a left descent of $u(\beta)$), when $\beta_j = \beta_{j+1}$ the reflection $s_j$ need not be a left descent of $u(\beta)$ (e.g., $\beta = (1,2,2)$, $j = 2$, $u(\beta) = s_1 s_2$). Instead, setting $r = u(\beta)^{-1}(j)$, minimal length of $u(\beta)$ in $u(\beta)W_\lambda$ gives $u(\beta)^{-1}(j+1) = r + 1$ with $\lambda_r = \lambda_{r+1}$ and $s_j u(\beta) = u(\beta) s_r$ (length $+1$), so by braid relations and symmetry of $x^\lambda$ in $(x_r, x_{r+1})$, $\pi_j \pi_{u(\beta)} x^\lambda = \pi_{u(\beta)} \pi_r x^\lambda = \pi_{u(\beta)} x^\lambda = \kappa_\beta$. Please add this 1–2 sentence justification.

### Issue 3 (Minor Edge Cases & Cosmetic Macro — `PROOF.md` L15, L51, L61)
1. **Empty composition $\alpha = 0$ ($m = 0$):** Lemma 3 (L51–53) assumes $\lambda_1 \ge \dots \ge \lambda_m > 0$; add an explicit 1-sentence remark handling $\alpha = 0$ ($\overline{\kappa}_0 = 1 = \overline{\mathfrak{S}}_{\mathrm{id}}$, $\eta(0) = \emptyset$, $\xi(1) = 0$) so Section 3–4 explicitly cover all compositions.
2. **Domain of $a, b, c$ in Lemma 3(1) (L61):** Explicitly state $1 \le a < b < c$ (since $c_a \ge c_b$ only holds for positive indices, and $w(0) = 0$ would otherwise create a spurious triple with any inversion).
3. **Custom LaTeX macro `\nilsim` (L15):** Replace the paper-internal macro `\nilsim` with standard LaTeX (e.g., `$\overset{\bullet}{\sim}$`).

---

## 3. Verified Sound Sections (No Issues Found)
- **Section 1 (Shift reduction):** $\gamma$-equivariance of $\overline{\kappa}_\alpha$, $\xi$, and $\eta(\alpha)$ verified.
- **Section 2 (Lemma 1):** $\partial_i(\overline{\mathfrak{S}}_w)$, $x_i = \overline{\mathfrak{S}}_{s_i} - \overline{\mathfrak{S}}_{s_{i-1}}$, $\xi\partial_i = \partial_i\xi$, $\xi(x_i) = 0$, and $\xi\pi_i = \pi_i\xi$ on $\overline{R}$ verified airtight.
- **Section 3 (Lemma 3(1), 3(2), 3(3) except L77, 3(4)):** $132$-avoidance, gapless lower inversion set ($*$), left-descent bijection with $\eta(\lambda)$, $\kappa_{\lambda-\delta_i}$ formula, $i=t=m$ base case, L78–82 transition steps, and Remark 8.4 lifting to $\overline{R}$ verified airtight.
- **Section 4 (Demazure induction):** All cases ($\ell < j$, $\ell > j+1$, and all four $(A, B) \in S_{<j}$ membership subcases for $\ell \in \{j, j+1\}$) verified airtight.

---

## 4. Re-Audit Verification (`#1092`) — PASS

Re-read the complete patched `targets/hardt-2412.06976-conj7.5/PROOF.md` (111 lines):
1. **Issue 1 (`PROOF.md` L77–81, Lemma 3(3)):** Cleanly split into the three exhaustive subcases ($q \le m$; $i < t = m$ with $q = m+k = s_w$, $w(m) \ge k+2$, $w(m+k+1) \ge k+2$; and $t < m, q > m$ with $\lambda_m < k$, $w(m) < k$, $q \ge m+2$, $w(q+1) \ge k+2$). Every inequality and boundary case (including $k=1$, e.g. $\lambda = (1,1)$) is now verified exact, yielding last descent $r = m$ and $s_u = s_w$ in all cases.
2. **Issue 2 (`PROOF.md` L45, Lemma 2):** Cleanly justified all three cases ($\beta_j > \beta_{j+1}$, $\beta_j < \beta_{j+1}$, and $\beta_j = \beta_{j+1}$ via minimal coset representative $u(\beta) \in u(\beta) W_\lambda$ forcing $r' = r + 1$, $s_j u(\beta) = u(\beta) s_r$, and $\pi_r(x^\lambda) = x^\lambda$).
3. **Issue 3 (`PROOF.md` L15, L61):** Replaced `\nilsim` with `\overset{\bullet}{\sim}`, explicitly handled $\alpha = 0$ ($\overline{\kappa}_0 = 1 = \overline{\mathfrak{S}}_{\mathrm{id}}$, $\eta(0) = \emptyset$, $\xi(1) = 0$), and specified $1 \le a < b < c$ in Lemma 3(1).
4. **Independent Verifier:** `.venv/bin/python -u targets/hardt-2412.06976-conj7.5/notes/check-check-1.py` (untouched since initial audit) passed cleanly (exit `0`, `PASS`).

**Final Verdict:** **PASS**. Ready for Gate 3 novelty verification.
