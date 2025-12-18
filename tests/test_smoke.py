"""
Smoke test for python-project-generator package.

This test validates:
1. Package installation
2. Project generation
3. Generated project structure correctness
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


class TestPackageInstallation:
    """Test that the package can be imported and CLI is available."""

    def test_package_import(self):
        """Test that the package can be imported."""
        try:
            import python_project_generator
            assert python_project_generator.__version__ == "1.0.0"
        except ImportError as e:
            pytest.fail(f"Failed to import package: {e}")

    def test_cli_module_import(self):
        """Test that CLI module can be imported."""
        try:
            from python_project_generator import cli
            assert hasattr(cli, "main")
        except ImportError as e:
            pytest.fail(f"Failed to import CLI module: {e}")

    def test_generator_module_import(self):
        """Test that generator module can be imported."""
        try:
            from python_project_generator import generator
            assert hasattr(generator, "ProjectGenerator")
        except ImportError as e:
            pytest.fail(f"Failed to import generator module: {e}")

    def test_cli_command_available(self):
        """Test that the CLI command is available."""
        result = subprocess.run(
            ["python-project-generator", "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"CLI command failed: {result.stderr}"
        assert "1.0.0" in result.stdout, f"Unexpected version output: {result.stdout}"


class TestProjectGeneration:
    """Test project generation functionality."""

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary directory for test output."""
        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_")
        yield Path(temp_dir)
        # Cleanup
        if Path(temp_dir).exists():
            shutil.rmtree(temp_dir)

    def test_generate_project_via_cli(self, temp_output_dir):
        """Test generating a project via CLI command."""
        project_name = "test_smoke_project"
        
        # Run the CLI command
        result = subprocess.run(
            [
                "python-project-generator",
                "--name", project_name,
                "--description", "Test smoke project",
                "--author", "Test Author",
                "--email", "test@example.com",
                "--github-username", "testuser",
                "--output", str(temp_output_dir),
                "--no-git",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"CLI failed: {result.stderr}"
        
        project_path = temp_output_dir / project_name
        assert project_path.exists(), f"Project directory not created: {project_path}"

    def test_generate_project_programmatically(self, temp_output_dir):
        """Test generating a project programmatically."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="test_api_project",
            description="Test API project",
            author_name="Developer",
            author_email="dev@example.com",
            github_username="devuser",
            output_dir=temp_output_dir,
        )

        project_path = generator.generate(force=False, init_git=False)
        
        assert project_path.exists(), f"Project not created at {project_path}"
        assert project_path.name == "test_api_project"
