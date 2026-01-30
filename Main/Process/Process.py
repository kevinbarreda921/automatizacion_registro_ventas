import openpyxl
import pandas as pd
from datetime import date


def def_Leer_parte_diario(Ruta_excel,dia_a_procesar):

 print("[INFO] PROCESO INICIADO")
 print("[INFO] Obteniendo Data...")
 df = pd.read_excel(Ruta_excel, sheet_name=dia_a_procesar, header=None)
 
 Venta_GPL = float(str(df.iloc[7, 15]).replace(',', '')) 
 Venta_GNV = float(str(df.iloc[8, 15]).replace(',', ''))

 Total_Tarjeta_de_Credito_Liquidos = float(str(df.iloc[16, 15]).replace(',', '').replace('-', ''))
 Total_Tarjeta_de_Credito_GLP = float(str(df.iloc[17, 15]).replace(',', '').replace('-', ''))
 Total_Tarjeta_de_Credito_GNV = float(str(df.iloc[18, 15]).replace(',', '').replace('-', '')) 
 
 Recaudo_Cofide_GNV = float(str(df.iloc[27, 15]).replace(',', '')) 
 Gastos = float(str(df.iloc[28, 15]).replace(',', '')) 

 # Data Hermes
 Hermes_monto_liquido=float(0)
 Hermes_monto_GLP=float(0)
 Hermes_monto_GNV1=float(0)
 Hermes_monto_GNV2=float(0)
 Hermes_contar_gnv=int(0)
 contador_hermes=124
 for i in range(4):
  tipo_combustible = str(df.iloc[contador_hermes, 16]) 
  tipo_combustible_precio = float(str(df.iloc[contador_hermes, 14]).replace(',', '')) 
  if(tipo_combustible=='Líquido'):
   Hermes_monto_liquido = tipo_combustible_precio
  elif(tipo_combustible=='GLP'):
   Hermes_monto_GLP = tipo_combustible_precio
  elif(tipo_combustible=='GNV'):
   Hermes_contar_gnv+=1
   if(Hermes_contar_gnv==1):
    Hermes_monto_GNV1 = tipo_combustible_precio
   else:
    Hermes_monto_GNV2 = tipo_combustible_precio
  else:
   print(f"Error: Se cambio el formato para tabla hermes")
  contador_hermes =contador_hermes+1

 # Total crédito
 Lista_clientes_credito = []
 Contador_credito=14
 
 if(str(df.iloc[Contador_credito, 0])!='nan'):
  while True:
   Cliente_credito = str(df.iloc[Contador_credito, 0].replace('  ', ''))
   Cliente_credito_total = float(str(df.iloc[Contador_credito, 6]).replace(',', '')) 
   if Contador_credito==14:
    Lista_clientes_credito.append({"cliente": Cliente_credito, "monto": Cliente_credito_total})
   else:
    if Cliente_credito==' ':
     break
    encontrado = False
    for Lista in Lista_clientes_credito:
      if Lista['cliente'] == Cliente_credito:
       Lista['monto'] = round(Lista['monto']+Cliente_credito_total, 2)
       encontrado = True
       break
    if not encontrado:
     Lista_clientes_credito.append({"cliente": Cliente_credito, "monto": Cliente_credito_total})
   Contador_credito+=1
 
#  for Lista in Lista_clientes_credito:
#   print(f"Lista_clientes_credito : {Lista}")
 
 # Total Padel
 Lista_clientes_padel = []
 Contador_credito+=1
 Cliente_credito =' '
 Cliente_credito_total =0
 
 if(str(df.iloc[Contador_credito, 0])!='nan'):
  while True:
   Cliente_credito = str(df.iloc[Contador_credito, 0].replace('  ', ''))
   Cliente_credito_total = float(str(df.iloc[Contador_credito, 6]).replace(',', '')) 
   if Cliente_credito==' ':
    break
   encontrado = False
   for Lista in Lista_clientes_padel:
     if Lista['cliente'] == Cliente_credito:
      Lista['monto'] = round(Lista['monto']+Cliente_credito_total, 2)
      encontrado = True
      break
   if not encontrado:
         Lista_clientes_padel.append({"cliente": Cliente_credito, "monto": Cliente_credito_total})
   Contador_credito+=1
 
#  for Lista in Lista_clientes_padel:
#   print(f"Lista_clientes_padel : {Lista}")
 
#  for Lista in Data.Lista_brasil:
#   if Lista['CLiente'] == 'SEGURO INTEGRAL DE SALUD':
#    print(f"Lista_brasil : {Lista['Fila']}")
#    break

 #Buscar Fila para insertar datos
 df = pd.read_excel("brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx", sheet_name="32. BRASIL", header=None)
 Fila_insert=0
 Fecha_Procesar = '2026-01-21'
 for t in range(32):
  try:
   t+=5
   Buscar_Fecha = str(df.iloc[t, 1].date())
   if(Buscar_Fecha==Fecha_Procesar):
    Fila_insert=t+1
    break
  except:
   break

# Guardar data

 print("[INFO] Registrando data...")

 wb = openpyxl.load_workbook('../Grifos/BRASIL/REGISTRO VENTAS -  2026- 01 (1).xlsx')
 nombre_hoja = '32. BRASIL'
 sheet = wb[nombre_hoja]

 Campo_venta_glp="D"+str(Fila_insert)
 Campo_venta_gnv="E"+str(Fila_insert)
 Campo_venta_rec_cofide="F"+str(Fila_insert)

 sheet[Campo_venta_glp] = Venta_GPL
 sheet[Campo_venta_gnv] = Venta_GNV
 sheet[Campo_venta_rec_cofide] = Recaudo_Cofide_GNV

 Campo_Total_Tarjeta_de_Credito_Liquidos="AO"+str(Fila_insert)
 Campo_Total_Tarjeta_de_Credito_GLP="AP"+str(Fila_insert)
 Campo_Total_Tarjeta_de_Credito_GNV="AQ"+str(Fila_insert)

 sheet[Campo_Total_Tarjeta_de_Credito_Liquidos] = Total_Tarjeta_de_Credito_Liquidos
 sheet[Campo_Total_Tarjeta_de_Credito_GLP] = Total_Tarjeta_de_Credito_GLP
 sheet[Campo_Total_Tarjeta_de_Credito_GNV] = Total_Tarjeta_de_Credito_GNV

 if(Gastos!=0.0):
  Campo_Gastos="BY"+str(Fila_insert)
  sheet[Campo_Gastos] = Gastos

 Campo_Hermes_monto_liquido="AX"+str(Fila_insert)
 Campo_Hermes_monto_GLP = "BD" + str(Fila_insert)
 Campo_Hermes_monto_GNV1 = "BE" + str(Fila_insert)
 Campo_Hermes_monto_GNV2 = "BF" + str(Fila_insert)

 sheet[Campo_Hermes_monto_liquido] = Hermes_monto_liquido
 sheet[Campo_Hermes_monto_GLP] = Hermes_monto_GLP
 sheet[Campo_Hermes_monto_GNV1] = Hermes_monto_GNV1
 sheet[Campo_Hermes_monto_GNV2] = Hermes_monto_GNV2

 for Lista in Lista_clientes_credito:
  print(f"Lista_clientes_credito : {Lista}")

 wb.save('brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx')

 print("[INFO] PROCESO FINALIZADO")


def obtener_fecha_actual():
    return date.today()


