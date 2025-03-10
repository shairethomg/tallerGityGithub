import logging
import unittest.util

unittest.util._MAX_LENGTH = 100000  # type: ignore[misc]


class DisallowLogsHandler(logging.Handler):
    def __init__(self, level=logging.WARNING):
        super().__init__(level=level)
        self.formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

    def emit(self, record):
        raise AssertionError(f'Unexpected log: {self.format(record)!r}')


logging.lastResort = DisallowLogsHandler()  # type: ignore
