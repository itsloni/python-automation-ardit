import statistics
import gspread

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("Automating google-sheet with python")

worksheet = spreadsheet.worksheet("2013")

column = worksheet.col_values(7)[1:]
print(column)
