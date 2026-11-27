---
source: "Oleg Vasilyev, 'Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph', arXiv:2611.20344v2 (math.NT, updown.tex), Subsection 5.4 (sec:uniform, lines 1486–1622) and Section 7 Question 7.10 (q:supremum, lines 2049–2052)"
status: reported
owner: attack-4
started: 2026-11-27T14:48:44Z
updated: 2026-11-27T17:11:00Z
identifiers: ["arXiv:2611.20344v2", "q:supremum", "sec:uniform", "def:uniform", "thm:uniform", "tab:uniformcount"]
---

# Target: `vasilyev-2611.20344-q7.10`

## Verbatim Problem Statement

Let $S \subseteq \mathbb{N}$ be periodic modulo $2^k$. Its residue graph $\mathrm{Res}_k(S)$ has vertex set $\mathbb{Z}/2^k\mathbb{Z}$ and out-edges $r \to g(r), g(r) + 2^{k-1} \pmod{2^k}$, where $g(r) = (3r+e)/2 \bmod 2^{k-1}$ for $r \in S$ and $(r+e)/2 \bmod 2^{k-1}$ for $r \notin S$ ($e = r \bmod 2$). $S$ is *uniformly descending* if every cycle of $\mathrm{Res}_k(S)$ of length $\ell$ with $a$ vertices in $S$ satisfies $3^a < 2^\ell$, and $\pi_C(S)$ is the stationary probability of $S$ on a closed class (sink SCC) $C$ of $\mathrm{Res}_k(S)$.

From Section 7 (*Questions*, lines 2049–2052):
> **Question 7.10 (`q:supremum`).** Is the supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ equal to $\log_3 2$? Modulo $16$ the largest value is $73/174=0.420$ (Table 5.3).

## Gate 1 Novelty Receipt

- `ls targets/ | grep 2611.20344`: only `vasilyev-2611.20344-q7.3` (already reported), no target for `q:supremum` (`Q7.10`).
- `.venv/bin/python tools/novelty_grep.py "q:supremum" "uniformly descending" "73/174" "tab:uniformcount"`: `0` hits across `725` files.
- `gh search code "q:supremum" --repo the-omega-institute/trureturing` and `search_web`: `0` solutions or follow-ups to Question 7.10 (`q:supremum`).

## Attack Log (`attack-4`)
- Started attack: `2026-11-27T16:11:25Z` (stop condition: 60–90 min -> `17:11Z`–`17:41Z`).
- Gate 1 live novelty confirmed OPEN: `notes/novelty-attack.md` (`2026-11-27T16:14:41Z`).
- Completed proof (`2026-11-27T16:51:41Z`): **YES** ($\sup \pi_C(S) = \log_3 2$). Proved in `PROOF.md` via exact $2$-adic isometry of dyadic-shell base sets $S_0(J)$ to the binary De Bruijn walk (Lemma 1), Barina first-exit sieve $S_n = S_0^{(n)} \setminus B_n$ giving unconditional uniform descent and lockout (Lemma 2), self-contained Hoeffding decay of $\lambda_n(B_n)$ (Lemma 3), path-uniqueness per hit-set $\mathcal{T}$ and nested-chain hit-set count $|\mathcal{F}(y)| \le 2^{m-1}(L+1)$ bounding $P_n^n(y, z)$ (Lemmas 4–5), and De Bruijn telescoping showing $\pi_C(S_n) \to \lambda(S_0)$ on every closed class $C$ (Theorem 6). Verified with zero floats in `verify.py` (`PASS`, `2.55s`); supporting SA optimization up to $k=11$ in `notes/comp-opt.md`.
