#!/bin/bash

# --- CONFIG ---
TARGET_BRANCH="main"  # Change this to your desired branch
EXTRAS="dev"          # Optional: pip install extras like pip install -e .[dev]

# --- STEP 1: Verify git repo ---
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "❌ This is not a git repository."
  exit 1
fi

# --- STEP 2: Check current branch ---
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$CURRENT_BRANCH" != "$TARGET_BRANCH" ]; then
  echo "⚠️  You are on branch '$CURRENT_BRANCH', but this script requires '$TARGET_BRANCH'."
  echo "👉  Run: git checkout $TARGET_BRANCH"
  exit 1
fi

# --- STEP 3: Install in editable mode ---
echo "✅ On branch '$CURRENT_BRANCH'. Installing in editable mode..."
pip install -e .["$EXTRAS"]

# --- STEP 4: Confirm install ---
if [ $? -eq 0 ]; then
  echo "✅ Installed successfully from branch '$CURRENT_BRANCH'."
else
  echo "❌ Installation failed."
  exit 1
fi