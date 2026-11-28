# Independent Check Report (`@check-2`): `targets/fernando-2606.01037-quesQ4/`

**Verdict:** `PASS` (re-checked after `#1886` / `#1887` audit fixes)

## 1. Primary Source & Restatement Verification
- **Primary source:** `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex` (Neranga Fernando and Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, `arXiv:2606.01037v1`, Section 6, lines 923–926, `\label{Q4}`).
- **Match check:** `TARGET.md` quotes Question 6.4 (`\label{Q4}`) verbatim across all quantifiers ($q > 2$ even, $e > 2$ positive integer, $n = (q-1)q^0 + (q-2)q^2 + q^e + q^{e+2}$, $g_{n,q} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ on $\mathbb{F}_{q^e}$) and matches compiled section/question numbering (`Question 6.4`), with line `928` fixed in `TARGET.md`.
- **`PROOF.md` (`#1886` / `#1887` re-check):**
  - **Step 4.5.2 (`L205–211`):** Verified exact Taylor expansion of $F_{\mathrm{red}}(k_0 + t, \alpha + u) \equiv 0 \pmod{u^2, u t^2}$ at $(k_0, \alpha)$ for all $5$ roots $\alpha \in \mathbb{F}_{32}$ of $w^5 + w^4 + w^2 + w + 1 = 0$, including $c_2 = ((\alpha+1)^2 k_0 + \alpha)/(k_0(k_0+1)) \neq 0$ and $c_3 = ((\alpha+1)^2 + c_2)/(k_0(k_0+1)) = (\alpha^3 + \alpha^2 + 1)^2 / (k_0^2(k_0+1)^2) \neq 0$.
  - **Step 6.3 (`L289`):** Verified $\gcd(\widetilde{P}_a, \widetilde{P}_b, \widetilde{Q}) = \gcd(P_0, P_1, Q_0) = 1$ and $\{\widetilde{Q}_2 = 0\}$ symmetry.
  - **Case 5 (`L230–233`):** Scoped explicitly to $q = 4$ (with general-$q$ parenthetical remark using $u := y + y^q$ and $z^q = z + c$).

## 2. Independent Exact Verifier (`notes/check-check-2.py`)
- **Methodology:** Zero-floating-point Python using `int`, bitmask $\mathbb{F}_{2^d}$ arithmetic, and SymPy over $\mathrm{GF}(2)$, written directly from `draftMay31.tex` and `PROOF.md`.
- **Checks performed:**
  1. Verbatim `draftMay31.tex` & `Question 6.4` numbering match against `TARGET.md`.
  2. Exhaustive finite-field verification of Lemmas 2.1 & 2.2 (including $\sum_{a \in \mathbb{F}_q} (X+a)^n = g_{n,q}(X^q + X)$) on $\mathbb{F}_{4^3}, \mathbb{F}_{4^4}, \mathbb{F}_{4^5}, \mathbb{F}_{8^3}, \mathbb{F}_{8^4}$.
  3. Case 1 root checks for $q \in \{4, 8, 16, 32\}$; Case 2 & Case 3 exact integer inequalities ($4(q-2)^2 > 9q$, $4^e > 24 \cdot 4^{e/2}$, $q^{e/2} - q^4 + 3q^3 - 2q^2 > 0$).
  4. Case 4 symbolic checks over $\mathrm{GF}(2)$ (`w+w^{q^3}`, `N_3+N_3'`, $\mu^5 A$ identity, resultant of $F_{\mathrm{red}}$, Gröbner basis `[1]` for $r \in \{0,1,2\}$, exact $\mathbb{F}_{32}$ mod-$t^4$ check of $c_2 \neq 0$ and $c_3 = (\alpha^3 + \alpha^2 + 1)^2 / (k_0(k_0+1))^2 \neq 0$ across all $5$ roots of $w^5 + w^4 + w^2 + w + 1 = 0$, local series $s(\pi) = \pi^2 + \pi^5 + \pi^9 + O(\pi^{10})$ and $k(\pi) = \pi^{-4} + \pi^{-1} + O(\pi)$), Kloosterman count check, and explicit colliding pairs $X_1 \neq X_2 \in \mathbb{F}_{q^6}$ for all $m \in \{2, \dots, 8\}$.
  5. Case 5 exhaustive $256$-element permutation verification of $g_{4387, 4}$ over $\mathbb{F}_{256}$ and exact $(u,c,r)$ formula check for $q \in \{4, 8, 16\}$.
  6. Case 6 symbolic Möbius conjugation & $P_{\mathrm{gen}}(A, B; X_0)$ resultant ($\deg 25$, $\mathrm{LC} = A^3(A+1)^2(B+1)^3$), $\mathbb{F}_{64}$ DDF factorizations (`[25]` with $\deg_{X_1}\gcd_K(f_0, f_1) = 1$ and $G(X_0, X_1) = (A_1, B_1)$, and `[2, 23]`), exact integer Cafure–Matera inequality check for $m \ge 38$, and explicit colliding pairs $X_1 \neq X_2 \in \mathbb{F}_{q^4}$ for every $m \in \{3, \dots, 37\}$.
- **Run command & output:**
  ```text
  .venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py
  [PASS] Primary source arXiv:2606.01037v1 Question 6.4 (\label{Q4}) verbatim & numbering verified.
  [PASS] Lemmas 2.1 & 2.2 exhaustively verified on F_{4^3}, F_{4^4}, F_{4^5}, F_{8^3}, F_{8^4}.
  [PASS] Cases 1 (e=3, q=4..32), 2 (odd e>=5), and 3 (even e>=8) verified.
  [PASS] Case 4 (e=6): symbolic identities, Groebner irreducibility, genus-9 Hasse-Weil, & m=2..8 collisions verified.
  [PASS] Case 5 ((q,e)=(4,4)) exhaustive 256-element bijection & general (u,c,r) formulas verified.
  [PASS] Case 6 (e=4, q>=8): Mobius conjugation, deg-25 P_gen, F_64 monodromy, Cafure-Matera (m>=38), and m=3..37 collisions verified.
  PASS
  ```
  (Exit code `0`.)

## 3. Gate Status
- Gate 1: `PASS` (recorded in `TARGET.md`).
- Gate 2: `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
