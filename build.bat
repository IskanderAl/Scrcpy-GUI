@echo off
set VERSION=2.0.0
set SCRCPY_SRC=H:\Projects\ScrpyInterface

echo [1/3] Building scrcpy-gui.exe...
pyinstaller --onefile --windowed --icon=icon.ico --name=scrcpy-gui main.py
if errorlevel 1 goto :error

echo [2/3] Copying scrcpy files to dist...
copy "%SCRCPY_SRC%\scrcpy.exe" dist\
copy "%SCRCPY_SRC%\adb.exe" dist\
copy "%SCRCPY_SRC%\scrcpy-server" dist\
copy "%SCRCPY_SRC%\AdbWinApi.dll" dist\
copy "%SCRCPY_SRC%\AdbWinUsbApi.dll" dist\
copy "%SCRCPY_SRC%\SDL2.dll" dist\
copy "%SCRCPY_SRC%\avcodec-61.dll" dist\
copy "%SCRCPY_SRC%\avformat-61.dll" dist\
copy "%SCRCPY_SRC%\avutil-59.dll" dist\
copy "%SCRCPY_SRC%\libusb-1.0.dll" dist\
copy "%SCRCPY_SRC%\swresample-5.dll" dist\
copy "%SCRCPY_SRC%\icon.ico" dist\

echo [3/3] Creating zip archive...
powershell -Command "Compress-Archive -Path 'dist\*' -DestinationPath 'dist\scrcpy-gui-v%VERSION%-win64.zip' -Force"

echo.
echo Done! Files ready:
echo   dist\scrcpy-gui.exe
echo   dist\scrcpy-gui-v%VERSION%-win64.zip
pause
goto :eof

:error
echo Build failed!
pause
