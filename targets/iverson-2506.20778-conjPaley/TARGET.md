source: https://arxiv.org/abs/2506.20778 (v1, 2025-06-25, Section 4, Conjecture conj:Paley)
status: reported
owner: attack-1
updated: 2026-11-27T05:56:00Z
identifiers: ["2506.20778", "Iverson", "Mixon", "Asymmetric SICs over finite fields", "Paley I", "conj:Paley"]

# Iverson–Mixon (2025) — Conjecture (`conj:Paley`)

- **Started:** 2026-11-27T02:41:40Z

## Exact Statement
From Joseph W. Iverson and Dustin G. Mixon, *Asymmetric SICs over finite fields*, arXiv:2506.20778v1 (25 June 2025), Section 4 (`2025.06.25.tex`, lines 829–840):

> **Conjecture (`conj:Paley`).** Given a prime power $q > 11$ with $q \equiv 3 \bmod 4$, consider the ``Paley I'' Hadamard matrix $H$ of order $d:=q+1$.
> Then the following hold:
> - **(a)** $\mathrm{Aut}_s(\tilde{H}) \cong P\Gamma L(2,q)$ has exactly two orbits on $[d] \times [d]$, namely, $\{(i,i) : i \in [d]\}$ and its complement, and
> - **(b)** for any prime $p \equiv 3 \bmod 4$ that divides $d-8$, the SIC $\{x_{ij}\}$ in $\mathbb{F}_{p^2}^d$ constructed by Theorem~\ref{thm.main} has $\mathrm{Aut}_s(\{x_{ij}\}) = \iota(\mathrm{Aut}_w(H))$ and $\mathrm{Aut}_w(\{x_{ij}\}) = \mathrm{Aut}_s(\tilde{H})$.
>
> In particular, there exist non-transitive SICs in infinitely many dimensions over various finite fields.

Definitions from Sections 2–3 (`lines 87–99, 334–417, 452, 462–488`):
- For a modular Hadamard matrix $H \in K^{d \times d}$ with $i$th row $r_i^\top$, $\tilde{H} \in K^{[d]^2 \times [d]^2}$ is defined entrywise by $\tilde{H}_{(i,j),(k,l)} = [r_k r_i^\top]_{j,l} = H_{k,j} H_{i,l}$.
- $\mathrm{Aut}_s(\tilde{H}) \le S_{[d]\times[d]}$ consists of all permutations $\pi$ for which there exist $\varepsilon_{i,j} \in \{\pm 1\}$ such that $\tilde{H}_{\pi(i,j),\pi(k,l)} = \varepsilon_{i,j} \varepsilon_{k,l} \tilde{H}_{(i,j),(k,l)}$.
- $\iota(\pi,\sigma)(i,j) = (\pi(i), \sigma(j))$, and by Theorem `thm:sandwich`(c), $\iota(\mathrm{Aut}_w(H)) \le \mathrm{Aut}_s(\{x_{ij}\}) \le \mathrm{Aut}_w(\{x_{ij}\}) \le \mathrm{Aut}_s(\tilde{H})$.

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T02:45:00Z
- **Local `novelty_grep.py`:** Searched `"2506.20778"`, `"Iverson"`, `"Paley"`, `"asymmetric SIC"` across 413 files (`watch/snapshots/**`, including `1337`, `trureturing*`, `aliromman/math`, `openai/math`, `formal-conjectures`, `discovered/`): 0 hits for `2506.20778`, `Iverson`, or `asymmetric SIC`.
- **arXiv / GitHub / Zenodo / Web:** `arxiv_fetch.py query --id-list 2506.20778` shows `v1` (2025-06-25) is latest; `gh search repos "2506.20778"` returned 0 hits; `zenodo.org/api/records?q=2506.20778` returned 0 hits; `search_web` returned only the paper itself.
- **What was not covered:** Papers/repos not indexed by arXiv/GitHub/Zenodo/web search/local snapshots as of 2026-11-27T02:45Z.
- **Verdict:** Open (passes Gate 1).

## Screening Summary (`scout2-2`, 2026-11-27T03:20:00Z)
- **Verdict:** `ESCALATE` — see [notes/screen-scout2-2.md](notes/screen-scout2-2.md).
- Proved computationally ($q = 3,7,11,19,23,27$) that all $\le 4$-vertex invariants of $G^{(x)}$ are identical on diagonal $\Delta$ vs off-diagonal (it is always $\mathrm{srg}(d^2-1, d^2/2, d^2/4, d^2/4)$), whereas **5-vertex $K_4$-counts per vertex `K4_per_u` in $G^{(x)}$** strictly separate $\Delta$ from $[d]^2 \setminus \Delta$ for $q = 19, 23, 27$ (while colliding at $q = 7, 11$, explaining $q > 11$).
- Further verified that once $\Delta$ is invariant, canonical switching puts $\tilde{H}|_\Delta$ into $2I_d - J_d$ and off-diagonal $\Delta$-signatures satisfy $|\langle v_{ij}, v_{ji}\rangle| = d-4$ vs $\le 8$ or $12$ for non-transpose pairs ($O(\sqrt{q})$ via Weil), directly attacking the authors' stated obstruction.
