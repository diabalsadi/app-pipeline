# Project state format

The state file is `pipeline/state.json` in Claude Code, or the "Pipeline status" document in a Claude Project. Both use this shape.

```json
{
  "project": "Plant Swap",
  "createdAt": "2026-10-08",
  "platform": null,
  "stages": {
    "discover":  { "status": "approved", "approvedAt": "2026-10-08", "outputs": ["docs/01-business-plan.md"] },
    "validate":  { "status": "awaiting_approval", "approvedAt": null, "outputs": ["docs/02-requirements.md"] },
    "design":    { "status": "not_started", "approvedAt": null, "outputs": [] },
    "architect": { "status": "not_started", "approvedAt": null, "outputs": [] },
    "setup":     { "status": "not_started", "approvedAt": null, "outputs": [] },
    "build":     { "status": "not_started", "approvedAt": null, "outputs": [] },
    "qa":        { "status": "not_started", "approvedAt": null, "outputs": [] }
  },
  "screens": [],
  "history": [
    { "at": "2026-10-08", "stage": "discover", "event": "approved", "note": "Founder approved the business plan." }
  ]
}
```

## Fields

- `project`: the app's working name, from the discover interview.
- `platform`: `"web"`, `"mobile"` or `"both"`, set by validate. It stays `null` until then.
- `stages.<name>.status`: one of the statuses below.
- `stages.<name>.approvedAt`: the date of the founder's approval, or `null`.
- `stages.<name>.outputs`: the files the stage produced.
- `screens`: filled by validate from the screen list as `{ "id": "S01", "name": "Sign up", "status": "not_started" }`. The build stage updates each screen's status.
- `history`: one entry per start, approval, change request, or reapproval, newest last.

## Statuses

| Status | Meaning |
| --- | --- |
| `not_started` | The stage has not begun. |
| `in_progress` | The stage is working, for example an interview or a draft. |
| `awaiting_approval` | The output is ready and the founder has been asked to approve it. |
| `approved` | The founder approved it on `approvedAt`. |
| `needs_reapproval` | An earlier approved output changed after this stage used it. |
