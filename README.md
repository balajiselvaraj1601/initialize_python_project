"""Project: python-project-generator

Purpose
-------
This repository provides a small, opinionated Python project scaffolder.

Quickstart
----------
1. Create a virtualenv and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the package in editable mode:

```bash
pip install -e .[dev]
```

3. Run the CLI to generate a project:

```bash
python -m python_project_generator.cli
# or installed entrypoint: python-project-generator
```

Layout
------
- `src/python_project_generator/` - generator package and CLI
- `templates/` - project templates used by the generator
- `docs/` - documentation and quickstart
- `tests/` - test suite for the generator

"""
# {{PROJECT_NAME}}

A generic Python project with a well-organized structure.

## Installation

Using uv (recommended):
```bash
# install uv via pipx (recommended)
pipx install uv

# create/sync the env and install deps from pyproject.toml
uv sync
```

Or using pip:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .[dev]
```

## Usage

```python
from {{PROJECT_NAME}}.main import hello_world
print(hello_world())
```

## Development

```bash
# Run tests
tox -e pytest

# Run linting
tox -e lint

# Run type checking
tox -e type
```

## License

MIT
