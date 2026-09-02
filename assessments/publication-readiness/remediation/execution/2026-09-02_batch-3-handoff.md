# Batch 3 — Session Handoff

**Written**: 2026-09-02, at the close of Batch 2 (merged as #6).
**For**: the next session, starting cold, executing **Batch 3 — Cross-chapter continuity & duplication**.

This document is the starting point. It states what is actually true in the repo
right now, which is **not** what every tracking file says — see §2.

---

## 1. Read these first, in this order

1. `CLAUDE.md` — voice standards, Hard "No" List, character canon, historical facts.
2. `context/chef-writer-context-profile.md` — the full voice profile and its Implementation Checklist.
3. `planning/decision-ledger_2026-08-30.md` — **the authoritative record of Bosco's rulings.** Where the ledger and a remediation plan disagree, the ledger wins.
4. `context/canon.md` — exists now (added by #5 under ledger B38). The master plan predates it and says it doesn't exist; that statement is stale.
5. The master plan: `../master/2026-09-02_150000_complete-manuscript_publication-remediation-plan.md` — §3 for the REM entries below, §8 for Batch 3, §9 risk table, §10 preservation requirements.
6. Chapter plans in `../chapters/` for 16, 17, 19, 20, 21, 04.

---

## 2. Trust the ledger and the files, not the matrix

**The execution matrix understates what is done.** Rows 1–25 (Batches 0 and 1) still
read `PLANNED`, but PR #5 executed most of them and PR #6 only updated the Batch 2
rows it touched. Verified as actually complete in the working tree despite a
`PLANNED` row:

| Item | Row | Real state |
|---|---|---|
| REM-015 (ch.21 line 9 commas) | 41 | Done — commas present |
| REM-018 (ch.04 faze/fazed) | 48 | Done — 2 instances corrected |
| REM-029 (filename) | 50 | **Half done.** The `git mv` landed (`09_SetUpYourStation.md`), but REM-029's strategy also requires updating internal cross-references and that sweep did not happen. Still naming the old path: the master plan's own Batch 5 file list (`:834`) and matrix row 50. Update those two *operational* references; **leave the dated historical records alone** (`reviews/manuscript-audit_2026-08-30.md`, the 2026-09-01 assessments, `_continuity-register.md`, and REM-029's own entry at `:468-476`) — they are point-in-time records that correctly describe the state when written |
| REM-030 (ch.15 H1) | 51 | Done — `# IF YOU DIDN'T TASTE IT, IT ISN'T YOURS` |
| REM-020 (ch.03 dual H1) | 3 | Done — B15 Option A, now one H1 + `## GENERAL POPULATION` |
| REM-028 / REM-040 (encoding) | 49, 22 | Done — zero mojibake in chapters |
| REM-016 (Dylan) | 9, 17, **38** | **Fully done, including the Batch 3 row** — see §3 |
| Batch 0 decisions | 1–14 | Ruled: ledger B13, B15, B21, B22, B34, B35, B36, B37, B38. **Two exceptions — rows 4 and 5 are genuinely still open**: REM-042 (ChefTips #2/#3/#4 placement) has no ruling, `planning/writing-plan_v1.4.0.md` still lists all three as `Unplaced / Open`; and REM-023 is blocked on it, with `chapters/08_EarningTheRight.md:59` still reading "Ten ChefTips". **Do not close either while cleaning the matrix** |

**Cleaning up rows 1–25 is a legitimate task for this session**, and cheap. Verify each
against the file before changing a status — do not mass-mark.

**A warning that cost time in Batch 2**: the local `main` ref was stale and every
`git diff main` was silently misleading. Run `git fetch origin main` and diff against
`origin/main` before drawing any conclusion from a diff.

---

## 3. Batch 3 scope — what is actually left

The master plan lists five items. One is already done and one is no-edit, so **the real
work is two prose edits plus one added sentence.**

### REM-010 — ch.16/17 verbatim duplication · MEDIUM · the main job
Confirmed still present, at the lines the plan cites. `16_TwoGlasses.md:97-99` and
`17_ProductionKitchen.md:3-5` share these two sentences **verbatim**:

> That was New Zealand. That was where it started.
>
> A lot of kitchens have happened since then. Different cities. Different countries. Different ways of being told I wasn't good enough yet.

- **Edit ch.17 only. Leave ch.16 untouched** — both chapter plans agree the ch.16 copy does legitimate work as a mid-chapter reflective aside, and the ch.17 copy is the drafting artefact.
- **Reword, do not delete.** Ch.17's assessment confirms the passage does real orienting work as an entry bridge (vineyard era ending, Australia beginning). Keep that information and the list-structure rhythm; change the wording.
- Validate: text-diff the two files for zero verbatim sentence overlap, then read ch.16 → ch.17 back to back — both assessments rate this transition strong in substance and the fix must not weaken it.

### REM-011 — ch.19/20 false claim of novelty · LOW · one clause
`20_Goose&Gander.md:33` reads "That's when I understood something I'd felt but never put
into words." — but `19_CoastOrClimb.md:125-129` already gave the narrator the same
formulation, attributed to the same source.

- The plan's **preferred fix is to cut "but never put into words"** from ch.20:33 — lightest touch, keeps the sentiment.
- ⚠️ **That fix may not satisfy its own validation, and you need to decide before applying it.** The cut leaves "That's when I understood something I'd felt." — which still frames *this* scene as the moment of understanding, while ch.19:129 already has "I'd learned that at the vineyard." REM-011's validation asks you to "confirm the second no longer claims to be discovering something the first already stated", and the clause-cut alone arguably fails it. The plan's own **Alternative** — reframing as an explicit callback to the vineyard rather than a fresh discovery — is the branch that actually clears the criterion. Judge it on a back-to-back read of both chapters; if you take the Alternative, the wording is yours to draft, but keep it to the one sentence.
- Leave ch.19 alone. Leave ch.20's range-hood scene alone — this is a single-sentence fix either way.

### REM-012 — recap redundancy at Part seams · LOW · **recommend NO edit**
The plan's own disposition is awareness-only. Three entry bridges (19, 20, 21) restate
prior facts, but each does legitimate work and none is individually broken; they also
serve non-linear readers arriving at a chapter cold.

- **Do not edit on your own initiative.** The plan says any trim should follow a full assembled read-through, which has not happened.
- Deliverable is a recorded decision ("no action, per plan disposition"), not a diff.

### REM-016 — chapter clause · **ALREADY DONE, close the row**
Ledger **B35** resolved it: Dylan is the same person as the food runner. The clause is
already in the prose at `21_TheFrenchChef.md:157`:

> He grabbed his keys and handed them to the closest food runner — Dylan.

`context/canon.md` carries the ruling. Matrix row 38 is stale — verify, then close it. **No edit.**

### REM-017 — ch.04 Ivian introduction · MEDIUM · **now unblocked**
The plan gates this on checking `drafts/TheEarlyDays.md` for an existing Ivian
introduction before touching ch.04. **That check has been run: zero occurrences of
"Ivian" anywhere in that draft** (467 lines, spanning CONCURRENT → GRANT'S KITCHEN,
prison-era material included). The introduction does not exist in the unpromoted material.

Therefore the plan's second branch applies: **add a single-sentence introductory beat to
`chapters/04_FourFlights.md` at Ivian's first mention (line 11).** Ivian is currently used
with full familiarity at `04:11` and `04:157` with no prior introduction anywhere in 01–04.

- One sentence. Match the register of the brief role-based introductions already in that chapter.
- Canon (`CLAUDE.md` §5, and the row added by #5): Ivian is **male**, the narrator's wing-cleaner partner — mopping, bins, extra unlock, extra milk. Do not invent beyond that.
- Must not pre-empt or duplicate what the eventual 05/06 chapters might cover (REM-026 is still open and is Bosco-only drafting work).

---

## 4. Rules that bind this batch

- **Smallest sufficient intervention.** No REM item in the register authorises a full-chapter rewrite. Every strategy names what must stay untouched.
- **Never invent.** No new named character, scene, date, age, or fact. Where a fix would require invention, the plan's answer is to cut or to ask Bosco.
- **Never soften.** Profanity, dark humour, bluntness and staccato rhythm are protected by §10. A "fix" that sanitises is a worse defect than the one it fixes.
- **Ring-fenced in the files this batch touches** — do not alter:
  - ch.16: the wine-education ritual, the departure scene (folded note, Chef's send-off), and the hedged "Almost like I belonged somewhere" (explicitly *not* a Hard-No violation — do not "fix" it).
  - ch.17: everything but lines 3–5. The present-tense asides, Dane/Robbie's "near enough" comedy, Gavin's first scene.
  - ch.20: the brigade-anticipation scene and the range-hood reversal; the exiting bridge to ch.21.
  - ch.21: the pork-belly brine/cure physics, the service-crisis sequence, the closing line, and **Rachael's name in the prose — Rachael, not Carly.**
    > ⚠️ The ch.21 chapter plan says to preserve "Carly" and that REM-032 would never touch this chapter's prose. **That plan predates ledger B36 and is wrong now.** Bosco ruled Rachael correct, against the chapter's own evidence, and #5 changed all four instances (lines 105, 107, 223, 235). The prose says Rachael today; `context/canon.md:29` carries the ruling. Do not "restore" Carly while checking protected passages — that would reverse an author ruling.
- **Author rulings are final and must not be re-litigated.** From Batch 2, in ch.11: the "Darren" strawman beat stays (Bosco overrode REM-001), and `:11` "trauma documentaries" stays. Both are recorded in the ch.11 plan and matrix. If a review bot flags either, the answer is the ruling.

---

## 5. What Batch 2 learned the hard way

1. **Do not mark an item DONE when it is partial.** Two Batch 2 items were recorded complete when they were not; both reviews caught it. `PARTIAL` with a reason is the honest status and costs nothing.
2. **Preservation requirements can conflict with an item's own success metric.** REM-003's word target was met by stripping every kitchen mechanic from a ChefTip block, which violated §10. Resolved by cutting the redundancy the scene had already dramatised instead. When two requirements pull apart, satisfy both by cutting something else — don't silently pick one.
3. **Cutting beats rewording for stated-thesis and forced-epiphany lines.** Every rewrite attempt reproduced the defect in new words. The plan says cut; it means it.
4. **Read the whole chapter after editing, not just the hunk.** Two defects (a tense break, an unparseable clause) existed only in prose the batch itself had written.
5. **Get two reviews before merge.** An independent editorial review and the repo's automated reviewer caught different, real things; neither caught everything.
6. **Record author rulings where the next pass will look** — the chapter plan and the matrix — or Batch 7 re-flags settled questions as defects.

---

## 6. Explicitly out of scope

- **Batch 4** (REM-015 done; REM-022 and REM-025 are optional line-edit polish reserved for Bosco) and **Batch 5** (remaining copy items — REM-007/013/014/018/028/029/030 are already done; check before touching).
- **REM-026** — the 05/06 chapter split. Bosco-only drafting/promotion work; no role writes new chapters into `chapters/`.
- **REM-027, REM-042, REM-043** — future-drafting scope, no action.
- **Batch 7** — the full re-score. Not this session.
- **REM-005 (ch.13 imagery density) — open, carried from Batch 2.** One of three flagged comparisons was cut; Bosco has not ruled on the rest. Leave it for Batch 7 unless he raises it.

---

## 7. Definition of done for Batch 3

- [ ] ch.17:3-5 reworded; zero verbatim sentence overlap with ch.16; ch.16 unchanged.
- [ ] ch.16 → ch.17 transition re-read and confirmed still strong.
- [ ] ch.20:33 no longer claims novelty; ch.19 untouched; range-hood scene untouched.
- [ ] REM-012 recorded as "no action, per plan disposition".
- [ ] REM-016 row closed against the already-present clause at ch.21:157.
- [ ] **`../chapters/...21_the-french-chef_remediation-plan.md` brought current** — it is stale twice over: its REM-016 steps still say Bosco must confirm Dylan and that the clause is yet to be added (both done, ledger B35), and its preservation list still protects "Carly" (superseded by B36). Left as is, it re-opens two settled rulings.
- [ ] ch.04 carries a one-sentence Ivian introduction at first mention, consistent with canon, inventing nothing.
- [ ] Matrix rows 34–38 updated honestly (`DONE` / `PARTIAL` with reason / `NO ACTION`), and the stale Batch 0/1 rows in §2 corrected against verified file state — **without closing REM-023 or REM-042, which are genuinely open.**
- [ ] REM-029's outstanding reference sweep done (master plan `:834`, matrix row 50), historical records left untouched.
- [ ] Chapter plans for 16, 17, 19, 20, 21, 04 updated with what was done.
- [ ] Every ring-fenced passage in §4 confirmed byte-identical.
- [ ] Reviewed before merge; findings answered and threads resolved.

---

*Batch 2 closed at `30662b9`. Chapters 11–14 remediated; REM-001…REM-009 each carry a
recorded disposition. This handoff supersedes nothing — it points at the plan and reports
the repo's true state as of 2026-09-02.*
