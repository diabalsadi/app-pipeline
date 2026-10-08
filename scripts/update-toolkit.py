#!/usr/bin/env python3
"""Copy the third-party skills listed in toolkit/sources.json into skills/<name>.

Each skill is fetched from its pinned commit, so a rerun with an unchanged
manifest produces no diff. After copying, the script applies the small edits
the manifest asks for (a narrower description, or allowing the model to
invoke the skill) and regenerates THIRD_PARTY_NOTICES.md.

Usage: python3 scripts/update-toolkit.py
"""
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "toolkit" / "sources.json"
SKILLS = ROOT / "skills"
NOTICES = ROOT / "THIRD_PARTY_NOTICES.md"


def fetch(repo: str, commit: str, dest: Path) -> None:
    subprocess.run(["git", "init", "-q", str(dest)], check=True)
    git = ["git", "-C", str(dest)]
    subprocess.run(git + ["remote", "add", "origin", f"https://github.com/{repo}"], check=True)
    subprocess.run(git + ["fetch", "-q", "--depth", "1", "origin", commit], check=True)
    subprocess.run(git + ["checkout", "-q", "FETCH_HEAD"], check=True)


def set_frontmatter(skill_md: Path, description: str | None, allow_model: bool) -> None:
    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit(f"{skill_md}: no frontmatter")
    lines = match.group(1).split("\n")
    out, skip_block = [], False
    for line in lines:
        if skip_block:
            if line.startswith((" ", "\t")):
                continue
            skip_block = False
        if description and line.startswith("description:"):
            out.append("description: " + json.dumps(description))
            skip_block = True
            continue
        if allow_model and line.startswith("disable-model-invocation:"):
            continue
        out.append(line)
    skill_md.write_text("---\n" + "\n".join(out) + "\n---\n" + text[match.end():])


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    checkouts: dict[tuple[str, str], Path] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for entry in manifest["skills"]:
            key = (entry["repo"], entry["commit"])
            if key not in checkouts:
                dest = Path(tmp) / f"src{len(checkouts)}"
                fetch(*key, dest)
                checkouts[key] = dest
            src_root = checkouts[key]
            src = (src_root / entry["path"]).resolve()
            target = SKILLS / entry["name"]
            if target.exists():
                shutil.rmtree(target)
            ignore = shutil.ignore_patterns(".git", ".github", "__pycache__")
            shutil.copytree(src, target, ignore=ignore)
            for rel in entry.get("exclude", []):
                path = target / rel
                if path.is_dir():
                    shutil.rmtree(path)
                elif path.exists():
                    path.unlink()
            if "licenseFile" in entry and not any(target.glob("LICENSE*")):
                shutil.copy(src_root / entry["licenseFile"], target / "LICENSE")
            set_frontmatter(
                target / "SKILL.md",
                entry.get("description"),
                entry.get("allowModelInvocation", False),
            )
            print(f"skills/{entry['name']}  <- {entry['repo']}@{entry['commit'][:7]}")

    rows = "\n".join(
        f"| `{e['name']}` | {e['stage']} | [{e['repo']}](https://github.com/{e['repo']}/tree/{e['commit']}/{e['path'].strip('./')}) | `{e['commit'][:7]}` | {e['license']} |"
        for e in manifest["skills"]
    )
    NOTICES.write_text(
        "# Third-party notices\n\n"
        "These skills are copied unchanged from the repositories below, at the pinned commits, "
        "with each one's license file kept in its folder. Two have a small frontmatter edit: "
        "`apple-design-system` has a narrower description so it only runs when an Apple-style "
        "direction is chosen, and `drawio-skill` drops `disable-model-invocation` so the "
        "architect stage can call it. Regenerate this file with `python3 scripts/update-toolkit.py`.\n\n"
        "| Skill | Stage | Source | Commit | License |\n| --- | --- | --- | --- | --- |\n"
        + rows + "\n"
    )


if __name__ == "__main__":
    main()
