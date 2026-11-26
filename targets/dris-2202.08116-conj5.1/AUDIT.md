# Adversarial Audit Report: `dris-2202.08116-conj5.1`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T21:22Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Independent Verifier:** `targets/dris-2202.08116-conj5.1/notes/check-check-2.py` (report: `targets/dris-2202.08116-conj5.1/notes/check-check-2.md`)

---

## 1. Isolation & Materials Inspected

In accordance with `CHARTER.md`, this audit was conducted without reading `verify.py`, `notes/screen-*`, `notes/attack-*`, or author scratch commentary. Inspected materials:
1. Primary source: `tools/.arxiv_cache/eprint/2202.08116/main.tex` (`arXiv:2202.08116v1`, sole version on arXiv; published in *Octogon Mathematical Magazine* 30(2), Oct 2022, pp. 883–895).
2. `targets/dris-2202.08116-conj5.1/TARGET.md`.
3. `targets/dris-2202.08116-conj5.1/PROOF.md`.
4. `targets/dris-2202.08116-conj5.1/notes/check-check-2.md` and `targets/dris-2202.08116-conj5.1/notes/check-check-2.py`.
5. Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and independent adversarial literature/Stack Exchange/verification notes (`notes/audit-helper-dris.md`, produced by Flash helper `dris-audit-hlp`).

---

## 2. Primary-Source Fidelity Audit

Verified directly against `main.tex` (Jose Arnaldo Bebita Dris, *"A new approach to odd perfect numbers via GCDs"*, `arXiv:2202.08116v1`):
- **Definitions (Section 1, line 63; Abstract, lines 57–59):** $\sigma(x) = \sum_{d \mid x} d$ is the sum of divisors of a positive integer $x$.
- **Exact Verbatim Conjecture (Section 5, Conjecture 5.1, `\label{AsymptoticDensity2}`, lines 386–391; also Abstract lines 57–59):**
  > The asymptotic density $\mathscr{A}$ of positive integers $m$ with $\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))$ satisfies $\mathscr{A} = 0$.
- **Fidelity Verdict:** Exact match across `TARGET.md`, `PROOF.md`, and `notes/check-check-2.py`. (Dris overloads $\mathscr{A}$ for the set in the abstract and its density in Conjecture 5.1; `PROOF.md` uses $A$ for the set and proves $\lim_{X \to \infty} |A \cap \{1,\dots,X\}|/X = 0$, matching unambiguously.) Zero quantifier, hypothesis, or definition drift.

---

## 3. Adversarial Line-by-Line Proof Audit

Checked every step, quantifier, edge case, and inequality of `PROOF.md`:

1. **Lemma 1 (Prime-power divisibility criterion):**
   - For any prime $p \equiv 1 \pmod 6$, $p \ge 7$ and $3 \mid (p-1)$, so the cyclic group $(\mathbb{Z}/p\mathbb{Z})^\times$ contains exactly two elements $r_p, s_p$ of order $3$, which are the distinct roots of $u^2 + u + 1 = (u^3-1)/(u-1) \equiv 0 \pmod p$. (Minor non-fatal expository note: line 21 explicitly rules out $u \equiv 0, 1$ without writing $(-1)^2+(-1)+1 = 1 \not\equiv 0$ for $u \equiv p-1$; however, elements of order $3$ in $(\mathbb{Z}/p\mathbb{Z})^\times$ automatically exclude $-1 \equiv p-1$ of order $2$, and the subsequent proof uses only $r_p, s_p \not\equiv 0 \pmod p$.)
   - Hence $p \notin \mathcal{Q}_p = \{q \text{ prime} : q \equiv r_p \text{ or } s_p \pmod p\}$.
   - If $p \parallel m$ and distinct primes $q_1, q_2 \in \mathcal{Q}_p$ satisfy $q_1 \parallel m$ and $q_2 \parallel m$, then $q_1^2 \parallel m^2$, $q_2^2 \parallel m^2$, and $\gcd(q_1^2, q_2^2) = 1$, so by multiplicativity of $\sigma$, $\sigma(q_1^2)\sigma(q_2^2) \mid \sigma(m^2)$. Since $\sigma(q_j^2) = q_j^2 + q_j + 1 \equiv 0 \pmod p$, we obtain $p^2 \mid \sigma(m^2)$, hence $v_p(\sigma(m^2)) \ge 2$. Together with $v_p(m) = 1$ and $v_p(m^2) = 2$, this forces $v_p(\gcd(m, \sigma(m^2))) = 1 < 2 = v_p(\gcd(m^2, \sigma(m^2)))$, so $m \notin A$. **Airtight.**

2. **Lemma 2 (Finite-truncation covering & CRT density of $E_k$):**
   - Contrapositive of $A \subseteq E_k \cup \bigcup_{i=1}^k B_i$: if $m \notin E_k$ and $m \notin \bigcup_{j=1}^k B_j$, then some $i \in \{1,\dots,k\}$ satisfies $p_i \parallel m$, and $m \notin B_i$ provides at least two distinct primes $q_1, q_2 \in \mathcal{Q}_{p_i}$ with $q_1 \parallel m, q_2 \parallel m$; Lemma 1 yields $m \notin A$. Placing the finite union $\bigcup_{i=1}^k B_i$ outside $E_k$ rigorously avoids any correlation between $p_i$ and $\mathcal{Q}_{p_i}$.
   - For each $i$, $p_i \nparallel m$ excludes exactly the $p_i - 1$ residue classes $\{p_i, 2p_i, \dots, (p_i-1)p_i\} \bmod p_i^2$. Since $p_1^2, \dots, p_k^2$ are pairwise coprime, CRT gives $R_k = \prod_{i=1}^k (p_i^2 - p_i + 1)$ admissible residue classes mod $M_k = \prod_{i=1}^k p_i^2$, with $| |E_k \cap [1, X]| - X R_k/M_k | \le M_k$, whence $d(E_k) = \prod_{i=1}^k (1 - \frac{p_i - 1}{p_i^2})$. **Airtight.**

3. **Lemma 3 (Each bad set $B_i$ has density $0$):**
   - Since $\gcd(r_p, p) = 1$, Dirichlet's theorem on primes in arithmetic progressions gives $\sum_{q \equiv r_p \pmod p} 1/q = \infty$. With $1 - 1/q \ge 1/2$ for all primes $q \ge 2$, $S(P) = \sum_{q \in \mathcal{Q}(P)} \frac{1}{q}(1 - \frac{1}{q}) \to \infty$ as $P \to \infty$.
   - For any finite cutoff $P$ with $S(P) \ge 2$, $B_i \subseteq \tilde{B}_{i,P} = \{m \ge 1 : f_P(m) \le 1\}$, and $\tilde{B}_{i,P}$ is periodic with exact period $N_P = \prod_{q \in \mathcal{Q}(P)} q^2$.
   - By CRT, $\{1, \dots, N_P\} \cong \prod_{q \in \mathcal{Q}(P)} \mathbb{Z}/q^2\mathbb{Z}$, making $X_q(m) = \mathbf{1}_{q \parallel m}$ ($q \in \mathcal{Q}(P)$) exact mutually independent $\mathrm{Bernoulli}(\alpha_q)$ variables with $\alpha_q = \frac{q-1}{q^2} = \frac{1}{q}(1 - \frac{1}{q})$.
   - Thus $\mathbb{E}[f_P] = S(P)$ and $\mathrm{Var}(f_P) = \sum \alpha_q(1-\alpha_q) \le S(P)$. Since $S(P) \ge 2$, $f_P(m) \le 1 \implies |f_P(m) - S(P)| \ge S(P) - 1 > 0$, so Chebyshev's inequality gives $\overline{d}(B_i) \le d(\tilde{B}_{i,P}) \le \frac{\mathrm{Var}(f_P)}{(S(P)-1)^2} \le \frac{S(P)}{(S(P)-1)^2} \to 0$ as $P \to \infty$. Hence $d(B_i) = 0$. **Airtight.**

4. **Conclusion:**
   - By finite subadditivity of upper asymptotic density, for every fixed $k \ge 1$,
     $$0 \le \overline{d}(A) \le d(E_k) + \sum_{i=1}^k \overline{d}(B_i) = \prod_{i=1}^k \left(1 - \frac{p_i - 1}{p_i^2}\right).$$
   - Because $0 < 1 - \frac{p_i - 1}{p_i^2} \le \exp(-\frac{p_i - 1}{p_i^2})$ and $\frac{p_i - 1}{p_i^2} \ge \frac{1}{2 p_i}$ ($p_i \ge 7$), taking products gives $\overline{d}(A) \le \exp(-\frac{1}{2}\sum_{i=1}^k \frac{1}{p_i})$.
   - By Dirichlet's theorem ($\gcd(1,6)=1$), $\sum_{i=1}^\infty \frac{1}{p_i} = \infty$; letting $k \to \infty$ gives $\overline{d}(A) = 0$, hence $d(A) = 0$. **Airtight.**

5. **Mechanical Check Verification:**
   - Audited `targets/dris-2202.08116-conj5.1/notes/check-check-2.py` (exact integer and `Fraction` arithmetic, zero floats) and confirmed re-run (`notes/audit-helper-dris.md` §3): exit code `0`, `PASS` in `0.914s`, verifying Dris's table counts through $10^4$, Lemma 1 on $m \le 10^4$, Lemma 2 exact period densities ($M_1 = 49, M_2 = 8281$), and Lemma 3 exact CRT moments on $N_P = 256036$ plus exact `Fraction` DP for the Chebyshev inequality.

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-dris.md`, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) confirmed:
- **MathOverflow & Math Stack Exchange (live Stack Exchange API):** Inspected full thread MO `Q369441` (including Aaron Meyerowitz's Answer `369521` and all comments — explicitly conditional heuristic *"If we can argue..."*, inactive since `2020-08-19`), all 59 MO questions and 515 MSE questions by Dris (including MSE `Q3629818`, `Q3628078`, MO `Q460092`), and broad SE searches. Zero prior proofs found.
- **Analytic/Elementary NT Literature & OEIS:** Inspected arXiv, OpenAlex (`W4226357996`, `cited_by_count: 0`), Crossref, OEIS, and full PDFs/texts of Pollack (2011, 2023), Erdős–Luca–Pomerance (2008), Kátai–Subbarao (2006), Dressler (1974), Luca (2007), Bordellès (2026), and OPN literature. None prove Conjecture 5.1.
- **What Is Not Established:**
  - This proof establishes $d(A) = 0$ (qualitative asymptotic density zero), not an explicit quantitative decay rate for $|A \cap [1, X]|/X$ (which decays very slowly, $\approx 92.35\%$ at $X = 10^6$).
  - It does not settle Dris's Section 7 conjecture that $\gcd(\sigma(q^k), \sigma(n^2)) \neq \gcd(n^2, \sigma(n^2))$ for odd perfect numbers $N = q^k n^2$.
  - Internal audit and small-case exact checks are not formal peer review or a formal Lean proof.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`. Gate 3 novelty cleared (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`, checked `2026-11-26T21:27–21:29Z`).
