# Open Math — Verified Results

This repository contains verified mathematical results and verification artifacts (exact-arithmetic Python verifiers, independent audit and novelty reports, and Lean 4 formalizations).

> **Note:** Internal auditing, exact computation, and formalization of primary-source definitions do not constitute external peer review. See [`RESULTS.md`](RESULTS.md) and each target's `AUDIT.md` for scope and caveats.

## Summary of Results

| # | Target | Conjecture | Result | Independent Python Verifier | Lean 4 Formalization |
|---|---|---|---|---|---|
| 1 | [`ferrero-2511.16335-conj1.8`](targets/ferrero-2511.16335-conj1.8/COUNTEREXAMPLE.md) | Ferrero–Hall–Hogben–Hunnell–Small Conjecture 1.8 (`arXiv:2511.16335v1`, AJC 96(2) 2026) | **False** (`Lean-checked`): $C_6[2K_1] \cong \mathrm{Circ}(12,\{1,5\})$ and infinite blowup family $C_6[r_0 K_1,\dots,r_5 K_1]$ ($r_i \ge 2$) | [`check-check-2.py`](targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py) (stdlib) | [`Ferrero251116335Conj18.lean`](lean/OpenMath/Ferrero251116335Conj18.lean) |
| 2 | [`wei-2310.17337-conj1.5`](targets/wei-2310.17337-conj1.5/COUNTEREXAMPLE.md) | Wei–Zhang–Zhao Conjecture 1.5 (`arXiv:2310.17337v1`) | **False** (`Lean-checked`): truncated tetrahedron at $k = 8$ ($\iota(G, C_8) = 2 > 19/10$), plus $GP(9,2)$ and $GP(11,2)$ | [`check-check-1.py`](targets/wei-2310.17337-conj1.5/notes/check-check-1.py) (stdlib) | [`Wei231017337Conj15.lean`](lean/OpenMath/Wei231017337Conj15.lean) |
| 3 | [`oeis-A100691`](targets/oeis-A100691/PROOF.md) | Mathar's 2022 conjecture linking OEIS `A100691` and `A193641` | **Resolved** (`Lean-checked`): proved stored recurrence ($n \ge 1$), disproved triangular-strip SAW reading for all $n \ge 5$ ($s(5)=160 \ne 158$) | [`check-check-3.py`](targets/oeis-A100691/notes/check-check-3.py) (`sympy`) | [`OeisA100691.lean`](lean/OpenMath/OeisA100691.lean) |
| 4 | [`dris-2202.08116-conj5.1`](targets/dris-2202.08116-conj5.1/PROOF.md) | Dris Conjecture 5.1 (`arXiv:2202.08116v1`, *Octogon Math. Mag.* 2022) | **Proved** (`Lean-checked`): asymptotic density of $\{m \ge 1 : \gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))\}$ is $0$ | [`check-check-2.py`](targets/dris-2202.08116-conj5.1/notes/check-check-2.py) (stdlib) | [`Dris220208116Conj51.lean`](lean/OpenMath/Dris220208116Conj51.lean) |
| 5 | [`oeis-A250917`](targets/oeis-A250917/PROOF.md) | Mathar's 2020 D-finite recurrence for OEIS `A250917` | **Proved** (`written proof, internally audited`): order-5 polynomial recurrence holds for all $n \ge 5$ (and $n=3,4$) | [`check-check-2.py`](targets/oeis-A250917/notes/check-check-2.py) (`sympy`) | — |
| 6 | [`oeis-A108430`](targets/oeis-A108430/PROOF.md) | Mathar's 2022 D-finite recurrence for OEIS `A108430` | **Proved** (`written proof, internally audited`): order-3 polynomial recurrence holds for all $n \ge 3$ | [`check-check-1.py`](targets/oeis-A108430/notes/check-check-1.py) (`sympy`) | — |
| 7 | [`linusson-2512.24346-conj1`](targets/linusson-2512.24346-conj1/PROOF.md) | Linusson–Özdemir Conjecture 1 (`arXiv:2512.24346v1`, `conj:complement`) | **Proved** (`written proof, internally audited`): explicit stationary law $\pi(\lambda) \propto d_\lambda^{(k)} d_{\lambda^{\mathrm{comp}}}^{(k)} / (|\lambda|!|\lambda^{\mathrm{comp}}|!)$ and $R$-reversibility | [`check-check-2.py`](targets/linusson-2512.24346-conj1/notes/check-check-2.py) (stdlib) | — |
| 8 | [`oeis-A006255`](targets/oeis-A006255/PROOF.md) | Corneth–Padhi conjecture on Graham's sequence (OEIS `A006255`) | **Proved** (`written proof, internally audited`): if $b(n)^2 \ge 2n$ then $a(n) = n + b(n)$ except $n \in \{2, 3, 10, 171\}$ | [`check-check-1.py`](targets/oeis-A006255/notes/check-check-1.py) (stdlib) | — |
| 9 | [`oeis-A386251`](targets/oeis-A386251/COUNTEREXAMPLE.md) | Hohn's 3-segment closed walk conjecture (OEIS `A386251`) | **False** (`Lean-checked`): explicit 4-segment walk of length $4m$ in $n = m^2 - 30$ ($m \ge 92$, first $n = 8434$), while every 3-segment walk has length $\ge 4m + 2$ | [`check-check-3.py`](targets/oeis-A386251/notes/check-check-3.py) (stdlib) | [`OeisA386251.lean`](lean/OpenMath/OeisA386251.lean) |
| 10 | [`yip-2309.10950-rem3.1`](targets/yip-2309.10950-rem3.1/PROOF.md) | Yip's $d = 2$ van Lint–MacWilliams conjecture (`arXiv:2309.10950v2` Rem. 3.3 / *Canad. J. Math.* 2026) | **Proved** (`written proof, internally audited`): for odd squares $q \ge 49$, $A \hat{+} A \subset S_2 \cup \{0\} \implies |A| \le \sqrt{q}$, equality iff $A = \alpha \mathbb{F}_{\sqrt{q}}$ | [`check-check-2.py`](targets/yip-2309.10950-rem3.1/notes/check-check-2.py) (stdlib) | — |
| 11 | [`oeis-A379818`](targets/oeis-A379818/PROOF.md) | Kurkov's binomial formula conjecture on OEIS `A379818` | **Proved** (`Lean-checked`): $a(2^m(2k+1)) = \sum_{j=0}^m (\binom{m+2}{j+1}-\binom{m}{j}) a(2^j k)$ for all $m, k \ge 0$ | [`check-check-1.py`](targets/oeis-A379818/notes/check-check-1.py) (stdlib) | [`OeisA379818.lean`](lean/OpenMath/OeisA379818.lean) |
| 12 | [`oeis-A061313`](targets/oeis-A061313/PROOF.md) | Zabolotskii's Hirzebruch continued fraction conjecture on OEIS `A061313` | **Proved** (`written proof, internally audited`): holds for all $n \ge 2$ with $n = 1$ as the sole exception | [`check-check-1.py`](targets/oeis-A061313/notes/check-check-1.py) (stdlib) | — |
| 13 | [`chang-2201.02781-conj2`](targets/chang-2201.02781-conj2/PROOF.md) | Chang–Yang–Yin–Yao Conjecture 2 (`arXiv:2201.02781v1`) | **Proved** (`written proof, internally audited`): $\mathrm{fgndi}_{\sum}(G) \le 3$ for every connected graph $G \neq K_2$ | [`check-check-2.py`](targets/chang-2201.02781-conj2/notes/check-check-2.py) (stdlib) | — |
| 14 | [`li-2505.12035-conj7`](targets/li-2505.12035-conj7/COUNTEREXAMPLE.md) | Li–Lu–Luo Conjecture 7 (`arXiv:2505.12035v1`, `conj:ore`) | **False** (`Lean-checked`): 6-vertex/5-edge and 7-vertex/6-edge linear 3-uniform hypergraphs satisfy the Ore degree bound with $|E| < n$ | [`check-check-3.py`](targets/li-2505.12035-conj7/notes/check-check-3.py) (stdlib) | [`Li250512035Conj7.lean`](lean/OpenMath/Li250512035Conj7.lean) |
| 15 | [`campbell-2509.16034-conj1`](targets/campbell-2509.16034-conj1/PROOF.md) | Campbell–Currie–Rampersad Open Problems `(c1)` & `(c2)` (`arXiv:2509.16034v1` / *INTEGERS* 2026) | **Solved** (`written proof, internally audited`): exact closed form, 2-regularity recurrences, and 8-state LSD 2-automatic sign automaton | [`check-check-1.py`](targets/campbell-2509.16034-conj1/notes/check-check-1.py) (stdlib) | — |
| 16 | [`oeis-A360949`](targets/oeis-A360949/PROOF.md) | Hanna's 2023 mod-4 Thue–Morse conjecture for OEIS `A360949` | **Proved** (`written proof, internally audited`): $a(0)=1$, $a(2\,\mathrm{A161674}(k)+1) \equiv 2 \pmod 4$, and $a(n) \equiv 0 \pmod 4$ otherwise | [`check-check-3.py`](targets/oeis-A360949/notes/check-check-3.py) (stdlib) | — |
| 17 | [`cooper-2302.00757-conj11.2`](targets/cooper-2302.00757-conj11.2/PROOF.md) | Cooper Conjecture 11.2 (`arXiv:2302.00757v2` / *Contemp. Math.* 818, 2025) | **Proved** (`written proof, internally audited`): $T_{11}(3n) \equiv T_{11}(n)+3n \pmod 9$ and $T_{11}(5n) \equiv T_{11}(n) \pmod{25} \iff 5 \mid n$ | [`check-check-1.py`](targets/cooper-2302.00757-conj11.2/notes/check-check-1.py) (stdlib) | — |
| 18 | [`oeis-A396911`](targets/oeis-A396911/PROOF.md) | Irvine's 2026 Vogel phyllotaxis walk bound (OEIS `A396911`) | **Proved** (`written proof, internally audited`): $a(n) \le \frac{3}{2}n^2$ for all $n \ge 0$ (and $\limsup a(n)/n^2 = \pi/\sqrt{5}$) | [`check-check-1.py`](targets/oeis-A396911/notes/check-check-1.py) (`mpmath`) | — |
| 19 | [`daugherty-2610.29291-conj6.1`](targets/daugherty-2610.29291-conj6.1/COUNTEREXAMPLE.md) | Daugherty et al. Conjecture 6.1 (`arXiv:2610.29291v1`, `conj:box`) | **False** (`counterexample, verified by exact computation`): wide pair $(6,5,5,3,2,1) \to (6,5,5,3,3,1)$ has $LT(\lambda)=32 < 56=LT(\mu)$ | [`check-check-3.py`](targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py) (stdlib) | — |
| 20 | [`gaetz-2512.08168-conj1`](targets/gaetz-2512.08168-conj1/PROOF.md) | Gaetz–Gao Conjecture 1.3 (`arXiv:2512.08168v2`, `conj:union-intersection`) | **Proved** (`written proof, internally audited`): $\mathrm{BP}(w)$ is closed under $\cap$ and $\cup$ for every Coxeter group $(W, S)$ and $w \in W$ | [`check-check-3.py`](targets/gaetz-2512.08168-conj1/notes/check-check-3.py) (stdlib) | — |
| 21 | [`oeis-A208425`](targets/oeis-A208425/PROOF.md) | Zhi-Wei Sun's supercongruence Conjecture (ii) on OEIS `A208425` | **Proved** (`written proof, internally audited`): $\sum_{k=0}^{p-1} a(k) \equiv \binom{2(p-1)/3}{(p-1)/3} \pmod{p^2}$ for all primes $p \equiv 1 \pmod 3$ | [`check-check-2.py`](targets/oeis-A208425/notes/check-check-2.py) (stdlib) | — |
| 22 | [`ragunathan-2603.29978-conj6.1`](targets/ragunathan-2603.29978-conj6.1/PROOF.md) | Ragunathan–Van Tuyl Conjecture 6.1 (`arXiv:2603.29978v2`) | **Proved** (`written proof, internally audited`): in $\mathrm{char}(K)=0$, $A(\mathrm{vdw}(n,k))$ has WLP for all $n>k$ ($k$ even) and fails WLP for $n \ge m$ ($k$ odd) | [`check-check-3.py`](targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py) (stdlib) | — |
| 23 | [`petyuk-2210.14762-conj1`](targets/petyuk-2210.14762-conj1/COUNTEREXAMPLE.md) | Petyuk Conjecture 1 (`arXiv:2210.14762v2`) | **False** (`counterexample, verified by exact computation`): $S(4,3)$ is 3-colorable and represented by an explicit length-4536 word | [`check-check-1.py`](targets/petyuk-2210.14762-conj1/notes/check-check-1.py) (stdlib) | — |
| 24 | [`blanco-2511.16959-conj5`](targets/blanco-2511.16959-conj5/PROOF.md) | Blanco et al. Conjecture 5 (`arXiv:2511.16959v3` / *DMTCS* 28:1, 2026) | **Proved** (`written proof, internally audited`): $\max_{n>k+1}|F_k(n)| = k+1$ ($k$ even) and $(k+1)/2$ ($k$ odd) for all $k \ge 2$ | [`check-check-2.py`](targets/blanco-2511.16959-conj5/notes/check-check-2.py) (stdlib) | — |
| 25 | [`biswas-2603.04876-conj5.5`](targets/biswas-2603.04876-conj5.5/PROOF.md) | Biswas–Mandal–Saha Conjecture 5.5 (`arXiv:2603.04876v1`) | **Proved** (`written proof, internally audited`): exact characterization of $\mathcal{RV}_{\mathrm{chordal}}(n)$ for all $n \ge 3$ | [`check-check-3.py`](targets/biswas-2603.04876-conj5.5/notes/check-check-3.py) (stdlib) | — |
| 26 | [`oeis-A400888`](targets/oeis-A400888/PROOF.md) | Lafitte's surjectivity conjecture for OEIS `A400888` | **Proved** (`written proof, internally audited`): OEIS `A400888` is surjective onto $\mathbb{Z}_{\ge 1}$ | [`check-check-2.py`](targets/oeis-A400888/notes/check-check-2.py) (stdlib) | — |

Full statements, novelty receipts, and caveats are recorded in [`RESULTS.md`](RESULTS.md) and each target's `TARGET.md` and `AUDIT.md`.

## Reproducing the Verification

### 1. Exact-Arithmetic Python Verifiers

Independent checker scripts (22 of 26 require Python 3.10+ standard library only):

```bash
python3 targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py   # stdlib
python3 targets/wei-2310.17337-conj1.5/notes/check-check-1.py       # stdlib
python3 targets/oeis-A100691/notes/check-check-3.py                 # sympy
python3 targets/dris-2202.08116-conj5.1/notes/check-check-2.py      # stdlib
python3 targets/oeis-A250917/notes/check-check-2.py                 # sympy
python3 targets/oeis-A108430/notes/check-check-1.py                 # sympy
python3 targets/linusson-2512.24346-conj1/notes/check-check-2.py    # stdlib
python3 targets/oeis-A006255/notes/check-check-1.py                 # stdlib
python3 targets/oeis-A386251/notes/check-check-3.py                 # stdlib
python3 targets/yip-2309.10950-rem3.1/notes/check-check-2.py        # stdlib
python3 targets/oeis-A379818/notes/check-check-1.py                 # stdlib
python3 targets/oeis-A061313/notes/check-check-1.py                 # stdlib
python3 targets/chang-2201.02781-conj2/notes/check-check-2.py       # stdlib
python3 targets/li-2505.12035-conj7/notes/check-check-3.py          # stdlib
python3 targets/campbell-2509.16034-conj1/notes/check-check-1.py    # stdlib
python3 targets/oeis-A360949/notes/check-check-3.py                 # stdlib
python3 targets/cooper-2302.00757-conj11.2/notes/check-check-1.py   # stdlib
python3 targets/oeis-A396911/notes/check-check-1.py                 # mpmath
python3 targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py # stdlib
python3 targets/gaetz-2512.08168-conj1/notes/check-check-3.py       # stdlib
python3 targets/oeis-A208425/notes/check-check-2.py                 # stdlib
python3 targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py # stdlib
python3 targets/petyuk-2210.14762-conj1/notes/check-check-1.py      # stdlib
python3 targets/blanco-2511.16959-conj5/notes/check-check-2.py      # stdlib
python3 targets/biswas-2603.04876-conj5.5/notes/check-check-3.py    # stdlib
python3 targets/oeis-A400888/notes/check-check-2.py                 # stdlib
```

Each target directory also includes the finder's `verify.py`.

### 2. Lean 4 Formal Verification

The Lean 4 project in [`lean/`](lean/) uses `leanprover/lean4:v4.36.0` and Mathlib `v4.36.0`:

```bash
cd lean
lake exe cache get   # download prebuilt Mathlib oleans (recommended)
lake build
```

All seven formalizations compile with no `sorry` and depend only on the standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound`):

- `OpenMath.Ferrero251116335Conj18`: `refutes_conjecture_1_8_infinite_family`, `refutes_conjecture_1_8_circ12`, `not_ferrero_conjecture_1_8`
- `OpenMath.Wei231017337Conj15`: `refutes_wei_conjecture_1_5_witness`, `not_wei_conjecture_1_5`
- `OpenMath.OeisA100691`: `A193641_recurrence`, `aOEIS_gf_identity`, `aOEIS_eq_A193641_sub_three`, `sawCount_eq_length_sawPaths`, `sawCount_five`, `refutes_combinatorial_reading_at_five`, `not_mathar_combinatorial_conjecture`
- `OpenMath.Dris220208116Conj51`: `not_summable_one_div_primes_eq_mod`, `dris_conjecture_5_1`
- `OpenMath.OeisA386251`: `witnessWalk4_simple_cycle`, `a386251_eq_four_mul`, `refutes_a386251_conjecture_infinite_family`, `refutes_a386251_at_8434`, `not_a386251_conjecture`
- `OpenMath.Li250512035Conj7`: `witness1_no_hamiltonian_berge_cycle`, `witness2_no_hamiltonian_berge_cycle`, `not_li_lu_luo_conjecture_7`, `not_li_lu_luo_conjecture_7_linear_uniform`
- `OpenMath.OeisA379818`: `kurkov_conjecture_A379818`, `kurkov_conjecture_A379818_int`, `kurkov_conjecture_A379818_of_recurrence`

## Repository Layout

```text
.
├── README.md
├── RESULTS.md
├── lean/
│   ├── lakefile.toml
│   ├── lake-manifest.json
│   ├── lean-toolchain
│   ├── OpenMath.lean
│   └── OpenMath/
│       ├── Ferrero251116335Conj18.lean
│       ├── Wei231017337Conj15.lean
│       ├── OeisA100691.lean
│       ├── Dris220208116Conj51.lean
│       ├── OeisA386251.lean
│       ├── Li250512035Conj7.lean
│       └── OeisA379818.lean
└── targets/   # 26 verified target directories
```

Each target directory contains `TARGET.md`, `COUNTEREXAMPLE.md` or `PROOF.md`, `AUDIT.md`, `verify.py`, and `notes/` (independent checker script and report, audit helper/ruling notes where applicable, and Gate 2/3 novelty receipts).
