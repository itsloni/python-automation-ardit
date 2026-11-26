import gspread
import time

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("Automating google-sheet with python")

worksheet = spreadsheet.worksheet("2013")

worksheet1 = spreadsheet.worksheet("watch")

while True:
    value1 = worksheet.acell("G26").value
    time.sleep(3)
    value2 = worksheet.acell("G26").value
    if value1 != value2:
        worksheet1.update([["changed"]], "A1")
