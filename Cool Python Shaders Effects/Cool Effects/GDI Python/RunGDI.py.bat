@ECHO OFF & CLS & ECHO.
NET FILE 1>NUL 2>NUL & IF ERRORLEVEL 1 (ECHO You must right-click and select &
  ECHO "RUN AS ADMINISTRATOR"  to run this batch. Exiting... & ECHO. &
  PAUSE & EXIT /D)
REM ... proceed here with admin rights ...