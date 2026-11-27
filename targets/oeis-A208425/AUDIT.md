# Adversarial Audit Report: `targets/oeis-A208425/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T02:58Z`
- **Target:** OEIS `A208425` (revision 60, `2025-11-05`) Zhi-Wei Sun (Nov 12, 2016) Conjecture (ii), Part 1 ($p \equiv 1 \pmod 3$) / `google-deepmind/formal-conjectures` `FormalConjectures/OEIS/208425.lean` (`OeisA208425.conjecture_2`)
- **Owner:** `attack-5`
- **Checker:** `check-2` (`notes/check-check-2.md`, `notes/check-check-2.py`)
- **Audit Helper:** `a208425-audit-hlp` (`notes/audit-helper-a208425.md`, killed)
- **Strict Isolation Observed:** Read ONLY `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and `notes/audit-helper-a208425.md` (plus live primary sources). Did NOT read author `verify.py` or any author scratch notes (`notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, etc.). Did NOT edit `TARGET.md` or `PROOF.md`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Statement Fidelity

Verified live (`notes/audit-helper-a208425.md` §1) against OEIS `A208425` (rev. 60, `2025-11-05T15:22:21-05:00`), OEIS `A066796` (rev. 73, `2026-08-30`), and `google-deepmind/formal-conjectures` `FormalConjectures/OEIS/208425.lean` (blob `6692a6604859e2615fd452aa1f41cade8b6f8dcc`):
- Sequence definition: $a(j) = [x^j]\sum_{k \ge 0}\frac{(3k)!}{k!^3}\frac{x^{2k}}{(1-x)^{3k+1}} = \sum_{k=0}^{j}\binom{j}{k}\binom{j-k}{k}\binom{j+k}{k}$ (both forms proved identical in Lemma 1 and checked against all 24 live OEIS `DATA` terms).
- Exact conjecture (`conjecture_2` / Sun Conjecture (ii), $p \equiv 1 \pmod 3$):
  $$\forall \text{ prime } p \equiv 1 \pmod 3, \qquad \sum_{k=0}^{p-1} a(k) \equiv \binom{\frac{2(p-1)}{3}}{\frac{p-1}{3}} \pmod{p^2}.$$
- Every prime $p \equiv 1 \pmod 3$ is odd and $\ge 7$, so writing $p = 6n + 1$ ($n \ge 1$) loses zero cases. Integer division `(2*(p-1)/3)` and `(p-1)/3` in Lean is exact.
- No `CONTESTED.md` exists in `targets/oeis-A208425/`.
- **Scope:** Part (i) (`conjecture_1`) was already proved by Pan–Sun (`arXiv:2012.05121v3`, *FCNT* **2** (2026), 55–62) and Part (ii) for $p \equiv 2 \pmod 3$ (`conjecture_3`) was already proved in `Varun-Dudipala/sun-conjectures-lean`; `PROOF.md` cleanly and accurately scopes to the remaining open case `conjecture_2` ($p \equiv 1 \pmod 3$).

---

## 2. Adversarial Line-by-Line Mathematical Audit

Every step of `PROOF.md` was checked independently from scratch for hidden hypotheses, division by $p$, edge cases ($p = 7$, i.e. $n = 1$), degree bounds, and localization issues:

1. **Step 1 (Lemma 1, lines 37–65):**
   - Equivalence of generating function and trinomial sum: valid for all $j \ge 0$, including $2k > j$ where $\binom{j-k}{k} = 0$ since $j - k < k$.
   - Hockey-stick summation $\sum_{j=2k}^{p-1}\binom{j+k}{3k} = \binom{p+k}{3k+1}$: valid for all $0 \le k \le 3n$ ($2k \le 6n = p-1$); exact upper bound $3n = (p-1)/2$.
   - Factorization $\binom{3k}{k}\binom{p+k}{3k+1} = \frac{p}{3k+1}\frac{\prod_{j=1}^k(p+j)}{k!}\frac{\prod_{j=1}^{2k}(p-j)}{(2k)!}$: checked carefully that $p - 2k - 1 \ge 0$ for $k \le 3n$, $k! \not\equiv 0$ and $(2k)! \not\equiv 0 \pmod p$ since $2k \le p-1$, and $1 \le 3k+1 \le 9n+1 < 12n+2 = 2p$, so $p \mid (3k+1) \iff k = 2n$.
   - At $k = 2n$: $2n$ is even, so $(-1)^{2n} = +1$ in $\binom{p-1}{2n} = \prod_{j=1}^{2n}(1 - p/j) \equiv 1 - p H_{2n} \pmod{p^2}$, and multiplying by $\binom{p+2n}{2n} \equiv 1 + p H_{2n} \pmod{p^2}$ cancels the $O(p)$ term cleanly, giving $t_{2n} \equiv \binom{4n}{2n} \pmod{p^2}$.
   - For $k \neq 2n$: $t_k / p \equiv \binom{2k}{k}/(3k+1) \pmod p$ holds in $\mathbb{Z}_{(p)}$. Reduction to $F(1) = 0$ in $\mathbb{F}_p$ is airtight.

2. **Step 2 (Lemma 2, lines 71–95):**
   - Part (a) ($H_n - H_{2n} \equiv H_{3n} \pmod p$): Checked index bijection $p - (2j-1) = 2(3n+1-j)$ for $1 \le j \le 2n \leftrightarrow n+1 \le 3n+1-j \le 3n$, and $H_{6n} = H_{p-1} \equiv 0 \pmod p$ (since $p \ge 7$ is odd, pairing $t \leftrightarrow p-t$ has no fixed points). Multiplying by $2$ (invertible mod $p$) is valid.
   - Part (b) ($\sum_{k=0}^{p-1}\binom{2k}{k} \equiv 1 \pmod{p^2}$): Checked Laurent extraction $[x^{p-1}]\frac{(1+x)^{2p} - x^p}{1+x+x^2}$ in $\mathbb{Z}[[x]]$. Note $[x^{p-1}](x^p/(1+x+x^2)) = 0$ strictly, and $[x^{6n}]((1+x)^{2p}(1-x)/(1-x^3)) = \sum_{j=0}^{2n}\binom{2p}{6n-3j} - \sum_{j=0}^{2n-1}\binom{2p}{6n-3j-1}$, where the $j=2n$ term is $\binom{2p}{0} = 1$. Sign tracking $(-1)^{s-1}$ for $s \equiv 0, 2 \pmod 3$, involution $t \mapsto p-t$ swapping $A_0 \equiv A_1 \pmod p$ (since $6n+1-t \equiv 1-t \pmod 3$), and $3A_0 = H_n - H_{2n}$, $A_0+A_1+A_2 = H_{3n} - H_{6n} \equiv H_{3n} \pmod p$ all check out with exact signs.

3. **Step 3 (Lemma 3, lines 101–139):**
   - Part (a): Beta integral $I_{i,i} = \frac{1}{(2i+1)\binom{2i}{i}}$ is exact; $P(t) = \sum_{i=0}^{2n-1}(t(1-t))^i \in \mathbb{Z}[t]$ has $\deg P = 4n - 2 < p - 1$, so every denominator $k + 1 \le 4n - 1 < p$ is invertible mod $p$, confirming $\int_0^1 P(t)\,dt \in \mathbb{Z}_{(p)}$.
   - $L_{\mathrm{poly}}(X) = (1 - X^p - (1-X)^p)/p \in \mathbb{Z}[X]$ reduces mod $p$ to $L(t) = \sum_{j=1}^{p-1} t^j / j \in \mathbb{F}_p[t]$ (constant term $0$, degree $p-1$).
   - Product $P(t)L(t)$ has zero constant term and degree $(4n-2)+(p-1) = 10n-2 < 12n = 2(p-1)$, so power-sum evaluation over $\mathbb{F}_p$ picks off *only* $-[t^{p-1}](P(t)L(t))$ (neither $d=0$ nor $d=2(p-1)$ occurs!). And $-(p-1-k)^{-1} \equiv (k+1)^{-1} \pmod p$ for $0 \le k \le 4n-2$ gives $\sum_{x \in \mathbb{F}_p} P(x)L(x) = \int_0^1 P(t)\,dt$ in $\mathbb{F}_p$.
   - Divisibility $\Phi(X) \mid L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$: checked modulo monic $\Phi(X) = X^2 - X + 1$: $X^3 \equiv -1$, $X^6 \equiv 1$, $1 - X \equiv -X^2 \equiv X^5$, $p = 6n+1 \implies X^p \equiv X$ and $(1-X)^p \equiv X^{5p} \equiv X^5 \equiv 1-X$, so $p L_{\mathrm{poly}}(X) \equiv 0 \pmod{\Phi(X)}$; since $\Phi$ is monic and $\mathbb{Z}[X]/(\Phi(X))$ is torsion-free, $\Phi(X) \mid L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$. Also $\Phi$ splits over $\mathbb{F}_p$ because $6 \mid (p-1)$, with distinct roots $\zeta, \zeta^{-1} \notin \{0, 1\}$.
   - $3$-orbit cancellation on $U = \mathbb{F}_p \setminus \{0, 1, \zeta, \zeta^{-1}\}$: verified $\sigma(x) = 1/(1-x)$ is well-defined and fixed-point-free on $U$ of order $3$, $|U| = p - 4 = 6n - 3$ divisible by $3$, $y(1-y) = -x/(1-x)^2$, $z(1-z) = -(1-x)/x^2$, raising to even power $2n$ uses $x^{6n} = (1-x)^{6n} = 1$, $P(y) = (1-x)^2 P(x)$, $P(z) = x^2 P(x)$, lift $\tilde{x} \in \{2,\dots,p-1\}$ guarantees $p \nmid \tilde{x}$ and $p \nmid (1-\tilde{x})$ so $\tilde{y}, \tilde{z} \in \mathbb{Z}_{(p)}$ and $(1-\tilde{x})^p \equiv 1-x$, $\tilde{x}^p \equiv x \pmod p$, giving $L(y) = -L(x)/(1-x)$ and $L(z) = -L(x)/x$. Sum on every orbit is $P(x)L(x)(1 - (1-x) - x) = 0$. Completely rigorous!
   - Part (b): Wilson's theorem step for $k = p - 1 - i \in [4n+1, p-1]$ ($0 \le i \le 2n-1$) has $2k = 2p - 2 - 2i \ge 2p - 4n = 8n + 2 > p$ and $2k \le 2p - 2 < 2p$, so $v_p(\binom{2k}{k}) = 1$ with exact quotient $\equiv -1/((2i+1)\binom{2i}{i}) \pmod p$. Combining with Lemma 2(b) and Lemma 3(a) yields Adamchuk's congruence $\sum_{k=0}^{4n}\binom{2k}{k} \equiv 1 \pmod{p^2}$.

4. **Step 4 (Lemma 4, lines 145–175):**
   - Checked $\tilde{Q}(X) \in \mathbb{Z}_{(p)}[X]$: exponents of $Q_{4n+1}(X)$ lie in $[4n+1, 8n+1]$; since $p = 6n+1$ and $2p = 12n+2 > 8n+1$, the *only* multiple of $p$ is $p$ itself, whose coefficient in $Q_{4n+1}$ is $\binom{4n}{2n}/p$, cancelled identically in $\tilde{Q}(X)$.
   - Part (a): $p Q_{4n+1}(1) = \frac{\binom{4n}{2n}}{\prod_{j=1}^{2n}(1 - p^2/j^2)} \equiv \binom{4n}{2n} \pmod{p^2}$ (valid since $2n$ is even, $p \nmid j$ for $1 \le j \le 2n$).
   - Part (b): Checked $H'(X)$, $\binom{3n}{k}(-4)^k \equiv \binom{2k}{k} \pmod p$ for $0 \le k \le 3n = (p-1)/2$, chain rule $(H(u))' = (1-2X^p)u^{4n} - \binom{4n}{2n}u^{p-1}(1-2X)$, and $A'(X)$: note carefully that $-(1-2X^p)\binom{4n}{2n}X^{p-1}$ cancels $-\binom{4n}{2n}(-X^{p-1} + 2X^{2p-1})$ identically!
   - Degree check: $\deg H(u) \le 2(7n+1) = 14n+2 = 2p+2n < 3p = 18n+3$ (holds for all $n \ge 1$), $\deg((1-2X^p)\tilde{Q}) = p+8n+1 = 2p+2n < 3p$, $\deg R = 2p-1 < 3p$. Thus $(H(u)-A)' = 0$ in $\mathbb{F}_p[X]$ implies $H(u)-A = c_0 + c_1 X^p + c_2 X^{2p}$.
   - Determination of $c_0 = c_2 = c_1 = 0$: verified every coefficient carefully, especially $[X^{2p}]H(u) = 0$: for $k = 2n+j$ ($1 \le j \le n$), $u^{p+j} \equiv (X^p - X^{2p}) X^j(1-X)^j \pmod p$ has exponents in $[p+j, p+2j] \cup [2p+j, 2p+2j]$; since $1 \le j \le n$, $p + 2j \le 8n + 1 < 12n + 2 = 2p$ and $2p + j \ge 2p + 1 > 2p$, so $X^{2p}$ never appears! Evaluating at $X=1$ gives $c_1 = -\tilde{Q}(1) = 0$ by Part (a).

5. **Step 5 (Lemma 5 & Completion, lines 181–204):**
   - Telescoping identity in $\mathbb{Q}[X]$: verified $\frac{d}{dt}((1-2t)u^k) = ku^{k-1} - (4k+2)u^k$, multiplication by $\binom{2k}{k}$ using $(4k+2)\binom{2k}{k} = (k+1)\binom{2k+2}{k+1}$, boundary $k=1$ term $2Q_1(X) = 2X$, adding $1-2X$ to match $k=0$, and final factor $(4n+1)\binom{8n+2}{4n+1} = \frac{2}{Q_{4n+1}(1)}$. Exact for all $n \ge 1$.
   - Reduction mod monic $\Phi(X) = X^2 - X + 1 \in \mathbb{Z}[X]$: Since $u(X) \equiv 1$ and $X^p \equiv X \pmod{\Phi(X)}$, the remainder of $2\tilde{Q}(X) \in \mathbb{Z}_{(p)}[X]$ modulo $\Phi(X)$ is linear in $X$ with both coefficients in $p\mathbb{Z}_{(p)}$ (from Lemma 4(a) and Lemma 3(b)). Because $\Phi(X)$ is monic, division in $\mathbb{Z}_{(p)}[X]$ agrees with division in $\mathbb{Q}[X]$, so reducing mod $p$ and evaluating at $\zeta$ gives $2\tilde{Q}(\zeta) = 0 \implies \tilde{Q}(\zeta) = 0$ in $\mathbb{F}_p$. Combined with $R(\zeta) = -\zeta^p L(\zeta) = 0$ and $3 \not\equiv 0 \pmod p$ ($p \ge 7$), Lemma 4(b) at $X = \zeta$ gives $F(1) = 0$ in $\mathbb{F}_p$. Q.E.D.

**Minor non-blocking bibliographic nit:** `PROOF.md` line 18 cites Guo-Shuai Mao (2021) as *J. Combin. Theory Ser. A* **181** (2021), 105478; the actual published volume is **182** (2021), Art. 105478 (DOI `10.1016/j.jcta.2021.105478`). Since `PROOF.md` is completely self-contained and does not rely on Mao (2021), this typo has zero mathematical impact.

---

## 3. Independent Mechanical Verification

Reran `check-2`'s independent exact-arithmetic verifier (`targets/oeis-A208425/notes/check-check-2.py`):
```sh
time .venv/bin/python -u targets/oeis-A208425/notes/check-check-2.py 2>&1
```
Raw output (`notes/audit-helper-a208425.md` §3):
```text
OEIS A208425 rev 60 definitions (GF == trinomial sum, all 24 live OEIS DATA terms): PASS
Lemmas 1, 2, 3 (incl. full 3-orbit F_p check for p<=200, direct sum p<=250) on 45 primes p<500: PASS
Lemmas 4 & 5 (exact Q[X] telescoping, F_p[X] ODE match, mod Phi(X) reduction) on [7, 13, 19, 31, 37, 43]: PASS
Target conjecture_2 verified across all 80 primes p == 1 (mod 3), p < 1000: PASS
PASS (all checks passed in 2.309s)
```
Exit code `0`, `2.383s` wall-clock.

---

## 4. Deep Novelty & Prior-Art Check

Verified independently in `notes/audit-helper-a208425.md` §2:
- **Guo-Shuai Mao (`arXiv:2003.09810v4`, *JCTA* 182 (2021), Art. 105478):** Inspected full 584-line `main.tex`. Proves Theorem 1.1 (Adamchuk's congruence on `A066796`) via Theorem 1.2 ($\sum_{k=0, k\neq(p-1)/3}^{(p-1)/2} \binom{2k}{k}/(3k+1) \equiv 0 \pmod p$), but **never mentions OEIS `A208425`, $\sum_{k=0}^{p-1} a(k)$, or Zhi-Wei Sun's Conjecture (ii)**.
- **Hao Pan & Zhi-Wei Sun (`arXiv:2012.05121v3`, *FCNT* 2 (2026), 55–62):** Inspected full 429-line `261p.tex`. Proves only `conjecture_1`; does not mention or prove `conjecture_2` or `conjecture_3`.
- **Zhi-Wei Sun conjecture papers (`0911.5665`, `1610.03384v8`, `2006.02918v3`):** No proof of `A208425` `conjecture_2` (Conjecture A46(i) of `0911.5665`, proved in `2006.02918v3`, has a different LHS $\sum \binom{3k}{k,k,k}/24^k$).
- **All 6 OpenAlex works citing Mao `2003.09810` and all 3 OpenAlex works citing Pan–Sun `2012.05121`**, plus additional 2020–2026 supercongruence preprints on arXiv, Crossref, Zenodo, and web search: 0 proofs of `A208425` `conjecture_2`.
- **`Varun-Dudipala/sun-conjectures-lean`:** Inspected directly; proves ONLY `conjecture_3` ($p \equiv 2 \pmod 3$) and explicitly states in `SunConjectures/A208425/README.md` that part (i) and the case $p \equiv 1 \pmod 3$ are not proved there.
- **All checked competing GitHub repos & 413 local snapshots** (`1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `openai/math`, `epoch-research/LeanOpenProblems*`, `BoltonBailey/formal-conjectures-ai-review`, `google-deepmind/formal-conjectures`): 0 proofs of `conjecture_2`.

### What Is Not Established / Caveats
- Solves only `OeisA208425.conjecture_2` ($p \equiv 1 \pmod 3$); `conjecture_1` and `conjecture_3` were already settled elsewhere (as accurately scoped in `PROOF.md`).
- Paywalled journal / ResearchGate full texts without arXiv preprints (such as Mao's 2023–2025 journal articles / ResearchGate preprints linked on `A066796`) could not be read in full, though none are linked on `A208425` or surfaced by OpenAlex/Crossref/arXiv/web queries.
- Internal audit and finite exact checks are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`.

- **Gate 3 Novelty Clearance (`2026-11-27T03:34Z`–`04:10Z`):** **PASS** across `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-3.md`, and `notes/novelty-gate3-watch-5.md` (`watch-3` co-covering `watch-6`), covering live OEIS `A208425` rev. 60, arXiv (`2003.09810v4`, `2012.05121v3`), OpenAlex citing cache, Zenodo, `470` snapshots, and all 15+ competing GitHub repos (`Varun-Dudipala/sun-conjectures-lean` re-verified as `conjecture_3` only). Cleared for coordinator verification.
