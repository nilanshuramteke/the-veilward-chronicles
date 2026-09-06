# Canon Rules

## Purpose
This document defines how canon is identified, prioritized, changed, and maintained across *The Veilward Chronicles* repository.

## Canon Status Vocabulary
- **CONFIRMED** — established and binding unless formally retconned.
- **PROVISIONAL** — currently intended but may change.
- **OPEN QUESTION** — intentionally undecided by the author.
- **DELIBERATELY UNKNOWN** — the author has chosen not to define this yet, or the answer is intentionally withheld from the story.
- **RETCONNED** — superseded by a later explicit canon decision.
- **NON-CANON** — brainstorming, alternatives, or rejected ideas.
- **DISPUTED** — temporary audit status used only while a conflict is being resolved.

## Canon Authority Hierarchy
When sources conflict, use the highest applicable authority:

1. **Author Final Truths** — locked endgame truths and final-series resolutions.
2. **Explicit Canon Decisions** — formal conflict resolutions and approved canon changes.
3. **Author Hidden Truths** — established truths intentionally protected from readers and early-book drafting.
4. **Core Series Canon** — premise, pillars, rules, and foundational chronology.
5. **Dedicated Domain Canon** — world, magic, species, academy, characters, and history.
6. **Book-Specific Canon** — locked decisions required for a particular book.
7. **Chapter Blueprints** — scene and chapter execution plans.
8. **Draft Manuscripts** — subordinate until manuscript events are explicitly promoted into canon.
9. **Research and Inspiration** — never canon by themselves.

## Reader Knowledge Is Not Author Knowledge
A mystery may be:
- known to the author,
- unknown to the characters,
- unknown to the reader,
- revealed only in a later book.

Do not mark an established author truth as an OPEN QUESTION merely because it has not yet been revealed.

## Repository Authority Map
| Subject | Primary Location |
|---|---|
| Core premise, pillars, canon rules, master timeline | `00_CORE/` |
| World structure and geography | `01_WORLD/` |
| Magic and species | `02_MAGIC_AND_SPECIES/` |
| Veilward Academy | `03_ACADEMY/` |
| Characters and relationships | `04_CHARACTERS/` |
| Lore and history | `05_LORE_AND_HISTORY/` |
| Prose and drafting craft | `06_WRITING_GUIDE/` |
| Trilogy and revelation architecture | `07_SERIES_BLUEPRINT/` |
| Book-specific blueprints | `08_BOOKS/` |
| Manuscripts | `09_MANUSCRIPTS/` |
| Progress tracking | `10_TRACKERS/` |
| Active canon register and conflict resolution | `11_CANON/` |
| Research | `12_RESEARCH/` |
| Audits and reviews | `13_REVIEWS_AND_AUDITS/` |

## Relationship Canon
The central Aurelia–Aarav progression is:

**Rivals → Forced Cooperation → Respect → Trust → Friendship → Emotional Intimacy → Love → Conscious Commitment**

They are not to be written as traditional enemies unless a specific scene-level conflict explicitly warrants hostile behavior.

## Canon Change Process
1. Identify the affected truth.
2. Check the Canon Authority Matrix.
3. Check the Revelation Matrix for spoiler consequences.
4. Record the decision in `11_CANON/`.
5. Update affected source documents.
6. Mark superseded material RETCONNED where necessary.
7. Run a continuity check before manuscript drafting resumes.

## Core Rule
When in doubt, do not invent a new fact to solve a continuity problem. Flag the conflict and resolve it explicitly.
