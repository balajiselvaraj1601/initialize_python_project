# Python Project Generator

[![PyPI version](https://badge.fury.io/py/python-project-generator.svg)](https://badge.fury.io/py/python-project-generator)
[![Python Support](https://img.shields.io/pypi/pyversions/python-project-generator.svg)](https://pypi.org/project/python-project-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
- ✅ **Testing** - pytest with coverage reporting
- 🎨 **Code Quality** - Ruff and mypy pre-configured
- 🔄 **CI/CD** - GitHub Actions workflows included
- 📚 **Documentation** - Sphinx setup with ReadTheDocs theme
- 🪝 **Pre-commit Hooks** - Automated code quality checks
- 🔒 **Security** - Built-in security scanning
- 🛠️ **Development Tools** - Makefile, tox, VS Code integration
- 📋 **Best Practices** - Proper project structure and community files

## 🎯 Quick Start

### Interactive Mode (Recommended)

Simply run the command and follow the prompts:

```bash
python-project-generator
```

or

```bash
create-python-project
```

You'll be prompted for:
- Project name
- Project description
- Author name
- Author email
- GitHub username

### Non-Interactive Mode

Provide all details via command-line arguments:

```bash
python-project-generator \
  --name my_awesome_project \
  --description "My awesome Python project" \
  --author "John Doe" \
  --email john@example.com \
  --github-username johndoe
```

### Advanced Options

```bash
# Specify output directory
python-project-generator --output /path/to/projects

# Force overwrite existing directory
python-project-generator --force

# Skip git initialization
python-project-generator --no-git

# Show version
python-project-generator --version

# Show help
python-project-generator --help
```

## 📋 What Gets Generated

Your new project will include:

```
my_awesome_project/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── .vscode/
│   ├── settings.json           # VS Code settings
│   ├── launch.json             # Debug configurations
│   └── extensions.json         # Recommended extensions
├── docs/
│   ├── conf.py                 # Sphinx configuration
│   ├── index.rst               # Documentation home
│   ├── installation.rst        # Install guide
│   ├── usage.rst               # Usage examples
│   └── modules.rst             # API reference
├── scripts/
│   └── validate_project.py     # Project validation
├── src/
│   └── my_awesome_project/
│       ├── __init__.py         # Package initialization
│       └── main.py             # Main module with example code
├── tests/
│   ├── __init__.py
│   └── test_main.py            # Test suite
├── .gitignore                  # Comprehensive ignore rules
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
└── tox.ini                     # Test automation
```

## 🛠️ Post-Generation Setup

After generating your project:

```bash
cd my_awesome_project

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install

# Run tests to verify everything works
make test

# Start developing!
```

## 📚 Development Workflow

The generated project includes convenient make commands:

```bash
make help          # Show all available commands
make test          # Run tests with coverage
make lint          # Check code quality
make format        # Auto-format code
make type-check    # Run type checking
make ci            # Run full CI pipeline locally
make docs          # Build documentation
make clean         # Remove build artifacts
```

Or use tox for testing across multiple Python versions:

```bash
tox -e pytest      # Run tests
tox -e lint        # Run linting
tox -e type        # Run type checking
tox -e ci          # Run full CI pipeline
```

## 🎨 Customization

The generated project is fully customizable:

### Adding Dependencies

Edit `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]
```

### Configuring Tools

All tools are pre-configured in `pyproject.toml`:
- `[tool.ruff]` - Linting, formatting, and import sorting
- `[tool.mypy]` - Type checking
- `[tool.pytest.ini_options]` - Test configuration

## 📦 Publishing Your Project

When ready to publish:

```bash
# Build the package
python -m build

# Test on TestPyPI first
twine upload --repository testpypi dist/*

# Publish to PyPI
twine upload dist/*
```

## 🆘 Getting Help

- 📖 [Full Documentation](https://github.com/YOUR_USERNAME/python-project-generator)
- 🐛 [Report Issues](https://github.com/YOUR_USERNAME/python-project-generator/issues)
- 💬 [GitHub Discussions](https://github.com/YOUR_USERNAME/python-project-generator/discussions)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Projects generated by this tool can use any license you choose.

## 🙏 Acknowledgments

Built with modern Python best practices and inspired by:
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [PyPA Sample Project](https://github.com/pypa/sampleproject)
- [Python Packaging Authority](https://www.pypa.io/)

## ⭐ Features at a Glance

| Feature | Included |
|---------|----------|
| Modern pyproject.toml | ✅ |
| GitHub Actions CI/CD | ✅ |
| Pre-commit hooks | ✅ |
| Testing with pytest | ✅ |
| Code formatting and linting (Ruff) | ✅ |
| Type checking (mypy) | ✅ |
| Documentation (Sphinx) | ✅ |
| VS Code integration | ✅ |
| Makefile shortcuts | ✅ |
| Tox automation | ✅ |
| Security scanning | ✅ |
| Community files | ✅ |
| Git initialization | ✅ |

## 🔧 Command Reference

### Interactive Mode
```bash
python-project-generator
```

### Non-Interactive Mode
```bash
python-project-generator \
  --name PROJECT_NAME \
  --description "Description" \
  --author "Author Name" \
  --email author@email.com \
  --github-username username
```

### Options
- `--name, -n` - Project name
- `--description, -d` - Project description
- `--author, -a` - Author name
- `--email, -e` - Author email
- `--github-username, -g` - GitHub username
- `--output, -o` - Output directory (default: current directory)
- `--force, -f` - Force overwrite existing directory
- `--no-git` - Skip git initialization
- `--version` - Show version
- `--help` - Show help message

## 🚀 Examples

### Basic Usage
```bash
# Interactive
python-project-generator

# With all options
python-project-generator \
  --name my_api \
  --description "REST API service" \
  --author "Jane Smith" \
  --email jane@example.com \
  --github-username janesmith
```

### Custom Output Location
```bash
python-project-generator \
  --name web_scraper \
  --output ~/projects \
  --author "Developer" \
  --email dev@example.com \
  --github-username devuser \
  --description "Web scraping tool"
```

### Overwrite Existing
```bash
python-project-generator --name my_project --force
```

---

**Made with ❤️ for the Python community**

**Star ⭐ this repo if you find it helpful!**
