# Branching Strategy

This repository uses `dev` as the **default development branch**.
`main` is the **production/release branch** and only receives merges from `dev`.

## Rules for all agents and contributors

- **All pull requests MUST target `dev`** unless explicitly instructed to target `main`.
- **Never push directly to `main`**. Use the "Promote dev to main" workflow or create a PR from `dev` → `main`.
- When creating feature branches, branch off `dev` and merge back into `dev`.
- CI runs on pushes to `dev` and pull requests targeting `dev`.

## Workflow

1. `feature/*` → PR → `dev` (requires CI pass)
2. `dev` → PR → `main` (requires CI pass + approval, triggered via promotion workflow)
