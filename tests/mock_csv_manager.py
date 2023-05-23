"""
Mock for CSVManager
"""

from typing import Optional


class CSVMock:
    """Mock for CSVManager"""

    def __init__(self, read: int = 0, write: int = 0, over: int = 0) -> None:
        self.read = read
        self.write = write
        self.over = over

    def override_to_file(self, _csv_list: list[str]) -> int:
        """
        writes lines to file
        """
        return self.over

    def write_to_file(self, _csv_list: list[str]) -> int:
        """
        writes lines to file
        """
        return self.write

    def read_from_file(self) -> Optional[list[str]]:
        """
        reads lines from file
        """
        if self.read == 0:
            return ["a"]
        return None
