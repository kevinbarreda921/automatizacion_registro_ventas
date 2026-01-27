import datetime
import pandas as pd

#Buscar Fila para insertar datos
df = pd.read_excel("brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx", sheet_name="32. BRASIL", header=None)
Fecha_Procesar = '2026-01-01'
for t in range(32):
 try:
  t+=5
  Buscar_Fecha = str(df.iloc[t, 1].date())
#   print(f"------",Buscar_Fecha)
  if(Buscar_Fecha==Fecha_Procesar):
   print(Buscar_Fecha)
   t+=1
   print(t)
   break
 except:
  break
