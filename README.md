# Open Math — Verified Results

This repository contains verified mathematical results and verification artifacts (exact-arithmetic Python verifiers, independent audit and novelty reports, and Lean 4 formalizations).

> **Note:** Internal auditing, exact computation, and formalization of primary-source definitions do not constitute external peer review. See [`RESULTS.md`](RESULTS.md) and each target's `AUDIT.md` for scope and caveats.

## Summary of Results

| Target | Conjecture | Result | Independent Python Verifier | Lean 4 Formalization |
|---|---|---|---|---|
| [`ferrero-2511.16335-conj1.8`](targets/ferrero-2511.16335-conj1.8/COUNTEREXAMPLE.md) | Ferrero–Hall–Hogben–Hunnell–Small Conjecture 1.8 (`arXiv:2511.16335v1`, AJC 96(2) 2026) | **False** (`Lean-checked`): 12-vertex circulant $C_6[2K_1] \cong \mathrm{Circ}(12,\{1,5\})$ and infinite blowup family $C_6[r_0 K_1,\dots,r_5 K_1]$ ($r_i \ge 2$) | [`check-check-2.py`](targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py) (stdlib) | [`Ferrero251116335Conj18.lean`](lean/OpenMath/Ferrero251116335Conj18.lean) |
| [`wei-2310.17337-conj1.5`](targets/wei-2310.17337-conj1.5/COUNTEREXAMPLE.md) | Wei–Zhang–Zhao Conjecture 1.5 (`arXiv:2310.17337v1`) | **False** (`Lean-checked`): 12-vertex, 18-edge truncated tetrahedral graph at $k = 8$ ($\iota(G, C_8) = 2 > 19/10$), plus $GP(9,2)$ ($k = 14$) and $GP(11,2)$ ($k = 18$) | [`check-check-1.py`](targets/wei-2310.17337-conj1.5/notes/check-check-1.py) (stdlib) | [`Wei231017337Conj15.lean`](lean/OpenMath/Wei231017337Conj15.lean) |
| [`oeis-A100691`](targets/oeis-A100691/PROOF.md) | R. J. Mathar's 2022 conjecture linking OEIS `A100691` and `A193641` | **Resolved** (`Lean-checked`): proved `a_OEIS(n) = A193641(n+2) - 3` ($n \ge 1$) for the stored recurrence, and disproved the triangular-strip SAW reading for every $n \ge 5$ ($s(5) = 160 \ne 158$) | [`check-check-3.py`](targets/oeis-A100691/notes/check-check-3.py) (`sympy`) | [`OeisA100691.lean`](lean/OpenMath/OeisA100691.lean) |
| [`dris-2202.08116-conj5.1`](targets/dris-2202.08116-conj5.1/PROOF.md) | Dris Conjecture 5.1 (`arXiv:2202.08116v1`, *Octogon Math. Mag.* 2022) | **Proved** (`written proof, internally audited`): asymptotic density of $\{m \ge 1 : \gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))\}$ is $0$ | [`check-check-2.py`](targets/dris-2202.08116-conj5.1/notes/check-check-2.py) (stdlib) | — |
| [`oeis-A250917`](targets/oeis-A250917/PROOF.md) | R. J. Mathar's 2020 D-finite recurrence for OEIS `A250917` | **Proved** (`written proof, internally audited`): order-5 polynomial recurrence holds for all $n \ge 5$ (and $n = 3, 4$) via exact identity in $\mathbb{Q}(x)[\sqrt{1-4x}]$ | [`check-check-2.py`](targets/oeis-A250917/notes/check-check-2.py) (`sympy`) | — |
| [`oeis-A108430`](targets/oeis-A108430/PROOF.md) | R. J. Mathar's 2022 D-finite recurrence for OEIS `A108430` | **Proved** (`written proof, internally audited`): order-3 polynomial recurrence holds for all $n \ge 3$ via exact reduction in $\mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$ | [`check-check-1.py`](targets/oeis-A108430/notes/check-check-1.py) (`sympy`) | — |
| [`linusson-2512.24346-conj1`](targets/linusson-2512.24346-conj1/PROOF.md) | Linusson–Özdemir Conjecture 1 (`arXiv:2512.24346v1`, `conj:complement`) | **Proved** (`written proof, internally audited`): exact closed-form stationary distribution $\pi(\lambda) \propto \frac{d_\lambda^{(k)} d_{\lambda^{\mathrm{comp}}}^{(k)}}{|\lambda|!|\lambda^{\mathrm{comp}}|!}$ and $R$-reversibility give $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$ for all $k \ge 1$ | [`check-check-2.py`](targets/linusson-2512.24346-conj1/notes/check-check-2.py) (stdlib) | — |
| [`oeis-A006255`](targets/oeis-A006255/PROOF.md) | Corneth/Padhi conjecture on Graham's sequence (OEIS `A006255`) | **Proved** (`written proof, internally audited`): if $b(n)^2 \ge 2n$ then $a(n) = n + b(n)$ for all $n \ge 1$ except $n \in \{2, 3, 10, 171\}$ | [`check-check-1.py`](targets/oeis-A006255/notes/check-check-1.py) (stdlib) | — |
| [`oeis-A386251`](targets/oeis-A386251/COUNTEREXAMPLE.md) | Hohn's 3-segment closed walk conjecture (OEIS `A386251`) | **False** (`written proof, internally audited`): for every $m \ge 92$ and $n = m^2 - 30$ (starting at $n = 8434$), an explicit 4-segment walk has length $4m$ while every 3-segment walk has length $\ge 4m + 2$ | [`check-check-3.py`](targets/oeis-A386251/notes/check-check-3.py) (stdlib) | — |
| [`yip-2309.10950-rem3.1`](targets/yip-2309.10950-rem3.1/PROOF.md) | Yip's $d = 2$ van Lint–MacWilliams conjecture (`arXiv:2309.10950v2` Rem. 3.3 / *Canad. J. Math.* 2026) | **Proved** (`written proof, internally audited`): for every odd square $q \ge 49$, $A \hat{+} A \subset S_2 \cup \{0\} \implies |A| \le \sqrt{q}$, with equality iff $A = \alpha \mathbb{F}_{\sqrt{q}}$ ($\alpha \in S_2$) | [`check-check-2.py`](targets/yip-2309.10950-rem3.1/notes/check-check-2.py) (stdlib) | — |

Full statements, novelty receipts, and caveats are recorded in [`RESULTS.md`](RESULTS.md) and each target's `TARGET.md` and `AUDIT.md`.

## Reproducing the Verification

### 1. Exact-Arithmetic Python Verifiers

Independent checker scripts:

```bash
python3 targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py   # stdlib only
python3 targets/wei-2310.17337-conj1.5/notes/check-check-1.py       # stdlib only
python3 targets/oeis-A100691/notes/check-check-3.py                 # requires sympy
python3 targets/dris-2202.08116-conj5.1/notes/check-check-2.py      # stdlib only
python3 targets/oeis-A250917/notes/check-check-2.py                 # requires sympy
python3 targets/oeis-A108430/notes/check-check-1.py                 # requires sympy
python3 targets/linusson-2512.24346-conj1/notes/check-check-2.py    # stdlib only
python3 targets/oeis-A006255/notes/check-check-1.py                 # stdlib only
python3 targets/oeis-A386251/notes/check-check-3.py                 # stdlib only
python3 targets/yip-2309.10950-rem3.1/notes/check-check-2.py        # stdlib only
```

Finder `verify.py` scripts:

```bash
python3 targets/ferrero-2511.16335-conj1.8/verify.py                # requires networkx
python3 targets/wei-2310.17337-conj1.5/verify.py                    # stdlib only
python3 targets/oeis-A100691/verify.py                              # requires sympy
python3 targets/dris-2202.08116-conj5.1/verify.py                   # requires sympy
python3 targets/oeis-A250917/verify.py                              # requires sympy
python3 targets/oeis-A108430/verify.py                              # requires sympy
python3 targets/linusson-2512.24346-conj1/verify.py                 # requires sympy
python3 targets/oeis-A006255/verify.py                              # stdlib only
python3 targets/oeis-A386251/verify.py                              # stdlib only
python3 targets/yip-2309.10950-rem3.1/verify.py                     # stdlib only
```

### 2. Lean 4 Formal Verification

The Lean 4 project in [`lean/`](lean/) uses `leanprover/lean4:v4.36.0` and Mathlib `v4.36.0`:

```bash
cd lean
lake exe cache get   # download prebuilt Mathlib oleans (recommended)
lake build
```

All three formalizations compile with no `sorry` and depend only on the standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound`):

- `OpenMath.Ferrero251116335Conj18`: `refutes_conjecture_1_8_infinite_family`, `refutes_conjecture_1_8_circ12`, `not_ferrero_conjecture_1_8`
- `OpenMath.Wei231017337Conj15`: `refutes_wei_conjecture_1_5_witness`, `not_wei_conjecture_1_5`
- `OpenMath.OeisA100691`: `A193641_recurrence`, `aOEIS_gf_identity`, `aOEIS_eq_A193641_sub_three`, `sawCount_eq_length_sawPaths`, `sawCount_five`, `refutes_combinatorial_reading_at_five`, `not_mathar_combinatorial_conjecture`

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
│       └── OeisA100691.lean
└── targets/
    ├── ferrero-2511.16335-conj1.8/
    ├── wei-2310.17337-conj1.5/
    ├── oeis-A100691/
    ├── dris-2202.08116-conj5.1/
    ├── oeis-A250917/
    ├── oeis-A108430/
    ├── linusson-2512.24346-conj1/
    ├── oeis-A006255/
    ├── oeis-A386251/
    └── yip-2309.10950-rem3.1/
```

Each target directory contains `TARGET.md`, `COUNTEREXAMPLE.md` or `PROOF.md`, `AUDIT.md`, `verify.py`, and `notes/` (independent checker script and report, audit helper notes where applicable, and Gate 2/3 novelty receipts).
