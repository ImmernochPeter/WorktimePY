"""run"""

from pathlib import Path

from models.csv_manager import CSVManager
from models.settings import Settings
from navigation.ways import way_endtime_now, way_full_day, way_starttime_now

from .dates import convert_csv_list_to_workday_list
from .menues import any_key_to_go_on, show_all_times, start_menue
from .messages import error_message
from .validators import validate_number

absolute_path = Path.home() / "worktimePY" / "time.csv"

manager = CSVManager(absolute_path)


# pylint:disable=too-many-return-statements, too-many-branches
def run(os_name: str, settings: Settings) -> bool:
    """run"""

    start_menue(os_name)
    way = validate_number()
    if way == -1:
        return True
    if way == 9:
        return False
    if way == 5:
        workdays = convert_csv_list_to_workday_list(manager.read_from_file())
        if not workdays:
            error_message("No times saved!", settings)
            return True
        show_all_times(os_name, workdays)
        any_key_to_go_on()
        return True
    if way == 1:
        return way_starttime_now(manager, settings)
    if way == 3:
        return way_endtime_now(manager, settings)
    if way == 8:
        return way_full_day(manager, settings, os_name)

    return False
