.PHONY: help install-dev test lint format type-check clean docs ci publish-test publish

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install-dev:  ## Install with dev dependencies
	pip install -e .[dev]

test:  ## Run tests with coverage
	pytest tests/ -v --cov=src --cov-report=html

lint:  ## Check code quality
	ruff check src tests scripts

format:  ## Auto-format code
	ruff format src tests scripts

type-check:  ## Run type checking
	mypy src

clean:  ## Remove build artifacts
	rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/ docs/_build/ .pytest_cache/

docs:  ## Build documentation
	cd docs && sphinx-build -b html . _build

ci: test lint type-check docs  ## Run full CI pipeline

publish-test: clean  ## Publish to TestPyPI
	python -m build
	twine upload --repository testpypi dist/*

publish: clean  ## Publish to PyPI
	python -m build
	twine upload dist/*
