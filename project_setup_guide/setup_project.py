#!/usr/bin/env python3
"""
Setup script for creating a new project from this template.

Usage:
    python setup_project.py
"""

import re
import shutil
import sys
from pathlib import Path
from typing import Dict


def get_user_input() -> Dict[str, str]:
    """Prompt user for project details."""
    print("=" * 60)
    print("Python Project Template Setup")
    print("=" * 60)
    print()

    values = {}
    values["PROJECT_NAME"] = input("Project name (e.g., my_awesome_project): ").strip()
    values["PROJECT_DESCRIPTION"] = input("Project description: ").strip()
    values["AUTHOR_NAME"] = input("Author name: ").strip()
    values["AUTHOR_EMAIL"] = input("Author email: ").strip()
    values["GITHUB_USERNAME"] = input("GitHub username: ").strip()

    print()
    print("Summary:")
    print("-" * 60)
    for key, value in values.items():
        print(f"{key}: {value}")
    print("-" * 60)

    confirm = input("\nProceed with these values? (y/n): ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        sys.exit(0)

    return values


def replace_in_file(file_path: Path, replacements: Dict[str, str]) -> None:
    """Replace placeholders in a file."""
    try:
        content = file_path.read_text(encoding="utf-8")

        for placeholder, value in replacements.items():
            pattern = r"\{\{" + placeholder + r"\}\}"
            content = re.sub(pattern, value, content)

        file_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not process {file_path}: {e}")


def setup_project(project_dir: Path, values: Dict[str, str]) -> None:
    """Set up the project with user values."""
    print("\nSetting up project...")

    # Files and directories to process
    template_files = [
        "README.md",
        "pyproject.toml",
        "LICENSE",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SUPPORT.md",
        "docs_conf.py",
        "docs_index.rst",
        "docs_installation.rst",
        "docs_usage.rst",
        "docs_modules.rst",
        "template_main.py",
        "src_template_main.py",
        "tests_template_test_main.py",
        ".vscode/settings.json",
        ".vscode/launch.json",
    ]

    # Helper to locate files which may have been moved into repo-level `rst_files/`
    def find_file(file_name: str) -> Path | None:
        # 1) check in the template/project dir
        candidate = project_dir / file_name
        if candidate.exists():
            return candidate

        # 2) check in repo root `rst_files/`
        repo_root = project_dir.parent
        candidate = repo_root / "rst_files" / file_name
        if candidate.exists():
            return candidate

        # 3) check in repo root `rst_files/templates/docs/` (for template docs)
        candidate = repo_root / "rst_files" / "templates" / "docs" / file_name
        if candidate.exists():
            return candidate

        return None

    # Replace placeholders in all template files (searching fallback locations)
    for file_name in template_files:
        file_path = find_file(file_name)
        if file_path is not None:
            replace_in_file(file_path, values)
            print(
                f"✓ Processed {file_name} (from {file_path.relative_to(project_dir) if file_path.exists() else file_path})"
            )

    # Create proper directory structure
    src_dir = project_dir / "src" / values["PROJECT_NAME"]
    tests_dir = project_dir / "tests"
    docs_dir = project_dir / "docs"

    src_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    # Move template files to proper locations
    template_mappings = {
        "src_template_main.py": src_dir / "main.py",
        "tests_template_test_main.py": tests_dir / "test_main.py",
        "template_main.py": project_dir / "__main__.py",
        "docs_conf.py": docs_dir / "conf.py",
        "docs_index.rst": docs_dir / "index.rst",
        "docs_installation.rst": docs_dir / "installation.rst",
        "docs_usage.rst": docs_dir / "usage.rst",
        "docs_modules.rst": docs_dir / "modules.rst",
    }

    for source, dest in template_mappings.items():
        # try to find the source file in its original or moved location
        source_path = find_file(source)
        if source_path is not None:
            # ensure destination parent exists
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source_path), str(dest))
            print(f"✓ Moved {source} → {dest.relative_to(project_dir)}")

    # Create additional directories
    (project_dir / "scripts").mkdir(exist_ok=True)
    (project_dir / "assets").mkdir(exist_ok=True)
    (project_dir / "reports").mkdir(exist_ok=True)

    print("\n✓ Project structure created successfully!")
    print("\nNext steps:")
    print(f"1. cd {project_dir.name}")
    print("2. python -m venv .venv")
    print("3. source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate")
    print("4. pip install -e .[dev]")
    print("5. pre-commit install")
    print("6. git init && git add . && git commit -m 'Initial commit'")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent

    values = get_user_input()
    setup_project(script_dir, values)


if __name__ == "__main__":
    main()
