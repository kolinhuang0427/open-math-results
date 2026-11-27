# Target: `mbirika-2301.05758-ques30`

- **Source:** aBa Mbirika, Janee Schrader, and Jürgen Spilker, *"Pell and associated Pell braid sequences as GCDs of sums of $k$ consecutive Pell, balancing, and related numbers"*, `arXiv:2301.05758v3` (`aBa_Janee_Jurgen_JIS_final_published_version_for_arXiv.tex`, published in *Journal of Integer Sequences*, Vol. 26, Issue 6 (2023), Article 23.6.4), Section 6.1 (*GCD of sums of $k$ consecutive squares*), **Question 30** (L1199–1216).
- **Status:** reported
- **Owner:** scout-11
- **Created (UTC):** 2026-11-27T09:38:11Z
- **Updated (UTC):** 2026-11-27T09:45:00Z
- **Identifiers:** `arXiv:2301.05758v3`, `Question 30` (L1199–1216), `Convention 1` (`\label{conv:notation_for_curl_GCD_closed_forms}`, L183–193), `Definitions 3, 6, and 7` (L233–268), sequences `(B_n)`, `(C_n)`, `(b_n)`, `(c_n)` (`OEIS:A001109`, `A001541`, `A053141`, `A002315`).

## Definitions (quoted from `arXiv:2301.05758v3`, Section 1–2, L183–189, L233–268)

> **Convention 1** (`L183–189`): When $(S_n)_{n \geq 0}$ is any of the six sequences $(P_n)_{n \geq 0}$, $(Q_n)_{n \geq 0}$, $(B_n)_{n \geq 0}$, $(C_n)_{n \geq 0}$, $(b_n)_{n \geq 0}$, or $(c_n)_{n \geq 0}$, we establish the notation $\mathcal{G}_S^m(k)$ to denote the GCD of all sums of $k$ consecutive $m^{\mathrm{th}}$ powers of sequence terms, in the respective six settings:
> $$\mathcal{G}_B^m(k) = \gcd\left\{ \left(\sum_{i=1}^k B_{n+i}^m\right)_{n \geq 0}\right\}, \quad \mathcal{G}_C^m(k) = \gcd\left\{ \left(\sum_{i=1}^k C_{n+i}^m\right)_{n \geq 0}\right\},$$
> $$\mathcal{G}_b^m(k) = \gcd\left\{ \left(\sum_{i=1}^k b_{n+i}^m\right)_{n \geq 0}\right\}, \quad \mathcal{G}_c^m(k) = \gcd\left\{ \left(\sum_{i=1}^k c_{n+i}^m\right)_{n \geq 0}\right\}.$$

> **Definitions 3, 6, and 7** (`L233–268`):
> - Pell $(P_n)_{n\ge 0}$: $P_n = 2P_{n-1} + P_{n-2}$ with $P_0 = 0, P_1 = 1$ (`A000129`).
> - Associated Pell $(Q_n)_{n\ge 0}$: $Q_n = 2Q_{n-1} + Q_{n-2}$ with $Q_0 = 1, Q_1 = 1$ (`A001333`).
> - Balancing $(B_n)_{n\ge 0}$: $B_n = 6B_{n-1} - B_{n-2}$ with $B_0 = 0, B_1 = 1$ (`A001109`).
> - Lucas-balancing $(C_n)_{n\ge 0}$: $C_n = 6C_{n-1} - C_{n-2}$ with $C_0 = 1, C_1 = 3$ (`A001541`).
> - Cobalancing $(b_n)_{n\ge 0}$: $b_n = 6b_{n-1} - b_{n-2} + 2$ with $b_0 = 0, b_1 = 0$ (`A053141`).
> - Lucas-cobalancing $(c_n)_{n\ge 0}$: $c_n = 6c_{n-1} - c_{n-2}$ with $c_0 = -1, c_1 = 1$ (`A002315`).

## Verbatim Question Statement (`arXiv:2301.05758v3`, Section 6.1, L1199–1216)

> **Question 30.** Can we find nice closed forms for $\mathcal{G}_B^2(k)$, $\mathcal{G}_C^2(k)$, $\mathcal{G}_b^2(k)$, and $\mathcal{G}_c^2(k)$? Thus far from evidence collected from `Mathematica`, we do have the following observations:
> - For all $k \geq 1$, we have $\mathcal{G}_B^2(k) = \begin{cases} \frac{1}{2}\mathcal{G}_C^2(k), & \text{if } k \text{ is even}; \\ \mathcal{G}_C^2(k), & \text{if } k \text{ is odd}. \end{cases}$
> - For all $k \geq 1$, we have $\mathcal{G}_c^2(k)$ satisfying $\mathcal{G}_C^2(k) = \begin{cases} \mathcal{G}_c^2(k), & \text{if } k \not\equiv 3 \pmod{6}; \\ \frac{1}{3}\mathcal{G}_c^2(k), & \text{if } k \equiv 3 \pmod{6}. \end{cases}$
> - For all $k \geq 1$, we have $\mathcal{G}_b^2(k) \equiv 0 \pmod{4}$.

*(Note: `\newtheorem{theorem}{Theorem}` in `aBa_Janee_Jurgen_JIS_final_published_version_for_arXiv.tex` L86–100 numbers all `theorem`, `corollary`, `lemma`, `proposition`, `result`, `definition`, `example`, `conjecture`, `question`, `convention`, and `remark` environments sequentially on a single global counter; the Question at L1199 is #30 in that counter.)*

## Gate 1 Novelty Check Receipt (`2026-11-27T09:34Z`)

- `targets/` check: no existing `mbirika-2301.05758-ques30` folder. (Note: `2301.05758` Conjecture 32 at L1237 on $\gcd(Q_k, k) > 1$ is separate and already settled in `trureturing`.)
- `tools/novelty_grep.py "curl{B}{2}" "curl{C}{2}" "curl{b}{2}" "curl{c}{2}" "2301.05758" "Lucas-cobalancing"` across all 608 files in `watch/snapshots/**`: `0` hits.
- `.venv/bin/python tools/arxiv_fetch.py query --max-results 10 "Mbirika cobalancing"`: `25` hits, latest `2301.05758v3` itself (`2023-06-28`); later Mbirika/Tekcan/Oyengo preprints (`2611.21142v1`, `2511.10797v2`, `2510.02008v2`, `2504.10152v2`, `2408.14632v2`) do not resolve Question 30 on $\mathcal{G}_B^2, \mathcal{G}_C^2, \mathcal{G}_b^2, \mathcal{G}_c^2$.
- `search_web` for `"2301.05758" OR "Lucas-cobalancing" "cobalancing" squares "mod 4"`: returns `arXiv:2301.05758` itself; no published resolution of Question 30 found.
- Verdict: OPEN, clear to attack.
