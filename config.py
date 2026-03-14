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


def find_adb() -> str | None:
    """Find adb.exe: first next to the app, then in PATH."""
    local = os.path.join(get_app_dir(), "adb.exe")
    if os.path.isfile(local):
        return local
    return shutil.which("adb")


DEFAULT_RECORD_DIR = os.path.join(os.path.expanduser("~"), "Videos")

RESOLUTIONS = ["Original", "1920", "1280", "720"]
BITRATES = ["8M", "4M", "2M"]
FPS_OPTIONS = ["60", "30", "15"]
FORMATS = ["mkv", "mp4"]
ORIENTATIONS = ["Auto", "Portrait", "Landscape"]
