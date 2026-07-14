#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$ROOT_DIR/PROJECTMIND_v4.0_PUBLIC_RESEARCH_EDITION.md"
OUTPUT="$ROOT_DIR/PROJECTMIND_v4.0_PUBLIC_RESEARCH_EDITION.pdf"
HEADER="$ROOT_DIR/pdf-header.tex"

command -v pandoc >/dev/null 2>&1 || {
  echo "ERROR: pandoc is required." >&2
  exit 1
}

command -v xelatex >/dev/null 2>&1 || {
  echo "ERROR: xelatex is required." >&2
  exit 1
}

pandoc "$SOURCE" \
  --from=gfm+yaml_metadata_block \
  --pdf-engine=xelatex \
  --include-in-header="$HEADER" \
  --toc \
  --toc-depth=1 \
  --highlight-style=tango \
  --variable=papersize:a4 \
  --variable=geometry:margin=21mm \
  --variable=fontsize:9pt \
  --variable=linestretch:1.06 \
  --variable=mainfont:"DejaVu Serif" \
  --variable=sansfont:"DejaVu Sans" \
  --variable=monofont:"DejaVu Sans Mono" \
  --variable=colorlinks:true \
  --variable=linkcolor:projectblue \
  --variable=urlcolor:projectblue \
  --metadata=pagetitle:"ProjectMind v4.0 Public Research Edition" \
  --output="$OUTPUT"

echo "Created: $OUTPUT"
