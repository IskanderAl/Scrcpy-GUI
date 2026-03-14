[Setup]
AppName=scrcpy GUI
AppVersion=2.0.0
AppPublisher=IskanderAl
AppPublisherURL=https://github.com/IskanderAl/Scrcpy-GUI
DefaultDirName={autopf}\scrcpy-gui
DefaultGroupName=scrcpy GUI
SetupIconFile=dist\icon.ico
UninstallDisplayIcon={app}\scrcpy-gui.exe
OutputDir=installer_output
OutputBaseFilename=scrcpy-gui-setup-v2.0.0
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Types]
Name: "full"; Description: "Full installation"
Name: "custom"; Description: "Custom installation"; Flags: iscustom

[Components]
Name: "app"; Description: "scrcpy GUI (required)"; Types: full custom; Flags: fixed
Name: "scrcpy"; Description: "scrcpy 3.3.4 (screen mirroring engine)"; Types: full
Name: "adb"; Description: "ADB (Android Debug Bridge)"; Types: full
Name: "dlls"; Description: "Required DLL libraries"; Types: full custom; Flags: fixed

[Files]
; Main app (always installed)
Source: "dist\scrcpy-gui.exe"; DestDir: "{app}"; Components: app; Flags: ignoreversion
Source: "dist\icon.ico"; DestDir: "{app}"; Components: app; Flags: ignoreversion

; scrcpy (optional)
Source: "dist\scrcpy.exe"; DestDir: "{app}"; Components: scrcpy; Flags: ignoreversion
Source: "dist\scrcpy-server"; DestDir: "{app}"; Components: scrcpy; Flags: ignoreversion

; adb (optional)
Source: "dist\adb.exe"; DestDir: "{app}"; Components: adb; Flags: ignoreversion
Source: "dist\AdbWinApi.dll"; DestDir: "{app}"; Components: adb; Flags: ignoreversion
Source: "dist\AdbWinUsbApi.dll"; DestDir: "{app}"; Components: adb; Flags: ignoreversion

; DLLs (always installed)
Source: "dist\SDL2.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion
Source: "dist\avcodec-61.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion
Source: "dist\avformat-61.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion
Source: "dist\avutil-59.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion
Source: "dist\libusb-1.0.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion
Source: "dist\swresample-5.dll"; DestDir: "{app}"; Components: dlls; Flags: ignoreversion

[Icons]
Name: "{group}\scrcpy GUI"; Filename: "{app}\scrcpy-gui.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall scrcpy GUI"; Filename: "{uninstallexe}"
Name: "{autodesktop}\scrcpy GUI"; Filename: "{app}\scrcpy-gui.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional:"

[Run]
Filename: "{app}\scrcpy-gui.exe"; Description: "Launch scrcpy GUI"; Flags: nowait postinstall skipifsilent
