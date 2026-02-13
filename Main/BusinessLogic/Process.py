from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
import time
import json
from Main.Services.Date_Timer import def_mostrar_tiempo
import pandas as pd
from Main.Config.Global_parameters import FILE_REGISTRO_VENTAS
from Main.Config.Global_parameters import FILE_PARTE_DIARIO
from Main.Services.SaleConfig import def_obtener_archivos_siges
from Main.Services.SaleConfig import def_procesar_listado_hojas

def def_RunProcess():
    inicio = time.time()
    try:
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        print("[INICIO] PROCESO INICIADO")
        lista_grifos_a_procesar=def_obtener_archivos_siges(FILE_PARTE_DIARIO)
        for date_grifo_excel in lista_grifos_a_procesar:
            
            # Venta_DTO=def_Leer_parte_diario(FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'],'04.01.26')
            # List_ventas_procesadas.append(Venta_DTO)
            # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))
            
            excel_file = pd.ExcelFile(FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'])
            nombres_hojas = excel_file.sheet_names
            mes_param='01'
            hojas_procesadas = def_procesar_listado_hojas(nombres_hojas,mes_param)
            for hp in hojas_procesadas:
                Venta_DTO=def_Leer_parte_diario(FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'], hp['fecha_correcta'],hp['libro'])
                List_ventas_procesadas.append(Venta_DTO)
            # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))    
            
        def_escribir_parte_diario(List_ventas_procesadas,FILE_REGISTRO_VENTAS)

        print("[FIN] PROCESO FINALIZADO")
    except FileNotFoundError:
        print("[ \u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[ \u274C ERROR] El archivo existe, pero no se encontró la hoja")
    except Exception as e:
        print(f"[ \u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

