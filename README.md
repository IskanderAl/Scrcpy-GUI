# scrcpy GUI

<p align="center">
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/us.png" height="20"> <b>English</b></a>
  &nbsp;|&nbsp;
  <a href="README_RU.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ru.png" height="20"> Русский</a>
  &nbsp;|&nbsp;
  <a href="README_CN.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/cn.png" height="20"> 中文</a>
  &nbsp;|&nbsp;
  <a href="README_KZ.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/kz.png" height="20"> Қазақша</a>
</p>

A GUI wrapper for [scrcpy](https://github.com/Genymobile/scrcpy) — mirror and record your Android screen with ease.
Built for QA testers.

## Features

- **Mirror Screen** — real-time device mirroring in a separate window
- **Screen Recording** — record with live timer display
- **Device Auto-Detection** — shows connected device model automatically
- **Configurable Settings** — format (MKV/MP4), resolution, bitrate, FPS, orientation, audio, show touches
- **Smart Process Management** — auto-closes mirror when recording starts, detects when scrcpy window is closed

## Installation

### Option 1 — Installer (recommended)

1. Go to [Releases](../../releases/latest)
2. Download `scrcpy-gui-setup-v2.0.0.exe`
3. Run it → select components → install
4. A desktop shortcut will be created

> If you already have scrcpy or adb installed, you can uncheck them during setup.

### Option 2 — ZIP archive

1. Download `scrcpy-gui-v2.0.0-win64.zip` from [Releases](../../releases/latest)
2. Extract to any folder
3. Run `scrcpy-gui.exe`

### Option 3 — From source

```bash
pip install customtkinter
python main.py
```

Requires `scrcpy.exe` next to `main.py` or in PATH.

## Requirements

- Windows 10+
- Android device with USB debugging enabled
- USB cable

### How to enable USB debugging

1. **Settings** > **About phone** > Tap **Build number** 7 times
2. **Settings** > **Developer options** > Enable **USB debugging**
3. Connect the phone via USB and allow debugging in the popup

## Usage

1. Connect your device via USB
2. Launch **scrcpy GUI** — the device name appears automatically
3. Click **Mirror Screen** to open a live mirror window
4. Adjust settings: format, resolution, bitrate, FPS, orientation, audio
5. Click **Record** — mirror closes, recording starts with a live timer
6. Click **Stop** — file is saved as `record_YYYY-MM-DD_HH-MM-SS.mkv`

## License

This project uses [scrcpy](https://github.com/Genymobile/scrcpy) (Genymobile / Romain Vimont), distributed under the [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE).

scrcpy GUI is an independent wrapper and does not modify scrcpy.
