# Blind Adversarial Audit — `targets/vereshchagin-2611.30127-q2/`

- **Auditor:** `@audit-1` (`auto`)
- **Primary Source Verified:** Nikolay Vereshchagin, *"How Much Randomness is Needed to Convert MA Protocols to AM Protocols?"*, `arXiv:2611.30127v1` (2026-11-23; CSR 2022 / ECCC TR22-060), `tools/.arxiv_cache/eprint/2611.30127.src` (`main-eng.tex`), **Section 6** (`\section{Open questions}`, lines 774–780), Section 1 (Conjecture 1, lines 101–106; algebrization remark, lines 151–154), and Section 2 (polynomial convention & Definitions 1–6, lines 213–320).
- **Files Audited (blind — author `verify.py` and scratch `notes/` not read):**
  - `targets/vereshchagin-2611.30127-q2/TARGET.md`
  - `targets/vereshchagin-2611.30127-q2/PROOF.md`
  - `targets/vereshchagin-2611.30127-q2/notes/check-check-1.md`
  - `targets/vereshchagin-2611.30127-q2/notes/check-check-1.py`
- **Verdict:** **PASS** (re-audit after `#1932` / `#1940` / `#1941` fixes; **Label:** `"written proof, internally audited"`).

---

## 1. Statement & Citation Fidelity (Re-Audit Verified)

- **Section 6 fix verified:** `TARGET.md` (L2, L13), `PROOF.md` (L5), and `notes/check-check-1.md` (L7–8, L17) all now accurately cite **Section 6** (`\section{Open questions}`, `main-eng.tex` lines 774–780; Section 7 is `\section{Acknowledgments}` at line 783) and `tools/.arxiv_cache/eprint/2611.30127.src` (`main-eng.tex`).
- **Verbatim fidelity:** Open Questions 2 & 3 (L774–780), Conjecture 1 (L101–106), Section 1 algebrization remark (L151–154), polynomial convention $p(n)=b(n+1)^c$ ($b,c \ge 1$, L218), and Definitions 1–6 (L222–320) match `main-eng.tex` verbatim.

---

## 2. Full Mathematical & Computational Audit Summary

- **Main Results (NO to both Open Question 2 and Open Question 3):** Single Boolean oracle $A : \{0,1\}^* \to \{0,1\}$ with canonical multilinear extension $\widetilde{A}$ (Aaronson–Wigderson `[AW]`, TOCT 2009, over all finite fields $\mathbb{F}_q$) separating $\mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a]$ from $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', a', t']$ whenever $a'(n) \le m(n) - \log_2(2(a'(n)+m'(n)+2t'(n)^2)+8) - 17$ for infinitely many $n$, via length-only languages. Simultaneously refutes algebrization of $\mathrm{MA}[m, a] \subset \mathrm{AM}[*, p(a)]$, $\mathrm{MA}[m, a] \subset \mathrm{PP}[p(a)]$, and Knop's Conjecture 1 ($\mathrm{Heur}\text{-}\mathrm{MA}[m, a] \subset \mathrm{Heur}\text{-}\mathrm{AM}[*, p(a)]$).
- **All proof components verified airtight:**
  - **Lemma 4.1:** Exact integer Gilbert–Varshamov packing ($8 \cdot 27^{20} < 32^{20}$) giving canonical code $\mathrm{Enc}_L : \{0,1\}^{\lfloor L/20 \rfloor} \to \{0,1\}^L$ with pairwise Hamming distance $\ge \lfloor L/3 \rfloor + 1 > L/3$ for all $L \ge 20$.
  - **Lemma 5.1:** Complete $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\mathrm{cc}}$ lower bound for $\mathrm{OR}_M \circ \mathrm{EQ}_N$ under $(\mathrm{P1})$–$(\mathrm{P4})$ via KL/Pinsker coordinate selection, Cauchy–Schwarz rectangle-shrinking ($\Delta = 2(a'+m'+C)+8$), Ping-Pong $(0.9)$-block-min-entropy restoration (invariants $(\mathrm{L1})$–$(\mathrm{L3})$, strict potential drop $-0.01 N|S| + 1 \le 0$), and final union bound at $i = K = 2^{a'-1}+1$.
  - **Theorem 1 (§6):** Prefix-free disjoint blocks $\mathcal{D}_{i,n}$, Lemma 6.1 ($\mathrm{MAP}^A[m_i, a_i] \cap \mathrm{MA}^A[m_i, a_i]$ with soundness $< 8/27 < 1/3$), Lemma 6.2 ($2 t'(n)^2$-bit deterministic additive simulation $f_A(X) + f_B(W) + c_{\mathrm{fix}} \in \mathbb{F}_q$ cleanly handling same-length blocks in $S_{\mathrm{fix}}$), stage-by-stage diagonalization freezing lengths $\le B_s = \max\{k_i(n), t'(n)\}$, and polynomial specialization $a(n)=n+1, m(n)=(b\cdot 2^c+1)(n+1)^{c+1}$.
  - **Theorem 2 (§7):** Length-only reduction at $\delta = 1/10$ ($n/\delta = 10n$ integer for all $n \ge 0$) converting $\mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[*, p(a)]$ to worst-case $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m'', a'', t'']$ with margins $> 3/5 > 1/2 > 2/5$, contradicting Theorem 1.
- **Independent Verifier Execution (re-run after patches):**
  - Command: `.venv/bin/python -u targets/vereshchagin-2611.30127-q2/notes/check-check-1.py`
  - AST audit: `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: [248, 255, 256]` (`pathlib.Path` joins only — zero floating-point arithmetic).
  - Exit code `0`, final output `PASS` (including live `tarfile` verification of Section 6 numbering).

---

## 3. Handoff
**PASS** — handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 live freshness check (`< 1h`, incl. ECCC/venues) and `@coordinator` reporting.
