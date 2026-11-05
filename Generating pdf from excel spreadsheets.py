import pandas
from fpdf import FPDF
df = pandas.read_excel('data.xlsx')
#print(df)

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page() # Important to always write this inorder to add the empty page created above

    pdf.set_font(family='Times', style='B', size=24)
    
