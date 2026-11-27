---
source: "arXiv:2411.00721v2 (haugland-omland-reversible-v2.tex, Section 2 Question line 327 / Section 4 Open Problem (iii) line 455)"
status: reported
owner: attack-1
updated: 2026-11-27T08:05:48Z
identifiers:
  - "arXiv:2411.00721v2"
  - "Haugland-Omland-2026-Deg2ProperLifting"
---

# Haugland–Omland Question 2 / Open Problem (iii): Existence of Proper Liftings of Algebraic Degree 2

## Statement (Verbatim from `arXiv:2411.00721v2`, `haugland-omland-reversible-v2.tex`)

Context (lines 89–95):
> A Boolean function $f\colon\F_2^k\to\F_2$ induces a function $F\colon\F_2^n\to\F_2^n$ for every $n\geq k$, by
> \[
> F(x_1,x_2,\dotsc,x_n)=\big(f(x_1,x_2,\dotsc,x_k),f(x_2,x_3,\dotsc,x_{k+1}), \dotsc,f(x_n,x_1,\dotsc,x_{k-1})\big),
> \]
> which is shift-invariant (or rotation-symmetric), that is, commutes with the right shift operator. ... If $f$ has diameter~$k$, i.e., depends on both $x_1$ and $x_k$, and $F$ is bijective, we say that $f$ is a $(k,n)$-lifting. If $f$ is a $(k,n)$-lifting for every $n\geq k$, then $f$ is called a \emph{proper lifting} (see~\cite{HO-1}).

Question (Section 2, lines 327–331):
> Does there exist a proper lifting of degree~$2$? We have checked that there are none of diameter~$\leq 7$, and that no composition of two proper liftings of degree~$\leq 6$ gives a degree~$2$ function. Moreover, by Proposition~\ref{shift-product}, every primitive landscape function has degree at least $3$.

Open Problem (iii) (Section 4, line 455):
> Do proper liftings of algebraic degree~$2$ exist, or more generally, what is the minimal possible degree as a function of diameter?

## Gate 1 Novelty Receipt

Checked `2026-11-27T04:48:00Z` (start UTC `2026-11-27T04:48Z`):
- `tools/novelty_grep.py 2411.00721 Haugland Omland "proper lifting"` across 470 snapshot files: 0 matches to this paper (matches are Haugland 1996/2016 Erdős #36 minimum overlap).
- arXiv (`2411.00721v2`, updated `2026-11-01`), Zenodo (`0` hits for `2411.00721`), `search_web`: no resolution found.
- Competing GitHub repos (`trureturing`, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `Wangwy-sjtu/lean-conjecture-proofs`, `facebookresearch/atlas-lean`, `rainwangphy/aftd-platform`, `valyuAI/research`): 0 matches in git trees.
