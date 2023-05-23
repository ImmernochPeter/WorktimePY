"""messages"""

from models.settings import Settings

from .menues import any_key_to_go_on


def succes_message(msg: str, settings: Settings) -> None:
    """success message"""
    if not settings.succes_msg:
        return
    print(f"Succes: {msg}")
    any_key_to_go_on()


def error_message(msg: str, settigs: Settings) -> None:
    """error message"""
    if not settigs.error_msg:
        return
    print(f"Error: {msg}")
    any_key_to_go_on()
