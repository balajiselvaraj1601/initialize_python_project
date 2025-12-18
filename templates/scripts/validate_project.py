#!/usr/bin/env python3
"""Validate that the project is properly set up."""

import sys
from pathlib import Path


def main() -> int:
    """Validate the project structure."""
    project_root = Path(__file__).parent.parent

    errors = []

    # Check for required files
    required_files = [
        "pyproject.toml",
        "README.md",
        "LICENSE",
        ".gitignore",
        "Makefile",
        "tox.ini",
        ".pre-commit-config.yaml",
    ]

    for file in required_files:
        if not (project_root / file).exists():
            errors.append(f"Missing required file: {file}")

    # Check for required directories
    required_dirs = [
        "src",
        "tests",
        "docs",
        "scripts",
        ".github/workflows",
        ".vscode",
    ]

    for dir in required_dirs:
        if not (project_root / dir).is_dir():
            errors.append(f"Missing required directory: {dir}")

    # Check for package
    src_dirs = list((project_root / "src").glob("*"))
    if len(src_dirs) != 1 or not src_dirs[0].is_dir():
        errors.append("src/ should contain exactly one package directory")
    else:
        package_dir = src_dirs[0]
        if not (package_dir / "__init__.py").exists():
            errors.append(f"Missing __init__.py in {package_dir}")
        if not (package_dir / "main.py").exists():
            errors.append(f"Missing main.py in {package_dir}")

    # Check tests
    if not (project_root / "tests" / "__init__.py").exists():
        errors.append("Missing __init__.py in tests/")
    if not (project_root / "tests" / "test_main.py").exists():
        errors.append("Missing test_main.py in tests/")

    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Project validation passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
