@echo off
set "file_path=%~dp0"
echo cd %file_path%
echo Activating virtual environment...
call !venv\Scripts\activate.bat
echo Installing requirements...
python -m pip install -r lib.lib
echo Done!
