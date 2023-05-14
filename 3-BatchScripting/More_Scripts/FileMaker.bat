@echo off

title File Maker

:label
color 0b

set /p NameofFile=Enter the name of your file:
set /p NameofExtension=Enter the name of your extension:

echo. >%NameofFile%.%NameofExtension%

goto :label
