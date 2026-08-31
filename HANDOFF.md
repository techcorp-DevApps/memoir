# HANDOFF — Cowork → Claude Code

**From:** a Cowork session, 30–31 August 2026
**To:** Claude Code (cloud), with write access to `TechCorp-DevApps/memoir`
**Read this first, then `context/SOURCES.md`, then `planning/decision-ledger_2026-08-30.md`.**

---

## 1. Why you exist

The Cowork session could clone this repo but **could not push to it** — its sandbox
proxies all GitHub traffic and refuses to inject a credential for a repo outside the
session's authorized set. A valid PAT made no difference; the proxy strips it.

So there is **one local commit that never reached origin**, delivered to Bosco as a
git bundle. If it is already applied, skip to § 4.

---

## 2. First job — land the commit

Check whether it is in already:

```bash
git log --oneline | head -5
ls drafts/19_ICanCookBetterThanYou_v1.2.0.md   # exists → already landed
```

If not, Bosco has `memoir-session-2026-08-30.bundle`:

```bash
git fetch /path/to/memoir-session-2026-08-30.bundle HEAD
git merge FETCH_HEAD          # or: git cherry-pick FETCH_HEAD
git push origin main
```

The bundle carries the `chapters/21_dave.md → 22_Dave.md` rename as a rename. A
plain file copy loses that.

---

## 3. What the commit contains

**Recovered — marked ✓ Complete in both planning docs but absent from 79 commits of
history. All three existed in a v1.2.0 draft set that was never committed:**

- `drafts/19_ICanCookBetterThanYou_v1.2.0.md`
- `drafts/20_ThePeopleWhoLaugh_v1.2.0.md`
- `drafts/23_YoureOnlyAsGoodAsYourLastService_v1.2.0.md`

⚠️ **All three are transcribed from a chat paste, not byte-verified.** Bosco has the
v1.2.0 original. **Replacing them with the exact text is a priority job.** §23's
closing quote is truncated mid-sentence.

**New:** `drafts/YULARA_ReturnToYulara_v1.0.md` · `planning/writing-plan_v1.4.0.md` ·
`planning/decision-ledger_2026-08-30.md` · `reviews/manuscript-audit_2026-08-30.md` ·
`reviews/source-recovery-assessment_2026-08-30.md` ·
`interviews/return-to-yulara/transcript-addendum_2026-08-30.md` · `context/SOURCES.md`

**Amended:** `CLAUDE.md` — register patch, composites/disguises table, retitle,
corrected § 3 state and placeholders.

---

## 4. State of the manuscript

Measured with the bundled scripts against the real repo, **before** this commit:
**20 chapter files, 23,129 words.** Numbering gaps at **05** and **06**.
ChefTips **#11–#5 written**, **#4–#1 open** (#1's host chapter now recovered).

### The book's shape, settled 30 Aug

```
BEFORE ANY OF IT        childhood → early teens        reserved, unscoped
PART ONE                origin arc                     no ChefTips — NEEDS A NEW NAME
VINEYARD ERA            ChefTips #11 → #7              complete
TRANSITION / AUSTRALIA  ChefTips #6, #5                complete
MELBOURNE / MID-CAREER
POST-MELBOURNE ARC      six venues                     venue 1 drafted, 2–6 unscoped
§23                     ChefTip #1                     recovered
   └─ ladder closes, career content phases out
AFTER THE LADDER        Jackson · grief · Madison · the new work
   └─ adaptive endpoint, at the present day
```

**The book is now titled *The Long Road To Nowhere*.** That was Part One's name;
Part One needs a new one.

---

## 5. Rules that bind every draft — do not relax these

1. **No career chapter foreshadows Jackson's death.** §23 names ChefTip #1 and
   withholds the story deliberately, so the reader carries the question and
   understands it retrospectively. A planted hint anywhere in the arc destroys the
   effect. This is Bosco's ruling, not a stylistic preference.
2. **Do not restate ChefTip #1 in Part Seven.** It is *lived* there, not repeated.
   The reader joins it up.
3. **Jackson is born in the Yulara chapter and does not die in it.** No shadow.
4. **Sanitising is a blocking defect.** `fucken` is house spelling and protected —
   ruled 30 Aug, closing DECIDE #4. No masked profanity, no minced oaths, no
   clinical euphemism. The author served a sentence and put it on the page; that is
   the subject, not content to be handled.
5. **Real names throughout** — venues, colleagues, and the German GM scene as
   written. Ruled 30 Aug. Worth a publisher's legal read before publication, not a
   rewrite.
6. **Marco is the only composite.** The event is real but it is Geoffrey's story.
7. **Never invent a specific to fill a gap.** Leave `[GAP: ...]`.
8. **Never assign a ChefTip number.** The numbering encodes cost; it is Bosco's.
9. **No role writes to `chapters/`.** Only Bosco promotes a draft.

---

## 6. Open decisions

**`planning/decision-ledger_2026-08-30.md` is the live list — 33 items, keyed,
20 answered.** Work them one at a time as single questions. Bosco's stated
preference: *checklist first, then single-point question and answer.* Do not bundle
them into a wall of text; he has asked for this explicitly, twice.

Highest value first:

| ID | Item |
|---|---|
| **B31** | The truncated closing quote in §23 (Bourdain). Recover in full; attribution and permissions are a publisher question |
| **B29** | Upload the v1.2.0 original and the pre-memoir blog source; replace the transcribed drafts; file the blog as `context/ORIGINAL-BLOG-SOURCE.md`, LOCKED |
| **B19** | Encoding repair — 15 chapters, counts per file in the audit. `formatting-agent`, scoped, backups on, **Bosco approves the scope first** |
| **B11** | Numbering alignment + stub files. Ruled, not executed. Needs Part Zero sized first |
| **B23** | `voice_check` blocking hit on the Yulara draft: *"I was proud of them too"* |
| **B32** | §20 lost *"You caught it before I had to. That's the job."* going blog → v1.2.0 |
| **B7, B21, B22, B27, B33** | See the ledger |

**Long-standing, Bosco's alone — do not close these:** the year Jackson died (not
derivable), where Jackson's care passed Stacey → Tegan, naming on the page for the
family, and the **10 remaining DECIDE items** in
`interviews/jackson/CORRECTION-LEDGER.md`.

---

## 7. Traps

- **`planning/register-patch-family.md` and `planning/next-session-kickoff.md` are
  superseded** on where the Jackson material goes. Both say "in #23". It goes
  **after**. Do not quote either as current.
- **`writing-plan_v1.3.0.md` and `manuscript-structure_v1.3.0.md` both close at
  #23** and conflate the ChefTip ladder ending with the book ending. Superseded by
  v1.4.0.
- **The pre-memoir blog source disguises identities.** Where it and the manuscript
  disagree about *who someone is*, the manuscript is right. Content survives the
  disguise; identity does not.
- **The repo has not been the whole manuscript.** See `context/SOURCES.md` for what
  still lives only in claude.ai project knowledge or on Bosco's disk.
- **Scripts live under the `memoir-studio` skill, not in this repo.**
  `manuscript_status.py`, `voice_check.py`, `encoding_check.py`, `corpus_stats.py`
  all run against `--repo <path>`. Reported numbers must come from a script that
  actually ran.

---

## 8. Next actual work, once the commit is in

1. Replace the three transcribed drafts with the byte-exact originals.
2. Resume the Yulara scope interview **from Segment 11** — the tenure's end, what
   followed the tasting, and the outstanding flagship dishes.
3. Scope **§1a** (Alice Springs, the birth) — it has a fact and no scene.
4. Scope **Part Zero** enough to size the front of the book.
5. Then the numbering pass, and both planning docs to v1.5.0.

**Order matters: scope first, then draft.** Drafting into an unscoped arc produces
chapters that get rewritten once the arc exists.
