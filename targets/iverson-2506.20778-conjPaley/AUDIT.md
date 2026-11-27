# Adversarial Audit Report: `targets/iverson-2506.20778-conjPaley/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T09:04Z`
- **Target:** Joseph W. Iverson and Dustin G. Mixon, *"Asymmetric SICs over finite fields"*, `arXiv:2506.20778v1` (`2025-06-25`, sole version), Section 4, Conjecture 22 (`\label{conj:Paley}`, `2025.06.25.tex` lines 829–840)
- **Owner:** `attack-1`
- **Checker:** `check-1` (`notes/check-check-1.md`, `notes/check-check-1.py`)
- **Strict Isolation Observed:** Read ONLY primary source `tools/.arxiv_cache/eprint/2506.20778v1/2025.06.25.tex`, `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Did NOT read author `verify.py` or any author scratch `notes/`. Did NOT edit `TARGET.md` or `PROOF.md`.
- **Verdict:** **`FAIL`** *(1 small blocking algebraic-step typo on L126 + 1 unverified theorem number on L49; every core lemma, proof argument, primary-source definition, and exact computation PASS)*

---

## 1. Exact Blocking Issues to Fix in `PROOF.md`

1. **Line 126 (Lemma 3 proof — wrong multiplying factor in algebra step):**
   - Line 125 has:
     $$S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} = s(i, j) S_{\tau(i), \tau(j)} S'_{i, j} S'_{i, k} S'_{k, j}.$$
   - Line 126 currently states: *"Multiplying both sides by $S_{\tau(j), \tau(i)} S'_{j, i}$ (using $S_{\tau(i), \tau(j)} S_{\tau(j), \tau(i)} = -1$ and $S'_{i, j} S'_{j, i} = -1$, whose product is $+1$) yields"* line 127:
     $$S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} S_{\tau(j), \tau(i)} = s(i, j) S'_{i, k} S'_{k, j} S'_{j, i}.$$
   - **Error:** Multiplying both sides of line 125 by $S_{\tau(j), \tau(i)} S'_{j, i}$ actually yields $S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} S_{\tau(j), \tau(i)} S'_{j, i} = s(i, j) S'_{i, k} S'_{k, j}$ (putting $S'_{j, i}$ on the LHS and removing it from the RHS).
   - **Fix:** Replace line 126 with: *"Multiplying both sides by $S_{\tau(j), \tau(i)}$ (using $S_{\tau(i), \tau(j)} S_{\tau(j), \tau(i)} = -1$ and $-S'_{i, j} = S'_{j, i}$) yields"* — which directly produces line 127.

2. **Line 49 (Lemma 1(2) — inaccurate/unverified theorem number in Kantor 1969):**
   - Line 49 cites `Kantor (1969, Theorem 5; cited in 2025.06.25.tex, line 820)`.
   - Kantor's 3-page paper (*J. Combin. Theory* 6 (1969), 279–281) proves $\mathrm{Aut}_w(H) \cong P\Sigma L(2, q)$ for $q > 11$ (and Iverson–Mixon cite it as `[Kantor:69]` without a theorem number on `2025.06.25.tex` line 820), whereas "Theorem 5" is an unverified/mismatched theorem label (in secondary references "Theorem 5" is associated with Hall's $q = 11 / M_{12}$ exception).
   - **Fix:** Drop the unverified `"Theorem 5"` qualifier and cite `Kantor (1969; cited in 2025.06.25.tex, line 820)`.

---

## 2. What Passed (No Rework Needed)

- **Primary-source fidelity (`2025.06.25.tex`):** Verified all internal numbering (`Definition 1`, `Theorem 2`, `Lemma 3`, `Definition 11`, `Definition 13`, `Theorem 15`, `Lemma 16`, `Proposition 17`, `Examples 18–21`, `Conjecture 22` / `\label{conj:Paley}` lines 829–840) and every quantifier/definition verbatim. Convention invariance under row/column sign switches and transpose $H^\top = I - S$ (including strong SIC equivalence via $\iota(g_0, g_0)$) is completely sound.
- **Section 1 & Lemma 1:** Prime-power parity ($q = p_0^r \equiv 3 \pmod 4 \implies p_0 \equiv 3 \pmod 4$, $r$ odd, Galois invariance of $\chi$), $S_{a, b} = \chi(\det(v_a, v_b))$, matrix identities, $P\Gamma L(2, q)$ action formula, homomorphism $\psi$, and exact two-orbit action on $\Delta$ and $X^2 \setminus \Delta$ via $2$-transitivity of $PSL(2, q)$ are all airtight.
- **Section 2, Lemma 2 & Lemma 3 (modulo L126 above):** Verified every boundary term of $B^{\mathrm{col}}$ and $B(u, v)$, smoothness of $y^2 = x(x - r_1)(x - r_2)$ in all odd characteristics including $p_0 = 3$, Hasse bound $2\sqrt{q} + 4 < q - 3$ for all $q \ge 19$, Case 2a–2c inner products, $\Delta$-restriction sign normalization, uniqueness of transpose partner via $|\langle v_{ij}, v_{ji}\rangle| = d - 4$, constancy of $s(i, j) = \eta$, and sign reconstruction $\delta_k$ in Lemma 3.
- **Section 3, Lemma 4 & Theorem 1 (Part (a)):** Same-row and same-column triple-product bounds ($\le 2$ per row/column), $m_2 \ge d/2 - 2$, column exclusion leaving $\ge 6$ candidate rows, $|R_1 \cap R_3| \ge d/2 - 2$ vs $(d + 2\sqrt{q} + 4)/4$ eliminating all $q \ge 23$, $PSL(2, 19)$ reduction and 17 square-scaling orbits eliminating $q = 19$, transpose symmetry for columns, and the slick $\sigma(\infty) = 0$ summation trick in Theorem 1 (verified explicitly including the edge case $y = \sigma(i) = \infty$) yielding a skew-Hadamard $H'$ and contradicting Kantor's theorem via Lemma 3 are all completely airtight.
- **Section 4, Theorem 2 (Part (b)) & Corollary:** Exact match between $\Phi(s, t) = -\frac{1}{2}(s + t) + \frac{\mathrm{i}}{2}(s - t)$ and `lem.gram matrix`, identity $\Phi(ac, be) = ae\,\overline{\Phi(ab, ce)}$, all 4 Gram cases for $\pi = \psi(g_0)$, non-degeneracy and construction of $U$ over $\mathbb{F}_{p^2}^d$ (including $p = 3$), Step 2 triple-product contradiction handling $\varepsilon \in \{\pm 1\}$ uniformly for all odd $p \equiv 3 \pmod 4$ (including $p = 3$), and Dirichlet + $q = 7^r$ ($r \ge 3$ odd) corollary are all completely airtight.
- **Independent mechanical verification:** Re-executed `.venv/bin/python -u targets/iverson-2506.20778-conjPaley/notes/check-check-1.py` -> exit code `0`, raw `PASS` (`27.45s`).
- **Gate 2 novelty receipts:** All clear (`notes/novelty-gate2-watch-{1,5,6}.md`).

## 3. Handoff

Returned to `@attack-1` and `@triage` for the quick 2-line fix (`PROOF.md` L126 and L49). Upon fix, ready for immediate re-audit PASS and Gate 3 novelty check.

---

## 4. Re-Audit Verdict (`@audit-2`, `2026-11-27T09:16Z`) — **PASS**

Verified `@attack-1`'s two fixes in `targets/iverson-2506.20778-conjPaley/PROOF.md`:
1. **Line 49:** Unverified `"Theorem 5"` qualifier removed; now cites `Kantor (1969; cited in 2025.06.25.tex, line 820)` cleanly.
2. **Line 126:** Multiplying factor corrected to $S_{\tau(j), \tau(i)}$ (using $S_{\tau(i), \tau(j)} S_{\tau(j), \tau(i)} = -1$ and $-S'_{i, j} = S'_{j, i}$), algebraically yielding line 127 verbatim.

All prior checks (verbatim primary-source fidelity against `2025.06.25.tex`, Sections 1–4 mathematical audit, Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`, and independent verifier `.venv/bin/python -u targets/iverson-2506.20778-conjPaley/notes/check-check-1.py` raw `PASS`) remain clear.

**Final Verdict: PASS.** Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.
