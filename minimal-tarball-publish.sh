#!/bin/bash
# Minimal Tarball Publishing Script
# Usage: ./minimal-tarball-publish.sh <project-name> <version>

set -euo pipefail

PROJECT_NAME=$1
VERSION=$2
TARBALL="${PROJECT_NAME}-${VERSION}-clean.tar.gz"

# Package the project
tar -czvf "${TARBALL}" --exclude='.git' --exclude='venv' --exclude='__pycache__' --exclude='*.pyc' .

# Create GitHub release
gh release create "v${VERSION}" "./${TARBALL}" --title "v${VERSION}" --notes "Initial release: ${PROJECT_NAME}"

echo "Published: https://github.com/$(gh api user | jq -r '.login')/${PROJECT_NAME}/releases/tag/v${VERSION}"