"""ways"""

import datetime

from models.csv_manager import CSVManager
from models.settings import Settings
from models.workday import Workday
from utils.dates import (
    check_if_current_date_is_in_file,
    check_if_date_is_in_file,
    convert_csv_list_to_workday_list,
    convert_workday_list_to_csv_list,
)
from utils.menues import (
    ask_for_arrival_time,
    ask_for_break_time,
    ask_for_date,
    ask_for_end_time,
    ask_for_notes,
    older_version_in_file,
)
from utils.messages import error_message, succes_message
from utils.validators import (
    validate_date,
    validate_string,
    validate_time,
    validate_time_minutes,
    validate_yes,
)


def way_starttime_now(manager: CSVManager, settings: Settings) -> bool:
    """starttime now"""
    workdays = convert_csv_list_to_workday_list(manager.read_from_file())
    today = check_if_current_date_is_in_file(workdays)
    if today and today.starttime:
        error_message("Starttime for today was already tracked!", settings)
        return True
    cur_day = Workday()
    cur_day.set_date_today()
    cur_day.set_start_now()
    status = manager.write_to_file([cur_day.get_today_as_str()])
    if status == 0:
        succes_message("Starttime added!", settings)
    return True


def way_endtime_now(manager: CSVManager, settings: Settings) -> bool:
    """endtime now"""
    workdays = convert_csv_list_to_workday_list(manager.read_from_file())
    today = check_if_current_date_is_in_file(workdays)
    if today and today.endtime:
        error_message("Endtime for today was already tracked!", settings)
        return True
    if today is None:
        cur_day = Workday()
        cur_day.set_date_today()
        cur_day.set_end_now()
        status = manager.write_to_file([cur_day.get_today_as_str()])
        if status == 0:
            succes_message("Endtime added!", settings)
        return True
    if not workdays:
        return True
    index = workdays.index(today)
    workdays[index].set_end_now()
    status = manager.override_to_file(
        convert_workday_list_to_csv_list(workdays)
    )
    if status == 0:
        succes_message("Endtime added!", settings)
    return True


def way_break_today(os_name: str, settings: Settings) -> bool:
    """break today"""


def _get_date(os_name: str, settings: Settings) -> datetime.date:
    """get date"""
    while True:
        ask_for_date(os_name)
        date = validate_date()
        if date:
            return date
        error_message("Invalid date! [yyyy-mm-dd]", settings)


def _get_arrival_time(os_name: str, settings: Settings) -> datetime.time:
    """get arrival time"""
    while True:
        ask_for_arrival_time(os_name)
        arv_time = validate_time()
        if arv_time:
            return arv_time
        error_message("Invalid time! [hh:mm]/[hh:mm:ss]", settings)


def _get_end_time(os_name: str, settings: Settings) -> datetime.time:
    """get end time"""
    while True:
        ask_for_end_time(os_name)
        end_time = validate_time()
        if end_time:
            return end_time
        error_message("Invalid time! [hh:mm]/[hh:mm:ss]", settings)


def _get_break_time(os_name: str, settings: Settings) -> int:
    """get break time"""
    while True:
        ask_for_break_time(os_name)
        break_time = validate_time_minutes()
        if break_time:
            return break_time
        error_message("Invalid minutes! [full minutes]", settings)


def _get_notes(os_name: str, settings: Settings) -> str:
    """get_notes"""
    while True:
        ask_for_notes(os_name)
        notes = validate_string()
        if notes is not None:
            return notes
        error_message("Something went wrong!", settings)


def way_full_day(
    manager: CSVManager,
    settings: Settings,
    os_name: str,
) -> bool:
    """full day"""
    date = _get_date(os_name, settings)
    arv_time = _get_arrival_time(os_name, settings)
    end_time = _get_end_time(os_name, settings)
    break_time = _get_break_time(os_name, settings)
    notes = _get_notes(os_name, settings)
    workday = Workday()
    workday.date = date
    workday.starttime = arv_time
    workday.endtime = end_time
    workday.breaktime = break_time
    workday.note = notes
    workdays = convert_csv_list_to_workday_list(manager.read_from_file())
    day = check_if_date_is_in_file(workday.date, workdays)
    if day is None:
        manager.write_to_file(convert_workday_list_to_csv_list([workday]))
        succes_message("Added day tto the file!", settings)
        return True
    old_version = convert_workday_list_to_csv_list([day])[0]
    older_version_in_file(os_name, old_version)
    des = validate_yes()
    assert isinstance(workdays, list)
    if des == "y":
        index = workdays.index(day)
        workdays[index] = workday
        manager.override_to_file(convert_workday_list_to_csv_list(workdays))
    return True
