"""
Tests for validate_project.py
"""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from validate_project import REQUIRED_DIRS, REQUIRED_FILES
from validate_project import validate_function as validate_main


class TestValidateProject:
    """Test the project validation functionality."""

    @pytest.fixture
    def temp_project_dir(self):
        """Create a temporary directory for test project."""
        temp_dir = tempfile.mkdtemp(prefix="test_validate_")
        return Path(temp_dir)
        # Cleanup will be handled by pytest

    def create_valid_project_structure(self, project_root: Path):
        """Create a minimal valid project structure."""
        # Required files
        file_contents = {
            "pyproject.toml": "# pyproject.toml",
            "README.md": "# README",
            "LICENSE": "MIT License",
            ".gitignore": "*.pyc",
            "Makefile": "all:",
            "tox.ini": "[tox]",
            ".pre-commit-config.yaml": "repos: []",
        }
        for file in REQUIRED_FILES:
            content = file_contents.get(file, "")
            (project_root / file).write_text(content)

        # Required directories
        for directory in REQUIRED_DIRS:
            Path(project_root / directory).mkdir(parents=True, exist_ok=True)

        # Package structure
        package_dir = project_root / "src" / "mypackage"
        package_dir.mkdir()
        (package_dir / "__init__.py").write_text("")
        (package_dir / "main.py").write_text("def main(): pass")

        # Test structure
        (project_root / "tests" / "__init__.py").write_text("")
        (project_root / "tests" / "test_main.py").write_text("def test_main(): pass")

    def test_valid_project_passes(self, temp_project_dir):
        """Test that a valid project structure passes validation."""
        self.create_valid_project_structure(temp_project_dir)

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 0

    def test_missing_required_files(self, temp_project_dir):
        """Test validation fails when required files are missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove a required file
        (temp_project_dir / "pyproject.toml").unlink()

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_missing_required_directories(self, temp_project_dir):
        """Test validation fails when required directories are missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove a required directory
        shutil.rmtree(temp_project_dir / "src")

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_invalid_package_structure_no_src(self, temp_project_dir):
        """Test validation fails when src/ directory is missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove src directory
        shutil.rmtree(temp_project_dir / "src")

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_invalid_package_structure_multiple_packages(self, temp_project_dir):
        """Test validation fails when src/ has multiple package directories."""
        self.create_valid_project_structure(temp_project_dir)

        # Add another package directory
        extra_package = temp_project_dir / "src" / "extrapackage"
        extra_package.mkdir()
        (extra_package / "__init__.py").write_text("")

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_invalid_package_structure_no_init(self, temp_project_dir):
        """Test validation fails when package __init__.py is missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove __init__.py
        (temp_project_dir / "src" / "mypackage" / "__init__.py").unlink()

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_invalid_package_structure_no_main(self, temp_project_dir):
        """Test validation fails when package main.py is missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove main.py
        (temp_project_dir / "src" / "mypackage" / "main.py").unlink()

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_missing_test_init(self, temp_project_dir):
        """Test validation fails when tests/__init__.py is missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove tests/__init__.py
        (temp_project_dir / "tests" / "__init__.py").unlink()

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1

    def test_missing_test_main(self, temp_project_dir):
        """Test validation fails when tests/test_main.py is missing."""
        self.create_valid_project_structure(temp_project_dir)

        # Remove tests/test_main.py
        (temp_project_dir / "tests" / "test_main.py").unlink()

        with patch("validate_project.Path") as mock_path:
            mock_path.return_value.parent.parent = temp_project_dir
            exit_code = validate_main()

        assert exit_code == 1
