---
artifact: decision-ledger
date: 2026-08-30
status: OPEN — 33 blockers (B30–B33 added), 20 answered — B10 CLOSED, B30 settles the book's shape end to end
title: THE BOOK IS NOW "THE LONG ROAD TO NOWHERE" — see B28
rule: one at a time. Answer with the key. Nothing is resolved by any role.
source: reviews/manuscript-audit_2026-08-30.md § 7, and the FLAG REGISTER in
  drafts/YULARA_ReturnToYulara_v1.0.md
---

# Decision ledger — 30 August 2026

> **B28 · BOOK TITLE — ANSWERED.** The book is **The Long Road To Nowhere**.
> Was *Diary of a Chef*. PART ONE carried that name and now needs a new one.
> Title sweep and the full source-recovery analysis:
> `reviews/source-recovery-assessment_2026-08-30.md` (B25–B28 live there).

Every open decision in the repo, keyed. Answer with a letter. Where a key is
marked **(repo)**, that option matches what the manuscript already does.

Status: `OPEN` / `ANSWERED: <key>` / `DEFERRED`

---

## TIER 1 — blocking the Yulara draft

### B1 · `fuken` vs `fucken` — FLAG F6 / LEDGER DECIDE #4 · **ANSWERED: A** · 2026-08-30

v0.9 normalised the transcript's `fuken` to `fucking`/`fucken`. v1.0 kept it.
That silently resolved an open ledger item. Confirm or revert.

| Key | Ruling |
|---|---|
| **A** | `fucken` is house spelling everywhere. Normalise the Jackson source copy to match. **(repo — 7 attested uses across approved chapters)** |
| **B** | `fucken` in the memoir; `fuken` preserved only in the Jackson chapter, as its own register |
| **C** | `fuken` everywhere — the corpus form is the error |
| **D** | Leave both, per-file, never normalise |

**RULING — A.** `fucken` is house spelling. The Jackson chapter copy normalises to
it when drafted. `interviews/jackson/SOURCE-VERBATIM.md` stays `LOCKED — VERBATIM`
and is never edited — the correction lives in the derived chapter.

**Effects:**
- `CORRECTION-LEDGER.md` DECIDE #4 → **CLOSED**. Move it to the APPLY list.
  Counts become **35 APPLY, 19 HOLD, 10 DECIDE**.
- `fucken` stays on the protected list in `memoir_lib.py` `ATTESTED_FORMS`.
  `fuken` is no longer a protected form — it is a correctable spelling.
- Yulara draft **F6 → RESOLVED**. Body prose already reads `fucken`; the retained
  `fuken` in F6's own description is commentary, not prose. No re-write needed.
- Any QC finding against `fucken` remains a false positive.

#### B1a · the other 10 DECIDE items · OPEN — answer after B1

`mail break`→`jail break` · `I look at home`→`him` · `we the fuck`→`where` ·
`bought along`→`brought` · `the shrills of` · missing `I` in *"To give things some
context need to go back"* · `something I was made proud of` · `we hug and thank
him` person-slip · `madz` vs `mads` · numerals (`5 maybe 6`) vs spelled out.

| Key | Ruling |
|---|---|
| **A** | Fix all ten. Meaning is obvious in every case |
| **B** | Fix none. They are his hand |
| **C** | Walk them one by one |

---

### B2 · Rhythm — FLAG F16 · **ANSWERED: A** · 2026-08-30

v0.9 measured 97.5% single-sentence paragraphs / 6.0 mean paragraph words.
Corpus band is 29.5–85.79 / 7.73–27.6. v1.0 re-clustered to ~36% / ~15 —
inside the band — keeping v0.9's diction and beats.

| Key | Ruling |
|---|---|
| **A** | Keep v1.0. The staccato was drift, not choice **(repo — matches Ch19/20 density)** |
| **B** | Revert to v0.9. The staccato was deliberate for this chapter |
| **C** | Split the difference — staccato for the bistro/Lewis escalation, clustered for the flagship and tasting |

**RULING — A.** v1.0's paragraphing stands. The staccato was drift, not a chapter
choice.

**Effects:**
- Yulara draft **F16 → RESOLVED**. No v1.1 required on rhythm grounds.
- The corpus band stays a live gate for this chapter — `voice_check.py` findings
  against paragraph density are real findings here, not false positives.
- v0.9 is superseded on rhythm as well as diction. Nothing to retrieve from it.

**Both blocking flags on `YULARA_ReturnToYulara_v1.0.md` are now cleared.** What
remains on that draft is scope, not rework: B3 (split), B4 (naming), B5 (dishes),
B6 (spellings), B7, B8.

---

### B3 · One chapter or three — FLAG F1 · **ANSWERED: A** · 2026-08-30

The material splits cleanly at three seams: the return + bistro absorption / the
noodle bar / the flagship + tasting.

| Key | Ruling |
|---|---|
| **A** | One chapter. The accretion of load *is* the shape |
| **B** | Three chapters. Each seam is its own arc |
| **C** | Two — bistro + noodle bar together, flagship + tasting separate |
| **D** | Decide after the tenure's end is scoped (Segment 11 onward) |

**RULING — A.** One chapter. The accretion of load is the shape and the seams stay
internal.

**Effects:**
- **F1 half-resolved**: the one-or-three question is closed. The **chapter number**
  remains unassigned and still waits on B11.
- The material from Segment 11 onward — what follows the tasting, how the tenure
  ended — **extends this same file**. It does not become a new chapter.
- Expect the finished chapter to run long against the corpus. That is a
  consequence of this ruling, not a defect; QC should not flag length here.
- The three seams stay as section breaks (`---`) inside the chapter, as drafted.
- Working stem stays `drafts/YULARA_ReturnToYulara_v{X.Y}.md` until you promote it
  and drop the version suffix.

---

### B4 · Naming policy — FLAGS F2, F3, F14 · **ANSWERED: A / A / A** · 2026-08-30

Three sub-rulings. Answer as `B4: A/B/A` etc.

**B4.1 — venues.** Yulara, Sails in the Desert, Lasseters, Park Hyatt Saigon,
World, The Boathouse, Mr Masons.

| Key | Ruling |
|---|---|
| **A** | Real names throughout |
| **B** | Real names for places, invented for the businesses |
| **C** | All renamed |

**B4.2 — colleagues.** Brett, Lewis, Hebe, Number 8, Philippe Michelle.

| Key | Ruling |
|---|---|
| **A** | First names as given **(repo — Fat Sam, Kein Do, Gavin, Joe, Matt all stand)** |
| **B** | First names changed, roles kept |

**B4.3 — the German GM.** Unnamed in the draft, but identifiable by role +
nationality, and the scene is unflattering.

| Key | Ruling |
|---|---|
| **A** | Stands as written. He was there |
| **B** | Drop the nationality, keep "Ma'am" and the role |
| **C** | Drop role or nationality — make her unidentifiable |
| **D** | Route to a publishing lawyer before the manuscript goes out |

**RULING — A / A / A.** Real venue names, real first names, the GM scene as
written. It happened and it goes on the page.

**Effects:**
- **F2, F3, F14 → RESOLVED.** Naming is now settled policy for the whole
  post-Melbourne arc, not just this chapter.
- Consistent with the 21 approved chapters, which already carry real first names
  throughout. No retro-sweep needed.
- `Kuniya`, `Hebe`, `Philippe Michelle`, `black onyx` are still **spelling**
  questions, not naming ones — they stay open under **B6**.
- Applies forward to Lasseters, Park Hyatt Saigon, World, The Boathouse and
  Mr Masons as those venues get scoped. No re-litigating per chapter.

**Recorded, not a block.** A/A/A is the highest-exposure combination available:
real employer + real first names + an identifiable executive in an unflattering
scene. That is a legitimate memoir choice and it is yours. It is worth a
publisher's legal read before the manuscript goes out — not a rewrite, a read.
Noted here so the decision is on the record as made deliberately, and so nobody
re-opens it later as if it were an oversight.

---

## TIER 2 — Yulara, lower cost

### B5 · Flagship menu dishes — FLAG F11 · **ANSWERED: B** · amended 2026-08-30
**RULING — B, superseding the earlier A.** *"Will provide this as part of next
interview phase as planned."* Collected when the interview resumes at Segment 11,
alongside the tenure's end and §1a. **F11 stays open until then.**

The three on record — Black Onyx trio, Keller tomato entrée, Alinea banana–duck
amuse — are the floor, not the ceiling (his words, Segment 8). The draft's
`[More dishes on record as offered, not yet collected]` marker **stays in place**
until they arrive.

### B6 · Unverified spellings — FLAGS F9, F10, F13, F15 · **PART-ANSWERED** · 2026-08-30

**RULING.** Fix obvious capitalisation and spelling of real proper nouns; route
anything unsure rather than guessing.

| Item | Outcome |
|---|---|
| `Hebe` | **Confirmed correct.** F9 → RESOLVED |
| `Kuniya` | **Confirmed correct** as spelled. F15 spelling → RESOLVED |
| `black onyx` → **Black Onyx** | Applied. Beef brand, proper noun. F10 → RESOLVED |
| `Philippe Michelle` → **Philippe Mouchel** | **Confirmed 2026-08-30.** F13 → RESOLVED |
| **Mayu** | **NEW.** The flagship restaurant was named Mayu. On record nowhere before today |

**B6a — ANSWERED · 2026-08-30. Kuniya is placed.** It is the **fine-dining
restaurant he transferred into under Kein Do** — the venue of
`chapters/18_TheBaseline.md`, which describes it but never names it. It **closed
before the renovation and kitchen refit**, about **six months after he moved to
Melbourne**. That closure brought **Kein Do and his family to stay with him and
Stacey in Melbourne** while Kein Do made the move to a role at **Crown Casino**.

Captured as § Segment 12b in the addendum. **F15 → RESOLVED.**

Three things it opens, none decided: whether **Mayu** occupies or replaces Kuniya;
whether Kuniya is **named retroactively** in the approved `18_TheBaseline.md`;
whether **Kein Do's departure** goes on a page at all.

**B6b — ANSWERED · 2026-08-30. Philippe Mouchel confirmed.** `Philippe Michelle`
→ **Philippe Mouchel**. **F13 → RESOLVED.**

**B6 is now fully closed.** F9, F10, F13, F15 all resolved. The sister's line in
the tasting scene reads *"a CDP off Philippe Mouchel"* from v1.1 on.

Captured in `interviews/return-to-yulara/transcript-addendum_2026-08-30.md`
§ Segment 12a.

### B7 · "pressure I had experienced before" — FLAG F5 · **OPEN — context supplied**
Bosco asked twice for the full paragraph as written. **Complete Segment 2 of
`transcript.md` reproduced verbatim in chat, 2026-08-30.**

**Material fact for the ruling:** there is no fuller paragraph in the repository.
The transcript preserved this as a **single quoted sentence** with an interviewer's
summary around it; it was never captured as continuous prose. If a longer original
exists it is outside the repo, in the raw session.

**A** insert `never` · **B** as given · **C** cut the line

### B8 · Jackson's placement in the draft — FLAG F12 · **ANSWERED: B** · 2026-08-30

**RULING — B. Expand — and it gets its own chapter as well.** Amended 2026-08-30:

> *"The expansion for the birth can definitely be touched on its own brief chapter
> more after the in-draft Yulara chapter, however it should definitely have more
> inclusion and depth than currently has in the chapter."*

**Two things, not one:**

1. **Inside the Yulara chapter** — the birth beat grows beyond its current three
   sentences. More inclusion, more depth. It does not stay a throwaway.
2. **A new brief chapter immediately after it** — §1a in the post-Melbourne arc,
   carrying the material that does not belong inside a chapter about workload.

Original rationale: *"an important milestone and there is actually valuable weight
the context contains which will only increase the ability to visualise the scene
when reading."*

**New material given, captured as Segment 12** in
`interviews/return-to-yulara/transcript-addendum_2026-08-30.md`: Stacey heavily
pregnant, on a milk crate in the kitchen, eating after her own work and before
dinner service — the only way she got to see him in the weeks either side of the
opening. Stewards spotting her and running to announce her. **Navi**, his CDP,
starting her dinner unasked. Her pride in his standing in that room.

**Effects:**
- **F12 half-resolved.** Placement settled; the **chronology conflict** in
  `BRIEF.md` and the **Stacey → Tegan handover** stay open (B17).
- **New character: Navi**, CDP at the flagship. Needs a `CLAUDE.md` § 5 row.
- **New chapter §1a** added to `writing-plan_v1.4.0.md` Part Five. Title TBC, no
  number (waits on B11), **no ChefTip** — a life chapter inside a career arc, same
  as the origin arc.
- Requires **v1.1** of the Yulara draft. Bundled with B5's dishes so it is one
  revision, not two.
- **Boundary unchanged:** Jackson is born in this material and does not die in it.
  No shadow, no foreshadowing, in either chapter. The expansion is warmth, not
  weight. This is a career high with a birth in it, not a set-up for a loss.
- **B3 is not disturbed.** Yulara remains one chapter. §1a is a separate chapter on
  a separate subject, not a split of the Yulara material.
- **"in those few prior to opening"** — probable missing *weeks*. Same class as
  B7, flagged not filled.

#### B8a · Where the seam falls · **ANSWERED: A** · 2026-08-30

**RULING — A. The kitchen stays; the birth carries.**

| Chapter | Takes |
|---|---|
| **Yulara** | The milk crate. Stacey coming in after her own work, before service. The stewards spotting her and running to announce her. **Navi** starting her dinner unasked. Her watching him work, and her pride in it. All of it kitchen-set, in a kitchen chapter |
| **§1a** | Alice Springs. The birth. What it meant |

**Consequence — §1a has almost no material yet.** Everything on record for it is
two lines in Segment 7: *born in Alice Springs, the nearest city, while living at
Yulara; birth year 2013*. Under ruling A the warm, concrete material stays in
Yulara, which is right for Yulara and leaves §1a with a fact and no scene.

**§1a therefore needs its own scope interview before it can be drafted.** It is
not a writing task yet. Do not draft it from the Yulara material — that would
either duplicate the kitchen beats or invent the Alice Springs ones.

Open questions §1a will need answered, recorded so the interview has a spine — **not
to be filled by any role**: the drive or flight to Alice Springs and who made it;
whether he was there; who covered the pass; what he went back to and how fast;
what he told the kitchen; the first time he saw Jackson; what Stacey said. **None
of this is on record. Do not infer any of it.**

### B9 · Resume the scope interview · OPEN
Paused at Segment 11. Outstanding: what follows the tasting, how the tenure ended.
**A** resume now · **B** after Tier 1 is cleared

---

## Pending v1.1 of the Yulara draft

Accumulated from the rulings above. **One revision, not five.** Not yet produced —
waiting on B5's dishes so the draft is opened once.

| From | Change |
|---|---|
| B6b | `Philippe Michelle` → **Philippe Mouchel** |
| B6 | `black onyx` → **Black Onyx** (both occurrences) |
| B6a | **Mayu** — the flagship is named. Placement on the page still open |
| B8 / B8a | Expand the birth beat: milk crate, Stacey after her own work, stewards announcing her, **Navi** starting her dinner, her pride in watching him. Birth event itself carries to §1a |
| B1 | `fucken` confirmed as house spelling — body prose already complies, no change |
| B2 | Rhythm confirmed — no change |
| B5 | Flagship dishes, **when supplied**. The `[More dishes…]` marker stays until then |
| B7 | **Unresolved.** Line is not in v1.0 and stays out unless ruled A or B |

Front-matter also needs correcting on the next pass: `continuity_read` points at
`chapters/20_Goose_Gander.md`; the real file is `chapters/20_Goose&Gander.md`.

---

## TIER 3 — blocking the plan

### B10 · Three sections marked ✓ Complete with no file · **ANSWERED: C-variant** · 2026-08-30

**RULING.** Not missing — **renamed, repositioned, or integrated** after draft
completion. Bosco will temporarily re-open the repo to public, re-check what
reached the project-knowledge sync, and push the work done here back to the repo.
If anything genuinely is absent, it may be on disk and he uploads it.

**Action is his, not a role's.** Nothing is marked unwritten on the strength of
this session's read.

**Blocking note:** until that re-sync lands, the repo state this session audited is
the best available but **not authoritative** on these three sections.

**SETTLED 2026-08-30 by direct repo access.** Full clone, history unshallowed,
**79 commits** read. Result:

**None of the three has ever existed in this repository.** Not under those names,
not renamed, not deleted. `git log --all --diff-filter=A` lists every path ever
added; none of them appears. A full-text search across every file for
*I CAN COOK BETTER*, *LAUGH WHILE* and *LAST SERVICE* returns nothing.

**My earlier §20 → `14_TheOnesWhoStay.md` hypothesis is withdrawn.** The rename
chain is `12_TheOnesWhoStay.md` → `14_TheOnesWhoStay.md`, and it carried that title
from creation. It was never *The People Who Laugh While You're Drowning*.

## ✅ B10 CLOSED — all three found. The ✓ marks were right.

Bosco surfaced **"DIARY OF A CHEF — Restructured Draft v1.2.0, December 2025"**.
All three sections are in it, complete, in the order both planning documents give.
They were written and then **never committed to git**.

| Section | Recovered to |
|---|---|
| §19 I CAN COOK BETTER THAN YOU | `drafts/19_ICanCookBetterThanYou_v1.2.0.md` |
| §20 THE PEOPLE WHO LAUGH WHILE YOU'RE DROWNING | `drafts/20_ThePeopleWhoLaugh_v1.2.0.md` |
| §23 YOU'RE ONLY AS GOOD AS YOUR LAST SERVICE | `drafts/23_YoureOnlyAsGoodAsYourLastService_v1.2.0.md` — **truncated, see B31** |

All three are **transcribed from a chat paste, not byte-verified.** Upload the
v1.2.0 file and they get replaced with the exact text.

**v1.2.0 also corrects §19 in every way that was flagged:** the father is a
**Cabinet Maker** and the punchline survives; **bbq chicken** and **curried
sausages** are in; *"my boy"* is **"my girl"** — a partner, not a son, which
**closes B26a**; and the blog's ChefTip-origin framing is **gone**, replaced by a
new opening and a bridge into §20 — which **largely dissolves B27**, since there is
no longer a collision with `08_EarningTheRight.md`.

### New blockers from the recovery

**B30 · Does the Jackson material go into §23? — ANSWERED: NO. It comes after.**

> *"The content surrounding the death of Jacks should come after the fact. It will
> allow for the career period and kitchen content to phase out naturally and will
> leave a level of wonder in the reader — perhaps questioning what the reasoning to
> what cost ChefTip #1 so much — and allow for retrospective understanding once
> further reading [is] done. It also removes some pretty heavy content from the
> career [arc], and while in real life it did suffocate it and ultimately result in
> not returning to the industry, I don't want it to take away from the reader."*

**§23 is finished as written.** The withholding is the design, not a gap. The
chapter names the lesson and refuses the story, the reader carries the question,
and the answer arrives later.

**The Jackson material becomes its own section, positioned AFTER §23.**

**Effects — this settles more structure than any other ruling today:**

1. **The book's shape is now known end to end.**
   Part Zero (childhood) → origin arc → career arc → **ChefTip ladder closes at
   §23** → **Jackson, after the ladder** → the close.
   This is exactly the adaptive-endpoint architecture ruled on earlier: the ladder
   ends, the manuscript does not.
2. **§23 is unblocked.** It was gated on the **11 DECIDE items** in
   `interviews/jackson/CORRECTION-LEDGER.md` because it was to host the verbatim
   material. It no longer hosts it. **Those items now gate the Jackson section
   only.** §23 can proceed on its own — it needs B31 (the quote) and nothing else.
3. **Two planning documents are now wrong and must be corrected**, both stating
   the Jackson material belongs *in* #23:
   - `planning/register-patch-family.md` § Structural note
   - `planning/next-session-kickoff.md` § The kickoff prompt
   Superseded by this ruling. Neither is to be quoted as current.
4. **The Yulara boundary holds and gets firmer.** Jackson is born in that chapter
   and does not die in it — no shadow, no foreshadowing. That was already a hard
   boundary; this ruling extends it across the whole career arc. **Nothing in any
   career chapter anticipates the death.** The reader is not being set up; they are
   being left to wonder.
5. **The wonder has to survive the front matter.** A contents page, a blurb or a
   dedication naming Jackson would spend the effect before page one. Worth deciding
   deliberately when the book is assembled. → **B33**

**B31 · The closing Bourdain quote.** Truncated in the paste; needs recovering in
full. If it stays, a real named public figure is quoted in a published memoir —
attribution and permissions are a publisher question.

**B32 · Losses from blog → v1.2.0 in §20.** Two lines were cut that were stronger
in the earlier version. Chef's close went from *"You caught it before I had to.
That's the job."* to *"alright lets go."*, and the chorus lost *"NO, THE OTHER
PAN—USE YOUR FUCKING EYES"* for *"IN THE OPEN YOUR FUCKEN EYES SECTION"*. The
second is arguably more authentic pass-voice; the first reads as a loss. Restore,
or let v1.2.0 stand?

---

### Earlier finding, superseded above — retained for the record

**AMENDED SAME DAY — two of the three are found.** Bosco surfaced the original
pre-memoir blog piece. It contains **§19 I CAN COOK BETTER THAN YOU** (~900 words)
and **§20 THE PEOPLE WHO LAUGH WHILE YOU'RE DROWNING** (~1,400 words), both
complete, neither ever migrated into the repo.

**§23 YOU'RE ONLY AS GOOD AS YOUR LAST SERVICE is still missing** — not in the
repo, not in its history, not in the source. Its ✓ remains unexplained, and it is
the ChefTip #1 host and the Jackson material's destination.

Full analysis: `reviews/source-recovery-assessment_2026-08-30.md`.

### What the repo actually contains — measured, not read

`manuscript_status.py` run against the clone:

- **20 chapter files, 23,129 words.** Not 21/23,167 — that figure in
  `next-session-kickoff.md` counted the uncommitted renames.
- **`chapters/21_dave.md` still exists.** The rename to `22_Dave.md` and the new
  `23_ReturnToYulara.md` placeholder were **never committed**.
- **No `interviews/` directory. No `reviews/qc/`.**
- **`CLAUDE.md` in the repo does not carry the register patch** — zero matches for
  `### Family` or `Jackson`.
- `planning/writing-plan_v1.3.0` has **no `.md` extension**.
- Numbering gaps confirmed at **05, 06**.
- ChefTip coverage confirmed: **#11–#5 done, #4–#1 open.**

**The project-knowledge snapshot is AHEAD of the repo, not behind it.** Everything
this session audited that is missing above was uploaded to the project directly and
never pushed. That inverts the assumption in the project instructions that the
synced repo is the baseline — for these files, it is not.

### Encoding — exact counts, `encoding_check.py`

15 damaged chapter files, as recorded. Issue counts:
`19_CoastOrClimb` 37 · `21_TheFrenchChef` 30 · `18_TheBaseline` 15 ·
`10_FatSam` 12 · `15_TasteIt` 12 · `13_HotTrays` 11 · `17_ProductionKitchen` 11 ·
`14_TheOnesWhoStay` 9 · `16_TwoGlasses` 9 · `12_TheStockPot` 8 ·
`08_EarningTheRight` 7 · `11_TheOnion` 6 · `20_Goose&Gander` 6 ·
`07_Chicken&Mash` 5 · `09_SetUpYoutStation` 2.
Plus **`context/chef-writer-context-profile.md` — 29 issues.**
Clean: `01`–`04`, `21_dave`, both drafts, `context/project-memory.md`.

**Correction to `next-session-kickoff.md`:** it calls two artefacts unrecoverable.
One is not. `21_TheFrenchChef.md:111` reads `"Three tasting, two Ã  la carte on six."`
— `Ã ` is ordinary mojibake for `à` and repairs cleanly. The context-profile header
is the real problem: its `description` still says **'Diary of an Apprentice'**, the
old title, and the file mandates `### ChefTip Number X` while every chapter uses
`## ChefTip #N`.

### B11 · Numbering + `manuscript-structure` · **ANSWERED: A-variant** · 2026-08-30

**RULING.** Align numbering and completed-chapter points into one clear sequence,
**with empty stub files created for intended or currently unwritten chapters** so
the plan and the filesystem show the same shape.

> *"The better option would be to align numbering and completed chapter points to
> ensure clear sequence as it stands with empty stub files with intended or
> currently unwritten chapters included in plan as it stands."*

**And a second thing, which changes the front of the book:**

> *"There is very likely still content even earlier to be included into the writing
> covering early childhood into early teens before incarceration — there is some
> really great content there and brings even more weight to the trajectory."*

Recorded as **B20** below.

**Sequencing — this is the one caution.** B11 and B10 are coupled. Renumbering
21 files while three chapters' existence is unknown risks numbering around content
that already exists under another name, then renumbering twice. The re-sync in B10
is cheap and lands first.

**Order of operations, on your go:**

1. B10 re-sync — establish true repo state.
2. B20 — a scope pass on the childhood block, enough to know roughly how many
   chapters sit at the front. Exact count not needed; a range is.
3. I produce a **renumbering map** (old path → new path), the **stub file
   contents**, and a `git mv` script. You run it — no role renames files in
   `chapters/`.
4. `manuscript-structure` and `writing-plan` both go to **v1.5.0** against the new
   sequence.

**Sequencing decision, handed to Claude and taken 2026-08-30:** accept the repo
access Bosco offered. It collapses steps 1 and 3 into one pass — read true state,
then build the rename map against it. Part Zero (B20) can be sized after; the front
of the book gets a reserved block rather than exact numbers.

---

## TIER 4 — facts in dispute

### B12 · Carly vs Rachael · OPEN
`21_TheFrenchChef.md` says **Carly**, twice. `CLAUDE.md` § 5 says **Rachael**.
**A** Carly — fix CLAUDE.md **(repo)** · **B** Rachael — fix the chapter ·
**C** neither, she's renamed

### B13 · Jen — commis or CDP · OPEN
`CLAUDE.md` says commis. `manuscript-structure` says CDP. `19_CoastOrClimb.md`
gives no rank.
**A** commis · **B** CDP · **C** commis then CDP — she progressed

### B14 · `drafts/TheEarlyDays.md` · OPEN
First third is pre-correction (age **23**, visits **behind glass**) and superseded.
The rest is the only copy of the parole officer, culinary school and Grant's kitchen.
**A** split into 05/06, retire the stale third · **B** supersede whole, rewrite from
interview · **C** archive, leave the gaps

### B15 · `03_FreshForUnlock.md` — two H1s · OPEN
Carries `# FRESH FOR UNLOCK` and `# GENERAL POPULATION`. Every other chapter has one.
**A** one chapter — drop the second to `##` · **B** two chapters — GENERAL POPULATION
becomes **05**, closing one gap

---

## TIER 5 — long-standing

### B16 · Year Jackson died · OPEN
Not established, not derivable from birth year 2013, "aged 7", or "Madison is now 10".
Needed to anchor the late-career section. **Yours alone.**

### B17 · Where Jackson's care passes Stacey → Tegan · OPEN
Split from Stacey at Lasseters; Tegan met after Saigon; the crossing point is
unstated. `register-patch-family.md` open item 2.

### B18 · Naming on the page — family · OPEN
**A** full names — Tegan, Jackson, Madison · **B** the source forms — *tee*, *jacks*,
*madz*, lower case · **C** source forms in dialogue, full names in narration

### B20 · The childhood block — NEW · OPEN · raised 2026-08-30

**New material, new front of the book.** Early childhood into early teens, before
incarceration. His words: *"there is some really great content there and brings
even more weight to the trajectory."*

This sits **before** `01_CatchYaOnTheFlipSide.md`, which currently opens the
manuscript in the courtroom. It is not an insertion into PART ONE — it is a new
part in front of it.

**Consequence for the plan.** v1.4.0 established the manuscript has no fixed
**end**. This establishes it has no fixed **start** either. Scope has now moved at
both ends, which is worth stating plainly in the plan rather than treating each as
a one-off.

**Consequence for B11.** The size of this block sets how much numbering space the
front needs. A rough range is enough — four chapters or twelve changes the scheme.

**Needs a scope interview.** Nothing about it is on record: not the years, not the
household, not what "before incarceration" reaches back to. `CLAUDE.md` § 6 carries
exactly two anchors that touch it — **left school at 13** and **bail conditions
breached from age 13** — and both are boundary markers, not content.

**Not to be inferred from anything.** The origin arc's existing chapters imply a
great deal about that childhood. None of it is stated, and none of it is evidence.

### B19 · Encoding repair scope · OPEN
15 chapters carry mojibake (07–21). Two artefacts unrecoverable: the `à la carte`
line in `21_TheFrenchChef.md`, and the H1 of `context/chef-writer-context-profile.md`.
**A** approve a scoped pass over all 15, backups on · **B** approve, but hold the two
unrecoverable ones for me · **C** not yet

---

## CANON — Marco is not a real person · recorded 2026-08-30

Bosco, this session:

> *"Marco isn't a real person — it's the only people in the memoir who isn't, or at
> least not in the scope it's portrayed. It's actually a real story, it's just a
> story of Geoffrey (chef), not mine. It's added for depth of the scene."*

- The **event is real** — the grill chef who cut himself and kept flipping steaks.
  It happened to **Geoffrey**, the vineyard head chef, not to Bosco's brigade.
- **Marco is the only composite in the manuscript.** Everyone else is real.
- Appears in `14_TheOnesWhoStay.md` (the cut, the fish cook's line) and
  `08_EarningTheRight.md` (breaking down an animal).

**Actions:**
1. `CLAUDE.md` § 5 lists Marco as a real Vineyard-era character. **Correct it** —
   mark him composite, and record whose story it is.
2. `Geoffrey` is the vineyard **Chef's name**. `CLAUDE.md` § 5 carries him only as
   "Chef". Add the name. It already appears in `transcript.md` § Segment 10
   ("Fat Sam and Geoffery" — spelling unverified, **B21**).
3. **B22 — does the composite get disclosed?** A memoir with one borrowed scene
   usually says so in a note. Bosco's call, not a role's.

### B23 · One blocking voice_check finding on the Yulara draft · NEW · OPEN

`voice_check.py` run against a baseline derived from the real corpus.
**All six bands pass** — 1,709 words, mean sentence 7.5 (band 5.23–12.72), 35.5%
single-sentence paragraphs (band 29.5–85.79), mean paragraph 18.4 words (band
7.73–27.6). B2's ruling is vindicated by measurement.

**VERDICT: REVISE — 1 blocking, 0 advisory.**

> line 231 · **[TELLING]** names the emotion instead of rendering it: **"I was proud"**
> *"They were fucking proud of themselves. **I was proud of them too.**"*

It is a true hit against the stated standard — `CLAUDE.md` hard-no list, *stating
emotions instead of rendering them*. Whether it is a defect is yours: the line is
spare, it is earned by the scene, and the juniors' pride is already rendered.

**A** cut it · **B** render it — an action instead of the statement · **C** it
stands; the checker is being literal

### B24 · Push this session's work to the repo · OPEN
The clone is read-only so far — nothing pushed, nothing altered. Six new files
exist only in project knowledge: the Yulara draft, the audit, `writing-plan_v1.4.0`,
this ledger, the transcript addendum, plus the uncommitted `22_Dave.md` /
`23_ReturnToYulara.md` renames and the patched `CLAUDE.md`.
**A** push it all · **B** push nothing, you commit by hand · **C** push a
specified subset

### B21 · `Geoffery` or `Geoffrey` · OPEN
Spelled `Geoffery` in the transcript, `Geoffrey` by Bosco this session. One letter,
goes in print.

### B22 · Disclose the composite · OPEN
Author's note, or leave it. Nothing else depends on it.

---

## Also on the list, not blocking

- `chapters/09_SetUpYoutStation.md` — filename typo, `Yout` → `Your`
- `17_ProductionKitchen.md` names the narrator **Chris** — the only place in 21
  chapters. Sits under B4/B18
- `04_FourFlights.md` drops the *"Same board. Same day. Different histories."*
  close its own review said to keep. Deliberate?
- `CLAUDE.md`, `README.md`, `context/project-memory.md` — stale word counts, version
  numbers, phantom directory tree, old repo URL. Mechanical, once B10/B11 land
- `project-memory.md` exists at repo root **and** at `context/`. One is authoritative

---

*19 open. Answer one at a time; each answer is written back here as
`ANSWERED: <key>` with the date.*
