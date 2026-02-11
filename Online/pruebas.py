import pandas as pd

# Debes modificar el enlace de compartir de Drive para que sea de descarga directa
# https://docs.google.com/spreadsheets/d/11pc6izCnj6bvzUSOyxT_LgfAx0em792W/edit?gid=577479952#gid=577479952
# https://docs.google.com/spreadsheets/d/1C3JLWUg1FzFE7k7sfxXh-7JWXekyNAqO/edit?usp=drive_link&ouid=100962766095096952178&rtpof=true&sd=true

# Tu ID extraído del link
FILE_ID = '1C3JLWUg1FzFE7k7sfxXh-7JWXekyNAqO'

# Convertimos el link de edición en un link de descarga directa para Excel
url = f'https://drive.google.com/uc?export=download&id={FILE_ID}'

try:
    # Pandas leerá el archivo directamente desde tu Drive
    df = pd.read_excel(url, sheet_name="21.01.26", header=None)
    Total_venta_acumulada = float(str(df.iloc[11, 15]).replace(",", ""))
    Venta_GPL = float(str(df.iloc[7, 15]).replace(",", ""))
    Venta_GNV = float(str(df.iloc[8, 15]).replace(",", ""))
    print(Total_venta_acumulada)
    print(Venta_GPL)
    print(Venta_GNV)
    
except Exception as e:
    print(f"Error: {e}")

# Lista_credito_brasil = [
#                 {'Fila':'H','CLiente':'COMMUNICATIONS AND SYSTEMS DEVELOPMENT SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'I','CLiente':'FUERO MILITAR POLICIAL'},
#                 {'Fila':'J','CLiente':'ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'L','CLiente':'C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'N','CLiente':'FONDO NACIONAL DE DESARROLLO PESQUERO'},
#                 {'Fila':'T','CLiente':'RED DE COMBUSTIBLES LIQUIDOS SAC REDCOL SAC'},
#                 {'Fila':'U','CLiente':'UNIDAD EJECUTORA 004 - FONDO DE COOPERACION PARA EL DESARROLLO SOCIAL'},
#                 {'Fila':'V','CLiente':'MUNICIPALIDAD DE JESUS MARIA'},
#                 {'Fila':'Y','CLiente':'SEGURO INTEGRAL DE SALUD'},
#                 {'Fila':'AC','CLiente':'INSTITUTO NACIONAL DE SALUD DEL NIñO'},
#                 {'Fila':'AL','CLiente':'ALMACENERA MERCANTIL SOCIEDAD COMERCIAL DE RESPONSABILIDAD LIMITADA'}
#             ]
# Lista_credito_puente_piedra= [
#                 {'Fila':'H','CLiente':'COMMUNICATIONS AND SYSTEMS DEVELOPMENT SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'I','CLiente':'FUERO MILITAR POLICIAL'},
#                 {'Fila':'J','CLiente':'ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'L','CLiente':'C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'N','CLiente':'FONDO NACIONAL DE DESARROLLO PESQUERO'},
#                 {'Fila':'T','CLiente':'RED DE COMBUSTIBLES LIQUIDOS SAC REDCOL SAC'},
#                 {'Fila':'U','CLiente':'UNIDAD EJECUTORA 004 - FONDO DE COOPERACION PARA EL DESARROLLO SOCIAL'},
#                 {'Fila':'V','CLiente':'MUNICIPALIDAD DE JESUS MARIA'},
#                 {'Fila':'Y','CLiente':'SEGURO INTEGRAL DE SALUD'},
#                 {'Fila':'AC','CLiente':'INSTITUTO NACIONAL DE SALUD DEL NIñO'},
#                 {'Fila':'AL','CLiente':'ALMACENERA MERCANTIL SOCIEDAD COMERCIAL DE RESPONSABILIDAD LIMITADA'}
#             ]
# Lista_credito_chilca= [
#                 {'Fila':'H','CLiente':'COMMUNICATIONS AND SYSTEMS DEVELOPMENT SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'I','CLiente':'FUERO MILITAR POLICIAL'},
#                 {'Fila':'J','CLiente':'ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'L','CLiente':'C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA'},
#                 {'Fila':'N','CLiente':'FONDO NACIONAL DE DESARROLLO PESQUERO'},
#                 {'Fila':'T','CLiente':'RED DE COMBUSTIBLES LIQUIDOS SAC REDCOL SAC'},
#                 {'Fila':'U','CLiente':'UNIDAD EJECUTORA 004 - FONDO DE COOPERACION PARA EL DESARROLLO SOCIAL'},
#                 {'Fila':'V','CLiente':'MUNICIPALIDAD DE JESUS MARIA'},
#                 {'Fila':'Y','CLiente':'SEGURO INTEGRAL DE SALUD'},
#                 {'Fila':'AC','CLiente':'INSTITUTO NACIONAL DE SALUD DEL NIñO'},
#                 {'Fila':'AL','CLiente':'ALMACENERA MERCANTIL SOCIEDAD COMERCIAL DE RESPONSABILIDAD LIMITADA'}
#             ]
# Lista_credito_viru = [
#                 {'Fila':'C','DATO':'TARJETA_CREDITO'},
#                 {'Fila':'D','DATO':'TARJETA_GLP'}
#             ]
# Lista_credito_BRASIL = [
#                 {'Fila':'D','DATO':'TARJETA_CREDITO'},
#                 {'Fila':'E','DATO':'TARJETA_GLP'}
#             ]
# Lista_credito_viru = [
#                 {'Fila':'C','DATO':'TARJETA_CREDITO'},
#                 {'Fila':'D','DATO':'TARJETA_GLP'}
#             ]
# Lista_credito_viru = [
#                 {'Fila':'C','DATO':'TARJETA_CREDITO'},
#                 {'Fila':'D','DATO':'TARJETA_GLP'}
#             ]