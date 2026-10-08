# Project state format

The state file is `pipeline/state.json` in Claude Code, or the "Pipeline status" document in a Claude Project. Both use this shape.

```json
{
  "project": "Plant Swap",
  "createdAt": "2026-10-08",
  "platform": null,
  "product": null,
  "repo": null,
  "backend": null,
  "stages": {
    "business":     { "status": "approved", "approvedAt": "2026-10-08", "outputs": ["docs/01-business/"] },
    "authenticity": { "status": "awaiting_approval", "approvedAt": null, "outputs": ["docs/02-authenticity/AUTHENTICITY.md"], "round": 2, "score": 1.9 },
    "design":       { "status": "not_started", "approvedAt": null, "outputs": [] },
    "architect":    { "status": "not_started", "approvedAt": null, "outputs": [] },
    "setup":        { "status": "not_started", "approvedAt": null, "outputs": [] },
    "frontend":     { "status": "not_started", "approvedAt": null, "outputs": [] },
    "backend":      { "status": "not_started", "approvedAt": null, "outputs": [] },
    "qa":           { "status": "not_started", "approvedAt": null, "outputs": [] }
  },
  "screens": [],
  "history": [
    { "at": "2026-10-08", "stage": "business", "event": "approved", "note": "Founder approved the business documents." }
  ]
}
```

## Fields

- `project`: the app's working name, from the business interview.
- `platform`: `"web"`, `"mobile"` or `"both"`, set by the business stage from the product profile. It stays `null` until then.
- `product`: set when business is approved: `{ "name": "Billing", "prefix": "BIL", "type": "surface", "features": [{ "code": "INV", "name": "Invoicing" }] }`. `type` is `"surface"`, `"service"` or `"engine"`. Later stages use the prefix and codes to find and cite business IDs.
- `stages.<name>.status`: one of the statuses below.
- `stages.<name>.approvedAt`: the date of the founder's approval, or `null`.
- `stages.<name>.outputs`: the files the stage produced.
- `stages.authenticity.round` and `score`: the number of passes through the authenticity loop and the latest average score, so the history shows it converging.
- `repo`: the app's GitHub repo URL, set by setup. It stays `null` until then.
- `backend`: set at the start of the backend stage: `{ "mode": "new" }` or `{ "mode": "existing", "location": "<repo or API address>" }`. Never put secrets here.
- `screens`: filled by the design stage from `docs/03-design/screen-list.md` as `{ "id": "S01", "name": "Sign up", "status": "not_started" }`. The frontend stage moves each screen through `not_started`, `in_progress`, `awaiting_founder`, `changes_requested`, `in_review`, and `done`, and adds `"pr"` (the merged pull request URL) when done.
- `history`: one entry per start, approval, change request, or reapproval, newest last.

## Statuses

| Status | Meaning |
| --- | --- |
| `not_started` | The stage has not begun. |
| `in_progress` | The stage is working, for example an interview or a draft. |
| `awaiting_approval` | The output is ready and the founder has been asked to approve it. |
| `approved` | The founder approved it on `approvedAt`. |
| `needs_reapproval` | An earlier approved output changed after this stage used it. |
