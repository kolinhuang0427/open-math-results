# Check Report: `targets/say-2611.32633-bqtisp-sublog/`

- **Verdict:** **PASS**
- **Primary Source:** `arXiv:2611.32633v1` (`main.tex` Section 5 `\section{Concluding remarks}` L1912–1928; Section 2 `thm:remscrimQTMtradeoff` L1100–1105; Section 4 `thm:hier` & `lem:dtm` L1556–1765)
- **Gate 2 Receipts:** `watch-1` (`#2037`), `watch-6` (`#2038`), `watch-5` (`#2040`) — all PASS (`notes/novelty-gate2-watch-{1,5,6}.md`).

## Checks Performed

1. **Primary-source alignment:** Confirmed `TARGET.md` L3 & L12 and `PROOF.md` L5 cite Section 5 (`Concluding remarks`, `main.tex` L1912–1928), and `TARGET.md` L14–18 reproduces the Section 5 open question and `thm:hier` verbatim.
2. **Proof review (`PROOF.md`):** Verified Lemma 1 ($O(\log\log N_k)$-space bit-length approximation $\tilde{r}_k$), Lemma 2 ($O(s(n))$-space / $n^{O(1)}$-time DTM upper bound), Lemma 3 (Remscrim nonregularity lower bound via monotonicity and $3$-step doubling smoothness $s(n) \le C^3 l_k$), and Theorem 1 ($i \ge 1$ special case noted at L16).
3. **Independent exact-integer verifier (`notes/check-check-1.py`):**

```text
$ .venv/bin/python -u targets/say-2611.32633-bqtisp-sublog/notes/check-check-1.py
LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True
FAMILY_sqrt_log: PASS
FAMILY_three_quarter_log: PASS
FAMILY_log_div_loglog: PASS
FAMILY_loglog_mul_logloglog: PASS
PASS
EXIT:0
AST_FLOATS: []
FLOAT_CALLS: []
```
