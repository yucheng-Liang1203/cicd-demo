#!/usr/bin/env bash
# Start the CI-CD Pipeline through the GitHub REST API (workflow_dispatch).
# Usage: GITHUB_TOKEN=github_pat_... ./scripts/trigger_pipeline.sh <owner>/<repo>
set -euo pipefail
REPO="$1"
curl -fsS -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/$REPO/actions/workflows/ci-cd.yml/dispatches" \
  -d '{"ref":"main"}'
echo "Requested. Watch it with: gh run watch  (or the Actions tab)"
