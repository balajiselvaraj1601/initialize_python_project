#!/usr/bin/env python3
"""Validate that the project is properly set up."""

import sys
from pathlib import Path

# Required files for project validation
REQUIRED_FILES = [
    "pyproject.toml",
    "README.md",
    "LICENSE",
    ".gitignore",
    "Makefile",
    "tox.ini",
    ".pre-commit-config.yaml",
]

# Required directories for project validation
REQUIRED_DIRS = [
    "src",
    "tests",
    "docs",
    "scripts",
    ".github/workflows",
    ".vscode",
]


def _check_package(project_root: Path, errors: list[str]) -> None:
    """Check the package structure."""
    src_dirs = list((project_root / "src").glob("*"))
    if len(src_dirs) != 1 or not src_dirs[0].is_dir():
        errors.append("src/ should contain exactly one package directory")
    else:
        package_dir = src_dirs[0]
        if not (package_dir / "__init__.py").exists():
            errors.append(f"Missing __init__.py in {package_dir}")
        if not (package_dir / "main.py").exists():
            errors.append(f"Missing main.py in {package_dir}")


def validate_function() -> int:
    """Validate the project structure."""
    project_root = Path(__file__).parent.parent

    errors = []

    # Check for required files
    errors.extend(
        [
            f"Missing required file: {file}"
            for file in REQUIRED_FILES
            if not (project_root / file).exists()
        ]
    )

    # Check for required directories
    errors.extend(
        [
            f"Missing required directory: {directory}"
            for directory in REQUIRED_DIRS
            if not (project_root / directory).is_dir()
        ]
    )

    # Check for package
    _check_package(project_root, errors)

    # Check tests
    if not (project_root / "tests" / "__init__.py").exists():
        errors.append("Missing __init__.py in tests/")
    if not (project_root / "tests" / "test_main.py").exists():
        errors.append("Missing test_main.py in tests/")

    if errors:
        print("Project validation failed:")  # noqa: T201
        for error in errors:
            print(f"  - {error}")  # noqa: T201
        return 1

    print("Project validation passed!")  # noqa: T201
    return 0


if __name__ == "__main__":
    sys.exit(validate_function())
