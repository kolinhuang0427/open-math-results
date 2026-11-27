---
slug: kovalyov-2611.32205-q1
title: Conservativity of IOpen + (Exp) over IOpen
source: arXiv:2611.32205v1 (math.LO, 2026-11-24), Konstantin Kovalyov, Section 3 (Question 3.5(1))
identifiers:
  arxiv: "2611.32205v1"
  subject: "math.LO"
owner: scout-9
status: reported
created: 2026-11-27T16:43:03Z
updated: 2026-11-27T17:23:00Z
attack_started_utc: 2026-11-27T16:43:03Z
---

# Target: Question 3.5(1) of Section 3 (`arXiv:2611.32205v1`)

## Verbatim Statement

From `main.tex`, Section 3 (`\section{Conservativity results for \IOpen + (\Exp)}`, lines 499–505):

> ```latex
> \begin{question}
>     \begin{enumerate}[(1)]
>         \item Is  $\IOpen + (\Exp)$ conservative over $\IOpen$?
>         \item More generally, what is the $\mathcal L_{OSR}$-fragment of $\IOpen + (\Exp)$?
>         \item  Is $\teip_{2^x}^+$ $\forall$-conservative over $\IOpen + (\Exp)$ in the language $\mathcal L_{\OSR}(\exp)$?
>     \end{enumerate}
> \end{question}
> ```

(Also closely linked to (2); the primary question attacked here is (1): whether every $\mathcal L_{\mathrm{OSR}}$-sentence provable in $\mathsf{IOpen} + (\mathrm{Exp})$ is already provable in $\mathsf{IOpen}$.)

## Primary Definitions (from `main.tex`, Section 2)

- $\mathcal L_{\mathrm{OSR}} := (+^{(2)}, \cdot^{(2)}, 0, 1, \leq^{(2)})$: language of ordered semirings; $\mathcal L_{\mathrm{OSR}}(\exp)$ adds the unary function symbol $\exp$.
- $\mathsf{DOSR}$: ordered semirings ($(\text{OR0})$–$(\text{OR13})$) with $x = 0 \vee 1 \leq x$ and $x \leq y \leftrightarrow \exists z (x + z = y)$.
- $\mathsf{IOpen}$: $\mathsf{DOSR}$ plus the open induction schema
  $$\big(\varphi(0, \overline y) \wedge \forall x\,(\varphi(x, \overline y) \to \varphi(x + 1, \overline y))\big) \to \forall x\,\varphi(x, \overline y)$$
  for every quantifier-free $\mathcal L_{\mathrm{OSR}}$-formula $\varphi(x, \overline y)$ (note: induction is ONLY over pure $\mathcal L_{\mathrm{OSR}}$ quantifier-free formulas, not formulas containing $\exp$).
- $(\mathrm{Exp})$: universal closure of
  $$\exp(1) = 2, \qquad \exp(x + y) = \exp(x)\exp(y), \qquad \exp(x) > x.$$
- $\mathsf{IOpen} + (\mathrm{Exp})$: deductive closure of $\mathsf{IOpen} \cup (\mathrm{Exp})$ in $\mathcal L_{\mathrm{OSR}}(\exp)$.
- $(\mathrm{Log})$: universal closure of $(x > 0) \to \exists y\,\big(\exp(y) \leq x < \exp(y + 1)\big)$; $\teip_{2^x}^+ := \mathsf{IOpen} + (\mathrm{Exp}) + (\mathrm{Log})$.
- Theorem 3.1 (`theorem_on_extension`): Every model of $\mathsf{IOpen}$ admits an end-extension to a model of $\mathsf{IOpen} + (\mathrm{Exp})$; hence $\mathsf{IOpen} + (\mathrm{Exp})$ is $\Pi_1$-conservative over $\mathsf{IOpen}$.

## Gate 1 Novelty Receipt

- Checked `2026-11-27T16:42:52Z`:
  - `novelty_grep.py` across `742` snapshot files (`2611.32205`, `Kovalyov`, `IOpen + (Exp)`): `1` unrelated match (`derkachkovalyov2017indefinitestieltjes.md` in `the-omega-institute/trureturing`).
  - `gh search prs/issues/repos "2611.32205"`: `0` matches (`gh search code` returned HTTP 403 rate-limit; `trureturing` `dev` tree grep returned no Kovalyov/IOpen files).
  - Zenodo API (`https://zenodo.org/api/records?q=2611.32205`): `0` records.
  - `arxiv_fetch.py abs 2611.32205 --no-cache`: `arXiv:2611.32205v1` (`math.LO`, `2026-11-24`), sole version.
  - `search_web`: returns only `arXiv:2611.32205` itself; Question (1) is open.
