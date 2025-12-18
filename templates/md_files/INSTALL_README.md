````markdown
# Python Project Generator

[![PyPI version](https://badge.fury.io/py/python-project-generator.svg)](https://badge.fury.io/py/python-project-generator)

A comprehensive, production-ready project generator for Python projects with modern tooling, best practices, and complete automation.

## 🚀 Installation

### From PyPI (Recommended)

```bash
pip install python-project-generator
```

### From Source

```bash
git clone https://github.com/YOUR_USERNAME/python-project-generator.git
cd python-project-generator
pip install -e .
```

## ✨ Features

- 🚀 **Modern Python** - Supports Python 3.9+
- 📦 **Package Management** - Uses pyproject.toml with pip or uv

### Using `uv`

Install `uv` via `pipx` for an isolated CLI:

```bash
python -m pip install --user pipx && python -m pipx ensurepath
pipx install uv
```

Create and sync the environment from `pyproject.toml`:

```bash
uv sync
source .venv/bin/activate
```
- ✅ **Testing** - pytest with coverage reporting
- 🎨 **Code Quality** - Ruff and mypy pre-configured

````
