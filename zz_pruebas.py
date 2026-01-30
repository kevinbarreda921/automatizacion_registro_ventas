import openpyxl

wb = openpyxl.load_workbook('MAIN/GRIFOS/brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx')

# 2. Seleccionamos la hoja por su nombre
nombre_hoja = '32. BRASIL'
sheet = wb[nombre_hoja]

# Ahora puedes trabajar solo en esa hoja
print(f"Estás trabajando en: {sheet.title}")
sheet['D26'] = 2355.55
wb.save('brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx')

