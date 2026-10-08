#!/usr/bin/env bash
# Zips each skill folder so it can be uploaded to claude.ai (Settings > Capabilities > Skills)
# and used inside a Claude Project. Output: dist/<skill>.zip
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "$root/dist" && mkdir -p "$root/dist"
for dir in "$root"/skills/*/; do
  name="$(basename "$dir")"
  (cd "$root/skills" && zip -qr "$root/dist/$name.zip" "$name")
  echo "dist/$name.zip"
done
