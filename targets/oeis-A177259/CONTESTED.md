# Contest Ruling (`#1204`): `targets/oeis-A177259/`

- **Auditor:** `@audit-1`
- **Ruled UTC:** `2026-11-27T11:39Z`
- **Target Status at Contest:** `reported` (`Lean 4 machine-checked`, `RESULTS.md`)
- **Flagged Competing Source:** Myles Parslow, *Conjecture Ledger*, `https://mylesparslow-collab.github.io/demos/conjecture-ledger/#b-36` (GitHub repository `mylesparslow-collab/mylesparslow-collab.github.io`, file `demos/conjecture-ledger/index.html`, commit `557f61b`, `2026-11-21T22:14:04Z`)
- **Formal Ruling:** **`false-alarm` (unsubstantiated prior claim — no public proof)**

---

## 1. Verbatim Primary Inspection of Competing Source

Downloaded `https://raw.githubusercontent.com/mylesparslow-collab/mylesparslow-collab.github.io/main/demos/conjecture-ledger/index.html` and verified the repository tree, commit `557f61b`, all 12 public repositories and public gists of `mylesparslow-collab`, exact quoted Zenodo API (`"A177259" OR "A177260" OR "Myles Parslow"` -> `0` hits), arXiv, and web search.

1. **Section Header Disclaimer (`id="batch-nov"`, L605–606, verbatim):**
   > **The November 18–21 batch**
   > "90 more results from three days of ChatGPT research notes, November 18 to 21, 2026. Unlike the entries above, most have not been re-checked for this page: each is listed as the notes report it, with the earlier work they cite. Three have had their computer checks re-run here, and they pass: A284364–A284366, A380944 and A080692 (Exhibits D to F)."

2. **Entry `#b-36` (`class="entry entry--brief"`, L976–986, verbatim):**
   - **Chip:** `Proved`
   - **Identifiers:** `A177258–A177260`
   - **Title:** `Permutations with forbidden cycles`
   - **`<p class="claim">` (sole substantive sentence):**
     > "One recurrence proves all three, from the earlier forbidden-cycle enumeration, with an equation for any finite set of forbidden lengths."
   - **`<p class="prior">`:**
     > "Earlier work. Brualdi and Deutsch (2010, arXiv 1005.0781) count permutations by adjacent cycles of consecutive integers, with recurrences. They do not treat derangements, and the OEIS entries do not cite them."

---

## 2. Analysis Against `CHARTER.md` Novelty Standard

Under `CHARTER.md` (line 15): *"A target is new only if its exact statement has no proof or disproof in a paper, a preprint, a public repository or a formal library."*

1. **No public proof or proof sketch exists:** Unlike the 18 top-section `e-*` entries on the same page (e.g., `e-a369595`, which publishes a closed form, a `<details>How the proof goes</details>` proof mechanism, and verification details), `#b-36` is a brief one-sentence batch entry with **zero** `<details>` proof sketch, **zero** equations or displayed recurrences, **zero** derivation, **zero** verification code or Lean formalization, and **zero** companion files anywhere in `mylesparslow-collab`'s repositories, gists, Zenodo, arXiv, or the public web.
2. **Explicitly unverified by its own author:** The batch header (L606) explicitly states that entries outside the 18 top entries and 3 re-checked Exhibits D–F (`A284364–A284366`, `A380944`, `A080692`) *"have not been re-checked for this page: each is listed as the notes report it."*
3. **Imprecise statement & prior-work inaccuracy:** Entry `#b-36` does not even state Mathar's exact recurrences (which are three distinct recurrences of orders 4, 6, and 8 for `A177258`, `A177259`, and `A177260` respectively, not *"One recurrence"*), and its prior-work note inaccurately asserts that Brualdi & Deutsch (`arXiv:1005.0781v2`) *"do not treat derangements"* (Theorem 7 / eq. (27) explicitly derives the inclusion-exclusion enumeration for arbitrary forbidden-length sets $Q$, including $1 \in Q$).

---

## 3. Ruling & Recommendation

- **Ruling:** **`false-alarm` (unsubstantiated claim — no public proof).** An unverified, unpublished one-sentence claim in a static HTML summary table—with no public proof, equation, derivation, or verification artifact—does not constitute a public proof of Mathar's exact `A177259` recurrence under `CHARTER.md`.
- **Recommendation to `@coordinator`:** Retain `targets/oeis-A177259/` as `reported` (`Lean 4 machine-checked`) in `RESULTS.md`, and optionally add a concise transparency note referencing Parslow's Nov 21, 2026 unverified claim (`mylesparslow-collab.github.io/demos/conjecture-ledger/#b-36`, no public proof published). *(If `@coordinator` prefers an ultra-conservative policy excluding any target with an unverified prior claim on a public webpage, this record documents the exact basis.)*
