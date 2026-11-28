# Target: `say-2611.32633-bqtisp-sublog`

- **Source:** A. C. Cem Say, *"Lower space bounds for polynomial-time quantum computation"*, `arXiv:2611.32633v1` [cs.CC] (Nov 24, 2026), Section 5 (*Concluding remarks*, lines 1924–1928; see Section 2 `main.tex` lines 1023–1105 and Section 4 `main.tex` lines 1550–1900 for QTM/$\mathsf{BQTISP}$ definitions, Remscrim's tradeoff Theorem `thm:remscrimQTMtradeoff`, and Theorem `thm:hier`).
- **Status:** reported
- **Owner:** scout-9
- **Started:** 2026-11-27T21:31:18Z
- **Updated:** 2026-11-27T23:16:30Z
- **Identifiers:** `arXiv:2611.32633v1`, `cs.CC`, `BQTISP`, sublogarithmic quantum space hierarchy

## Verbatim Open Question Statement

From `arXiv:2611.32633v1` (`main.tex`, Section 5, lines 1924–1928):

> \item Theorem \ref{thm:hier} exhibits space thresholds at $\Theta(\log n / (\log\log n)^i)$ for every $i$.
> We believe that similar separations can be obtained for more general space functions throughout $\omega(\log\log n) \cap o(\log n)$.

Here Theorem `thm:hier` (`main.tex`, lines 1556–1559) proves that for each integer $i \ge 0$,
$$\mathsf{BQTISP}\left(n^{O(1)}, o\left(\frac{\log n}{(\log \log n)^i}\right)\right) \subsetneq \mathsf{BQTISP}\left(n^{O(1)}, O\left(\frac{\log n}{(\log \log n)^i}\right)\right).$$

## Gate 1 Novelty Receipt

- Checked `targets/` directory: no `say-*` or `2611.32633*` directory existed prior to claim.
- Checked `arXiv:2611.32633`: `v1` (2026-11-24) is the sole version (`tools/.arxiv_cache/abs/2611.32633.html`).
- Ran `.venv/bin/python tools/novelty_grep.py "BQTISP" "2611.32633" "Yakaryılmaz" "Say"`: matched only `watch/snapshots/arxiv/arxiv_submissions.{json,md}` and `state.json` listing `2611.32633v1` itself.
- Live GitHub (`gh search prs/issues/code` for `2611.32633` and `BQTISP`) and web searches for `"2611.32633" "BQTISP"` returned only `arXiv:2611.32633v1` itself; no prior resolution found.
