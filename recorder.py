import os
import signal
import subprocess
from datetime import datetime

from config import find_scrcpy, find_adb


class Recorder:
    def __init__(self):
        self._process: subprocess.Popen | None = None
        self._mirror_process: subprocess.Popen | None = None
        self._output_path: str | None = None
        self._start_time: datetime | None = None

    @property
    def is_recording(self) -> bool:
        return self._process is not None and self._process.poll() is None

    @property
    def is_mirroring(self) -> bool:
        return self._mirror_process is not None and self._mirror_process.poll() is None

    @property
    def output_path(self) -> str | None:
        return self._output_path

    @property
    def start_time(self) -> datetime | None:
        return self._start_time

    def get_devices(self) -> list[tuple[str, str]]:
        """Get list of connected devices via adb devices.

        Returns list of (serial, display_name) tuples.
        """
        adb = find_adb()
        if adb is None:
            return []
        try:
            result = subprocess.run(
                [adb, "devices", "-l"],
                capture_output=True, text=True, timeout=5,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            devices = []
            for line in result.stdout.strip().splitlines()[1:]:
                if "device" in line and "offline" not in line:
                    parts = line.split()
                    serial = parts[0]
                    model = serial  # fallback
                    for part in parts:
                        if part.startswith("model:"):
                            model = part.split(":", 1)[1]
                            break
                    devices.append((serial, model))
            return devices
        except Exception:
            return []

    def mirror(self, serial: str | None = None,
              show_touches: bool = False) -> None:
        """Start mirroring only (no recording)."""
        if self.is_mirroring:
            return  # already mirroring

        scrcpy_path = find_scrcpy()
        if scrcpy_path is None:
            raise RuntimeError(
                "scrcpy.exe not found. Place it next to the app or add to PATH."
            )

        cmd = [scrcpy_path]
        if serial:
            cmd += ["-s", serial]
        if show_touches:
            cmd.append("--show-touches")

        self._mirror_process = subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        )

    def stop_mirror(self) -> None:
        """Stop mirroring."""
        if not self.is_mirroring:
            return
        try:
            self._mirror_process.send_signal(signal.CTRL_BREAK_EVENT)
        except OSError:
            self._mirror_process.terminate()
        try:
            self._mirror_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self._mirror_process.kill()
            self._mirror_process.wait()
        self._mirror_process = None

    def start(self, output_dir: str, fmt: str = "mkv",
              max_size: str = "Original", bitrate: str = "4M",
              fps: str = "60", audio: bool = True,
              orientation: str = "Auto",
              show_touches: bool = False,
              serial: str | None = None) -> str:
        """Start recording with given settings. Returns the output file path."""
        if self.is_recording:
            raise RuntimeError("Already recording")

        scrcpy_path = find_scrcpy()
        if scrcpy_path is None:
            raise RuntimeError(
                "scrcpy.exe not found. Place it next to the app or add to PATH."
            )

        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"record_{timestamp}.{fmt}"
        self._output_path = os.path.join(output_dir, filename)

        cmd = [scrcpy_path, "--record", self._output_path]

        if serial:
            cmd += ["-s", serial]

        if max_size != "Original":
            cmd += ["--max-size", max_size]

        cmd += ["--video-bit-rate", bitrate]
        cmd += ["--max-fps", fps]

        if not audio:
            cmd.append("--no-audio")

        if orientation == "Portrait":
            cmd += ["--lock-video-orientation=0"]
        elif orientation == "Landscape":
            cmd += ["--lock-video-orientation=1"]

        if show_touches:
            cmd.append("--show-touches")

        self._process = subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        )
        self._start_time = datetime.now()
        return self._output_path

    def stop(self) -> str | None:
        """Stop recording. Returns path to the saved file."""
        if not self.is_recording:
            return None

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
        self._start_time = None
        return self._output_path
