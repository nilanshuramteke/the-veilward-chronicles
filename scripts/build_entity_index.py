"""Regenerate 10_TRACKERS/entity-index.md from 10_TRACKERS/entity-registry.md.

For every registered entity, records where it appears:
  - manuscript chapters (09_MANUSCRIPTS, local only), with mention counts
  - chapter drafting packages (08_BOOKS/BOOK_NN/05_CHAPTERS/CHAPTER_NN)
  - every other markdown document in the repo
It also writes a per-chapter cast list, the reverse view.

Matching is whole-word and case-sensitive. Writes the file only when its
content changes, and warns about profile paths that don't exist.

Usage:  python scripts/build_entity_index.py [--check]
        --check  exit 1 if the index is out of date, without writing it
"""

import glob
import os
import re
import subprocess
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = "10_TRACKERS/entity-registry.md"
OUTPUT = "10_TRACKERS/entity-index.md"
SKIP = {"INDEX.md", REGISTRY, OUTPUT}
MANUSCRIPT_RE = re.compile(r"^09_MANUSCRIPTS/BOOK_(\d+)/chapter-(\d+)-(.+)\.md$")
PACKAGE_RE = re.compile(r"^08_BOOKS/BOOK_(\d+)/05_CHAPTERS/CHAPTER_(\d+)/")
TOP_REFERENCES = 10


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def parse_registry():
    """Return [(category, name, [terms], profile)] from the registry tables."""
    entities, category = [], None
    for line in read(REGISTRY).splitlines():
        if line.startswith("## "):
            category = line[3:].strip()
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if category is None or not line.lstrip().startswith("|") or len(cells) < 2:
            continue
        if cells[0] in ("Entity", "") or set(cells[0]) <= set("-: "):
            continue
        terms = [t.strip() for t in cells[1].split(",") if t.strip()]
        profile = cells[2] if len(cells) > 2 else ""
        if terms:
            entities.append((category, cells[0], terms, profile))
    return entities


def pattern(terms):
    alts = "|".join(re.escape(t) for t in sorted(terms, key=len, reverse=True))
    return terms, re.compile(rf"(?<!\w)(?:{alts})(?!\w)")


def count(matcher, text):
    terms, rx = matcher
    if not any(t in text for t in terms):
        return 0
    return len(rx.findall(text))


def repo_docs():
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", "*.md"],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout.decode("utf-8")
    return sorted(
        p for p in set(out.split("\0"))
        if p and p not in SKIP and not p.startswith(".")
        and os.path.exists(os.path.join(ROOT, p))
    )


def manuscript_chapters():
    chapters = []
    for full in glob.glob(os.path.join(ROOT, "09_MANUSCRIPTS", "BOOK_*", "chapter-*.md")):
        rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
        m = MANUSCRIPT_RE.match(rel)
        if m:
            chapters.append((int(m.group(1)), int(m.group(2)), heading(rel) or title(m.group(3)), rel))
    return sorted(chapters)


def heading(path):
    """Title from the first heading: '# Chapter Two: The Serpent's Measure' -> The Serpent's Measure"""
    for line in read(path).splitlines():
        if line.startswith("# "):
            return line[2:].split(":", 1)[-1].strip()
        if line.strip():
            return None
    return None


def link(path, text=None):
    return f"[{text or path}](../{path})"


def title(slug):
    small = {"a", "an", "the", "of", "in", "on", "to", "and", "or"}
    words = slug.split("-")
    return " ".join(w if i and w in small else w.capitalize() for i, w in enumerate(words))


def chapter_ranges(nums):
    """[1,2,3,5,7,8] -> '1–3, 5, 7–8'"""
    out, start = [], None
    for i, n in enumerate(nums):
        if start is None:
            start = n
        if i + 1 == len(nums) or nums[i + 1] != n + 1:
            out.append(str(start) if start == n else f"{start}–{n}")
            start = None
    return ", ".join(out)


def generate():
    entities = parse_registry()
    patterns = {name: pattern(terms) for _, name, terms, _ in entities}
    chapters = manuscript_chapters()
    docs = repo_docs()

    ms_hits = defaultdict(dict)       # name -> {(book, ch): count}
    cast = defaultdict(list)          # (book, ch) -> [(count, name)]
    for book, ch, _, path in chapters:
        text = read(path)
        for name, rx in patterns.items():
            n = count(rx, text)
            if n:
                ms_hits[name][(book, ch)] = n
                cast[(book, ch)].append((n, name))

    pkg_hits = defaultdict(set)       # name -> {(book, ch)}
    pkg_readme = {}                   # (book, ch) -> link target
    doc_hits = defaultdict(list)      # name -> [(count, path)]
    for path in docs:
        text = read(path)
        pm = PACKAGE_RE.match(path)
        if pm:
            key = (int(pm.group(1)), int(pm.group(2)))
            folder = pm.group(0)
            readme = folder + "README.md"
            pkg_readme[key] = readme if os.path.exists(os.path.join(ROOT, readme)) else folder
        for name, rx in patterns.items():
            n = count(rx, text)
            if not n:
                continue
            if pm:
                pkg_hits[name].add(key)
            else:
                doc_hits[name].append((n, path))

    warnings = [f"{name}: profile '{profile}' not found"
                for _, name, _, profile in entities
                if profile and not os.path.exists(os.path.join(ROOT, profile))]

    L = [
        "# ENTITY INDEX",
        "",
        "Where each named character, place, force, and artifact appears across the manuscript, the chapter drafting packages, and the story bible.",
        "",
        f"*Auto-generated by `scripts/build_entity_index.py` from [entity-registry.md](entity-registry.md). "
        "Do not edit by hand: add or change entities in the registry, then regenerate. "
        f"Manuscript data reflects the local `09_MANUSCRIPTS/` drafts ({len(chapters)} chapters scanned). "
        "Counts are whole-word, case-sensitive mentions.*",
        "",
        "**Contents:** [Summary](#summary) · [Chapter Cast](#chapter-cast) · [Entity Details](#entity-details)",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Entity | Category | Manuscript chapters | First | Last | Mentions | Packages | Docs |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for category, name, _, _ in entities:
        hits = ms_hits.get(name, {})
        by_book = defaultdict(list)
        for (b, c) in sorted(hits):
            by_book[b].append(c)
        chs = "; ".join(f"B{b}: {chapter_ranges(cs)}" for b, cs in sorted(by_book.items())) or "—"
        keys = sorted(hits)
        first = f"B{keys[0][0]} Ch {keys[0][1]}" if keys else "—"
        last = f"B{keys[-1][0]} Ch {keys[-1][1]}" if keys else "—"
        anchor = re.sub(r"[^a-z0-9 -]", "", name.lower()).replace(" ", "-")
        L.append(f"| [{name}](#{anchor}) | {category} | {chs} | {first} | {last} | "
                 f"{sum(hits.values())} | {len(pkg_hits.get(name, ()))} | {len(doc_hits.get(name, ()))} |")

    L += ["", "---", "", "## Chapter Cast", "",
          "Registered entities present in each manuscript chapter, most-mentioned first.", ""]
    current_book = None
    for book, ch, name, path in chapters:
        if book != current_book:
            current_book = book
            L += [f"### Book {book}", "", "| Ch | Chapter | Present |", "|---|---|---|"]
        present = ", ".join(f"{n} ({c})" for c, n in sorted(cast[(book, ch)], key=lambda x: (-x[0], x[1])))
        L.append(f"| {ch} | {link(path, name.replace('|', '/'))} | {present or '—'} |")
        if (book, ch + 1) not in {(b, c) for b, c, _, _ in chapters}:
            L.append("")
    if not chapters:
        L += ["*No manuscript chapters found in `09_MANUSCRIPTS/`.*", ""]

    L += ["---", "", "## Entity Details", ""]
    current = None
    for category, name, terms, profile in entities:
        if category != current:
            current = category
            L += [f"<!-- {category} -->", ""]
        L += [f"### {name}", ""]
        L.append(f"- **Category:** {category} · **Matches:** {', '.join(f'`{t}`' for t in terms)}")
        L.append(f"- **Profile:** {link(profile) if profile else '*none yet*'}")
        hits = ms_hits.get(name, {})
        if hits:
            parts = []
            for b in sorted({b for b, _ in hits}):
                chs = ", ".join(
                    link(p, f"Ch {c}") + f" ({hits[(b, c)]})"
                    for bb, c, _, p in chapters if bb == b and (b, c) in hits)
                parts.append(f"Book {b}: {chs}")
            L.append("- **Manuscript:** " + " · ".join(parts))
        else:
            L.append("- **Manuscript:** not yet on the page")
        pk = sorted(pkg_hits.get(name, ()))
        if pk:
            L.append("- **Chapter packages:** " + ", ".join(
                link(pkg_readme[k], f"B{k[0]} Ch {k[1]}") for k in pk))
        refs = sorted(doc_hits.get(name, []), key=lambda x: (-x[0], x[1]))
        if refs:
            folders = defaultdict(int)
            for _, p in refs:
                folders[p.split("/")[0] if "/" in p else "(root)"] += 1
            L.append(f"- **Story bible:** {len(refs)} docs — " +
                     ", ".join(f"{f} {n}" for f, n in sorted(folders.items())))
            top = ", ".join(f"{link(p, os.path.basename(p))} ({n})" for n, p in refs[:TOP_REFERENCES])
            more = f", +{len(refs) - TOP_REFERENCES} more" if len(refs) > TOP_REFERENCES else ""
            L.append(f"- **Top references:** {top}{more}")
        else:
            L.append("- **Story bible:** no mentions")
        L.append("")

    return "\n".join(L).rstrip() + "\n", warnings


def main():
    new, warnings = generate()
    for w in warnings:
        print(f"entity-registry warning: {w}", file=sys.stderr)
    out = os.path.join(ROOT, OUTPUT)
    try:
        with open(out, encoding="utf-8", newline="") as f:
            old = f.read()
    except FileNotFoundError:
        old = ""
    if new == old:
        return 0
    if "--check" in sys.argv:
        print(f"{OUTPUT} is out of date - run: python scripts/build_entity_index.py")
        return 1
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
    print(f"{OUTPUT} updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
