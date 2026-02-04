# import openpyxl

# wb = openpyxl.load_workbook('MAIN/GRIFOS/brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx')

# # 2. Seleccionamos la hoja por su nombre
# nombre_hoja = '32. BRASIL'
# sheet = wb[nombre_hoja]

# # Ahora puedes trabajar solo en esa hoja
# print(f"Estás trabajando en: {sheet.title}")
# sheet['D26'] = 2355.55
# wb.save('brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx')


# Lista_credito_brasil = [
#         {'Fila':'J','CLiente':'ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA '},
#         {'Fila':'L','CLiente':'C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA '},
#         {'Fila':'T','CLiente':'RED DE COMBUSTIBLES LIQUIDOS SAC REDCOL SAC '},
#         {'Fila':'Y','CLiente':'SEGURO INTEGRAL DE SALUD'},
#         {'Fila':'AL','CLiente':'ALMACENERA MERCANTIL SOCIEDAD COMERCIAL DE RESPONSABILIDAD LIMITADA '}
#     ]
# # for Lista in Lista_credito_brasil:
# #     if(Lista['cliente']=='C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA'):
# registro = next((u for u in Lista_credito_brasil if u["CLiente"] == "ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA "), None)

# print(registro)
# if(registro!=None):
#     print(registro)

from datetime import datetime

print(datetime.strptime("21.01.26", "%d.%m.%y").strftime("%Y-%m-%d"))