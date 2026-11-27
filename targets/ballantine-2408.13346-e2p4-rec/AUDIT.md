# Adversarial Audit Report (`audit-1`): `targets/ballantine-2408.13346-e2p4-rec/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Cristina Ballantine, George Beck, and Mircea Merca, *Partitions and elementary symmetric polynomials – an experimental approach*, `arXiv:2408.13346v1` (`2024-08-23`), Section 1, conjectured order-$22$ linear recurrence for $e_2p_4(n)$ (`main.tex` L89–91)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2408.13346/main.tex`
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against `tools/.arxiv_cache/eprint/2408.13346/main.tex`:
- Definitions of $\mathcal{P}(m,n)$, $p_m(n)$, $e_j(\lambda)$, and $e_j p_m(n)$ (`main.tex` L54, L61–67, L84–85) match `TARGET.md` and `PROOF.md`.
- The conjectured linear recurrence for $e_2 p_4(n)$ (`main.tex` L89–91) matches `TARGET.md` L22–24 and `PROOF.md` L67–73 term-for-term (every sign and coefficient verified).
- Checked Section 3 of `main.tex` (L259–320): the authors only establish modular generating functions modulo $2, 3, 4$ (Theorem 2) and do not derive the exact rational generating function $N(q)/D(q)$ over $\mathbb{Z}[[q]]$ or prove the conjectured recurrence.
- Boundary convention (`main.tex` L62): $\mathcal{P}(4,n) = \emptyset$ for $0 \le n \le 3$, so $e_2p_4(n) = 0$ for $0 \le n \le 3$ and $e_2p_4(4) = e_2(1,1,1,1) = 6$, consistent with $N(q) = 6q^4 + \dots$ and the recurrence holding for all $n \ge 0$.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Section 1 (Bijection & expansion, L7–18):** $(y_1, y_2, y_3, y_4) = (\lambda_1-\lambda_2, \lambda_2-\lambda_3, \lambda_3-\lambda_4, \lambda_4) \in \mathbb{Z}_{\ge 0}^3 \times \mathbb{Z}_{\ge 1}$ is an exact bijection onto $\mathcal{P}(4, n)$ with $|\lambda| = y_1 + 2y_2 + 3y_3 + 4y_4$; both the $9$-term expansion of $e_2(\lambda)$ (L17) and the parenthetical quick-check expression (L18) match identically in $\mathbb{Z}[y_1, y_2, y_3, y_4]$.
- **Section 2 (Rational generating function, L22–56):**
  - All six geometric-series identities (L25–26) hold in $\mathbb{Z}[[x]]$, and variable separation is formally valid in $\mathbb{Z}[[q]]$ since each $[q^n]$ has finitely many nonnegative solutions to $y_1 + 2y_2 + 3y_3 + 4y_4 = n$.
  - Independently checked **every single** factored rational expression on L28–36, common denominator $D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3$ (L41), all $9$ individual polynomial numerators over $D(q)$ (L43–51), and their sum $N(q)$ (L56, degree $16$, coprime to $D(q)$): zero typos, exact identity $D(q) G(q) = N(q)$ in $\mathbb{Z}[[q]]$.
- **Section 3 (Recurrence extraction, L60–74):**
  - Expansion of $D(q)$ (L63, degree $22$, $d_0 = 1$, palindromic $d_j = d_{22-j}$) is exact.
  - Because $\deg N(q) = 16 < 22$, $[q^{n+22}](D(q) G(q)) = [q^{n+22}] N(q) = 0$ for every integer $n \ge 0$. Solving for $e_2p_4(22+n)$ yields the conjectured recurrence verbatim for all $n \ge 0$.

---

## 3. Independent Mechanical Verification

1. Executed `@check-2`'s independent exact-arithmetic verifier:
   - Command: `.venv/bin/python -u targets/ballantine-2408.13346-e2p4-rec/notes/check-check-2.py`
   - Raw output (exit code `0`): `PASS (9-term GF, D(q)/N(q) exact, direct P(4,n) match n=0..40, 22-term recurrence verified)`
2. Executed independent auditor SymPy script confirming L18's quick-check identity, all $9$ factored right-hand sides on L28–36 individually, and $\gcd(N(q), D(q)) = 1$.

---

## 4. Verdict

**PASS.** Gate 2 novelty receipts from all three watchers (`watch-1` `#311`, `watch-5` `#337`, `watch-6` `#317`) are clear. Ready for Gate 3 novelty verification (`<1h`).
