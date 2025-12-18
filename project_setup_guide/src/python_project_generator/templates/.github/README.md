# GitHub templates for Python projects

This folder contains reusable workflows, issue/PR templates, and community files intended as a template for new repositories.

Quick notes:

- CI: Use `./.github/workflows/ci.yml` — it calls `ci-reusable.yml` which defaults to Python `3.10,3.11,3.12`.
- Publish: `publish-pypi.yml` is included but disabled by default. To enable publishing:
  1. Add `PYPI_API_TOKEN` to repository secrets.
  2. Remove the `if: false` guard in `publish-pypi.yml` or modify it to `if: github.event.inputs.enable == 'true'`.
- Reuse patterns:
  - Reference workflows directly: `uses: your-org/your-templates-repo/.github/workflows/ci-reusable.yml@v1`
  - Or copy the `.github` folder into a new repo/submodule for full control.
