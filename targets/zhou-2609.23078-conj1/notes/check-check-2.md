# Check Report: `targets/zhou-2609.23078-conj1/` (`@check-2`)

**Verdict:** `PASS` (post `#1549` patch fixing Theorem 2 Step 2 in `PROOF.md`; zero floats).

## 1. Primary-Source Alignment (`arXiv:2609.23078v1`)
- Verified verbatim against `tools/.arxiv_cache/eprint/2609.23078/MAXIMAL_PROPER_EXTREMAL_SUBSET_IN_THE_CRYSTAL_BASIS_OF_A_FINITE-DIMENSIONAL_IRREDUCIBLE_MODULE.tex` (with compiled numbering verified from `\section{Introduction}` = §1):
  - `Conjecture 1` / §4 `Conjecture 4.1` (`\label{conj:main1-all-types}`, lines 136–138, 516–523): $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$ for $\lambda \in P^+$.
  - `Proposition 2.2` (`\label{prop:eimax-indep}`), `Proposition 3.7` (`\label{prop:max-proper-extremal}`), `Proposition 3.12` (`\label{prop:eimax-to-chkw}`), `Proposition 4.2` (`\label{prop:reduction}`), `Proposition 7.2` (`\label{prop:w0Tgew0fiT}`), and Hong–Kang §4.4 tensor crystal rule match the target definitions verbatim (`TARGET.md`/`PROOF.md` had an off-by-one section numbering offset noted by `@audit-1` in `#1579`).
- **Gate 2 status:** `PASS` (`#1531` `watch-6`, `#1532` `watch-1`, `#1533` `watch-5`; receipts in `targets/zhou-2609.23078-conj1/notes/novelty-gate2-watch-{1,5,6}.md`).

## 2. Independent Verification (`check-check-2.py`)
Executed `.venv/bin/python -u targets/zhou-2609.23078-conj1/notes/check-check-2.py` (pure exact `int` / `Fraction`, zero floats, `Command exited with code 0`):
- **Theorem 2 Step 2 (`PROOF.md` lines 270–290, post `#1549` fix):** Verified mathematically and computationally:
  1. Every highest-weight element of $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$ has the form $b_\rho \otimes d$ with weight $\eta \ge \nu_0 = \rho + \mathrm{wt}(b_\star)$ (tested across all 25 $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$ decompositions in $A_2, C_2, G_2, A_3, B_3, C_3$).
  2. PRV identification $\nu_0 = \overline{\rho + w_\circ \lambda}$ verified across all 31 crystals in $A_2, C_2, G_2, A_3, B_3, C_3, D_4, F_4$.
  3. Cyclic generation $U(\mathfrak{g})(v_\rho \otimes v_{w_\circ \lambda}) = V(\rho) \otimes V(\lambda) \implies \mathrm{mult}_{V(\rho)\otimes V(\lambda)}(V(\nu_0)) \le \dim V(\nu_0)_{\rho+w_\circ\lambda} = 1$ verified mathematically; exact crystal multiplicity $\mathrm{mult}(\nu_0) = 1$ confirmed on all 25 $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$ pairs.
- **Conjecture 1, Theorem 1, Lemma 4(2):** Using an independent exact `Fraction` Littelmann LS path crystal engine $\mathcal{P}(\lambda)$ across **31 crystals** in types $A_2, C_2, G_2, A_3, B_3, C_3, D_4, F_4$ and **11,643 tensor monotonicity comparisons**, verified $\tilde{e}_j^{\max} = \mathcal{P}_j$, $H(a \otimes b) - H(a \otimes \tilde{f}_i b) \in Q^+$, $H(\tilde{f}_i a \otimes b) - H(a \otimes b) \in Q^+$, $\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$, and $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$.
- **Lemma 1 folding & Lemma 2(3) gauge identity:** Verified non-negative Chevalley matrix folding ($A_3 \to C_2^\vee$ and $D_4 \to G_2^\vee$) and verified the exact path-ordered exponential gauge identity $g(\psi_u)(t) = y_j(a(t)) g(\psi)(t) y_j(-b)$ in $\mathrm{Mat}_4(\mathbb{Q}[t]/(t^{11}))$.
