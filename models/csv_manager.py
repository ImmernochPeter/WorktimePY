"""CSV manager"""
from pathlib import Path
from typing import Optional


class CSVManager:
    """Manager for CSV"""

    def __init__(self, tpath: Path) -> None:
        self.path = tpath

    def override_to_file(self, csv_list: list[str]) -> int:
        """
        writes lines to file
        """
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                for elem in csv_list:
                    file.write(elem + "\n")
        # pylint:disable=broad-exception-caught
        except Exception:
            return -1
        return 0

    def write_to_file(self, csv_list: list[str]) -> int:
        """
        writes lines to file
        """
        try:
            with open(self.path, "a", encoding="utf-8") as file:
                for elem in csv_list:
                    file.write(elem + "\n")
        # pylint:disable=broad-exception-caught
        except Exception:
            return -1
        return 0

    def read_from_file(self) -> Optional[list[str]]:
        """
        reads lines from file
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if lines[-1] == "\n":
                    lines = lines[:-1]
                return lines
        # pylint:disable=broad-exception-caught
        except Exception:
            return None
