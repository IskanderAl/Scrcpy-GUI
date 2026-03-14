@echo off
if "%SCRCPY_DIR%"=="" set SCRCPY_DIR=scrcpy
echo Using scrcpy from: %SCRCPY_DIR%

echo [1/3] Building scrcpy-gui.exe...
pyinstaller --onefile --windowed --name=scrcpy-gui main.py
if errorlevel 1 goto :error

echo [2/3] Copying scrcpy files to dist...
copy "%SCRCPY_DIR%\scrcpy.exe" dist\
copy "%SCRCPY_DIR%\adb.exe" dist\
copy "%SCRCPY_DIR%\scrcpy-server" dist\
copy "%SCRCPY_DIR%\AdbWinApi.dll" dist\
copy "%SCRCPY_DIR%\AdbWinUsbApi.dll" dist\
copy "%SCRCPY_DIR%\SDL2.dll" dist\
copy "%SCRCPY_DIR%\avcodec-61.dll" dist\
copy "%SCRCPY_DIR%\avformat-61.dll" dist\
copy "%SCRCPY_DIR%\avutil-59.dll" dist\
copy "%SCRCPY_DIR%\libusb-1.0.dll" dist\
copy "%SCRCPY_DIR%\swresample-5.dll" dist\

echo [3/3] Creating zip archive...
powershell -Command "Compress-Archive -Path 'dist\*' -DestinationPath 'dist\scrcpy-gui-v1.0.0-win64.zip' -Force"

echo.
echo Done! Ready to upload:
echo   dist\scrcpy-gui-v1.0.0-win64.zip
pause
goto :eof

:error
echo Build failed!
pause
