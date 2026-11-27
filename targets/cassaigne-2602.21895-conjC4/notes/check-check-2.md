# Independent Check Report: `targets/cassaigne-2602.21895-conjC4/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2602.21895v1` (Julien Cassaigne, Bastián Espinoza, Michel Rigo, Manon Stipulanti, *"Symbols frequencies in the Thue--Morse word in base $3/2$ and related conjectures"* — confirmed sole/latest version via `tools/arxiv_fetch.py query --id-list 2602.21895`), TeX file `tools/.arxiv_cache/eprint/2602.21895/merge_version.tex`.
- **Exact sections/lines verified:**
  - Definition & relations (`merge_version.tex` lines 362–417, `eq:t32relations`): $t_0 = {\tt 0}$, $t_{3n} = t_{3n+1} = t_{2n}$, $t_{3n+2} = 1 - t_{2n+1}$ ($\forall n \ge 0$), initial prefix `00111011111011011...`.
  - Section 1.3 (`merge_version.tex` lines 431–483, `lem:morphic_image`): $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`A357448`) with $\varphi({\tt 0}) = {\tt 010}$, $\varphi({\tt 1}) = {\tt 101}$, initial prefix `0100101011011010101011011...`.
  - Section 1.4 (`merge_version.tex` lines 485–496, Conjecture `(C_4)`): existence of frequencies of all finite words $w \in \{{\tt 0}, {\tt 1}\}^*$ in $\mathbf{t}'$ (and $\mathbf{t}_{3/2}$), and equality of frequencies of $w$ and its reversal $\widetilde{w}$.
  - Section 3 (`merge_version.tex` lines 1265–1273, `thm:existence_freqs_iff_mun_exist` and lines 1406–1424, `eq:mod2m`): $\lim_{N\to\infty} C_n(c,k,N)/N = 2^{-n-1}$ for single symbols $c \in \{{\tt 0}, {\tt 1}\}$, and Section 7 (`merge_version.tex` lines 2116–2121): open length-$2$ factor frequencies (`3/10, 2/10` in $\mathbf{t}_{3/2}$; `4/10` for `01` in $\mathbf{t}'$).
- **Comparison with `TARGET.md` and `PROOF.md`:**
  - `TARGET.md` and `PROOF.md` match `arXiv:2602.21895v1` verbatim with zero quantifier or definition drift (proving existence, explicit rationality, reversal invariance, and bit-complement invariance for all $w \in \{0,1\}^*$ in both $\mathbf{t}_{3/2}$ and $\mathbf{t}'$).
  - Every step of `PROOF.md` (Lemmas 1–2, Proposition 1 diagonal compactness + $(2/3)^m / (1/3)^m$ contraction, Proposition 2 involution $\sigma(m) = 3M+1-m, \tau(j) = 2M-j$, and Section 4 sliding-block transfer via $\varphi$) is verified rigorous and gap-free.

## 2. Independent Mechanical Check

Written independently from `arXiv:2602.21895v1` (`merge_version.tex`) and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/cassaigne-2602.21895-conjC4/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/cassaigne-2602.21895-conjC4/notes/check-check-2.py
  ```
- **Raw output (exit code 0):**
  ```text
  Primary-source prefixes (t_{3/2} len 17, t' len 25) match merge_version.tex verbatim: PASS
  Lemma 1 (preimage lengths l_0, l_1, l_2 for 2 <= L <= 50): PASS
  Lemma 2 (exact desubstitution recurrence C_n(w,k,N), |E|<=3L+3 for 2<=L<=5, N<=10000): PASS
  Exact Fraction frequencies & rev/comp symmetries (t_{3/2} 1<=L<=9, t' 1<=L<=7; L=2 values): PASS
  Empirical density agreement on t_{3/2}[0..100000) and t'[0..300000) (L<=5, filtered n<=2): PASS
  PASS (all checks passed in 1.058s)
  ```

## 3. Gate 2 & Contest Status

- **Gate 2 receipts present:** `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md` (both PASS).
- **Contested status:** No `CONTESTED.md` present.
