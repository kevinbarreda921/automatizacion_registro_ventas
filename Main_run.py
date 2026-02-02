from Main.BusinessLogic import Process
import os

# Main
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_excel = os.path.join(
    BASE_DIR,  
    "Main",
    "Grifos",
    "BRASIL",
    "21.01.26",
    "PARTE DIARIO - SIGES- 3ENERO- BRASIL.xlsx"
)
Process.def_Leer_parte_diario("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","21.01.26")

# Fecha_Procesar = Process.obtener_fecha_actual()
# print(Fecha_Procesar)
