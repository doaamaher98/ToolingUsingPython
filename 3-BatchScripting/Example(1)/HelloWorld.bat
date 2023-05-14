@ECHO OFF

cls

if [%3]==[] goto INVALIDEntry

set text_value=%1
set output_folder=%2
set output_file=%3

IF EXIST %output_folder% (
GOTO AfterDIRECTORY
)

MKDIR %output_folder%

:AfterDIRECTORY
cd %output_folder%
attrib -r %output_file%
ECHO %text_value%>%output_file%
attrib +r %output_file%
cd..

:INVALIDentry
echo "Invalid Entry"
pause
exit 0