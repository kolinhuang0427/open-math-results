# Target: Buan–Hanson–Marsh (arXiv:2610.34398v1) Conjecture 7.2 (`\label{conj:TFordered}`)

- **source**: `arXiv:2610.34398v1` (Aslak B. Buan, Eric J. Hanson, and Bethany R. Marsh, *Lifting $\tau$-exceptional sequences*, 2026-10-25), Section 7.1 (`\section{Conjectures}`, `\subsection{TF-ordered $\tau$-rigid modules}`, `\label{sec:conj1}`), **Conjecture 7.2** (`\label{conj:TFordered}`, lines 1932–1938 of `lifting_arxiv_25102026.tex`; tracked under legacy directory slug `targets/buan-2610.34398-conj6.2/`).
- **status**: `reported`
- **owner**: `attack-2`
- **updated**: `2026-11-27T11:54:00Z`
- **start_utc**: `2026-11-27T11:05:21Z`
- **identifiers**: `arXiv:2610.34398v1`, `math.RT`, `\label{conj:TFordered}`, `Conjecture 7.2`, `L_I`, `TF-ordered`

## Exact Statement

From `2610.34398v1/lifting_arxiv_25102026.tex`, Section 7.1, lines 1917–1938 (with $\Lambda$ a $\tau$-tilting finite finite-dimensional $k$-algebra, $I \subseteq \mathrm{rad}\Lambda$ a two-sided ideal, $F = (\Lambda/I)\otimes_\Lambda -$, $\Delta_I$ the injective map of Theorem 1.1 (`\label{thm:main1}`), $\omega$ and $\omega_I$ the Mendoza–Treffinger bijections from TF-ordered $\tau$-rigid modules to $\tau$-exceptional sequences of Theorem 7.1 (`\label{thm:TF-bij}`), and $L_I = \omega^{-1} \Delta_I \omega_I$):

> **Conjecture 7.2** (`\label{conj:TFordered}`). Let $(M_1, M_2, \ldots, M_t)$ be a TF-ordered $\tau$-rigid $\Lambda/I$-module and let
> $$L_I(M_1, M_2, \ldots, M_t) = (N_1, N_2, \ldots, N_t).$$
> Then $F(N_i) = M_i^{r_i} \amalg X$ where $X \in \mathrm{add}(\coprod_{j=i+1}^t M_j)$ and $r_i \geq 1$ is an integer.

## Resolution Summary

- **Verdict**: **PROVED** unconditionally (see [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/buan-2610.34398-conj6.2/PROOF.md) and exact-arithmetic verifier [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/buan-2610.34398-conj6.2/verify.py)).
- **Method**: Prove the strictly stronger 2-term presilting theorem (**Theorem 1**) by induction on $t \ge 1$: in $K^b(\mathrm{proj}(\Lambda/I))$, $F(P_{N_i}) \cong P_{M_i}^{r_i} \oplus \bigoplus_{j=i+1}^t P_{M_j}^{s_{ij}}$ with **no** shifted projective summands ($r_i \ge 1, s_{ij} \ge 0$). The base case ($i = t$) follows from `Proposition 4.8` and the Adachi–Iyama–Reiten bound $|M| + |P| \le \mathrm{rk}(\Lambda/I)$. For $1 \le i \le t - 1$, a 2-term Bongartz presentation of $P_{N_i}$ in $K^b(\mathrm{add} P_{B_Z})$ is pushed around the commuting square $K^b(\Phi_C) \circ K^b(F) \simeq K^b(F_Z) \circ K^b(\Phi_Z)$ (using `Proposition 5.6`, `Lemma 5.7`, `Proposition 5.8`, `Theorem 5.10`, and a direct mutation-pigeonhole silting reduction Proposition 2.3). Taking $H^0$ gives Conjecture 7.2 (**Corollary 2**), and primitivity of silting $g$-vectors further yields the sharp multiplicity **$r_i = 1$** for all $i$ (and $F(Z) \cong C$ in `Proposition 4.8(b)`, **Corollary 3**).
- **Exact Verification**: `.venv/bin/python -u targets/buan-2610.34398-conj6.2/verify.py` (AST-verified 0 floats, 0 true divisions) prints `PASS` in 3.3s across 10 algebra-quotient pairs (797 TF-ordered sequences, 2,303 terms, including Paper Examples 1–3, $C_3/J^4 \to C_3/J^3$, $D_4 \to D_4/\langle ca\rangle$, 2-cycle, $Q_4$, loop algebra, and $\Pi(A_3) \to kA_3$, with 114 non-trivial $X \neq 0$ terms and 13 non-$L_I$-lifted modules confirming $R[1] \neq 0$ in general).

## Gate 1 Novelty Receipt

- **Checked UTC**: `2026-11-27T11:06:26Z`–`2026-11-27T11:08:51Z` (full receipt in [notes/novelty-attack.md](file:///Users/kolinhuang/Documents/open-math/targets/buan-2610.34398-conj6.2/notes/novelty-attack.md), updating the initial `10:18Z` triage receipt).
- **Verdict**: **OPEN**.
- **`tools/novelty_grep.py`**: `0` hits across `651` local snapshot files for `2610.34398`, `TF-ordered`, `tau-exceptional`, `conj:TFordered`, `Buan`, `tau-rigid`, `tau-tilting` (incl. `openai-math`, `1337-solved-conjectures`, `the-omega-institute/trureturing`).
- **Live arXiv**: `2610.34398v1` (`2026-10-25`) is the sole version (`2610.34398v2` returns HTTP 404); live `math.RT` author/topic queries confirm no follow-up or resolution.
- **Live Zenodo / DataCite / Crossref / OpenAIRE / HAL / InspireHEP**: `0` matches for `2610.34398` and `conj:TFordered`; no follow-up works resolving Conjecture 7.2.
- **Live GitHub (`gh`) & Web search**: `0` repos/issues/code solving Conjecture 7.2 (`openai/math` HEAD git tree scanned directly).
- **Coverage limits**: OpenAlex and Semantic Scholar returned HTTP 429 during the check window (mitigated by live arXiv, DataCite, Crossref, InspireHEP, and web search).
