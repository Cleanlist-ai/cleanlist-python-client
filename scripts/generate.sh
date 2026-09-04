#!/usr/bin/env bash
#
# Regenerate the Cleanlist Python SDK from the v2 OpenAPI schema.
#
# Produces two clients from the SAME spec using openapi-generator-cli (pinned to
# the version in openapitools.json, matching the backend):
#
#   cleanlist_ai        -> synchronous client  (urllib3)
#   cleanlist_ai/aio    -> asynchronous client (asyncio + aiohttp)
#
# Both ship inside the single `cleanlist-ai` distribution. Re-run this whenever
# openapi/cleanse-api-v2.oas.json changes.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

RAW_SPEC="openapi/cleanse-api-v2.oas.json"
BUILD="$ROOT/.build"
GEN_SPEC="$BUILD/spec.json"
PKG_VERSION="${PKG_VERSION:-2.0.0}"

PYTHON="${PYTHON:-python3}"
GEN=(npx --yes @openapitools/openapi-generator-cli generate)

echo "==> Cleaning previous build output"
rm -rf "$BUILD"
mkdir -p "$BUILD"

echo "==> Preparing spec (clean operationIds -> readable method names)"
"$PYTHON" scripts/prepare_spec.py "$RAW_SPEC" "$GEN_SPEC"

echo "==> Generating SYNC client (urllib3) -> cleanlist_ai"
"${GEN[@]}" \
  -i "$GEN_SPEC" \
  -g python \
  -o "$BUILD/sync" \
  --additional-properties="packageName=cleanlist_ai,projectName=cleanlist-ai,packageVersion=${PKG_VERSION},library=urllib3,generateSourceCodeOnly=true,hideGenerationTimestamp=true"

echo "==> Generating ASYNC client (asyncio/aiohttp) -> cleanlist_ai/aio"
"${GEN[@]}" \
  -i "$GEN_SPEC" \
  -g python \
  -o "$BUILD/async" \
  --additional-properties="packageName=cleanlist_ai.aio,projectName=cleanlist-ai-aio,packageVersion=${PKG_VERSION},library=asyncio,generateSourceCodeOnly=true,hideGenerationTimestamp=true"

echo "==> Assembling package tree"
rm -rf "$ROOT/cleanlist_ai"
cp -R "$BUILD/sync/cleanlist_ai" "$ROOT/cleanlist_ai"
# The async client is generated with packageName cleanlist_ai.aio, so it already
# lands at cleanlist_ai/aio inside its own build dir — nest it under the sync pkg.
cp -R "$BUILD/async/cleanlist_ai/aio" "$ROOT/cleanlist_ai/aio"

# Keep the importable package lean: move generated reference docs out, drop the
# generated unit-test stubs (they only assert models instantiate).
rm -rf "$ROOT/docs/reference"
mkdir -p "$ROOT/docs/reference"
[ -d "$ROOT/cleanlist_ai/docs" ] && mv "$ROOT/cleanlist_ai/docs" "$ROOT/docs/reference/sync" || true
[ -d "$ROOT/cleanlist_ai/aio/docs" ] && mv "$ROOT/cleanlist_ai/aio/docs" "$ROOT/docs/reference/async" || true
rm -rf "$ROOT/cleanlist_ai/test" "$ROOT/cleanlist_ai/aio/test"

echo "==> Applying hand-authored overlay (Cleanlist convenience facade)"
cp "$ROOT/overlay/sync/client.py" "$ROOT/cleanlist_ai/client.py"
cp "$ROOT/overlay/async/client.py" "$ROOT/cleanlist_ai/aio/client.py"
# Export the facade from each package's __init__ so `from cleanlist_ai import
# Cleanlist` (and the .aio variant) works. Idempotent: __init__ is regenerated
# fresh each run, so this appends exactly once.
for init in "cleanlist_ai/__init__.py" "cleanlist_ai/aio/__init__.py"; do
  base="$(dirname "$init" | tr '/' '.')"
  {
    echo ""
    echo "# --- Cleanlist convenience facade (appended by scripts/generate.sh) ---"
    echo "from ${base}.client import Cleanlist as Cleanlist"
    echo "__all__.append(\"Cleanlist\")"
  } >> "$ROOT/$init"
done

echo "==> Done. Packages:"
echo "    cleanlist_ai       (sync)"
echo "    cleanlist_ai/aio   (async)"
