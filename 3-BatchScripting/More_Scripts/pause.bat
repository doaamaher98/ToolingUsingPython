@echo off
title Custom Pause

echo Paused
ping localhost -n 3 >nul

echo Done pausing.
pause