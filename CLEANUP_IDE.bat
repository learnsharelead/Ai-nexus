@echo off
echo ==================================================
echo      IDE RESOURCE NUCLEAR CLEANUP
echo ==================================================
echo.
echo [1/3] Killing stuck language server processes...
taskkill /F /IM pyrefly.exe /T 2>nul
taskkill /F /IM language_server_windows_x64.exe /T 2>nul
taskkill /F /IM node.exe /T 2>nul
echo.
echo [2/3] Cleaning Python cache folders...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo.
echo [3/3] System Optimization complete.
echo.
echo ==================================================
echo Please RESTART VS Code now.
echo ==================================================
pause
