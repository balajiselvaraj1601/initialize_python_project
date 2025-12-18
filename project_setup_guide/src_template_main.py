"""Main module for the application."""

import logging

logger = logging.getLogger(__name__)

def hello_world() -> str:
    """Return a greeting message."""
    return "Hello, World!"


def main() -> None:
    """Main entry point."""
    logger.info(hello_world())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
