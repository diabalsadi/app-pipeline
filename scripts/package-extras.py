#!/usr/bin/env python3
"""Zip the skills of every extra plugin in toolkit/extras.json for claude.ai.

Each plugin is fetched from its pinned commit, and each of its skills becomes
dist/extras/<plugin>/<skill>.zip. The zips are for uploading to your own
claude.ai account; dist/ is not committed, since some of these skills may not
be redistributed (see the README).

Usage: python3 scripts/package-extras.py   (or ./scripts/package-skills.sh --extras)
"""
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRAS = ROOT / "toolkit" / "extras.json"
OUT = ROOT / "dist" / "extras"


def fetch(repo: str, commit: str, dest: Path) -> None:
    subprocess.run(["git", "init", "-q", str(dest)], check=True)
    git = ["git", "-C", str(dest)]
    subprocess.run(git + ["remote", "add", "origin", f"https://github.com/{repo}"], check=True)
    subprocess.run(git + ["fetch", "-q", "--depth", "1", "origin", commit], check=True)
    subprocess.run(git + ["checkout", "-q", "FETCH_HEAD"], check=True)


def skill_dirs(plugin_root: Path, listed: list[str] | None) -> list[Path]:
    """The skills Claude Code would load: the marketplace list, else the plugin's own list, else skills/*."""
    manifest = plugin_root / ".claude-plugin" / "plugin.json"
    if not listed and manifest.exists():
        listed = json.loads(manifest.read_text()).get("skills")
        if isinstance(listed, str):
            listed = [listed]
    found = []
    for entry in listed or ["skills"]:
        path = (plugin_root / entry).resolve()
        # An entry is either one skill folder or a folder of skills.
        found += [path] if (path / "SKILL.md").exists() else sorted(p.parent for p in path.glob("*/SKILL.md"))
    return found


def main() -> None:
    shutil.rmtree(OUT, ignore_errors=True)
    checkouts: dict[tuple[str, str], Path] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for e in json.loads(EXTRAS.read_text())["plugins"]:
            key = (e["repo"], e["commit"])
            if key not in checkouts:
                checkouts[key] = Path(tmp) / f"src{len(checkouts)}"
                fetch(*key, checkouts[key])
            root = checkouts[key] / e.get("path", "")
            for src in skill_dirs(root, e.get("skills")):
                dest = OUT / e["name"]
                dest.mkdir(parents=True, exist_ok=True)
                archive = shutil.make_archive(str(dest / src.name), "zip", src.parent, src.name)
                print(Path(archive).relative_to(ROOT))


if __name__ == "__main__":
    main()
