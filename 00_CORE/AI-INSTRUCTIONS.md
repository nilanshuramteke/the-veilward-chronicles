# AI Instructions — The Veilward Chronicles

> **Purpose:** This document defines how any AI system should read, interpret, develop, and write within *The Veilward Chronicles* repository.

---

# 1. Primary Instruction

Before generating story content, planning new lore, or writing a manuscript chapter:

> **Treat this repository as the source of truth for the universe.**

Do not rely solely on a single prompt or conversation summary when relevant repository files are available.

Read the appropriate files before making creative decisions.

---

# 2. Repository Authority

Information within this project has different levels of authority.

When information conflicts, use the following hierarchy:

```text
1. CONFIRMED CANON
        ↓
2. BOOK-SPECIFIC CANON
        ↓
3. SERIES BLUEPRINT
        ↓
4. WORLD, MAGIC, ACADEMY, AND CHARACTER FILES
        ↓
5. PROVISIONAL DECISIONS
        ↓
6. MANUSCRIPT DRAFT IDEAS
```

The highest available authority must always take priority.

The primary canon authority is:

```text
11_CANON/confirmed-canon.md
```

---

# 3. Information Status Definitions

Every important piece of story information may belong to one of three categories.

## CANON

Confirmed facts about the universe.

Canon information must not be contradicted unless a deliberate retcon is approved and recorded.

Examples:

- Mythical creatures have one fixed Mortal Form.
- True shapeshifters can assume multiple appearances.
- The Veilward Academy trains future Veilwardens.

---

## PROVISIONAL

Current ideas that have not yet been permanently established.

Provisional information may be changed as the story develops.

Do not treat provisional information as permanent canon unless it has been promoted to canon.

---

## HIDDEN TRUTH

Confirmed canon intentionally hidden from:

- Readers
- Characters
- Specific books
- Specific points in the narrative

Hidden Truth must never be revealed earlier than the relevant story blueprint permits.

---

# 4. Required Reading Before Writing

The AI must not read every file for every task.

Instead, read only the files relevant to the current task.

---

## Before Writing Any New Story Chapter

Read, at minimum:

1. `README.md`
2. `AI-INSTRUCTIONS.md`
3. Relevant files from `11_CANON/`
4. Relevant files from `06_WRITING_GUIDE/`
5. The current book's `book-bible.md`
6. The current book's `chapter-outline.md`
7. The specific chapter detail file
8. Character files for all major characters appearing in the chapter
9. Relevant continuity trackers

---

## Before Creating New World Lore

Read:

1. `11_CANON/confirmed-canon.md`
2. Relevant files from `01_WORLD/`
3. Relevant files from `02_MAGIC_AND_SPECIES/`
4. Relevant files from `05_LORE_AND_HISTORY/`
5. `11_CANON/provisional-decisions.md`

---

## Before Creating or Changing a Character

Read:

1. `04_CHARACTERS/character-index.md`
2. Relevant existing character files
3. `04_CHARACTERS/relationships.md`
4. Relevant canon files
5. Relevant book and series blueprints

---

## Before Planning a Romance Scene

Read:

1. `04_CHARACTERS/aurelia.md`
2. `04_CHARACTERS/aarav.md`
3. `04_CHARACTERS/relationships.md`
4. `06_WRITING_GUIDE/romance-guide.md`
5. `07_SERIES_BLUEPRINT/romance-arc.md`
6. The current relationship tracker

---

# 5. Core Canon Rules

Unless explicitly changed in `confirmed-canon.md`, the following rules must be respected.

## Rule 1: Mythical Creatures Have a Fixed Mortal Form

Most mythical creatures possess:

- A True Form
- A single fixed Mortal Form

Their Mortal Form cannot be altered into another person's appearance.

A Phoenix always has the same human appearance when taking Mortal Form.

A Naga always has the same human appearance when taking Mortal Form.

---

## Rule 2: True Shapeshifters Are Different

True shapeshifters can:

- Change faces
- Alter physical appearance
- Assume multiple forms
- Potentially imitate other beings

This distinction must remain clear throughout the story.

A normal mythical creature must never suddenly demonstrate unrestricted shapeshifting.

---

## Rule 3: Power Has Limits

No character may solve every problem simply because they possess powerful magic.

Every magical ability must have:

- Limits
- Costs
- Risks
- Situational constraints

Power should create new problems as often as it solves existing ones.

---

## Rule 4: Characters Must Earn Their Development

Characters cannot change suddenly because the plot requires it.

Every meaningful transformation must be supported by:

- Experience
- Conflict
- Consequences
- Reflection
- Relationships
- Choices

---

## Rule 5: Romance Must Develop Naturally

Aurelia and Aarav must not fall in love simply because they are the central romantic pairing.

Their relationship must develop through:

```text
Conflict
    ↓
Understanding
    ↓
Respect
    ↓
Trust
    ↓
Friendship
    ↓
Vulnerability
    ↓
Emotional Attachment
    ↓
Love
```

Do not skip stages without strong narrative justification.

---

# 6. The Golden Story Rule

> **Never let the lore become more important than the characters.**

The world exists to challenge, shape, and reveal the characters.

Ancient history matters because it affects someone living in the present.

Magic matters because characters must make choices about how to use it.

The mystery matters because its truth changes the characters emotionally and personally.

---

# 7. Character Consistency Rules

Before writing a character, ask:

- What does this character want right now?
- What does this character fear right now?
- What does this character know?
- What does this character not know?
- What emotional state are they currently in?
- How has their relationship with the other characters changed?
- What would this character realistically choose?

Do not make a character behave differently simply to force the plot forward.

If the plot requires an unrealistic action:

> Change the circumstances, not the character's intelligence or personality.

---

# 8. Character Knowledge Rules

Characters may only act on information they reasonably possess.

Always distinguish between:

## Reader Knowledge

What the audience knows.

## Character Knowledge

What an individual character knows.

## Hidden Truth

What neither the reader nor the relevant characters currently know.

Never allow characters to:

- Know information they have not learned.
- Understand mysteries before the story reveals sufficient evidence.
- React to events they were not aware of.
- Remember information they never received.

Always consult:

```text
10_TRACKERS/character-knowledge.md
```

when relevant.

---

# 9. Romance Rules

The Aurelia and Aarav relationship is a slow-burn romance.

## Their Differences Must Remain Real

Do not erase their personalities or species differences once they become closer.

Their differences should create:

- Conflict
- Humor
- Misunderstanding
- Growth
- Attraction
- New perspectives

The solution is not for one character to become more like the other.

The solution is for both characters to understand one another better.

---

## Enemies to Friends to Lovers

Their relationship should not move directly from hostility to romance.

The middle stage is essential.

They must become genuine friends.

Friendship should include:

- Shared experiences
- Private jokes
- Emotional safety
- Trust
- Dependence during difficult moments
- Learning each other's vulnerabilities

Romance becomes believable because friendship exists first.

---

## Avoid Instant Emotional Certainty

Characters should sometimes:

- Misunderstand their feelings.
- Hide their feelings.
- Rationalize their feelings.
- Fear the consequences of their feelings.

However:

> Do not create artificial misunderstandings simply to delay the romance.

Conflict must emerge naturally from personality, circumstances, history, or genuine differences.

---

# 10. Mystery Rules

Mysteries must be built through evidence.

Do not hide information simply because the author needs a surprise.

Instead:

> Reveal information without immediately revealing its meaning.

A good mystery structure is:

```text
CLUE
 ↓
QUESTION
 ↓
PARTIAL ANSWER
 ↓
NEW QUESTION
 ↓
REVELATION
 ↓
REINTERPRETATION OF PREVIOUS EVENTS
```

---

## Every Major Reveal Must Be Earned

Before revealing a major truth, ensure the story has already provided:

- Clues
- Suspicion
- Emotional relevance
- Alternative explanations

A reveal should make readers think:

> "I did not predict that, but I understand how it happened."

---

# 11. Foreshadowing Rules

Before introducing a major future event, consider whether it requires earlier foreshadowing.

Foreshadowing may appear as:

- A strange historical detail
- A character reaction
- An unexplained symbol
- A missing record
- An unusual magical reaction
- A seemingly unimportant conversation

Do not make every clue obvious.

A good clue often appears insignificant until its payoff.

Track important clues in:

```text
10_TRACKERS/foreshadowing.md
```

---

# 12. Magic Rules

Magic must feel consistent.

Before introducing a new magical ability, determine:

1. What can it do?
2. What can it not do?
3. What does it cost?
4. How rare is it?
5. Who knows about it?
6. Has the ability existed historically?
7. Does it conflict with established canon?

Do not introduce a new power simply because the characters need an easy solution.

---

# 13. Serpentfire Rules

Serpentfire is a major mystery and a significant element of the series.

It must be treated with care.

Do not:

- Explain its full nature too early.
- Give Aurelia and Aarav complete mastery immediately.
- Allow it to solve every major problem.
- Reveal historical truths before the series blueprint allows.

Serpentfire should evolve through:

```text
Unexpected Reaction
    ↓
Confusion
    ↓
Investigation
    ↓
Partial Understanding
    ↓
Danger
    ↓
Historical Discovery
    ↓
Mastery or Transformation
```

The exact progression must follow the relevant book and series blueprints.

---

# 14. The Outer Dark Rules

The Outer Dark must remain unsettling because it is not fully understood.

Do not explain everything immediately.

Avoid reducing the Outer Dark to:

> "An evil kingdom with monsters."

Its nature should initially feel:

- Ancient
- Uncertain
- Alien
- Difficult to define
- Dangerous

Information about the Outer Dark should expand gradually.

Mystery is part of its identity.

---

# 15. Academy Rules

The Veilward Academy is not merely a magical school.

It is:

- A training institution
- A cultural meeting place
- A political environment
- A place where future Veilwardens are shaped
- A place with traditions and secrets

Student life must include more than classes.

Include opportunities for:

- Friendships
- Rivalries
- Competitions
- Ceremonies
- Private conversations
- Exploration
- Mistakes
- Consequences
- Humor

The Academy should feel inhabited.

---

# 16. Writing New Lore

When the AI encounters an area of the world that has not yet been defined:

Do not immediately establish permanent canon.

Instead, follow this process.

## Step 1: Check Existing Canon

Search relevant files first.

---

## Step 2: Determine Whether New Lore Is Necessary

Ask:

> Does this new information improve the story?

If not, do not create unnecessary lore.

---

## Step 3: Match Existing World Logic

New information must be consistent with:

- Magic rules
- Transformation rules
- Historical timeline
- Existing mythology
- Character knowledge

---

## Step 4: Assign Status

New information should be classified as:

- CANON
- PROVISIONAL
- HIDDEN TRUTH

Unless explicitly approved, newly invented major lore should initially be treated as:

> PROVISIONAL

---

# 17. What the AI May Invent

The AI may create minor details when necessary.

Examples:

- Small locations
- Minor Academy traditions
- Background students
- Temporary objects
- Short historical references
- Food
- Clothing details
- Weather
- Small dialogue details

These additions must not contradict established canon.

---

# 18. What the AI Must Not Invent Without Approval

The AI must not permanently establish the following without checking the relevant files or receiving explicit approval:

- Major new species
- New primary magic systems
- Changes to transformation rules
- New ancient wars
- Major historical figures
- Major Academy institutions
- Major protagonist backstory changes
- Major relationship changes
- New primary villains
- Major mythology that changes existing canon

If such information is required during planning, mark it as:

> PROVISIONAL

---

# 19. Chapter Writing Workflow

When writing a chapter, follow this sequence.

## Step 1: Understand the Chapter Purpose

Identify:

- What must happen?
- Why must it happen?
- What changes by the end?

---

## Step 2: Identify the POV

Determine:

- Whose perspective is used?
- What does this character know?
- What does this character want?

---

## Step 3: Check Continuity

Review:

- Current timeline
- Character knowledge
- Injuries
- Relationships
- Active mysteries
- Previous chapter ending

---

## Step 4: Review Character State

Determine the emotional state of major characters.

Do not begin each chapter as if previous events had no consequences.

---

## Step 5: Write the Scene

Prioritize:

1. Character
2. Emotion
3. Conflict
4. Story movement
5. Worldbuilding

---

## Step 6: Check the Ending

Every chapter should leave the reader with at least one of the following:

- A new question
- An emotional change
- A decision
- A revelation
- A consequence
- A new danger

Do not manufacture cliffhangers for every chapter.

---

# 20. Scene-Level Requirements

Every meaningful scene should have a purpose.

A scene should ideally include:

## Goal

What does the POV character want?

## Conflict

What prevents them from getting it?

## Change

What is different when the scene ends?

If nothing changes, reconsider whether the scene is necessary.

---

# 21. Dialogue Rules

Dialogue should reveal:

- Personality
- Relationships
- Conflict
- Information
- Emotion

Avoid dialogue that exists only to explain the world.

Characters should rarely say things they both already know merely for the reader's benefit.

Prefer:

Natural conversation.

Subtext.

Interrupted explanations.

Different interpretations.

---

# 22. Emotional Writing Rules

Do not constantly explain emotions directly.

Avoid repeatedly writing:

> She felt sad.

Instead, show emotion through:

- Actions
- Physical reactions
- Thoughts
- Silence
- Dialogue
- What the character notices
- What the character refuses to acknowledge

However:

Do not make every emotion subtle.

Important emotional moments may be direct and honest.

The goal is emotional clarity, not unnecessary ambiguity.

---

# 23. Action Writing Rules

Action scenes should prioritize:

- Spatial clarity
- Character decisions
- Consequences
- Emotional stakes

Do not turn combat into a list of magical attacks.

Ask:

> Why does this fight matter?

A character should leave an important action sequence changed in some way.

Possible consequences:

- Injury
- Fear
- New knowledge
- Relationship change
- Moral consequence
- Failure
- Victory with a cost

---

# 24. Injury and Consequence Rules

Injuries must persist unless established magic reasonably heals them.

Do not:

- Injure a character dramatically.
- Forget the injury in the next chapter.

Track injuries in:

```text
10_TRACKERS/continuity.md
```

The same rule applies to:

- Emotional trauma
- Broken relationships
- Public consequences
- Magical exhaustion

---

# 25. Pacing Rules

The story should balance:

- Romance
- Mystery
- Academy life
- Friendship
- Training
- Action
- Worldbuilding

Do not allow one element to completely disappear for long periods unless the narrative requires it.

The reader should regularly feel that multiple story threads are moving.

---

# 26. Avoid Artificial Drama

Do not create conflict through avoidable misunderstandings when a simple conversation would solve everything.

Conflict should emerge from:

- Genuine personality differences
- Different values
- Fear
- History
- External pressure
- Incomplete information
- Real consequences

Characters may fail to communicate.

But that failure must make sense.

---

# 27. Avoid Plot Convenience

Do not introduce:

- A new power
- A forgotten artifact
- A convenient character
- A sudden prophecy

at the exact moment the protagonists need an easy solution.

If an important solution appears later:

> Establish its possibility earlier whenever practical.

---

# 28. Mythological Respect

The series draws inspiration from mythologies and traditions from across the world.

Treat those traditions with respect.

Do not reduce mythological creatures to:

- Decorative aesthetics
- Random superpowers
- Stereotypes

When adapting mythology:

- Preserve meaningful inspiration.
- Avoid claiming that every story exactly reproduces traditional mythology.
- Allow this universe to develop its own internal history.

The Veilward Chronicles is an original fantasy universe inspired by mythology.

It is not intended to reproduce any mythology exactly.

---

# 29. Cultural Diversity

The world contains creatures inspired by mythologies from multiple cultures.

Diversity should feel natural.

Do not introduce a character solely to represent a culture or mythology.

Every significant character should have:

- Personality
- Goals
- Flaws
- Relationships
- Agency

Their cultural or mythological background should enrich who they are rather than replace their individuality.

---

# 30. Continuity Update Requirements

After completing a significant chapter, review whether the following files need updating:

```text
10_TRACKERS/continuity.md
10_TRACKERS/character-knowledge.md
10_TRACKERS/relationships.md
10_TRACKERS/foreshadowing.md
10_TRACKERS/mysteries.md
10_TRACKERS/unresolved-questions.md
```

Do not update canon merely because something appeared in a draft.

A draft detail becomes canon only when deliberately confirmed.

---

# 31. Handling Contradictions

If the AI discovers conflicting information:

## Do Not Guess

Instead:

1. Identify the conflicting files.
2. Check their information status.
3. Check canon priority.
4. Follow the higher-authority source.

If both sources have equal authority and the contradiction cannot be resolved:

> Flag the contradiction for review.

Do not silently invent a solution.

---

# 32. Handling Missing Information

If necessary information is missing:

## Minor Detail

The AI may invent it temporarily, provided it does not conflict with canon.

Example:

A minor student's name.

---

## Major Detail

Do not permanently invent it.

Instead:

- Ask for clarification, or
- Propose options, or
- Create a clearly marked PROVISIONAL decision.

---

# 33. Spoiler Protection

When generating content intended for readers or individual books:

Do not reveal Hidden Truth information early.

Before revealing:

- Ancient secrets
- Character secrets
- Villain identities
- Major historical truths

Check:

```text
07_SERIES_BLUEPRINT/
08_BOOKS/
```

The existence of information in the repository does not mean the reader should know it.

---

# 34. Book Boundary Rules

Each book must feel complete.

Every book should contain:

- A beginning
- A central conflict
- Major emotional development
- Meaningful resolution

At the same time:

The series should contain larger unresolved mysteries.

Avoid ending a book with no emotional resolution simply to force readers into the next book.

---

# 35. The Emotional Priority

At major story moments, ask:

> What does this event mean emotionally to the characters?

Examples:

A magical battle is not important merely because someone wins.

It matters because:

- Someone failed.
- Someone made a sacrifice.
- Someone discovered something about themselves.
- A relationship changed.

Always look for the human or personal consequence inside the fantastical event.

---

# 36. Final Quality Check Before Delivering a Chapter

Before considering a chapter complete, verify:

## Continuity

- [ ] No established canon is contradicted.
- [ ] Character knowledge is accurate.
- [ ] Injuries and consequences are remembered.
- [ ] Timeline is correct.

## Characters

- [ ] Characters behave consistently.
- [ ] Character choices make sense.
- [ ] Emotional changes are earned.

## Romance

- [ ] Relationship progression is appropriate.
- [ ] No stage of the slow burn is skipped.
- [ ] Attraction does not replace emotional development.

## Mystery

- [ ] No Hidden Truth is revealed too early.
- [ ] Important clues are tracked.
- [ ] New questions feel earned.

## Writing

- [ ] The POV remains consistent.
- [ ] Dialogue sounds natural.
- [ ] The chapter has a clear purpose.
- [ ] Something changes by the end.

---

# 37. Default Story Priorities

When forced to choose between competing priorities, use this order:

```text
1. Character Consistency
2. Established Canon
3. Emotional Truth
4. Story Logic
5. Relationship Development
6. Mystery Structure
7. Plot Requirements
8. Worldbuilding Detail
```

The story should never sacrifice believable characters merely to reach a predetermined plot event.

---

# 38. The Final Principle

The Veilward Chronicles is a story about mythical creatures.

But its emotional foundation is universal.

The characters may possess:

- Fire
- Water
- Wings
- Ancient magic
- Mythical forms

But their struggles should remain recognizable.

They struggle with:

- Expectations
- Identity
- Fear
- Trust
- Belonging
- Love
- The consequences of their choices

The mythology makes the world extraordinary.

The characters make the story matter.

---

# AI Operating Summary

Before creating content:

> **Read the relevant files.**

Before changing lore:

> **Check canon.**

Before writing a character:

> **Check what they know, want, fear, and feel.**

Before advancing the romance:

> **Check the relationship stage.**

Before revealing a mystery:

> **Check the story blueprint.**

Before introducing new magic:

> **Check the rules and consequences.**

Before finalizing:

> **Check continuity.**

And always remember:

> **The world must support the characters. The characters must drive the story.**
