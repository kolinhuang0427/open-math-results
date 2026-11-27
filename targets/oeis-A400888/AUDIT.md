# Adversarial Audit Report (`audit-3`) — `targets/oeis-A400888/`

- **Verdict:** **PASS**
- **Charter label:** `"written proof, internally audited"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py` or author scratch `notes/screen-*` / `notes/attack-*` / `notes/triage-brief.md`)
- **Audited at (UTC):** 2026-11-27 04:26 UTC
- **Files inspected:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, `notes/audit-helper-a400888.md`, and live OEIS JSON for `A400888` (rev 16), `A000361` (rev 53), `A000360` (rev 154), `A284556` (rev 28), `A002487` (rev 719).

---

## 1. Primary-Source Fidelity (Live OEIS `A400888` rev 16 & `A000361` rev 53)

Directly verified live OEIS JSON (`2026-11-27T04:06Z`, `notes/audit-helper-a400888.md` §1):
- **OEIS `A400888`** (rev 16, `2026-10-15T16:25:59-04:00`, offset `0,1`, author M. Jeremie Lafitte (Levitas)):
  - Definition of $V(n)$, $(p_n, q_n)$, $u_n = v_n + J c_n = (p_n - e_n, q_n + f_n)^T$, $a(n) = \gcd(p_n - e_n, q_n + f_n)$, PARI/GP recurrence `f(v,c,h)`, `w(n)`, `vecsort(w(n),,4)` (descending), and `a(n)` match `PROOF.md` lines 5–20 verbatim.
  - Conjecture (*"It is conjectured that the sequence is surjective onto the positive integers"*) remains open/unproved on OEIS.
- **OEIS `A000361`** (rev 53, `2026-11-23T16:58:18-05:00`):
  - Modular `fusc` formula $v_j = (((j p_0 - 1) \bmod q_0) + 1 - p_0) \bmod 2$ ($0 \le j < q_0$, $p_0 = \mathrm{A002487}(n)$, $q_0 = \mathrm{A002487}(n+1)$) matches `PROOF.md` lines 17–18 verbatim (and independently verified equal to descending `w(n) mod 2` for $0 \le n \le 99$).

---

## 2. Adversarial Line-by-Line Audit of `PROOF.md`

Every induction, algebraic identity, congruence, norm bound, and analytic inequality was checked independently:

1. **Lemma 1 (Periodicity $V(4n+3) = V(n)$ & column words $V(n(r,t)) = (0^r 1^r)^{t-1} 0^r 1^{r-1}$, L36–88):**
   - Verified $2(x+h)+c-(2c+1)(x\bmod 2) = 2(2y+h)+(b\oplus c)$ for all $(b,c)\in\{0,1\}^2$.
   - Verified $V(4n+3)=V(n)$ via $[n\not\equiv 2] = [2n+1\not\equiv 2]\pmod 3$ and strictly increasing parity-preserving map $2y+b \mapsto 8y+6+b$, giving $a(4^j(n+1)-1) = a(n)$.
   - Verified all four inductions (Steps 1–4) for $n(r,t) = 2^{2t+r-1} - 2^{r-1} - 2 = 2M(r,t)$ ($r\ge 2, t\ge 1$), including base $r=2$ ($t=1 \implies m'=0$ valid), exact identity $2U_j(r) = U_j(r+1) - 2$, strict interval separation $U_{j+1}(r+1)+2 \le 2y \le U_j(r+1)-2 < U_j(r+1)$, and independent derivation from `A000361` ($p_0 = 2tr-2t-1$, $q_0 = 2tr-1$, boundary $(k,i)=(2t-2, r-1)$). **Airtight.**
2. **Lemma 2 (Matrix evaluation & quadratic-form divisibility, L91–126):**
   - Checked left-to-right Stern action $R^{r-1} L^r A^{t-1} = R^{-1} A^t$ giving $(p, q) = (x_t - y_t, y_t)$, and $\gcd(x_t - y_t - tr, y_t + tr - 1) = \gcd(x_t - 1, y_t + tr - 1) = r\gcd(X_t, Z_t)$ with $X_t, Z_t > 0$.
   - Checked $Q(B(x,y)) = -Q(x,y)$ for $Q(x,y) = x^2 - rxy - y^2$, hence $Q(x_t, y_t) = Q(1,1) = -r$, and exact expansion of the Bézout identity $X_t(2+rX_t-r-r^2Y_t) + Z_t(-r-2-rZ_t+2rt) = t((t-1)r - 2)$, forcing $\gcd(X_t, Z_t) \mid t((t-1)r - 2)$. **Airtight.**
3. **Lemma 3 (Elementary cases $r \not\equiv 27 \pmod{30}$, L129–154):**
   - Checked $r=1$ ($n=2$, $w(2)=[5,0]$, $a(2)=1$), even $r\ge 2$ ($t=1$, $\gcd(r+1,2)=1$), odd $r\not\equiv 2\pmod 5$ ($t=2$, exact polynomials $X_2, Z_2$, $\gcd(X_2, Z_2) = \gcd(r-2, 10) = 1$), and odd $r\equiv 2\pmod 5, 3\nmid r$ ($t=3$, exact $X_3, Z_3$, mod-2, mod-3, and $p\mid(r-1) \implies p\mid\gcd(20,15)=5$ contradiction). **Airtight.**
4. **Lemma 4 (Parity lemma, L157–166):**
   - $B^3 \equiv I_2 \pmod 2$ for odd $r$, $t\equiv 2\pmod 3 \implies 2t\equiv 1\pmod 3 \implies x_t$ even $\implies r X_t = x_t - 1$ odd $\implies 2\nmid X_t$. **Airtight.**
5. **Lemma 5 (Algebraic norm bound ruling out $p \mid \gcd(X_t, Z_t)$, L169–202):**
   - Checked $\gamma_m > 0$ and $\gamma'_m < 0$, hence $C_m(r) = \gamma_m \gamma'_m < 0$ is a nonzero integer (and $|C_{3r}(r)| > r(r^2+4)$ for all $r\ge 3$, so $P_0(r) > r(r^2+4)$ strictly).
   - Checked $tr = 2p+r+2$, $r(2t+1) = 4p+3r+4$, $p\mid\gcd(X_t, Z_t) \implies B^{2t+1}(1,1)^T \equiv (-1,1)^T \pmod p$, eigenbasis coordinates over $\mathbb{F}_{p^2}$, $\bar{\alpha}^{2t+1}(\bar{\alpha}+1) = 1-\bar{\alpha}$, both Legendre symbol cases ($\left(\frac{r^2+4}{p}\right)=+1 \implies m=3r+8$; $-1 \implies m=3r$), and ring homomorphism $\mathbb{Z}[\alpha] \to \mathbb{F}_{p^2}$ forcing $p \mid C_m(r)$, contradicting $p > P_0(r)$. **Airtight.**
6. **Lemma 6 (Analytic sieve for all odd $r\ge 3$ with $3\mid r$, L205–265):**
   - **Step 1:** Checked $0 < F_k < (r+1)^k$, $d_q = \mathrm{ord}_{\mathbb{F}_{q^2}^\times}(\bar{\alpha}^2) \ge 2$, $\gcd(q, d_q) = 1$, $q \mid F_{2d_q}$, and $q\mid t, q\mid\gcd(X_t,Z_t) \implies q d_q \mid t$ with $d_q$ odd when $t$ is odd.
   - **Step 2:** Checked $\varphi(d) \ge \sqrt{d}$ for odd $d\ge 1$, integral bound $\sum_{n=Y+1}^\infty \frac{1}{n(\log n)^2} \le \frac{1}{\log Y}$ ($Y>39>e$), $\omega(F_{2d}) < 2d\log_2(r+1)$, split at $D_0 = \lfloor(\log Y)^4\rfloor$ ($\sum_{d=3}^{D_0} d < D_0^2 \le (\log Y)^8$), and $e^u > u^9/9!$ tail convergence giving $\lim_{Y\to\infty} S(Y) = 0$.
   - **Step 3:** Checked CRT construction of $u_0 \bmod W$, $\gcd(a_0, rW) = 1$ (using $r$ odd, $3\mid r$, and all prime divisors of $r$ being $\le Y$), $t = (2p+r+2)/r \le \frac{2}{3}X + \frac{5}{3} \le X$ (for $X\ge 6$), $t\equiv 2\pmod 3$, $\gcd(t, rW) = 1$, and $\gcd(q d_q, rW) = 1$ for every bad prime $q\mid t$.
   - **Step 4:** Checked Case 1 ($q d_q \le X^{1/2}$): CRT residue $a_q \bmod M_q$ ($M_q = r W q d_q \le X^{3/4} < X$), exact coprimality $\gcd(a_q, M_q) = 1$ (since $2a_q + r + 2 \equiv 0 \pmod{qd_q}$ and every prime $\ell\mid qd_q$ exceeds $Y > r+2$), and **Montgomery–Vaughan (1973) Theorem 2** ($\pi(X; M_q, a_q) < \frac{2X}{\varphi(M_q)\log(X/M_q)}$ unconditionally for all $1 \le M_q < X$, $\gcd(a_q, M_q)=1$, independently verified in `notes/audit-helper-a400888.md` §3), yielding $E_1(X) < \frac{2}{5}\frac{X}{\varphi(rW)\log X}$. Checked Case 2A ($\sum_{d=2}^{\lfloor X^{1/5}\rfloor} d \le X^{2/5} \implies E_{2A}(X) \le 2\log_2(r+1) X^{9/10}$) and Case 2B ($d_q$ uniquely determined by $q$, $E_{2B}(X) \le X^{4/5}(1+\log X)$). Checked final PNT in AP subtraction ($\frac{1}{2} - \frac{2}{5} = \frac{1}{10} > 0$), proving infinitely many $n(r, t)$ with $a(n(r,t)) = r$. **Airtight.**

---

## 3. Independent Computation & Deep Novelty Check

- **Independent verifier rerun (`notes/check-check-2.py`):** Exited `0` in `0.13s` (`real 0.13s`), confirming all 96 live OEIS `A400888` terms match both PARI `w(n)` and `A000361`, Lemmas 1–5, and $\ge 5$ explicit prime witnesses for every $r \equiv 27 \pmod{30}$ up to $147$ (plus $r = 3, 9, 15, 21$).
- **Additional concrete Step 4 Case 1 check (`notes/audit-helper-a400888.md` §3):** Verified $u_0$, $a_0$, $a_q$, $\gcd(a_q, M_q) = 1$, $2a_q+r+2 \equiv 0 \pmod{qd_q}$, and $t_{\mathrm{cand}}$ across 15 concrete $(r, Y, q)$ triples for $r \in \{3, 9, 27\}$.
- **Deep novelty check (`notes/audit-helper-a400888.md` §2):** Live OEIS `A400888` rev 16 unchanged; 0 hits across 470 local watch snapshots, arXiv, Zenodo, Crossref, OpenAlex, web search, all 45 `the-omega-institute/*` repos, `1337isnot1337/solved-conjectures`, `joaquimmj/oeis-conjectures`, and 14 other competing GitHub repos (`aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `openai/math`).

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (exact Charter label: `"written proof, internally audited"`).
- **Next step:** Requesting Gate 3 live pre-report novelty re-check before final report to `@coordinator`.
