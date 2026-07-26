import pandas as pd
from fpdf import FPDF, XPos, YPos

df = pd.read_excel('data.xlsx')
print(df.head())

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font('helvetica', 'B', size=24)
    pdf.cell(w=0, h=50, text=row['name'], align='CENTER', new_x=XPos.LMARGIN,new_y=YPos.NEXT)

    for column in df.columns[1:]:
        pdf.set_font('helvetica', 'B', size=14)
        pdf.cell(w=100, h=25, text=f"{column.title()}:")

        pdf.set_font('helvetica', size=14)
        pdf.cell(w=100, h=25, text=row[column], new_x=XPos.LMARGIN,new_y=YPos.NEXT)

    pdf.output(f"{row['name']}.pdf")