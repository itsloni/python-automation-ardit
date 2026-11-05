from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')# So this line basically an empty pdf page, portrait, units is in points and it's an A4 Paper.
pdf.add_page() # IMPORTANT to add the empty  page you just created above.

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

pdf.set_font(family='Times', style='B', size=20)
pdf.cell(w=0, h=40, txt="Loni's Human Classification", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Kingdom:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Animalia", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Phylum:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Chordata", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Class:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Mammalia", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Order:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Primates", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Family:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Hominidae", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Genus:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Homo", ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=20, txt="Species:")

pdf.set_font(family='Times', size=18)
pdf.cell(w=100, h=20, txt="Homo sapiens", ln=1)



pdf.output('output.pdf')

