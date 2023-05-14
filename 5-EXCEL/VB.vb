Private Sub CommandButton1_Click()

Dim FileName As String
Dim RowCounter As Integer
Dim PinMode As String

FileName = InputBox("Enter the wanted path : ", "DIO_Configuration")
FileName = FileName + "\DIO_config.h"

Open FileName For Output As #1
    For RowCounter = 2 To 22
        Print #1, "define DIO_" + Cells(RowCounter, 1).Value + "         " + Cells(RowCounter, 2).Value

    Next RowCounter
    
Close #1