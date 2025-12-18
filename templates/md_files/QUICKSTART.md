````markdown
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

---

**That's it! You can now generate production-ready Python projects in seconds! 🎉**

````
