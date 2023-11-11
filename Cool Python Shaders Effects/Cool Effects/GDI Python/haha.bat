:: @echo OFF
NET SESSION
IF %ERRORLEVEL% NEQ 0 GOTO ELEVATE
GOTO ADMINTASKS

:ELEVATE
CD /d %~dp0
MSHTA "javascript: var shell = new ActiveXObject('shell.application'); shell.ShellExecute('%~nx0', '', '', 'runas', 1);close();"
GOTO ADMINTASKS
::MSHTA "javascript:alert('Exiting With Error Code 5\n\nNo Elevation\nProgram must be ran as administrator');close();"

:ADMINTASKS
python GDI.py