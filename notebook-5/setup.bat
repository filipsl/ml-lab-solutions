@echo off

pip3.exe install virtualenv
python.exe -m virtualenv venv
call venv\Scripts\activate.bat
pip3.exe install -r requirements.txt
python.exe -m ipykernel install --user --name=venv