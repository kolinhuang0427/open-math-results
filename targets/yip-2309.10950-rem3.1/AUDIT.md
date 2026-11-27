# Adversarial Audit Report (`audit-3`) — `targets/yip-2309.10950-rem3.1/`

- **Verdict:** **PASS**
- **Charter label:** `"written proof, internally audited"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py`, `notes/screen-*`, `notes/attack-*`, or `notes/triage-brief.md`)
- **Audited at (UTC):** 2026-11-26 23:22 UTC
- **Files inspected:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, `notes/audit-helper-yip.md`, and primary source `tools/.arxiv_cache/eprint/2309.10950/main.tex` (`arXiv:2309.10950v2`, published *Canad. J. Math.* **78**(2) (2026), 594–618, DOI `10.4153/S0008414X24000920`).

---

## 1. Primary-Source Fidelity & Published-Version Verification

- Directly verified `arXiv:2309.10950v2` (`main.tex` lines 57, 61, 105–107, 381–420; confirmed sole/latest arXiv version corresponding to the accepted *Canad. J. Math.* **78**(2) (2026), 594–618 publication, Crossref `update-to: None`):
  - $S_d = \{x^d : x \in \mathbb{F}_q^*\}$ ($0 \notin S_d$) and $A \hat{+} A = \{a + b : a, b \in A,\, a \ne b\}$.
  - `\label{thm:VLM}` is **Theorem 1.7** and the Section 3.2 Remark (`lines 405–407`) is **Remark 3.3** in the compiled PDF and published paper, matching `PROOF.md` verbatim. (Minor non-blocking typo in `TARGET.md` line 12: labels the blockquote `Theorem 1.5`, whereas `TARGET.md` line 1 and `PROOF.md` line 7 correctly state Theorem 1.7; folder slug `rem3.1` reflects Subsection 3.2's first remark while the paper shares a single section counter giving Remark 3.3.)
  - For any odd square $q = r^2 \ge 49$, $r$ is an odd prime power $\ge 7$, so $q \equiv 1 \pmod 2$ and $2 \mid (r+1)$ hold automatically.
- Verified that **Blokhuis (1984)** (*Indag. Math.* **46**, 369–372) holds for **all odd prime powers** $r$ (not only primes), matching its invocation in Case 1.

---

## 2. Adversarial Line-by-Line Audit of `PROOF.md`

Every lemma, case split, algebraic step, characteristic-$3$ edge case, and boundary calculation in `PROOF.md` was independently checked and holds without gap:

1. **Preliminaries (Facts 1–3, lines 31–38):** $\mathbb{F}_r^* \subset S_2$ (hence $-1, 2 \in S_2$), $\chi(x) = \chi_{\mathbb{F}_r}(N(x))$ for all $x \in \mathbb{F}_{r^2}$, and sufficiency of $\alpha \mathbb{F}_r$ ($\alpha \in S_2$) are exact.
2. **Case 1 ($A + A \subset S_2 \cup \{0\}$, lines 44–56):** Checked $M\mathbf{1} = 0$, $M^2 = qI - J$ (diagonal $q-1$, off-diagonal $-1$), Rayleigh bound $|\langle v, Mv\rangle| \le r|A|(1 - |A|/r^2)$, and $|A|^2 - |A| \le |A|^2 - |A \cap (-A)| = \sum_{a,b \in A} \chi(a+b)$, giving $|A|(r+1)(|A|-r) \le 0 \implies |A| \le r$. At equality $|A| = r$, $A = -A$ forces $0 \in A$ ($r$ odd, odd char), $A - A = A + A \subset S_2 \cup \{0\}$, picking $\alpha \in A \setminus \{0\} \subset S_2$ gives $0, 1 \in \alpha^{-1}A$, and Blokhuis (1984) yields $A = \alpha \mathbb{F}_r$. Airtight.
3. **Case 2 — Step 1 (Lemma 2.2, lines 60–98):** Reduction to $|A| = r$ with $b_0 \in B = A \cap N_2 \ne \emptyset$ and Observation 2.1 ($0 \notin A$) are exact. Lagrange identity (1), $\deg H_k \le (r-1)/2$ (for $0 \le k \le K = (r-3)/2 < r-1$), Frobenius $(b^r + a^r)^{(r+1)/2} = (b+a)^{(r^2-1)/2}(b+a)^{(r+1)/2}$, all three cases ($a \ne \pm b$, $a = -b$, $a = b$), and exact cancellation of $\delta_{k,K}$ yield $H_k(b^r) = 0$ on $A_S$ and $-2c_b(2b)^{(r+1)/2}b^k \ne 0$ on $B$. Airtight.
4. **Case 2 — Step 2 (Lemma 2.3, lines 101–125):** $K = (r-3)/2 \ge 2$ for $r \ge 7$. $Q_k = H_0 H_k - H_1 H_{k-1}$ has degree $\le r-1$ and $r$ distinct roots $\{b^r : b \in A\}$, so $Q_k \equiv 0$. Induction gives $U^k H_k = V^k H_0$ in lowest terms, UFD yields $H_k = W U^{K-k} V^k$, $|A_S| \le \deg W$, and (2) gives $\deg W + K \max(\deg U, \deg V) \le (r-1)/2$. For $r \ge 7$, $2K = r-3 > (r-1)/2$ forces $\max(\deg U, \deg V) \le 1$; degree $0$ forces $|B| \le 1$ and $|A| \le (r+1)/2 < r$. Thus $\max(\deg U, \deg V) = 1$, $|A_S| \le 1$, $|B| \ge r-1 \ge 6$, and $b U(b^r) - V(b^r) = 0$ on $B$. Airtight.
5. **Case 2 — Step 3A ($u_1 = 0$, lines 135–142):** $\varphi(z) = z - \alpha z^r$ is nonzero $\mathbb{F}_r$-linear on $\mathbb{F}_{r^2}$, so fibers have size $0, 1,$ or $r$; $|B| \ge 6$ forces an affine $\mathbb{F}_r$-line $L$. $0 \in L \implies L \cap S_2 = \emptyset \implies |B| \le 2$; $0 \notin L \implies |B| \le |L \cap N_2| \le (r+1)/2 < r-1$ (for $r \ge 7$). Airtight.
6. **Case 2 — Step 3B ($u_1 = 1$, lines 144–210):** Frobenius-subtraction either reduces to 3A or yields $u_0 = -v_1^r, v_0 \in \mathbb{F}_r$ and norm circle $N(b - c) = \lambda \in \mathbb{F}_r^*$ ($\lambda = u_1 v_0 - u_0 v_1 \ne 0$).
   - **3B(i) ($c = 0$):** Parity classes of $k \bmod 2$ in $\mu_{r+1}$ satisfy $b_1 + b_2 \in N_2$ whenever $b_1 + b_2 \ne 0$, forcing $|B| \le 4 < 6 \le r-1$. Airtight.
   - **3B(ii) ($c \ne 0$):** Claim 2.4 (`1 - chi(t^2 - 4 mu)`), identity (4), and both subcases $\lambda = N(c)$ ($|C \cap N_2| \le (r+1)/2 < r-1$) and $\lambda \ne N(c)$ (equation (5)) were verified term-by-term. For $\lambda \ne N(c)$, $f(t) = (s+t)(t^2 - 4\mu)$ has 3 distinct roots in $\overline{\mathbb{F}}_r$ in **every odd characteristic including $p = 3$** ($4\mu \ne 0$ and $(-s)^2 - 4\mu = (N(c)-\lambda)^2 \ne 0$), so $E: Y^2 Z = (X+sZ)(X^2 - 4\mu Z^2)$ is a smooth projective plane cubic (genus $1$, elliptic curve) over $\mathbb{F}_r$. Hasse's theorem (1933) gives $r - 1 \le (r+1)/2 + \sqrt{r} \implies (\sqrt{r}-3)(\sqrt{r}+1) \le 0 \implies r \le 9$, closing all odd prime powers $r \ge 11$ ($q \ge 121$). Airtight.
7. **Case 2 — Step 3B(iii) ($r = 7$ and $r = 9$, lines 213–262):** Every value of $S(\theta)$, every orbit symmetry, both $r=7$ circles with shared witness pair $(4+u, 2+3u)$, and the unique $r=9$ circle ($z^{10} = -1$) with characteristic-3 identities $\beta^4 = -1$, $N(b_1+b_2) = -\beta(\beta^2+\beta+1)$, and $N(b_1+b_2)^4 = -1$ were verified both by hand and by exact computation. Airtight.

---

## 3. Independent Exact Computation & Prior-Art Novelty

- **Independent verifier (`notes/check-check-2.py`):** Re-executed via `.venv/bin/python targets/yip-2309.10950-rem3.1/notes/check-check-2.py` — exit code `0` (`PASS (all checks passed in 0.387s)`).
- **Additional adversarial exact checks (`notes/audit-helper-yip.md` §3.2):**
  - Confirmed Yip's small exceptions ($\mathbb{F}_9$: unique size-4 clique $N_2(\mathbb{F}_9)$; $\mathbb{F}_{25}$: 15 size-5 cliques = 3 canonical cosets + 12 non-coset cliques) and verified why Case 2 breaks precisely at $r = 3, 5$.
  - Exhaustive exact clique search over all 49 vertices of $GPS(49, 2)$ ($\mathbb{F}_{49}$) confirmed maximum clique size $7$ with **precisely the 4 canonical cosets** $\alpha \mathbb{F}_7$ ($\alpha \in S_2$) and zero non-coset cliques of size $\ge 7$.
  - Verified all $S(\theta)$ values in `PROOF.md` lines 241–243 and the $\beta = z - z^{-1}$ norm identity across all 8 roots $z \in \mathbb{F}_{81} \setminus \mathbb{F}_9$ of $z^{10} = -1$.
- **Deep novelty check (`notes/audit-helper-yip.md` §2):** Clear across all 333 watch snapshots, `aliromman/math`, `the-omega-institute/trureturing*`, `1337isnot1337/solved-conjectures`, `openai/math`, global GitHub, arXiv (all 77 papers of Chi Hoi Yip through Nov 2026 + topic queries), Crossref & Semantic Scholar (all 12 citations of `10.4153/S0008414X24000920`), Zenodo, and web search. No `CONTESTED.md`.
- **Gate 3:** Requested from `@watch-1 @watch-5 @watch-6` prior to final report to `@coordinator`.
- **What is not established:** This is an internal adversarial audit plus exact finite-field testing of key lemmas and boundary cases, not peer review or a Lean formalization (note Blokhuis 1984 and Hasse 1933 are cited as external classical theorems).
