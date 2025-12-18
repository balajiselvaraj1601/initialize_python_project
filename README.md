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

Generated Project Structure
---------------------------
The generator creates a well-organized Python project with the following structure:

```
my_project/
├── .github/
│   ├── CODEOWNERS
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── actions/
│   │   └── verify-metadata/
│   │       └── action.yml
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI
├── .vscode/
│   ├── settings.json           # VS Code settings
│   ├── launch.json             # Debug configurations
│   └── extensions.json         # Recommended extensions
├── docs/
│   ├── conf.py                 # Sphinx configuration
│   ├── index.rst               # Documentation home
│   ├── installation.rst        # Install guide
│   ├── usage.rst               # Usage guide
│   └── modules.rst             # API reference
├── md_files/
│   ├── CHANGELOG.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── CONVERSION_SUMMARY.md
│   ├── FIX_SUMMARY.md
│   ├── INSTALL_README.md
│   ├── PACKAGE_USAGE.md
│   ├── QUICKSTART.md
│   ├── SECURITY.md
│   ├── SUPPORT.md
│   ├── TEMPLATE_README.md
│   └── USAGE.md
├── scripts/
│   └── validate_project.py     # Project validation
├── src/
│   └── my_project/
│       ├── __init__.py         # Package initialization
│       └── main.py             # Main module
├── tests/
│   ├── __init__.py
│   └── test_main.py            # Test suite
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # Pre-commit hooks
├── LICENSE                     # MIT License
├── Makefile                    # Convenient commands
├── pyproject.toml              # Project configuration
├── README.md                   # Project readme
├── __main__.py                 # CLI entry point
└── tox.ini                     # Tox test environments
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

Or using pip (installing the optional `uv` extras):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .[dev]

# Install with the uv extras (provides `uvicorn` and `uvloop`):
pip install .[uv]
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
