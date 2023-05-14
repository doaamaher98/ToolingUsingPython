:::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::: Calculator by Doaa Maher ::::::::::::::
::::::::::::::::::: VERSION : 1.0 :::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::


@echo off

title My Calculator

:opr
goto :main

:mul
set /a mul_val=%~1*%~2
echo %mul_val%
goto :eof

:add
set /a sum_val=%~1+%~2
echo %sum_val%
goto :eof

:sub
set /a sub_value=%~1-%~2
echo %sub_value%
goto :eof

:div
set /a div_value=%~1/%~2
echo %div_value%
goto :eof


:main
set /p n1=Enter first value:
set /p n2=Enter second value:
set /p op=Enter Wanted operation name:

set /a n1=%n1%
set /a n2=%n2%


if %op% equ mul (
	call :mul %n1% %n2%
	
) else if %op% equ add (
	call :add %n1% %n2%
	
) else if %op% equ sub (
	call :sub %n1% %n2%
	
) else if %op% equ div (
	call :div %n1% %n2%
	
)
goto :opr