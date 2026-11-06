import pymupdf
import pandas
import tabula

pdf_table = tabula.read_pdf('Table+and+Text.pdf', pages=1)
print(pdf_table[0])


