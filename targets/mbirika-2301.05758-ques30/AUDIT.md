# Adversarial Audit Report (`audit-1`): `targets/mbirika-2301.05758-ques30/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** aBa Mbirika, Janee Schrader, & Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of $k$ consecutive Pell, balancing, and related numbers*, `arXiv:2301.05758v3` (*J. Integer Sequences* 26(6), 2023, Art. 23.6.4), Section 6.1, **Question 30** (L1199–1216)
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `@scout-11` patch in `#649`), `notes/check-check-2.md`, `notes/check-check-2.py` (re-checked in `#652`), and primary source `tools/.arxiv_cache/eprint/2301.05758/aBa_Janee_Jurgen_JIS_final_published_version_for_arXiv.tex` (verified live arXiv latest version is `2301.05758v3`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Statement Fidelity
- Verified verbatim against `aBa_Janee_Jurgen_JIS_final_published_version_for_arXiv.tex` (global `[theorem]` counter in L86–100):
  - **Convention 1** (L183–189), **Definitions 3, 6, and 7** (L233, L260, L265), and **Question 30** (Section 6.1, L1199–1216) match `TARGET.md` and `PROOF.md` verbatim (prior FAIL Issue 2 `Definitions 4–5` -> `Definitions 3, 6, and 7` resolved across `TARGET.md` L8/L16 and `notes/check-check-2.{md,py}`).
  - All six sequence recurrences/initial conditions and all three Question 30 observations match verbatim.

## 2. Adversarial Line-by-Line Mathematical Audit
- **Section 1 (Lemma 1 & Corollary 2, L13–41):** Binet formulas, both consecutive-sum identities, and all four exact square-sum formulas for $S_C(k,n), S_B(k,n), S_c(k,n), S_b(k,n)$ verified line-by-line.
- **Section 2 (Lemmas 3–4, L47–90):** Pure periodicity via determinant-$1$ companion matrices and all modular / $p$-adic valuations ($p = 2, 3, 7$, including $B_k \equiv 3k \pmod{2^{a+4}}$, $B_k \equiv 51k \pmod{2^{a+6}}$, $P_k \equiv 3k \pmod{2^{a+3}}$ for $4 \mid k$, $\nu_3(B_k) = 1+\nu_3(k)$ for even $k$, and $\nu_7$ for $3 \mid k$) verified line-by-line.
- **Section 3 (Theorems A–C, L95–125):** Closed forms $\mathcal{G}_C^2(k) = \gcd(k, B_k)$, $\mathcal{G}_B^2(k) = \frac{1}{2}\mathcal{G}_C^2(k)$ ($k$ even) / $\mathcal{G}_C^2(k)$ ($k$ odd), and $\mathcal{G}_c^2(k) = \gcd(k, 3B_k)$ (establishing Question 30 Bullets 1–2 for all $k \ge 1$) verified completely airtight.
- **Section 4 (Theorem D, L131–192 — re-audited after `#649` patch):**
  - Prior FAIL Issue 1 (`PROOF.md` L137) is completely resolved: L137 now explicitly proves evenness of $b_r$ from $b_0 = 0$ and $P_{2r-1} \equiv 1 \pmod 4$ for all $r \ge 1$ (from Lemma 4.1: $P_{2r-1} \equiv 1$ or $5 \pmod 8$), giving $4 \mid b_r^2$ for every $r \ge 0$.
  - Both even-$k$ ($S_b(k,n)/4 = B_k w_n + c_1 x_n + c_0$) and odd-$k$ ($S_b(k,n)/4 = B_k y_n^2 + d_1 y_n + c_0'$) quadratic reductions, integrality proofs, reverse divisibility for all primes $p$ (including $p = 2, 3, 7$ and exact $\nu_2(\mathcal{G}_b^2(k)) = \nu_2(k)+1$ for even $k$ / $2$ for odd $k$), and Bullet 3 ($\mathcal{G}_b^2(k) \equiv 0 \pmod 4$) verified completely airtight.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Re-executed `.venv/bin/python -u targets/mbirika-2301.05758-ques30/notes/check-check-2.py` -> exit code `0`, `PASS` (verified all 6 sequences, Lemma 1, Corollary 2, Lemma 4, Theorems A–D, all 4 closed forms, and all 3 Question 30 observations for $1 \le k \le 120$).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#514`, `watch-5` `#521`, `watch-6` `#520`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
