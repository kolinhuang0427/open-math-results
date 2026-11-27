# Audit Helper Report: `targets/cooper-2302.00757-conj11.2/`

**Prepared for:** `@audit-2`  
**Prepared by:** `cooper-audit-hlp`  
**Date (UTC):** 2026-11-27 01:38 UTC  
**Isolation compliance:** Did not read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or author scratch notes (`notes/check_*.py`); did not edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source, Published-Version & OEIS Verification

### 1.1 Target folder status
- Files in `targets/cooper-2302.00757-conj11.2/`: `PROOF.md`, `TARGET.md`, `verify.py`, `notes/` (`check-check-1.md`, `check-check-1.py`, `check_gf.py`, `check_qx.py`, `check_sturm5.py`, `check_sturm_both.py`, `check_t11.py`, `novelty-gate2-watch-1.md`, `novelty-gate2-watch-2.md`, `novelty-gate2-watch-5.md`).
- **Confirmed:** No `CONTESTED.md` is present.

### 1.2 arXiv metadata (`tools/arxiv_fetch.py query --id-list 2302.00757,2312.07134`)
- **`arXiv:2302.00757v2`**: Shaun Cooper, *"Apéry-like sequences defined by four-term recurrence relations"*, published `2023-02-01T21:03:06Z`, updated `2024-05-08T00:29:10Z` (`math.NT`). `comment: ""`, `journal_ref: ""`, `doi: ""` on arXiv metadata.
- **`arXiv:2312.07134v2`**: Brendan Alinquant and Robert Osburn, *"On sporadic sequences"*, published `2023-12-12T10:13:08Z`, updated `2024-05-10T09:11:57Z`, published in *Monatshefte für Mathematik* **205** (2024), no. 2, 217–234, DOI `10.1007/s00605-024-01994-8`.
  - In `tools/.arxiv_cache/eprint/2312.07134/main.tex` line 108, Alinquant–Osburn explicitly note: *"Cooper \cite{cooper2} has recently investigated sequences that are solutions to four-term recurrences and exhibit several novel features. For example, some of the sequences take values in $\mathbb{Z}[i]$ or $\mathbb{Z}[\sqrt{2}]$ and appear to satisfy ``rare'' supercongruences \cite[Conjectures 11.1--11.5]{cooper2}."* (cited as still-open computational conjectures).

### 1.3 Published journal version check (`10.1090/conm/818/16373`)
- Crossref API (`https://api.crossref.org/works?query.title=Apery-like+sequences+defined+by+four-term+recurrence+relations`) and Campbell's bibliography (`arXiv:2610.00551`, `seprefe.bib`, `MR4901163`) confirm Cooper's paper was published as:
  - Shaun Cooper, *"Apéry-like sequences defined by four-term recurrence relations"*, in *Classical Hypergeometric Functions and Generalizations*, *Contemporary Mathematics* **818**, Amer. Math. Soc. (2025), pp. 137–179, DOI [`10.1090/conm/818/16373`](https://doi.org/10.1090/conm/818/16373).
- Note that `arXiv:2302.00757v2` (updated 2024-05-08) already contains the referee acknowledgement (line 2763: *"I am grateful to the anonymous referee for suggestions that have improved the presentation of the work."*), matching the post-referee *Contemp. Math.* version. Campbell (`arXiv:2610.00551`, Sep 30, 2026) cites Cooper's 2025 *Contemp. Math.* volume (`\cite{Cooper2025}`) and gives no indication of any proof of Section 11 supercongruences in the print volume. (Caveat: the paywalled AMS PDF itself was not directly opened.)

### 1.4 Exact numbering and recurrence in `tools/.arxiv_cache/eprint/2302.00757/main.tex`
- **Theorem-numbering scheme** (lines 30–46): `\newtheorem{theorem}{Theorem}[section]` with `lemma`, `definition`, `example`, `xca`, `remark`, `openquestion`, and `conjecture` all sharing the `[theorem]` counter.
- **Section 11 environments** (lines 2472–2765): Zero `theorem`/`lemma`/`definition`/`example`/`xca`/`remark`/`openquestion`/`proposition`/`corollary` environments; **exactly 6 `conjecture` environments**:
  1. Line 2537 (`\label{c11}`): **Conjecture 11.1** — $T_{11}(pn) \equiv T_{11}(n) \pmod{p^2}$ for $p \in \{2, 59, 5581\}$, plus mod $2^6$ at $p=2$. (`\label{c11}` is indeed on 11.1, not 11.2.)
  2. Line 2557 (unlabelled): **Conjecture 11.2** — $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod{3^2}$ and $T_{11}(5n) \equiv T_{11}(n) \pmod{5^2} \iff 5 \mid n$. Matches `TARGET.md` and `PROOF.md` verbatim (implicit quantifier: all positive integers $n$, per lines 2539, 2555–2567; trivially holds at $n=0$ since $T_{11}(0)=1$).
  3. Line 2592 (`[Conjecture 5.5 in~\cite{ccs}]`): **Conjecture 11.3** (for $t_{11}(n)$).
  4. Line 2626 (Subsection 11.2): **Conjecture 11.4** (Level 14).
  5. Line 2669 (Subsection 11.3): **Conjecture 11.5** (Level 15).
  6. Line 2735 (Subsection 11.4): **Conjecture 11.6** (Level 24).
- **Theorem 3.1 (`\label{interesting}`) & Tables:**
  - `\label{interesting}` (lines 515–550) is indeed **Theorem 3.1** (the first theorem-class environment in Section 3).
  - Table 1 (`\label{table11}`, line 401/455) and Table 2 (`\label{table1}`, line 681/744) cover levels 1–6 weights 1 and 2; Table 3 (`\label{1to35}`, lines 1092–1314) and Table 4 (`\label{1to35b}`, lines 1316–1530) give the level-11 modular data ($X = (\eta_1\eta_{11}/\theta_{1,1,3})^2$, $Z = \eta_1^2\eta_{11}^2/X = \theta_{1,1,3}^2$, $B^2 = 1-20X+56X^2-44X^3$, $H = 4X(1-8X+11X^2)$, citing `\cite{cooperbook}` = Cooper 2017 and `\cite{ge}` = Cooper–Ge–Ye 2015 *J. Math. Anal. Appl.* 421(2) Thm 4.7); Table 5 (`\label{table5}`, lines 2250–2290) lists level-11 parameters $(a,b,c,d,e) = (10, 4, -56, -8, 22)$.
  - Section 5 (lines 1607–1632) applies Theorem 3.1 (`\ref{interesting}`) to $Z = U_1(q)$ and $X = X_1(q)$ to prove $U_1(q) = \sum_{n=0}^\infty T_{11}(n) X_1(q)^n$ where $T_{11}(n) \in \mathbb{Z}$ satisfies the exact four-term recurrence in `PROOF.md` line 4 (`(n+1)^3 T(n+1) = 2(2n+1)(5n^2+5n+2)T(n) - 8n(7n^2+1)T(n-1) + 22n(2n-1)(n-1)T(n-2)` with $T(0)=1$).

### 1.5 Live OEIS Check (`https://oeis.org/search?q=1,4,28,268,3004,36784&fmt=json`)
- **Exact match:** **OEIS [A284756](https://oeis.org/A284756)** (`revision: 44`, `time: 2026-10-06T00:16:49-04:00`).
- **All comments/links/formulas in A284756:**
  - Comment: `"This sequence is c_11 in the 2015 paper of Cooper et al."`
  - Links:
    1. Seiichi Manyama, `b284756.txt` ($n=0..819$).
    2. **John M. Campbell**, `arXiv:2610.00551` (*"On a problem on Ramanujan-Sato series of level 11"*, 2026, p. 2).
    3. **Xavier Caruso, Florian Fürnsinn, Daniel Vargas-Montoya, and Wadim Zudilin**, `arXiv:2510.23298` (*"Galois Groups of Apéry-like Series Modulo Primes"*, 2025, Table 1, p. 10).
    4. Shaun Cooper, Askey 80 talk slides (2013).
    5. Cooper, Ge, Ye, *J. Math. Anal. Appl.* 421(2) (2015), 1358–1376.
  - **No mod-9, mod-25, or supercongruence proofs or references** appear anywhere in A284756.

---

## 2. Deep Novelty / Prior-Art Search (Feb 2023 – Nov 27, 2026)

### 2.1 Snapshot grep (`tools/novelty_grep.py 2302.00757 Cooper "T_{11}" "T_11" "36784"`)
- Returned 58 lines across 29/367 files (1.80s).
- Zero hits in `1337-solved-conjectures`, `openai-math`, `ai-collections`, `formal`, or `arxiv` for Cooper's level-11 sequence (`T_{11}` hits in `techno-optimist` are Erdős #131; `Cooper` in `1337` is Cooper–Hollars Erdős #611; `T_{11}` in `the-omega-institute/trureturing` `Library/Fourier/liu2026quasirhdual.md` is an unrelated matrix entry $V(t_{11})$).
- **Two important discovered-repo hits inspected in full via `gh api`:**
  1. **`rbajaj5/a183068-supercongruence`** (`related-results/CooperLevel11RarePrimes.md`, dated `2026-07-26`, and `verification/related/verify_cooper_level11.py`, `RESULT_INDEX.md` item `C11`):
     - Explicitly cites Cooper's Conjectures 11.1 and 11.2 and Beukers–Tsai–Ye (`arXiv:2408.16616`, which proves only the mod-$p$ Lucas congruences).
     - Notes that a conjectural first-order Frobenius law $D_p(n) \equiv n T(n-1) q_p \pmod p$ (tested on 8,300 pairs) *would* imply both parts of Cooper's Conjecture 11.2, and notes a conjectural 3-branch mod-9 recursion (tested through $n \le 10{,}000$), **explicitly stating both remain UNPROVED "computational theorem targets"** ("Existing proved Lucas foundation plus reproducible computational theorem targets. The rank-one Cartier lift and the three-branch [recursion remain unproved]").
  2. **`eliottcassidy2000/math`** (`05-knowledge/results/cooper_s7_weight_one_root_frobenius_20261018.md` and `session53_g27_collatz_cooper_20261024/...`):
     - Addresses Cooper's **level-7** weight-one root sequence $c(n)$ (`s7`, OEIS A279619), plus $s_{10}, s_{18}$, NOT $T_{11}$. Explicitly lists Chan–Cooper–Sica Conjecture 5.5 (level 11) as **OPEN** and has no proof of Cooper `2302.00757` Section 11.2.

### 2.2 arXiv, Zenodo, Crossref, and Web Searches
- **`tools/arxiv_fetch.py query` results:**
  - `2610.00551v1` (John M. Campbell, Sep 30, 2026, *"On a problem on Ramanujan-Sato series of level 11"*, inspected in full from `tools/.arxiv_cache/eprint/2610.00551.src` -> `ElevenV89.tex`): proves a double binomial sum formula for $c_{11}(n) = T_{11}(n)$. Does **not** study or prove mod-9, mod-25, or any supercongruences for $T_{11}(n)$.
  - `2510.23298v1` (Caruso, Fürnsinn, Vargas-Montoya, Zudilin, Oct 27, 2025 / *Bull. Aust. Math. Soc.* 114 (2026) 65–78, `apery.tex`): studies Galois groups of reductions **modulo $p$** (not $p^2$) of Apéry-like series; cites A284756 in Table 2 (p. 10) for mod-$p$ splitting of $A_p(t)$. No mod-9/mod-25 supercongruences.
  - `2408.16616v2` (Beukers, Tsai, Ye, Aug/Oct 2024, *Bull. LMS* 57 (2025), *"Lucas congruences using modular forms"*): proves Cooper's **mod-$p$ Lucas congruence** for $T_{11}(n)$ (Theorem 1.1/1.2), NOT mod-$p^2$ supercongruences.
  - `2403.03301v3` (Beukers, Mar 2024 / Jun 2025, *Alg. Number Th.* 20 (2026) 1727–1768, *"Supercongruences using modular forms"*, `SupercongruencesRevise.tex`): covers Cooper's $s_7, s_{10}, s_{18}$ (three-term recurrences) and makes no mention of level-11 $T_{11}(n)$ or `2302.00757`.
  - Targeted arXiv queries (`all:"2302.00757"`, `au:Cooper AND all:congruence`, `all:"level 11" AND all:"supercongruence"`, `all:"four-term" AND all:"Lucas"`, `all:"36784" OR all:"3004"`, `(au:Beukers AND au:Vlasenko) OR (au:Rowland AND au:Yassawi) OR (au:Malik AND au:Straub)`, `(au:Zudilin AND all:"level 11") OR (au:Guo AND all:"four-term" AND all:congruence)`): 0 hits settling Cooper's mod-9 or mod-25 congruences.
- **Crossref API & Zenodo API:** Crossref returned only Cooper's own *Contemp. Math.* 818 (2025) publication (`10.1090/conm/818/16373`); Zenodo returned `0` hits for `2302.00757` and no relevant hits for `"Shaun Cooper four-term"` or `"36784 3004"`.
- **`search_web`:** Queries for `"2302.00757"`, `"T_{11}(3n)"`, `"T_{11}(5n)"`, `"Shaun Cooper" "supercongruence" "level 11"`, `"A284756" ("mod 9" OR "mod 25" OR "supercongruence" OR "Conjecture 11.2")`, and `"Conjecture 11.2" "Cooper"` surfaced only Cooper's paper, A284756, and general Apéry/level-11 references — **0 proofs or settlements** of Cooper's Conjecture 11.2.

### 2.3 Competing GitHub Repositories & Global GitHub Search
- **Local snapshots checked:** `watch/snapshots/1337-solved-conjectures/` (all `.md`/`.jsonl`/`.txt`), `watch/snapshots/openai-math/`, `the-omega-institute__trureturing*.json`, `aliromman__math.json`, `KnowledgeSense__math.json`, `rainwangphy__aftd-platform.json`, `valyuAI__research.json`, `facebookresearch__atlas-lean.json` -> **0 matches** for `2302.00757`, `A284756`, `36784`, or `T_{11}` level-11 congruences.
- **Live `gh search code` & `gh search issues`:**
  - Global `gh search code` for `"2302.00757"`, `"T_11" "3n"`, `"Shaun Cooper" "5581"`, `"36784" "3004"`, `"A284756"`: all returned `[]` (0 hits).
  - Scoped `gh search code` across `the-omega-institute/trureturing`, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `openai/math` for `"Shaun Cooper"`, `Cooper supercongruence`, and `T_{11}`: `[]` for the first two; `T_{11}` returned only tensor/matrix notations in `openai/math` and `Library/Fourier/liu2026quasirhdual.md` (verified $V(t_{11})$ via `gh api`).
  - Global `gh search issues` for `"2302.00757"` and `"A284756"` returned `[]`; `"Shaun Cooper"` returned only an unrelated `trureturing` issue (`#25990`, A258655).

**Novelty conclusion for Cooper Conjecture 11.2:** Clean as of 2026-11-27 01:38 UTC across arXiv, OEIS A284756, Crossref, Zenodo, web search, and all watched/searched GitHub repositories (with `rbajaj5/a183068-supercongruence` explicitly noting Conjecture 11.2 remains unproved there).

### 2.4 Bonus Gate 3 check for `@audit-2`: `gaetz-2512.08168-conj1/`
- Checked `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, and `the-omega-institute/trureturing-mdbook` (plus `trureturing-tools` snapshot and global `gh search issues` for `"2512.08168"`):
  - `gh search code` for `"2512.08168"` and `Billey Postnikov` across all 4 repos: **`[]` (0 hits)**.
  - `gh search code` for `Gaetz` across all 4 repos: **2 hits in `facebookresearch/atlas-lean` only**, both on **weak order Sperner property** (`MathlibExt/Combinatorics/WeakOrderSpernerAMR30Problem0039.lean` and `blueprint/roadmap/.../weak-order-sperner-holds.md`), unrelated to `2512.08168` / Billey–Postnikov.
  - Note from local snapshots: `the-omega-institute__trureturing-tools.json` (`tools/scripts/agent/openproblem/SCREENED-OUT-R52.md`) records only `"arXiv:2512.08168 Conjecture 1.9 由同文 Theorem 6.2 首个反例"` (Conjecture 1.9, not Conjecture 1). `gh search issues` for `"2512.08168"` hit only `the-omega-institute/trureturing#7333` (a generic standing search-lane issue).

---

## 3. Independent Exact Computation & Symbolic Algebra Verification

### 3.1 Execution of `notes/check-check-1.py`
Command: `time .venv/bin/python targets/cooper-2302.00757-conj11.2/notes/check-check-1.py`  
Exit code: **`0`** | Runtime: **`0.686s` wall (`0.62s user`, `0.03s sys`)**  
Exact raw output:
```text
T11 recurrence, Cooper first 11 terms, & direct checks (0<=n<=1000): OK
q-series U1, V1, E_{2,11} identity, & Z(X1)==U1 mod 9, 25: OK
Gamma_0(33) G3 == 0 mod 9 up to q^130 (Sturm 120) & Step 2.4: OK
Gamma_0(55) G_{5,luc} == 0 mod 5 up to q^80 (Sturm 60) & G5 == 0 mod 25 up to q^405 (Sturm 396): OK
PASS
```

### 3.2 Independent SymPy Symbolic Algebra Verification (`PROOF.md` Steps 2.3, 2.4, and 3.3)
Ran an inline SymPy verification in `.venv/bin/python` over exact rational/polynomial rings $\mathbb{Z}[U_1, V_1, U_p, V_p]$ and finite fields:
1. **Step 2.3 ($p=3$):**
   - Verified $\widetilde{N}_3(U_1, V_1) = U_1^6 N_3(V_1/U_1)$ identically.
   - Verified every monomial of $G_3$ (`PROOF.md` line 58) has total degree $15$ in $(U_1, V_1, U_3, V_3)$, i.e. **exact uniform modular weight $2 \cdot 15 = 30$** (`degs_G3 == {15}` -> weights `{30}`).
   - Verified $G_3 / D_3$ (`PROOF.md` lines 58 and 56) equals the Step 2.3 rational expression (line 54 with the $(U_1 - V_1)$ weight-2 factor inserted on the two mod-3-divisible terms $\frac{X_1^3 - X_3}{(1-X_3)^2}$ and $3 \frac{N_3(X_1)}{(1-X_1^3)^2}$) identically (`simplify(G3/D3 - lhs_54) == 0`). Since $U_1 - V_1 \equiv 1 \pmod{3\mathbb{Z}[[q]]}$ (Step 2.1) and both terms are divisible by $3$ in $\mathbb{Z}[[q]]$, multiplying them by $(U_1 - V_1)$ preserves exact congruence modulo $9\mathbb{Z}[[q]]$.
   - Verified Step 2.4 identity in $\mathbb{F}_3[X]$: $(1-X)(X^3 - X^5 + X(1-X^3)) \equiv X + 2X^2 + X^3 + X^4 + X^6 \pmod 3$ (`True`).
2. **Step 3.3 ($p=5$):**
   - Verified $P_5'(X) = 4 + 6X + 9X^2 + 16X^3 \equiv 4 + X + 4X^2 + X^3 \pmod 5$ in $\mathbb{F}_5[X]$ (`True`). Because $X_1(q)^5 - X_5(q) = 5\Delta_5(q)$ has a prefactor of $5$ (and $P_5(X_5)$ is a unit in $\mathbb{Z}[[q]]$), replacing $P_5'(X_5)$ by its mod-5 reduction $4 + X_5 + 4X_5^2 + X_5^3$ (homogenized as $\widetilde{P}_5'(U_5, V_5)$) inside the $5\Delta_5$ term is strictly valid modulo $25\mathbb{Z}[[q]]$.
   - Verified every monomial of $G_5$ (`PROOF.md` line 94) has total degree $33$ in $(U_1, V_1, U_5, V_5)$, i.e. **exact uniform modular weight $2 \cdot 33 = 66$**, while $D_5 = U_1^{24} U_5^4 \widetilde{P}_5(U_5, V_5)$ has total degree $32$ (weight $64$).
   - Verified $G_5 / D_5$ equals Step 3.3's expression (with $P_5'$ reduced mod 5 as $\widetilde{P}_5'(U_5,V_5)/U_5^3$) identically (`simplify(G5/D5 - rhs_96) == 0`).
