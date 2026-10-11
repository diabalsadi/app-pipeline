# GitHub setup

Run these from the scaffolded project folder, signed in with `gh` as the founder.

## 1. Create the repo and push

```bash
git init -b main
git add -A
git commit -m "Scaffold <app name> from the app pipeline"
gh repo create <app-name> --private --source=. --remote=origin --push
```

## 2. Add CI

Copy `ci.yml` (next to this file) to `.github/workflows/ci.yml`, adjust the scripts if the stack differs, then commit and push it. Wait for the first run with `gh run watch` and fix anything red before moving on.

## 3. Protect `main`

Create a ruleset that requires a pull request and the `checks` job to pass, and blocks force-pushes and deletion:

```bash
gh api repos/{owner}/{repo}/rulesets -X POST --input - <<'JSON'
{
  "name": "Protect main",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request", "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false } },
    { "type": "required_status_checks", "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [ { "context": "checks" } ] } }
  ]
}
JSON
```

Rulesets on private repos need a paid GitHub plan. If the call fails on a free plan, tell the founder in one line. The pipeline then enforces the same rule itself: it never pushes to `main` directly and merges only pull requests with green checks.

## 4. Create the labels

```bash
gh label create "bug" --color D73A4A --description "Something is not working" --force
gh label create "severity: critical" --color B60205 --description "Crash, data loss, security hole, or money handled wrongly" --force
gh label create "severity: high" --color D93F0B --description "Core feature broken with no workaround" --force
gh label create "severity: medium" --color FBCA04 --description "Works with a workaround, or fails in an edge case" --force
gh label create "severity: low" --color C5DEF5 --description "Cosmetic or wording" --force
gh label create "screen" --color 0E8A16 --description "Pull request that builds one screen" --force
```

## 5. Record it

Set `repo` in `pipeline/state.json` to the repo URL, and commit the state change through a pull request like any other change.
