````markdown
# {{PROJECT_NAME}}

A generic Python project with a well-organized structure.

## Installation

Using uv (recommended):
```bash
# install uv via pipx for an isolated CLI
pipx install uv

# create/sync the environment and install dependencies
uv sync

# activate the environment created by uv
source .venv/bin/activate
```

Or using pip:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .[dev]
```

## Usage

```python
from {{PROJECT_NAME}}.main import hello_world
print(hello_world())
```

## Development

```bash
# Run tests
tox -e pytest

# Run linting
tox -e lint

# Run type checking
tox -e type
```

## License

MIT

````
