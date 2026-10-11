#!/usr/bin/env bash
# Zips each skill folder so it can be uploaded to claude.ai (Settings > Capabilities > Skills)
# and used inside a Claude Project. Output: dist/<skill>.zip
# With --extras, also zips every extra plugin's skills into dist/extras/<plugin>/<skill>.zip.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "$root/dist" && mkdir -p "$root/dist"
for dir in "$root"/plugins/app-pipeline/skills/*/; do
  name="$(basename "$dir")"
  (cd "$root/plugins/app-pipeline/skills" && zip -qr "$root/dist/$name.zip" "$name")
  echo "dist/$name.zip"
done
if [[ "${1:-}" == "--extras" ]]; then
  python3 "$root/scripts/package-extras.py"
fi
