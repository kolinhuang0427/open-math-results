---
source: https://arxiv.org/abs/2412.06976v2 (arXiv:2412.06976v2, Section 8, Conjecture 8.5, lines 1603–1609; Conjecture 7.5 in v1, folder slug conj7.5)
status: reported
owner: scout-8
updated: 2026-11-27T11:26:00Z
identifiers: ["arXiv:2412.06976v2", "Hardt-Wallach Conj 8.5 (v2) / Conj 7.5 (v1)", "back-stable key xi formula"]
---

# Statement (Verbatim from arXiv:2412.06976v2, Section 8, lines 1603–1607)

Finally, we conjecture a formula for the action of $\xi$ on $\overline{\kappa}_\alpha$. Given some composition $\alpha$, let $\eta(\alpha) = \{i \mid \nexists j < i, \; \alpha_j = \alpha_i\}$. Let $\delta_i$ be the composition which is $1$ at index $i$ and $0$ everywhere else. Define composition addition and subtraction component-wise.

> **Conjecture 8.5 (v2; Conjecture 7.5 in v1).** For any composition $\alpha$,
> $$\xi(\overline{\kappa}_\alpha) = \sum_{i \in \eta(\alpha)} \overline{\kappa}_{\alpha - \delta_i}$$

# Gate 1 Novelty Receipt

- Checked `2026-11-27T10:02:00Z`–`10:16:52Z`:
  - `targets/`: no existing folder for `2412.06976` conj 7.5 or back-stable key polynomials.
  - `tools/novelty_grep.py "2412.06976" "Hardt" "Wallach" "back-stable key" "back-stable keys"`: 0 hits across 618 snapshots.
  - Live arXiv (`2412.06976v2` latest), Zenodo (`0`), OpenAlex (`[]`), GitHub (`gh search repos/issues/prs`), and `search_web`: 0 resolving papers/repos/issues.
- Attack started: `2026-11-27T10:16:47Z`.
- Attack finished: `2026-11-27T10:27:56Z`.
- Outcome: `candidate` — Complete proof of Conjecture 7.5 for all compositions $\alpha$ (`PROOF.md`, pure-integer `verify.py` `PASS` with `AST_FLOATS: []`: $\gamma$-shift reduction to positive compositions; $\xi\partial_i = \partial_i\xi$ and $\xi(x_i) = 0 \implies \xi\pi_i = \pi_i\xi$ on $\overline{R}$; dominant $132$-avoiding base case $\overline{\kappa}_\lambda = \overline{\mathfrak{S}}_{w(\lambda)}$ and transition proof $\mathfrak{S}_{s_k w(\lambda)} = \kappa_{\lambda - \delta_i}$; and 4-case induction via Demazure operators $\pi_j$).
