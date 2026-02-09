from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
import time
import json
from Main.Services.Date_Timer import def_mostrar_tiempo

def def_RunProcess(Ruta_excel, dia_a_procesar):
    print("[INICIO] PROCESO INICIADO")
    print(f"[INFO] Fecha procesar: "+dia_a_procesar)
    inicio = time.time()
    # # # # mis_registros = []
    try:
        # # for i in range(3): # Imprime 0, 1, 2
        Venta_DTO=Venta()
        Venta_DTO=def_Leer_parte_diario(Ruta_excel, dia_a_procesar)
        def_escribir_parte_diario(Venta_DTO,dia_a_procesar)
            # # # # mis_registros.append(Venta_DTO)
            
        # print(json.dumps(Venta_DTO.__dict__, indent=4, default=lambda o: o.__dict__))
        # # # # print(json.dumps([v.__dict__ for v in mis_registros], indent=4, default=lambda o: o.__dict__))
        
        print("[FIN] PROCESO FINALIZADO")
    
    except FileNotFoundError:
        print("[ \u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[ \u274C ERROR] El archivo existe, pero no se encontró la hoja: {dia_a_procesar}")
    except Exception as e:
        print(f"[ \u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        # print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

