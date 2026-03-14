import ctypes
import os
import signal
import subprocess
from datetime import datetime

from config import find_scrcpy


class Recorder:
    def __init__(self):
        self._process: subprocess.Popen | None = None
        self._output_path: str | None = None

    @property
    def is_recording(self) -> bool:
        return self._process is not None and self._process.poll() is None

    @property
    def output_path(self) -> str | None:
        return self._output_path

    def start(self, output_dir: str) -> str:
        """Start recording. Returns the output file path.

        Raises RuntimeError if scrcpy is not found or already recording.
        """
        if self.is_recording:
            raise RuntimeError("Already recording")

        scrcpy_path = find_scrcpy()
        if scrcpy_path is None:
            raise RuntimeError(
                "scrcpy.exe not found. Place it next to the app or add to PATH."
            )

        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"record_{timestamp}.mkv"
        self._output_path = os.path.join(output_dir, filename)

        self._process = subprocess.Popen(
            [scrcpy_path, "--record", self._output_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        )
        return self._output_path

    def stop(self) -> str | None:
        """Stop recording. Returns path to the saved file."""
        if not self.is_recording:
            return None

        # Send CTRL_BREAK_EVENT so scrcpy can finalize the MP4 file
        try:
            self._process.send_signal(signal.CTRL_BREAK_EVENT)
        except OSError:
            self._process.terminate()
        try:
            self._process.wait(timeout=15)
        except subprocess.TimeoutExpired:
            self._process.kill()
            self._process.wait()

        self._process = None
        return self._output_path
