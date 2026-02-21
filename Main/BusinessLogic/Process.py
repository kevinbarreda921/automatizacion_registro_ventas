import time
import os
import pandas as pd
import json 
from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
from Main.Services.Date_Timer import def_mostrar_tiempo
from Main.Config.Global_parameters import GLOBAL_FILE_REGISTRO_VENTAS, GLOBAL_FILE_PARTE_DIARIO
from Main.Services.SaleConfig import def_obtener_archivos_siges, def_procesar_listado_hojas

def ejecutar_proceso_base(mes, filtro_hojas_fn=None, fecha_esperada=None):
    inicio = time.time()
    list_ventas_procesadas = []
    try:
        lista_grifos = def_obtener_archivos_siges(GLOBAL_FILE_PARTE_DIARIO)
        if not lista_grifos: return

        for grifo in lista_grifos:
            ruta_completa = os.path.join(GLOBAL_FILE_PARTE_DIARIO, grifo['Ruta'])
            excel_file = pd.ExcelFile(ruta_completa)
            hojas_totales = def_procesar_listado_hojas(excel_file.sheet_names, mes)
            
            # 1. Filtramos las hojas por el criterio (ej. el día "15")
            hojas_candidatas = [h for h in hojas_totales if filtro_hojas_fn(h)] if filtro_hojas_fn else hojas_totales

            if not hojas_candidatas and fecha_esperada:
                print(f"[❌ ERROR] El dia {fecha_esperada} no existe para el grifo {grifo['Grifo']}")
                continue

            for hoja in hojas_candidatas:
                # 2. Aquí recuperamos tu validación de fecha completa
                if fecha_esperada and hoja['fecha_correcta'] != fecha_esperada:
                    print(f"[❌ ERROR] La fecha {fecha_esperada} no coincide con {hoja['fecha_correcta']} en {grifo['Grifo']}")
                    continue

                venta_dto = def_Leer_parte_diario(
                    ruta_completa, 
                    grifo['Grifo'], 
                    hoja['fecha_correcta'], 
                    hoja['libro']
                )
                list_ventas_procesadas.append(venta_dto)
        # print(json.dumps(list_ventas_procesadas, indent=4, default=lambda o: o.__dict__))
        if list_ventas_procesadas:
            def_escribir_parte_diario(list_ventas_procesadas, GLOBAL_FILE_REGISTRO_VENTAS)

    except Exception as e:
        print(f"[❌ ERROR] Ocurrió un error inesperado: {e}")
    finally:
        fin = time.time()
        print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio, fin)}")
        print("\n==============================================================================")

# --- Así quedarían tus funciones llamadas por el Menu ---

def def_procesar_hoy(dia, mes, fecha):
    # Pasamos la 'fecha' para que la función base la valide
    ejecutar_proceso_base(mes, lambda h: h['dia'] == dia, fecha_esperada=fecha)

def def_procesar_por_dia(dia, mes):
    # Aquí no validamos fecha completa, solo el número de día
    ejecutar_proceso_base(mes, lambda h: h['dia'] == dia)

def def_procesar_por_mes(mes):
    # Procesa todo el mes sin filtros específicos
    ejecutar_proceso_base(mes)