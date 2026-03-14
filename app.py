import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk

from config import DEFAULT_RECORD_DIR, find_scrcpy
from recorder import Recorder


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("scrcpy GUI")
        self.geometry("420x220")
        self.resizable(False, False)

        self._recorder = Recorder()
        self._output_dir = DEFAULT_RECORD_DIR

        self._build_ui()
        self._update_scrcpy_status()

    def _build_ui(self):
        # --- Output folder row ---
        folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        folder_frame.pack(fill="x", padx=16, pady=(16, 8))

        ctk.CTkLabel(folder_frame, text="Save to:").pack(side="left")

        self._folder_var = tk.StringVar(value=self._output_dir)
        self._folder_entry = ctk.CTkEntry(
            folder_frame, textvariable=self._folder_var, width=240
        )
        self._folder_entry.pack(side="left", padx=8)

        ctk.CTkButton(
            folder_frame, text="Browse", width=70, command=self._browse_folder
        ).pack(side="left")

        # --- Control buttons ---
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", padx=16, pady=8)

        self._start_btn = ctk.CTkButton(
            btn_frame,
            text="Start Recording",
            fg_color="#2ecc71",
            hover_color="#27ae60",
            command=self._on_start,
        )
        self._start_btn.pack(side="left", expand=True, fill="x", padx=(0, 8))

        self._stop_btn = ctk.CTkButton(
            btn_frame,
            text="Stop Recording",
            fg_color="#e74c3c",
            hover_color="#c0392b",
            state="disabled",
            command=self._on_stop,
        )
        self._stop_btn.pack(side="left", expand=True, fill="x")

        # --- Status bar ---
        self._status_var = tk.StringVar(value="Idle")
        self._status_label = ctk.CTkLabel(
            self,
            textvariable=self._status_var,
            anchor="w",
            font=ctk.CTkFont(size=13),
        )
        self._status_label.pack(fill="x", padx=16, pady=(8, 16))

    def _update_scrcpy_status(self):
        path = find_scrcpy()
        if path is None:
            self._status_var.set("⚠ scrcpy.exe not found")
            self._start_btn.configure(state="disabled")

    def _browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self._output_dir)
        if folder:
            self._output_dir = folder
            self._folder_var.set(folder)

    def _on_start(self):
        self._output_dir = self._folder_var.get()
        try:
            path = self._recorder.start(self._output_dir)
        except RuntimeError as e:
            self._status_var.set(f"Error: {e}")
            return

        self._status_var.set(f"Recording... → {path}")
        self._start_btn.configure(state="disabled")
        self._stop_btn.configure(state="normal")

    def _on_stop(self):
        saved = self._recorder.stop()
        if saved:
            self._status_var.set(f"Saved to {saved}")
        else:
            self._status_var.set("Idle")

        self._start_btn.configure(state="normal")
        self._stop_btn.configure(state="disabled")

    def destroy(self):
        if self._recorder.is_recording:
            self._recorder.stop()
        super().destroy()
