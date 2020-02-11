' Assigned to Ctrl + Shift + M (M is for Magic)
Sub AnalyzeEverySheet()
    ' Declare variables
    Dim start As Date
    Dim minutes As Integer
    Dim seconds As Integer
    start = Now
    
    ' Analyze each worksheet
    For Each Sheet In ThisWorkbook.Sheets
        Sheet.Activate
        Sheet.Range("A1").Activate
        AnalyzeStocks
        ExtraChallenge
        Sheet.Range("A1").Activate
    Next
    Sheet1.Activate
    
    ' Print runtime
    seconds = DateDiff("s", start, Now)
    minutes = seconds / 60
    seconds = seconds Mod 60
    MsgBox ("Runtime: " & vbNewLine & vbNewLine _
        & minutes & " minutes and " & seconds & " seconds")
End Sub
Sub AnalyzeStocks()
    ' Declare variables
    Dim current_row As Integer
    Dim ticker As String
    Dim price_open As Double
    Dim price_close As Double
    Dim volume As LongLong
    
    ' Print headers
    ActiveSheet.Range("I1").Value = "Ticker"
    ActiveSheet.Range("J1").Value = "Yearly Change"
    ActiveSheet.Range("K1").Value = "Percent Change"
    ActiveSheet.Range("L1").Value = "Total Stock Volume"
    
    ' Read first line
    ticker = ActiveSheet.Range("A2").Value
    price_open = ActiveSheet.Range("C2").Value
    price_close = ActiveSheet.Range("F2").Value
    volume = ActiveSheet.Range("G2").Value
    
    current_row = 2
    ' Loop through data
    For i = 3 To ActiveSheet.Range("A1").CurrentRegion.Rows.Count + 1
        ' Check for new ticker symbol
        If ActiveSheet.Range("A" & i).Value = ticker Then
            price_close = ActiveSheet.Range("F" & i).Value
            volume = volume + ActiveSheet.Range("G" & i).Value
        Else
            DoEvents
            ActiveSheet.Range("I" & current_row & ":L" & current_row).Activate
            ' print previous ticker
            ActiveSheet.Range("I" & current_row).Value = ticker
            ActiveSheet.Range("J" & current_row).Value = _
                price_close - price_open
            ' can't divide by zero
            If price_open <> 0 Then _
                ActiveSheet.Range("K" & current_row).Value = _
                (price_close * 1# - price_open) / price_open
            ActiveSheet.Range("L" & current_row).Value = volume
            ' format previous ticker
            ActiveSheet.Range("I" & current_row).NumberFormat = "@"
            ActiveSheet.Range("J" & current_row).Interior.Color = _
                255 - 65025 * Int(price_close - price_open >= 0)
            ActiveSheet.Range("J" & current_row).NumberFormat = "0.00"
            ActiveSheet.Range("K" & current_row).NumberFormat = "0.00%"
            ActiveSheet.Range("L" & current_row).NumberFormat = "0"
            ' read first line of new ticker
            ticker = ActiveSheet.Range("A" & i).Value
            price_open = ActiveSheet.Range("C" & i).Value
            price_close = ActiveSheet.Range("F" & i).Value
            volume = ActiveSheet.Range("G" & i).Value
            current_row = current_row + 1
        End If
    Next
    
    ' Adjust column widths
    ActiveSheet.Range("I:L").Columns.AutoFit
End Sub
Sub ExtraChallenge()
    ' Declare variables
    Dim greatest_increase As Double
    Dim greatest_decrease As Double
    Dim greatest_total_volume As LongLong
    Dim greatest_increase_ticker As String
    Dim greatest_decrease_ticker As String
    Dim greatest_total_volume_ticker As String
    
    ' Print headers
    ActiveSheet.Range("P1").Value = "Ticker"
    ActiveSheet.Range("Q1").Value = "Value"
    ActiveSheet.Range("O2").Value = "Greatest % Increase"
    ActiveSheet.Range("O3").Value = "Greatest % Decrease"
    ActiveSheet.Range("O4").Value = "Greatest Total Volume"
    
    ' Read first line
    greatest_increase = ActiveSheet.Range("K2").Value
    greatest_decrease = ActiveSheet.Range("K2").Value
    greatest_total_volume = ActiveSheet.Range("L2").Value
    greatest_increase_ticker = ActiveSheet.Range("I2").Value
    greatest_decrease_ticker = ActiveSheet.Range("I2").Value
    greatest_total_volume_ticker = ActiveSheet.Range("I2").Value
    ' Loop through data
    For i = 2 To ActiveSheet.Range("I1").CurrentRegion.Rows.Count
        If ActiveSheet.Range("K" & i).Value > greatest_increase Then
            greatest_increase = ActiveSheet.Range("K" & i).Value
            greatest_increase_ticker = ActiveSheet.Range("I" & i).Value
        End If
        If ActiveSheet.Range("K" & i).Value < greatest_decrease Then
            greatest_decrease = ActiveSheet.Range("K" & i).Value
            greatest_decrease_ticker = ActiveSheet.Range("I" & i).Value
        End If
        If ActiveSheet.Range("L" & i).Value > greatest_total_volume Then
            greatest_total_volume = ActiveSheet.Range("L" & i).Value
            greatest_total_volume_ticker = ActiveSheet.Range("I" & i).Value
        End If
    Next
    ' Print values
    ActiveSheet.Range("P2").Value = greatest_increase_ticker
    ActiveSheet.Range("Q2").Value = greatest_increase
    ActiveSheet.Range("P3").Value = greatest_decrease_ticker
    ActiveSheet.Range("Q3").Value = greatest_decrease
    ActiveSheet.Range("P4").Value = greatest_total_volume_ticker
    ActiveSheet.Range("Q4").Value = greatest_total_volume
    ' Format value
    ActiveSheet.Range("Q3").NumberFormat = "0.00%"
    ActiveSheet.Range("Q2").NumberFormat = "0.00%"
    ' Adjust column widths
    ActiveSheet.Range("O:Q").Columns.AutoFit
    ActiveSheet.Range("O1:Q4").Activate
    DoEvents
End Sub
' Assigned to Ctrl + Shift + C
Sub CleanSheets() ' remove columns created through VBA
    For Each Sheet In ThisWorkbook.Sheets
        Sheet.Activate
        DoEvents
        Sheet.Range("A1").Activate
        Sheet.Range("I:Q").Delete
        DoEvents
    Next
    Sheet1.Activate
End Sub