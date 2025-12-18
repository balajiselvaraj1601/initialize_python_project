#!/usr/bin/env python3
"""
Validation script to check if the project structure is correct.

Usage:
    python scripts/validate_project.py
"""

import sys
from pathlib import Path
from typing import List, Tuple


def check_file_exists(path: Path, required: bool = True) -> Tuple[bool, str]:
    """Check if a file exists."""
    if path.exists():
        return True, f"✓ {path}"
    else:
        status = "✗" if required else "○"
        return not required, f"{status} {path} (missing)"


def validate_structure() -> bool:
    """Validate the project structure."""
    project_root = Path(__file__).parent.parent
    
    print("Validating project structure...")
    print("=" * 60)
    
    all_valid = True
    
    # Required files
    required_files = [
        'pyproject.toml',
        'README.md',
        'LICENSE',
        '.gitignore',
        'CHANGELOG.md',
        'CODE_OF_CONDUCT.md',
        'CONTRIBUTING.md',
        'SUPPORT.md',
        'SECURITY.md',
    ]
    
    print("\nRequired files:")
    for file_name in required_files:
        valid, msg = check_file_exists(project_root / file_name)
        print(f"  {msg}")
        all_valid = all_valid and valid
    
    # Optional files
    optional_files = [
        'tox.ini',
        'Makefile',
        '.pre-commit-config.yaml',
    ]
    
    print("\nOptional files:")
    for file_name in optional_files:
        valid, msg = check_file_exists(project_root / file_name, required=False)
        print(f"  {msg}")
    
    # Check directory structure
    print("\nDirectory structure:")
    required_dirs = [
        'src',
        'tests',
        'docs',
    ]
    
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists() and dir_path.is_dir():
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ (missing)")
            all_valid = False
    
    # Check for placeholders
    print("\nChecking for unreplaced placeholders:")
    files_to_check = [
        project_root / 'pyproject.toml',
        project_root / 'README.md',
    ]
    
    placeholders_found = False
    for file_path in files_to_check:
        if file_path.exists():
            content = file_path.read_text()
            if '{{' in content and '}}' in content:
                print(f"  ⚠ {file_path.name} contains placeholders")
                placeholders_found = True
    
    if not placeholders_found:
        print("  ✓ No placeholders found")
    else:
        print("\n  Note: Run setup_project.py to replace placeholders")
    
    print("\n" + "=" * 60)
    if all_valid:
        print("✓ Project structure is valid!")
        return True
    else:
        print("✗ Project structure has issues")
        return False


if __name__ == '__main__':
    sys.exit(0 if validate_structure() else 1)
