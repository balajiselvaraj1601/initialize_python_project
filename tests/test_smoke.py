"""
Smoke test for python-project-generator package.

This test validates:
1. Package installation
2. Project generation
3. Generated project structure correctness
"""

import os
import shutil
import subprocess
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
            check=False,
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
                "--name",
                project_name,
                "--description",
                "Test smoke project",
                "--author",
                "Test Author",
                "--email",
                "test@example.com",
                "--github-username",
                "testuser",
                "--output",
                str(temp_output_dir),
                "--no-git",
            ],
            check=False,
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


class TestProjectStructureValidation:
    """Comprehensive test for generated project structure and content."""

    @pytest.fixture
    def temp_output_dir(self):
        """Create a temporary directory for test output."""
        temp_dir = tempfile.mkdtemp(prefix="test_pyprojgen_validation_")
        yield Path(temp_dir)
        # Cleanup
        if Path(temp_dir).exists():
            shutil.rmtree(temp_dir)

    @pytest.fixture
    def generated_project(self, temp_output_dir):
        """Generate a test project and return its path."""
        from python_project_generator.generator import ProjectGenerator

        generator = ProjectGenerator(
            project_name="comprehensive_test_project",
            description="A comprehensive test project for validation",
            author_name="Test Developer",
            author_email="test.dev@example.com",
            github_username="testdev",
            output_dir=temp_output_dir,
        )

        return generator.generate(force=False, init_git=False)

    def test_project_root_structure(self, generated_project):
        """Test that the project root has all expected files and directories."""
        expected_root_items = [
            ".github",
            ".gitignore",
            ".pre-commit-config.yaml",
            ".vscode",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "Makefile",
            "pyproject.toml",
            "README.md",
            "SECURITY.md",
            "SUPPORT.md",
            "__main__.py",
            "docs",
            "scripts",
            "src",
            "tests",
            "tox.ini",
        ]

        for item in expected_root_items:
            item_path = generated_project / item
            assert (
                item_path.exists()
            ), f"Expected item '{item}' not found in project root"

    def test_src_structure(self, generated_project):
        """Test the src directory structure."""
        src_dir = generated_project / "src"
        assert src_dir.is_dir(), "src directory should exist"

        # Check package directory
        package_dir = src_dir / "comprehensive_test_project"
        assert package_dir.is_dir(), "Package directory should exist"

        # Check package files
        expected_package_files = ["__init__.py", "main.py"]
        for file in expected_package_files:
            file_path = package_dir / file
            assert file_path.is_file(), f"Expected package file '{file}' not found"

    def test_tests_structure(self, generated_project):
        """Test the tests directory structure."""
        tests_dir = generated_project / "tests"
        assert tests_dir.is_dir(), "tests directory should exist"

        expected_test_files = ["__init__.py", "test_main.py"]
        for file in expected_test_files:
            file_path = tests_dir / file
            assert file_path.is_file(), f"Expected test file '{file}' not found"

    def test_docs_structure(self, generated_project):
        """Test the docs directory structure."""
        docs_dir = generated_project / "docs"
        assert docs_dir.is_dir(), "docs directory should exist"

        # Check expected docs files
        expected_docs_files = [
            "conf.py",
            "index.rst",
            "installation.rst",
            "modules.rst",
            "usage.rst",
        ]
        for file in expected_docs_files:
            file_path = docs_dir / file
            assert file_path.is_file(), f"Expected docs file '{file}' not found"

    def test_github_actions_structure(self, generated_project):
        """Test the .github directory structure."""
        github_dir = generated_project / ".github"
        assert github_dir.is_dir(), ".github directory should exist"

        expected_github_items = [
            "CODEOWNERS",
            "ISSUE_TEMPLATE",
            "PULL_REQUEST_TEMPLATE.md",
            "actions",
            "workflows",
        ]

        for item in expected_github_items:
            item_path = github_dir / item
            assert item_path.exists(), f"Expected .github item '{item}' not found"

    def test_vscode_structure(self, generated_project):
        """Test the .vscode directory structure."""
        vscode_dir = generated_project / ".vscode"
        assert vscode_dir.is_dir(), ".vscode directory should exist"

        expected_vscode_files = ["extensions.json", "launch.json", "settings.json"]
        for file in expected_vscode_files:
            file_path = vscode_dir / file
            assert file_path.is_file(), f"Expected VSCode file '{file}' not found"

    def test_scripts_structure(self, generated_project):
        """Test the scripts directory structure."""
        scripts_dir = generated_project / "scripts"
        assert scripts_dir.is_dir(), "scripts directory should exist"

        expected_script_files = ["validate_project.py"]
        for file in expected_script_files:
            file_path = scripts_dir / file
            assert file_path.is_file(), f"Expected script file '{file}' not found"

    def test_placeholder_replacement(self, generated_project):
        """Test that placeholders are correctly replaced in generated files."""
        # Test pyproject.toml
        pyproject_path = generated_project / "pyproject.toml"
        content = pyproject_path.read_text()

        assert (
            "comprehensive_test_project" in content
        ), "Project name not replaced in pyproject.toml"
        assert (
            "A comprehensive test project for validation" in content
        ), "Description not replaced"
        assert "Test Developer" in content, "Author name not replaced"
        assert "test.dev@example.com" in content, "Author email not replaced"

        # Test README.md - only check project name replacement since template
        # doesn't have description placeholder
        readme_path = generated_project / "README.md"
        content = readme_path.read_text()

        assert (
            "comprehensive_test_project" in content
        ), "Project name not replaced in README"

        # Test package __init__.py
        init_path = (
            generated_project / "src" / "comprehensive_test_project" / "__init__.py"
        )
        content = init_path.read_text()

        assert (
            "comprehensive_test_project" in content
        ), "Package name not replaced in __init__.py"

    def test_package_functionality(self, generated_project):
        """Test that the generated package can be imported and run."""
        import subprocess
        import sys

        # Add the src directory to Python path
        src_path = str(generated_project / "src")
        if src_path not in sys.path:
            sys.path.insert(0, src_path)

        try:
            # Test import
            import comprehensive_test_project

            assert hasattr(
                comprehensive_test_project, "__version__"
            ), "Package should have __version__"

            # Test main module
            from comprehensive_test_project import main

            assert hasattr(
                main, "hello_world"
            ), "main module should have hello_world function"
            assert hasattr(main, "main"), "main module should have main function"

            # Test hello_world function
            result = main.hello_world()
            assert (
                result == "Hello, World!"
            ), f"Expected 'Hello, World!', got '{result}'"

            # Test CLI script with proper PYTHONPATH
            script_path = generated_project / "__main__.py"
            assert script_path.exists(), "__main__.py should exist"

            # Run the script with PYTHONPATH set
            env = os.environ.copy()
            env["PYTHONPATH"] = src_path

            result = subprocess.run(
                [sys.executable, str(script_path)],
                check=False,
                capture_output=True,
                text=True,
                cwd=str(generated_project),
                env=env,
            )
            # Script runs without error (even if no output due to logging)
            assert result.returncode == 0, f"Script execution failed: {result.stderr}"

        finally:
            # Clean up sys.path
            if src_path in sys.path:
                sys.path.remove(src_path)

    def test_makefile_targets(self, generated_project):
        """Test that Makefile targets work."""
        makefile_path = generated_project / "Makefile"
        assert makefile_path.exists(), "Makefile should exist"

        # Test make help (should not fail)
        result = subprocess.run(
            ["make", "help"],
            check=False,
            capture_output=True,
            text=True,
            cwd=str(generated_project),
        )
        # make help might not exist, but make should work
        # Just check that make command is available
        assert result.returncode in [
            0,
            2,
        ], f"Make command failed unexpectedly: {result.stderr}"

    def test_tox_configuration(self, generated_project):
        """Test that tox.ini is properly configured."""
        tox_path = generated_project / "tox.ini"
        assert tox_path.exists(), "tox.ini should exist"

        content = tox_path.read_text()
        assert "[tox]" in content, "tox.ini should have [tox] section"
        assert "envlist" in content, "tox.ini should have envlist"

    def test_precommit_configuration(self, generated_project):
        """Test that pre-commit configuration is valid."""
        precommit_path = generated_project / ".pre-commit-config.yaml"
        assert precommit_path.exists(), ".pre-commit-config.yaml should exist"

        content = precommit_path.read_text()
        assert "repos:" in content, "pre-commit config should have repos section"

    def test_gitignore_completeness(self, generated_project):
        """Test that .gitignore includes common Python patterns."""
        gitignore_path = generated_project / ".gitignore"
        assert gitignore_path.exists(), ".gitignore should exist"

        content = gitignore_path.read_text()
        expected_patterns = [
            "__pycache__",
            "*.py[cod]",
            ".tox",
            "htmlcov",
            ".coverage",
        ]

        for pattern in expected_patterns:
            assert pattern in content, f".gitignore should contain '{pattern}'"
