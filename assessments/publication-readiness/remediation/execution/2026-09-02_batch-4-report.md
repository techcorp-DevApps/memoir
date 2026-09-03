# Batch 4 — Execution Report

**Scope**: REM-015, REM-022, REM-025 (master plan §Batch 4). Carried forward from Batch 3: B39-followup, REM-036.
**Closure rule applied**: every file an item touches opened and verified this session; unopened = PARTIAL, never DONE.

---

## REM-015 — Ch.21 line 9 punctuation

- **Files touched**: `chapters/21_TheFrenchChef.md` (read), `assessments/.../chapters/2026-09-02_150000_21_the-french-chef_remediation-plan.md` (read), `assessments/.../execution/2026-09-02_150000_publication-remediation_execution-matrix.md` (edited, row 41).
- **Evidence**: `21_TheFrenchChef.md:9` — "I'd left a CDC position at a modern bistro, hundred and fifty covers, double sittings, fifteen-plus staff under me, a beast by any definition, to take a pay cut..." — commas present, parses cleanly. Chapter plan `:10` already recorded DONE. Matrix row 41 still read `PLANNED` — stale record, not stale manuscript.
- **Status**: **DONE.** No manuscript edit needed (already correct). Fixed the matrix row only.
- **Blocker**: none.

## REM-022 — Ch.07 closing-three-paragraphs register shift

- **Files touched**: `chapters/07_Chicken&Mash.md` (read, **unedited**), chapter plan 07 (edited), matrix row 40 (edited), ledger B41 (added).
- **Evidence**: Ledger B34 cleared the REM-021 dependency. Put to Bosco 2026-09-02; **he elected to leave the close as written** — recorded at ledger B41.
- **Status**: **DONE — NO ACTION.** Chapter unchanged. Plan and matrix both now say "do not re-flag".
- **Blocker**: none.

## REM-025 — Ch.08 "months passed" opening

- **Files touched**: `chapters/08_EarningTheRight.md` (read, **unedited**), chapter plan 08 (edited), matrix row 42 (edited), ledger B42 (added).
- **Evidence**: Put to Bosco 2026-09-02; **he elected to leave the opening as written** — recorded at ledger B42. Each flagged line is a topic sentence answered immediately by hard specifics.
- **Status**: **DONE — NO ACTION.** Chapter unchanged. Plan checklist item ticked as *explicitly declined*, which is what it asked for.
- **Blocker**: none.

## B39-followup — naming Ivian at ch.03:215

- **Files touched**: `chapters/03_FreshForUnlock.md:215` (**edited**), `chapters/04_FourFlights.md:11` (**edited**), `CLAUDE.md:220` (edited), `context/canon.md:23` (edited), ledger B39 (followup resolution added), matrix row 37 (edited), chapter plans 03 and 04 (edited).
- **Bosco's ruling**, in his words: the wing-cleaning scene in ch.04 happens *after* the move into Ivian's cell, so the naming belongs at the earlier point — *"there was a spare bunk in my mate Ivians cell and he had a TV"*, with the later reference dropping the name so it becomes simply *"my celly"*.
- **Executed**: `03:215` — "But my mate had a spare bunk in his cell." → **"But there was a spare bunk in my mate Ivian's cell."** The "And a TV." beat and the "So I got myself moved to his house instead." close are untouched. `04:11` — "Ivian, my celly, was out in the yard." → **"My celly was out in the yard."** He is still named at `04:157`.
- **Status**: **DONE.** This supersedes REM-017's interim ch.04 clause — the gap is now closed by the ch.03 naming. Both chapter plans and matrix row 37 record the supersession so a later batch reads it as a ruling, not drift.
- **Blocker**: none.

## REM-036 — evidence standard for the two `CLAUDE.md` canon facts

- **Files touched**: `CLAUDE.md:220` and `:263` (read; `:220` separately edited under B39-followup), `governing/...:20` (read), master plan `:560-561` (read), matrix rows 1 and 19 (edited), ledger B43 (added).
- **Evidence**: Master plan `:561` permits facts "explicitly confirmed by Bosco **or** directly sourced from approved manuscript text"; governing plan `:20` states "Ivian: already given, no further confirmation needed." Matrix row 19's validation column was the only document reading that `or` as an `and`.
- **Bosco's ruling** (ledger B43): the `or` reading is correct. Rows 1 and 19 close **DONE**, and row 19's validation wording was corrected to match the two plans rather than left for a later batch to re-trip over.
- **Status**: **DONE.** Both facts stand as already written; nothing was fabricated and nothing was needed.
- **Blocker**: none.

---

## Inverse-check (Batch 3 items re-verified this session)

Spot-checked REM-021 (matrix row 2/39, chapter plan) and REM-016 (row 38) against file state — both correctly DONE, nothing found mismarked open.

---

## Decisions taken (2026-09-02)

All four open items were put to Bosco and answered in the same session. Ledger keys B41, B42, B43, and the B39 followup carry the rulings.

| Item | Ruling | Manuscript effect |
|---|---|---|
| REM-022 | Leave the ch.07 close as written | None |
| REM-025 | Leave the ch.08 opening as written | None |
| B39-followup | Name Ivian at `03:215`; thin `04:11` to "my celly" | Two lines, both to Bosco's own wording |
| REM-036 | Confirm the `or` evidence standard; rows 1/19 DONE | None |

**Nothing in Batch 4 remains open.**

---

## Inherited defect found and corrected — line citation `03:213` → `03:215`

Every governing file cited the spare-bunk line as `03_FreshForUnlock.md:213`.
It is at **`:215`**; `:213` is "I couldn't be associated with that." The
miscitation predates this batch — it is wrong in `origin/main` too — and came
in with ledger B39 on 2026-09-02.

Corrected in the live governing files this batch already had open: `CLAUDE.md`,
`context/canon.md`, the ledger, the execution matrix, and the 03/04 chapter
plans. **Dated point-in-time records were left alone** — the Batch 3 QC report
and the 2026-09-01 assessments correctly describe what they saw when written.

Not rework, per the batch rule on inherited defects: a note with routing. It is
recorded here rather than silently carried, because the naming ruling above
makes that line a canon anchor and a wrong ref would be re-copied forward.
