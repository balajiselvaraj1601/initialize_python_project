````markdown
# Contributing to {{PROJECT_NAME}}

Thank you for considering contributing! We appreciate your help in making this project better.

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/balajiselvaraj1601/{{PROJECT_NAME}}.git
   cd {{PROJECT_NAME}}
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .[dev]
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description
   ```

2. Make your changes and ensure code quality:
   ```bash
   # Run tests
   pytest tests/ -v

   # Run linting
   ruff check src tests --fix
   black src tests
   isort src tests

   # Run type checking
   mypy src

   # Or run everything at once
   tox -e ci
   ```

3. Commit your changes:
   - Use clear, descriptive commit messages
   - Follow conventional commit format: `type(scope): description`
   - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
   - Example: `feat(api): add new endpoint for user data`

4. Push and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Guidelines

- Target the `main` branch
- Include a clear description of changes
- Add tests for new features
- Update documentation as needed
- Ensure all CI checks pass
- Reference any related issues

## Code Style

- Follow PEP 8 (enforced by Black and Ruff)
- Add type hints to function signatures
- Write docstrings for public APIs (Google style)
- Keep functions focused and testable

## Testing

- Write tests for all new features
- Maintain or improve code coverage
- Test edge cases and error conditions
- Run the full test suite before submitting

## Questions?

Feel free to open an issue for discussion or ask in pull request comments.

See `CODE_OF_CONDUCT.md` for community guidelines.

````
