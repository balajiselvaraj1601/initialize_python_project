"""Tests for main module."""

import pytest
from {{PROJECT_NAME}}.main import hello_world


def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"


def test_hello_world_not_empty():
    """Test that hello_world returns a non-empty string."""
    result = hello_world()
    assert isinstance(result, str)
    assert len(result) > 0
