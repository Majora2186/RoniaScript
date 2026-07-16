@echo off
echo Uninstalling NanoFast dependencies...
python -m pip uninstall -y pandas openpyxl numpy python-dateutil six tzdata et_xmlfile

echo Deleting NanoFast directory...
:: Change directory to the parent folder to release the working directory lock
cd /d "%~dp0.."

:: Spawn an independent hidden command prompt that waits 2 seconds for this script to close, then deletes the folder
start /min cmd /c "ping 127.0.0.1 -n 2 > nul & rd /s /q "%~dp0""

:: Exit immediately to release the file lock
exit