# Adversarial Audit Report (`audit-3`) — `targets/campbell-2509.16034-conj1/`

- **Verdict:** **PASS** (rescoped strictly to Open Problems `(c1)` and `(c2)` per `notes/contest-ruling-audit-3.md`)
- **Charter label:** `"written proof, internally audited"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py` or `notes/screen-*`)
- **Audited at (UTC):** 2026-11-27 01:51 UTC
- **Files inspected:** `TARGET.md`, `PROOF.md`, `notes/contest-ruling-audit-3.md`, `notes/contest-helper-campbell.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, `notes/audit-helper-campbell.md`, and primary source `tools/.arxiv_cache/eprint/2509.16034/ReducedComplexityV85.tex` (`arXiv:2509.16034v1`, published *INTEGERS* 26 (2026), #A34).

---

## 1. Primary-Source Fidelity & Rescope Compliance

- Directly verified `arXiv:2509.16034v1` (`ReducedComplexityV85.tex` Section 1 lines 75–113, Section 2.1 lines 180–348, Section 3 lines 675–699):
  - **Prior results cited from Section 2.1:** Theorem 1 (`\ref{tm_red}`, proving $\rho_{\mathbf{t}}^{\mathrm{red}}(n) = 2(M_n - m_n + 1)$, realization of every $(\text{first letter}, r) \in \{0,1\} \times [m_n+1, M_n+1]$ by sliding-window discrete continuity + bit-complement closure, and $2$-regularity of $\rho_{\mathbf{t}}^{\mathrm{red}}$), Lemma 2 (`\ref{tm_max_min}`, $j \ge 2$), and Lemma 3 (`\ref{tm_mod4}`, $n \ge 1$) all match `PROOF.md` lines 21–29 and 74 verbatim (also verified $n = 1$ directly for Lemma 3: $(m_4, M_4) = (1, 3)$ and $(m_6, M_6) = (2, 4)$).
  - **Rescope compliance:** Per `notes/contest-ruling-audit-3.md`, `TARGET.md` and `PROOF.md` claim **strictly** the two unsettled Section 3 open problems — **(c1)** explicit evaluation of the sign of $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$ in the nonzero case (lines 691–694) and **(c2)** explicit recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$, full recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$, and $2$-regularity (lines 680–682, 695–696) — while explicitly crediting `the-omega-institute/trureturing` (Sept 2026, commits `832f82f782` & `96baee8682`) for prior settlement of the odd recurrence, eq. (11) `displayconjecture`, and non-$k$-automaticity.

---

## 2. Adversarial Line-by-Line Audit of `PROOF.md`

Every lemma, parity calculation, $2$-kernel closure, $2$-regularity step, and sign formula in `PROOF.md` was checked independently and holds without gap:

1. **Lemma 1 (Weighted run-count formula, lines 35–42):** Alternating binary words of length $r$ yield $1$ abelian class for even $r$ and $2$ abelian classes for odd $r$; checked the closed form $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n) = \frac{3}{2}(M_n - m_n + 1) + \frac{(-1)^{m_n} + (-1)^{M_n}}{4}$ across all four parity pairs of $(m_n, M_n) \bmod 2$. Exact.
2. **Theorem 1(1) (Explicit recursion for $4n, 4n+2, 2n+1$, lines 51–54 & 62–67):** Using Lemma 3 (`tm_mod4`, $n \ge 1$), $[m_{4n}+1, M_{4n}+1] = \{2n + m_{n+1}\} \sqcup (2n + [m_{n+1}+1, M_{n+1}+1])$ and $[m_{4n+2}+1, M_{4n+2}+1] = (2n + [m_{n+1}+1, M_{n+1}+1]) \sqcup \{2n + 2 + M_{n+1}\}$. Parity invariance under $+2n$ yields $\rho(4n) = \rho(n+1) + 1 + a_{n+1}$ and $\rho(4n+2) = \rho(n+1) + 1 + b_{n+1}$ for all $n \ge 1$. Exact.
3. **Theorem 1(2) (Coupled mod-2 recurrences & $2$-automaticity, lines 55–58 & 68–73):**
   - Reducing Lemma 2 (`tm_max_min`) mod $2$ gives $a_{2j} \equiv 1 - b_{j+1}$, $b_{2j} \equiv 1 - a_j$, $a_{2j+1} \equiv b_{j+1}$, $b_{2j+1} \equiv a_{j+1} \pmod 2$ for $j \ge 2$, with base values $(a_1,b_1)=(0,0), (a_2,b_2)=(0,1), (a_3,b_3)=(1,0)$.
   - For the shifted sequences $a'_k := a_{k+1}, b'_k := b_{k+1}$ ($k \ge 0$), direct audit confirms all four identities $a'_{2k} = b'_k$, $b'_{2k} = a'_k$, $a'_{2k+1} = 1 - b'_{k+1}$, $b'_{2k+1} = 1 - a'_k$ hold for **all $k \ge 0$** (including $k = 0$ and $k = 1$, with zero boundary exceptions!).
   - Audited the complete $8 \times 2$ transition table on $\{a'_k, b'_k, a'_{k+1}, b'_{k+1}, 1-a'_k, 1-b'_k, 1-a'_{k+1}, 1-b'_{k+1}\}$ under $k \mapsto 2k$ and $k \mapsto 2k+1$: exact closure with all 8 states reachable and pairwise distinct on $k \in \{0,1,2,3\}$. Hence $(a'_k)_{k \ge 0}$ and $(b'_k)_{k \ge 0}$ (and thus $(a_k)_{k \ge 1}, (b_k)_{k \ge 1}$) are $2$-automatic with explicit $8$-state LSD DFAO. *(Minor non-blocking editorial nits in `PROOF.md`: unused notation $u_k, v_k$ on line 70, and line 73 mentions possible $k=1$ boundary adjustments that are not even needed since the identities hold for all $k \ge 0$.)*
4. **Theorem 1(3) ($2$-regularity, lines 74–76):** From Lemma 1, $4\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n) = 3\rho_{\mathbf{t}}^{\mathrm{red}}(n) + (-1)^{m_n} + (-1)^{M_n}$ is a $\mathbb{Z}$-linear combination of $2$-regular sequences ($\rho_{\mathbf{t}}^{\mathrm{red}}$ by Theorem 1 of `2509.16034v1`; $(-1)^{m_n} = 1 - 2a_n$ and $(-1)^{M_n} = 1 - 2b_n$ are $2$-automatic, hence $2$-regular). Since $\mathbb{Z}$ is Noetherian, an integer-valued sequence whose $4\times$ multiple is $2$-regular is itself $2$-regular (Allouche–Shallit §16.1). Exact.
5. **Theorem 2 (Exact sign formula — Open Problem `(c1)`, lines 82–90):** Subtracting Theorem 1(1) gives $\rho(4n+2) - \rho(4n) = b_{n+1} - a_{n+1} = \frac{(-1)^{m_{n+1}} - (-1)^{M_{n+1}}}{2} \in \{-1, 0, +1\}$ for all $n \ge 1$. When nonzero ($a_{n+1} \ne b_{n+1}$), $a_{n+1} = 1 - b_{n+1}$ forces $\mathrm{sgn}(\rho(4n+2) - \rho(4n)) = 2b_{n+1} - 1 = (-1)^{1 - b_{n+1}} \in \{-1, +1\}$, computed explicitly in $O(\log n)$ steps by the $8$-state $2$-automatic DFAO on the binary digits of $n$. Exact.

---

## 3. Independent Exact Verification & Novelty

- **Independent verifier (`notes/check-check-1.py`):** Re-executed via `.venv/bin/python targets/campbell-2509.16034-conj1/notes/check-check-1.py` — exit code `0`, `PASS` in `3.09s` (direct factor enumeration $1 \le n \le 120$, paper prefix $1..19$, recurrences & closed form $1 \le n \le 20{,}000$, $2$-kernel sizes $8/8$ shifted & $9/10$ unshifted, exact sign $1 \le n \le 4999$).
- **Additional audit verification (`notes/audit-helper-campbell.md` §2):** Confirmed $0$ exceptions to all four shifted identities for $0 \le k \le 5000$ (incl. $k=0,1$), exact $8 \times 2$ state closure, and $0$ mismatches running the $8$-state LSD DFAO for $b_{n+1} - a_{n+1} = \rho(4n+2) - \rho(4n)$ across $1 \le n \le 4999$.
- **Novelty check (`notes/contest-helper-campbell.md` & `notes/audit-helper-campbell.md` §3):** Clear for `(c1)` and `(c2)` across `the-omega-institute/trureturing` (which explicitly states the nonzero sign, recursion for $\rho(4n)$, and full recursion remain unsettled), `trureturing-mdbook`, `facebookresearch/atlas-lean` (only formalizes $\rho^{\mathrm{red}}_{\mathbf{t}}$ and paperfolding $\rho^{\mathrm{red}}_{\mathbf{f}}, \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{f}}$), `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, arXiv, Zenodo, Crossref, and web search.
- **Gate 3:** Requested from `@watch-1 @watch-5 @watch-6` prior to final report to `@coordinator`.
- **What is not established:** Internal adversarial audit + exact computation up to $n = 20{,}000$, not peer review or a Lean formalization.
