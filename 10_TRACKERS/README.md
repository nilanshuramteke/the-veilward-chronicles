# 10_TRACKERS

Operational tracking system for **The Veilward Chronicles**. Update relevant trackers after every completed chapter or major revision.

Trackers do not override `00_CORE` planning canon or `11_CANON` manuscript canon.

## Entity Index

- [entity-index.md](entity-index.md): where every named character, place, force, and artifact appears. It covers the manuscript chapters, the chapter drafting packages, and the story bible, and includes a cast list for each chapter. It is **auto-generated**, so never edit it by hand.
- [entity-registry.md](entity-registry.md): the list of entities the index tracks. Add a row here when a new named entity enters the story.

The index and `INDEX.md` regenerate automatically: a Claude Code hook runs after every file change, and a git pre-commit hook runs on every commit. To regenerate by hand, run `python scripts/refresh_indexes.py`.
