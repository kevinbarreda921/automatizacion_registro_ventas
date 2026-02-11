import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("vast-lightning-453521-e6-8907d2746436.json", scope)
client = gspread.authorize(creds)

# Abrir el archivo por su ID
# El ID es el que ya tienes: 1C3JLWUg1FzFE7k7sfxXh-7JWXekyNAqO
sheet = client.open_by_key("1C3JLWUg1FzFE7k7sfxXh-7JWXekyNAqO").worksheet("01.01.26")

# Escribir en una celda (Fila, Columna, Valor)
# Ojo: gspread empieza a contar en 1, no en 0.
sheet.update_cell(1, 1, "Dato Nuevo") 

print("¡Escritura completada con éxito!")