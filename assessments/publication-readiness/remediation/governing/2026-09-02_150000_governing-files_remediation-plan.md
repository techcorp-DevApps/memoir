# Governing-Files Remediation Plan

**Companion to**: `assessments/publication-readiness/remediation/master/2026-09-02_150000_complete-manuscript_publication-remediation-plan.md`
**Starting point**: `assessments/publication-readiness/2026-09-01_231520_governing-files_manuscript-reconciliation.md` (Phase 6), reconciled against this session's own direct read of every governing file named below.

For each item: whether manuscript evidence is sufficient to update the file now, whether the update should happen before or after manuscript editing, whether Bosco's confirmation is required, and which chapters depend on it. No governing file is edited by this plan — it is a plan for later action.

---

## `CLAUDE.md`

`CLAUDE.md` is this repository's actual authoritative governing file — every other document (the profile, project-memory, the ledger, the writing plan) either derives from it or should be reconciled to it, not the reverse.

| REM | Item | Manuscript evidence sufficient? | Before/after manuscript editing? | Bosco confirmation required? | Chapters depending on it |
|---|---|---|---|---|---|
| REM-032 | Carly vs Rachael | Yes — four consistent chapter uses vs. one table row | **Before** — the table should catch up to already-approved prose, not the reverse | Formal sign-off requested, though evidence leans hard toward Carly | 21 |
| REM-033 | Scotty/Raj missing rows | Yes — first appearances unambiguous in ch.21 | Before (pure addition, no conflict to resolve) | Not strictly required | 21 |
| REM-016 | Dylan row | **No** — the manuscript itself doesn't disambiguate who Dylan is | Must wait until **after** the chapter clarification (or non-clarification) is decided | Required — only Bosco knows the intended reading | 21 |
| REM-031 | ChefTip #5 bold outlier + CLAUDE.md self-contradiction (lines 155 vs 171) | Partially — the self-contradiction is directly quotable and certain; which form should win is not | Before any further ChefTip chapters are drafted (so #2–#4, once placed, don't inherit an unresolved format question) | Required | 09, 11, 12, 13, 15, 18, 20 (all seven ChefTip chapters, for consistency once resolved) |
| REM-036 | Ivian gender + fine-dining covers (moved here from unreachable `canon.md`) | Yes for both — Bosco supplied the gender directly; `18_TheBaseline.md:7` supplies the covers figure directly in approved prose | Before — both are settled facts waiting only on the mechanical edit | Ivian: already given, no further confirmation needed. Covers: low need, but recommend a quick sign-off per how every other canon-fact promotion in this project has been handled | 04 (Ivian), 18 (covers) |
| REM-037 | PART ONE name | No — this is a naming choice, not evidence-derivable | Whenever Bosco decides; not blocking any other item | Required | None directly (affects framing only) |
| REM-041 | Jen's rank (B13) | No — genuinely three-way open (`CLAUDE.md` commis / superseded `manuscript-structure` CDP / chapter silent) | After Bosco decides; no urgency | Required | 19 |
| REM-044 | Geoffrey/Geoffery spelling (B21) | No — two sources disagree, neither self-evidently right | Whenever decided; no chapter currently prints either spelling | Required | None yet (future chapters only, if he's ever named on the page) |
| REM-047 | §9 repository-structure diagram (stale, describes a `/manuscript/part-1-origin/` tree that doesn't exist) | Yes — directly confirmed against this session's own repo listing | **After** other batches, so the diagram doesn't need updating twice as files move (e.g. if the 09 filename typo is fixed, if 05/06 are split) | Not required — purely descriptive/mechanical | None |

**Sequencing note**: Bundle every `CLAUDE.md` edit above into **one pass** once its prerequisite decisions land (per the master plan's Batch 1), rather than editing the file repeatedly across the remediation window — `CLAUDE.md` is read at the start of every future session and should not be left in a half-updated state between batches.

---

## `canon.md` (external — not in this repository)

**This file cannot be remediated from within this repository.** It is a reference bundled with the memoir-studio Claude Code skill (`references/canon.md` inside that skill's own directory), confirmed absent from every location in `techcorp-DevApps/memoir` by this session's own repository listing, and flagged as such in a note added to every 2026-09-01 assessment file after an automated PR reviewer correctly caught the unverifiable citations.

| Item | Disposition |
|---|---|
| Ivian's gender clarification | Redirected to `CLAUDE.md` §5 — see REM-036 above. Not actionable in `canon.md` from this session. |
| Fine-dining-covers reclassification | Redirected to `CLAUDE.md` §6 — see REM-036 above. |
| ChefTip #5 outlier note | The underlying question is redirected to `CLAUDE.md` — see REM-031. `canon.md`'s own copy of this note, if it still exists in the skill directory, is untouched by this plan and will read as slightly behind `CLAUDE.md` once REM-031 resolves; this is a known, accepted limitation of a two-location canon system, not something this plan can close. |
| "Ten ChefTips" known-defect entry | The underlying question is redirected to `planning/writing-plan_v1.4.0.md` (REM-023/042). Same limitation as above. |
| Encoding-defects table (per-chapter mojibake counts) | Once REM-028 closes (all mojibake repaired), `canon.md`'s counts would read as stale. Cannot be updated from here. |

**Recommendation to Bosco (not an action this plan can take)**: decide whether to bring an equivalent reference into `context/` (e.g. `context/canon.md`), so future sessions without the memoir-studio skill installed can still verify these facts in-repo, or to consciously accept that canon-fact tracking will continue to live partly outside the repository. Either way, future assessment work should stop citing `canon.md` as if it were a repo-governed file without this same caveat — the note already added to the 2026-09-01 assessment files is the right model to follow going forward.

**Before/after manuscript editing**: N/A — no in-repo action exists to sequence.

---

## `planning/decision-ledger_2026-08-30.md`

This is the correct home for every Bosco-only decision this plan generates. It already has the right format (keyed items, `OPEN`/`ANSWERED: <key>`/`DEFERRED`, dated rulings) — **recommend every Batch-0 decision in the master plan be recorded here, using new keys where none exists**, rather than inventing a separate decision-tracking mechanism.

| REM | Ledger key | Manuscript evidence sufficient? | Before/after? | Confirmation required? | Chapters |
|---|---|---|---|---|---|
| REM-020 | B15 (existing) | No — genuinely a structural author's choice | Before REM-026 execution if Option B is chosen | Required (already understood to be his call) | 03, prospectively 05 |
| REM-021 | New key needed (recommend "B34") | No — turns entirely on authorial intent re: Jackson | **Before any edit to ch.07** | Required, and this is the single highest-sensitivity item in this whole plan | 07 |
| REM-024 | B22 (existing) | No — a disclosure-policy choice, not a fact | Before either chapter is touched for this reason | Required | 08, 14 |
| REM-016 | New key needed (recommend "B35") | No | Before the CLAUDE.md Dylan row and before any chapter clarification is added | Required | 21 |
| REM-019 | Existing ledger note ("Also on the list, not blocking") — promote to a keyed item (recommend "B36") | No — requires Bosco's memory of his own prior editorial intent | Before any restoration | Required | 04 |
| REM-023 | Coupled to the existing ChefTip-ladder open items (#2–#4) — no dedicated key yet; recommend "B37" | No | After #2–#4 placement is decided | Required | 08 |
| REM-041 | B13 (existing) | No | Whenever decided | Required | 19 |
| REM-044 | B21 (existing) | No | Whenever decided | Required | None yet |
| REM-037 | New key needed (recommend "B38") | No | Whenever decided | Required | None directly |

**Before/after manuscript editing**: every ledger item above must be answered **before** its corresponding REM item's execution step — this is already how the ledger is designed to work (its own header: "one at a time. Answer with the key. Nothing is resolved by any role.").

---

## `planning/writing-plan_v1.4.0.md`

| REM | Item | Manuscript evidence sufficient? | Before/after? | Confirmation required? | Chapters |
|---|---|---|---|---|---|
| REM-023/042 | ChefTips #2–#4 placement and "Ten ChefTips" reconciliation | No | Before REM-023's ch.08 edit | Required | 08, and wherever #2–#4 eventually land |
| REM-020 (Option B) | If ch.03 splits, the Part One table gains a new row | Depends on REM-020's decision | After REM-020/REM-026 resolve | Required | 03, prospectively 05 |
| REM-026 | 05/06 split | The draft material's *existence* is confirmed; its *readiness to promote* is not — the plan itself flags the first third of `drafts/TheEarlyDays.md` as superseded (age-23 material) | This is a drafting/promotion task; the writing plan is updated **after** the split executes, not before | Required (promotion is explicitly reserved to Bosco per the project's own process) | 04, 07 (both bridge chapters) |
| REM-037 | PART ONE name | No | Whenever decided | Required | None directly |

**Note**: `planning/writing-plan_v1.4.0.md` is itself current and internally coherent — this plan found no defect in it, only downstream consequences of decisions tracked elsewhere (the decision ledger) that will eventually require an edit here once those decisions land. No standalone action is owed to this file today beyond what the table above already routes through the ledger.

---

## `planning/manuscript-structure_v1.3.0.md`

**Explicitly superseded** per `context/SOURCES.md` ("Superseded, do not quote as current... both close at #23") and per `planning/writing-plan_v1.4.0.md`'s own paired-document note ("NOT yet updated to match"). This plan recommends no edit to this file — it is scheduled for a full v1.5.0 replacement once the numbering work (REM-020, REM-026) executes, per the writing plan's own §Numbering section ("both planning documents go to v1.5.0 against the new sequence"). Editing the v1.3.0 file now would create a third, briefly-current-then-immediately-stale version — not a good use of remediation effort. **Recommendation: leave as-is until REM-026 executes, then retire it in favour of a v1.5.0 document, not patch it forward.**

---

## `context/chef-writer-context-profile.md`

| REM | Item | Manuscript evidence sufficient? | Before/after? | Confirmation required? | Chapters |
|---|---|---|---|---|---|
| REM-039 | Book-title conflict ("Diary of an Apprentice") | Yes — `CLAUDE.md` unambiguously states the current title | Before this file is next referenced by a drafting session | Not required — this is a pure staleness fix, no judgment call | None directly (affects every future session's self-orientation) |
| REM-040 | Encoding damage throughout front matter and body | Yes — visible directly in this session's own read | Bundle with REM-039 (same file, one edit) | Not required | None directly |
| REM-031 | ChefTip heading form (`### ChefTip Number X` / bold, never adopted by any chapter) | Partially — the fact that zero chapters use this form is certain; whether the profile should change to match practice, or the manuscript should change to match the profile, is Bosco's call | After REM-031's `CLAUDE.md`-side decision lands, in the same pass | Required (shared decision with REM-031) | 09, 11, 12, 13, 15, 18, 20 |

**Note**: the substantive voice-profile content (identity blend, tonal foundations, structural patterns, the Hard "No" List) is not in question anywhere in the audit or this plan — every voice-remediation strategy in the master plan cites this file as accurate and current. The only issues here are self-identification staleness (title, encoding) and one shared formatting-convention question. This file should not be substantively rewritten.

---

## `context/project-memory.md`

| REM | Item | Manuscript evidence sufficient? | Before/after? | Confirmation required? | Chapters |
|---|---|---|---|---|---|
| REM-045 | Conflicts with `CLAUDE.md` on title, Dave-arc status, editorial score/word count, ChefTip progress state | Yes — directly cross-checked against `CLAUDE.md`'s current state in this session | **After** other governing-file edits settle (REM-037's PART ONE name, REM-032's Carly/Rachael, etc.), since this file is meant to be a condensed summary derived from `CLAUDE.md`, not an independent source | Recommend Bosco review the regenerated summary before it's treated as current, though the underlying facts to reconcile against are already settled in `CLAUDE.md` | None directly |

**This is a genuine, high-impact governing-file finding this plan validated directly rather than inheriting from the prior audit's reports** — none of the 21 chapter assessments or the governing-files reconciliation report names `context/project-memory.md` specifically (its Sources Reviewed list correctly did not require re-reading it, since the prior audit's scope was chapter-vs-canon reconciliation, not a full governing-file health check). This plan's broader instruction — read every governing file in full — surfaced it. **Recommend regenerating this file's Current State and On the Horizon sections from `CLAUDE.md` directly** rather than hand-patching individual sentences, since the drift is broad enough (title, a whole character-arc's status, a stale editorial score) that patching risks leaving other undetected disagreements in place.

The decision ledger's own "Also on the list, not blocking" note — "`project-memory.md` exists at repo root **and** at `context/`. One is authoritative" — was checked directly against this session's own repository listing: **no root-level copy was found.** This suggests that specific duplication may already be resolved, but this plan did not run an exhaustive full-tree search to confirm no copy exists under a different path, so it is recorded as "likely resolved, worth a final confirmation" rather than closed outright.

---

## `context/SOURCES.md`

No governing-file reconciliation finding in any of the 21 chapter assessments, the continuity register, or the manuscript synthesis names this file, and this plan's own direct read found it internally consistent, current (dated 30 Aug 2026), and doing exactly the job it describes (flagging what's off-repo and what supersedes what). **No action recommended.** It is, if anything, a model for how `context/project-memory.md` (REM-045) should eventually read once refreshed — clear about what's current, what's superseded, and why.

---

## Governing-file edit sequencing (summary)

1. **Decisions land first** (`planning/decision-ledger_2026-08-30.md` — new and existing keyed items, per the table above). No governing-file *content* edit happens before its corresponding decision is recorded.
2. **`CLAUDE.md`** — one consolidated edit pass, incorporating every decided item above, done after the corresponding chapter-level facts (Dylan's identity, the 05/06 split status) are also settled where the two are coupled.
3. **`context/chef-writer-context-profile.md`** — one consolidated edit pass (title + encoding + ChefTip form, once decided).
4. **`context/project-memory.md`** — regenerated last among the governing files, once `CLAUDE.md` itself reflects every other decision, so it summarises a settled state rather than a moving one.
5. **`planning/writing-plan_v1.4.0.md`** — updated only as a consequence of REM-026/REM-020/REM-023 executing, not on its own timeline.
6. **`planning/manuscript-structure_v1.3.0.md`** — left untouched; retired in favour of a v1.5.0 successor once REM-026 executes.
7. **`canon.md`** — no in-repo action possible; Bosco's decision on bringing an equivalent into `context/` is the only lever available.

---

*End of governing-files remediation plan.*
