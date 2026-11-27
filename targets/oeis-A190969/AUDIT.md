# Adversarial Audit Report: `targets/oeis-A190969/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T08:59Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary sources:
  - OEIS `A190969` (`https://oeis.org/search?q=id:A190969&fmt=text`, rev `#48`, `2025-11-05 15:22:20`);
  - `google-deepmind/formal-conjectures` (`FormalConjectures/OEIS/190969.lean`, fetched live via `gh api`);
  - Cited reference F. Beukers, *Supercongruences using modular forms*, `arXiv:2403.03301v3` (`SupercongruencesRevise.tex` verified verbatim for Assumption (II), Remark 1.14(2), Theorem 1.15 `thm:CMpoints3`, Corollary `specialcongruence3`, `F_p(t)` definition, Appendix C `Hypergeometric F(1/2,1/2,1/2;1,1|64t)`, and arXiv/journal metadata `Alg. Number Th. 20 (2026) 1727-1768`, DOI `10.2140/ant.2026.20.1727`);
  - ArXiv metadata for Z.-H. Sun `arXiv:1012.3898v2`.
- `targets/oeis-A190969/TARGET.md`
- `targets/oeis-A190969/PROOF.md`
- `targets/oeis-A190969/notes/check-check-2.md` and `targets/oeis-A190969/notes/check-check-2.py`
- Confirmed no `targets/oeis-A190969/CONTESTED.md` exists, and Gate 2 PASS receipts posted by `watch-1` (`#40`), `watch-5` (`#51`), and `watch-6` (`#77`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Fidelity Audit (PASS)

- Live OEIS `A190969` (rev 48) and `FormalConjectures/OEIS/190969.lean` match `TARGET.md` and `PROOF.md` verbatim:
  - $a(0)=0, a(1)=1, a(n)=5a(n-1)-8a(n-2)$;
  - $S(p) = \sum_{k=0}^{p-1} a(4k)\binom{2k}{k}^3 / (-4096)^k \in \mathbb{Z}_{(p)}$ for every odd prime $p$, reducing to `sMod p m` in `ZMod (p^m)`;
  - `conjecture_1`: $S(p) \equiv 0 \pmod{p^2}$ for all odd primes $p$;
  - `conjecture_2`: $S(p) \equiv 0 \pmod{p^3}$ for all odd primes $p \equiv 1, 2, 4 \pmod 7$.
- Zero quantifier, domain, or edge-case drift.

---

## 3. Line-by-Line Mathematical Audit (PASS)

1. **Section 2 (Algebraic decomposition in $K = \mathbb{Q}(\sqrt{-7})$):**
   - Verified Binet formula $a(n) = (\alpha^n - \beta^n)/s$, exact values $\alpha^2 = (9+5s)/2$, $\alpha^4 = (-47+45s)/2$, $\beta^4 = (-47-45s)/2$, $t_1 = (47+45s)/8192$, $t_2 = (47-45s)/8192$, $S(p) = (F_p(t_2) - F_p(t_1))/s$, and exact factorization $(16t-1)^3 - 15^3 t^2 = (t-1)(4096t^2 - 47t + 1)$.
2. **Section 3 (Split primes $p \equiv 1, 2, 4 \pmod 7$, `conjecture_2`):**
   - **Lemma 3.1:** Verified the Jacobi $\theta$/$\eta$-product derivation of $(16t(\tau)-1)^3 + j(2\tau)t(\tau)^2 = 0$, the product identity $t(\tau) = q / \prod_{n=1}^\infty (1 + q^{2n-1})^{24}$, the rigorous analytic bounds $\rho = e^{-\pi\sqrt{7}/2} < 1/50$, $|t(\tau_1)| < 1/50 < 1$, and phase bound $|\phi - \pi/2| < 24/49 < 1/2 < \pi/2$ proving $\mathrm{Im}(t(\tau_1)) > 0$, hence $t(\tau_1) = t_1$ and by conjugation $t(\tau_2) = t_2$.
   - **Lemma 3.2:** Verified norm-Euclidean UFD proof for $\mathcal{O}_K = \mathbb{Z}[\omega]$, quadratic reciprocity $(\frac{-7}{p}) = (\frac{p}{7}) = 1$, and parity step giving $p = x^2 + 7y^2$.
   - **Proposition 3.3:** Checked **every single hypothesis** of Beukers Theorem 1.15 (`arXiv:2403.03301v3`, `\label{thm:CMpoints3}`, lines 610–622, together with its proof via `Corollary \ref{specialcongruence3}` and `Proposition \ref{theta-mirror3}` lines 1642–1730):
     - Assumption (II) with $N = 4$, $\Gamma = \Gamma_0(4) + \langle w_4 \rangle$, $\eta$-product $\Theta(\tau) = \eta(2\tau)^{20}/(\eta(\tau)^8 \eta(4\tau)^8)$ of weight 2, $F(t(\tau)) = \Theta(\tau)$ (verified in Beukers Remark 1.14(2), Appendix C, and `q`-series to $O(q^{26})$).
     - Beukers defines $F_p(t)$ as the exact $p$-truncation $\sum_{k=0}^{p-1} g_k t^k$ (L111), and Theorem 1.15 holds for every prime $p \nmid N$ (no hidden restriction on $p$).
     - Verified $4|\tau_i|^2 = 2 \in \mathbb{Z}$, $4(\tau_i + \overline{\tau_i}) = \pm 2 \in \mathbb{Z}$, $4 \mid c_i = 4y$, $c_1\tau_1 + d_1 = c_2\tau_2 + d_2 = x + ys$ with $|x+ys|^2 = p$ and $\iota(x+ys) \in \mathbb{Z}_p^\times$ under the **same** embedding $\iota: K \hookrightarrow \mathbb{Q}_p$, and $\iota(t_1), \iota(t_2) \in \mathbb{Z}_p$ since $2 \in \mathbb{Z}_p^\times$.
     - Subtracting $F_p(\iota(t_1)) \equiv F_p(\iota(t_2)) \equiv \iota(x+ys)^2 \pmod{p^3 \mathbb{Z}_p}$ and dividing by $\sigma_p \in \mathbb{Z}_p^\times$ ($p \neq 7$) yields $S(p) \equiv 0 \pmod{p^3}$ in $\mathbb{Z}_{(p)}$. Completely airtight.
3. **Section 4 (Inert primes $p \equiv 3, 5, 6 \pmod 7$, `conjecture_1`):**
   - **Lemma 4.1 (Finite Clausen identity):** Verified every step of the self-contained differential-operator derivation in $\mathbb{Q}\llbracket z \rrbracket$ (including Legendre's ODE, chain rule for $y(z)=P_m((1-z)^{1/2})$, operator factorization to $\theta^3 Y = z(\theta-m)(\theta+m+1)(\theta+\frac12)Y$, Pochhammer evaluation, and substitution $z = 4u(1-u)$).
   - **Lemma 4.2:** Verified $p^3 \mid \binom{2k}{k}^3$ for $m < k \le p-1$, the mod-$p^2$ identity $(-1)^k \binom{m+k}{2k} \equiv \binom{2k}{k}/16^k \pmod{p^2\mathbb{Z}_p}$, and the mod-$p$ identity $P_m(1-2u) \equiv H_p(u) \pmod{p\mathbb{Z}_p[u]}$ for every odd prime $p$ (including $p=3, 5$).
   - **Proposition 4.3:** Verified $u_1 = (1+3s)/32$ satisfies $u_1(1-u_1) = 16t_1$, $N(u_1) = 1/16, N(1-u_1) = 1$, $\Delta(E_{u_1}) = 16u_1^2(1-u_1)^2 \in \mathcal{O}_{K,\mathfrak{p}}^\times$ (good reduction at $\mathfrak{p} = p\mathcal{O}_K$ for every odd inert $p$, including $p=3,5$), $j(E_{u_1}) = -3375 = j(\mathcal{O}_K)$, Deuring's criterion (Lang Ch. 13, §4, Thm. 12) for supersingularity of $\widetilde{E}_{u_1}$ over $\mathbb{F}_{p^2}$, Hasse invariant criterion (Silverman Ch. V, Thm. 4.1, valid for all odd $p \ge 3$) giving $H_p(u_1) \in p\mathcal{O}_{K,\mathfrak{p}}$, Galois conjugation $s \mapsto -s$ preserving $\mathfrak{p}$ and sending $t_1 \mapsto t_2$, division by $s \in \mathcal{O}_{K,\mathfrak{p}}^\times$ ($p \neq 7$), and intersection $p^2\mathcal{O}_{K,\mathfrak{p}} \cap \mathbb{Q} = p^2\mathbb{Z}_{(p)}$. Completely airtight.
4. **Section 5 (Ramified prime $p = 7$) & Section 6 (Case exhaustion):**
   - Verified every residue mod $49$ in the explicit $p=7$ computation ($S(7) \equiv 0 + 18 + 29 + 2 + 0 + 0 + 0 = 49 \equiv 0 \pmod{49}$, and $S(7) \equiv 294 \pmod{343}$).
   - Every odd prime $p$ is covered by $p \equiv 1,2,4 \pmod 7$, $p \equiv 3,5,6 \pmod 7$, or $p = 7$.

---

## 4. Independent Verifier Re-Execution (PASS)

Re-executed `.venv/bin/python targets/oeis-A190969/notes/check-check-2.py`:
- Exit code `0`
- Raw output: `PASS (checked Sec 2-5 lemmas, 61 odd primes <= 300 for conj_1, 27 split primes <= 300 for conj_2)`

---

## 5. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python targets/oeis-A190969/notes/check-check-2.py` and paths `targets/oeis-A190969/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
