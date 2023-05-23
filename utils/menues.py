"""menues"""

import os

from models.workday import Workday


def any_key_to_go_on() -> None:
    """any key to go on"""
    print("Press any key to go on")
    _ = input()


def start_menue(os_name: str) -> None:
    """prints the start menue"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("--- Time management ---")
    print("=================================")
    print("[1] Add arrival time (today)")
    print("[2] Add break time (today)")
    print("[3] Add end time (today)")
    print("[4] Add note (today)")
    print("[5] Show all times")
    print("[6] Add arrival time (individual)")
    print("[7] Add end time (individual)")
    print("[8] Add full day")
    print("[9] Leave")
    print("=================================")


def show_all_times(os_name: str, workdays: list[Workday]) -> None:
    """show all workdays"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    pos = 0
    for elem in workdays:
        print(
            f"[{pos}] DATE: {elem.date}  FROM: {elem.starttime}  "
            f"TO: {elem.endtime}  BREAK: {elem.breaktime} minutes  "
            f"NOTE: {elem.note}"
        )
        pos += 1


def ask_for_date(os_name: str) -> None:
    """asks for date"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("What day do you want ot add? [yyyy-mm-dd]: ")


def ask_for_arrival_time(os_name: str) -> None:
    """asks for arrival time"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("What time do you arrived? [hh:mm]/[hh:mm:ss]: ")


def ask_for_end_time(os_name: str) -> None:
    """asks for end time"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("What time do you finished your work? [hh:mm]/[hh:mm:ss]: ")


def ask_for_break_time(os_name: str) -> None:
    """ask for break time"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("How long was your break? [full minutes]")


def ask_for_notes(os_name: str) -> None:
    """ask for notes"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("Notes? [text]")


def older_version_in_file(os_name: str, older_version: str) -> None:
    """asks to override"""
    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
    print("ERROR: There is already a line for this day in the file:")
    print(older_version)
    print(
        "To override the older version wirte [y],"
        "to keep the older version write [n]"
    )
