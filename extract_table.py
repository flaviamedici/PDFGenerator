import tabula

table = tabula.read_pdf('weather.pdf', pages=1)
print(table)

table[0].to_csv('weather.csv', index=False)
