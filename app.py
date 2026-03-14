import tkinter as tk
from datetime import datetime
from tkinter import filedialog

import customtkinter as ctk

from config import (
    DEFAULT_RECORD_DIR, RESOLUTIONS, BITRATES, FPS_OPTIONS, FORMATS,
    ORIENTATIONS, find_scrcpy,
)
from recorder import Recorder


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("scrcpy GUI v2.0")
        self.geometry("360x720")
        self.resizable(False, False)

        self.recorder = Recorder()
        self._timer_id = None

        self._build_ui()
        self._refresh_device()

    # ── UI ─────────────────────────────────────────────

    def _build_ui(self):
        pad = {"padx": 12, "pady": (6, 0)}

        # ── Device section ──
        sec_device = ctk.CTkFrame(self, fg_color="transparent")
        sec_device.pack(fill="x", **pad)

        ctk.CTkLabel(sec_device, text="Device",
                     font=ctk.CTkFont(size=14, weight="bold")).pack(
            side="left")

        self.btn_refresh = ctk.CTkButton(
            sec_device, text="Refresh", width=70, height=28,
            command=self._refresh_device)
        self.btn_refresh.pack(side="right")

        self.lbl_device = ctk.CTkLabel(self, text="Searching...",
                                       font=ctk.CTkFont(size=13),
                                       text_color="#aaaaaa")
        self.lbl_device.pack(anchor="w", padx=12, pady=(2, 4))

        # ── Mirror button ──
        frm_mirror = ctk.CTkFrame(self, fg_color="transparent")
        frm_mirror.pack(fill="x", padx=12, pady=(4, 0))

        self.btn_mirror = ctk.CTkButton(
            frm_mirror, text="Mirror Screen", height=34,
            fg_color="#3498db", hover_color="#2980b9",
            command=self._on_mirror)
        self.btn_mirror.pack(fill="x")

        self._add_separator()

        # ── Controls section ──
        frm_controls = ctk.CTkFrame(self, fg_color="transparent")
        frm_controls.pack(fill="x", **pad)

        self.btn_record = ctk.CTkButton(
            frm_controls, text="Record", width=140, height=38,
            fg_color="#e74c3c", hover_color="#c0392b",
            command=self._on_start)
        self.btn_record.pack(side="left", padx=(0, 8))

        self.btn_stop = ctk.CTkButton(
            frm_controls, text="Stop", width=140, height=38,
            fg_color="#555555", hover_color="#444444",
            state="disabled", command=self._on_stop)
        self.btn_stop.pack(side="left")

        self.lbl_timer = ctk.CTkLabel(self, text="",
                                      font=ctk.CTkFont(size=13),
                                      text_color="#e74c3c")
        self.lbl_timer.pack(anchor="w", padx=12, pady=(2, 4))

        self._add_separator()

        # ── Settings section ──
        ctk.CTkLabel(self, text="Settings",
                     font=ctk.CTkFont(size=14, weight="bold")).pack(
            anchor="w", padx=12, pady=(8, 4))

        # Save to
        frm_save = ctk.CTkFrame(self, fg_color="transparent")
        frm_save.pack(fill="x", padx=12, pady=2)
        ctk.CTkLabel(frm_save, text="Save to:", width=90,
                     anchor="w").pack(side="left")
        self.var_dir = tk.StringVar(value=DEFAULT_RECORD_DIR)
        ctk.CTkEntry(frm_save, textvariable=self.var_dir,
                     width=170).pack(side="left", padx=(4, 4))
        ctk.CTkButton(frm_save, text="...", width=32, height=28,
                      command=self._browse).pack(side="left")

        # Format
        self.var_format = tk.StringVar(value=FORMATS[0])
        self._add_combo_row("Format:", self.var_format, FORMATS)

        # Resolution
        self.var_resolution = tk.StringVar(value=RESOLUTIONS[0])
        self._add_combo_row("Resolution:", self.var_resolution, RESOLUTIONS)

        # Bitrate
        self.var_bitrate = tk.StringVar(value=BITRATES[1])
        self._add_combo_row("Bitrate:", self.var_bitrate, BITRATES)

        # FPS
        self.var_fps = tk.StringVar(value=FPS_OPTIONS[0])
        self._add_combo_row("FPS:", self.var_fps, FPS_OPTIONS)

        # Orientation
        self.var_orientation = tk.StringVar(value=ORIENTATIONS[0])
        self._add_combo_row("Orientation:", self.var_orientation, ORIENTATIONS)

        # Audio switch
        frm_audio = ctk.CTkFrame(self, fg_color="transparent")
        frm_audio.pack(fill="x", padx=12, pady=2)
        ctk.CTkLabel(frm_audio, text="Audio:", width=90,
                     anchor="w").pack(side="left")
        self.var_audio = tk.BooleanVar(value=True)
        ctk.CTkSwitch(frm_audio, text="", variable=self.var_audio,
                      width=40).pack(side="left", padx=4)

        # Show touches switch
        frm_touches = ctk.CTkFrame(self, fg_color="transparent")
        frm_touches.pack(fill="x", padx=12, pady=2)
        ctk.CTkLabel(frm_touches, text="Show touches:", width=90,
                     anchor="w").pack(side="left")
        self.var_touches = tk.BooleanVar(value=False)
        ctk.CTkSwitch(frm_touches, text="", variable=self.var_touches,
                      width=40).pack(side="left", padx=4)

        self._add_separator()

        # ── Status section ──
        ctk.CTkLabel(self, text="Status",
                     font=ctk.CTkFont(size=14, weight="bold")).pack(
            anchor="w", padx=12, pady=(8, 2))

        self.lbl_status = ctk.CTkLabel(
            self, text="Idle", font=ctk.CTkFont(size=13),
            text_color="#2ecc71")
        self.lbl_status.pack(anchor="w", padx=12, pady=(0, 2))

        self.lbl_file = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=11),
            text_color="#888888", wraplength=330)
        self.lbl_file.pack(anchor="w", padx=12, pady=(0, 8))

    # ── Helpers ────────────────────────────────────────

    def _add_separator(self):
        sep = ctk.CTkFrame(self, height=1, fg_color="#333333")
        sep.pack(fill="x", padx=12, pady=6)

    def _add_combo_row(self, label: str, var: tk.StringVar, values: list):
        frm = ctk.CTkFrame(self, fg_color="transparent")
        frm.pack(fill="x", padx=12, pady=2)
        ctk.CTkLabel(frm, text=label, width=90, anchor="w").pack(side="left")
        ctk.CTkComboBox(frm, variable=var, values=values,
                        width=160, height=28, state="readonly").pack(
            side="left", padx=4)

    def _browse(self):
        d = filedialog.askdirectory(initialdir=self.var_dir.get())
        if d:
            self.var_dir.set(d)

    def _refresh_device(self):
        self.lbl_device.configure(text="Searching...")
        self.update_idletasks()
        device = self.recorder.get_device()
        if device:
            self.lbl_device.configure(text=f"Connected: {device}",
                                      text_color="#2ecc71")
        else:
            self.lbl_device.configure(text="No device found",
                                      text_color="#e74c3c")

    # ── Mirror ─────────────────────────────────────────

    def _on_mirror(self):
        if self.recorder.is_mirroring:
            self.recorder.stop_mirror()
            self.btn_mirror.configure(text="Mirror Screen",
                                      fg_color="#3498db",
                                      hover_color="#2980b9")
            self.lbl_status.configure(text="Mirror stopped",
                                      text_color="#aaaaaa")
            return

        try:
            self.recorder.mirror(show_touches=self.var_touches.get())
        except RuntimeError as e:
            self.lbl_status.configure(text=str(e), text_color="#e74c3c")
            return

        self.btn_mirror.configure(text="Stop Mirror",
                                  fg_color="#555555",
                                  hover_color="#444444")
        self.lbl_status.configure(text="Mirroring...", text_color="#3498db")
        self._poll_mirror()

    def _poll_mirror(self):
        """Check if mirror process is still alive."""
        if not self.recorder.is_mirroring:
            self.btn_mirror.configure(text="Mirror Screen",
                                      fg_color="#3498db",
                                      hover_color="#2980b9")
            self.lbl_status.configure(text="Mirror stopped",
                                      text_color="#aaaaaa")
            self.recorder._mirror_process = None
            return
        self.after(1000, self._poll_mirror)

    # ── Recording ─────────────────────────────────────

    def _on_start(self):
        # Stop mirror if running — Record opens its own scrcpy window
        if self.recorder.is_mirroring:
            self.recorder.stop_mirror()
            self.btn_mirror.configure(text="Mirror Screen",
                                      fg_color="#3498db",
                                      hover_color="#2980b9")

        scrcpy = find_scrcpy()
        if not scrcpy:
            self.lbl_status.configure(text="scrcpy.exe not found",
                                      text_color="#e74c3c")
            return

        try:
            path = self.recorder.start(
                output_dir=self.var_dir.get(),
                fmt=self.var_format.get(),
                max_size=self.var_resolution.get(),
                bitrate=self.var_bitrate.get(),
                fps=self.var_fps.get(),
                audio=self.var_audio.get(),
                orientation=self.var_orientation.get(),
                show_touches=self.var_touches.get(),
            )
        except RuntimeError as e:
            self.lbl_status.configure(text=str(e), text_color="#e74c3c")
            return

        self.btn_record.configure(state="disabled")
        self.btn_stop.configure(state="normal", fg_color="#e74c3c",
                                hover_color="#c0392b")
        self.lbl_status.configure(text="Recording...", text_color="#e74c3c")
        self.lbl_file.configure(text=path)
        self._update_timer()

    def _on_stop(self):
        path = self.recorder.stop()
        if self._timer_id:
            self.after_cancel(self._timer_id)
            self._timer_id = None

        self.btn_record.configure(state="normal")
        self.btn_stop.configure(state="disabled", fg_color="#555555",
                                hover_color="#444444")
        self.lbl_timer.configure(text="")
        self.lbl_status.configure(text="Saved", text_color="#2ecc71")
        self.lbl_file.configure(text=path or "")

    def _update_timer(self):
        # Check if scrcpy process died (user closed the window)
        if not self.recorder.is_recording:
            self._on_process_died()
            return

        if self.recorder.start_time:
            elapsed = datetime.now() - self.recorder.start_time
            mins, secs = divmod(int(elapsed.total_seconds()), 60)
            hrs, mins = divmod(mins, 60)
            self.lbl_timer.configure(text=f"REC  {hrs:02d}:{mins:02d}:{secs:02d}")
            self._timer_id = self.after(1000, self._update_timer)

    def _on_process_died(self):
        """Handle scrcpy process ending unexpectedly (e.g. user closed window)."""
        self._timer_id = None
        self.recorder._process = None
        self.recorder._start_time = None

        self.btn_record.configure(state="normal")
        self.btn_stop.configure(state="disabled", fg_color="#555555",
                                hover_color="#444444")
        self.lbl_timer.configure(text="")
        path = self.recorder.output_path
        if path:
            self.lbl_status.configure(text="Saved", text_color="#2ecc71")
            self.lbl_file.configure(text=path)
        else:
            self.lbl_status.configure(text="Idle", text_color="#2ecc71")

    def destroy(self):
        if self.recorder.is_recording:
            self.recorder.stop()
        if self.recorder.is_mirroring:
            self.recorder.stop_mirror()
        super().destroy()
