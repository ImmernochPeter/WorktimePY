"""main"""

import platform
import sys

from models.settings import Settings
from utils.run import run

OSNAME: str = platform.system()
SETTINGS = Settings()


def main() -> None:
    """main"""
    runner = True
    while runner:
        runner = run(OSNAME, SETTINGS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
