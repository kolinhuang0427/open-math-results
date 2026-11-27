# Check Report: `targets/ulfarsson-2603.16004-conj1/` (`@check-2`)

- **Primary Source Fidelity:** Verified against `arXiv:2603.16004v1` (`ItsAllFunAndGamesUntilMonotonicity.tex`, Definition 1.1 L59–64, Definition 2.1 L120–135, Conjecture 2.9 L371–375, Definition 2.10 L380–385, Lemma 2.11, Proposition 2.12, Corollary 2.13 L387–438). `TARGET.md` and `PROOF.md` match Conjecture 2.9 (`conj:general-reverse`) and all game definitions verbatim.
- **Proof & Computation Verification (`check-check-2.py` -> `PASS`):**
  - **Threshold & Reduction (Proposition 1, Lemma 1):** Checked $n_0(k) = k + ((2k+1)(k-1))^2 + 1 = 4k^4 - 4k^3 - 3k^2 + 3k + 2$, $n_0(k) > (k-1)^2 + 1$, and $n_0(k) - k > 2k - 2 > k$ for all $3 \le k \le 500$. Verified Erdős–Szekeres + pigeonhole grid-cell extraction ($2k+1$ monotone diagonals).
  - **Lemma 0(1)–(3):** Exhaustively checked reversal identity, shadow stabilization ($t \ge k$), and contiguous monotone-block inflation on $m = 3, 4$, $1 \le t \le 5$, $\varepsilon \in \{+, -\}$.
  - **Lemma 2:** Exhaustively verified Case 1, Subcase 2a, and Subcase 2b witness constructions ($\omega_1, \omega_2 \in \mathrm{Av}_n(F \cup \{p\})$ containing $p^r$) over all non-monotone $p \in S_k$, 1-point extensions $\beta \in S_{k+1}$, and signs $\varepsilon \in \{+, -\}$ for $k = 3, 4$.
  - **Theorem 3 / Claims 3A–3B:** Exhaustively verified Claims 3A/3B and Theorem 3 (no non-monotone $p \in S_k$ appears in both $\mathrm{Sh}_k(I_k(p^r, j_1, +))$ and $\mathrm{Sh}_k(I_k(p^r, j_2, -))$) over all non-monotone $p \in S_k$ for $k = 3, 4, 5, 6$.
  - **Exact PAP Game Tree:** Verified $\mathrm{sg}(S_n, 3) = 0$ and move-by-move reverse-strategy win across every play for $k = 3, n \in \{3, 4, 5, 6\}$.
- **Script & Result:** `.venv/bin/python -u targets/ulfarsson-2603.16004-conj1/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, plus `notes/novelty-attack.md`).
