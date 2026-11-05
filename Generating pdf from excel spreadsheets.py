import pandas
from fpdf import FPDF
df = pandas.read_excel('data.xlsx')
#print(df)

for index, row in df.iterrows():
