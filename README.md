# {{PROJECT_NAME}}

A generic Python project with a well-organized structure.

## Installation

Using uv:
```bash
uv sync
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
