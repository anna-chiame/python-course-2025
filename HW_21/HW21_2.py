"""
Task 2: Writing tests for context manager (unittest)

This file includes:
1) FileCM context manager (Task 1 implementation)
2) A thorough unittest suite for it (Task 2)

Run:
    python task2_tests_context_manager.py
or:
    python -m unittest -v task2_tests_context_manager.py
"""

from __future__ import annotations

import io
import logging
import os
import tempfile
import unittest
from typing import Optional, TextIO, Any


class FileCM:
    """
    A context manager wrapper around Python's built-in open().

    Features:
    - Works like open(): supports file path, mode, encoding, newline.
    - Counter:
        * FileCM.open_count  -> total number of successful opens
        * FileCM.active_count -> number of contexts currently entered
    - Logging:
        * logs OPEN/CLOSE
        * logs exceptions that happen inside the 'with' block
    - __exit__ follows context manager rules:
        * always closes the file if it was opened
        * can suppress exceptions if suppress_exceptions=True
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
            # logger.exception() includes traceback automatically
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
            # Make sure active_count is decremented even if close() fails
            if FileCM.active_count > 0:
                FileCM.active_count -= 1

        if exc_type is not None and self.suppress_exceptions:
            return True

        return False

    @property
    def file(self) -> Optional[TextIO]:
        """Return the underlying file object (or None if not opened yet)."""
        return self._file


class TestFileCM(unittest.TestCase):
    """Unit tests for FileCM context manager."""

    def setUp(self) -> None:
        # Reset class counters so tests are independent
        FileCM.open_count = 0
        FileCM.active_count = 0

        # Create an in-memory log stream for capturing logger output
        self.log_stream = io.StringIO()
        self.logger = logging.getLogger(f"test_logger_{id(self)}")
        self.logger.setLevel(logging.INFO)

        # Clean handlers to avoid duplicates if the test runner reuses loggers
        self.logger.handlers = []

        handler = logging.StreamHandler(self.log_stream)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(levelname)s:%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Prevent logs from propagating to root logger (keeps test output clean)
        self.logger.propagate = False

    def _log_text(self) -> str:
        """Helper to read captured log output."""
        return self.log_stream.getvalue()

    def test_successful_write_and_close(self) -> None:
        """Positive: file exists (created), write works, file closes on exit."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "a.txt")

            cm = FileCM(path, mode="w", encoding="utf-8", logger=self.logger)
            with cm as f:
                f.write("hello")
                self.assertFalse(f.closed)  # open inside context

            # closed after context
            self.assertIsNotNone(cm.file)
            self.assertTrue(cm.file.closed)

            # counters updated
            self.assertEqual(FileCM.open_count, 1)
            self.assertEqual(FileCM.active_count, 0)

            # logging contains OPEN and CLOSE
            logs = self._log_text()
            self.assertIn("OPEN", logs)
            self.assertIn("CLOSE", logs)

    def test_successful_read_existing_file(self) -> None:
        """Positive: file exists, read works."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "b.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("data")

            with FileCM(path, mode="r", encoding="utf-8", logger=self.logger) as f:
                content = f.read()

            self.assertEqual(content, "data")
            self.assertEqual(FileCM.open_count, 1)
            self.assertEqual(FileCM.active_count, 0)

    def test_open_nonexistent_for_read_raises(self) -> None:
        """Negative: opening missing file in 'r' mode should raise FileNotFoundError."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "missing.txt")

            cm = FileCM(path, mode="r", encoding="utf-8", logger=self.logger)

            with self.assertRaises(FileNotFoundError):
                with cm:
                    pass

            # __enter__ failed -> counters should remain 0
            self.assertEqual(FileCM.open_count, 0)
            self.assertEqual(FileCM.active_count, 0)

            # file object was never created
            self.assertIsNone(cm.file)

    def test_exception_inside_context_not_suppressed_by_default(self) -> None:
        """Negative: exception inside context should be re-raised by default."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "c.txt")

            cm = FileCM(path, mode="w", encoding="utf-8", logger=self.logger)

            with self.assertRaises(ValueError):
                with cm as f:
                    f.write("before error")
                    raise ValueError("boom")

            # file must still be closed
            self.assertIsNotNone(cm.file)
            self.assertTrue(cm.file.closed)

            # counters: opened successfully, then exited
            self.assertEqual(FileCM.open_count, 1)
            self.assertEqual(FileCM.active_count, 0)

            # logs should contain EXCEPTION and CLOSE
            logs = self._log_text()
            self.assertIn("EXCEPTION inside context", logs)
            self.assertIn("CLOSE", logs)

    def test_exception_inside_context_can_be_suppressed(self) -> None:
        """Negative but expected behavior: exception is swallowed when suppress_exceptions=True."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "d.txt")

            cm = FileCM(
                path,
                mode="w",
                encoding="utf-8",
                suppress_exceptions=True,
                logger=self.logger,
            )

            # No assertRaises: exception should not escape
            with cm as f:
                f.write("ok")
                raise RuntimeError("should be suppressed")

            # file must still be closed
            self.assertIsNotNone(cm.file)
            self.assertTrue(cm.file.closed)

            # logs contain EXCEPTION and CLOSE
            logs = self._log_text()
            self.assertIn("EXCEPTION inside context", logs)
            self.assertIn("CLOSE", logs)

    def test_active_count_during_context(self) -> None:
        """active_count should increment on enter and decrement on exit."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "e.txt")

            cm = FileCM(path, mode="w", encoding="utf-8", logger=self.logger)
            self.assertEqual(FileCM.active_count, 0)

            with cm as _:
                self.assertEqual(FileCM.active_count, 1)

            self.assertEqual(FileCM.active_count, 0)

    def test_multiple_contexts_increment_open_count(self) -> None:
        """open_count should increase for each successful __enter__."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "f.txt")

            with FileCM(path, mode="w", encoding="utf-8", logger=self.logger) as f:
                f.write("1")
            with FileCM(path, mode="a", encoding="utf-8", logger=self.logger) as f:
                f.write("2")
            with FileCM(path, mode="r", encoding="utf-8", logger=self.logger) as f:
                _ = f.read()

            self.assertEqual(FileCM.open_count, 3)
            self.assertEqual(FileCM.active_count, 0)

    def test_close_is_attempted_even_if_close_raises(self) -> None:
        """
        Negative: simulate a close() failure to ensure active_count still decrements.

        We patch the file object's close method to raise, then check that
        active_count is decremented in the finally block.
        """
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "g.txt")

            cm = FileCM(path, mode="w", encoding="utf-8", logger=self.logger)

            # We expect the close() error to propagate out of __exit__
            with self.assertRaises(RuntimeError):
                with cm as f:
                    f.write("x")

                    original_close = f.close

                    def bad_close() -> None:
                        # Call original close? doesn't matter; raise to simulate failure
                        raise RuntimeError("close failed")

                    # Replace close with a failing version
                    f.close = bad_close  # type: ignore[assignment]

            # Even though close failed, active_count should be decremented to 0
            self.assertEqual(FileCM.active_count, 0)

            # open_count increments because __enter__ succeeded
            self.assertEqual(FileCM.open_count, 1)

    def test_file_property_none_before_enter(self) -> None:
        """Before entering context, cm.file should be None."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "h.txt")
            cm = FileCM(path, mode="w", encoding="utf-8", logger=self.logger)
            self.assertIsNone(cm.file)


if __name__ == "__main__":
    unittest.main(verbosity=2)