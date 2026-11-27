# Independent Check Report (`check-3`) — `targets/gaetz-2512.08168-conj1/`

- **Checked at (UTC):** 2026-11-26T23:30Z
- **Checker:** `check-3` (independent; written without reading `verify.py` or author's `notes/`)
- **Primary source inspected:** `arXiv:2512.08168v2` (Christian Gaetz and Yibo Gao, *"Billey--Postnikov posets, rationally smooth Schubert varieties, and Poincar\'e duality"*, revised 2026-06-08), fetched via `tools/arxiv_fetch.py query --id-list 2512.08168` (`v2` is latest) and `tools/arxiv_fetch.py eprint 2512.08168 --extract` (`tools/.arxiv_cache/eprint/2512.08168/main.tex`).

## 1. Primary-Source Fidelity & Definition Match

- **Conjecture 1.3 (`main.tex` lines 113–116, `\label{conj:union-intersection}`):**
  > Let $W$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K, J \cup K \in \mathrm{BP}(w)$.
- **Definitions (`main.tex` lines 192–205, `\label{def:BP}`):**
  - $\ell$, $\le$ (Bruhat order), $\le_L$ (left weak order), $W_J$, $W^J$, $w = w^J w_J$, $D_L(u)$, $D_R(u)$, $\mathrm{Supp}(u) = \{s \in S \mid s \le u\}$, and $\mathrm{BP}(w) := \{J \subset S \mid \mathrm{Supp}(w^J) \cap J \subset D_L(w_J)\}$.
- **Match:** Verbatim match in `TARGET.md` and `PROOF.md`. No quantifier, rank, finiteness, or definition drift.

## 2. Line-by-Line Proof Audit & Independent Mechanical Verification

Reviewed every step of `PROOF.md` (Lemmas 1–5 and Theorem 1 Parts 1–2):
- All arguments use only finite reduced words, standard Coxeter axioms (Deletion, Exchange, Subword Property, sign homomorphism, parabolic decomposition uniqueness/length-additivity), and require no finiteness of $|W|$ or $|S|$.
- Wrote independent exact Tits-representation verifier `targets/gaetz-2512.08168-conj1/notes/check-check-3.py` (exact integer, $\mathbb{Z}[\sqrt{2}]$, and $\mathbb{Z}[\phi]$ arithmetic, zero floating point) without reading `verify.py`, testing Lemmas 1–5 and Theorem 1 (intersection & union closure of $\mathrm{BP}(w)$) on:
  - Finite Coxeter groups: $A_3$ ($24$ elements), $B_3$ ($48$ elements), non-crystallographic $H_3$ ($120$ elements);
  - Bounded-length balls of infinite Coxeter groups: affine $\widetilde{C}_2$ ($\ell \le 7$, $76$ elements), right-angled Coxeter group $C_4$ ($\ell \le 6$, $575$ elements), and non-crystallographic rank-4 hyperbolic group ($m_{01}=5, m_{12}=3, m_{23}=\infty$, $\ell \le 6$, $197$ elements).

- **Command run:**
  ```bash
  .venv/bin/python targets/gaetz-2512.08168-conj1/notes/check-check-3.py
  ```
- **Raw output:**
  ```text
  A_3 PASS: verified 24 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  B_3 PASS: verified 48 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  H_3 PASS: verified 120 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  tilde_C_2(len<=7) PASS: verified 76 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  RACG_C4(len<=6) PASS: verified 575 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  Hyperbolic_4(len<=6) PASS: verified 197 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
  PASS
  ```

## 3. Verdict

**PASS** — Primary source matches `TARGET.md` and `PROOF.md` verbatim, and all lemmas and main closure theorem pass line-by-line review and independent exact Coxeter verification.
