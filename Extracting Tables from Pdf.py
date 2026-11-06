import tabula #THis library installed pandas/ uses pandas in the background so pandas methods can be used

table = tabula.read_pdf('weather.pdf', pages=1)

print(table[0])

table[0].to_csv('output.csv', index=None)
