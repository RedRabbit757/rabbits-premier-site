@echo off
rem Double-click to preview the Rabbit's Premier site locally.
rem Keep this window open while recording. Close it (or Ctrl+C) to stop.
cd /d "%~dp0"
set PORT=8093
echo.
echo   Rabbit's Premier Property Care - local preview
echo   Open in your browser:  http://localhost:%PORT%
echo   Keep this window open. Close it to stop the server.
echo.
start "" http://localhost:%PORT%
python -m http.server %PORT%
