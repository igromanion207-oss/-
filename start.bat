@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist .venv (
    echo Создаю виртуальное окружение...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate.bat
)
echo Сайт запускается: http://127.0.0.1:5000
start "" http://127.0.0.1:5000
python run.py
