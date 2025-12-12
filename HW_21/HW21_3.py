"""
Task 3 (Optional): Pytest fixtures with context manager

What is inside:
1) FileCM context manager (from Task 1)
2) Function that works with a file object: analyze_text(file_obj)
3) Pytest tests + fixture that uses FileCM to provide a file object

Run:
    pytest -q task3_pytest_fixture.py
"""

from __future__ import annotations

import os
import logging
from typing import Optional, TextIO, Any

import pytest


class FileCM:
    """
    A context manager wrapper around Python's built-in open() with counter and logging.
    """

    open_count: int = 0
    active_count: int = 0

    def __init__(
        self,
        file_path: str,
        mode: str = "r",
        encoding: Optional[str] = None,
        newline: Optional[str] = None,
        suppress_exceptions: bool = False,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding
        self.newline = newline
        self.suppress_exceptions = suppress_exceptions
        self.logger = logger or logging.getLogger(__name__)
        self._file: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        self._file = open(
            self.file_path,
            self.mode,
            encoding=self.encoding,
            newline=self.newline,
        )
        FileCM.open_count += 1
        FileCM.active_count += 1
        self.logger.info("OPEN path=%r mode=%r", self.file_path, self.mode)
        return self._file

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_value: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> bool:
        if exc_type is not None:
            self.logger.exception(
                "EXCEPTION inside context: %s: %s",
                exc_type.__name__,
                exc_value,
            )

        try:
            if self._file is not None and not self._file.closed:
                self._file.close()
                self.logger.info("CLOSE path=%r", self.file_path)
        finally:
            if FileCM.active_count > 0:
                FileCM.active_count -= 1

        if exc_type is not None and self.suppress_exceptions:
            return True
        return False


def analyze_text(file_obj: TextIO) -> dict[str, int]:
    """
    Analyze text data from an already opened file object.

    Logic (simple but useful):
    - Count total lines
    - Count total words
    - Count total non-space characters

    Args:
        file_obj: An opened text file object.

    Returns:
        Dictionary with counts: {"lines": X, "words": Y, "chars": Z}
    """
    # Read everything from the current file position
    text = file_obj.read()

    # Basic normalization: treat any whitespace as separators for words
    lines = 0 if text == "" else text.count("\n") + 1
    words = len(text.split())
    chars = sum(1 for ch in text if not ch.isspace())

    return {"lines": lines, "words": words, "chars": chars}



# Pytest fixture


@pytest.fixture
def file_obj(tmp_path) -> TextIO:
    """
    Create a temp file with known content and return an OPEN file object.

    Uses FileCM (custom context manager) to open the file.
    The fixture yields the file object so tests can pass it into analyze_text().

    After the test finishes, the context manager closes the file automatically.
    """
    # Arrange: create a file with predictable content
    path = tmp_path / "sample.txt"
    content = "Hello world\nThis is pytest\n"
    path.write_text(content, encoding="utf-8")

    cm = FileCM(str(path), mode="r", encoding="utf-8")

    # Yield an OPEN file object; after yield, __exit__ will run and close the file
    with cm as f:
        yield f



# Pytest tests


def test_analyze_text_counts(file_obj: TextIO) -> None:
    """Positive: analyze_text returns correct counts for known content."""
    result = analyze_text(file_obj)

    # "Hello world\nThis is pytest\n"
    # Lines: 2 logical lines (because trailing newline still means there are 2 lines of text)
    # Words: Hello(1) world(2) This(3) is(4) pytest(5) => 5
    # Non-space chars: count letters only (no spaces/newlines)
    assert result["lines"] == 2
    assert result["words"] == 5
    assert result["chars"] == len("HelloworldThisispytest")


def test_analyze_text_empty_file(tmp_path) -> None:
    """Edge case: empty file should return zeros."""
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")

    with FileCM(str(path), mode="r", encoding="utf-8") as f:
        result = analyze_text(f)

    assert result == {"lines": 0, "words": 0, "chars": 0}


def test_fixture_uses_context_manager_counters(tmp_path) -> None:
    """
    Check that FileCM counters change correctly in a real pytest-style usage.
    """
    FileCM.open_count = 0
    FileCM.active_count = 0

    path = tmp_path / "x.txt"
    path.write_text("a b c", encoding="utf-8")

    cm = FileCM(str(path), mode="r", encoding="utf-8")

    assert FileCM.open_count == 0
    assert FileCM.active_count == 0

    with cm as f:
        _ = analyze_text(f)
        assert FileCM.open_count == 1
        assert FileCM.active_count == 1

    assert FileCM.active_count == 0