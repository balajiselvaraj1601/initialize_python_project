````markdown
# Python Project Repository Setup Guide

This guide provides a step-by-step process for creating a Python project repository using a modern, reproducible layout.

## Quick Start (tox-only)

Follow these steps to get started using `tox` for development and CI tasks.

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
tox -l           # list available tox environments
tox -e pytest    # run tests
tox -e lint      # run linters
```

## Using `uv` (PyPI CLI)

This repository supports using the `uv` CLI to create and maintain reproducible virtual environments and sync dependencies.

On macOS (zsh) a recommended flow is:

```bash
# install uv (prefer pipx for isolation)
python -m pip install --user pipx && python -m pipx ensurepath
pipx install uv

# in your project root: create and sync environment
uv sync

# activate the created environment (created in .venv by default)
source .venv/bin/activate

# install editable dev dependencies (fallback)
pip install -e .[dev]
```

`uv sync` will create the virtual environment and install packages declared in `pyproject.toml` (including dev extras when configured). Use `uv add <pkg>` or `uv remove <pkg>` to manage dependencies and `uv sync` again to apply changes.


````
