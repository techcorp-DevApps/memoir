---
artifact: manuscript-audit
date: 2026-08-30
scope: full read of every file in chapters/ and drafts/, cross-checked against
  CLAUDE.md, README.md, context/project-memory.md,
  planning/manuscript-structure_v1.3.0.md, planning/writing-plan_v1.3.0.md,
  planning/next-session-kickoff.md, planning/register-patch-family.md,
  interviews/jackson/CORRECTION-LEDGER.md, interviews/return-to-yulara/*
status: FLAGGED — nothing resolved. Every item below is Bosco's call.
baseline: project-knowledge snapshot of TechCorp-DevApps/memoir
---

# Manuscript audit — current state vs. what the core files say

Read end to end this session: all 21 files in `chapters/`, both files in
`drafts/`, and every planning, context and interview document in the synced repo.
Nothing here has been corrected in place. Conflicts are recorded and routed.

**Measurement note.** `corpus_stats.py`, `voice_check.py`, `manuscript_status.py`
and `encoding_check.py` did not run — the repo is not on disk on this surface,
only in project knowledge. Encoding findings below come from reading the byte
sequences directly and are reliable. Word counts are **not** reported; the only
figure in the repo is `next-session-kickoff.md`'s 23,167 across 21 chapter files,
which is a recorded number, not one measured here.

---

## 1. What actually exists

### `chapters/` — 21 files, gaps at 05 and 06

| File | Title as written in the file | State |
|---|---|---|
| `01_CatchYaOnTheFlipSide.md` | CATCH YA ON THE FLIPSIDE | full chapter |
| `02_MagicTrick.md` | MAGIC TRICK | full chapter |
| `03_FreshForUnlock.md` | FRESH FOR UNLOCK (+ `# GENERAL POPULATION` as a second H1) | full chapter |
| `04_FourFlights.md` | FOUR FLIGHTS | full chapter |
| — | **05 — no file** | gap |
| — | **06 — no file** | gap |
| `07_Chicken&Mash.md` | CHICKEN AND MASH | full chapter |
| `08_EarningTheRight.md` | EARNING THE RIGHT | full chapter |
| `09_SetUpYoutStation.md` | SET UP YOUR STATION | full chapter — **ChefTip #11** |
| `10_FatSam.md` | FAT SAM | full chapter |
| `11_TheOnion.md` | THE ONION WILL NOT WAIT FOR YOU | full chapter — **ChefTip #10** |
| `12_TheStockPot.md` | NEVER TAKE YOUR EYES OFF THE STOCKPOT | full chapter — **ChefTip #9** |
| `13_HotTrays.md` | HOT TRAYS DON'T ANNOUNCE THEMSELVES | full chapter — **ChefTip #8** |
| `14_TheOnesWhoStay.md` | THE ONES WHO STAY | full chapter |
| `15_TasteIt.md` | TASTE IT | full chapter — **ChefTip #7** |
| `16_TwoGlasses.md` | TWO GLASSES ON THE PASS | full chapter |
| `17_ProductionKitchen.md` | PRODUCTION KITCHEN | full chapter |
| `18_TheBaseline.md` | THE BASELINE | full chapter — **ChefTip #6** |
| `19_CoastOrClimb.md` | COAST OR CLIMB | full chapter |
| `20_Goose&Gander.md` | GOOSE & GANDER | full chapter — **ChefTip #5** |
| `21_TheFrenchChef.md` | THE FRENCH CHEF IN AN ITALIAN KITCHEN | full chapter |
| `22_Dave.md` | — | one-line placeholder |
| `23_ReturnToYulara.md` | — | one-line placeholder |

### `drafts/` — 2 files, plus the one filed this session

| File | State |
|---|---|
| `TheEarlyDays.md` | Draft v0.1, Dec 2025. Eight titled movements: CONCURRENT / HIGH RISK OF REOFFENDING / THE WOMAN WHO CHOSE COOKING / FIRST DAY / THE CLOWN SUIT / EVERY SUNDAY / THE GRIND / GRANT'S KITCHEN. **Superseded in part and factually stale — see §3.1.** |
| `04_TitleToBeConfirmed.md` | Draft v0.1, Jan 2026. Superseded by `chapters/04_FourFlights.md`. |
| `YULARA_ReturnToYulara_v1.0.md` | **Filed this session.** See §5. |

### ChefTip ladder — measured against the chapters, not the tables

Placed and written: **#11, #10, #9, #8, #7, #6, #5** — seven tips, all in files.
Unwritten: **#4, #3, #2** (no topic settled) and **#1** (topic settled — "Make
time for the people who matter" — but **no file anywhere in the repo**).

`08_EarningTheRight.md` promises the reader *"Ten ChefTips. I'll even give you one
for free"* — eleven total. That is consistent with the #11→#1 ladder. No defect.

---

## 2. Core files vs. reality — discrepancy register

### 2.1 `CLAUDE.md`

| # | What it says | What the repo shows | Route |
|---|---|---|---|
| C1 | § 3 lists **TITLE TBC — ✓ Draft v0.1** and **TITLE TBC — not started** | Chapter 04 is written, titled **FOUR FLIGHTS**, and promoted to `chapters/`. Chapters 02 and 03 are also promoted full chapters. | Update § 3 |
| C2 | § 3 marks MAGIC TRICK **✓ complete** and FRESH FOR UNLOCK **✓ Draft v0.4**; § 3 *Active Development* then marks MAGIC TRICK **✓ Draft v0.4** and FRESH FOR UNLOCK **In progress** | The same file contradicts itself in two adjacent sections. Both are promoted chapters. | Update § 3 |
| C3 | § 3 *Placeholders*: "RETURN TO YULARA — placeholder, **not yet scoped**" | Scoped across 11 transcript segments; drafted to v1.0. | Update § 3 |
| C4 | § 3 marks **I CAN COOK BETTER THAN YOU**, **THE PEOPLE WHO LAUGH WHILE YOU'RE DROWNING** and **YOU'RE ONLY AS GOOD AS YOUR LAST SERVICE** ✓ Complete | **No file for any of the three.** Confirmed against all 21 chapter files. Pre-existing defect, already recorded in `next-session-kickoff.md`. | Bosco — written elsewhere, or is the mark wrong? |
| C5 | § 5 **Rachael** — CDP (Italian), Joe's missus | `21_TheFrenchChef.md` names her **Carly**, twice. | **Fact in dispute.** Bosco decides which name stands. |
| C6 | § 5 **Jen** — commis (Bistro) | `manuscript-structure_v1.3.0.md` says **CDP**. `19_CoastOrClimb.md` gives her no rank — only that she transferred from the main-kitchen commissary. | Two planning docs disagree; the manuscript is silent. Bosco decides. |
| C7 | § 9 repository tree shows `/manuscript/part-1-origin/…` etc. | No such directory. Content lives in `/chapters/`. Phantom tree. | Replace § 9 |
| C8 | § 12 repository `https://github.com/lufp005x/memoir.git` | Project of record is `TechCorp-DevApps/memoir`. | Bosco confirms which is current |
| C9 | Header: *Current Version v1.3.0 (~18,500 words)*; footer: *Last updated January 2026 / Version 1.0.0* | Word count contradicts `next-session-kickoff.md` (23,167). Version line contradicts the header. | Update both |
| C10 | § 5 Family block and § 6 Jackson rows are present | Good — the `register-patch-family.md` edits **are** applied in the synced copy. `next-session-kickoff.md` still lists this as an uncommitted blocker. | Kickoff is stale on this point |

### 2.2 `README.md`

| # | Issue |
|---|---|
| R1 | Word count **~18,500**, editorial score **94/100**, version **1.3.0** — all carried over from CLAUDE.md and all now behind the repo. |
| R2 | Repository tree lists `/README.md/` as a directory. Typo. |
| R3 | Structure section describes **PART SIX: EXIT — "Final chapter"**, singular. Superseded by this session's ruling (see §4). |

### 2.3 `context/project-memory.md`

| # | Issue |
|---|---|
| P1 | "currently v1.3.0, ~18,500 words … 94/100" — same stale figures. |
| P2 | "Work continues on **THE LIBRARY** chapter about the friendship with Dave, with multiple iterations…" — `22_Dave.md` is a one-line placeholder. No iterations exist in the repo. |
| P3 | Lists **Chef Gavin** as a mentor. `17_ProductionKitchen.md` and `19_CoastOrClimb.md` render him as the exec chef who set the bistro as a test. Not wrong, but thinner than the chapters. |
| P4 | ChefTip timeline says "**ChefTips #2-6**" outstanding. #6 and #5 are written and in files. Should read #4, #3, #2, #1. |
| P5 | A second copy of this file exists at repo root as `project-memory.md`. Two paths, one subject. Confirm which is authoritative. |

### 2.4 `planning/next-session-kickoff.md`

Accurate on almost everything, and its three headline claims verify:

- **21 chapter files, gaps at 05 and 06** — confirmed.
- **Fifteen chapters carry inherited mojibake** — confirmed exactly (see §3.2).
- **Three sections ✓ Complete with no file** — confirmed (§19, §20, §23 of the
  structure doc).

Two items are now stale: the register patch **is** applied in the synced
`CLAUDE.md` (C10), and RETURN TO YULARA is no longer unscoped.

---

## 3. Defects found in the manuscript itself

### 3.1 `drafts/TheEarlyDays.md` contradicts settled canon

The CONCURRENT movement reads:

> *"The main charges alone carried a maximum of eight years. **I was
> twenty-three.**"*

`CLAUDE.md` § 6 fixes age at sentencing at **19**, and `writing-plan_v1.3.0.md`
Key Decision 2 records the correction explicitly: *"19 at sentencing, not 23."*
`chapters/01_CatchYaOnTheFlipSide.md` carries the corrected version.

Two further conflicts in the same file:

- *"every Sunday in jail. Both times … for an hour **behind glass** with me"* —
  `04_FourFlights.md` establishes the glass hall was still under construction and
  the visits happened **in the gymnasium**, sitting together.
- The parole-board scene appears in both `TheEarlyDays.md` and
  `04_FourFlights.md`, with different endings.

**Routing:** this is a pre-correction draft that the promoted chapters have
overtaken in its first third. It still holds the **only** copy of the parole
officer, culinary school, Wüsthof knives, focaccia, City and Guilds and Grant's
kitchen material — which is chapters 05 and 06 in file terms. Suggest splitting
it rather than archiving it whole. **Not done here.**

### 3.2 Encoding — fifteen chapters, exactly as recorded

`â€"` for em dash throughout, plus `Ã¡`/`Ã©`/`Ã¯` forms. Present in:

`07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21`

**Clean:** `01, 02, 03, 04`, both existing drafts, `22`, `23`, and the new
`YULARA_ReturnToYulara_v1.0.md`.

The two artefacts `next-session-kickoff.md` calls unrecoverable are confirmed:
the `Ã  la carte` line in `21_TheFrenchChef.md`, and the mangled H1 of
`context/chef-writer-context-profile.md`.

**Inherited defect, not introduced.** Scoped `formatting-agent` pass, on your
approval of the scope.

### 3.3 Filename typo

`chapters/09_SetUpYoutStation.md` — **Yout** should be **Your**. Renaming it is a
git mv and a reference sweep; nothing in the manuscript body points at it.

### 3.4 `03_FreshForUnlock.md` carries two H1s

`# FRESH FOR UNLOCK` and, two-thirds through, `# GENERAL POPULATION`. Every other
chapter file has exactly one H1. Either it is one chapter with an internal
divider that should drop to `##`, or it is two chapters — which would fill the
**05** gap. Your call.

### 3.5 Chapter 04 diverges from its own editorial review

`reviews/drafts/04_FourFlights.md` scored the draft 82/100 and named the closing
lines *"Same board. Same day. Different histories."* as strong and to be kept
as-is. The promoted chapter **drops the Ivian parole-outcome close entirely**,
reorders the parole board ahead of the Stacey section, and ends on Stacey.

The review's other four corrections **were** applied — the Jay backstory
repetition is gone, the stakes paragraph is condensed to the exact line the
review suggested, the letter description is tightened verbatim as suggested, and
the fear distinction is rendered rather than named. So the divergence looks
deliberate. Recorded so it is not mistaken for a regression. The review also
recommended **PERMISSION** or **DIFFERENT HISTORIES** as titles; the chapter went
with **FOUR FLIGHTS**, which was on the review's list.

### 3.6 The narrator is named on the page once

`17_ProductionKitchen.md`: *"G'day, mate. You must be **Chris**."* This is the
only place in 21 chapters where the narrator is named. It sits inside the open
naming-policy question already flagged for venues, family and the German GM.

---

## 4. The ruling recorded this session

Bosco, 30 August 2026:

1. **Chapter 23 is not the hard end.** The manuscript has an **adaptive endpoint**
   that will arrive naturally. No fixed chapter count, no fixed close.
2. **The ChefTip ladder will very likely close before the manuscript does**, as
   the career writing closes — with several chapters still to go after it.

This confirms and now **authorises** the ruling recorded in
`interviews/return-to-yulara/BRIEF.md`, which raised the same point but was
explicitly barred from writing it into the planning documents. That bar is lifted
for the writing plan.

**Consequences, applied in `writing-plan_v1.4.0.md`:**

- PART SIX is no longer "EXIT — final chapter".
- §23 **YOU'RE ONLY AS GOOD AS YOUR LAST SERVICE** / ChefTip #1 is no longer the
  terminal row.
- The six-venue post-Melbourne arc from the scope interview enters the plan as a
  part in its own right, **without chapter numbers**.
- ChefTips #4, #3, #2, #1 are released from their provisional Melbourne /
  retrospective slots and become placeable anywhere up to the close of the career
  arc.

**Deliberately not done:** the plan-section ↔ filename renumbering. That is a
decision, not a cleanup, and `next-session-kickoff.md` correctly defers it until
the post-Melbourne stretch is scoped. `manuscript-structure_v1.3.0.md` is
therefore now one version behind the writing plan — see §6.

---

## 5. `YULARA_ReturnToYulara_v1.0.md` — filed, with notes

**Written to:** `drafts/YULARA_ReturnToYulara_v1.0.md`

Not `chapters/23_ReturnToYulara.md`. Only Bosco promotes into `chapters/`, the
chapter number is unassigned, and the handover records that this material may be
**one chapter or three**. The placeholder at `chapters/23_ReturnToYulara.md`
stands untouched.

Checked against `transcript.md` segment by segment: **no invented specifics.**
Every dish, name, quoted line and setting detail traces to a segment. The
outstanding-dishes gap is marked in the draft as a gap, not filled. The
"for reasons I'd find out later" hook is left unresolved, as instructed. Jackson
is born in it and does not die in it; no foreshadowing was added.

Mechanical notes (my own count, not `voice_check.py`): 1,962 words total, ~1,496
of body. **No mojibake — the file is clean UTF-8.** Profanity ≈ 7.4 per thousand
body words, inside the corpus range of 0.00–16.13. Paragraph density ≈ 36%
single-sentence, ≈ 15 mean paragraph words — inside the bands quoted in flag F16,
which corroborates the v1.0 re-clustering claim.

Three front-matter references point at files not present in the synced snapshot:
`drafts/YULARA_ReturnToYulara_v0.9.md`, `reviews/drafts/Return-to-Yulara-v0.8.md`,
and `chapters/20_Goose_Gander.md` — the last is a path mismatch for the real
`chapters/20_Goose&Gander.md`. The first two are most likely a sync gap rather
than missing work.

**The draft's own FLAG REGISTER carries 13 open items.** Two are marked *Needs
ruling* and block promotion:

- **F6** — `fuken` vs `fucken`. v0.9 silently resolved CORRECTION-LEDGER DECIDE #4
  and v1.0 kept it. Confirm or revert. (Body prose uses `fucken`; the only `fuken`
  left in the file is inside F6's own description of the problem.)
- **F16** — rhythm. v1.0 re-clustered to corpus density. If the staccato in v0.9
  was a deliberate choice for this chapter, say so and it reverts.

---

## 6. What is now inconsistent by design

`planning/writing-plan_v1.4.0.md` carries the adaptive-endpoint ruling.
`planning/manuscript-structure_v1.3.0.md` does not — it still closes at #23 with
EXIT as the final part, and still carries the provisional `21a` row for RETURN TO
YULARA.

That gap is intentional and one instruction away from closing: bringing the
structure doc into line means touching the numbering, and the numbering is your
decision. Say the word and it becomes v1.4.0 to match.

---

## 7. Decisions waiting on you

**Blocking the Yulara draft:**

1. F6 — `fuken`/`fucken` ruling (and the other 10 DECIDE items in the ledger).
2. F16 — rhythm: keep v1.0's clustering or revert to v0.9's staccato.
3. One chapter or three?
4. Naming policy — venues, people, and the German GM who is identifiable by role
   and nationality even unnamed.

**Blocking the plan:**

5. Do §19, §20 and §23 have files somewhere outside the repo, or is the ✓ wrong?
6. Plan-section ↔ filename renumbering — and whether `manuscript-structure` gets
   brought to v1.4.0 now or after.

**Facts in dispute — not resolved here:**

7. **Carly** vs **Rachael** (chapter beats CLAUDE.md, but it is your call).
8. **Jen** — commis or CDP.
9. `drafts/TheEarlyDays.md` — split into 05/06 and retire the stale first third,
   or supersede whole?
10. `03_FreshForUnlock.md` — one chapter or two?

**Still open from earlier sessions, untouched:**

11. Year of Jackson's death — not established, not derivable.
12. Where the Stacey → Tegan handover of Jackson's care sits.
13. Naming on the page — full names vs the lower-case `tee`/`jacks`/`madz`.
14. Encoding repair scope — fifteen chapters, plus the two unrecoverable
    artefacts.

---
*End of audit. Nothing above was applied to the manuscript.*
