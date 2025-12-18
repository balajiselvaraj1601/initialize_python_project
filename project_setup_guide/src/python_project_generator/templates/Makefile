.PHONY: help install install-dev test lint format type-check clean build docs ci pre-commit

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package
	pip install -e .

install-dev:  ## Install package with dev dependencies
	pip install -e .[dev]

test:  ## Run tests
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

test-fast:  ## Run tests without coverage
	pytest tests/ -v

lint:  ## Run linting checks
	ruff check src tests
	black --check src tests
	isort --check-only src tests

format:  ## Format code
	ruff check src tests --fix
	black src tests
	isort src tests

type-check:  ## Run type checking
	mypy src

clean:  ## Clean build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov/
	rm -rf .tox/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

build:  ## Build distribution packages
	python -m build

docs:  ## Build documentation
	cd docs && sphinx-build -b html . _build

docs-serve:  ## Serve documentation locally
	cd docs && python -m http.server --directory _build 8000

ci:  ## Run full CI pipeline
	tox -e ci

pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

setup-env:  ## Set up development environment
	python -m venv .venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source .venv/bin/activate  # macOS/Linux"
	@echo "  .venv\\Scripts\\activate     # Windows"

publish-test:  ## Publish to TestPyPI
	python -m twine upload --repository testpypi dist/*

publish:  ## Publish to PyPI
	python -m twine upload dist/*
