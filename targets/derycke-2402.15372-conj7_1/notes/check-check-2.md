# Check Report: `targets/derycke-2402.15372-conj7_1/` (`@check-2`)

- **Primary Source Fidelity:** Verified against `arXiv:2402.15372v3` (`qtss1.tex`, Section 2 L866–1165, Section 3, and Section 6 L2659–2669). `TARGET.md` matches Section 6 **Conjecture 6.1** (`conj:ITCCTIsymmetry`) verbatim, and every cross-reference in `PROOF.md` (`Proposition 2.1`, `Theorem 2.7`, `Corollary 3.6`, `Proposition 3.9`, `Conjecture 6.2`, `Conjecture 6.3`) matches the exact compiled `[theorem]` numbering of `qtss1.tex`.
- **Proof & Computation Verification (`check-check-2.py` -> `PASS`):**
  - **Direct Abelian Sandpile ($n+d \le 6$, 2314 sorted recurrent configs via Dhar's burning test + `S_{2,2}` Example 2.3):** Exact agreement of CTI and ITC parallel topplings with Propositions 1.1 and 2.1, confirming the refined equality $\mathfrak{F}_{n,d,r}^{\mathrm{CTI}}(q,t) = \mathfrak{F}_{n,d,r}^{\mathrm{ITC}}(q,t)$ for every $1 \le r \le n+d$.
  - **Cell formulas (Propositions 1.1 & 2.1):** Exact equality in $\mathbb{Z}[q,t]$ verified across all $n \ge 1, d \ge 0$ with $n+d \le 9$ and all $1 \le r \le n+d$.
  - **Generating functions (Section 3 & Theorem 4.4):** Verified $P_r^{(N)}(X,Y) = \widetilde{P}_r^{(N)}(X,Y)$ and agreement of $t^{-r}P_r(tx,ty)$ with Proposition 2.1 (plus the $y^r$ degree-$r$ term) up to total degree $N \le 7$.
  - **Core $q$-hypergeometric identities (Lemmas 4.2, 4.3, Theorem 4.4):** Verified Lemma 4.2 in $\mathbb{Q}(q)[a,b]$ for $0 \le N \le 5$, Lemma 4.3 in $\mathbb{Z}[q,u]$ for all $1 \le r, r' \le 7$, and the Theorem 4.4 telescoping $q$-binomial identity for $1 \le a, m \le r' \le 7$.
- **Script & Result:** `.venv/bin/python -u targets/derycke-2402.15372-conj7_1/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
