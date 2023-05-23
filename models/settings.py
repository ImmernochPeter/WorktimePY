"""settings"""
import json
from typing import Any


# pylint:disable=too-few-public-methods
class Settings:
    """Settings"""

    def _read_seetings_from_json(self) -> None:
        """reads the settings from json file"""
        with open("options.json", "r", encoding="utf-8") as file:
            data: dict[str, dict[str, Any]] = json.load(file)
            settings = data["settings"]
            self.succes_msg = settings["success-messages"]
            self.error_msg = settings["error-messages"]

    def __init__(self) -> None:
        self.succes_msg = True
        self.error_msg = True
        self._read_seetings_from_json()
