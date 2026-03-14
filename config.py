import os
import shutil
import sys


def get_app_dir() -> str:
    """Directory where the executable (or main.py) lives."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def find_scrcpy() -> str | None:
    """Find scrcpy.exe: first next to the app, then in PATH."""
    local = os.path.join(get_app_dir(), "scrcpy.exe")
    if os.path.isfile(local):
        return local
    return shutil.which("scrcpy")


DEFAULT_RECORD_DIR = os.path.join(os.path.expanduser("~"), "Videos")
