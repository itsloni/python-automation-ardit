from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')# So this line basically an empty pdf page, portrait, units is in points and it's an A4 Paper.
pdf.add_page()

pdf.image('LONI PROFILE (red) (1).JPEG', w=80, h=90)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Loni's Profile Picture", align='C', ln=1)



pdf.output('output.pdf')

