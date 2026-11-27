# Adversarial Audit — `targets/gaetz-2512.08168-conj1/`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T23:59Z` (Gate 3 pending)
- **Target:** Conjecture 1.3 (`conj:union-intersection`) of Christian Gaetz and Yibo Gao, *"Billey--Postnikov posets, rationally smooth Schubert varieties, and Poincar\'e duality"*, `arXiv:2512.08168v2` (`math.CO`, submitted 2025-12-09, revised 2026-06-08).
- **Isolation:** Inspected ONLY primary source (`arXiv:2512.08168v2`, `tools/.arxiv_cache/eprint/2512.08168/main.tex`, plus cited Richmond–Slofstra / Slofstra / Oh–Richmond TeX sources via helper), `TARGET.md`, `PROOF.md`, independent checker files (`notes/check-check-3.md`, `notes/check-check-3.py`), Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`), and adversarial helper report (`notes/audit-helper-gaetz.md`). Did **not** read `verify.py` or author scratch `notes/`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Fidelity & Definition Verification

Verified directly against `tools/.arxiv_cache/eprint/2512.08168/main.tex` (`2512.08168v2`, sole latest version on arXiv, no journal-ref/DOI) and `notes/audit-helper-gaetz.md` §1:

1. **Exact statement match (`main.tex` lines 95–116):**
   - Theorem 1.1 (`thm:intro-bp-pattern-characterization`), Theorem 1.2 (`thm:intro-union-intersection`), and **Conjecture 1.3** (`conj:union-intersection`, lines 113–116):
     > *Let $W$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K, J \cup K \in \mathrm{BP}(w)$.*
   - `TARGET.md` and `PROOF.md` quote Conjecture 1.3 verbatim with zero quantifier or scope drift.
2. **Exact definition match (`main.tex` lines 192–205, Definition 2.1 `def:BP`):**
   - Arbitrary Coxeter system $(W, S)$ (following Björner–Brenti; $|W|$ and $|S|$ need not be finite, and every $w \in W$ has finite support), length $\ell$, Bruhat order $\le$, left weak order $\le_L$, parabolic subgroup $W_J = \langle J \rangle$, minimal left-coset representatives $W^J$ of $W/W_J$, unique length-additive parabolic decomposition $w = w^J w_J$, left descent set $D_L(u) = \{s \in S \mid \ell(su) < \ell(u)\}$, support $\mathrm{Supp}(u) = \{s \in S \mid s \le u\}$, and $\mathrm{BP}(w) := \{J \subseteq S \mid \mathrm{Supp}(w^J) \cap J \subseteq D_L(w_J)\}$ (noting `main.tex` uses `\subset` for `\subseteq`, as confirmed by lines 204, 468, and 494).
   - `PROOF.md` matches every convention identically (left vs. right parabolic decompositions, left vs. right weak order, $D_L$ vs. $D_R$).
3. **Minor non-blocking `TARGET.md` citation slip (not in `PROOF.md`):**
   - `TARGET.md` line 29 parenthetically cites the rank-$\le 3$ case in the primary source as `"Theorem 3.7 / Section 3.3"`. In `main.tex`, `3.7` is `Definition 3.7` (`def:BP-poset`, Section 3.3), while the rank-$\le 3$ union/intersection theorem is **Theorem 3.15** (`thm:rank-three-union-intersection`, lines 463–466) in **Section 3.5** (`\label{sec:rank-three}`). `PROOF.md` does not repeat this citation slip.

---

## 2. Adversarial Line-by-Line Mathematical Audit of `PROOF.md`

Audited every lemma, case split, quantifier, and edge case ($w = e$, $J, K \in \{\emptyset, S\}$, infinite $|W|$, infinite rank $|S|$ with infinite $J, K \subseteq S$, non-crystallographic $m_{ij}$, $m_{ij} = \infty$) with zero gaps found:

- **Standard Coxeter foundations (lines 7–24):** Deletion Property, Left/Right Exchange Property, Subword Property of Bruhat order, sign homomorphism $\epsilon: W \to \{\pm 1\}$, and existence/uniqueness/length-additivity of $w = w^J w_J$ all hold for arbitrary Coxeter systems $(W, S)$ regardless of $|S|$ (every $w \in W$ has a finite reduced expression, and minimal-length coset representatives exist by well-ordering of $\mathbb{N}_{\ge 0}$).
- **Lemma 1 (Elementary Parabolic Properties, lines 26–39):**
  - (1) Reduction in $A^*$ by Deletion + Subword Property for $s \le u$ yields $\mathrm{Supp}(u) \subseteq A$ and downward Bruhat closure of $W_A$. Complete.
  - (2) $w = xu$ ($\ell$-additive) + $x = x^A x_A \implies w = x^A(x_A u)$, so uniqueness gives $w^A = x^A, w_A = x_A u$ and $\ell(w_A) = \ell(x_A) + \ell(u)$, i.e. $u \le_L w_A$. Complete.
  - (3) Splitting a reduced subword $\mathbf{u} = \mathbf{a}\mathbf{b}$ of $\mathbf{x}^J \mathbf{x}_J$ gives $a \le x^J$, $b \in W_J$, $u^J = a^J \le a \le x^J$. Complete.
- **Lemma 2 (0-Hecke / Demazure Action and Monotonicity, lines 43–64):**
  - (1) $(s * x) * t = s * (x * t)$ verified across all four exhaustive length cases (parity via $\epsilon$ leaves only $\ell(sxt) \in \{k, k+2\}$ in Case 4; in Case 4b $\ell(sxt) = k$, Right Exchange on reduced $s s_1 \cdots s_k$ cannot delete any $s_i$ without contradicting $\ell(xt) = k+1$, so it deletes $s$ — valid even for $k = 0$, $x = e$ — yielding $sx = xt$). Complete.
  - (2) $\mathrm{Dem}(s\mathbf{b}) = s * \mathrm{Dem}(\mathbf{b})$ by induction using (1); $\mathrm{Dem}(\mathbf{a}\mathbf{b}) \ge_L \mathrm{Dem}(\mathbf{b})$ by induction using $s * y \ge_L y$ and transitivity of $\le_L$; $\mathrm{Dem}(\mathbf{w}) = w$ for reduced $\mathbf{w}$ by induction on $\ell(w)$. Complete.
- **Lemma 3 (Subword–Demazure Formula and Parabolic Bruhat Slices, lines 68–88):**
  - (1) $\mathrm{Sub}(\mathbf{a}) = [e, \mathrm{Dem}(\mathbf{a})]$ (for all not-necessarily-reduced finite words $\mathbf{a} \in S^*$) proved cleanly by induction on $|\mathbf{a}|$ via the Lifting/Subword cases $\ell(xt) > \ell(x)$ and $\ell(xt) < \ell(x)$. Complete.
  - (2) For any reduced $\mathbf{w}$ of $w$ and any (even infinite) $A \subseteq S$, $\mathbf{w}|_A$ is a finite word in $A^*$ and $[e, w] \cap W_A = [e, \mathrm{Dem}(\mathbf{w}|_A)]$; antisymmetry of Bruhat order shows $m(w, A) := \mathrm{Dem}(\mathbf{w}|_A)$ is independent of $\mathbf{w}$. Complete.
- **Lemma 4 (Characterizations of $\mathrm{BP}(w)$, lines 92–114):**
  - Equivalence of (1) $\mathrm{Supp}(w^J) \cap J \subseteq D_L(w_J)$, (2) $[e, w] \cap W_J = [e, w_J]$ (equivalently $m(w, J) = w_J$), and (3) $u \le w \iff u^J \le w^J \text{ and } u_J \le w_J$ verified in every direction. Crucially, the "if" direction of (3) is explicitly proved unconditionally (without assuming $J \in \mathrm{BP}(w)$) by concatenating reduced subwords $\mathbf{u}^J \mathbf{u}_J$ of $\mathbf{w}^J \mathbf{w}_J$. Complete.
- **Lemma 5 (Comparison Lemma in $W_{J \cup K}$, lines 117–128):**
  - Let $u, v \in W_M$ ($M = J \cup K$) with $J, K \in \mathrm{BP}(u)$, $u_J \le v_J$, $u_K \le v_K$. Taking minimal-length $z \in [e, u] \setminus [e, v]$ (valid by well-ordering of $\ell \in \mathbb{N}_{\ge 0}$): $J \in \mathrm{BP}(u)$ and $z \le u$ give $z_J \le u_J \le v_J$ by Lemma 4(3). If $z^J \le v$, then Lemma 1(3) gives $z^J = (z^J)^J \le v^J$, and the unconditional "if" direction of Lemma 4(3) gives $z \le v$, contradiction. Thus $z^J \in [e, u] \setminus [e, v]$; minimality of $\ell(z)$ forces $\ell(z_J) = 0$, hence $z \in W^J$. By symmetry on the same $z$, $z \in W^K$. By Lemma 1(1), $z \le u \in W_M \implies z \in W_M$, so $z \neq e$ would have a right descent $s \in M = J \cup K$, contradicting $z \in W^J \cap W^K$. Thus $z = e \in [e, v]$, contradiction. Complete and airtight.
- **Theorem 1 (Conjecture 1.3, lines 133–163):**
  - **Part 1 (Intersection closure, $L := J \cap K \in \mathrm{BP}(w)$):** Taking reduced $\mathbf{w} = \mathbf{w}^J \mathbf{w}_J$, Lemma 1(1) gives $\mathbf{w}_J|_K = \mathbf{w}_J|_L$. Using $J \in \mathrm{BP}(w)$ (Lemma 4(2)) and $W_L \subseteq W_J$, Lemma 3(2) gives $\mathrm{Dem}(\mathbf{w}_J|_L) = m(w, L) =: m$. Using $K \in \mathrm{BP}(w)$ and independence of $\mathrm{Dem}(\mathbf{w}|_K)$ from $\mathbf{w}$ (Lemma 3(2)), Lemma 2(2) yields $w_K = \mathrm{Dem}((\mathbf{w}^J|_K)(\mathbf{w}_J|_L)) \ge_L m$. Transitivity with $w_K \le_L w$ gives $m \le_L w$, so Lemma 1(2) gives $m \le_L w_L$, while $w_L \in [e, w] \cap W_L = [e, m]$ gives $w_L \le m$; comparing lengths forces $m = w_L$, hence $L \in \mathrm{BP}(w)$ by Lemma 4(2). Complete.
  - **Part 2 (Union closure, $M := J \cup K \in \mathrm{BP}(w)$):** Setting $m := m(w, M) \in W_M$, we have $w_M \le m \le w$. Writing $\mathbf{w}|_M = (\mathbf{w}^J|_M)\mathbf{w}_J$ (since $J \subseteq M$) gives $m \ge_L w_J$ by Lemma 2(2), hence $w_J \le_L m_J$ by Lemma 1(2); conversely $m_J \in [e, w] \cap W_J = [e, w_J]$ forces $m_J = w_J$, and sandwiching $[e, m_J] = [e, w_J] \subseteq [e, m] \cap W_J \subseteq [e, w] \cap W_J = [e, m_J]$ gives $J \in \mathrm{BP}(m)$ (and symmetrically $m_K = w_K, K \in \mathrm{BP}(m)$). Applying Lemma 1(2) twice to $w_J \le_L w$ gives $m_J = w_J \le_L (w_M)_J$ (and symmetrically $m_K \le (w_M)_K$). Lemma 5 then yields $m \le w_M$, forcing $m = w_M$, hence $M \in \mathrm{BP}(w)$ by Lemma 4(2). Finally, $\emptyset, S \in \mathrm{BP}(w)$ and closure under finite $\cap, \cup$ make $(\mathrm{BP}(w), \subseteq)$ a distributive sublattice of $(2^S, \subseteq)$. Complete.

---

## 3. Independent Computational Verification & Adversarial Stress Testing

1. **Re-execution of independent checker verifier (`notes/check-check-3.py`):**
   - Ran `.venv/bin/python /Users/kev/Documents/open-math/targets/gaetz-2512.08168-conj1/notes/check-check-3.py` (exact Tits geometric representations over $\mathbb{Z}, \mathbb{Z}[\sqrt{2}], \mathbb{Z}[\phi]$): **PASS**, exit code `0`, wall time `19.83s` across $A_3$ (24), $B_3$ (48), $H_3$ (120), $\widetilde{C}_2$ ($\ell \le 7$, 76), right-angled $C_4$ ($\ell \le 6$, 575), and rank-4 hyperbolic $(m_{01}=5, m_{12}=3, m_{23}=\infty)$ ($\ell \le 6$, 197).
   - Code review of `check-check-3.py` confirmed exact arithmetic, faithfulness of Tits reflection matrices, closure of bounded-length balls under subword/descent operations, and faithful checking of Lemmas 1–4 and Theorem 1 (note: lines 25–105 contain an unused draft class `ExactCoxeter`, harmless dead code; line 378 skips Lemma 5 when `len(elems) > 150`).
2. **Additional adversarial exact stress tests (`notes/audit-helper-gaetz.md` §3B):**
   - To close the two gaps left by `check-check-3.py` (non-reduced words in Lemma 3(1) and rank $\ge 4$ testing of Lemma 5), ran an independent exact Tits verifier over $\mathbb{Z}, \mathbb{Z}[\phi], \mathbb{Z}[\sqrt{3}]$ computing Bruhat intervals independently via Strong-Exchange reflection deletions:
     - **Lemma 3(1) on strictly non-reduced words:** 500 random strictly non-reduced words of lengths $2 \dots 8$ in $H_3$ and `Hyperbolic_4`: **PASS**.
     - **Lemma 5 & Theorem 1 (non-vacuous incomparable pairs $\emptyset \subsetneq J \cap K \subsetneq J, K \subsetneq J \cup K \subsetneq S$):**
       - `Hyperbolic_4` ($\ell \le 6$, 197 elements): **PASS** (`155,244` qualifying Lemma 5 tuples; `860` incomparable BP pairs, `192` non-vacuous).
       - `tildeG2+extra` (rank 4, $m_{01}=6, m_{12}=3, m_{23}=3$ over $\mathbb{Z}[\sqrt{3}]$, $\ell \le 6$, 145 elements): **PASS** (`114,882` Lemma 5 tuples; `762` incomparable pairs, `188` non-vacuous).
       - `RACG_P5` (rank-5 path $P_5$, $\ell \le 5$, 297 elements): **PASS** (`851,876` Lemma 5 tuples; `17,170` incomparable pairs, `1,690` non-vacuous).
       - `RACG_C5` (rank-5 cycle $C_5$, $\ell \le 5$, 441 elements): **PASS** (`1,184,384` Lemma 5 tuples; `19,250` incomparable pairs).

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-gaetz.md` §2, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) confirmed:
- **No prior proof found** in classical Coxeter/BP literature (inspected TeX of Richmond–Slofstra `1408.0084v2`, Slofstra `1312.7540v2`, Richmond–Slofstra `1510.06060v1`, and Oh–Richmond `2409.03096v1`; none study or prove union/intersection closure of $\mathrm{BP}(w)$) or in 2025–2026 sources (`2512.08168v2` sole latest version; Gaetz–Gao's later preprints `2610.22857v1` and `2611.33572v1` inspected directly and unrelated; OpenAlex `citing_count: 0` on `2026-11-26T22:55:34Z`; Zenodo, Crossref, web search, 356 local snapshot files, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing`, and `the-omega-institute/trureturing-tools` all clear — verified verbatim that `SCREENED-OUT-R52.md` line 401 refers solely to `2512.08168` Conjecture 1.9, already disproved in Gaetz–Gao's own Theorem 6.2).
- **No `CONTESTED.md`** exists in `targets/gaetz-2512.08168-conj1/`.
- **What Is Not Established / Caveats:**
  - Proves Conjecture 1.3 (`conj:union-intersection`) for all Coxeter groups, establishing that $(\mathrm{BP}(w), \subseteq)$ is a distributive sublattice of $2^S$. It does not address the paper's other open items (e.g. Remark on type-$E$ Lehmer codes) nor claim Birkhoff finite-poset representation for infinite $|S|$ (not part of Conjecture 1.3).
  - Semantic Scholar API was rate-limited (`HTTP 429`) during checks (mitigated by OpenAlex `citing_count: 0`, live arXiv, Zenodo, Crossref, GitHub, and web searches).
  - Internal audit and finite-ball exact computations are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`.

- **Gate 3 Novelty Clearance (`2026-11-27T03:34Z`–`04:10Z`, refreshed):** **PASS** across `notes/novelty-gate3-watch-1.md` (refreshed `04:10Z`), `notes/novelty-gate3-watch-3.md` (refreshed `03:34Z`–`03:52Z`, co-covering `watch-6`), and `notes/novelty-gate3-watch-5.md` (`03:40Z`), plus prior `notes/novelty-gate3-watch-6.md` (`00:57Z`), covering live arXiv `2512.08168v2`, OpenAlex citing cache (`citing_count: 0`), Zenodo, `470` snapshots, and all 15+ competing GitHub repos (`trureturing-tools` `SCREENED-OUT-R52.md` targets Conj 1.9 only). Cleared for coordinator verification.
