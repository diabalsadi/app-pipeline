#!/usr/bin/env python3
"""Render the one-page Authenticity Card (self-contained HTML) from profile.json.

Usage:  python render_card.py path/to/profile.json path/to/authenticity-card.html
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_gate import load, evaluate, radar_svg, NAMES, LENS_OF, COLORS  # noqa: E402

TEMPLATE = Path(__file__).parent.parent / "assets" / "card-template.html"
LENS_LABEL = {"people": "PEOPLE", "place": "PLACE", "purpose": "PURPOSE", "presence": "PRESENCE"}


def short(s, limit=140):
    s = str(s or "").strip()
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def esc(s):
    return html.escape(str(s or ""))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    data, dims, problems = load(sys.argv[1])
    if problems:
        print("profile.json is not complete:", *problems, sep="\n - ")
        sys.exit(2)
    res = evaluate(data, dims)

    lens_blocks = []
    for lens in ["people", "place", "purpose", "presence"]:
        rows = []
        for i in NAMES:
            if LENS_OF[i] != lens:
                continue
            d = dims[i]
            dots = "".join(f'<i class="{"on" if k < d["score"] else ""}"></i>' for k in range(3))
            star = " ★" if i in ("01", "03", "06", "12") else ""
            rows.append(f'<div class="dim"><div class="dh"><b>{i}</b><span>{esc(NAMES[i])}{star}</span>'
                        f'<em class="dots">{dots}</em></div><p>{esc(short(d.get("summary", "")))}</p></div>')
        lens_blocks.append(f'<section class="lens" style="--c:{COLORS[lens]}"><h3>{LENS_LABEL[lens]}</h3>{"".join(rows)}</section>')

    rules = []
    for n, (name, ok, note) in enumerate(res["rules"], 1):
        cls = "ok" if ok else ("wait" if n == 5 else "no")
        mark = "✓" if ok else ("…" if n == 5 else "✕")
        rules.append(f'<li class="{cls}"><span>{mark}</span>{esc(name)}<small>{esc(note)}</small></li>')

    sig = data.get("signatures") or {}
    def sigline(key, role):
        s = sig.get(key) or {}
        return (f'<div class="sig"><small>{role}</small><b>{esc(s.get("name")) or "—"}</b>'
                f'<span>{esc(s.get("date")) or "not signed yet"}</span></div>')

    page = TEMPLATE.read_text(encoding="utf-8")
    repl = {
        "{{PRODUCT}}": esc(data.get("product")),
        "{{CLIENT}}": esc(data.get("client")),
        "{{TAGLINE}}": esc(data.get("tagline")),
        "{{DATE}}": esc(data.get("date")),
        "{{VERSION}}": esc(data.get("version")),
        "{{STATUS}}": esc(res["status"]),
        "{{STATUS_CLASS}}": {"Approved": "ok", "Ready for sign-off": "wait", "Not yet": "no"}[res["status"]],
        "{{FEELS_LIKE}}": esc(data.get("feels_like")),
        "{{ALWAYS}}": "".join(f"<li>{esc(x)}</li>" for x in data.get("always", [])),
        "{{NEVER}}": "".join(f"<li>{esc(x)}</li>" for x in data.get("never", [])),
        "{{SIGNATURE}}": esc(data.get("signature")),
        "{{AVERAGE}}": f'{res["average"]:.1f}',
        "{{RADAR}}": radar_svg(res["scores"], 300),
        "{{LENSES}}": "".join(lens_blocks),
        "{{RULES}}": "".join(rules),
        "{{SIGNATURES}}": sigline("authenticity_lead", "OP Authenticity Lead") + sigline("client", "Founder / client"),
    }
    for k, v in repl.items():
        page = page.replace(k, v)
    Path(sys.argv[2]).write_text(page, encoding="utf-8")
    print(f"Card written to {sys.argv[2]} — status: {res['status']}")


if __name__ == "__main__":
    main()
