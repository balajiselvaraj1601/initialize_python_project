# Python Project Generator

Generate production-ready Python projects with modern tooling and best practices.

## Quickstart

1. Install the package:

```bash
pip install python-project-generator
```

2. Run the CLI to generate a project:

```bash
python-project-generator
```

## Generated Project Structure

The generator creates a well-organized Python project with the following structure:

```
YOUR_PROJECT/
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
│   ├── SECURITY.md
│   └── SUPPORT.md
├── scripts/
│   └── validate_project.py     # Project validation
├── src/
│   └── YOUR_PROJECT/
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

## Layout

- `src/python_project_generator/` - generator package and CLI
- `templates/` - project templates used by the generator
- `docs/` - documentation and quickstart
- `tests/` - test suite for the generator

## Installation

From PyPI:
```bash
pip install python-project-generator
```

From source:
```bash
git clone https://github.com/balajiselvaraj1601/initialize_python_project.git
cd initialize_python_project
pip install -e .
```

## Usage

```bash
python-project-generator
```

Follow the prompts to create your project.

## License

MIT
