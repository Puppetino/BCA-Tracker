@echo off

:: Activate the environment
call venv\Scripts\activate
echo Enviroment Started
echo Starting Tracker...

:: Start the Tracker
python BCA_Tracker.py

pause