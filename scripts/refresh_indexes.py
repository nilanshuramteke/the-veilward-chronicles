"""Regenerate INDEX.md and 10_TRACKERS/entity-index.md.

Usage:
  python scripts/refresh_indexes.py           rebuild both (only writes files that changed)
  python scripts/refresh_indexes.py --check   exit 1 if either is out of date
  python scripts/refresh_indexes.py --hook    Claude Code PostToolUse mode: reads the hook
                                              payload from stdin and rebuilds only what the
                                              tool call could have affected
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_entity_index  # noqa: E402
import build_index  # noqa: E402

GENERATED = {"INDEX.md", "entity-index.md"}


def hook_targets():
    """Decide which indexes a tool call could have made stale."""
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return True, True
    tool = payload.get("tool_name", "")
    if tool == "Bash":
        # Shell commands can create, move, or delete files. Rebuild the tree, and
        # the entity index too if the tree changed.
        return True, None
    path = (payload.get("tool_input") or {}).get("file_path", "")
    if not path.lower().endswith(".md") or os.path.basename(path) in GENERATED:
        return False, False
    return True, True


def _read_index():
    try:
        with open(build_index.INDEX, encoding="utf-8", newline="") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def main():
    args = sys.argv[1:]
    if "--hook" in args:
        tree, entities = hook_targets()
        sys.argv = [sys.argv[0]]
    else:
        tree = entities = True
    status = 0
    if tree:
        before = _read_index()
        status |= build_index.main()
        if entities is None:
            entities = _read_index() != before
    if entities:
        status |= build_entity_index.main()
    # A hook must never block the agent, even if a build fails.
    return 0 if "--hook" in args else status


if __name__ == "__main__":
    sys.exit(main())
