import pandas as pd

df = pd.read_excel(
    "Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx",
    sheet_name="01.01.26",
    header=None,
)

# Data Hermes
Hermes_monto_liquido = float(0)
Hermes_monto_GLP = float(0)
Hermes_monto_GNV1 = float(0)
Hermes_monto_GNV2 = float(0)
Hermes_contar_gnv = int(0)
contador_hermes = 120
Buscar_tabla_hermes=0
while True:
  Buscar_tabla_hermes+=1
  contador_hermes+=1
  tipo_combustible = str(df.iloc[contador_hermes, 16])
  if(Buscar_tabla_hermes==10):
    continue
  else:
    if(tipo_combustible=='TIPO'):
      contador_hermes+=1
      for i in range(4):
          tipo_combustible = str(df.iloc[contador_hermes, 16])
          tipo_combustible_precio = float(str(df.iloc[contador_hermes, 14]).replace(",", ""))
          if tipo_combustible == "Líquido":
              Hermes_monto_liquido = tipo_combustible_precio
          elif tipo_combustible == "GLP":
              Hermes_monto_GLP = tipo_combustible_precio
          elif tipo_combustible == "GNV":
              Hermes_contar_gnv += 1
              if Hermes_contar_gnv == 1:
                  Hermes_monto_GNV1 = tipo_combustible_precio
              else:
                  Hermes_monto_GNV2 = tipo_combustible_precio
          else:
              print(f"[ \u274C ERROR] Se cambio el formato para tabla hermes")
          contador_hermes = contador_hermes + 1    
      print(f"Hermes_monto_liquido : {Hermes_monto_liquido}")
      print(f"Hermes_monto_GNV1 : {Hermes_monto_GNV1}")
      print(f"Hermes_monto_GNV2 : {Hermes_monto_GNV2}")
      break


