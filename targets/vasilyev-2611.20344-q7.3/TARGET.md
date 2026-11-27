---
source: "Oleg Vasilyev, 'Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph', arXiv:2611.20344v2 (math.NT, updown.tex), Section 7, Question 7.3 (q:types, lines 1991–1993; Remark 4.4 rem:types, lines 1134–1145)"
status: reported
owner: attack-4
started: 2026-11-27T13:01:00Z
updated: 2026-11-27T14:03:00Z
identifiers: ["arXiv:2611.20344v2", "q:types", "rem:types", "up-down graph", "T_S"]
---

# Target: `vasilyev-2611.20344-q7.3`

## Verbatim Problem Statement

For $x \in \mathbb{N} = \{1, 2, 3, \dots\}$, let $U(x) = \lceil 3x/2 \rceil$ and $D(x) = \lceil x/2 \rceil$, and for $S \subseteq \mathbb{N}$ let $T_S(x) = U(x)$ if $x \in S$ and $D(x)$ if $x \notin S$.

From Section 7 (*Questions*, `updown.tex` lines 1991–1993, referencing Remark 4.4 `rem:types`, lines 1134–1145; note `updown.tex` shares the section counter across Lemma 2.1, Definition 2.2, Proposition 2.3 `prop:dict`, and Remark 4.4 `rem:types`):
> **Question 7.3.** Is there a map with infinitely many cycles and a divergent orbit (Remark 4.4)?

## Gate 1 & Attack Novelty Receipts

- Initial screening (`scout-10`, `2026-11-27T13:09:30Z`): `0` hits for Question 7.3 (`q:types`) across snapshots, GitHub, Zenodo, and web.
- Full live novelty check (`vasilyev-lit`, `2026-11-27T13:49:00Z`, receipt in `notes/novelty-attack.md`): **CLEAR** across all `720` snapshots, live GitHub (`trureturing` `dev`, `Mira-Cult/math`, `s66lem`, `OjasMor`, `andrheabacor`, `Hwzw`, `insorrowmeow`, `1337isnot1337`), Zenodo API, arXiv API (`2611.20344v2` latest), Crossref, and web search (all prior resolutions address only Q7.1, Q7.7, or Q7.12).

## Attack Log (`attack-4`)
- Started attack: `2026-11-27T13:46:30Z`.
- Completed proof: `2026-11-27T13:55:30Z` -> `status: candidate`. Proved **YES** to Question 7.3 (`q:types`) with exact orbit type $(k, l) = (\infty, 1)$ (Remark 4.4 `rem:types`) via two elementary lemmas: (1) Closed-Box Trap Lemma ($V(B) = [B+1, 3B-1] \setminus (R \cup \{2B\})$ is closed under $U$ on $[B+1, 2B-1]$ and $D$ on $[2B+1, 3B-1]$ whenever $B \equiv 5 \pmod 6$, $U(\mathbb{N} \setminus R) \subseteq \mathbb{N} \setminus R$, and $R \cap [B+1, U(B)-1] = \emptyset$), and (2) Admissible Stage Extension constructing a divergent ray $R$ (using only $U$-steps and $D$-steps at $x \equiv 2 \pmod 6$) with infinitely many strictly separated trap anchors $B_m \equiv 5 \pmod 6$ (handling all residues via $2$-adic parity flipping $3^e u$ vs $3^{e+1} u \pmod 4$ and $v_2(5q+3)$ descent).
- Deliverables: `PROOF.md`, standalone pure-integer zero-float `verify.py` (`.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/verify.py` -> `PASS` in 0.14s).
