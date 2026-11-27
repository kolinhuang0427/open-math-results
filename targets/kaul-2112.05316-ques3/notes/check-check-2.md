# Check Report: `targets/kaul-2112.05316-ques3/` (`@check-2`)

- **Primary Source Fidelity:** Verified against `arXiv:2112.05316v2` (`Gluings_Paper.tex`, Section 1.1–1.4, L52–60, L126–205). `TARGET.md` and `COUNTEREXAMPLE.md` match Question 2 (`ques: classify`, §1.3) and Question 3 (`ques: easier`, §1.3; L199 remark §1.4) verbatim (`\newtheorem{ques}[thm]{Question}` shares the `[thm]` counter: Theorem 1, Question 2, Question 3), and Lemma 2 Case 3 covers all 9 pairs.
- **Refutation Proof Verification (`check-check-2.py` -> `PASS`):**
  - **Lemma 1:** Verified $P_{DP}(K_{p+1}, p+1) = (p+1)!$ and exact count of $2p$ $p$-cliques $K^{(i,j)} = W \cup \{v_i, u_j\}$ in $G_0^{(p)} = K_{p-2} \vee K_{2,p}$.
  - **Lemma 2:** Directly enumerated all 3-subset extensions and full vertex colorings for $p \in \{3, 4, 5, 6, 7\}$ (plus exact closed-form check for $3 \le p \le 25$) under the $(1\,2)$-twisted cover $\mathcal{H}$ on edge $v_1 u_p$, confirming $P_{DP}(G_0^{(p)}, p+1) \le P(G_0^{(p)}, p+1) - (p-1)!(2^p - 2p + 2) < P(G_0^{(p)}, p+1)$.
  - **Lemma 3 & Main Contradiction ($G^* = G_{2p}$):** Exhaustively tested precoloring extension on twisted covers for $p = 3, 4$ and verified the Case 1 / Case 2 counting argument showing at least one gluing step $k \in \{1,\dots,2p\}$ satisfies $P_{DP}(G_k, p+1) > P_{DP}(G_{k-1}, p+1)$, simultaneously refuting Question 3 for $d_G(v) = p \ge 4$ and Question 2 for $p \ge 4$ at $m = p+1$.
- **Script & Result:** `.venv/bin/python -u targets/kaul-2112.05316-ques3/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-6.md`).
