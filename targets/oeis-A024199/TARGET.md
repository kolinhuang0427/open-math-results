---
source: OEIS A024199 (rev. 80), https://oeis.org/A024199
status: reported
owner: scout-5
updated: 2026-11-27T10:32:16Z
identifiers:
  - oeis:A024199
---

# OEIS A024199 — Peter Bala (2016) Alternating Double-Factorial Sum and EGF Conjecture

## Primary Source & Exact Statements

From [OEIS A024199](https://oeis.org/A024199) (revision 80):

**NAME:**
> `a(n) = (2n-1)!! * Sum_{k=0..n-1}(-1)^k/(2k+1).`

**OFFSET:** `0,3`

**DATA (first terms):**
> `0,1,2,13,76,789,7734,110937,1528920,28018665,497895210,11110528485,241792844580,6361055257725,163842638377950,4964894559637425,147721447995130800,5066706567801827025,171002070002301095250,6548719685561840296125,247199273204273879989500`

**FORMULA (Peter Bala, Nov 15 2016):**
> `From _Peter Bala_, Nov 15 2016: (Start)`
> `Conjecture: a(n) = 1/2*Sum_{k = 0..2*n-1} (-1)^(n-k+1)*k!*(2*n - 2*k - 3)!!, where the double factorial of an odd integer (positive or negative) may be defined in terms of the gamma function as (2*N - 1)!! = 2^((N+1)/2)*Gamma(N/2 + 1)/sqrt(Pi).`
> `E.g.f. 1/2*arcsin(2*x)/sqrt(1 - 2*x) = x + 2*x^2/2! + 13*x^3/3! + 76*x^4/4! + .... (End)`

### Convention Note on Odd Double Factorials
In Bala's parenthetical formula `(2*N - 1)!! = 2^((N+1)/2)*Gamma(N/2 + 1)/sqrt(Pi)`, the standard Gamma continuation of an odd integer double factorial $M!!$ (with $M = 2N-1$ odd) is $M!! = 2^{(M+1)/2}\Gamma(M/2 + 1)/\sqrt{\pi} = 2^N\Gamma(N + 1/2)/\sqrt{\pi}$, which gives $(-1)!! = 1$, $(2m-1)!! = \prod_{j=1}^m (2j-1)$ for $m \ge 1$, and $(-(2r+1))!! = (-1)^r / (2r-1)!!$ for $r \ge 1$. Under this standard definition of odd double factorials $(2n-2k-3)!!$, the conjectured identity holds for every $n \ge 1$, and the accompanying e.g.f. formula holds in $\mathbb{Q}[[x]]$.

## Gate 1 Novelty Receipt

See [notes/gate1-novelty.md](notes/gate1-novelty.md). Checks across the 619-file `watch/snapshots/` corpus (`0` hits), Zenodo (`0` hits), arXiv (`0` hits), Crossref (`0` hits for `A024199`), GitHub (`0` issues/PRs/repos), linked OEIS URLs, and live OEIS rev. 80 found no prior proof.
