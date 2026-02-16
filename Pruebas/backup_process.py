from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
import time
import json
from Main.Services.Date_Timer import def_mostrar_tiempo
import pandas as pd
from Main.Config.Global_parameters import GLOBAL_FILE_REGISTRO_VENTAS
from Main.Config.Global_parameters import GLOBAL_FILE_PARTE_DIARIO
from Main.Services.SaleConfig import def_obtener_archivos_siges
from Main.Services.SaleConfig import def_procesar_listado_hojas

def def_procesar_hoy(dia,mes,fecha):
    inicio = time.time()
    try:
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        print("\n\n[INICIO] PROCESO INICIADO")
        lista_grifos_a_procesar=def_obtener_archivos_siges(GLOBAL_FILE_PARTE_DIARIO)
        if lista_grifos_a_procesar:
            for date_grifo_excel in lista_grifos_a_procesar:
                
                excel_file = pd.ExcelFile(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'])
                nombres_hojas = excel_file.sheet_names
                hojas_procesadas = def_procesar_listado_hojas(nombres_hojas,mes)
                # print(hojas_procesadas)
                Buscar_hojas_por_dia = [fila for fila in hojas_procesadas if fila['dia'] == dia]
                for hoja in Buscar_hojas_por_dia:
                    if(fecha==hoja['fecha_correcta']):
                        Venta_DTO=def_Leer_parte_diario(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'], fecha,hoja['libro'])
                        List_ventas_procesadas.append(Venta_DTO)
                    else:
                        print(f"[\u274C ERROR] El dia {fecha} no existe para el grifo {date_grifo_excel['Grifo']}")
            # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))
            if List_ventas_procesadas:
                def_escribir_parte_diario(List_ventas_procesadas,GLOBAL_FILE_REGISTRO_VENTAS)

        print("[FIN] PROCESO FINALIZADO")
    except FileNotFoundError:
        print("[\u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[\u274C ERROR] El archivo existe, pero no se encontró la hoja")
    except Exception as e:
        print(f"[\u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")
        
def def_procesar_por_dia(dia,mes):
    inicio = time.time()
    try:
        Dia_ejecutar=str(dia)+'.'+str(mes)+'.26'
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        print("\n\n[INICIO] PROCESO INICIADO")
        lista_grifos_a_procesar=def_obtener_archivos_siges(GLOBAL_FILE_PARTE_DIARIO)
        if lista_grifos_a_procesar:
            for date_grifo_excel in lista_grifos_a_procesar:
                
                excel_file = pd.ExcelFile(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'])
                nombres_hojas = excel_file.sheet_names
                hojas_procesadas = def_procesar_listado_hojas(nombres_hojas,mes)
                Buscar_hojas_por_dia = [fila for fila in hojas_procesadas if fila['dia'] == dia]
                for hoja in Buscar_hojas_por_dia:
                    Venta_DTO=def_Leer_parte_diario(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'], Dia_ejecutar,hoja['libro'])
                    List_ventas_procesadas.append(Venta_DTO)
            # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))
            # if List_ventas_procesadas:
            #     def_escribir_parte_diario(List_ventas_procesadas,FILE_REGISTRO_VENTAS)

        print("[FIN] PROCESO FINALIZADO")
    except FileNotFoundError:
        print("[\u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[\u274C ERROR] El archivo existe, pero no se encontró la hoja")
    except Exception as e:
        print(f"[\u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

def def_procesar_por_mes(mes):
    inicio = time.time()
    try:
        Venta_DTO=Venta()
        List_ventas_procesadas = []
        print("\n\n[INICIO] PROCESO INICIADO")
        lista_grifos_a_procesar=def_obtener_archivos_siges(GLOBAL_FILE_PARTE_DIARIO)
        if lista_grifos_a_procesar:
            for date_grifo_excel in lista_grifos_a_procesar:
                excel_file = pd.ExcelFile(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'])
                nombres_hojas = excel_file.sheet_names
                hojas_procesadas = def_procesar_listado_hojas(nombres_hojas,mes)
                for hp in hojas_procesadas:
                    Venta_DTO=def_Leer_parte_diario(GLOBAL_FILE_PARTE_DIARIO+'/'+date_grifo_excel['Ruta'],date_grifo_excel['Grifo'], hp['fecha_correcta'],hp['libro'])
                    List_ventas_procesadas.append(Venta_DTO)
                # print(json.dumps(List_ventas_procesadas, indent=4, default=lambda o: o.__dict__))    
            if List_ventas_procesadas:
                def_escribir_parte_diario(List_ventas_procesadas,GLOBAL_FILE_REGISTRO_VENTAS)
    
        print("[FIN] PROCESO FINALIZADO")
    except FileNotFoundError:
        print("[\u274C ERROR] El archivo de Excel no existe.")
    except ValueError:
        print(f"[\u274C ERROR] El archivo existe, pero no se encontró la hoja")
    except Exception as e:
        print(f"[\u274C ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")

