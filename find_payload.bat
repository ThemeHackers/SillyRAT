@echo off
echo ====== Searching for sillyrat.exe in running processes ======
tasklist /FI "IMAGENAME eq sillyrat.exe" /FO TABLE

echo.
echo ====== Searching for running processes containing 'sillyrat' (partial match) ======
tasklist | findstr /I "sillyrat"

echo.
echo ====== Searching Registry for keys or values containing 'sillyrat' ======
echo Searching in HKEY_CURRENT_USER...
reg query HKCU /f sillyrat /t REG_SZ /s 2>nul

echo.
echo Searching in HKEY_LOCAL_MACHINE...
reg query HKLM /f sillyrat /t REG_SZ /s 2>nul

echo.
pause
