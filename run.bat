@echo off
setlocal enabledelayedexpansion
echo ==========================================
echo    AI Nexus - AI Transformation Ecosystem
echo ==========================================
echo.

:: Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo Python version: %PYVER%

:: Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo.
)

:: Activate virtual environment
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

:: Install dependencies (only if requirements changed)
set REQFILE=requirements.txt
set MARKER=venv\.requirements_installed

if not exist "%MARKER%" (
    echo Installing dependencies...
    pip install -r %REQFILE% -q
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    type nul > "%MARKER%"
) else (
    :: Check if requirements.txt is newer than marker
    for %%A in (%REQFILE%) do set REQ_DATE=%%~tA
    for %%A in (%MARKER%) do set MARKER_DATE=%%~tA
    if "!REQ_DATE!" gtr "!MARKER_DATE!" (
        echo Updating dependencies...
        pip install -r %REQFILE% -q
        type nul > "%MARKER%"
    )
)

echo.
echo Starting AI Nexus...
echo ==========================================
echo Access the app at: http://localhost:8501
echo ==========================================
echo.

:: Run Streamlit app
streamlit run app.py --server.port 8501 --server.headless false

:: If we get here, Streamlit exited
echo.
echo AI Nexus has stopped.
pause
