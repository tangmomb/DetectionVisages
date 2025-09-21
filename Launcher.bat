@echo off
REM Active l'environnement Python et lance Launcher.py

REM Remplacez 'venv' par le nom de votre dossier d'environnement si besoin
set VENV_DIR=venv

REM Active l'environnement
call %VENV_DIR%\Scripts\activate.bat

REM Lance le launcher
python Launcher.py

exit
