@echo off
echo ==========================================
echo    AI Nexus - AI Transformation Ecosystem
echo ==========================================
echo.

:: Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q

echo.
echo Starting AI Nexus...
echo ==========================================
echo.

:: Run Streamlit app
streamlit run app.py --server.port 8501

pause
