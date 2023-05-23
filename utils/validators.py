"""validators"""

import datetime
from typing import Optional


def validate_number() -> int:
    """
    validates if inpt is a number
    returns the number or -1 if input isnt a number
    """

    incoming = input()
    num = -1
    try:
        num = int(incoming)
    except ValueError:
        return -1
    return num


def validate_date() -> Optional[datetime.date]:
    """validates if input is a date"""
    incoming = input()
    try:
        return datetime.datetime.strptime(incoming, "%Y-%m-%d").date()
    except ValueError:
        return None


def validate_time() -> Optional[datetime.time]:
    """validates if input is a time"""
    incoming = input()
    check_format = incoming.split(":")
    if len(check_format) == 2:
        incoming += ":00"
    try:
        return datetime.datetime.strptime(incoming, "%H:%M:%S").time()
    except ValueError:
        return None


def validate_time_minutes() -> Optional[int]:
    """validates if input is int over 0"""
    incoming = input()
    try:
        num = int(incoming)
        if num >= 0:
            return num
    except ValueError:
        return None
    return None


def validate_string() -> Optional[str]:
    """validates string"""
    incoming = input()
    return incoming


def validate_yes() -> Optional[str]:
    incoming = input()
    return incoming
