# 🚀 Quick Start Guide - Python Project Generator

## Installation

```bash
# From this repository (development mode)
cd project_setup_guide
pip install -e .
```

## Usage

### 🎯 Interactive Mode (Easiest)

```bash
python-project-generator
```

Follow the prompts to enter your project details.

### 🤖 Non-Interactive Mode (For Automation)

```bash
python-project-generator \
  --name my_awesome_project \
  --description "My awesome Python project" \
  --author "Your Name" \
  --email "your.email@example.com" \
  --github-username yourusername
```

### 📋 Common Options

```bash
# Custom output directory
python-project-generator --output ~/projects

# Force overwrite existing project
python-project-generator --force

# Skip git initialization
python-project-generator --no-git

# Show help
python-project-generator --help

# Show version
python-project-generator --version
```

## After Generation

```bash
# Navigate to your new project
cd my_awesome_project

# Set up development environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .[dev]

# Set up pre-commit hooks
pre-commit install

# Run tests
make test

# Start coding!
code .  # Or your preferred editor
```

## What You Get

✅ Complete project structure  
✅ GitHub Actions CI/CD  
✅ Pre-commit hooks  
✅ Testing with pytest  
✅ Code quality tools (ruff, black, mypy, isort)  
✅ Documentation with Sphinx  
✅ VS Code configuration  
✅ Makefile with shortcuts  
✅ All community files (LICENSE, CONTRIBUTING, etc.)  

## Examples

### Example 1: Data Science Project

```bash
python-project-generator \
  --name data_analyzer \
  --description "Data analysis and visualization tool" \
  --author "Data Scientist" \
  --email "data@example.com" \
  --github-username datascientist
```

### Example 2: Web API

```bash
python-project-generator \
  --name api_service \
  --description "RESTful API service" \
  --author "Backend Developer" \
  --email "dev@example.com" \
  --github-username devuser \
  --output ~/work/projects
```

### Example 3: CLI Tool

```bash
python-project-generator \
  --name cli_tool \
  --description "Command-line utility" \
  --author "Developer" \
  --email "dev@example.com" \
  --github-username devuser \
  --no-git
```

## Makefile Commands

After generation, use these shortcuts:

```bash
make help          # Show all commands
make test          # Run tests with coverage
make lint          # Check code quality
make format        # Auto-format code
make type-check    # Run type checking
make ci            # Run full CI pipeline
make docs          # Build documentation
make clean         # Clean build artifacts
```

## Need Help?

- 📖 Read [INSTALL_README.md](INSTALL_README.md) for detailed documentation
- 📋 Read [PACKAGE_USAGE.md](PACKAGE_USAGE.md) for comprehensive usage guide
- 📝 Read [CONVERSION_SUMMARY.md](CONVERSION_SUMMARY.md) for technical details
- 🐛 Open an issue for bugs or questions

---

**That's it! You can now generate production-ready Python projects in seconds! 🎉**
