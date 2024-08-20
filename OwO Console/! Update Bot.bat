@echo off
set "file_path=%~dp0"
echo cd %file_path%
call !venv\Scripts\activate.bat
python core\!Update.py
pause
