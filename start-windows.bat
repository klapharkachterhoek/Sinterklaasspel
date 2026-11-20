@echo off
rem Sinterklaas Dobbelspel - starten op Windows (schermvullend / kiosk)
rem Afsluiten: Alt+F4
setlocal
cd /d "%~dp0"
set "URL=%~dp0index.html"

rem Python aanwezig? Dan server starten zodat instellingen in config.json worden bewaard.
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"
if defined PY %PY% --version >nul 2>nul || set "PY="
if defined PY (
  start "Sinterklaas server" /min %PY% server.py --no-browser
  set "URL=http://127.0.0.1:8765/"
  timeout /t 2 /nobreak >nul
)

set "EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE%" set "EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if exist "%EDGE%" (
  start "" "%EDGE%" --kiosk "%URL%" --edge-kiosk-type=fullscreen --no-first-run --autoplay-policy=no-user-gesture-required --user-data-dir="%LOCALAPPDATA%\Sinterklaasspel\edge"
) else (
  start "" "%URL%"
)
endlocal
