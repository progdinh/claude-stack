#!/usr/bin/env bash
# Copy the reflex skills into ~/.claude/skills so you can type /go, /huh, /last ... without a prefix.
# Never overwrites: a skill you already have is skipped. Usage: tools/install-bare.sh [dest-dir]
set -euo pipefail
src="$(cd "$(dirname "$0")/.." && pwd)/plugins/reflexes/skills"
dest="${1:-$HOME/.claude/skills}"
mkdir -p "$dest"
for d in "$src"/*/; do
  n="$(basename "$d")"
  if [ -e "$dest/$n" ]; then echo "skip   $n (already in $dest)"; else cp -R "$d" "$dest/$n"; echo "added  $n"; fi
done
echo "Done. Start a new session, then type /go, /huh, /last, /progress, /your-take."
