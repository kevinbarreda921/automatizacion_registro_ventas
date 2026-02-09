from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
import time
import json
from Main.Services.Date_Timer import def_mostrar_tiempo

def def_RunProcess():
    print("[INICIO] PROCESO INICIADO")
    # print(f"[INFO] Fecha procesar: "+dia_a_procesar)
    inicio = time.time()
    try:
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        # Dias = ["01.01.26","02.01.26","03.01.26","04.01.26","05.01.26","06.01.26","07.01.26","08.01.26","09.01.26", "10.01.26",
        #         "11.01.26","12.01.26","13.01.26","14.01.26","15.01.26","16.01.26","17.01.26","18.01.26","19.01.26", "20.01.26",
        #         "21.01.26","22.01.26","23.01.26"]
        Dias = ["01.01.26","02.01.26","03.01.26","04.01.26","05.01.26","06.01.26","07.01.26","08.01.26","09.01.26", "10.01.26",
                "11.01.26","12.01.26","13.01.26","14.01.26","15.01.26"]
        # Dias = ["21.01.26","22.01.26"]
        for dia in Dias:
            # print(f"[INFO] Fecha procesar: "+dia)
            Venta_DTO=def_Leer_parte_diario("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx", dia)
            List_ventas_procesadas.append(Venta_DTO)
        # # # # Imprimir json
        # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))

        def_escribir_parte_diario(List_ventas_procesadas)
        
        print("[FIN] PROCESO FINALIZADO")
    
    except FileNotFoundError:
        print("[ \u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[ \u274C ERROR] El archivo existe, pero no se encontró la hoja: {dia_a_procesar}")
    except Exception as e:
        print(f"[ \u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

