# Chapter Identification
- Chapter number: 18
- Chapter title: THE BASELINE
- Source file(s): `chapters/18_TheBaseline.md`
- Intended manuscript position: PART THREE: TRANSITION / AUSTRALIA, § 12 — ChefTip #6
- Assessment date/time: 2026-09-01 23:15

> **Note on `canon.md` citations in this file, added 2026-09-02:** an
> automated PR reviewer (Codex) correctly flagged that `canon.md` does not
> exist anywhere in this repository, so its citations below could not be
> verified by anyone reading only `techcorp-DevApps/memoir`. This is accurate
> and worth being explicit about: `canon.md` is a reference file bundled with
> the **memoir-studio Claude Code skill** that produced this audit
> (`references/canon.md` inside that skill's own directory, not this
> project). It was read directly, for real, during this audit — the citations
> reflect actual content, not invention — but it is external to this repo and
> only accessible to a session with that skill installed. Treat every
> `canon.md` citation below as traceable only via the skill, not via this
> repository alone, until/unless Bosco decides to bring an equivalent
> reference into the repo itself (e.g. under `context/`).

# Publication Readiness Scorecard
| Criterion | Rating /5 | Status | Key Finding |
|---|---|---|---|
| Context Profile Accuracy | 5 | Publication Ready | The "coast or hold the standard" choice is rendered through specific behaviour, not moralised at the reader |
| Voice Standard Adherence | 5 | Publication Ready | No stated-emotion or forced-epiphany constructions found; ChefTip block's explicit thesis is structurally appropriate to the form |
| Context Realism | 5 | Publication Ready | Promotion timeline (CDP +4mo, Junior Sous +6mo, CDC ~2yr) matches canon exactly |
| Reading Quality | 5 | Publication Ready | Confident, well-paced career-milestone chapter |
| Natural Flow | 5 | Publication Ready | Clean movement from arrival, to the "coast" temptation, to Kein Do's notice, to the promotion cascade |
| Exiting Bridge | Strong | — | ChefTip close ("When the kitchen gets easier, your standard doesn't. Protect it.") functions as a craft-statement close, appropriate to the form |
| Chapter Bridge | Strong | — | Direct continuity into 19 (COAST OR CLIMB, per the writing plan) — same CDC promotion, same bistro |
| Entry Bridge | Strong | — | Opens directly from ch.17's transfer ("The fine dining kitchen changed everything") — no redundant recap, direct causal pickup |
| Internal Continuity | 5 | Publication Ready | Self-consistent |
| Cross-Manuscript Continuity | 5 | Publication Ready | Matches CLAUDE.md and canon.md's sequence exactly; see Governing-File Reconciliation for a new fact this chapter supplies |
| Publication Standards | 5 | Publication Ready | Clean |

Overall readiness score: 5/5 across every criterion. No critical defect found. This is the batch's clear standout alongside `15_TasteIt.md`.

# Context Profile Assessment
The chapter's central tension — "when the kitchen doesn't demand your standard, you have a choice" — is developed through specific, lived detail rather than moralising: the vineyard's from-scratch-everything baseline (potatoes, onions, garlic, stocks, bread, pasta, all made in-house), contrasted against the fine-dining kitchen's stewarding infrastructure and shorter hours. The narrator's decision not to coast is grounded in identity, not performance: "It was just... me. / The way I set up a board... Those weren't habits. They were identity" (lines 73–77) — this is interiority rendered through the accumulation of specific, previously-established habits (the damp cloth under the board, from ChefTip #11) rather than a declared emotion.

# Voice Standard Assessment
No introduced defects. The chapter does state its thesis directly in the ChefTip block ("Your standard is yours. Protect it") — but this is structurally correct for the ChefTip form, which explicitly calls for a stated, quotable rule (§5.1.6, §10 of the profile) — unlike the "I realised" constructions flagged in 13 and 14, which occur mid-narrative rather than in the designated instructional block. The narrative portion proper stays in show-don't-tell mode throughout.

# Context Realism Assessment
The promotion sequence is precise and matches `canon.md`'s Sequence table exactly: CDP at 4 months after arrival (line 109; canon cites `18_TheBaseline.md:109`), Junior Sous 6 months after that (line 111; canon cites `:111`), CDC roughly 2 years after arrival at age 24 (lines 113–125; canon cites `:113`, `:125`). Kein Do's characterisation ("didn't yell. Didn't need to. The kitchen moved around him like water around a stone," lines 13) matches CLAUDE.md § 5 and `canon.md`'s anchors precisely.

# Reading Quality Assessment
Strong, confident chapter. The "how do you go from Demi to CDC in two years" framing (lines 127–149) risks reading as an explained-thesis passage but earns it by immediately grounding the answer in specific, repeated behaviour ("I held the standard when no one was asking me to") rather than abstraction — and this passage sits inside territory the ChefTip form explicitly licenses (the chapter is building directly toward its ChefTip block, unlike 14's non-ChefTip essay which explained its thesis without that structural cover).

# Natural Flow Assessment
Clean throughout — arrival, contrast with the vineyard, the coasting temptation, Kein Do's quiet notice, the promotion cascade, the ChefTip. No structural issues.

# Chapter Connection Assessment

## Exiting Bridge
Strong. The ChefTip's closing lines function as a thematic capstone appropriate to the form, not a narrative cliffhanger — correct for a ChefTip Episode.

## Bridge
Direct continuity into 19 (COAST OR CLIMB, per `writing-plan_v1.4.0.md` § PART THREE) — same CDC promotion, same bistro, continuing the career arc.

## Entry Bridge
Strong. Opens directly from ch.17's transfer announcement with no redundant recap ("The fine dining kitchen changed everything. / Same resort. Same red dirt outside...") — orients the reader instantly while picking up exactly where 17 left off.

# Continuity Assessment
No contradictions found against the register, `CLAUDE.md`, or `canon.md`. All promotion timeline facts (CDP +4mo, Junior Sous +6mo, CDC ~2yr, age 24) match canon precisely — see Context Realism above. Kein Do fully named and characterised here, consistent with his unnamed first appearance in ch.17.

**New fact for the register, and a governing-file reconciliation finding — see below:** line 7 states "Fifty covers on a big night" for the fine-dining restaurant. This directly resolves a gap flagged in `canon.md` § Unverified: canon.md currently states "no chapter states [fine-dining covers of 50]" and calls `fine_dining_covers: 50` an unverified figure carried only by `continuity_check.py` and an earlier canon file, distinct from the "fifty seats" at Grant's Auckland kitchen (`drafts/TheEarlyDays.md:417`). That claim is now out of date: `18_TheBaseline.md:7` supplies the figure directly, in the fine-dining context canon.md was looking for. This should be reported to Bosco/the reconciliation phase as a governing-file update, not silently corrected here.

# Publication Standards Assessment
**Developmental:** None found.
**Line-editing:** None found.
**Copy-editing:** Inherited mojibake present (`canon.md` logs `18_TheBaseline` at 15 issues, the highest count in this batch) — not introduced, not a new finding.
**Proofreading:** None beyond the above.

# Governing-File Reconciliation Findings
**Governing-file issue.** `{SKILL_DIR}/references/canon.md` § Unverified currently states no chapter supports a fine-dining covers figure of 50 and instructs "do not write these into prose. Confirm with Bosco first" and flags `continuity_check.py`'s `fine_dining_covers: 50` check as enforcing a number canon does not support. `18_TheBaseline.md:7` ("Fifty covers on a big night") now directly supports that exact figure in a fine-dining context. This chapter did not introduce an error — it supplies the missing source canon.md was looking for. Recommend the Phase 6 reconciliation report flag `canon.md`'s Unverified entry and the corresponding `continuity_check.py` note as needing an update to cite `18_TheBaseline.md:7` as the source and remove the "unverified" classification, rather than continuing to treat any fine-dining-covers figure in prose as a false positive.

# Critical Issues
No critical publication blockers identified.

# Recommended Revisions
## Required before publication
- None.

## Recommended improvement
- None specific to this chapter's prose.

## Optional editorial refinement
- None.

# Readiness Overview
This chapter is the batch's clear standout alongside `15_TasteIt.md` — a confident, well-paced career-milestone chapter that renders its central theme (protecting your standard when nobody's enforcing it) through specific, accumulated behaviour rather than declaration, and matches the manuscript's canonical timeline exactly at every checkable point. It also resolves a genuine open question in `canon.md` (the fine-dining covers figure) that the reconciliation phase should act on. Authentically in the established narrator's voice throughout; no revision needed.

# Final Status
PUBLICATION READY
