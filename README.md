# Open Math — Verified Results

This repository contains verified mathematical results and verification artifacts (exact-arithmetic Python verifiers, independent audit and novelty reports, and Lean 4 formalizations).

> **Note:** Internal auditing, exact computation, and formalization of primary-source definitions do not constitute external peer review. See [`RESULTS.md`](RESULTS.md) and each target's `AUDIT.md` for scope and caveats.

## Summary of Results

| Target | Conjecture | Result | Independent Python Verifier | Lean 4 Formalization |
|---|---|---|---|---|
| [`ferrero-2511.16335-conj1.8`](targets/ferrero-2511.16335-conj1.8/COUNTEREXAMPLE.md) | Ferrero–Hall–Hogben–Hunnell–Small Conjecture 1.8 (`arXiv:2511.16335v1`, AJC 96(2) 2026) | **Refuted**: 12-vertex circulant $C_6[2K_1] \cong \mathrm{Circ}(12,\{1,5\})$ and infinite blowup family $C_6[r_0 K_1,\dots,r_5 K_1]$ ($r_i \ge 2$) | [`check-check-2.py`](targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py) (stdlib only) | [`Ferrero251116335Conj18.lean`](lean/OpenMath/Ferrero251116335Conj18.lean) |
| [`wei-2310.17337-conj1.5`](targets/wei-2310.17337-conj1.5/COUNTEREXAMPLE.md) | Wei–Zhang–Zhao Conjecture 1.5 (`arXiv:2310.17337v1`) | **Refuted**: 12-vertex, 18-edge truncated tetrahedral graph at $k = 8$ ($\iota(G, C_8) = 2 > 19/10$), plus $GP(9,2)$ ($k = 14$) and $GP(11,2)$ ($k = 18$) | [`check-check-1.py`](targets/wei-2310.17337-conj1.5/notes/check-check-1.py) (stdlib only) | [`Wei231017337Conj15.lean`](lean/OpenMath/Wei231017337Conj15.lean) |

Full statements, novelty receipts, and caveats (including the published DMAA journal version caveat for `arXiv:2310.17337v1`) are recorded in [`RESULTS.md`](RESULTS.md) and each target's `TARGET.md` and `AUDIT.md`.

## Reproducing the Verification

### 1. Exact-Arithmetic Python Verifiers

The independent checker scripts require only Python 3.10+ (no third-party packages):

```bash
python3 targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py
python3 targets/wei-2310.17337-conj1.5/notes/check-check-1.py
```

The finder `verify.py` scripts can also be run directly (`ferrero-2511.16335-conj1.8/verify.py` requires `networkx`; `wei-2310.17337-conj1.5/verify.py` uses only the standard library):

```bash
python3 targets/ferrero-2511.16335-conj1.8/verify.py
python3 targets/wei-2310.17337-conj1.5/verify.py
```

### 2. Lean 4 Formal Verification

The Lean 4 project in [`lean/`](lean/) uses `leanprover/lean4:v4.36.0` and Mathlib `v4.36.0`:

```bash
cd lean
lake exe cache get   # download prebuilt Mathlib oleans (recommended)
lake build
```

Both formalizations compile with no `sorry` and depend only on the standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound`):

- `OpenMath.Ferrero251116335Conj18`: `refutes_conjecture_1_8_infinite_family`, `refutes_conjecture_1_8_circ12`, `not_ferrero_conjecture_1_8`
- `OpenMath.Wei231017337Conj15`: `refutes_wei_conjecture_1_5_witness`, `not_wei_conjecture_1_5`

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
│       └── Wei231017337Conj15.lean
└── targets/
    ├── ferrero-2511.16335-conj1.8/
    │   ├── TARGET.md
    │   ├── COUNTEREXAMPLE.md
    │   ├── AUDIT.md
    │   ├── verify.py
    │   └── notes/
    │       ├── check-check-2.py
    │       ├── check-check-2.md
    │       ├── audit-helper-ferrero.md
    │       └── novelty-gate{2,3}-watch-{1,5,6}.md
    └── wei-2310.17337-conj1.5/
        ├── TARGET.md
        ├── COUNTEREXAMPLE.md
        ├── AUDIT.md
        ├── verify.py
        └── notes/
            ├── check-check-1.py
            ├── check-check-1.md
            ├── audit-lit-wei.md
            └── novelty-gate{2,3}-watch-{1,5,6}.md
```
