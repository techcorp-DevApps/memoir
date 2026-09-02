# Publication Remediation — Execution Matrix

**Companion to**: the master plan and governing-files plan in this same remediation directory. Status column reflects repo state as of this plan's authoring (2026-09-02) — `PLANNED` unless direct evidence showed otherwise (none did; no batch has executed yet).

| Order | Batch | REM ID | Severity | Priority | Chapter/File | Dependency | Action Type | Validation | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | REM-036 | HIGH | P0 | `CLAUDE.md` §5/§6 | none | Decision + mechanical addition | Two new facts cite manuscript source lines | PLANNED |
| 2 | 0 | REM-021 | HIGH | P1 | `chapters/07_Chicken&Mash.md` | none | Bosco read/decision only | Recorded in decision ledger (new key) | PLANNED |
| 3 | 0 | REM-020 | MEDIUM | P1 | `chapters/03_FreshForUnlock.md` | none | Decision (A or B) | Ledger B15 answered | PLANNED |
| 4 | 0 | REM-023 | MEDIUM | P1 | `chapters/08_EarningTheRight.md` | REM-042 | Decision | Ledger new key answered | PLANNED |
| 5 | 0 | REM-042 | LOW | P2 | none yet | none | Decision (future scope) | Writing-plan ladder table updated once placed | PLANNED |
| 6 | 0 | REM-024 | MEDIUM | P1 | `chapters/08_EarningTheRight.md`, `chapters/14_TheOnesWhoStay.md` | none | Decision (ledger B22) | Ledger B22 answered | PLANNED |
| 7 | 0 | REM-031 | MEDIUM | P1 | `CLAUDE.md`, `context/chef-writer-context-profile.md` | none | Decision | Ledger new key answered | PLANNED |
| 8 | 0 | REM-032 | MEDIUM | P1 | `CLAUDE.md` §5 | none | Decision (sign-off) | Ledger B12 answered | PLANNED |
| 9 | 0 | REM-016 | MEDIUM | P1 | `chapters/21_TheFrenchChef.md` | none | Decision | Ledger new key answered | PLANNED |
| 10 | 0 | REM-019 | LOW | P1 | `chapters/04_FourFlights.md` | none | Decision | Ledger note promoted/answered | PLANNED |
| 11 | 0 | REM-037 | LOW | P2 | `CLAUDE.md`, `planning/writing-plan_v1.4.0.md` | none | Decision (naming) | Ledger new key answered | PLANNED |
| 12 | 0 | REM-039 | MEDIUM | P1 | `context/chef-writer-context-profile.md` | none | Decision not required (mechanical) | — | PLANNED |
| 13 | 0 | REM-041 | LOW | P2 | `CLAUDE.md` §5 | none | Decision (ledger B13) | Ledger B13 answered | PLANNED |
| 14 | 0 | REM-044 | LOW | P4 | `CLAUDE.md` §5 | none | Decision (ledger B21) | Ledger B21 answered | PLANNED |
| 15 | 1 | REM-032 (execute) | MEDIUM | P1 | `CLAUDE.md:202` | REM-032 (decision) | Governing-file edit | Chapter and table agree | PLANNED |
| 16 | 1 | REM-033 | LOW | P2 | `CLAUDE.md` §5 | none | Governing-file edit (addition) | Two new rows added | PLANNED |
| 17 | 1 | REM-016 (execute) | MEDIUM | P2 | `CLAUDE.md` §5, `chapters/21_TheFrenchChef.md` | REM-016 (decision) | Governing-file edit + minimal chapter clause | Reader can identify Dylan | PLANNED |
| 18 | 1 | REM-031 (execute) | MEDIUM | P1 | `CLAUDE.md:155,171`, ChefTip chapters | REM-031 (decision) | Governing-file edit + possible chapter formatting edit(s) | All 7 ChefTip chapters match; CLAUDE.md self-consistent | PLANNED |
| 19 | 1 | REM-036 (execute) | HIGH | P0 | `CLAUDE.md` §5/§6 | REM-036 (decision) | Governing-file addition | Two facts added, cited | PLANNED |
| 20 | 1 | REM-037 (execute) | LOW | P2 | `CLAUDE.md`, `planning/writing-plan_v1.4.0.md` | REM-037 (decision) | Governing-file edit | Both files agree | PLANNED |
| 21 | 1 | REM-039 (execute) | MEDIUM | P1 | `context/chef-writer-context-profile.md` | none | Governing-file edit | Title matches CLAUDE.md | PLANNED |
| 22 | 1 | REM-040 | MEDIUM | P1 | `context/chef-writer-context-profile.md` | bundle with REM-039 | Encoding repair | Zero mojibake remaining | PLANNED |
| 23 | 1 | REM-044 (execute) | LOW | P4 | `CLAUDE.md` §5 | REM-044 (decision) | Governing-file edit | Spelling confirmed, hedge removed | PLANNED |
| 24 | 1 | REM-045 | MEDIUM | P1 | `context/project-memory.md` | after other CLAUDE.md edits | Governing-file regeneration | No disagreement vs CLAUDE.md | PLANNED |
| 25 | 1 | REM-047 | LOW | P4 | `CLAUDE.md` §9 | after other batches | Governing-file edit | Diagram matches actual repo tree | PLANNED |
| 26 | 2 | REM-001 | MEDIUM | P2 | `chapters/11_TheOnion.md` | none | Line/scene edit | Voice-checklist re-pass, no TV-trope framing | CLOSED — 2026-09-02, part remediated / part ruled by Bosco. Ramsay clause at `:3` removed (the remediation). Darren strawman: **author ruled the original back in verbatim**, overriding the finding. `:11` "trauma documentaries": **author ruled it stays**. Both rulings are final — Batch 7 must not re-flag either |
| 27 | 2 | REM-002 | HIGH | P2 | `chapters/12_TheStockPot.md` | none | Line edit (2 instances) | No bare stated-emotion construction remains | DONE — 2026-09-02 |
| 28 | 2 | REM-003 | MEDIUM | P2 | `chapters/12_TheStockPot.md` | REM-002 (same file) | ChefTip-block trim | Word count roughly halved | DONE — 2026-09-02 |
| 29 | 2 | REM-004 | CRITICAL | P2 | `chapters/13_HotTrays.md` | none | Line/scene edit | No "I realised" construction remains | DONE — 2026-09-02 |
| 30 | 2 | REM-005 | MEDIUM | P2 | `chapters/13_HotTrays.md` | REM-004 (same file) | Imagery trim | Comparison density matches ch.10/19 | PARTIAL — 2026-09-02 (one of the three flagged comparisons cut; "Instant. Biblical." and "modern art than first aid" retained as the single image on their own beats — density call stays open into Batch 7) |
| 31 | 2 | REM-006 | LOW | P2 | `chapters/13_HotTrays.md` | REM-004 (same file) | ChefTip-close edit | Bosco read-through | DONE — 2026-09-02, **Bosco read-through completed and confirmed**: the stated-thesis line stays cut, close lands on "Eventually, survival becomes instinct." Validation satisfied, not pending |
| 32 | 2 | REM-008 | HIGH | P2 | `chapters/14_TheOnesWhoStay.md` | none | Line cut | Section break reads cleanly post-cut | DONE — 2026-09-02 |
| 33 | 2 | REM-009 | MEDIUM | P2 | `chapters/14_TheOnesWhoStay.md` | REM-008 (same file) | Paragraph trim | Close lands without restated thesis | DONE — 2026-09-02 |
| 34 | 3 | REM-010 | MEDIUM | P3 | `chapters/16_TwoGlasses.md`, `chapters/17_ProductionKitchen.md` | none | Reword (one side) | Zero verbatim overlap post-edit | PLANNED |
| 35 | 3 | REM-011 | LOW | P3 | `chapters/20_Goose&Gander.md` | none | Clause cut | No false novelty claim remains | PLANNED |
| 36 | 3 | REM-012 | LOW | P3 | `chapters/19,20,21` (entry bridges) | none | Awareness only — likely no edit | Full read-through pacing check post-assembly | PLANNED |
| 37 | 3 | REM-017 | MEDIUM | P2 | `chapters/04_FourFlights.md` | REM-026 (check draft material first) | Conditional beat addition, or no-op | Confirmed via 05/06 review | PLANNED |
| 38 | 3 | REM-016 (chapter clause) | MEDIUM | P2 | `chapters/21_TheFrenchChef.md` | REM-016 (decision) | Minimal clarifying clause | Chapter reads naturally, not as a patch | PLANNED |
| 39 | 4 | REM-021 (execute, conditional) | HIGH | P1→P3 | `chapters/07_Chicken&Mash.md` | REM-021 (Bosco read) | Reword or no-op | Bosco confirms resolved reading | PLANNED |
| 40 | 4 | REM-022 | LOW | P3 | `chapters/07_Chicken&Mash.md` | REM-021 must resolve first | Optional line trim | Bosco read-through | PLANNED |
| 41 | 4 | REM-015 | LOW | P3 | `chapters/21_TheFrenchChef.md` | none | Punctuation fix | Read-aloud parses cleanly | PLANNED |
| 42 | 4 | REM-025 | LOW | P3 | `chapters/08_EarningTheRight.md` | none | Optional image swap | Bosco read-through | PLANNED |
| 43 | 4 | REM-023 (execute) | MEDIUM | P1→P2 | `chapters/08_EarningTheRight.md` | REM-023/042 decision | Line edit | Count matches final ChefTip scheme | PLANNED |
| 44 | 4 | REM-024 (execute, conditional) | MEDIUM | P1→P2 | front/back matter (new file, if disclosure chosen) | REM-024 (decision) | New author's-note file, or no-op | Bosco confirms; Marco scenes untouched | PLANNED |
| 45 | 5 | REM-007 | LOW | P4 | `chapters/13_HotTrays.md` | bundle with Batch 2 pass on ch.13 (run after Batch 2 closes) | Punctuation fix | Diff shows only the mark changed | DONE — 2026-09-02 (executed inside the Batch 2 ch.13 pass, as the plan's own bundling note directs; the diff shows more than the mark alone because REM-006 cut the line immediately before it) |
| 46 | 5 | REM-013 | LOW | P4 | `chapters/19_CoastOrClimb.md` | none | Grammar/spelling fix | Line 259 clean | PLANNED |
| 47 | 5 | REM-014 | LOW | P4 | `chapters/19_CoastOrClimb.md` | bundle with REM-013 | Formatting fix | Em dash used at both instances | PLANNED |
| 48 | 5 | REM-018 | LOW | P4 | `chapters/04_FourFlights.md` | none | Word-correction fix | Zero remaining phase/phased misuse | PLANNED |
| 49 | 5 | REM-028 | MEDIUM | P4 | 15 chapter files | run after Batches 2–3 close | Scripted encoding repair | Zero mojibake, diff-reviewed | PLANNED |
| 50 | 5 | REM-029 | LOW | P4 | `chapters/09_SetUpYoutStation.md` | none | `git mv` + reference updates | History preserved, refs updated | PLANNED |
| 51 | 5 | REM-030 | LOW | P4 | `chapters/15_TasteIt.md` | none | Heading fix | H1 matches canonical title | PLANNED |
| 52 | 6 | REM-026 | HIGH | P0 (scoping) | `drafts/TheEarlyDays.md` → new `chapters/05_*.md`, `06_*.md` | REM-020 (if Option B chosen) | Drafting/promotion (Bosco-only) | New chapters pass full rubric | PLANNED |
| 53 | 6 | REM-027 | LOW | P2 | none yet (future chapter) | none | No action — future scope | N/A | PLANNED |
| 54 | 6 | REM-043 | N/A | P2 | `chapters/22_Dave.md`, `chapters/23_ReturnToYulara.md` | none | No action — future scope (Stage 0 interviews) | N/A | PLANNED |
| 55 | 7 | — (verification) | — | — | 03, 04, 07, 08, 09, 11–14, 15–17, 19–21 | Batches 1–5 complete | Full rubric re-run | See master plan §11 | PLANNED |

**Reading the matrix**: Order is the recommended execution sequence, not a rigid lockstep — items within the same Batch/Order cluster with no listed dependency on each other may run in parallel. Batch 6 (Order 52–54) is tracked for completeness per the master plan's traceability rule but is future-drafting work outside this remediation pass's authority to execute.

---

*End of execution matrix.*
