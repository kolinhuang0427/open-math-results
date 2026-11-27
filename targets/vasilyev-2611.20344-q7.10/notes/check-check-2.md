# Check Report: `targets/vasilyev-2611.20344-q7.10/` (`@check-2`)

**Verdict:** `PASS` (exact verification against `arXiv:2611.20344v2` `updown.tex`, including post-`#1730` `Subsection 5.4` / `Table 5.3` / §7 updates; zero floats).

## 1. Primary-Source Alignment (`arXiv:2611.20344v2`)
- Verified verbatim against `tools/.arxiv_cache/eprint/2611.20344/updown.tex`:
  - Section 5 (`Subsection 5.4` `sec:uniform` L1486–1622, `Definition 5.3` `def:residue`, `Definition 5.8` `def:pi`, `Definition 5.10` `def:uniform`, `Theorem 5.11` `thm:uniform`, `Table 5.3` `tab:uniformcount`) and Section 7 (`Question 7.10` `q:supremum`, lines 2049–2052: *"Is the supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ equal to $\log_3 2$? Modulo $16$ the largest value is $73/174=0.420$"*).
- **Gate 2 status:** `PASS` (`#1701` `watch-1`, `#1702` `watch-5`, `#1703` `watch-6`; receipts in `targets/vasilyev-2611.20344-q7.10/notes/novelty-gate2-watch-{1,5,6}.md`).

## 2. Independent Exact Verifier (`check-check-2.py`)
Executed `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py` (pure exact `int` / `Fraction` arithmetic, zero floats, `Command exited with code 0`):
- **Table 5.3 baseline:** Reproduced `mod 4` (`3` uniformly descending, max $\pi = 1/4$), `mod 8` (`20` uniformly descending, max $\pi = 5/18$), and spot-checked the `mod 16` optimal set `{1, 3, 6, 7, 8, 11, 13}` ($\pi = 73/174$).
- **Lemma 1 (Dyadic-shell base sets & De Bruijn conjugacy):** Across `6` base sets $S_0(J)$ ($m \in \{2, 3, 4, 5\}$), verified $\lambda(S_0) = 1/2 + \sum_{j \in J} 2^{-(j+2)}$, forward Lipschitz property, $2$-to-$1$ exact $2$-adic preimages, bijectivity of $\Phi_n$, De Bruijn conjugacy, and exact path-count identity $P_0^n = 2^{-n}\mathbf{1}\mathbf{1}^\top$.
- **Lemmas 2–5 & Theorem 6 (Barina sieve & stationary convergence):** Exhaustively tested `5` concrete Barina sieve instances $(m, J, \mu, L)$ up to $n = 7$ ($N = 128$):
  - Verified exact lockout stopping time $\tau(r)$ (`Lemma 2(a)`) and exact Karp maximum cycle mean $\mu^* < \mu$ with $3^a < 2^\ell$ (`Lemma 2(b)`).
  - Verified `Lemma 3` exponential tail bound $\lambda_n(B_n) \le m \exp(-2\delta^2 \lfloor L/m \rfloor)$ via exact rational Taylor upper bounds when $L \ge m$.
  - Enumerated all `57,344` length-$n$ directed paths from every $y \in \mathbb{Z}/2^n\mathbb{Z}$, verifying backward uniqueness `(y, z, T)` (`Lemma 4`), total inclusion order of $\mathcal{F}_0(y)$ and $|\mathcal{F}(y)| \le 2^{m-1}(L+1)$ (`Lemma 5(a)-(b)`), and $P_n^n(y, z) \le 2^{-n} \cdot 2^{m-1}(L+1)$ (`Lemma 5(c)`).
  - Solved exact `Fraction` stationary distributions $\mu_C$ on every sink SCC, verifying all three inequalities of `Theorem 6` (`summaries=[(4,6,18,'39/176'), (4,7,27,'5/18'), (3,6,19,'125/442'), (3,7,29,'1489/4102'), (5,7,42,'1/5')]`).
