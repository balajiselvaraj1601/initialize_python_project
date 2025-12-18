"""
Project generator core functionality.

This module handles the generation of new Python projects from templates.
"""

import re
import shutil
from datetime import date
from pathlib import Path
from typing import Dict, Optional


class ProjectGenerator:
    """Generate a new Python project from templates."""

    def __init__(
        self,
        project_name: str,
        description: str,
        author_name: str,
        author_email: str,
        github_username: str,
        output_dir: Path = Path.cwd(),
    ):
        """
        Initialize the project generator.

        Args:
            project_name: Name of the project (will be converted to valid Python package name)
            description: Project description
            author_name: Author's full name
            author_email: Author's email address
            github_username: GitHub username
            output_dir: Directory where project will be created
        """
        self.project_name = self._sanitize_project_name(project_name)
        self.description = description
        self.author_name = author_name
        self.author_email = author_email
        self.github_username = github_username
        self.output_dir = Path(output_dir)

        self.template_dir = Path(__file__).parent.parent.parent / "templates"

    @staticmethod
    def _sanitize_project_name(name: str) -> str:
        """
        Convert project name to valid Python package name.

        Args:
            name: Raw project name

        Returns:
            Sanitized package name (lowercase, underscores only)
        """
        # Convert to lowercase and replace non-alphanumeric with underscore
        name = re.sub(r"[^a-z0-9_]", "_", name.lower())
        # Remove leading/trailing underscores
        name = name.strip("_")
        # Replace multiple underscores with single
        name = re.sub(r"_+", "_", name)
        # Ensure it doesn't start with a number
        if name and name[0].isdigit():
            name = f"project_{name}"
        return name or "my_project"

    @classmethod
    def from_interactive(cls, output_dir: Path = Path.cwd()) -> "ProjectGenerator":
        """
        Create generator instance from interactive prompts.

        Args:
            output_dir: Directory where project will be created

        Returns:
            ProjectGenerator instance
        """
        print("=" * 70)
        print("Python Project Generator")
        print("=" * 70)
        print()

        project_name = input("Project name (e.g., my-awesome-project): ").strip()
        if not project_name:
            raise ValueError("Project name is required")

        description = input("Project description: ").strip() or "A Python project"
        author_name = input("Author name: ").strip() or "Developer"
        author_email = input("Author email: ").strip() or "dev@example.com"
        github_username = input("GitHub username: ").strip() or "username"

        print()
        print("Summary:")
        print("-" * 70)
        sanitized_name = cls._sanitize_project_name(project_name)
        print(f"Project name: {project_name} (package: {sanitized_name})")
        print(f"Description: {description}")
        print(f"Author: {author_name} <{author_email}>")
        print(f"GitHub: {github_username}")
        print("-" * 70)

        confirm = input("\nProceed with these values? (y/n): ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            raise SystemExit(0)

        return cls(
            project_name=project_name,
            description=description,
            author_name=author_name,
            author_email=author_email,
            github_username=github_username,
            output_dir=output_dir,
        )

    def _get_replacements(self) -> Dict[str, str]:
        """
        Get placeholder replacement mapping.

        Returns:
            Dictionary mapping placeholders to values
        """
    return {
        "{{PROJECT_NAME}}": self.project_name,
        "{{PROJECT_DESCRIPTION}}": self.description,
        "{{AUTHOR_NAME}}": self.author_name,
        "{{AUTHOR_EMAIL}}": self.author_email,
        "{{GITHUB_USERNAME}}": self.github_username,
        "{{CURRENT_YEAR}}": str(date.today().year),
    }

    def _replace_in_file(self, file_path: Path) -> None:
        """
        Replace placeholders in a file.

        Args:
            file_path: Path to file to process
        """
        try:
            content = file_path.read_text(encoding="utf-8")
            replacements = self._get_replacements()

            for placeholder, value in replacements.items():
                content = content.replace(placeholder, value)

            file_path.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"Warning: Could not process {file_path}: {e}")

    def _copy_template_files(self, project_path: Path) -> None:
        """
        Copy template files to project directory.

        Args:
            project_path: Path to new project directory
        """
        # Copy all template files
        for item in self.template_dir.rglob("*"):
            if item.is_file():
                rel_path = item.relative_to(self.template_dir)
                if 'md_files' in str(rel_path):
                    dest_path = project_path / item.name
                else:
                    dest_path = project_path / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_path)
                self._replace_in_file(dest_path)

    def _create_project_structure(self, project_path: Path) -> None:
        """
        Create the project directory structure.

        Args:
            project_path: Path to new project directory
        """
        # Create main directories
        (project_path / "src" / self.project_name).mkdir(parents=True, exist_ok=True)
        (project_path / "tests").mkdir(parents=True, exist_ok=True)
        (project_path / "docs").mkdir(parents=True, exist_ok=True)
        (project_path / "scripts").mkdir(parents=True, exist_ok=True)

        # Package files: create main module(s)

        # Create main.py
        main_content = '''"""Main module for the application."""\n\nimport logging\n\nlogger = logging.getLogger(__name__)\n\n\ndef hello_world() -> str:\n    """Return a greeting message."""\n    return "Hello, World!"\n\n\ndef main() -> None:\n    """Main entry point."""\n    logger.info(hello_world())\n\n\nif __name__ == "__main__":\n    logging.basicConfig(level=logging.INFO)\n    main()\n'''
        (project_path / "src" / self.project_name / "main.py").write_text(main_content)

        # Create __init__.py
        __init_content = f'''"""{{PROJECT_NAME}} package."""

__version__ = "0.1.0"

'''
        (project_path / "src" / self.project_name / "__init__.py").write_text(__init_content)

        # Create test files

        test_content = f'''"""Tests for main module."""\n\nimport pytest\nfrom {self.project_name}.main import hello_world\n\n\ndef test_hello_world():\n    """Test the hello_world function."""\n    assert hello_world() == "Hello, World!"\n\n\ndef test_hello_world_not_empty():\n    """Test that hello_world returns a non-empty string."""\n    result = hello_world()\n    assert isinstance(result, str)\n    assert len(result) > 0\n'''
        (project_path / "tests" / "test_main.py").write_text(test_content)

        # Create __init__.py for tests
        (project_path / "tests" / "__init__.py").write_text("")

        # Create __main__.py for CLI entry
        main_entry = f'''"""Main entry point for {self.project_name}"""\n\nimport sys\nfrom {self.project_name}.main import main\n\nif __name__ == "__main__":\n    sys.exit(main())\n'''
        (project_path / "__main__.py").write_text(main_entry)

    def generate(self, force: bool = False, init_git: bool = True) -> Path:
        """
        Generate the project.

        Args:
            force: Force overwrite if directory exists
            init_git: Initialize git repository

        Returns:
            Path to created project

        Raises:
            FileExistsError: If project directory exists and force=False
        """
        project_path = self.output_dir / self.project_name

        # Check if directory exists
        if project_path.exists():
            if not force:
                raise FileExistsError(
                    f"Directory '{project_path}' already exists. "
                    "Use --force to overwrite."
                )
            shutil.rmtree(project_path)

        # Create project directory
        project_path.mkdir(parents=True, exist_ok=True)

        print(f"\n📁 Creating project structure in {project_path}...")

        # Copy template files
        print("📋 Copying template files...")
        self._copy_template_files(project_path)

        # Create project structure
        print("🏗️  Creating project directories...")
        self._create_project_structure(project_path)

        # Initialize git if requested
        if init_git:
            import subprocess

            try:
                print("🔧 Initializing git repository...")
                subprocess.run(
                    ["git", "init"],
                    cwd=project_path,
                    check=True,
                    capture_output=True,
                )
                subprocess.run(
                    ["git", "add", "."],
                    cwd=project_path,
                    check=True,
                    capture_output=True,
                )
                subprocess.run(
                    ["git", "commit", "-m", "Initial commit from python-project-generator"],
                    cwd=project_path,
                    check=True,
                    capture_output=True,
                )
                print("✅ Git repository initialized")
            except subprocess.CalledProcessError:
                print("⚠️  Git initialization failed (git might not be installed)")
            except FileNotFoundError:
                print("⚠️  Git not found - skipping repository initialization")

        return project_path
