#!/usr/bin/env python3
"""Check an Authenticity Profile against the OP pass rules and draw its radar.

Usage:  python check_gate.py path/to/profile.json [--no-radar]

Prints each pass rule with a verdict, the overall status, and writes radar.svg
next to profile.json. Exit code 0 = rules 1-4 pass, 1 = not yet, 2 = invalid file.
"""
import json
import math
import sys
from pathlib import Path

CRITICAL = ["01", "03", "06", "12"]
NAMES = {
    "01": "Audience", "02": "Persona", "03": "Culture & Values", "04": "Accessibility & Inclusion",
    "05": "Market & Region", "06": "Language & Script", "07": "Context of Use", "08": "Local Ecosystem",
    "09": "Industry & Domain", "10": "Brand DNA", "11": "Business Model", "12": "Trust & Compliance",
    "13": "Visual Identity", "14": "Interaction Patterns", "15": "Voice & Tone", "16": "Content & Imagery",
}
LENS_OF = {f"{i:02d}": ["people", "place", "purpose", "presence"][(i - 1) // 4] for i in range(1, 17)}
COLORS = {"people": "#D4553A", "place": "#15806C", "purpose": "#C98A12", "presence": "#6A3D8F"}


def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    dims = {d["id"]: d for d in data.get("dimensions", [])}
    problems = []
    for i in NAMES:
        if i not in dims:
            problems.append(f"dimension {i} ({NAMES[i]}) is missing")
        elif not isinstance(dims[i].get("score"), int) or not 0 <= dims[i]["score"] <= 3:
            problems.append(f"dimension {i} has no valid 0-3 score")
    return data, dims, problems


def evaluate(data, dims):
    scores = {i: dims[i]["score"] for i in NAMES}
    avg = sum(scores.values()) / 16
    zeros = [i for i, s in scores.items() if s == 0]
    weak_critical = [i for i in CRITICAL if scores[i] < 2]
    sig = data.get("signatures") or {}
    lead = (sig.get("authenticity_lead") or {})
    client = (sig.get("client") or {})
    signed = bool(lead.get("name") and lead.get("date") and client.get("name") and client.get("date"))
    rules = [
        ("No dimension at 0", not zeros,
         "none at 0" if not zeros else "at 0: " + ", ".join(f"{i} {NAMES[i]}" for i in zeros)),
        ("Average of all 16 is 2.0 or higher", round(avg, 2) >= 2.0, f"average {avg:.1f}"),
        ("Critical four (01, 03, 06, 12) at 2 or higher", not weak_critical,
         "all at 2+" if not weak_critical else "below 2: " + ", ".join(f"{i} {NAMES[i]} ({scores[i]})" for i in weak_critical)),
        ("Generic diff resolved", bool(data.get("generic_diff_resolved")),
         "resolved" if data.get("generic_diff_resolved") else "unexplained overlaps remain"),
        ("Two signatures (Authenticity Lead + founder/client)", signed,
         f"signed by {lead.get('name')} and {client.get('name')}" if signed else "waiting for both signatures"),
    ]
    first_four = all(r[1] for r in rules[:4])
    status = "Approved" if first_four and signed else ("Ready for sign-off" if first_four else "Not yet")
    return {"scores": scores, "average": round(avg, 2), "rules": rules, "status": status}


def radar_svg(scores, size=320):
    c = size / 2
    R = size * 0.36
    def pt(i, v):
        a = math.radians(i * 22.5 - 90)
        return c + R * v / 3 * math.cos(a), c + R * v / 3 * math.sin(a)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}" font-family="sans-serif">']
    for lv in (1, 2, 3):
        pts = " ".join("%.1f,%.1f" % pt(i, lv) for i in range(16))
        style = 'stroke="#16172B" stroke-width="1.4" stroke-dasharray="4 4"' if lv == 2 else 'stroke="#E4DACA" stroke-width="1"'
        out.append(f'<polygon points="{pts}" fill="none" {style}/>')
    for i in range(16):
        x, y = pt(i, 3)
        out.append(f'<line x1="{c}" y1="{c}" x2="{x:.1f}" y2="{y:.1f}" stroke="#E4DACA"/>')
    ids = list(NAMES)
    poly = " ".join("%.1f,%.1f" % pt(k, scores[i]) for k, i in enumerate(ids))
    out.append(f'<polygon points="{poly}" fill="#E8B33C" fill-opacity=".25" stroke="#E8B33C" stroke-width="2"/>')
    for k, i in enumerate(ids):
        x, y = pt(k, scores[i])
        col = COLORS[LENS_OF[i]]
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{col}"/>')
        lx, ly = pt(k, 3.55)
        out.append(f'<text x="{lx:.1f}" y="{ly + 3.5:.1f}" text-anchor="middle" font-size="10" font-weight="600" fill="{col}">{i}</text>')
    out.append(f'<text x="{c + 3}" y="{c - R * 2 / 3 - 4:.1f}" font-size="8" fill="#16172B">pass line 2</text>')
    out.append("</svg>")
    return "".join(out)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = Path(sys.argv[1])
    data, dims, problems = load(path)
    if problems:
        print("profile.json is not complete:")
        for p in problems:
            print(" -", p)
        sys.exit(2)
    res = evaluate(data, dims)
    print(f"Authenticity gate — {data.get('product', '?')}")
    for n, (name, ok, note) in enumerate(res["rules"], 1):
        mark = "PASS" if ok else ("WAITING" if n == 5 else "FAIL")
        print(f"  {n}. {name}: {mark} — {note}")
    print(f"Average: {res['average']:.1f} / 3")
    print(f"Status: {res['status']}")
    if "--no-radar" not in sys.argv:
        out = path.with_name("radar.svg")
        out.write_text(radar_svg(res["scores"]), encoding="utf-8")
        print(f"Radar written to {out}")
    sys.exit(0 if res["status"] != "Not yet" else 1)


if __name__ == "__main__":
    main()
