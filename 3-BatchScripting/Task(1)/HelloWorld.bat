@ECHO OFF
setLocal EnableDelayedExpansion 

IF [%4]==[] GOTO INVALIDINPUT

REM Get the arguments inside internal variables
SET output_folder=TXT\%1

SET txt_file=%2
SET src_file=%3
SET header_file=%4

REM Create output directory if it does not already exist
IF EXIST %output_folder% ( GOTO AFTERDIRECTORY )
REM If it doesn't exist, create it
MKDIR %output_folder%

REM Moving inside the folder
:AFTERDIRECTORY
CD %output_folder%

REM Removing read only attribute from the files to write to
attrib -r %txt_file%>nul
attrib -r %src_file%>nul
attrib -r %header_file%>nul

REM Check if text files existance, if yes inc val by 1, else put zero by default
IF EXIST %txt_file% (
  SET /p val=<%txt_file%
  SET /a inc1=val+1
  ECHO !inc1! >%txt_file% 
) ELSE (ECHO 0 >%txt_file%
)

REM Check if src files existance, if yes inc val by 1, else put zero by default
IF EXIST %src_file% (
  SET /p val=<%src_file%
  SET /a inc2=val+1
  ECHO !inc2! >%src_file% 
) ELSE (ECHO 0 >%src_file%
)

REM Check if header files existance, if yes inc val by 1, else put zero by default
IF EXIST %header_file% (
  SET /p val=<%header_file%
  SET /a inc3=val+1
  ECHO !inc3! >%header_file% 
) ELSE (ECHO 0 >%header_file%
)

REM Returing to read only attribute from the files to write to
attrib +r %txt_file%
attrib +r %src_file%
attrib +r %header_file%

CD ..
COPY /Y TXT\*.txt %txt_file% >NUL
COPY /Y TXT\*.c %src_file% >NUL
COPY /Y TXT\*.h %header_file% >NUL

GOTO END

:INVALIDINPUT
ECHO "invalid input"
:END