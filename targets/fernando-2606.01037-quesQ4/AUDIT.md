# Blind Adversarial Audit — `targets/fernando-2606.01037-quesQ4/`

- **Auditor:** `@audit-1` (`auto`)
- **Primary Source Verified:** Neranga Fernando & Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1` (sole live version), `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex`, Section 6, **Question 6.4** (`\label{Q4}`, lines 923–925) and Table 1 (`\label{Tb3}`, line 1085).
- **Files Audited (blind — author `verify.py` and scratch `notes/` not read):**
  - `targets/fernando-2606.01037-quesQ4/TARGET.md`
  - `targets/fernando-2606.01037-quesQ4/PROOF.md`
  - `targets/fernando-2606.01037-quesQ4/notes/check-check-2.md`
  - `targets/fernando-2606.01037-quesQ4/notes/check-check-2.py`
- **Verdict:** **PASS** (re-audit after `#1886` / `#1887` / `#1889` fixes; **Label:** `"written proof, internally audited"`).

---

## 1. Statement & Citation Fidelity

- **Question 6.4 (`\label{Q4}`):** Verbatim match across `draftMay31.tex` L923–925, `TARGET.md` L16–19, and `PROOF.md` L7–9 (all quantifiers, domains, formula for $n$ and $g_{n,q}$, and compiled Section 6 numbering verified; commented example line fixed to `928` in `TARGET.md` L21).
- **Internal paper citations in `PROOF.md`:** Eq. (1.1) (`\label{AB1}`, L74–76), Proposition 2.1 (`\label{lem 2.2}`, L123–125), Lemma 2.5 (`\label{lem 3.2}`, L173–176), and Table 1 (`\label{Tb3}`, L1085: `(4387, 4; 4)`) all verified exact against `draftMay31.tex`.
- **External citations verified:** Lidl–Niederreiter *Finite Fields* Theorems 5.38 & 5.45; Heintz (1983) Theorem 1 / Fulton *Intersection Theory* Example 8.4.6; Cafure & Matera (2006) *Finite Fields Appl.* 12 (2006), 155–185, Theorem 7.1 & Lemma 2.1.

---

## 2. Resolution of Prior FAIL Findings (`#1886`)

All defects identified in the initial blind audit (`#1886`) were patched (`#1887`, `#1889`) and independently re-verified:
1. **`PROOF.md` L205–211 (Case 4, Step 4.5.2 — local expansion at $w^5 + w^4 + w^2 + w + 1 = 0$):** Replaced the erroneous truncated expansion with the exact characteristic-$2$ congruence modulo $(u^2, u t^2)$ retaining both $((\alpha+1)^2 k_0 + \alpha) t^2$ and $+ t u$. Independently verified every new identity over $\mathrm{GF}(2)[\alpha]$ and $\mathbb{F}_{32}$:
   - $F_{\mathrm{red}}(1, \alpha) = \alpha^4(\alpha + 1)^2 \neq 0$, confirming $k_0 \notin \{0, 1\}$;
   - $(\alpha+1)^2(\alpha^6+\alpha^4+\alpha+1)+\alpha^2 = \alpha^8+\alpha^4+\alpha^3+\alpha+1 \equiv \alpha^4+1 \neq 0 \pmod{\alpha^5+\alpha^4+\alpha^2+\alpha+1}$, confirming $c_2 = ((\alpha+1)^2 k_0 + \alpha)/(k_0(k_0+1)) \neq 0$ (hence $e = 2$, double root);
   - $c_3 = ((\alpha+1)^2 + c_2)/(k_0(k_0+1)) = (\alpha^3+\alpha^2+1)^2/(k_0^2(k_0+1)^2) \neq 0$ (`17` in $\mathbb{F}_{32}$), confirming $v_P(dw/dt) = 2$ at all $5$ places (total contribution $10$, giving $g(\mathcal{C}_{\mathrm{red}}) = 5$ and $g(\widetilde{\mathcal{C}}_{\mathrm{red},1}) = 9$).
   - `notes/check-check-2.py` (L454–507) now verifies $c_2 \neq 0$, $c_3 = (\alpha^3+\alpha^2+1)^2/(k_0(k_0+1))^2 \neq 0$, and $F_{\mathrm{red}}(k_0 + t, \alpha + c_2 t^2 + c_3 t^3) \equiv 0 \pmod{t^4}$ across all $5$ roots $\alpha \in \mathbb{F}_{32}$.
2. **`PROOF.md` L289 (Case 6, Step 6.3):** Replaced unproved $\gcd(\widetilde{P}_a, \widetilde{Q}) = 1$ with $\gcd(\widetilde{P}_a, \widetilde{P}_b, \widetilde{Q}) = \gcd(P_0, P_1, Q_0) = 1$ (by invertibility of $(a, b) \leftrightarrow (Y_0, Y_1)$) and noted $\{\widetilde{Q}_2 = 0\}$ symmetry.
3. **`PROOF.md` L230–233 (Case 5) & `TARGET.md` L21:** Scoped Case 5 cleanly to $q = 4$ (with accurate parenthetical $u := y + y^q, z^q = z + c$ for general even $q$), standardized `(k_0, \alpha)` order on L205, and fixed `line 928` in `TARGET.md`.

---

## 3. Complete Mathematical & Computational Audit Summary

- **Main Theorem:** For even $q = 2^m > 2$ ($m \ge 2$), integer $e > 2$, and $n = (q-1) + (q-2)q^2 + q^e + q^{e+2}$, $g_{n,q}(X) = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ is a PP of $\mathbb{F}_{q^e}$ **if and only if $(q, e) = (4, 4)$**.
- **Exhaustive case coverage:**
  - **Lemmas 2.1 & 2.2:** Explicit formula for $g_{n,q} \pmod{X^{q^e}-X}$ and exact fiber-bijection reduction to $(s, \Psi)$ on $\Omega_e$ ($H_e$ for odd $e$, $D_e$ for even $e$).
  - **Case 1 ($e = 3$, all even $q > 2$):** Pigeonhole cubic $T^3 + cT + c \implies s(y) = 0$.
  - **Case 2 (odd $e \ge 5$, all even $q \ge 4$):** Carlitz–Uchiyama ($q = 4$ directly; $q \ge 8$ via $\lambda$-scaling $N_F + N_G < q^{e-1}$).
  - **Case 3 (even $e \ge 8$, all even $q \ge 4$):** Carlitz–Uchiyama on $\mathbb{F}_{q^2} \times \mathbb{F}_q$.
  - **Case 4 ($e = 6$, all even $q \ge 4$):** Explicit Rabin-verified colliding pairs $X_1 \neq X_2 \in \mathbb{F}_{q^6}$ for $2 \le m \le 8$; for $m \ge 9$ ($q \ge 512$), $\mathbb{F}_{q^2} \times \mathbb{F}_{q^3}$ ansatz, Kloosterman count, quadratic-resolvent involution, Gröbner absolute irreducibility of $\mathcal{C}_{\mathrm{red}}$, genus $g(\mathcal{C}_{\mathrm{red}}) = 5$ and unramified Artin–Schreier twist $g(\widetilde{\mathcal{C}}_{\mathrm{red},1}) = 9$ (independently corroborated by auditor Weil zeta functional-equation check over $\mathbb{F}_2, \dots, \mathbb{F}_{64}$), and Hasse–Weil lower bound $3 N_0 \ge (q - 7)/2 - 11\sqrt{q} > 0$.
  - **Case 5 ($(q, e) = (4, 4)$):** Exact 2-orbit action ($z \mapsto z^8$ on $O_1$, $z \mapsto z^4$ on $O_2$) + exhaustive 256-element bijection verification.
  - **Case 6 ($e = 4$, all even $q = 2^m \ge 8$):** Explicit Rabin-verified colliding pairs $X_1 \neq X_2 \in \mathbb{F}_{q^4}$ for all $3 \le m \le 37$; for $m \ge 38$ ($q \ge 2^{38}$), $\mathbb{F}_q$-plane coordinate descent ($\tau$-invariance verified), Möbius conjugation to $G$, degree-$25$ resultant $P_{\mathrm{gen}}$, two $\mathbb{F}_{64}$ specializations giving $[25]$ ($\deg_{X_1}\gcd = 1$) and $[2, 23]$, Dedekind + Jordan monodromy $H = S_{25}$ and $G_{\mathrm{geom}} \supseteq A_{25}$, $2$-transitivity uniqueness & Galois descent of $W_0$ with Bézout degree $\delta \le 288$, and Cafure–Matera Theorem 7.1 + Lemma 2.1 contradiction ($q > 6 \cdot 288^2$, $(q - 287\cdot 286 \lceil\sqrt{q}\rceil - 288)^3 > 125 \cdot 288^{13}$).
- **Independent Verifier Execution (re-run after patches):**
  - Command: `.venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py`
  - AST audit: `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: [16, 17, 18, 854, 855, 856, 857, 859, 860]` (exclusively `pathlib.Path` joins and SymPy symbolic rational expressions over `GF(2)` — zero floating-point arithmetic).
  - Exit code `0`, final output `PASS`.

---

## 4. Handoff
**PASS** — handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 live freshness check (`< 1h`) and `@coordinator` reporting.
