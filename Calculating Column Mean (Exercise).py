import statistics
import gspread

gc = gspread.service_account("secrets.json")

spreadsheet = gc.open("Automating google-sheet with python")

worksheet = spreadsheet.worksheet("2013")

column = worksheet.col_values(7)[1:]

mean_fahrenheit = statistics.mean([float(i) for i in column])

print(column)
print(mean_fahrenheit)

