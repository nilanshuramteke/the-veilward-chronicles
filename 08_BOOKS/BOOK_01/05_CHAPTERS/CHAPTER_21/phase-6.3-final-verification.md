# Chapter 21 — Phase 6.3 Final Verification

## 1. Verification Metadata
- **Chapter:** 21
- **Title:** Come Back
- **Verification date:** 2026-09-26
- **Current manuscript word count:** 5,507 (`wc -w`, matches expected)
- **Hard ceiling:** 5,550 — PASS (43-word margin)
- **Preferred band:** 4,300–4,900 — exceeded; informational only, not a correction target
- **Fresh full read:** Yes. The current manuscript was read in full (337 lines) this phase, after the Phase 6.1 commit.
- **Scope disclosure:**
  - Continuity comparison (Ch 7/8/11/18/19/20) relies on the state-lock, handoff and canon-constraints material read earlier in this session (Phase 6). Those files were not re-read this turn. Every continuity claim below was checked against the fresh manuscript read.
  - No file was edited. Nothing was committed or pushed.

## 2. Phase 6.1 Correction Verification

### Correction A — Signature
**PASS.** L322 reads: "...a slow, wavering line with the last stroke dragged low." The grep for `*H*` returns nothing. No letter, initial or surname is implied anywhere in the chapter. The only name in the signature scene is "Aarav," written "directly under hers." The sentence still reads naturally as handwriting description. No surname appears in the manuscript. The `git status` for this session showed only INDEX/entity-index/report changes and no character or canon file changes, so no surname was added to canon.

### Correction B — Word Count
**PASS on the ceiling. One caveat: the trim left three mechanical punctuation defects (see §14).** The count is 5,507 (≤ 5,550). The fresh read confirms that no narrative beat, decision point, rescue step, or consequence was removed. The three defects are stray punctuation left by cuts, not lost content.

## 3. Phase 5 Correction Verification
| AC | Result | Evidence |
|----|--------|----------|
| AC-01 | PASS | Redundancy trims are present with every beat intact: danger (L83–93), decision (L97–132), rescue (L136–238), aftermath (L248–294), review (L298–336). |
| AC-02 | PASS | "neither of them said anything" is absent (grep). The proctor beat, "did not say anything at all" (L244), is a single-person reaction, not a shared silence. No romance is created. |
| AC-03 | PASS | L310: "The low stretch stays closed, and the works sealed, until the ward team has been through it stone by stone." It states closure, sealing and procedural inspection. The ward check "records nothing" (L308), so the mystery stays unresolved. |
| AC-04 | PASS | "the way it had once before" is absent (grep). Sound return (L164–170) is described with no earlier equivalent experience. |
| AC-05 | PASS | The proctor is unnamed ("the gate proctor," L19, L101). First-year training context remains (L23, L27, L99). The "They had us tie each other to the post" construction at L27 is coherent. |
| AC-06 | PASS | Geometry is intact: Aarav is at the rope, hip to the stake, "on the safe side of the cordon" (L83). A dark line spreads "back toward the rope" (L83). The bank goes under him, "rope, stake and all" (L87). He loses ground (L87), her grip fails (L89), and he falls with the spoil (L91). |

## 4. Unauthorized Change Audit
No substantive unauthorized changes were found in plot, dialogue content, characterization, POV, relationship progression, mystery information, Echo behavior, magic, setting, scene structure, supporting roles or ending. All differences from the Phase 6 state are the signature wording and prose trims. **However**, three trims left punctuation artifacts (L280, L286, L308). These are side effects of authorized edits, not new content, and are recorded in §14. They are not fixed.

## 5. Continuity Verification
- **Ch 7:** Three accounts with a shared core plus single-source details. This is compatible with earlier witness evidence, and nothing retrofits an explanation to Ch 7.
- **Ch 8:** Seraphine's concerns are answered through physical evidence and procedure only (frost, split slab, rime on the left face, ward check reading nothing). There is no explanation of the mystery.
- **Ch 11:** The manuscript has no reference to a fourth stone. The low stretch is a crew-cut trench with a drain and is not equated with it.
- **Ch 18:** Aurelia's knowledge is limited to what she already had. "There's more, and it isn't mine to tell. Some of it belongs to Aarav" (L35) keeps his interpretation undisclosed.
- **Ch 19:** Voss appears once (L290) as a person to be told. Statement analysis and two-account comparison are not touched or resolved.
- **Ch 20:** Fourteen-C does not appear. Aurelia proposes bringing it to Voss together ("the two of us," L290), which is consistent with the "do not decide alone" rule.

## 6. Echo Epistemic Verification
- **Observation:**
  - Cold in the wrists and knees; the flame shrinking.
  - Sound thinning out, and no voice.
  - Frost climbing the cord.
  - The lantern at the low end dimming first.
  - Warmth returning along the left wall, "in order."
  - Cold thinning along the channel and not across it.
  - The ward check reading nothing.
- **Inference:** Aarav's "That fits." and "I don't know. With that." are one hedged inference, with no target named and explicit reluctance ("I'd rather not say more than I've got"). He flags the along-not-across observation as unvouched.
- **Unknown:** cause, identity, motive and destination are all unstated.
- **Not present:** no identity, motive, destination, intention, awareness of the characters, pursuit, avoidance, or search language. No link to Seeker, Outer Dark, Serpentfire or First Ember (grep confirmed).
- **Note:** L79 (Aurelia braces for a voice "in a tone that was almost right") and L170 ("waited for it to be smooth") are her expectation from prior chapters. Nothing in the text asserts the Echo intends anything.

## 7. Magic Verification
- **Aurelia:**
  - Small, controlled flame throughout, with the coin-sized bead widening and being drawn back (L5, L13).
  - The flare in the drain when the prop groans (L186) fits her established failure tendency.
  - She has a physical cost: a burned forearm and hand (L186, L248).
  - The steam and spall are the cost, not the fire itself.
  - No sudden mastery and no new ability.
- **Aarav:**
  - Stone-taps, chalk, timing and pace-setting by hand.
  - He is cold, breathing hard and injured. There is no True Form, Naga ability, cold resistance or regeneration.

## 8. Relationship Verification
- **Opening:** Stage 2 / edge of 3 (L49 straight to the box; the tally, the chalk).
- **Ending:** Stage 4 through action, with no spoken declaration.
- **Required beats:** all present.
  1. Aarav acts by reflex (L85).
  2. Aurelia chooses to go in (L128–132).
  3. They cooperate physically (L158–226).
  4. They trust each other's competence (L202, L214).
  5. They share the aftermath (L248–294).
  6. He enters his name voluntarily under hers (L326–332).
- **Absent:** no confession, kiss or romance. The trimming introduced no romantic framing.

## 9. POV Verification
Close Aurelia POV throughout. Others' states are inferred from outward behavior only: "whatever he saw in her face" (L85), "understood some of it anyway" (L126), "not what she had expected" (L202). There is no access to Aarav's, Mira's or Seraphine's thoughts, and no Echo or lore access.

## 10. Scene Structure Verification
Six scenes, separated by `---` (L73, 95, 134, 246, 296):
1. Warm opening / training setup (L3–71)
2. Cold / collapse (L75–93)
3. Procedure / Aurelia's decision (L97–132)
4. Rescue (L136–244)
5. Aftermath / institutional response (L248–294)
6. Accounts / review / signatures (L298–336)

Same order, none merged, deleted or added.

## 11. Act II-B Verification
The chapter provides genuine physical danger, a real consequence (a burn, a formal review, and restrictions), Echo escalation through observable phenomena, a procedural institutional response, and friendship established through action. The mystery stays open (ward check clean, low stretch sealed pending ward team), and momentum carries toward Voss and the review. It does not solve the mystery, begin Act III or resolve the Angular Mark, wall/names, Fourteen-C or the fourth stone.

## 12. Reader-Promise Verification
DANGER (collapse, L83–93) → DECISION (L97–132) → ACTION (L136–226) → TEAMWORK (the melt pace, the count, the slab lift) → CONSEQUENCE (burn, review, restrictions, two signatures). This is not an investigation chapter. The physical event changes both the relationship and the institutional situation.

## 13. Index / Entity-Index Verification
- **INDEX.md:** Both `phase-6-post-correction-verification.md` and `phase-6.1-targeted-corrections.md` are listed (L371–372). The `phase-6.3` file is new and not yet indexed. That is expected, because this phase forbids regenerating indexes.
- **entity-index.md, Chapter 21 row (L79):** Mira 28, Aurelia 25, Aarav 16, Seraphine 7, Voss 1, Training Grounds 1. I checked these against the current manuscript with `grep -o | wc -l`, and all six match exactly. The manuscript is gitignored, so this was checked against the local file, not against a committed copy.
- **Edits required by Phase 6.3:** none to either generated file.

## 14. Remaining Issues

**Blocking issues:** none.

**Non-blocking notes:**
1. **Stray punctuation from the Phase 6.1 trim, L280:** `She looked at the frost, then the cut,. "Cordon,"` has a comma-period sequence. The intended form is presumably `the cut. "Cordon,"`.
2. **Stray punctuation from the Phase 6.1 trim, L286:** `and at his hands,. Then to Aurelia.` has the same defect.
3. **Dialogue seam from the Phase 6.1 trim, L308:** `"has come back." "It records nothing...` runs two quoted segments together where a tag or sentence previously sat between them. It is readable but abrupt.
4. **Pre-existing, unchanged:** L85 "She had done this once before. She had gone for him." is not touched by 6.1. It was accepted in Phases 4–6 and is out of scope here.

I did not correct any of these. Notes 1–3 are mechanical, and the author may wish to authorize a punctuation-only fix.

**Preferred-band observation:** 5,507 is above the preferred 4,300–4,900 band but within the hard ceiling. No further trim is recommended by this phase.

## 15. Final Verdict
**PASS WITH NOTES**

## 16. Finalization Readiness
**Chapter 21 is ready for finalization.** The chapter is verified and canon-safe on a fresh full read. The three punctuation artifacts in §14 are non-blocking but visible on the page. I recommend the author decide whether to authorize a punctuation-only fix before or as part of finalization.
