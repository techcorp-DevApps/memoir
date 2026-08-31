# SOURCES — where the manuscript actually lives

Updated 2026-08-30.

The manuscript is not all in this repository, and this file exists so nobody has to
discover that the hard way again. It was discovered the hard way on 30 August 2026.

---

## The three layers

| Layer | What it holds | Authority |
|---|---|---|
| **This repo** | Committed chapters, drafts, planning, reviews | The baseline for anything committed |
| **claude.ai project knowledge** (`chef-writer`) | Everything below under "Project-only" | **Ahead of the repo** for those files |
| **Bosco's disk / chat history** | Original pre-memoir source. *(The v1.2.0 restructured draft set is now filed at `archive/Diary_of_a_Chef_v1_2_0.md`.)* | Ahead of both. Only Bosco indexes this |

**Do not assume the repo is complete.** On 30 Aug 2026 three sections were marked
✓ Complete in both planning documents with no file in 79 commits of history. All
three existed — in a v1.2.0 draft set that had never been committed.

---

## Project-only — NOT in this repo, should be

These live in claude.ai project knowledge and nowhere else durable. Each should be
committed here by Bosco, exported byte-exact rather than transcribed.

| File | Destination in this repo |
|---|---|
| `BRIEF.md` | `interviews/return-to-yulara/BRIEF.md` |
| `transcript.md` | `interviews/return-to-yulara/transcript.md` — **source of record for `drafts/YULARA_ReturnToYulara_v1.0.md`** |
| `RETURN-TO-YULARA-INTERVIEW-HANDOVER.md` | `interviews/return-to-yulara/RETURN-TO-YULARA-INTERVIEW-HANDOVER.md` |
| `interviews/jackson/SOURCE-VERBATIM.md` | same path — status `LOCKED — VERBATIM` |
| `interviews/jackson/CORRECTION-LEDGER.md` | same path — 34 APPLY, 19 HOLD, **10 DECIDE** (was 11; #4 closed 30 Aug) |
| `planning/register-patch-family.md` | same path — **superseded** on where the Jackson material goes |
| `planning/next-session-kickoff.md` | same path — **superseded** on the same point, and stale on the register patch |
| `memoir/reviews/skill-package-assessment.md` | `reviews/skill-package-assessment.md` |
| `memoir/planning/prison-chapter-todo.md` | already committed here |

**Why they were not committed by the assistant on 30 Aug:** committing them would
have meant retyping them out of a chat context. These are sources of record, and a
transcription is lossy by definition. Bosco can export them exactly in seconds.

**`interviews/jackson/SOURCE-VERBATIM.md` specifically** was also left alone because
moving a locked verbatim account of his son's death does not justify pulling it into
a working context to do so.

---

## Off-repo entirely — Bosco's disk / chat history

| Source | Status |
|---|---|
| **The original pre-memoir blog piece** — headed *The Diary of a Chef* | Pasted to chat 30 Aug, **never filed**. Should become `context/ORIGINAL-BLOG-SOURCE.md`, `LOCKED — VERBATIM`. Contains the blog-era §19 and §20 with **identities disguised** |
| **"DIARY OF A CHEF — Restructured Draft v1.2.0, December 2025"** | **No longer off-repo.** Uploaded 31 Aug and filed byte-exact as `archive/Diary_of_a_Chef_v1_2_0.md`. All three recovered chapters diffed against it and **verified byte-identical** — the transcription was accurate, nothing needed replacing. **It is truncated**: its last two lines are the recovery marker, so §23's closing quote is not in it (B31, open). See `archive/README.md` |

### The disguise rule — important

The pre-memoir blog was written for a public audience **with identities disguised.**
The memoir names people truthfully. Where the two disagree about **who someone is**,
**the manuscript is right and the blog is the softened one.**

Confirmed disguises in the blog source:

| Blog | Truth |
|---|---|
| "a woman named Sam", sous chef | **Fat Sam** — real identity restored deliberately |
| Father is a **dental surgeon**; apple torte | **Machinist at a forestry mill**, previously **cabinet maker**; **curried sausages** |
| Mother's **kangaroo curry** | **BBQ chicken** |
| *"if my boy is cooking for me"* | *"if my girl is cooking for me"* — a partner, not a son |

**Content survives the disguise. Identity does not.** Anyone named in blog-era
material is unverified until Bosco confirms them.

---

## Reading order for a new session

1. `CLAUDE.md` — state, characters, timeline anchors
2. `planning/decision-ledger_2026-08-30.md` — **every open decision, keyed**
3. `planning/writing-plan_v1.4.0.md` — current plan and the book's shape
4. `reviews/manuscript-audit_2026-08-30.md` — repo vs planning discrepancies
5. `reviews/source-recovery-assessment_2026-08-30.md` — what was recovered and what diverged
6. `archive/README.md` — what the archived v1.2.0 manuscript is authoritative for, and what it is not

**Superseded, do not quote as current:** `planning/writing-plan_v1.3.0.md`,
`planning/manuscript-structure_v1.3.0.md` (both close at #23),
`planning/register-patch-family.md` and `planning/next-session-kickoff.md` (both
place the Jackson material inside #23 — it goes after).
