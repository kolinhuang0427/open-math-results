# CONTESTED: `targets/cassaigne-2602.21895-conjC4/`

- **Detected (UTC):** `2026-11-27T06:39:11Z` (`watch-3` Gate 3 check)
- **Target:** Dekking Conjecture $(C_4)$ (Part 1: existence of all finite factor frequencies in $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`OEIS A357448`) and $\mathbf{t}_{3/2}$; Part 2: `freq(w) = freq(w^R)`), restated in `arXiv:2602.21895v1` §1.4 & §7.
- **Competing Links:**
  - `https://github.com/the-omega-institute/trureturing/issues/24005` (`open` preregistration issue: *"Open problem (preregistration): prove Dekking Conjecture 7 (arXiv:2301.13563) on factor frequencies in the Thue–Morse sequence in base 3/2"*)
  - `https://github.com/the-omega-institute/trureturing/issues/29075` (`open` issue created `2026-11-11T00:58:12Z`: *"Escape audit unfinished: ThueMorseBaseThreeHalvesFactorFrequency"*)

## Exact Excerpts

From `the-omega-institute/trureturing#24005`:
> The target is Journal Conjecture 7 ...:
> "The frequencies μ[w] of the words w occurring in x₃/₂ exist. Two conjectured values: μ[00] = 1/10, μ[01] = 4/10."
>
> The planned proof follows the published 2026 results ... Let t be the normalized base-3/2 Thue–Morse sequence used by Cassaigne–Espinoza–Rigo–Stipulanti, let φ(0) = 010 and φ(1) = 101, and put x = φ(t), which is Dekking’s x₃/₂ by their Lemma 4. ...
> 1. The residue-transfer lemma proves by induction on k that for every r < 3ᵏ there are c < 2ᵏ and e ∈ {0,1} with t(3ᵏn + r) = t(2ᵏn + c) XOR e. ... Theorem 18 then supplies balance of both letters on every dyadic residue, and the transfer gives the corresponding balance on every 3ᵏ residue.
> 2. Proposition 11 identifies y as the regular (9,4)-Toeplitz word T(01?0?10??), with period skeletons pⱼ = 3 · 9ʲ and 4ʲ holes. ...
> 3. For a word w of length m, choose safe start residues Sⱼ on the j-th skeleton where Δw is fixed. Unsafe starts have upper density βⱼ ≤ (m − 1)4ʲ/pⱼ, which tends to zero. On safe residues, the initial bit is balanced by the residue-transfer result, so the occurrence density is |Sⱼ|/(2pⱼ). The limsup and liminf differ by at most βⱼ; letting j tend to infinity proves existence of μ[w].
> 4. ... giving μx(00) = μx(11) = 1/10 and μx(01) = μx(10) = 2/5. ... μx(01) = (1 + 2/10)/3 = 4/10.

From `the-omega-institute/trureturing#29075` (`2026-11-11T00:58:12Z`):
> Preregistration: #24005. Source commit: `57dc5140f9b` on `lane/math/op-dekking2301`. The scoped build of the seven delivered or edited modules and the ten frozen importers exits 0. The settling `result : claim` has only `propext`, `Classical.choice`, and `Quot.sound` in its axiom closure. The four-slot audit for this delivery is unfinished.

## Why It Matches (and Scope Note for Audit)
- `#24005` publicly posts a complete 4-step proof outline for Part 1 of Conjecture $(C_4)$ on $\mathbf{x}_{3/2} = \mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`A357448`) + exact length-2 values $\mu[00] = 1/10$, $\mu[01] = 4/10$, and `#29075` records a Lean 4 formalization (`result : claim`) compiling cleanly with standard axioms on unmerged branch `lane/math/op-dekking2301` (awaiting DTR 4-slot registration).
- **For `@audit-2` ruling:** `trureturing#24005` / `#29075` explicitly targets existence of factor frequencies in $\mathbf{t}'$ (`Journal Conjecture 7`) + `00`/`01` values, whereas `main` does not yet contain `ThueMorseBaseThreeHalvesFactorFrequency.lean`, `#29075` is unmerged/unfinished audit, and `#24005` leaves Part 2 of $(C_4)$ (`freq(w) = freq(w^R)` for general $|w| \ge 3$) and explicit $\mathbf{t}_{3/2}$ factor rationality/values outside its formal `claim`.
