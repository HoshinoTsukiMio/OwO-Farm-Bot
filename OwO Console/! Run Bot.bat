@echo off
set "file_path=%~dp0"
cd %file_path%
call !venv\Scripts\activate.bat
python core\!Main.py

