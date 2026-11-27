# CONTESTED — `targets/campbell-2509.16034-conj1/` (Resolved Elsewhere in `the-omega-institute/trureturing`)

- **Detected UTC:** `2026-11-26T23:57:39Z`
- **Watcher:** `watch-6`
- **Source Links:**
  - https://github.com/the-omega-institute/trureturing/blob/1b221a306acf68c117194cb3b4bd26b0076867d7/Problems/campbell-currie-rampersad-eq-11.md (commit `04a561c88d`, `2026-09-08T15:16:17Z`: *"math(words): settle equation (11) of Campbell-Currie-Rampersad for the Thue-Morse word"*, plus commit `96baee8682`, `2026-09-14T23:06:50Z`: *"docs: record Thue-Morse nonautomaticity consequence"*)
  - https://github.com/the-omega-institute/trureturing/blob/1b221a306acf68c117194cb3b4bd26b0076867d7/Problems/thue-morse-reduced-abelian-odd.md (formalized module `D5/S1/Words/Complexity/ThueMorseReducedAbelianOdd`)
  - https://github.com/the-omega-institute/trureturing/blob/1b221a306acf68c117194cb3b4bd26b0076867d7/Blueprint/D5/S1/Words/Complexity/ThueMorseReducedAbelianEven.md

## Excerpt
From `the-omega-institute/trureturing/Problems/campbell-currie-rampersad-eq-11.md`:
> Campbell, Currie and Rampersad display
>     `|rho(4n+2) - rho(4n)| = 0  if t(n+1) = t(3n+1),  and 1 otherwise,`
> as equation (11) in the Conclusion of `arXiv:2509.16034v1` ...
> The odd-index half of the same paragraph is already carried here as `Problems/thue-morse-reduced-abelian-odd`, together with the frozen module `D5/S1/Words/Complexity/ThueMorseReducedAbelianOdd`.

Commit `04a561c88d` (`2026-09-08`): `math(words): settle equation (11) of Campbell-Currie-Rampersad for the Thue-Morse word`; commit `96baee8682` (`2026-09-14`): `docs: record Thue-Morse nonautomaticity consequence`.

## Why It Matches
`targets/campbell-2509.16034-conj1/` targets Section 3 Conclusion of Campbell–Currie–Rampersad (`arXiv:2509.16034v1` / *INTEGERS* 26 #A34): odd recurrence $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(2n+1) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1)$, eq. (11) `displayconjecture`, and non-$k$-automaticity. Those problems are already proved and Lean-4-formalized (`D5/S1/Words/Complexity/ThueMorseReducedAbelian{Odd,Even}`) in `the-omega-institute/trureturing` (`2026-09-08` / `2026-09-14`).
