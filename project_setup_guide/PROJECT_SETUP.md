# Python Project Repository Setup Guide

This guide provides a step-by-step process for creating a Python project repository using a modern, reproducible layout.

## Quick Start

**Using the automation script (recommended):**
```bash
python setup_project.py
```

This script will:
1. Prompt you for project details (name, author, etc.)
2. Replace all placeholders throughout the template
3. Create the proper directory structure
4. Move template files to their correct locations

**Manual setup** is described in the sections below if you prefer full control.

---

## Prerequisites

- **Python 3.9+** (recommended: 3.11 or 3.12)
- **git** - version control
- **pip** - package installer (included with Python)

**Optional but recommended:**
- `uv` - fast Python package installer ([install guide](https://github.com/astral-sh/uv))
- `make` - for convenient command shortcuts (usually pre-installed on macOS/Linux)

---

## Manual Setup Steps

### Step 1 — Clone or Copy This Template

Option A: Use this as a template
```bash
# If this is a GitHub template repository
gh repo create YOUR_PROJECT --template YOUR_USERNAME/python-project-template
cd YOUR_PROJECT
```

Option B: Copy manually
```bash
cp -r project_setup_guide YOUR_PROJECT_NAME
cd YOUR_PROJECT_NAME
git init
```

---

### Step 2 — Run Setup Script

```bash
python setup_project.py
```

The script will prompt you for:
- Project name (lowercase, underscores allowed)
- Project description
- Author name
- Author email
- GitHub username

It will then replace all `{{PLACEHOLDER}}` values throughout the template files.

**Verify:**
```bash
# Check that placeholders are replaced
grep -r "{{" pyproject.toml README.md
# Should return no results if successful
```

---

### Step 3 — Create Virtual Environment

Using venv (standard):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Using uv (faster):
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Verify:**
```bash
which python  # Should point to .venv/bin/python
python --version  # Should show Python 3.9+
```

---

### Step 4 — Install Dependencies

Using pip:
```bash
pip install --upgrade pip
pip install -e .[dev]
```

Using uv:
```bash
uv sync
```

**Verify:**
```bash
pip list  # Should show installed packages
pytest --version  # Should show pytest version
ruff --version  # Should show ruff version
```

---

### Step 5 — Install Pre-commit Hooks

```bash
pre-commit install
```

This sets up automatic code quality checks before each commit.

**Verify:**
```bash
pre-commit run --all-files  # Should run all hooks
```

---

### Step 6 — Verify Installation

Run the validation script:
```bash
python scripts/validate_project.py
```

Run tests:
```bash
make test
# Or manually:
pytest tests/ -v
```

**Troubleshooting:**

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and dependencies installed |
| `pytest: command not found` | Run `pip install -e .[dev]` again |
| Pre-commit hooks fail | Run `pre-commit run --all-files` to see specific issues |
| Import errors in tests | Check that package is installed with `pip list \| grep YOUR_PROJECT` |

---

## Project Structure

After setup, your project will have this structure:

```
YOUR_PROJECT/
├── .github/
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
├── CHANGELOG.md                # Version history
├── CODE_OF_CONDUCT.md          # Community guidelines
├── CONTRIBUTING.md             # Contribution guide
├── LICENSE                     # MIT License
├── Makefile                    # Convenient commands
├── pyproject.toml              # Project configuration
├── README.md                   # Project readme
├── SECURITY.md                 # Security policy
├── SUPPORT.md                  # Support information
└── tox.ini                     # Tox test environments
```

---

## Common Development Tasks

### Using Make Commands

```bash
make help                # Show all available commands
make install-dev         # Install with dev dependencies
make test                # Run tests with coverage
make lint                # Check code quality
make format              # Auto-format code
make type-check          # Run type checking
make clean               # Remove build artifacts
make docs                # Build documentation
make ci                  # Run full CI pipeline locally
```

### Using Tox

```bash
tox -e pytest            # Run tests
tox -e lint              # Run linting
tox -e type              # Run type checking
tox -e ci                # Run full CI pipeline
tox list                 # Show all environments
```

### Manual Commands

```bash
# Testing
pytest tests/ -v
pytest tests/ -v --cov=src --cov-report=html

# Linting and formatting
ruff check src tests --fix
ruff format src tests

# Type checking
mypy src

# Build package
python -m build

# Documentation
cd docs && sphinx-build -b html . _build
```

---

## Customization

### Adding Dependencies

Edit `pyproject.toml`:
```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    # Keep existing dev dependencies
    "ipython>=8.0.0",  # Add new ones here
]
```

Then reinstall:
```bash
pip install -e .[dev]
```

### Adding New Modules

1. Create new file: `src/YOUR_PROJECT/new_module.py`
2. Add tests: `tests/test_new_module.py`
3. Update docs: `docs/modules.rst`
4. Export in `__init__.py` if public API

### Configuring Tools

All tool configurations are in `pyproject.toml`:
- `[tool.ruff]` - Linting, formatting, and import sorting
- `[tool.mypy]` - Type checking
- `[tool.pytest.ini_options]` - Test configuration

---

## Publishing Your Package

### To TestPyPI (testing)

```bash
python -m build
make publish-test
# or
twine upload --repository testpypi dist/*
```

### To PyPI (production)

```bash
python -m build
make publish
# or
twine upload dist/*
```

---

## Continuous Integration

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically:

- Runs tests on multiple Python versions (3.9, 3.10, 3.11, 3.12)
- Runs tests on multiple OS (Ubuntu, macOS, Windows)
- Checks code quality (linting, formatting, type checking)
- Runs security audits
- Builds the package
- Reports coverage to Codecov

**To enable:**
1. Push your code to GitHub
2. The workflow runs automatically on push/PR
3. View results in the "Actions" tab

---

## Getting Help

- **Issues**: Check existing issues or open a new one
- **Documentation**: See the `docs/` folder
- **Validation**: Run `python scripts/validate_project.py`
- **Community**: See `SUPPORT.md` for support channels

---

## Next Steps

After running `setup_project.py`, you're ready to:

1. **Start Development**
   ```bash
   cd YOUR_PROJECT
   make test  # Verify everything works
   ```

2. **Create Your First Feature**
   - Edit `src/YOUR_PROJECT/main.py`
   - Add tests in `tests/`
   - Run `make ci` to verify

3. **Set Up GitHub Repository**
   ```bash
   git add .
   git commit -m "Initial commit"
   gh repo create YOUR_PROJECT --public --source=. --push
   # or manually create on GitHub and:
   git remote add origin https://github.com/USERNAME/YOUR_PROJECT.git
   git push -u origin main
   ```

4. **Enable GitHub Actions** - Push to GitHub and workflows run automatically

5. **Build Documentation**
   ```bash
   make docs
   open docs/_build/index.html  # View locally
   ```

---

## Troubleshooting Common Issues

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'YOUR_PROJECT'`

**Solution**:
```bash
# Ensure package is installed in editable mode
pip install -e .
# Verify installation
pip list | grep YOUR_PROJECT
```

### Virtual Environment Not Activated

**Problem**: Commands use system Python instead of venv

**Solution**:
```bash
# Activate the environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Verify
which python  # Should show .venv path
```

### Pre-commit Hooks Failing

**Problem**: Commits are blocked by pre-commit hooks

**Solution**:
```bash
# Run hooks manually to see errors
pre-commit run --all-files

# Auto-fix most issues
make format

# If persistent, temporarily skip (not recommended)
git commit --no-verify
```

### Tests Failing After Setup

**Problem**: Tests fail immediately after setup

**Solution**:
```bash
# Ensure all dependencies are installed
pip install -e .[dev]

# Check for placeholder values still present
grep -r "{{" src/ tests/

# Run validation script
python scripts/validate_project.py
```

### Tox Errors

**Problem**: `tox: command not found` or tox environments fail

**Solution**:
```bash
# Install tox
pip install tox

# List available environments
tox list

# Run specific environment with verbose output
tox -e pytest -v
```

---

## Template Maintenance

### Updating Dependencies

Periodically update dependencies for security and features:

```bash
# Show outdated packages
pip list --outdated

# Update specific package
pip install --upgrade PACKAGE_NAME

# Update all dev dependencies
pip install --upgrade pip setuptools wheel
pip install --upgrade -e .[dev]

# Test everything still works
make ci
```

### Updating Pre-commit Hooks

```bash
# Update hook versions
pre-commit autoupdate

# Test updated hooks
pre-commit run --all-files
```

---

## Advanced Configuration

### Custom CI Matrix

Edit `.github/workflows/ci.yml` to customize:
- Python versions tested
- Operating systems
- Additional jobs (security scans, deployments)

### Custom Make Targets

Add to `Makefile`:
```makefile
deploy:  ## Deploy to production
	@echo "Deploying..."
	# Your deployment commands

benchmark:  ## Run performance benchmarks
	pytest tests/ -v --benchmark-only
```

### Additional Documentation Pages

Add new `.rst` files in `docs/` and reference in `docs/index.rst`:
```rst
.. toctree::
   :maxdepth: 2
   
   installation
   usage
   your_new_page
```

---

## FAQ

**Q: Do I need to use `uv`?**  
A: No, standard `pip` and `venv` work fine. `uv` is faster but optional.

**Q: Can I use pytest-cov instead of coverage?**  
A: Yes, it's already configured in `pyproject.toml` and used by the test commands.

**Q: How do I add a CLI command?**  
A: The `[project.scripts]` section in `pyproject.toml` already defines one. After `pip install -e .`, you can run your project name as a command.

**Q: Should I commit `.venv/`?**  
A: No, it's already in `.gitignore`. Virtual environments are local only.

**Q: How do I change the license?**  
A: Replace `LICENSE` file content and update `pyproject.toml` classifiers.

**Q: Can I use a different test framework?**  
A: Yes, but you'll need to update `pyproject.toml`, `tox.ini`, and `Makefile` accordingly.

---

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Template Version**: 1.0.0  
**Last Updated**: December 2025  
**Python Support**: 3.9+
