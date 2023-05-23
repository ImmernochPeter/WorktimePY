"""workday"""

import datetime
from typing import Optional


class Workday:
    """Model for workday"""

    def __init__(self, csv_string: Optional[str] = None) -> None:
        self.date: Optional[datetime.date] = None
        # pylint:disable=no-member
        self.starttime: Optional[datetime._Time] = None
        self.endtime: Optional[datetime._Time] = None
        self.breaktime: Optional[int] = None
        self.note: str = ""
        if not csv_string:
            return
        values = csv_string.split(";")
        if values[0] is not None and values[0] != "None":
            self.date = datetime.datetime.strptime(
                values[0], "%Y-%m-%d"
            ).date()
        if values[1] is not None and values[1] != "None":
            self.starttime = datetime.datetime.strptime(
                values[1], "%H:%M:%S"
            ).time()
        if values[2] is not None and values[2] != "None":
            self.endtime = datetime.datetime.strptime(
                values[2], "%H:%M:%S"
            ).time()
        if values[3] is not None and values[3] != "None":
            self.breaktime = int(values[3])
        self.note = values[4]

    def set_date_today(self) -> None:
        """sets date to today"""
        self.date = datetime.date.today()

    def set_start_now(self) -> None:
        """sets startpoint to now"""
        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")
        self.starttime = datetime.datetime.strptime(current, "%H:%M:%S").time()

    def set_end_now(self) -> None:
        """sets startpoint to now"""
        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")
        self.endtime = datetime.datetime.strptime(current, "%H:%M:%S").time()

    def get_today_as_str(self) -> str:
        """gets current day as str"""
        result = ""
        result += str(self.date)
        result += ";"
        result += str(self.starttime)
        result += ";"
        result += str(self.endtime)
        result += ";"
        result += str(self.breaktime)
        result += ";"
        result += self.note
        return result
