# Check Report: `targets/hardt-2412.06976-conj7.5/` (`@check-1`)

**Verdict:** **PASS** (after `#827` patch fixing all 5 citation/numbering mismatches against `arXiv:2412.06976v2`).

## 1. Primary Source & Statement Verification
- Checked against `tools/.arxiv_cache/eprint/2412.06976/schubert-paper.tex` and the compiled PDFs of `arXiv:2412.06976v1` (28 pp.) and `arXiv:2412.06976v2` (32 pp.).
- `TARGET.md` and `PROOF.md` now match `arXiv:2412.06976v2` cleanly and verbatim:
  - Conjecture statement (`TARGET.md` L11–14) matches `schubert-paper.tex` lines 1603–1607 verbatim, accurately labeled **Section 8, Conjecture 8.5** in `v2` (noting `Conjecture 7.5` in `v1`, matching folder slug).
  - All `PROOF.md` references match `v2` compiled numbering: `Definition 2.2` (Lehmer code, `L324`), `Definition 3.4` (`L431`) & `Definition 3.13` (back-stable Schubert, `L562`), `Section 4.3, Proposition 4.21` (Nenashev's Leibniz rule on $\overline{R}$, `L807`), `Section 8, Eq. (34)` (nilplactic equivalence, `L1531–1537`), `Definition 8.1` (`L1563`), `Proposition 8.2` (`L1576`), `Proposition 8.3` (`L1584`), `Remark 8.4` (`L1598–1599`), and labels `eq:nabla-xi-olR-action` (`L800`) and `eq:key-stabilization` (`L1572`).
- Gate 2 novelty PASS receipts present from `watch-1`, `watch-5`, `watch-6`.

## 2. Independent Exact-Arithmetic Verification
Script: `targets/hardt-2412.06976-conj7.5/notes/check-check-1.py` (exact sparse integer polynomials over $\mathbb{Z}$ and `fractions.Fraction`, zero floats, built directly from primary definitions without reading author `verify.py` or `notes/`):
- `PASS` Lemma 1: $\xi \partial_i = \partial_i \xi$ on all 120 permutations in $S_5$ ($i=1..4$), and $x_i = \mathfrak{S}_{s_i} - \mathfrak{S}_{s_{i-1}}$ with $\xi(x_i) = 0$.
- `PASS` BJS compatible-sequence Schubert == divided-difference Schubert on all 120 permutations in $S_5$.
- `PASS` Lemma 2: `2310` exact $\pi_i(\kappa_\alpha)$ checks ($m=6, |\alpha| \le 5$).
- `PASS` Lemma 3(1)–(3): all `43` partitions with $|\lambda| \le 7$ and $\mathrm{supp}(w(\lambda)) \le 8$ ($132$-avoidance, $\mathfrak{S}_{w(\lambda)} = x^\lambda$, left-descent bijection with $\eta(\lambda)$, and $\mathfrak{S}_{s_k w(\lambda)} = \kappa_{\lambda - \delta_i}$).
- `PASS` Main conjecture in exact $\overline{\mathfrak{S}}$-basis: `922` positive compositions ($|\alpha| \le 6$ for $m \le 5$, $|\alpha| \le 5$ for $m \le 6$).
- `PASS` Section 4 induction transition identity: `1404` checks ($\beta_j > \beta_{j+1}$).
- `PASS Citations` (exit code `0`).
