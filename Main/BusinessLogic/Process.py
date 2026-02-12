from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
import time
import json
from Main.Services.Date_Timer import def_mostrar_tiempo
import pandas as pd
from Main.Config.Global_parameters import FILE_REGISTRO_VENTAS
import os
from Main.Config.Global_parameters import FILE_PARTE_DIARIO
import Main.Config.Config_celdas_grifos as Config_celdas_grifos

def def_RunProcess():

    # print(f"[INFO] Fecha procesar: "+dia_a_procesar)
    inicio = time.time()
    try:
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        
        # 1. Configuración
        ruta_carpeta = FILE_PARTE_DIARIO 
        Listado_grifos = list(Config_celdas_grifos.config_celdas_grifos.keys())
        lista_grifos_a_procesar = []
        try:
            # 1. Obtenemos la lista de archivos reales
            archivos = os.listdir(ruta_carpeta)
        
            print(f"--- Analizando archivos en: {ruta_carpeta} ---\n")
        
            for nombre_archivo in archivos:
                nombre_min = nombre_archivo.lower()
                
                encontrado = False
                lugar_detectado = ""
        
                for lugar in Listado_grifos:
                    if lugar.lower() in nombre_min:
                        encontrado = True
                        lugar_detectado = lugar
                        break
        
                if encontrado:
                    print(f"✅ EXISTE: El archivo '{nombre_archivo}' es un registro de [{lugar_detectado.upper()}]")
                    datos_grifo = {
                        'Grifo': lugar_detectado.upper(),
                        'Ruta': nombre_archivo
                        }
                    lista_grifos_a_procesar.append(datos_grifo)
                else:
                    print(f"❌ NO REGISTRADO: El archivo '{nombre_archivo}' no coincide con ninguna palabra clave")
            # print(lista_grifos_a_procesar)
            print("")
            print("")
            print("[INICIO] PROCESO INICIADO")
            for date_grifo_excel in lista_grifos_a_procesar:
                Venta_DTO=def_Leer_parte_diario(FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'],'21.01.26')
                List_ventas_procesadas.append(Venta_DTO)
                def_escribir_parte_diario(List_ventas_procesadas,FILE_REGISTRO_VENTAS)
                print("[FIN] PROCESO FINALIZADO")
        except FileNotFoundError:
            print("Error: No se encontró la carpeta especificada.")
    
        # # # Dias = ["01.01.26","02.01.26","03.01.26","04.01.26","05.01.26","06.01.26","07.01.26","08.01.26","09.01.26", "10.01.26",
        # # #         "11.01.26","12.01.26","13.01.26","14.01.26","15.01.26","16.01.26","17.01.26","18.01.26","19.01.26", "20.01.26",
        # # #         "21.01.26","22.01.26","23.01.26"]
        # # # for dia in Dias:
        # # #     Venta_DTO=def_Leer_parte_diario("ArchivosExcel/Parte_diario/PARTE DIARIO 3 ENERO BRASIL.xlsx", dia)
        # # #     List_ventas_procesadas.append(Venta_DTO)
        
        # excel_file = pd.ExcelFile("ArchivosExcel/Parte_diario/PARTE DIARIO 3 ENERO BRASIL.xlsx")
        # nombres_hojas = excel_file.sheet_names
        # for l in nombres_hojas:
        #     Venta_DTO=def_Leer_parte_diario("ArchivosExcel/Parte_diario/PARTE DIARIO 3 ENERO BRASIL.xlsx",'BRASIL', l)
        #     List_ventas_procesadas.append(Venta_DTO)
        
        # # # # Imprimir json
        # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))
        
        
    except FileNotFoundError:
        print("[ \u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[ \u274C ERROR] El archivo existe, pero no se encontró la hoja")
    except Exception as e:
        print(f"[ \u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

