@echo off

cd /D %~dp0

setlocal
set "PYTHONDIR=D:\Program Files\Python27"
set "PATH=%PATH%;%PYTHONDIR%\Scripts"

python ez_setup.py

easy_install PIL

@pause
