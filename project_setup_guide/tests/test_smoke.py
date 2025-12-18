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
                "--no-git",  # Skip git for faster tests
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


class TestGeneratedProjectStructure:
    """Test that generated project has correct structure and files."""

    @pytest.fixture(scope="class")
    def generated_project(self):
        """Generate a test project once for all structure tests."""
        from python_project_generator.generator import ProjectGenerator

        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_struct_")
        output_dir = Path(temp_dir)
        
        generator = ProjectGenerator(
            project_name="test_structure_check",
            description="Project for structure validation",
            author_name="Test User",
            author_email="test@test.com",
            github_username="testgithub",
            output_dir=output_dir,
        )

        project_path = generator.generate(force=False, init_git=False)
        
        yield project_path
        
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)

    def test_root_files_exist(self, generated_project):
        """Test that all required root files exist."""
        required_files = [
            "README.md",
            "pyproject.toml",
            "LICENSE",
            ".gitignore",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "SUPPORT.md",
            "SECURITY.md",
            "Makefile",
            "tox.ini",
            ".pre-commit-config.yaml",
            "__main__.py",
        ]

        for filename in required_files:
            file_path = generated_project / filename
            assert file_path.exists(), f"Required file missing: {filename}"

    def test_directory_structure(self, generated_project):
        """Test that required directories exist."""
        required_dirs = [
            "src",
            "src/test_structure_check",
            "tests",
            "docs",
            "scripts",
            ".github",
            ".github/workflows",
            ".vscode",
        ]

        for dir_path in required_dirs:
            full_path = generated_project / dir_path
            assert full_path.exists(), f"Required directory missing: {dir_path}"
            assert full_path.is_dir(), f"Path exists but is not a directory: {dir_path}"

    def test_source_package_files(self, generated_project):
        """Test that source package has required files."""
        src_dir = generated_project / "src" / "test_structure_check"
        
        required_files = [
            "__init__.py",
            "main.py",
        ]

        for filename in required_files:
            file_path = src_dir / filename
            assert file_path.exists(), f"Source file missing: {filename}"

    def test_test_files_exist(self, generated_project):
        """Test that test files exist."""
        tests_dir = generated_project / "tests"
        
        required_files = [
            "__init__.py",
            "test_main.py",
        ]

        for filename in required_files:
            file_path = tests_dir / filename
            assert file_path.exists(), f"Test file missing: {filename}"

    def test_documentation_files(self, generated_project):
        """Test that documentation files exist."""
        docs_dir = generated_project / "docs"
        
        required_files = [
            "conf.py",
            "index.rst",
            "installation.rst",
            "usage.rst",
            "modules.rst",
        ]

        for filename in required_files:
            file_path = docs_dir / filename
            assert file_path.exists(), f"Documentation file missing: {filename}"

    def test_github_workflows(self, generated_project):
        """Test that GitHub workflows exist."""
        workflows_dir = generated_project / ".github" / "workflows"
        
        # At least one workflow should exist
        workflow_files = list(workflows_dir.glob("*.yml")) + list(workflows_dir.glob("*.yaml"))
        assert len(workflow_files) > 0, "No GitHub workflow files found"

    def test_vscode_configuration(self, generated_project):
        """Test that VS Code configuration exists."""
        vscode_dir = generated_project / ".vscode"
        
        config_files = [
            "settings.json",
            "extensions.json",
            "launch.json",
        ]

        for filename in config_files:
            file_path = vscode_dir / filename
            assert file_path.exists(), f"VS Code config file missing: {filename}"


class TestPlaceholderReplacement:
    """Test that placeholders are correctly replaced in generated files."""

    @pytest.fixture(scope="class")
    def test_project(self):
        """Generate a test project for placeholder validation."""
        from python_project_generator.generator import ProjectGenerator

        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_placeholder_")
        output_dir = Path(temp_dir)
        
        generator = ProjectGenerator(
            project_name="placeholder_test_proj",
            description="Testing placeholder replacement",
            author_name="John Doe",
            author_email="john@example.com",
            github_username="johndoe",
            output_dir=output_dir,
        )

        project_path = generator.generate(force=False, init_git=False)
        
        yield project_path
        
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)

    def test_pyproject_toml_placeholders(self, test_project):
        """Test that pyproject.toml has no unreplaced placeholders."""
        pyproject_path = test_project / "pyproject.toml"
        content = pyproject_path.read_text()
        
        # Check that placeholders are replaced
        assert "placeholder_test_proj" in content, "Project name not replaced"
        assert "John Doe" in content, "Author name not replaced"
        assert "john@example.com" in content, "Email not replaced"
        
        # Check that no unreplaced placeholders exist
        assert "{{PROJECT_NAME}}" not in content, "Unreplaced PROJECT_NAME placeholder"
        assert "{{AUTHOR_NAME}}" not in content, "Unreplaced AUTHOR_NAME placeholder"
        assert "{{AUTHOR_EMAIL}}" not in content, "Unreplaced AUTHOR_EMAIL placeholder"
        assert "{{GITHUB_USERNAME}}" not in content, "Unreplaced GITHUB_USERNAME placeholder"

    def test_readme_placeholders(self, test_project):
        """Test that README has no unreplaced placeholders."""
        readme_path = test_project / "README.md"
        content = readme_path.read_text()
        
        # Check that no unreplaced placeholders exist
        assert "{{PROJECT_NAME}}" not in content, "Unreplaced PROJECT_NAME in README"

    def test_init_file_placeholders(self, test_project):
        """Test that __init__.py has correct values."""
        init_path = test_project / "src" / "placeholder_test_proj" / "__init__.py"
        content = init_path.read_text()
        
        # Should contain actual values
        assert "Testing placeholder replacement" in content
        assert "John Doe" in content
        assert "john@example.com" in content


class TestProjectNameSanitization:
    """Test that project names are properly sanitized."""

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary directory for test output."""
        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_sanitize_")
        yield Path(temp_dir)
        if Path(temp_dir).exists():
            shutil.rmtree(temp_dir)

    def test_sanitize_project_name_with_dashes(self, temp_output_dir):
        """Test that project names with dashes are converted to underscores."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="my-cool-project",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        # Should be sanitized to underscores
        assert generator.project_name == "my_cool_project"

    def test_sanitize_project_name_with_spaces(self, temp_output_dir):
        """Test that project names with spaces are converted to underscores."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="My Cool Project",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        assert generator.project_name == "my_cool_project"

    def test_sanitize_project_name_uppercase(self, temp_output_dir):
        """Test that project names are converted to lowercase."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="MyProject",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        assert generator.project_name == "myproject"

    def test_sanitize_project_name_starting_with_number(self, temp_output_dir):
        """Test that project names starting with numbers get prefixed."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="123project",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        assert generator.project_name.startswith("project_")
        assert not generator.project_name[0].isdigit()


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary directory for test output."""
        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_edge_")
        yield Path(temp_dir)
        if Path(temp_dir).exists():
            shutil.rmtree(temp_dir)

    def test_project_already_exists_without_force(self, temp_output_dir):
        """Test that existing project raises error without force flag."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="existing_project",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        # Create project first time
        project_path = generator.generate(force=False, init_git=False)
        assert project_path.exists()

        # Try to create again without force
        with pytest.raises(FileExistsError):
            generator.generate(force=False, init_git=False)

    def test_project_overwrite_with_force(self, temp_output_dir):
        """Test that existing project can be overwritten with force flag."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="force_project",
            description="Test",
            author_name="Test",
            author_email="test@test.com",
            github_username="test",
            output_dir=temp_output_dir,
        )

        # Create project first time
        project_path1 = generator.generate(force=False, init_git=False)
        assert project_path1.exists()

        # Create a marker file
        marker = project_path1 / "marker.txt"
        marker.write_text("original")

        # Overwrite with force
        project_path2 = generator.generate(force=True, init_git=False)
        assert project_path2.exists()
        
        # Marker file should be gone (project was recreated)
        assert not marker.exists()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
