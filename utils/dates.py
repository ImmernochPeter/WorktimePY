"""dates"""

import datetime
from typing import Optional

from models.workday import Workday


def check_if_date_is_in_file(
    date: datetime.date, workdays: Optional[list[Workday]]
) -> Optional[Workday]:
    """checks if date is already in file"""
    if not workdays:
        return None
    for elem in workdays:
        if elem.date == date:
            return elem
    return None


def check_if_current_date_is_in_file(
    workdays: Optional[list[Workday]],
) -> Optional[Workday]:
    """checks if the current day is already in the file"""
    if not workdays:
        return None
    today = datetime.date.today()
    for elem in workdays:
        if elem.date == today:
            return elem
    return None


def convert_csv_list_to_workday_list(
    csv_list: Optional[list[str]],
) -> Optional[list[Workday]]:
    """converts a list full of csv-strings to a list ful of workdays"""
    if not csv_list:
        return None
    if len(csv_list) == 0:
        return None
    result: list[Workday] = []
    for elem in csv_list:
        result.append(Workday(elem))
    return result


def convert_workday_list_to_csv_list(workdays: list[Workday]) -> list[str]:
    """Converts a list of workdays to a csv list"""
    result: list[str] = []
    for elem in workdays:
        result.append(elem.get_today_as_str())
    return result
