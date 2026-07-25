from fpdf import FPDF, XPos, YPos

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.image('pic1.jpg', w=80, h=50)

pdf.set_font('helvetica', 'B', size=24)
pdf.cell(w=0, h=50, text='Rabbits vs Hare', align='C')

pdf.set_font('helvetica', 'B', size=14)
pdf.cell(w=0, h=15, text='Description', new_x=XPos.LMARGIN,new_y=YPos.NEXT)

pdf.set_font('helvetica', size=12)
text1= """
In general, rabbits are smaller and have shorter ears than hares. 
They are born without fur and with closed eyes after a gestation period of 31 days. 
Rabbits prefer to hide, rather than run, from their enemies. 
They prefer habitats composed of trees and shrubs, 
where they live in burrows dug into the soil. 
Hares, in contrast, are larger, and they are born fully developed with fur and 
opened eyes after a gestation period of about 42 days. 
"""
pdf.multi_cell(w=0, h=15, text=text1)

pdf.set_font('helvetica', 'B', size=14)
pdf.cell(w=100, h=15, text='Kingdom: ')

pdf.set_font('helvetica', size=14)
pdf.cell(w=100, h=15, text='Animalia')

pdf.set_font('helvetica', 'B', size=14)
pdf.cell(w=100, h=15, text='Phylum: ')

pdf.set_font('helvetica', size=14)
pdf.cell(w=100, h=15, text='Chordata')

pdf.output('output.pdf')