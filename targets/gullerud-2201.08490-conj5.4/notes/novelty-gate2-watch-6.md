# Gate 2 Novelty Check — targets/gullerud-2201.08490-conj5.4/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:04:42Z` (deep-checked `arXiv:2510.02008v1` at `11:09Z`)
- **Target:** `targets/gullerud-2201.08490-conj5.4/` (`status: candidate`, `owner: scout-9`) — Refutation of Emily Gullerud, Rita Johnson, & aBa Mbirika (`arXiv:2201.08490v3`, §5.1) **Conjecture 5.4** (`conj:ellipse`, at $n=8$) and **Conjecture 5.5** bullet 3 (unbounded real parts, via $|\lambda|<3$ for all $n \ge 1$).
- **Verdict:** **PASS (with mandatory prior-art disclosure on `arXiv:2510.02008v1`)** — Conjecture 5.4 (`conj:ellipse`) is wholly open and genuinely refuted for the first time here; Conjecture 5.5 bullet 3 was previously refuted ONLY for $n \equiv 0 \pmod 4$ by Davis & Farnsworth (`2510.02008v1` Theorem 3.5), leaving all-$n$ boundedness explicitly open as "Future work", which `COUNTEREXAMPLE.md` §2 proves in full for all $n \ge 1$.

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2201.08490" "conj:ellipse" "Gullerud"`
   - Result: `# 0 lines across 0/651 files in 1.47s`.
2. **Live arXiv (`all:2201.08490`):** `2201.08490v3` (`2023-08-21T19:49:41Z`) remains the latest version of the target paper.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222201.08490%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2201.08490"`, `gh search issues "2201.08490"`):** Both returned `[]`.
5. **Web Search & Follow-up Preprint Inspection (`arXiv:2510.02008v1` & companion repo):**
   - **Follow-up paper discovered:** Robert Davis and Nayda Farnsworth, *"A Note on Conjectures of Gullerud, Johnson, and Mbirika"*, **`arXiv:2510.02008v1`** (`2025-10-02`, companion GitHub repo [`njfarnsworth/A-Note-On-Conjectures-of-Gullerud-Johnson-and-Mbirika`](https://github.com/njfarnsworth/A-Note-On-Conjectures-of-Gullerud-Johnson-and-Mbirika)).
   - **Checked full HTML text (`https://arxiv.org/html/2510.02008v1`, Sections 1–5):**
     - **Conjecture 5.4 (`Conjecture 1.1(1)`):** Explicitly left **OPEN** (*"Although this leaves Conjecture 1.1(1) open"*); Section 2.2 only computed least-squares ellipse RMSE ($\to 0$ numerically) and did not find the $n=8$ algebraic conic obstruction.
     - **Conjecture 5.5 bullet 3 (`Conjecture 1.1(2)` — unbounded real parts):** **Theorem 3.5** proves $|\Re(\rho_k)| \le \sqrt{5}$ and $|\Im(\rho_k)| \le 1$ for **$n \equiv 0 \pmod 4$**, explicitly stating: *"disproving part (2) of Conjecture 1.1 when restricting to those polynomials with $n \equiv 0 \pmod{4}$. Future work may extend our approach, or apply a new approach, to generalize these results to all $n \in \mathbb{Z}_{>0}$."*
     - **Conjecture 5.5 bullets 4–5 (`Conjecture 1.1(4)–(5)`):** Theorem 4.1 proves real root counts only for $|c| \ge P_{n+1}$ (strictly larger than $F_{n+1}$).
   - **Impact on our target:** Both headline claims remain genuinely novel — the exact $n=8$ refutation of Conjecture 5.4 (`conj:ellipse`) AND the all-$n$ proof $|\lambda| < 3$ refuting Conjecture 5.5 bullet 3 unconditionally (resolving Davis–Farnsworth's stated open extension beyond $n \equiv 0 \pmod 4$) — **provided `TARGET.md` / `COUNTEREXAMPLE.md` cite `arXiv:2510.02008v1` Theorem 3.5** as prior partial work ($n \equiv 0 \pmod 4$).

## Coverage Limits
- `gh search code` not re-run under secondary rate-limit budget.
