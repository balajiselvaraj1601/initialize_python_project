# Using This Template

## For Template Users

This is a **template repository**. To use it:

1. **Run the setup script**:
   ```bash
   python setup_project.py
   ```
   
   This will:
   - Prompt you for project details
   - Replace all `{{PLACEHOLDER}}` values
   - Create the proper directory structure (`src/`, `tests/`, `docs/`)
   - Move template files to their correct locations

2. **Verify the setup**:
   ```bash
   python scripts/validate_project.py
   ```
   
   Should now show all checks passing.

3. **Start developing**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   make test
   ```

## For Template Maintainers

The template intentionally has:
- ❗ Placeholders like `{{PROJECT_NAME}}` - **Expected**, replaced by setup script
- ❗ Missing `src/`, `tests/`, `docs/` directories - **Expected**, created by setup script
- ❗ Template files with `template_` prefix - **Expected**, moved by setup script

Running `python scripts/validate_project.py` on the template itself will show issues. This is normal.

## Documentation

- **TEMPLATE_README.md** - About this template
- **PROJECT_SETUP.md** - Detailed setup guide
- **FIX_SUMMARY.md** - What was fixed in this version
- **README.md** - Will be your project's README (contains placeholders)

## Files Overview

### Template Files (moved during setup)
- `template___init__.py` → `src/YOUR_PROJECT/__init__.py`
- `template_main.py` → `__main__.py`
- `template_tests___init__.py` → `tests/__init__.py`
- `src_template_main.py` → `src/YOUR_PROJECT/main.py`
- `tests_template_test_main.py` → `tests/test_main.py`
- `docs_*.rst` → `docs/*.rst`

### Automation Scripts
- `setup_project.py` - Initialize new project
- `scripts/validate_project.py` - Validate structure

### Configuration
- `pyproject.toml` - Project metadata and tool config
- `tox.ini` - Test automation
- `Makefile` - Convenient commands
- `.pre-commit-config.yaml` - Pre-commit hooks
- `.vscode/` - VS Code configuration
- `.github/workflows/` - CI/CD

### Documentation
- `PROJECT_SETUP.md` - Setup instructions
- `CONTRIBUTING.md` - Contribution guide
- `CODE_OF_CONDUCT.md` - Community standards
- `SUPPORT.md` - Getting help
- `SECURITY.md` - Security policy
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License

## Quick Commands

After running `setup_project.py`:

```bash
make help         # Show all commands
make install-dev  # Install with dev dependencies
make test         # Run tests
make lint         # Check code quality
make format       # Auto-format code
make ci           # Run full CI pipeline
make clean        # Remove build artifacts
```

## Support

- 📖 Read `TEMPLATE_README.md` for features
- 📋 Read `PROJECT_SETUP.md` for detailed setup
- 🐛 Check `FIX_SUMMARY.md` for what was fixed
- ❓ Open an issue for questions
