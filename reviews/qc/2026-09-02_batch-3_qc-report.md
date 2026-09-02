# QC Report — Remediation Batch 3

**Target:** branch `claude/remediation-batch-three-6srfwz` (PR #9) — the Batch 3 change set
**Type:** draft (three prose edits) + formatting/tracking report (governing-file and matrix updates)
**Produced by:** Batch 3 execution session
**Checked:** 2026-09-02 | **Loop:** 1 of 2
**This report:** `reviews/qc/2026-09-02_batch-3_qc-report.md`

**Scope note — the branch moved during review.** The brief named commits `539c95c` and
`173bb7a`. Two further commits landed mid-review: `06ae2cf` (voice-baseline refresh) and
`2dc02f7` (six review findings addressed, which **rewrote both prose edits again**). This
report gates `2dc02f7`, i.e. `git diff origin/main...HEAD`, because that is what merges.
Findings drafted against the earlier commits — a present-perfect tense break at ch.17:5 and a
stale "wing-cleaning partner" quote at matrix row 37 — were both already fixed by `2dc02f7`
and are recorded as *resolved-in-flight* below rather than as live findings.

**Baseline:** `context/voice-baseline.json`, regenerated 2026-09-02 against the current
corpus (19 files, 22,971 words). `context/owner-voice-profile.md` **does not exist**; the
voice layer is assessed against `context/chef-writer-context-profile.md` alone.

---

## Verdict

**REWORK** — 92/100

The prose work is genuinely good and the tracking work is honest — three minimal, in-register
edits, every ring-fenced passage byte-identical, and no status claim that overstates. One
introduced canon inaccuracy caps it: the new Dylan row in `CLAUDE.md` §5 reverses who handed
the keys to whom. That is a one-word fix, not a redraft.

---

## Layer 0 — Mechanical

| Check | Result | Inherited or introduced |
|---|---|---|
| Encoding integrity | ✓ — `encoding_check.py` CLEAN on all five touched text files (chs. 04, 17, 20, `CLAUDE.md`, `context/canon.md`) | n/a — no damage |
| Spelling variant (AU/UK) | ✓ — no US spelling in any added line | n/a |
| Filename convention | ✓ — no new files created | n/a |
| Required sections present | ✓ — all six chapter plans and the matrix carry their completion-criteria blocks | n/a |

No introduced Layer 0 defect. Nothing here blocks.

---

## Layer 1 — Voice (38/40)

| Dimension | Score | Note |
|---|---:|---|
| POV & tense discipline | 5/5 | All three edits first-person past. See *Scrutiny (a)* — the tense concern was real against `173bb7a` and is gone at HEAD. |
| Register & profanity | 4/5 | `17:5` ("Everything after it was somewhere else — the same job, learned over again in a room that did it differently") is the most abstract sentence in the batch; no kitchen noun, faintly literary against the corpus register. |
| Rendering vs stating | 10/10 | No stated emotion introduced. `20:33` replaces an announced realisation with cost and ownership. |
| Restraint | 10/10 | All three edits remove explanation rather than add it. `20:33` in particular no longer narrates the narrator understanding something. |
| Rhythm | 4/5 | `17:3-5` trades a staccato tricolon for two medium sentences. Deliberate and documented, but ch.17 is the corpus's most fragmented file (75.7% single-sentence paragraphs) and this is its opening. |
| Dialogue authenticity | 5/5 | No dialogue touched. |

---

## Layer 2 — Substance (32/35)

| Dimension | Score | Note |
|---|---:|---|
| Historical accuracy | 13/15 | "Three years at the vineyard" matches `CLAUDE.md` §6. "my celly" is consistent with ch.03 (see *Scrutiny (b)*). **−2: the Dylan row inverts the key handover** — see Blocker 1. |
| Specificity | 9/10 | `17:5`'s "a room that did it differently" is the batch's one unanchored image. |
| Structural integrity | 10/10 | Every edit is the smallest sufficient intervention: one sentence in ch.20, one clause in ch.04, two sentences in ch.17. No entry-type structure disturbed. |

---

## Layer 3 — Cohesion & readiness (22/25)

| Dimension | Score | Note |
|---|---:|---|
| Redundancy with adjacent chapters | 9/10 | REM-010 is resolved at both the verbatim **and** the paraphrase level — sentence-set diff of chs. 16/17 returns the empty set, and the second rewrite removed the near-identical list as well. −1 for the "room" echo at the seam (Owner decision 4). |
| Continuity of arc | 5/5 | ch.16 → ch.17 now reads as a step forward rather than a restatement. ch.20:33 no longer competes with ch.19:129. |
| Opening and close | 4/5 | "Three years at the vineyard, then the door shut behind me." is a strong chapter opening. Line 5 softens the entry it just earned. |
| Owner-facing completeness | 4/5 | Matrix and all six chapter plans are accurate and honest, including two rows deliberately left OPEN. −1 for the miscitation at Finding 2 and the missing ledger key at Owner decision 2. |

---

## Findings

**BLOCKER — `CLAUDE.md` §5 Melbourne Era, Dylan row — reversed action against the prose**

> | **Dylan** | Food runner (Italian) | Handed Scotty's keys during Joe's injury; drove Chef to A&E and brought him back. …

The registry makes Dylan the one who handed the keys over. `21_TheFrenchChef.md:157` has it
the other way: "He grabbed his keys and handed them to the closest food runner — Dylan."
Scotty hands; Dylan receives. The rest of the row is sound — `:159` supports the A&E trip and
`:261` ("The food runner got back a few minutes later with Joe in tow") supports "brought him
back". Introduced this batch, in the file drafters read *instead of* the chapter, which is how
a reversed beat reaches a future chapter.
**Fix:** `Handed Scotty's keys` → `Given Scotty's keys`. One word. Nothing else in the row changes.

---

**FINDING — `…20_goose-and-gander_remediation-plan.md:33` — wrong line cited for the ChefTip italic convention**

> …this chapter's rule line at line 55 already uses italic, matching `CLAUDE.md:155`.

`CLAUDE.md:155` is the ChefTip #9 table row. The italic convention is stated at
`CLAUDE.md:172` ("`## ChefTip #X` with the quotable rule in *italics*"), which is what matrix
row 18 correctly cites. Introduced by `539c95c`; the same criterion line inherits the
`:155,171` pair from the pre-existing plan text at `:11,28`, which was the REM-031 conflict and
is now stale in its own right.
**Fix:** cite `CLAUDE.md:172`.

---

**NOTE — inherited — `17_ProductionKitchen.md:341` — `TELLING` block**

`voice_check.py` returns REVISE on ch.17 for a single line that foreshadows from outside the
moment ("Little did I know…"). Verified present in `origin/main`; not this batch's line, not in
Batch 3 scope, and no REM item covers it.
**Fix:** none here. Raise for Batch 7 or route to the owner.

---

**NOTE — inherited — chs. 19/20 carry two verbatim shared sentences**

A sentence-set diff of `19_CoastOrClimb.md` and `20_Goose&Gander.md` returns
`"You can't demand what you won't demonstrate."` (19:127, 20:35) and `"No exceptions."` Both
predate Batch 3. This is REM-010's exact defect class at a seam no REM item covers — the first
is very likely a deliberate refrain (it is ChefTip #5's thesis), the second is trivial.
**Fix:** none here. Record in `_continuity-register.md` so Batch 7 rules on it once rather than
re-finding it.

---

## Scrutiny requested in the brief

**(a) Does the ch.17 rewording introduce a tense inconsistency? — No, and the earlier version
that did has already been replaced.**

At HEAD both new sentences are past tense ("the door shut behind me", "Everything after it was
somewhere else"), so the question is moot. It is worth recording that it would **not** have
been a defect against `173bb7a` either, where line 5 read "Since then it's been kitchen after
kitchen": the sentence it replaced was itself present-perfect ("A lot of kitchens *have
happened* since then"), ch.16:99 carries the identical construction, ch.17 narrates in the
present throughout (`:39, :63, :157, :159, :189, :191`), and handoff §4 ring-fences "the
present-tense asides" as a deliberate feature of this chapter. The retrospective
present/present-perfect is the chapter's established register, not drift.

**(b) Does "Ivian, my celly" contradict canon? — No. It is consistent, in-register, and
under-recorded.**

- *In register*: "celly" is the manuscript's own word, used twice in ch.03 (`:55`, `:207`).
  Not imported vocabulary.
- *Not contradicted*: ch.03 moves the narrator through two cell arrangements — the
  classification celly (`:207`, "They moved me with my classification celly at first"), then
  "my mate had a spare bunk in his cell. And a TV. So I got myself moved to his house instead"
  (`:213`). Ch.04 is set after that move. A named celly in general population fits the
  sequence with nothing to reverse.
- *Authority*: the change went beyond handoff §3's explicit "Do not invent beyond that", but it
  came from the author, which outranks the handoff. `CLAUDE.md` §5 and `context/canon.md` were
  both amended to match, and matrix row 37 records the correction and its origin. Correctly
  handled.
- *The gap*: the ruling has **no decision-ledger key** (the ledger ends at B38, and B34–B38
  were all opened this cycle for smaller rulings), and the amendment silently identifies Ivian
  as the previously-unnamed mate at ch.03:213. See Owner decisions 1 and 2.

**(c) Does ch.20's new line 33 duplicate the vineyard attribution at line 37? — Not at HEAD.**

The version in `173bb7a` did, and worse: "That's when **the vineyard lesson** stopped being
something I knew…" pre-labelled and pre-attributed four lines before `:37` dramatises it, and
collided head-on with `:37`'s "Never made it a lesson." The current line —

> Same rule the vineyard gave me — it just cost more now the kitchen was mine.

— names the vineyard as source but frames the beat around **cost and ownership**, so `:33` is
now setup and `:37` is illustration. That is ordinary structure, not duplication, and the word
"lesson" is gone. REM-011's own validation is met: no first-discovery claim survives, and the
line no longer competes with ch.19:129 ("I'd learned that at the vineyard") or with ch.19:145-161,
where the narrator is already scrubbing grout beside the brigade.

---

## Ring-fence verification (handoff §4)

Byte-identity checked with SHA-256 against `origin/main`, and line-deletion diffs for the three
edited files. **All pass.**

| Ring-fenced | Result |
|---|---|
| ch.16 — wine ritual, departure scene, "Almost like I belonged somewhere" | File **byte-identical**; `:15-45`, `:81`, `:45` all intact |
| ch.17 — everything but lines 3–5 | File identical with lines 3 and 5 excluded; present-tense asides, Dane/Robbie, Gavin's scene untouched |
| ch.20 — brigade-anticipation scene, range-hood reversal, exiting bridge | File identical with line 33 excluded |
| ch.21 — pork-belly physics, service crisis, closing line, **Rachael not Carly** | File **byte-identical**; Rachael stands at `:105, :107, :223, :235`; zero occurrences of "Carly" |
| ch.04 — everything but line 11 | File identical with line 11 excluded |
| REM-029 historical records (`reviews/manuscript-audit_2026-08-30.md`, `_continuity-register.md`, master plan `:468-476`) | **Byte-identical** — correctly left alone while the two operational references were swept |

No author ruling reversed. No approved prose overwritten.

---

## Status-claim verification

Every claim in the execution matrix and the six chapter plans was checked against file state.
**No claim overstates or understates completion.** Spot-verified:

| Claim | Verified |
|---|---|
| Row 4 / 5 — REM-023, REM-042 OPEN | ✓ `08_EarningTheRight.md:59` still reads "Ten ChefTips"; correctly **not** closed |
| Row 10 — REM-019 OPEN, Bosco's decision | ✓ mirrored in the ch.04 plan's unticked box |
| Row 12 / 21 — REM-039 NOT done | ✓ profile `:400` still says "Diary of an Apprentice"; `:115, :313, :316` still mandate `### ChefTip Number X` |
| Row 14 / 23 — Geoffrey Welham, no hedge | ✓ `CLAUDE.md:240` |
| Row 16 — Scotty, Raj rows present | ✓ `CLAUDE.md:206-207` |
| Row 18 — italic convention stated, no bold remains | ✓ `CLAUDE.md:172`, sole match in the file |
| Row 19 — REM-036 **PARTIAL**, one cited fact not two | ✓ `18_TheBaseline.md:7` is the only source citation in §6. Honest downgrade |
| Row 34 — zero verbatim overlap chs. 16/17 | ✓ sentence-set intersection is empty |
| Row 37 — ch.04:11 clause, celly correction recorded | ✓ matches the file exactly (was stale at `173bb7a`, fixed in `2dc02f7`) |
| Row 39 / 44 — NO ACTION, closed by B34 / B22 | ✓ ledger confirms both; row 44's warning against creating the author's-note file is a real catch |
| Row 50 — REM-029 **PARTIAL** | ✓ `git mv` landed; master plan `:834` and row 50 both now say `09_SetUpYourStation.md` |
| ch.04 plan — faze/fazed already correct | ✓ `:45`, `:261` |
| ch.21 plan — Dylan clause present, Carly guidance superseded | ✓ `:157`; plan now says preserve Rachael |

Definition of done (handoff §7): eleven of twelve items complete. The twelfth ("reviewed
before merge; findings answered and threads resolved") is this report.

---

## Owner decisions

Judgement calls the rubric doesn't settle. Not scored as defects, not blocking.

- **Is Ivian the mate with the spare bunk and the TV?** `03_FreshForUnlock.md:213` has the
  narrator move into an unnamed mate's cell in general population; `04_FourFlights.md:11` now
  calls Ivian "my celly" in that same wing. Reading A: they are one man, and ch.03 already
  introduces him unnamed — which closes the REM-017 gap more thoroughly than the clause alone,
  and means `_continuity-register.md` is carrying two entries for one person. Reading B: they
  are different men, and the reader will hit two cell arrangements with no bridge. Your call —
  and if A, the register entry should be merged.
- **The celly ruling has no ledger key.** B34–B38 were all opened this cycle for rulings of
  equal or lesser weight, and handoff §1.3 makes the ledger authoritative over every plan.
  Right now the only record of your instruction is a commit message. Recommend a B39 entry;
  without one this is the Carly/Rachael failure mode waiting to happen.
- **ch.17 dropped the list the handoff told it to keep.** Handoff §3 said "Keep that
  information and the list-structure rhythm; change the wording." The second pass removed the
  "different cities / different countries / wasn't good enough" triple from ch.17 entirely,
  because keeping it reproduced ch.16's close in near-identical terms even without shared
  sentences. Two requirements pulled apart and the batch picked one — but it picked the right
  one, said so in the chapter plan and the commit, and did not do it silently. Confirm the
  override, and note ch.17 still carries the "good enough" theme at `:127`.
- **"room" repeats across the ch.16/17 seam.** ch.16's final line ends "…staying in the room
  long enough to become someone worth keeping"; ch.17:5 now ends "…in a room that did it
  differently." Adjacent, and at the exact seam REM-010 exists to clean. Reading A: an
  invisible function word, leave it. Reading B: swap it for a kitchen noun and gain the
  specificity Layer 2 marks down. Either is defensible; a one-word change would settle it.

---

## Overrides

None recorded this cycle. Standing overrides respected and **not** re-flagged, per handoff §4:
the ch.11 "Darren" strawman beat, ch.11:11 "trauma documentaries", and Rachael over Carly in
ch.21.

---

## Automated check summary

| Script | Exit | Result |
|---|---|---|
| `encoding_check.py` | 0 | 5 files clean, 0 damaged (chs. 04, 17, 20, `CLAUDE.md`, `context/canon.md`). No mojibake of any kind in the touched set |
| `voice_check.py` | 0 / 0 / 2 | ch.04 PASS, ch.20 PASS (clean against the measured fingerprint), ch.17 REVISE — 1 blocking `TELLING` at `:341`, **inherited**, verified present in `origin/main`. All six metrics in band on all three files |
| `continuity_check.py` | 0 | No contradictions against canon on any of the three chapters |

*Signal, not verdict — the human-legible check decided every line above. ch.17's script
verdict is REVISE and the chapter passes this gate: the flagged line is not Batch 3's and not
in Batch 3 scope. Neither of the two blockers this report raises came from a script.*

Baseline used by `voice_check.py`: `context/voice-baseline.json`, generated 2026-09-02, 19
files / 22,971 words. Refreshed once for this session; the working tree was left clean.

---

## Routing

**Next:** rework by the Batch 3 execution session (loop 1 of 2) — one word, then re-gate
**Blockers to resolve:** `CLAUDE.md` §5 Dylan row — "Handed Scotty's keys" → "Given Scotty's keys"
**Also fix while in there (non-blocking):** ch.20 plan `:33` — cite `CLAUDE.md:172`, not `:155`
**Routed to `formatting-agent`:** none — the touched files are encoding-clean
**Raise with the owner:** four decisions above; the celly ledger key is the one with a cost if skipped
