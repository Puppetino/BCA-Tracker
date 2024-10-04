@echo off

:: Activate the environment
call venv\Scripts\activate

:: Pull latest changes from Git repository
git pull https://github.com/Puppetino/BCA-Tracker.git

:: Install updated requirements
pip install -r requirements.txt

deactivate