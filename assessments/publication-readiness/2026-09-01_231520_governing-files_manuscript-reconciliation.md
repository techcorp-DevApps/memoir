# Governing-Files ↔ Manuscript Reconciliation Report

**Phase**: 6 (final) — full-manuscript publication-readiness audit, "The Long
Road To Nowhere" (`TechCorp-DevApps/memoir`)
**Run timestamp**: 2026-09-01_231520
**Compiled from**: the 19 individual chapter assessment files' own
"Governing-File Reconciliation Findings" sections, `_continuity-register.md`
(all four batches plus the mid-audit owner correction), and §17 of the
manuscript-level synthesis
(`2026-09-01_231520_complete-manuscript_publication-readiness-assessment.md`).

> **Note on `canon.md` citations throughout this file, added 2026-09-02:** an
> automated PR reviewer (Codex) correctly flagged that `canon.md` does not
> exist anywhere in this repository, so its citations could not be verified
> by anyone reading only `techcorp-DevApps/memoir`. This is accurate:
> `canon.md` is a reference file bundled with the **memoir-studio Claude Code
> skill** that produced this audit (`references/canon.md` inside that skill's
> own directory, not this project). It was read directly, for real, during
> this audit — the citations reflect actual content, not invention — but it
> is external to this repo and only accessible to a session with that skill
> installed. Every `canon.md` citation below is traceable only via the skill
> until/unless Bosco decides to bring an equivalent reference into the repo
> itself (e.g. under `context/`).
Each item below was checked against the current text of the governing file it
concerns before being recorded here.

**Purpose and boundary.** This is compilation, not new investigation — every
item below already exists in a prior audit artefact; the citations here point
back to where it was first found. **No governing file, chapter file, or prior
assessment file has been edited to produce this report.** Nothing here is
resolved; each item is a discrete decision for Bosco to take up on his own
schedule, one at a time.

**Confidence scale used throughout**: High = the manuscript/governing-file
text itself settles the fact, only the edit is pending. Medium = plausible and
likely, but genuinely turns on authorial intent or an unread source. Low =
flagged for awareness only, actively ambiguous, or already superseded by a
ruling that just hasn't propagated into every file.

---

## 1. CLAUDE.md

### 1.1 — Melbourne character table missing three names (Scotty, Raj, Dylan)

- **Governing file**: `CLAUDE.md`
- **Relevant section**: § 5 Key Characters → "Melbourne Era" table (lines
  196–204)
- **Manuscript evidence**: `chapters/21_TheFrenchChef.md` — Scotty (FOH
  manager, hospitality veteran, takes charge during the Joe emergency, hands
  off his car keys, later returns with beers for the brigade); Raj (Nepalese
  dishie, silent, begins anticipating the narrator's calls after the crisis);
  Dylan (named once, at the point Scotty "must've handed Joe off to Dylan" —
  role/identity ambiguous). Source: ch.21 individual assessment's
  Governing-File Reconciliation Findings; `_continuity-register.md` Batch 4 §
  People established/expanded.
- **Affected chapter(s)**: 21 (THE FRENCH CHEF IN AN ITALIAN KITCHEN)
- **Nature of discrepancy**: Manuscript introduces named characters the
  reference table doesn't carry — the same "prose has moved ahead of the
  table" pattern already seen with Kein Do, Dane & Robbie, and Gavin in the
  Australia arc (Batch 3).
- **Authoritative source**: Manuscript. These are legitimate first
  appearances in approved prose; the table is simply behind.
- **Recommended change**: Add Scotty and Raj as new rows to § 5's Melbourne
  table with the anchors above. For Dylan, see 1.2 below — recommend holding
  that row until the identity question is resolved, rather than adding it
  alongside Scotty/Raj as a settled entry.
- **Confidence**: High (Scotty, Raj — straightforward table gap, clear from
  the text) / Low (Dylan — see 1.2).
- **Human confirmation required**: Not strictly required for Scotty/Raj (the
  chapter is unambiguous); Bosco's steer would help only on how much detail
  to carry into the table. Dylan needs Bosco either way (1.2).

### 1.2 — Dylan's identity is ambiguous, distinct from the Scotty/Raj gap

- **Governing file**: `CLAUDE.md`
- **Relevant section**: § 5 Key Characters → "Melbourne Era" table (same
  location as 1.1)
- **Manuscript evidence**: `chapters/21_TheFrenchChef.md` — Dylan is named
  once, at the moment "Scotty must've handed Joe off to Dylan." The chapter
  elsewhere references an unnamed food runner. It is not established in the
  text whether Dylan **is** that runner given a name at last mention, or a
  wholly separate, otherwise-unmentioned person.
- **Affected chapter(s)**: 21
- **Nature of discrepancy**: Not a table-completeness gap like Scotty/Raj —
  the open question is upstream of the table, in the manuscript itself (a
  Reading Quality clarity issue, per the ch.21 assessment), not something a
  table row can settle without first knowing who Dylan is.
- **Authoritative source**: Neither. This can't be resolved by picking the
  manuscript or the governing file — the manuscript itself doesn't disambiguate.
- **Recommended change**: Do not add a Dylan row to § 5 until Bosco confirms
  whether Dylan is the previously-unnamed food runner or a distinct character.
  If he confirms "distinct person," add normally alongside Scotty/Raj. If he
  confirms "same as the food runner," the chapter itself may want a small
  clarifying edit (out of scope for this report to prescribe).
- **Confidence**: Low — genuinely unresolved in the source text, not just in
  the governing file.
- **Human confirmation required**: Yes — Bosco, since only he knows whether
  this was meant as one character or two.

### 1.3 — Unnamed exec sous (production kitchen, Filipino woman) not in table

- **Governing file**: `CLAUDE.md`
- **Relevant section**: § 5 Key Characters → "Australia Era" table (lines
  185–194)
- **Manuscript evidence**: `chapters/17_ProductionKitchen.md:349` — an exec
  sous, Filipino woman, also runs the pastry kitchen. No name given in the
  chapter. Source: `_continuity-register.md` Batch 3 § People established.
- **Affected chapter(s)**: 17
- **Nature of discrepancy**: Same "manuscript has moved ahead of the
  reference table" pattern as 1.1, but the character has no name to add — the
  table has nothing concrete to receive yet.
- **Authoritative source**: Manuscript, but it doesn't supply enough to act
  on (no name).
- **Recommended change**: Flag for awareness only; no table row is actionable
  until/unless the character is named on the page (this or a future chapter)
  or Bosco supplies a name directly.
- **Confidence**: Low — not because the sighting is in doubt, but because
  there's nothing yet to write into the table.
- **Human confirmation required**: No action needed from Bosco unless he
  wants to supply a name now.

### 1.4 — Ivian's unintroduced appearance in ch.04 (continuity gap, not a table error)

- **Governing file**: `CLAUDE.md` (the § 3 "Placeholders Remaining" /
  numbering-gap material this touches) and, separately, `canon.md` — see 2.1
  for the canon.md half of this item.
- **Relevant section**: `CLAUDE.md` § 3 "Numbering: files run 01–23 with gaps
  at 05/06" (line ~144) and § 5 pre-kitkchen character table (no Ivian row
  currently exists there either — Ivian isn't in `CLAUDE.md` § 5 at all,
  only in `canon.md` § People → Pre-kitchen).
- **Manuscript evidence**: `chapters/04_FourFlights.md` names Ivian twice
  (wing-cleaner partner) with no prior introduction anywhere in
  chs. 01–03. Source: ch.04 assessment's Governing-File Reconciliation
  Findings (implicit — flagged as a Developmental finding, not classified
  there as a governing-file item); `_continuity-register.md` Batch 1 § People
  established and Batch 2 "Ivian gap — extended, not resolved."
- **Affected chapter(s)**: 04 (and, prospectively, the still-unsplit
  05/06 material in `drafts/TheEarlyDays.md`)
- **Nature of discrepancy**: This is a **continuity/developmental gap in the
  chapter**, not an error in any governing file — `canon.md`'s Ivian entry is
  accurate as far as it goes, and `CLAUDE.md` doesn't claim otherwise. It is
  listed here because the audit brief calls for it, but per the audit's own
  taxonomy it classifies as a **Continuity issue** requiring a manuscript
  decision (add an introductory beat to ch.04, or resolve naturally when
  05/06 are split out per ledger B11), not a **governing-file** edit on this
  half of the finding.
- **Authoritative source**: N/A — no governing file is wrong.
- **Recommended change**: No CLAUDE.md/canon.md edit is indicated for the
  introduction gap itself. Recommend Bosco decide, when the 05/06 split
  (ledger B11/B14) is executed, whether that draft material naturally
  supplies Ivian's introduction, or whether ch.04 needs a short added beat.
- **Confidence**: High that this is real and unresolved; Low/not-applicable
  for "which governing file to amend," since none needs amending for this
  half.
- **Human confirmation required**: Yes — Bosco decides the fix (introductory
  beat vs. wait for 05/06 split), not which file is wrong.

### 1.5 — Gavin's "proper introduction chapter" remains outstanding

- **Governing file**: `CLAUDE.md`
- **Relevant section**: § 3 "Placeholders Remaining" — "Chef Gavin proper
  introduction — placeholder marked in the v1.2.0 draft set" (line 130); § 5
  Australia Era table, Chef Gavin row: "Needs proper introduction chapter."
  (line 189)
- **Manuscript evidence**: `chapters/17_ProductionKitchen.md` gives Gavin his
  first full scene ("Good morning, sir. Come, take a seat.") — but per the
  ch.17 assessment and `_continuity-register.md` Batch 3, this is explicitly
  **not** the dedicated introduction chapter the plan still calls for.
- **Affected chapter(s)**: 17 (partial coverage only)
- **Nature of discrepancy**: Not a conflict — both `CLAUDE.md` and the
  manuscript agree the dedicated Gavin chapter is still unwritten. Recorded
  here only because ch.17's arrival narrows what that future chapter needs to
  cover (Gavin's introduction to *readers* has effectively already happened
  via ch.17; a dedicated chapter would now be building on that, not starting
  cold).
- **Authoritative source**: Both agree; no correction needed.
- **Recommended change**: None required now. When Bosco does scope the
  dedicated Gavin chapter, note that ch.17 already carries his first
  full-scene appearance, so the new chapter's job is deepening/backstory, not
  a first meeting.
- **Confidence**: High (both sources agree, nothing to fix).
- **Human confirmation required**: No — informational only, useful context
  for whenever Bosco schedules that chapter.

### 1.6 — Carly vs Rachael (cross-reference to canon.md's tracked conflict)

- **Governing file**: `CLAUDE.md`
- **Relevant section**: § 5 Melbourne Era table, "Rachael" row: `| **Rachael**
  | CDP (Italian) | Joe's missus. Assisted plating. |` (line 202)
- **Manuscript evidence**: `chapters/21_TheFrenchChef.md` lines 105, 107,
  223, 235 — all four instances use "Carly," never "Rachael." Source: ch.21
  assessment's Governing-File Reconciliation Findings; `_continuity-register.md`
  Batch 4; manuscript synthesis §17 item 4; `canon.md` § Source conflicts.
- **Affected chapter(s)**: 21
- **Nature of discrepancy**: Direct naming conflict between finished,
  approved prose (Carly, four occurrences) and `CLAUDE.md`'s table (Rachael,
  one occurrence, and the only occurrence of "Rachael" anywhere in the
  repository per `canon.md`).
- **Authoritative source**: Manuscript (Carly) — `canon.md` already reasons
  this out explicitly: finished, approved prose outranks a reference table,
  and there's no reading in which four consistent uses in the actual chapter
  are the error. `canon.md`'s `continuity_check.py` already holds Carly as
  canonical for drafting purposes while still reporting the CLAUDE.md
  disagreement as an open finding.
- **Recommended change**: Update `CLAUDE.md:202` from "Rachael" to "Carly"
  (row and any surrounding prose that assumes "Rachael"), matching what
  `canon.md` already treats as canonical-for-drafting. This is the one
  governing-file edit in this report where the "which name is correct"
  question is close to already answered by the weight of evidence — what's
  outstanding is Bosco's formal sign-off, since `canon.md` states explicitly
  this is his call to make, not an agent's.
- **Confidence**: High that Carly is what the finished prose says; Medium on
  whether Bosco intends to keep "Rachael" as the real name and fix the
  chapters instead (unlikely given four consistent uses, but not this
  report's call).
- **Human confirmation required**: Yes — Bosco specifically. `canon.md` is
  explicit that source conflicts are "reported, never resolved by an agent."

### 1.7 — "Rachael" wording is the only governing-file item touching this
   conflict; canon.md and continuity_check.py also need updating in lockstep

- **Governing file**: `CLAUDE.md` (this row) plus, as a bundled follow-on,
  `canon.md` and `{SKILL_DIR}/scripts/continuity_check.py` per canon.md's own
  standing instruction ("update this file, CLAUDE.md, and continuity_check.py
  together").
- **Relevant section**: canon.md § Source conflicts → "Carly vs Rachael."
- **Manuscript evidence**: Same as 1.6.
- **Affected chapter(s)**: 21
- **Nature of discrepancy**: Same underlying conflict as 1.6; listed
  separately only to flag that fixing `CLAUDE.md` alone would leave
  `canon.md`'s "Still unreconciled" framing and any `continuity_check.py`
  reporting logic pointing at a closed question.
- **Authoritative source**: Manuscript (Carly), per 1.6.
- **Recommended change**: When Bosco decides 1.6, action all three files in
  the same pass — `CLAUDE.md:202`, `canon.md`'s Source-conflicts entry
  (remove or mark resolved), and confirm `continuity_check.py` no longer
  needs to carry this as an open `SOURCE_CONFLICTS` report.
- **Confidence**: High (mechanical follow-through once 1.6 is decided).
- **Human confirmation required**: Same decision as 1.6 — one confirmation
  covers both.

---

## 2. canon.md (`{SKILL_DIR}/references/canon.md`)

### 2.1 — Ivian's gender: clarification, not correction

- **Governing file**: `canon.md`
- **Relevant section**: § People → Pre-kitchen table, Ivian row: "Wing
  cleaner partner | Mopping, bins, extra unlock, extra milk." (no gender
  stated)
- **Manuscript evidence**: `chapters/04_FourFlights.md` — Ivian is named,
  never assigned a pronoun on the page.
- **Affected chapter(s)**: 04
- **Nature of discrepancy**: Not a discrepancy in the normal sense — canon.md
  was never wrong about Ivian, it was simply silent on gender. Bosco has
  since confirmed directly, mid-audit and outside any chapter, that Ivian is
  male (clear from context: the scene is set within a men's prison). Source:
  `_continuity-register.md` "Owner correction — 2026-09-01, mid-audit."
- **Affected governing file passage**: canon.md's Ivian row is silent, not
  incorrect; no wording currently misstates gender.
- **Authoritative source**: Bosco's direct statement — the highest-authority
  source available, and canon.md itself instructs that source conflicts (and,
  by extension, gaps like this) are escalated to him rather than resolved by
  an agent. Since he has already resolved it, this is now settled fact
  awaiting only the mechanical edit.
- **Recommended change**: Add "(male)" or equivalent explicit gender note to
  canon.md's Ivian row, so no future role or drafting pass infers otherwise
  from silence.
- **Confidence**: High — Bosco supplied this directly and unambiguously.
- **Human confirmation required**: Already given (Bosco confirmed this
  directly, mid-audit). No further confirmation needed — this is close to a
  pure "someone go make the edit" item, the most ready of anything in this
  report to action immediately. Per the audit's standing rule, no assessment
  role edits canon.md — a future session (or Bosco himself) makes the change.

### 2.2 — Fine-dining covers figure (50) is now sourced, "Unverified" listing is stale

- **Governing file**: `canon.md` (and, per canon.md's own cross-reference
  instruction, `{SKILL_DIR}/scripts/continuity_check.py`)
- **Relevant section**: § Unverified — "Fine dining covers — 50 on a big
  night," including the note that `continuity_check.py:41` carries
  `fine_dining_covers: 50` in `CANON_FACTS` and `:280–284` raises a `FACT`
  finding against any non-50 fine-dining cover count.
- **Manuscript evidence**: `chapters/18_TheBaseline.md:7` — "Fifty covers on
  a big night," stated in the fine-dining context (matching the section
  canon.md was looking for a source for, as distinct from the "maybe fifty
  seats" at Grant's Auckland kitchen in `drafts/TheEarlyDays.md:417`). Source:
  ch.18 assessment's Governing-File Reconciliation Findings;
  `_continuity-register.md` Batch 3 "New finding — resolves a canon.md
  'Unverified' gap"; manuscript synthesis §17 item 2.
- **Affected chapter(s)**: 18 (source), and indirectly 19 (which references
  the same fine-dining context without introducing a new figure, per the
  ch.19 assessment's Governing-File Reconciliation Findings — confirmed not
  implicated).
- **Nature of discrepancy**: canon.md currently treats any fine-dining
  covers figure in prose as unconfirmed and instructs agents not to write it
  in; the manuscript has since supplied exactly the figure canon.md was
  waiting for, in the right context. `continuity_check.py`'s
  `fine_dining_covers` check is, as canon.md itself already half-anticipates,
  now enforcing a number that's actually supported — but the "Unverified"
  framing and false-positive warning are stale.
- **Authoritative source**: Manuscript (`18_TheBaseline.md:7`) — this is the
  chapter did not introduce an error, it supplied the missing source
  canon.md was explicitly looking for.
- **Recommended change**: Move the fine-dining-covers fact from § Unverified
  into § Hard facts, citing `chapters/18_TheBaseline.md:7`; remove the
  "backwards enforcement" warning against `continuity_check.py`'s
  `fine_dining_covers` check (or rewrite it to confirm the check is now
  correctly grounded); update `continuity_check.py`'s comment/source citation
  for `CANON_FACTS['fine_dining_covers']` to point at the new source instead
  of treating it as unconfirmed.
- **Confidence**: High — the chapter text itself is the source; no
  interpretation required.
- **Human confirmation required**: Low need — the chapter is unambiguous.
  Still recommend a quick Bosco sign-off before editing, consistent with how
  every other canon.md fact-table change in this project has been handled
  (author confirms, then it moves from Unverified to Hard facts).

### 2.3 — ChefTip #5 bold-heading outlier (`20_Goose&Gander.md:55`)

- **Governing file**: `canon.md`
- **Relevant section**: § Source conflicts → "ChefTip heading form — the
  profile against every chapter"
- **Manuscript evidence**: `chapters/20_Goose&Gander.md:55` uses a **bold**
  rule-line, the lone outlier against the italic form used by all six other
  approved ChefTips (`09`, `11`, `12`, `13`, `15`, `18`). Source: ch.20
  assessment's Governing-File Reconciliation Findings; `_continuity-register.md`
  Batch 4 (reconfirmed, not new); manuscript synthesis §17 item 3.
- **Affected chapter(s)**: 20
- **Nature of discrepancy**: Three-way disagreement, not two: the voice
  profile mandates bold + a different heading format entirely
  (`### ChefTip Number X`); `CLAUDE.md:171` also says "bold quotable rule";
  but six of seven approved chapters, plus `CLAUDE.md:155`
  ("`## ChefTip #X`"), agree on italics and the `##`/`#N` form. Ch.20 is the
  single chapter that breaks from its six siblings toward the bold form the
  profile and one other CLAUDE.md line separately specify.
- **Authoritative source**: canon.md already reasons this through — finished,
  approved prose (six of seven chapters) plus `CLAUDE.md:155`'s heading form
  outrank the profile's un-adopted form; canon.md marks `## ChefTip #N` /
  italic rule line as canonical-for-drafting. **Note for Bosco**: `CLAUDE.md`
  is not internally consistent on this — line 155 (ChefTip Structure section)
  says `## ChefTip #X`, but line 171 (Episode Pattern step 6) says "bold
  quotable rule," which is what ch.20 actually did. So ch.20 may not be an
  outlier by accident — it may be the one chapter that followed
  `CLAUDE.md:171` literally.
- **Recommended change**: Two things need Bosco's decision, not one: (a)
  whether ch.20's bold heading gets changed to italic to match its six
  siblings, or the siblings get changed to bold to match ch.20 and
  `CLAUDE.md:171`; (b) reconcile `CLAUDE.md:171`'s "bold" instruction against
  `CLAUDE.md:155`'s and the manuscript's actual `##`/italic practice, since
  right now CLAUDE.md contradicts itself on this point independent of the
  chapter question. `canon.md`'s Source-conflicts entry should be updated to
  note this CLAUDE.md self-contradiction once found, not just the
  profile-vs-manuscript one it currently records.
- **Confidence**: Medium — the "which form wins" question is genuinely
  Bosco's to call, though the fact of the CLAUDE.md internal contradiction
  itself is High confidence (both lines are quoted directly above).
- **Human confirmation required**: Yes — Bosco, since canon.md is explicit
  that source conflicts are never resolved by an agent, and this one now has
  three sources in play (profile, CLAUDE.md self-contradiction, manuscript
  majority) rather than two.

### 2.4 — "Ten ChefTips" (`08_EarningTheRight.md:59`) vs. the eleven-number scheme

- **Governing file**: `canon.md`
- **Relevant section**: § Known repo defects — "'Ten ChefTips' promised,
  eleven numbers reserved"; also § ChefTips table (eleven numbered rows,
  #1–#11).
- **Manuscript evidence**: `chapters/08_EarningTheRight.md:59` — "So here
  they are. Ten ChefTips." Source: ch.08 assessment's Governing-File
  Reconciliation Findings; `_continuity-register.md` Batch 2.
- **Affected chapter(s)**: 08
- **Nature of discrepancy**: The chapter that introduces the ChefTip concept
  to the reader states a different count (ten) than the eleven-slot scheme
  canon.md and `CLAUDE.md` § 4 both carry.
- **Authoritative source**: Undetermined by this audit — already an open
  question in canon.md itself (§ Open questions: "ChefTips #2, #3, #4 —
  content undecided"), and this specific ten-vs-eleven line is separately
  logged as a Known repo defect there. No new resolution is proposed here;
  this item is carried at the same status the individual chapter assessment
  and the manuscript synthesis both already gave it.
- **Recommended change**: None proposed here beyond what canon.md already
  says (flagged, not resolved). Once Bosco decides whether ChefTips #2–#4
  will exist as separate entries or the scheme collapses to ten, ch.08's
  line and the eleven-row table both get reconciled together in one pass.
- **Confidence**: Low on resolution direction (genuinely open); High that the
  discrepancy itself exists and is correctly already tracked.
- **Human confirmation required**: Yes — Bosco, and it's coupled to the
  larger #2/#3/#4 content decision, not a standalone fix.

### 2.5 — Melbourne-era minor characters (cross-reference to §1.1/1.2/1.3)

- **Governing file**: `canon.md`
- **Relevant section**: § People → Melbourne table (no Scotty/Raj/Dylan rows)
- **Manuscript evidence / nature / recommendation**: Identical to CLAUDE.md
  items 1.1–1.3 above — canon.md's Melbourne table has the same gap
  `CLAUDE.md` § 5 does, for the same three names. Recorded once here as a
  cross-reference rather than repeating the full entry; when Bosco actions
  1.1–1.3 in `CLAUDE.md`, the matching rows should go into `canon.md` in the
  same pass (canon.md is the more detailed, source-cited table of the two).
- **Confidence / human confirmation**: Same as 1.1 (Scotty/Raj: High
  confidence, no confirmation strictly needed) and 1.2 (Dylan: Low
  confidence, Bosco confirmation required).

---

## 3. `planning/decision-ledger_2026-08-30.md`

### 3.1 — B15 (`03_FreshForUnlock.md` dual-H1) — already tracked, no new action

- **Governing file**: `planning/decision-ledger_2026-08-30.md`
- **Relevant section**: § B15 · `03_FreshForUnlock.md` — two H1s · OPEN
  (line 543): "Carries `# FRESH FOR UNLOCK` and `# GENERAL POPULATION`. Every
  other chapter has one. **A** one chapter — drop the second to `##` · **B**
  two chapters — GENERAL POPULATION becomes **05**, closing one gap"
- **Manuscript evidence**: `chapters/03_FreshForUnlock.md` — confirmed
  present exactly as ledger B15 describes, `# GENERAL POPULATION` at line 185.
  Source: ch.03 assessment's Governing-File Reconciliation Findings;
  `_continuity-register.md` Batch 1; manuscript synthesis §17 item 8.
- **Affected chapter(s)**: 03 (and, if option B is chosen, the numbering
  scheme for ch.05)
- **Nature of discrepancy**: None newly found — this is the ledger's own
  open item, confirmed present in the text exactly as already described.
- **Authoritative source**: N/A — nothing to reconcile, both option A and B
  are already correctly stated as live choices in the ledger.
- **Recommended change**: No new recommendation. Already tracked; belongs in
  this report only as a cross-reference confirming the audit did not find
  anything the ledger doesn't already know. Bosco picks A or B whenever he's
  ready.
- **Confidence**: High that the item is accurately described and unresolved.
- **Human confirmation required**: Yes (already understood to be his call —
  not new information from this audit).

### 3.2 — B22 (Marco composite disclosure) — already tracked, restated for completeness

- **Governing file**: `planning/decision-ledger_2026-08-30.md`
- **Relevant section**: § B22 · Disclose the composite · OPEN (line 652); see
  also `CLAUDE.md` § 5 "Composites and disguises" table, Marco row.
- **Manuscript evidence**: `chapters/08_EarningTheRight.md` and
  `chapters/14_TheOnesWhoStay.md` both carry Marco content (the
  animal-breakdown line in 08; the cut-himself-and-kept-flipping-steaks scene
  in 14) with no on-page signal to the reader that this is composited/borrowed
  material (per `canon.md`'s CANON note, the event is really Geoffrey's
  story). Source: ch.08 and ch.14 assessments' Governing-File Reconciliation
  Findings; manuscript synthesis §17 item 11.
- **Affected chapter(s)**: 08, 14
- **Nature of discrepancy**: None newly found — B22 is already open in the
  ledger exactly as described. Recorded here because this audit is the first
  to actually read both chapters where the undisclosed composite appears on
  the page, confirming the open question is live in both, not just one.
- **Authoritative source**: N/A.
- **Recommended change**: No new recommendation beyond what B22 already
  frames (disclose or not — Bosco's call). Worth noting for him that the
  choice touches two chapters, not one.
- **Confidence**: High that both instances are present and undisclosed;
  Low/not-applicable on which way B22 should resolve.
- **Human confirmation required**: Yes (already his call per the ledger).

---

## 4. `planning/writing-plan_v1.4.0.md`

### 4.1 — B30 foreshadowing tension in `07_Chicken&Mash.md`'s closing paragraph

- **Governing file**: `planning/writing-plan_v1.4.0.md`
- **Relevant section**: § PART SEVEN: AFTER THE LADDER, rule 1 (line 286):
  "No career chapter anticipates the death. No shadow, no foreshadowing,
  no..." — the B30 no-foreshadowing rule, cross-referenced in `CLAUDE.md`'s
  closing structural ruling ("No career chapter foreshadows the death").
- **Manuscript evidence**: `chapters/07_Chicken&Mash.md`, closing paragraph:
  "I didn't know yet what that would cost. What I'd give up. What I'd miss.
  The birthdays and anniversaries and ordinary Tuesday nights that would slip
  past while I stood over a hot stove, chasing something I couldn't quite
  name." Source: ch.07 assessment's Governing-File Reconciliation Findings
  (verbatim quote and classification); `_continuity-register.md` Batch 2;
  manuscript synthesis §17 item 6.
- **Affected chapter(s)**: 07
- **Nature of discrepancy**: The line never names a person, a child, or a
  loss — on its face it's generic career-cost reflection, a legitimate,
  voice-consistent theme in its own right. But the specific phrasing
  ("birthdays and anniversaries," "ordinary Tuesday nights that would slip
  past") reads uncannily close to dramatic irony aimed at Jackson's death,
  which the B30 ruling explicitly forbids in any career chapter. This is the
  first chapter after the origin arc where the binding B30 rule applies, so
  the audit is flagging it deliberately rather than assuming either reading.
  **This item's classification is carried through unchanged from Batch 2**:
  it was ambiguous when first flagged and remains ambiguous — this report
  does not upgrade it to a confirmed violation or downgrade it to a
  non-issue, per the task's instruction to carry it at the same confidence
  level.
- **Authoritative source**: Neither — genuinely a **Continuity issue**
  (per the audit's taxonomy: neither source is safely authoritative without
  Bosco reconciling them). The rule is accurate and current; whether the
  chapter actually violates it is a judgment only Bosco can make, since it
  turns on authorial intent he alone knows.
- **Recommended change**: No edit proposed. Recommend Bosco read this
  specific paragraph against the B30 rule directly and decide: (a) leave as
  is (generic reflection, not a violation), or (b) soften/generalise the
  phrasing further so it can't be read as pointed at a specific later loss.
- **Confidence**: Medium — real and specific enough to be worth flagging, but
  the "is this actually a violation" question is inherently unresolvable by
  audit alone (stated at Medium in the original finding; not moved to High or
  Low here).
- **Human confirmation required**: Yes — Bosco specifically, since this
  touches his own family history and only he knows whether the phrasing was
  written with Jackson in mind.

### 4.2 — B30 rule confirmed intact and unbroken elsewhere (no action needed)

- **Governing file**: `planning/writing-plan_v1.4.0.md`
- **Relevant section**: Same B30 rule as 4.1
- **Manuscript evidence**: `_continuity-register.md` Batch 4 confirms
  chapters 19–21 contain no career-arc foreshadowing of Jackson's death,
  "consistent with the B30 boundary ruling. The Yulara/no-shadow rule holds
  through the end of the currently-written manuscript."
- **Affected chapter(s)**: 19, 20, 21 (clean)
- **Nature of discrepancy**: None. Recorded only for completeness, so this
  report doesn't read as silent on the rest of the manuscript's B30
  compliance — everything outside ch.07 checked clean.
- **Authoritative source**: N/A.
- **Recommended change**: None.
- **Confidence**: High.
- **Human confirmation required**: No.

---

## 5. `context/chef-writer-context-profile.md`

No new discrepancy is recorded here beyond the two items already fully
compiled under canon.md above, since canon.md is where the profile-vs-
manuscript conflicts are tracked in this project's own architecture:

- The **ChefTip heading form** conflict (profile mandates bold +
  `### ChefTip Number X`; manuscript and most of `CLAUDE.md` use italic +
  `## ChefTip #N`) — see **2.3** above, which also surfaces a `CLAUDE.md`
  internal self-contradiction on this same point not previously isolated in
  any single chapter assessment.
- The **book title** conflict (`context/chef-writer-context-profile.md`
  describes itself as reproducing the voice of *Diary of an Apprentice*;
  `CLAUDE.md` and everything else say *Diary of a Chef*, now further
  superseded by the 30 Aug 2026 retitling to *The Long Road To Nowhere*) —
  this was not raised as a new finding in any of the 19 individual
  assessments or the continuity register, so it is not compiled as a fresh
  item here; it is already logged in `canon.md` § Known repo defects and §
  Open questions, and per this report's brief is cited only, not re-raised.

No individually-flagged chapter finding in this audit implicates any other
part of the voice profile.

---

## 6. `context/SOURCES.md`

No governing-file reconciliation finding in any of the 19 chapter assessments,
the continuity register, or the manuscript synthesis names `SOURCES.md`. No
item is recorded in this section — checked per the task's input list, nothing
found to compile.

---

## 7. Items explicitly NOT re-reported here (already tracked elsewhere, no new action)

Per the task brief, the following are cross-referenced only, not treated as
fresh findings, to avoid double-counting against work already logged
elsewhere in the project:

| Item | Where it's tracked | Status here |
|---|---|---|
| Ch.03's dual-H1 structure | Ledger B15 | See §3.1 above — restated as a cross-reference only |
| Ch.04's missing closing line ("Same board. Same day. Different histories.") | "Also on the list, not blocking" per prior review | Not re-flagged; noted in `_continuity-register.md` Batch 1 as open but not newly actioned here |
| Inherited mojibake across chapters | `canon.md` § Known repo defects (encoding_check.py) | Not re-flagged; confirmed still present at the counts canon.md already logs, per Batches 3 and 4 |
| Carly/Rachael conflict | `canon.md` § Source conflicts | Elevated in this report at §1.6/§1.7/§2 cross-ref because it's the one item close to a clean resolution — not a new discovery, but carried forward with a concrete recommended edit since the evidence is unusually one-sided |
| Ch.15 heading/title mismatch (`# TASTE IT` vs. full canon title) | `canon.md` § Known repo defects | Not re-flagged as new; confirmed present, no new recommendation beyond canon.md's existing entry |

---

## Summary

**Total discrepancies compiled**: 13 distinct items across 4 governing files
(CLAUDE.md: 7 including cross-references; canon.md: 5 including
cross-references; decision-ledger: 2; writing-plan: 2 — several items are
cross-referenced between files rather than double-counted, so the true count
of distinct underlying issues is 11: Ivian gender clarification, Ivian
introduction gap, fine-dining covers, ChefTip #5 bold outlier +
CLAUDE.md self-contradiction, "Ten ChefTips," Carly/Rachael, Scotty/Raj
table gap, Dylan identity ambiguity, unnamed exec sous, B15 dual-H1
cross-ref, B22 composite cross-ref, B30/ch.07 foreshadowing tension).

**Confidence breakdown**:
- **High**: Ivian gender clarification (2.1); fine-dining covers (2.2);
  Scotty/Raj table gap (1.1/2.5); Gavin cross-check (1.5, no action needed);
  B15 and B22 cross-references (3.1, 3.2 — tracked accurately, not new);
  B30 clean elsewhere (4.2, no action needed); CLAUDE.md internal
  self-contradiction on bold vs. italic ChefTip form (part of 2.3).
- **Medium**: Carly vs Rachael resolution direction (1.6/1.7 — which name
  wins is asked of Bosco, though the evidence leans hard toward Carly);
  ChefTip #5 form resolution direction (2.3); B30/ch.07 foreshadowing
  tension (4.1).
- **Low**: Dylan's identity (1.2); "Ten ChefTips" resolution direction (2.4,
  coupled to the larger #2–#4 content decision); unnamed exec sous (1.3, not
  actionable without a name).

**Single item most ready for Bosco to close immediately**: **§2.1, the
Ivian gender clarification in canon.md.** He has already supplied the answer
directly and unambiguously (mid-audit, recorded in
`_continuity-register.md`'s "Owner correction" section); the canon.md row
was never wrong, only silent; and the fix is a one-line addition
("(male)" or equivalent) to an existing table row with no further
investigation, drafting, or decision-making required from him — he's already
decided it.
