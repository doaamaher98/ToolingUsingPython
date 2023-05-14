@ECHO OFF

title Files Generation

FOR /F "tokens=1-4" %%G IN (Input.txt) DO (CALL HelloWorld.bat %%G %%H %%I %%J)

ECHO "reached end"