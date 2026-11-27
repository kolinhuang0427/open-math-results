# Independent Check Report: `targets/fernando-2606.01037-quesQ3`

- **Verdict:** **PASS**
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/fernando-2606.01037-quesQ3/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, pure integer and $\mathbb{F}_2$-polynomial arithmetic)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2606.01037.src` (`draftMay31.tex`, Neranga Fernando and Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, `arXiv:2606.01037v1`).
- Confirmed `TARGET.md` reproduces **Question 6.3** (`\label{Q3}`, Section 6, `draftMay31.tex` lines 911–915) and notation $S_k$ (Section 2, line 119; identity Lemma 2.4 `\label{L310}`, lines 148–151; defining functional equation Eq. (1) `\label{AB1}` lines 74–76 and Waring's formula Eq. (2) `\label{AB2}` lines 78–80) verbatim.
- Verified every step of the proof classifying PP behavior of $g_{n,q}$ on $\mathbb{F}_{q^e}$ for even $q = 2^m > 2$ ($m \ge 2$) and even $e = 2k > 0$:
  - **Section 1:** Fiber bijection $x \mapsto S_k(x)^{q^k}$ with $\Phi_{\mathrm{Q3}}$ on $\mathrm{im}(S_k)$ (Lemma 1.1, Proposition 1.2) and involution on $\mathbb{F}_{q^k}$ when $k$ is even (Lemma 1.3).
  - **Section 2 ($k$ odd):** $g_{n,q}(1) = 0 = g_{n,q}(0)$.
  - **Section 3 ($q = 4$, $k$ even):** Separation $s(z) \in t\{\omega, \omega^2\}$, quartic invariant $\Phi_{\mathrm{Q3}}(z)^4 + \Phi_{\mathrm{Q3}}(z) = (z^2 + tz)^2$, and $Q(A)^2 + Q(A) + \omega^2 A = 0$ vs. $1$ contradiction.
  - **Section 4 ($q \ge 8$, $k \ge 4$ even):** Odd-degree $q - 3$ reduction $h_\lambda(u)$ and Carlitz–Uchiyama lower bound $N_0 \ge q(5q - 4) > 0$.
  - **Section 5 ($q \ge 8$, $e = 4$):** $s$-free moment reduction $\sum_{w \in H_1} N(w)^{3(q-1)} = 0$ if PP (Proposition 5.1) vs. four-piece binary-weight parity sum $\Sigma_{\mathrm{I}} + \Sigma_{\mathrm{II}} + \Sigma_{\mathrm{III}} + \Sigma_{\mathrm{IV}} \equiv (m-1) + (1 + \binom{m-2}{2}) + \binom{m-3}{2} + 0 \equiv 1 \pmod 2$ (Lemmas 5.2–5.4, Theorem 5.5).

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Primary $g_{n,q}$ & PP tests:** Verified Waring's formula (Eq. 2) matches Q6.3 pointwise for $(m, e) \in \{(2, 2), (2, 4), (3, 2)\}$, Eq. (1) $\sum_{a \in \mathbb{F}_q}(u+a)^n = g_{n,q}(u^q-u)$ matches Q6.3 for $(3, 4)$ and $(4, 4)$, and exhaustive PP checks match $(4 \mid e \text{ and } q=4)$ across all $(m, e) \in \{2,3,4\} \times \{2,4\}$ plus $(2, 6), (2, 8)$.
2. **Section 1 & Theorem 3.1:** Verified $|\mathrm{im}(S_k)| = q^{k+1}$, Lemma 1.3 involution, bijection on $\mathrm{im}(S_k)$, $s(z) \in t\{\omega, \omega^2\}$, quartic invariant, and $Q(A)^2 + Q(A) + \omega^2 A = 1$ for $(q, e) \in \{(4, 4), (4, 8)\}$.
3. **Section 4:** Verified Carlitz–Uchiyama count for $(q, e) = (8, 8)$ over $\mathbb{F}_{8^4}$: $N_0 = 576 \ge q(5q - 4) = 288$.
4. **Section 5:** Exhaustively verified Lemma 5.3 (6 bits), Lemma 5.4 (7 bits), direct finite-field moment $\sum_{w \in H_1} N(w)^{3(q-1)} = 0$ ($m=2$) and $= 1$ ($m=3,4,5$), Lemma 5.2 and $M_{1,\mathrm{rem}}$ identity in $\mathbb{F}_2[w]/(w^{q^2-1}-1)$, and exact four-piece $[w^0]_{\mathcal{R}}$ parities $(\Sigma_{\mathrm{I}}, \Sigma_{\mathrm{II}}, \Sigma_{\mathrm{III}}, \Sigma_{\mathrm{IV}})$ for $m \in \{3, 4, 5\}$.

## 3. Gate 2 Novelty Status
- Passed by `watch-5` (`#1794`), `watch-1` (`#1795`), and `watch-6` (`#1796`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).
