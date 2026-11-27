# Target: hartwig-2611.23687-conj1.4

- source: https://arxiv.org/abs/2611.23687v1 (Section 1, Conjecture 1.4 / `\label{conj_denominator_N-truncated}`, Jonas T. Hartwig & Sagar Shrivastava, *Extremal Projectors and the Virasoro Algebra*, 2026-11-18)
- status: reported
- owner: scout2-6
- updated: 2026-11-27T09:38:00Z
- start_utc: 2026-11-27T09:27:34Z
- identifiers: arXiv:2611.23687, arXiv:2611.23687v1, conj_denominator_N-truncated, Virasoro-Extremal-Projector

## Statement (verbatim from `main.tex`, lines 147–169)

Define $K_n \in \mathbb{Z}[L_0, c]$ by
$$K_n(L_0,c) = c_n\prod_{\substack{r,s\ge 1\\ rs=n}} \varphi_{r,s}(L_0,c),$$
where $c_n$ is chosen so that $K_n \in \mathbb{Z}[L_0,c]$ is primitive with positive leading coefficient in $L_0$, $\tau_n$ is the automorphism of $\mathbb{C}(L_0,c)$ given by $\tau_n(L_0)=L_0+n$ and $\tau_n(c)=c$, and
$$\varphi_{r,s}(L_0,c) = L_0 - \frac{(13-c)(r^2+s^2)-24rs+2(c-1)+(r^2-s^2)\sqrt{(c-1)(c-25)}}{48}.$$
Here $P_N = \sum_{n=0}^N P[n]$ is the $N$-truncation of the Virasoro extremal projector $P = \sum_{n\ge 0} P[n]$, $P[n] = \sum_{\lambda,\mu \vdash n} b_{\lambda,\mu}(L_0,c) L_\lambda^\dagger L_\mu$ ($b_{\lambda,\mu} \in \mathbb{C}(L_0,c)$). Saying a polynomial $Q(L_0,c)$ *regularizes* $P_N$ means $Q(L_0,c) P_N \in U(\mathrm{Vir})$ (as in Theorem 1.3, where $D_N' = \prod_{1\le m\le n\le N} \tau_{-n}(K_m)$ regularizes $P_N$).

> **Conjecture 1.4** (`\label{conj_denominator_N-truncated}`). Define the $N^{th}$ denominator $D_N$ as
> $$D_N = \prod_{1\le n\le N} \tau_{-n}(K_n).$$
> Then $D_N$ is the least degree polynomial in $L_0,c$ which regularizes the N-truncated extremal projector of the Virasoro algebra.

(The authors verified Conjecture 1.4 symbolically for $N=1,2,3,4,5,6$ via SymPy.)

## Gate 1 Novelty Receipt

- Checked at: `2026-11-27T09:27:04Z`
- `ls targets/ | grep -iE "hartwig|shrivastava|2611\.23687|virasoro"`: 0 matches.
- `.venv/bin/python tools/novelty_grep.py "2611.23687" "Hartwig" "Shrivastava" "Virasoro extremal"`: matched only `watch/snapshots/arxiv/` submission index entries for `2611.23687v1`.
- `gh search issues "2611.23687"`: 0 matches.
- `gh search repos "Virasoro-Extremal-Projector"`: matched only the authors' companion code repo `sagarsmaths-afk/Virasoro-Extremal-Projector` (README confirms exact symbolic check only up to $N=6$, matching paper).
- Web search (`search_web` for `"2611.23687" OR ("Extremal Projectors and the Virasoro Algebra" "Hartwig")`): only indexes `2611.23687v1` itself; no later resolution found.
- Coverage note: `gh search code` was in secondary rate limit cooldown (`~690s` from `09:26Z`).
