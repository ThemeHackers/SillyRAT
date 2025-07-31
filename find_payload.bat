@echo off
echo ====== Searching for payload.exe in running processes ======
tasklist /FI "IMAGENAME eq payload.exe" /FO TABLE

echo.
echo ====== Searching for running processes containing 'payload' (partial match) ======
tasklist | findstr /I "payload"

echo.
echo ====== Searching Registry for keys or values containing 'payload' ======
echo Searching in HKEY_CURRENT_USER...
reg query HKCU /f payload /t REG_SZ /s 2>nul

echo.
echo Searching in HKEY_LOCAL_MACHINE...
reg query HKLM /f payload /t REG_SZ /s 2>nul

echo.
pause
