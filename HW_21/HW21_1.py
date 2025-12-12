"""
Task 1: File Context Manager class

Create a custom context manager that behaves like built-in open(),
but adds:
- Counter (how many successful opens happened)
- Logging (open/close and exceptions)

Usage example:
    with FileCM("data.txt", "w", encoding="utf-8") as f:
        f.write("hello")
"""

from __future__ import annotations

import logging
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

    # Total number of successful opens across all instances
    open_count: int = 0

    # Number of contexts currently active (entered but not exited)
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
        # Save parameters similar to built-in open()
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

        # If True, __exit__ will swallow exceptions (return True)
        self.suppress_exceptions = suppress_exceptions

        # Use provided logger or a default logger
        self.logger = logger or logging.getLogger(__name__)

        # Will hold the real file object after opening
        self._file: Optional[TextIO] = None

    def __enter__(self) -> TextIO:
        # Open the file using built-in open()
        self._file = open(
            self.file_path,
            self.mode,
            encoding=self.encoding,
            newline=self.newline,
        )

        # Update counters only after successful open()
        FileCM.open_count += 1
        FileCM.active_count += 1

        # Log open
        self.logger.info("OPEN path=%r mode=%r", self.file_path, self.mode)

        # Return the file object so user can work with it
        return self._file

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_value: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> bool:
        """
        Exit the runtime context and handle cleanup.

        Args:
            exc_type: Exception class if an exception occurred, otherwise None.
            exc_value: Exception instance if occurred, otherwise None.
            exc_tb: Traceback if occurred, otherwise None.

        Returns:
            True  -> suppress exception (do not re-raise)
            False -> do not suppress (exception will be re-raised)
        """
        # If an exception happened in the with-block, log it
        if exc_type is not None:
            self.logger.exception(
                "EXCEPTION inside context: %s: %s",
                exc_type.__name__,
                exc_value,
            )

        # Always close the file if it was opened
        try:
            if self._file is not None and not self._file.closed:
                self._file.close()
                self.logger.info("CLOSE path=%r", self.file_path)
        finally:
            # Decrement active count even if closing raised something unexpected
            if FileCM.active_count > 0:
                FileCM.active_count -= 1

        # Suppress exception only if requested AND there was an exception
        if exc_type is not None and self.suppress_exceptions:
            return True

        return False

    @property
    def file(self) -> Optional[TextIO]:
        """Return the underlying file object (or None if not opened yet)."""
        return self._file


if __name__ == "__main__":
    # Basic demo (not tests)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("Before:", FileCM.open_count, FileCM.active_count)

    with FileCM("demo.txt", "w", encoding="utf-8") as f:
        f.write("Hello from FileCM!\n")

    print("After:", FileCM.open_count, FileCM.active_count)