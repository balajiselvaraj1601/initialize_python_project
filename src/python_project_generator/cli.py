"""
Command-line interface for Python Project Generator.

This module provides the CLI commands for generating new Python projects.
"""

import argparse
import sys
from pathlib import Path

from python_project_generator.generator import ProjectGenerator


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate production-ready Python projects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (prompts for details)
  python-project-generator

  # Non-interactive mode
  python-project-generator --name YOUR_PROJECT --author "John Doe" \
    --email john@example.com

  # Specify output directory
  python-project-generator --output /path/to/projects

  # Show version
  python-project-generator --version
        """,
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )

    parser.add_argument(
        "--name",
        "-n",
        help="Project name (e.g., my_awesome_project)",
    )

    parser.add_argument(
        "--description",
        "-d",
        help="Project description",
    )

    parser.add_argument(
        "--author",
        "-a",
        help="Author name",
    )

    parser.add_argument(
        "--email",
        "-e",
        help="Author email",
    )

    parser.add_argument(
        "--github-username",
        "-g",
        help="GitHub username",
    )

    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path.cwd(),
        help="Output directory (default: current directory)",
    )

    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force overwrite if project directory exists",
    )

    parser.add_argument(
        "--no-git",
        action="store_true",
        help="Skip git initialization",
    )

    args = parser.parse_args()

    # Interactive mode if no project name provided
    if not args.name:
        generator = ProjectGenerator.from_interactive()
    else:
        # Validate all required fields are provided in non-interactive mode
        if not all([args.description, args.author, args.email, args.github_username]):
            parser.error(
                "In non-interactive mode, all of --name, --description, "
                "--author, --email, and --github-username are required"
            )

        generator = ProjectGenerator(
            project_name=args.name,
            description=args.description,
            author_name=args.author,
            author_email=args.email,
            github_username=args.github_username,
            output_dir=args.output,
        )

    try:
        generator.generate(
            force=args.force,
            init_git=not args.no_git,
        )

        return 0

    except Exception:
        return 1


if __name__ == "__main__":
    sys.exit(main())
