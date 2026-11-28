"""MkDocs hook: replaces <!-- gear-totals --> with per-gear totals built from session front matter."""

import pathlib
import re

import yaml

PLACEHOLDER = "<!-- gear-totals -->"
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---", re.S)


def _totals(docs_dir):
    totals = {}
    for path in sorted((pathlib.Path(docs_dir) / "sessions").rglob("*.md")):
        match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        meta = yaml.safe_load(match.group(1)) or {}
        gear = meta.get("gear")
        if not gear:
            continue
        for gear_id in gear if isinstance(gear, list) else [gear]:
            entry = totals.setdefault(gear_id, {"sessions": 0, "km": 0.0, "first": None, "last": None})
            entry["sessions"] += 1
            entry["km"] += float(meta.get("distance_km") or 0)
            date = str(meta.get("date", ""))
            entry["first"] = min(filter(None, [entry["first"], date]))
            entry["last"] = max(filter(None, [entry["last"], date]))
    return totals


def on_page_markdown(markdown, page, config, files):
    if PLACEHOLDER not in markdown:
        return markdown
    totals = _totals(config["docs_dir"])
    if not totals:
        return markdown.replace(PLACEHOLDER, "*No sessions tagged with gear yet.*")
    rows = ["| Gear | Sessions | Distance | First used | Last used |", "|---|---|---|---|---|"]
    for gear_id, t in sorted(totals.items(), key=lambda kv: kv[1]["last"], reverse=True):
        rows.append(
            f"| [`{gear_id}`](#{gear_id}) | {t['sessions']} | {t['km']:.1f} km | {t['first']} | {t['last']} |"
        )
    return markdown.replace(PLACEHOLDER, "\n".join(rows))
