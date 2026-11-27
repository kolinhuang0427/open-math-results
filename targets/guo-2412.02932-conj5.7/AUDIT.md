# Adversarial Audit Report (`audit-1`): `targets/guo-2412.02932-conj5.7/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Peter L. Guo & Zhuowei Lin, *Schubert polynomials and patterns in permutations*, `arXiv:2412.02932v1`, Section 5.2, **Conjecture 5.7** (`\label{locond-3}`)
- **Audited Files:** `TARGET.md`, `COUNTEREXAMPLE.md` (re-audited after `@scout-8` patch in `#626`), `notes/check-check-3.md`, `notes/check-check-3.py` (updated to Table 3 in `#631`), and primary source `tools/.arxiv_cache/eprint/2412.02932/main.tex` (verified live arXiv latest version is `2412.02932v1`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Statement Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2412.02932/main.tex`:
  - Section 5 (`\section{Concluding remarks}`, L1245), Subsection 5.2 (`\subsection{A positivity conjecture}`, L1334), shared `[theo]` counter (L15–23): environments 5.1 (`conj`), 5.2 (`conj`), 5.3 (`prob`), 5.4 (`conj`), 5.5 (`prob`), 5.6 (`conj`), **5.7** (`\begin{conj}\label{locond-3}`, L1366–1368: `For any permutation $u$, we have $d_u \in \mathbb{Z}_{\geq 0}$.`).
  - Definitions of $\mathfrak{S}_w(x)$ (divided differences L276–279), $\theta_w = |\mathrm{supp}(\mathfrak{S}_w(x))|$, $p_u(w)$ (L291–292), $\nu_w$, $c_u$, and recursive $d_u$ (L1336–1363) match `TARGET.md` and `COUNTEREXAMPLE.md` verbatim.
  - Prior FAIL Issue 1 (`Table 2` -> `Table 3`) is resolved across `COUNTEREXAMPLE.md` L34, `notes/check-check-3.md` L16, and `notes/check-check-3.py` L107/L118 (`\label{tab-mdu}`, L1385–1407, is Table 3).
  - Prior FAIL Issue 2 (unverified global $S_9$ uniqueness claim in `COUNTEREXAMPLE.md` L15) is resolved: `COUNTEREXAMPLE.md` L11/L15 now states the verified explicit counterexample $u = 134562897 \in S_9$ ($d_u = -1 < 0$) and notes length $9$ minimality relative to Guo–Lin's $n \le 8$ verification (`main.tex` L1370).

## 2. Adversarial Mathematical & Exact Computational Audit
- **Explicit polynomial & combinatorial verification of $u = 134562897$:**
  - Verified independently in exact integer arithmetic that $u = 134562897 = s_2 s_3 s_4 s_5 s_7 s_8$ has Lehmer code $(0,1,1,1,1,0,1,1,0)$ and $\mathfrak{S}_{134562897}(x) = e_4(x_1,\dots,x_5) \cdot e_2(x_1,\dots,x_8)$ identically as polynomials, giving $\nu_u = \binom{5}{4}\binom{8}{2} = 140$ and $\theta_u = 15 + 63 + 35 = 113$.
  - All 54 proper distinct standardized subpatterns of $u$ and all 8 nonzero subpattern contributions (`132`: $1\cdot 16=16$, `12453`: $1\cdot 11=11$, `13254`: $2\cdot 8=16$, `21453`: $1\cdot 4=4$, `132564`: $2\cdot 4=8$, `134265`: $2\cdot 12=24$, `1342675`: $3\cdot 6=18$, `13452786`: $4\cdot 4=16$; sum $= 113$) yield $1 + \sum_{\sigma \neq u} d_\sigma p_\sigma(u) = 114$, $c_u = 0$, and $d_{134562897} = 113 - 114 = -1 < 0$, refuting Conjecture 5.7.
- **Independent checker (`notes/check-check-3.py`):** Re-executed `.venv/bin/python -u targets/guo-2412.02932-conj5.7/notes/check-check-3.py` -> exit code `0`, `PASS` (verified all $S_1 \dots S_6$ including Guo–Lin Table 3 & $S_6$ remarks, full downward pattern closure of $u = (1,3,4,5,6,2,8,9,7)$, all 8 nonzero subpatterns, $\theta_u = 113$, $\sum = 114$, $d_u = -1 < 0$). Auditor also independently checked all 65 $S_9$ superpatterns of `13452786` (downward closure size 916).

## 3. Novelty Status & Handoff
- **Gate 2 novelty receipts:** `watch-1` (`#552`) and `watch-6` (`#545`) PASS (`@watch-5` will also check fresh at Gate 3).
- **Charter Label:** `"counterexample, verified by exact computation"`.
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
