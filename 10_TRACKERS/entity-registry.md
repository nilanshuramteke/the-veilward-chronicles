# ENTITY REGISTRY

The list of named story entities that `scripts/build_entity_index.py` tracks. The generated result lives in [entity-index.md](entity-index.md).

## How to Edit

- Add a row when a new named character, place, artifact, force, or concept enters canon. Remove or rename rows when canon changes.
- **Entity**: the canonical name as it should appear in the index.
- **Match terms**: comma-separated words or phrases to search for. Matching is whole-word and case-sensitive, so `Veil` does not match `Veilward`, and `Dev` does not match `Development`. Possessives (`Aurelia's`) match automatically. List plurals and alternate names separately.
- **Profile**: the file that owns this entity's canon, as a repo-relative path. Leave blank if none exists yet.
- Section headings (`## Characters`, and so on) become the categories in the index. Add new sections freely.
- Only rows inside tables under a `##` heading are read. Everything else in this file is ignored.

## Characters

| Entity | Match terms | Profile |
|---|---|---|
| Aurelia | Aurelia | 04_CHARACTERS/aurelia.md |
| Aarav | Aarav | 04_CHARACTERS/aarav.md |
| Professor Elian Voss | Voss, Elian | 04_CHARACTERS/professor-elian-voss.md |
| Warden Seraphine | Seraphine | 04_CHARACTERS/character-directory.md |
| Dev | Dev | 04_CHARACTERS/dev.md |
| Mira | Mira | 04_CHARACTERS/mira.md |
| Lyra | Lyra | 04_CHARACTERS/lyra.md |
| The Archivist | Archivist | |
| Elyra | Elyra | 04_CHARACTERS/elyra.md |
| Varun | Varun | 04_CHARACTERS/character-directory.md |
| The Unknown Student | Unknown Student | 04_CHARACTERS/character-directory.md |

## Species

| Entity | Match terms | Profile |
|---|---|---|
| Phoenix | Phoenix, Phoenixes | 02_MAGIC_AND_SPECIES/phoenix.md |
| Naga | Naga, Nagas | 02_MAGIC_AND_SPECIES/naga.md |

## Locations

| Entity | Match terms | Profile |
|---|---|---|
| Veilward Academy | Veilward Academy, Academy | 03_ACADEMY/veilward-academy.md |
| The Archive | Archive | 03_ACADEMY/academy-campus-and-locations.md |
| The Hidden Chamber | Hidden Chamber | 08_BOOKS/BOOK_01/04_WORLD_AND_LOCATIONS/hidden-chamber.md |
| Training Grounds | Training Grounds | 03_ACADEMY/academy-campus-and-locations.md |
| Heart Hall | Heart Hall | 03_ACADEMY/academy-campus-and-locations.md |
| Threshold Hall | Threshold Hall | 03_ACADEMY/academy-campus-and-locations.md |
| Open Court | Open Court | 03_ACADEMY/academy-campus-and-locations.md |
| Observatory | Observatory | 03_ACADEMY/academy-campus-and-locations.md |
| Old Foundations | Old Foundations | 03_ACADEMY/academy-campus-and-locations.md |
| Student Commons | Student Commons | 03_ACADEMY/academy-campus-and-locations.md |
| Form Sanctuaries | Form Sanctuaries, Form Sanctuary | 03_ACADEMY/academy-campus-and-locations.md |

## Forces and Powers

| Entity | Match terms | Profile |
|---|---|---|
| The Veil | Veil | 01_WORLD/the-veil.md |
| Serpentfire | Serpentfire | 05_LORE_AND_HISTORY/serpentfire-history.md |
| The Outer Dark | Outer Dark | 05_LORE_AND_HISTORY/outer-dark-history.md |
| The Seeker | Seeker | 11_CANON/canon-glossary.md |
| The Harbinger | Harbinger | 11_CANON/canon-glossary.md |

## Artifacts and Lore

| Entity | Match terms | Profile |
|---|---|---|
| The First Ember | First Ember | 11_CANON/artifact-canon.md |
| The Lost Path | Lost Path | 11_CANON/canon-glossary.md |
| The Forgotten Age | Forgotten Age | 05_LORE_AND_HISTORY/forgotten-age.md |
| Veilwardens | Veilwarden, Veilwardens | 03_ACADEMY/veilward-academy.md |
