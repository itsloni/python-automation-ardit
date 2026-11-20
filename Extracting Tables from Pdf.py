import tabula #This library installed pandas/ uses pandas in the background so pandas methods can be used
# Tabula is used to extract table from ONLY PDF files!

table = tabula.read_pdf('weather.pdf', pages=1)

print(table[0])

table[0].to_csv('output.csv', index=None)
