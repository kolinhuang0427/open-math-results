# Blind Independent Audit Report — `targets/orzechowski-2611.34308-q3.9/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2611.34308/{Measurable-equidecompositions-in-Q_p_n.tex,references.bib}`, Salehi Golsefidy's primary source `tools/.arxiv_cache/eprint/1602.00403.src` (`SG_Introduction.tex`), `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-1.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Kamil Orzechowski, *"Measurable equidecomposability and the Banach--Ruziewicz problem over locally compact non-Archimedean valued fields"*, `arXiv:2611.34308v1` (dated `November 24, 2026`, submitted `2026-11-25T13:00:20Z`, verified sole version via live `tools/arxiv_fetch.py query --id-list 2611.34308 --no-cache`), Section 3, **Question 3.9** (`\label{q:prime_residue_field}`, `Measurable-equidecompositions-in-Q_p_n.tex` L621–623).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all 3 fixes from initial FAIL `#1601` were cleanly applied to `PROOF.md`; publication label: `"written proof, internally audited"`).

---

## 1. Primary Source & Statement Fidelity Check

- **Question wording (`Measurable-equidecompositions-in-Q_p_n.tex` L621–623):**
  > `\begin{question}\label{q:prime_residue_field} Let $\LL$ be a locally compact non-Archimedean valued field with residue field $\FF_p$, $p$ prime. Is the action $\Iso(\LL)\acts (\LL,m_{\LL})$ expanding? \end{question}`
  Matches `TARGET.md` L12 verbatim.
- **Section & theorem numbering:** Verified every environment in Sections 2–3 against `\newtheorem{theorem}{Theorem}[section]` (L16–27):
  - Section 2: Definition 2.8 (`def:domain_of_exp`, L321–334), Definition 2.10 (`def:expanding_action`, L342–344), Remark 2.11 (`rem:expanding_one_set`, L346–349), Definition 2.13 (`def:local_spectral_gap`, L359–367), Remark 2.14 (`rem:operator_norm_SG`, L369–374), Theorem 2.15 (`thm:Golsefidy's_theorem`, L393–398), Lemma 2.16 (`lem:LSG=domain`, L403–411), Theorem 2.17 (`thm:consequences_of_parad+expanding`, L416–422).
  - Section 3: Proposition 3.1 (`prop:SG_for_group_acting_on_itself`), Proposition 3.2 (`prop:transfer_of_expansion`), Theorem 3.3 (`th:main_expanding`), Corollary 3.4 (`cor:final`), Example 3.5 (`ex:empty_interior`), Corollary 3.6 (`cor:unramified`), Corollary 3.7 (`cor:general_isometries`), Question 3.8 (`q:positive_characteristic`), **Question 3.9** (`q:prime_residue_field`, L621–623).
- **`TARGET.md` check:** All primary definitions and citations match `Measurable-equidecompositions-in-Q_p_n.tex` verbatim. Zero defects in `TARGET.md`.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Step 1 (L13–21) — Polish space, Radon measure, and measure preservation:** **SOUND.**
  - $|\mathbb{L}^\times| = \langle c \rangle$ ($c > 1$), $|\pi| = c^{-1}$, $|\pi^{-n}\mathcal{O}_{\mathbb{L}}/\pi^m\mathcal{O}_{\mathbb{L}}| = p^{n+m}$, each $\pi^{-n}\mathcal{O}_{\mathbb{L}}$ compact metrizable, hence $\mathbb{L}$ Polish and $m_{\mathbb{L}}$ $\sigma$-finite, finite on compact sets, nonzero on nonempty open sets.
  - Measure preservation of $\mathrm{Iso}(\mathbb{L}) \curvearrowright (\mathbb{L}, m_{\mathbb{L}})$ follows cleanly from `[Christensen, Theorem 1]` (L386) plus $g(\mathcal{O}_{\mathbb{L}}) = g(0) + \mathcal{O}_{\mathbb{L}}$ and $0 < m_{\mathbb{L}}(\mathcal{O}_{\mathbb{L}}) < \infty$.
- **Step 2 (L22–83) — Pro-$p$ filtration, ultrametric/measure isomorphism $\Phi$, and extension $\tilde{\alpha}_g$:** **SOUND** (with 1 minor omission noted below).
  - For $m \ge e$ ($e=1$ for $p \ge 3$, $e=2$ for $p=2$), $2m \ge m+1$ yields the surjective homomorphism $\theta_m : K_m \to \mathfrak{sl}_2(\mathbb{F}_p)$ with $\ker(\theta_m) = K_{m+1}$. Verified explicitly even for $p=2$: $\{E_{12}, E_{21}, \mathrm{diag}(1, -1) = I_2\}$ is an $\mathbb{F}_2$-basis of $\mathfrak{sl}_2(\mathbb{F}_2) = \{X : \mathrm{tr}(X)=0\}$.
  - **Minor polish (L47):** `PROOF.md` asserts each $U_{3(m-e)+r} = \theta_m^{-1}(V_r)$ is a **normal** subgroup of $U_0$ without justifying normality in $U_0$ (vs. only in $K_m$). This IS true because $g \in U_0 = K_e \implies g \equiv I \pmod p \implies g A g^{-1} \equiv A \pmod p$, so $\theta_m(g h g^{-1}) = \theta_m(h)$ for all $h \in K_m$ (i.e., $U_0$ acts trivially by conjugation on $K_m/K_{m+1}$). Add this 1-line check for completeness.
  - The coset-tree bijection $\Phi = \psi \circ \tau : (U_0, d_U) \to (\mathcal{O}_{\mathbb{L}}, d_{\mathbb{L}})$ is a surjective isometry sending every level-$k$ coset $u U_k$ to a translate of $\pi^k\mathcal{O}_{\mathbb{L}}$, so $\Phi_* m_{U_0} = m_{\mathbb{L}}(\mathcal{O}_{\mathbb{L}})^{-1} m_{\mathbb{L}}|_{\mathcal{O}_{\mathbb{L}}}$ by $\pi$-$\lambda$ uniqueness on the countable basis of clopen balls.
  - Extending $\Phi \circ L_g \circ \Phi^{-1}$ by the identity on $\mathbb{L} \setminus \mathcal{O}_{\mathbb{L}}$ yields a surjective isometry $\tilde{\alpha}_g \in \mathrm{Iso}(\mathbb{L})$ by the ultrametric isosceles principle ($|x| \le 1 < |y| \implies |\tilde{\alpha}_g(x) - y| = |y| = |x - y|$).
- **Step 3 (L85–104) — Spectral gap via Theorem 2.15 & local spectral gap on $\mathcal{O}_{\mathbb{L}}$:**
  - Finite generation of $\Gamma$ (Schreier's lemma), density $\overline{\Gamma} = U_0$ in $\mathrm{GL}_2(\mathbb{Q}_p)$ (surjectivity of $\mathrm{SL}_2(\mathbb{Z}) \to \mathrm{SL}_2(\mathbb{Z}/p^k\mathbb{Z})$ via local-ring transvections), and semisimple Zariski closure $\overline{\Gamma}^{\mathrm{Zar}} = \mathrm{SL}_2$ are all **SOUND**.
  - **DEFECT 1 (Blocking — Bipartite $-1$ eigenvalue obstruction at $p = 2$ unless $I \in S$, `PROOF.md` L89 & L93):**
    - `PROOF.md` L89 chooses *"a nonempty finite symmetric generating set $S \subseteq \Gamma$"* without requiring $I \in S$, and L93 asserts $\|T_S|_{L^2_0(U_0, m_{U_0})}\| < 1$ and sets $\delta := 1 - \|T_S|_{L^2_0(U_0, m_{U_0})}\| > 0$.
    - When $p = 2$, $U_0 = K_2$ surjects onto $K_2/K_3 \cong (\mathbb{Z}/2\mathbb{Z})^3$ and therefore admits nontrivial continuous characters $\chi : U_0 \to \{\pm 1\}$ with $\chi \in L^2_0(U_0, m_{U_0})$. For an arbitrary symmetric generating set $S \subseteq \Gamma$ satisfying $\chi(S) = \{-1\}$ (for instance, the generating set `S_gens` tested in `check-check-1.py` L269–276, where $\chi(a,b,c) = (-1)^{b+c}$ evaluates to $-1$ on all $6$ generators!), we have $T_S(\chi) = -\chi$, so **$\|T_S|_{L^2_0(U_0, m_{U_0})}\| = 1$** (not $< 1$) and $\delta = 0$!
    - (Although Orzechowski's Theorem 2.15 — echoing the same wording in Salehi Golsefidy `arXiv:1602.00403` `SG_Introduction.tex` Theorem 1 — omits an explicit $1 \in \Omega$ / non-bipartite clause in its two-sided norm statement while the one-sided gap $\sup\mathrm{Spec}(T_S|_{L^2_0}) < 1$ holds unconditionally, `PROOF.md` L89–95 uses $\delta = 1 - \|T_S|_{L^2_0}\| > 0$ directly.)
    - **Fix:** Stipulate **$I \in S$** in `PROOF.md` L89 (*"fix a finite symmetric generating set $S \subseteq \Gamma$ containing $I$"*) and note explicitly that $I \in S$ ensures $\langle T_S \varphi, \varphi \rangle \ge -1 + \frac{2}{|S|} \|\varphi\|_2^2$ for all $\varphi$, ruling out $-1 \in \mathrm{Spec}(T_S|_{L^2_0})$ even for $p = 2$ (while still satisfying Theorem 2.15 and contributing $0$ to $\sum_{g \in S} \|g\cdot\varphi - \varphi\|_2$).
  - Once $\delta > 0$ is established, the Cauchy–Schwarz derivation (L95–97, noting triviality when $\|\varphi\|_2 = 0$), the measure-preserving pull-back to $\mathcal{O}_{\mathbb{L}}$ (L99–102, noting $g \mapsto \tilde{\alpha}_g$ is injective), and Lemma 2.16 (L103) are **SOUND**.
- **Step 4 (L105–128) — Extension from $\mathcal{O}_{\mathbb{L}}$ to all $C \in \mathcal{B}_{m_{\mathbb{L}}} \cap \mathcal{C}(\mathrm{Iso}(\mathbb{L}) \curvearrowright \mathbb{L})$:** **SOUND.**
  - Mutual covering via translations + Remark 2.11 works directly, and the self-contained Definition 2.8(i) covering-transfer proof (for both $\eta \in (0, 1)$ and $\eta \ge 1$) was verified line-by-line with zero gaps.
- **DEFECT 2 (Blocking — Statement-fidelity overclaim in L5 Remark on `Corollary 3.7`):**
  - `PROOF.md` L5 claims that combining the result with paradoxicality of $\mathrm{Iso}(\mathbb{L}) \curvearrowright \mathbb{L}$ (`[KO-CMB, Theorem 11]`) via Theorem 2.17 *"immediately extends Corollary 3.7 (`cor:general_isometries`) to prime residue fields $\mathbb{F}_p$ as well."*
  - However, `Corollary 3.7` (L603) explicitly asserts the existence of a **countable** group $\Gamma \le \mathrm{Iso}(\mathbb{L})$ that is paradoxical and expanding, whereas $\mathrm{Iso}(\mathbb{L})$ is uncountable.
  - **Fix:** Either state precisely that Theorem 2.17 applied to $\mathrm{Iso}(\mathbb{L})$ extends the measurable equidecomposability and Banach–Ruziewicz conclusions (assertions (i) and (ii) of Corollary 3.4) to $\mathrm{Iso}(\mathbb{L})$ for prime residue fields $\mathbb{F}_p$, OR (if claiming full Corollary 3.7 with a countable subgroup $\Gamma$) give the 2-line construction of a countable subgroup $\Gamma \le \mathrm{Iso}(\mathbb{L})$ generated by $\tilde{S}$, a countable dense subgroup of translations of $\mathbb{L}$, and finitely many isometries witnessing $\mathrm{Iso}(\mathbb{L})$-paradoxicality of $\mathcal{O}_{\mathbb{L}}$ (applying Lemma 2.4, Corollary 2.5, and Remark 2.11).

---

## 3. Independent Verifier Audit (`notes/check-check-1.py`)

- Re-executed `.venv/bin/python -u targets/orzechowski-2611.34308-q3.9/notes/check-check-1.py`: exited `0`, `PASS` across all four verification suites (`Step 2(1)`, `Step 2(2)-(3)`, `Step 3`, `Step 4`).
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Line-by-line inspection confirms zero bugs; notably, L280–300 already explicitly verified that `S_gens + {I}` has all $L^2_0$ eigenvalues strictly inside $(-1, 1)$ for $p \in \{2, 3, 5\}$ (whereas `S_gens` without $I$ admits eigenvalue $-1$ at $p = 2$). No changes needed to `notes/check-check-1.py`.

---

## 4. Novelty Gate 2 Status

- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`2026-11-27T15:02Z`–`15:04Z`, `0` settlement hits across `727` snapshots + `hexagonmath-index.md`, `2611.34308v1` sole arXiv version, OpenAlex `cited_by=0`, GH/Zenodo/HexagonMath/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

All three items flagged in the initial audit (`#1601`) have been cleanly patched in `PROOF.md` (`@scout-9`, `#1603`) and independently re-verified (`TARGET.md` and `notes/check-check-1.py` unchanged):

1. **`PROOF.md` L89 & L93:** Stipulates $I \in S$ in the finite symmetric generating set $S \subseteq \Gamma$ and proves $\langle T_S\varphi, \varphi \rangle \ge (-1 + 2/|S|)\|\varphi\|_2^2$, eliminating $-1 \in \mathrm{Spec}(T_S|_{L^2_0})$ even at $p = 2$ while preserving Theorem 2.15 and contributing $0$ to $\sum_{g \in S}\|g\cdot\varphi - \varphi\|_2$.
2. **`PROOF.md` L5 Remark:** Accurately narrowed to Theorem 2.17's measurable equidecomposability and Banach–Ruziewicz conclusions (assertions (i)–(ii) of Corollary 3.4 with $\mathrm{Iso}(\mathbb{L})$ in place of $\Gamma$), without overclaiming Corollary 3.7's countable subgroup $\Gamma$.
3. **`PROOF.md` L47:** Added the explicit 1-line check that $g \in U_0 = K_e$ ($e \ge 1$) satisfies $g \equiv I \pmod p$, hence $g A g^{-1} \equiv A \pmod p$ and $\theta_m(g h g^{-1}) = \theta_m(h)$, establishing normality of every $U_k$ in $U_0$.
4. **Independent Verifier:** `.venv/bin/python -u targets/orzechowski-2611.34308-q3.9/notes/check-check-1.py` (already verified exit `0`, `PASS`, `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`, unchanged MD5 `9ba8955e3beb03bb584a0a47f84ff7db`).

**Final Verdict: PASS.** Handed off to `@watch-1 @watch-5 @watch-6` for Gate 3 freshness verification (`<1h`).
