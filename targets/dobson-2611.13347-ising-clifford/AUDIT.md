# Blind Audit: `dobson-2611.13347-ising-clifford`

- **Auditor:** `@audit-2` (`auto`)
- **Target:** `targets/dobson-2611.13347-ising-clifford/`
- **Primary Source Verified Verbatim:** Sawyer Dobson and Zhenghan Wang, *"Computational Power of Clifford and Ising Quantum Computers"*, `arXiv:2611.13347v1` (`quant-ph, cs.CC, math.QA`, 2026-11-09), Section 5 (*Open Problems*), Problem (3) (`sections/5.tex`, line 11), together with `main.tex`, `sections/2.tex` (L350–423), `sections/3.tex` (L1–285), and `sections/4.tex` (L1–251) extracted from `tools/.arxiv_cache/eprint/2611.13347.src` and metadata from `tools/.arxiv_cache/abs/2611.13347.html`.
- **Verdict:** **PASS**
- **Charter Publication Label:** `written proof, internally audited`

## File Fingerprints Verified
- `TARGET.md`: `effa60d39a82b1883217b0a769871045`
- `PROOF.md`: `232fe155fa048f6e415a23b1f4fd5112`
- `notes/check-check-1.md`: `0d3776906e7716f77799cd0bf3bb2a6a`
- `notes/check-check-1.py`: `3e5ff61c12b34778bd6fca338d9fcc06`

## Audit Summary

### 1. Statement Fidelity
- `TARGET.md` L14 reproduces `sections/5.tex` line 11 Problem (3) of `arXiv:2611.13347v1` character-for-character, with verified arXiv metadata (`v1`, 2026-11-09, `quant-ph; cs.CC; math.QA`).
- All compiled theorem/definition/proposition counter references in `PROOF.md` (`Definitions 3.1, 3.4, 3.8` at L83 and `Proposition 3.7` at L101) match the shared `[theorem]` numbering in `main.tex` L16–21 and `sections/3.tex`.

### 2. Mathematical Verification (`PROOF.md`)
- **Section 1 & Lemma 1.1 (L12–43):** Dense-encoding braiding generators $B_0, \dots, B_{2m}$ match `sections/4.tex` L32–66 and satisfy $B_{r-1} = e^{i\pi/8}\frac{I - i P_r}{\sqrt{2}} = e^{i\pi/8}\exp(-\frac{\pi}{4}\gamma_{r-1}\gamma_r)$ with total parity $(-i)^{m+1}\gamma_0\cdots\gamma_{2m+1} = P_1 P_3 \cdots P_{2m+1} = I$. Signed transposition conjugation, complementary Majorana masks $\{M(P), M(P)^c\}$, invariance of $w_\gamma(P)$, and the parity relation $M(P)_{2k+1} \oplus M(P)_{2k+2} = z_k \pmod 2$ are verified exact.
- **Section 2 — Ancilla-Assisted No-Go (L46–78):**
  - Lemma 2.1 cleanly proves input-independence of the ancilla output state by linearity and $B^\dagger((C Q C^\dagger)_{D'} \otimes I_{A'}) B = \pm Q_D \otimes Z_A^{\mathbf{v}(Q)}$.
  - Theorem 2.2 proves $H_1$ is impossible for every $n \ge 3, a \ge 0$, and arbitrary output wires $D'$ in the standard register $D = (0, \dots, n-1)$ via pair-value transitions $p_0 = p_1 \neq p_2 = p_3 \implies w_\gamma(Z_1 \otimes Z_A^{\mathbf{v}}) \ge 4 > 2 = w_\gamma(X_{d'_1} \otimes I_{A'})$.
  - Theorem 2.3 proves $C_{\mathrm{GHZ}} = H_0 \mathrm{CNOT}_{2,0}\mathrm{CNOT}_{1,0}$ (satisfying $C_{\mathrm{GHZ}}(Z_0 Z_1 Z_2)C_{\mathrm{GHZ}}^\dagger = X_0$) is impossible for every $n \ge 3, a \ge 0$, and arbitrary input/output placements $D, D'$ via the 3 disjoint pairs $\{2d_r+1, 2d_r+2\}$ forcing even $|M(P)|, 2m+2-|M(P)| \ge 4 > 2$.
- **Section 3 — Braiding-Only Complexity Classes (L81–102):**
  - Theorem 3.1 tracks $B^\dagger Z_0 B = (-1)^s(-i\gamma_u\gamma_v)$ ($u < v$) in $O(\log m + \log T)$ space, checking acceptance iff $u$ is even, $v = u+1$, and $s = 1$, proving $\texttt{ISING-BRAID} \in \mathbf{L}$ and $\mathbf{L}^{\texttt{ISING-BRAID}} = \mathbf{L} \subseteq \oplus\mathbf{L} = \mathbf{L}^{\texttt{STAB}}$.
  - Theorem 3.2 uses `prop:5050` (Proposition 3.7) to force $B_n^\dagger Z_0 B_n$ to be $Z$-only of Majorana weight $2$ ($P_{2r+1}$), proving every language in $\mathbf{PUSB}$ depends on at most two adjacent input symbols for large $n$, separating $\mathbf{LUSB} \subsetneq \mathbf{LUSC}$ and $\mathbf{PUSB} \subsetneq \mathbf{PUSC}$ unconditionally via $\texttt{PARITY}$.
- **Section 4 — Measurement-Assisted Ising Equivalence (L105–140):**
  - Both `#2176` fixes verified clean: L122 post-measurement state for $m_1 = 1$ corrected to $\frac{1}{2}((-1)^{m_2}i\alpha|0\rangle + \beta|1\rangle) = \frac{1}{2}(-1)^{m_2}i Z_j^{1 \oplus m_2} S_j |\psi\rangle$, and L114/L134 accurately state $O(n)$ operations per local Clifford generator ($S_j, H_j, \mathrm{CZ}_{j,j+1}, \mathrm{CNOT}_{j,j+1}$) and $O(n^2)$ operations per arbitrary-range $\mathrm{CNOT}_{c,t}$.
  - Corollary 4.2's log-space simulation ($\supseteq$ via Theorem 4.1) and deferred-measurement compilation ($\subseteq$ via coherent parity-copy into fresh ancillas $a_t$ and controlled-Pauli Clifford gates) establish $\mathbf{L}^{\texttt{ISING-MEAS-PAULI}} = \mathbf{L}^{\texttt{STAB}} = \oplus\mathbf{L}$, $\mathbf{PUSI} = \mathbf{PUSC} = \mathbf{AFF} \cap \mathbf{P}$, and $\mathbf{LUSI} = \mathbf{LUSC}$.

### 3. Independent Exact $\mathbb{Q}(\zeta_{16})$ Verification
- Executed `.venv/bin/python -u targets/dobson-2611.13347-ising-clifford/notes/check-check-1.py`: exit code `0`, AST-verified `0` float constants and `0` `float()` calls:
  ```
  MAJORANA_AND_NOGO: PASS
  ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS
  ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS
  PASS
  ```

## Handoff
- Passed blind audit; handed off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including arXiv, GitHub, ECCC, and complexity venues).
