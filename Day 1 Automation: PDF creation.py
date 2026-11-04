from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')# So this line basically an empty pdf page, portrait, units is in points and it's an A4 Paper.
pdf.add_page()

pdf.image('LONI PROFILE (red) (1).JPEG', w=80, h=90)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Loni's Profile Picture", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt="Description", ln=1) #cell method is used for text with about just single line

pdf.set_font(family='Times', style='B', size=12)
txt1 = """My name is Lonnie, and this is my personal profile. The red profile picture you see is one of my favorite photos. 
It has a bold and confident model-like feel that I really like. I use this same red picture across my platforms, including Discord 
and Notion, because it stands out and feels like my personal brand. This PDF is a simple introduction to who I am."""
pdf.multi_cell(w=0, h=15, txt=txt1, ln=1) #Multi_cell method is use for text with multiple lines

pdf.output('output.pdf')

