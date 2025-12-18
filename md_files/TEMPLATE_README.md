# Python Project Template

A comprehensive, production-ready template for Python projects with modern tooling, best practices, and complete automation.

## ✨ Features

- 🚀 **Modern Python** - Supports Python 3.9+
- 📦 **Package Management** - Uses pyproject.toml with pip or uv
- ✅ **Testing** - pytest with coverage reporting
- 🎨 **Code Quality** - Ruff, Black, isort, and mypy pre-configured
- 🔄 **CI/CD** - GitHub Actions workflows included
- 📚 **Documentation** - Sphinx setup with ReadTheDocs theme
- 🪝 **Pre-commit Hooks** - Automated code quality checks
- 🔒 **Security** - Built-in security scanning
- 🛠️ **Development Tools** - Makefile, tox, VS Code integration
- 📋 **Best Practices** - Proper project structure and community files

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone or download this template
git clone https://github.com/YOUR_USERNAME/python-project-template.git my-new-project
cd my-new-project

# Run the setup script
python setup_project.py

# Follow the prompts to enter:
# - Project name
# - Description
# - Author details
# - GitHub username
```

The script will automatically:
- Replace all template placeholders
- Create proper directory structure
- Move files to correct locations
- Prepare your project for development

### Option 2: Manual Setup

See [PROJECT_SETUP.md](PROJECT_SETUP.md) for detailed manual setup instructions.

## 📁 Project Structure

```
your-project/
├── .github/
│   └── workflows/        # CI/CD workflows
├── .vscode/              # VS Code settings
├── docs/                 # Sphinx documentation
├── scripts/              # Utility scripts
├── src/
│   └── your_project/     # Main package
├── tests/                # Test suite
├── pyproject.toml        # Project configuration
├── Makefile              # Convenient commands
└── ...                   # Community files
```

## 🛠️ Development Workflow

### Initial Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Common Commands

```bash
make test          # Run tests with coverage
make lint          # Check code quality
make format        # Auto-format code
make type-check    # Run type checking
make ci            # Run full CI pipeline locally
make docs          # Build documentation
make clean         # Clean build artifacts
```

### Running Tests

```bash
# Quick test run
pytest tests/

# With coverage
pytest tests/ --cov=src --cov-report=html

# Using tox (multiple environments)
tox -e pytest
```

### Code Quality

```bash
# Lint code
ruff check src tests

# Format code
black src tests
isort src tests

# Type check
mypy src

# Run all checks
make ci
```

## 📝 What's Included

### Configuration Files

- **pyproject.toml** - Project metadata, dependencies, and tool configurations
- **tox.ini** - Test automation across multiple Python versions
- **Makefile** - Convenient development commands
- **.pre-commit-config.yaml** - Automated pre-commit hooks
- **.gitignore** - Comprehensive ignore rules

### Documentation

- **README.md** - Project overview (template)
- **PROJECT_SETUP.md** - Detailed setup guide
- **CHANGELOG.md** - Version history
- **CONTRIBUTING.md** - Contribution guidelines
- **CODE_OF_CONDUCT.md** - Community standards
- **SUPPORT.md** - Getting help
- **SECURITY.md** - Security policy
- **LICENSE** - MIT License

### Development Tools

- **docs/** - Sphinx documentation setup
- **scripts/validate_project.py** - Project structure validation
- **setup_project.py** - Automated project initialization
- **.vscode/** - VS Code configuration with recommended extensions

### CI/CD

- **GitHub Actions** - Automated testing, linting, and building
  - Multi-version Python testing (3.9, 3.10, 3.11, 3.12)
  - Multi-OS testing (Ubuntu, macOS, Windows)
  - Security scanning
  - Coverage reporting

## 🔧 Customization

### Adding Dependencies

Edit `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]
```

Then reinstall:
```bash
pip install -e .[dev]
```

### Configuring Tools

All tools are configured in `pyproject.toml`:

- `[tool.ruff]` - Linting configuration
- `[tool.black]` - Code formatting
- `[tool.isort]` - Import sorting
- `[tool.mypy]` - Type checking
- `[tool.pytest.ini_options]` - Test configuration

### Adding New Modules

1. Create: `src/your_project/new_module.py`
2. Test: `tests/test_new_module.py`
3. Document: Update `docs/modules.rst`
4. Export: Add desired exports in `src/your_project/main.py` or create explicit module files and export from them

## 📦 Publishing

### Build Package

```bash
python -m build
```

### Publish to PyPI

```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## 🤝 Contributing

This template itself welcomes contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This template is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Your projects created from this template can use any license you choose.

## 🆘 Support

- 📖 [Detailed Setup Guide](PROJECT_SETUP.md)
- 🐛 [Report Issues](https://github.com/YOUR_USERNAME/python-project-template/issues)
- 💬 [GitHub Discussions](https://github.com/YOUR_USERNAME/python-project-template/discussions)

## 🙏 Acknowledgments

Built with modern Python best practices and inspired by:
- [Python Packaging Authority](https://www.pypa.io/)
- [PyPA Sample Project](https://github.com/pypa/sampleproject)
- [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)

## ⭐ Features at a Glance

| Feature | Tool/Config |
|---------|-------------|
| Package Management | `pyproject.toml`, pip, uv |
| Testing | pytest, coverage, tox |
| Linting | Ruff |
| Formatting | Black, isort |
| Type Checking | mypy |
| Documentation | Sphinx, ReadTheDocs |
| CI/CD | GitHub Actions |
| Pre-commit | Multiple hooks configured |
| Code Security | pip-audit, safety |
| VS Code | Settings, launch, extensions |
| Automation | Makefile, setup script |

---

**Made with ❤️ for the Python community**
