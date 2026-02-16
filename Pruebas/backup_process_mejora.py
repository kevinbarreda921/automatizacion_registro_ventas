import time
import os
import pandas as pd
from Main.Entity.VentaDTO import Venta
from Main.Services.SaleReader import def_Leer_parte_diario
from Main.Services.SaleWrite import def_escribir_parte_diario
from Main.Services.Date_Timer import def_mostrar_tiempo
from Main.Config.Global_parameters import GLOBAL_FILE_REGISTRO_VENTAS, GLOBAL_FILE_PARTE_DIARIO
from Main.Services.SaleConfig import def_obtener_archivos_siges, def_procesar_listado_hojas

def ejecutar_proceso_base(mes, filtro_hojas_fn=None):
    """
    Función genérica para evitar repetir bloques try-except y bucles de archivos.
    filtro_hojas_fn: Una función lambda para filtrar las hojas (por día, fecha, etc.)
    """
    inicio = time.time()
    list_ventas_procesadas = []
    print("\n\n[INICIO] PROCESO INICIADO")

    try:
        lista_grifos = def_obtener_archivos_siges(GLOBAL_FILE_PARTE_DIARIO)
        if not lista_grifos:
            return

        for grifo in lista_grifos:
            ruta_completa = os.path.join(GLOBAL_FILE_PARTE_DIARIO, grifo['Ruta'])
            
            if not os.path.exists(ruta_completa):
                print(f"[❌ ERROR] No existe: {grifo['Ruta']}")
                continue

            excel_file = pd.ExcelFile(ruta_completa)
            hojas_totales = def_procesar_listado_hojas(excel_file.sheet_names, mes)
            
            # Aplicamos el filtro (si existe) o procesamos todo el mes
            hojas_a_procesar = filter(filtro_hojas_fn, hojas_totales) if filtro_hojas_fn else hojas_totales

            for hoja in hojas_a_procesar:
                venta_dto = def_Leer_parte_diario(
                    ruta_completa, 
                    grifo['Grifo'], 
                    hoja['fecha_correcta'], 
                    hoja['libro']
                )
                list_ventas_procesadas.append(venta_dto)

        if list_ventas_procesadas:
            def_escribir_parte_diario(list_ventas_procesadas, GLOBAL_FILE_REGISTRO_VENTAS)
            print(f"[SUCCESS] Se procesaron {len(list_ventas_procesadas)} registros.")

    except Exception as e:
        print(f"[❌ ERROR] Error inesperado: {str(e)}")
    finally:
        fin = time.time()
        print(f"[FIN] Tiempo total: {def_mostrar_tiempo(inicio, fin)}")

# --- Funciones específicas ahora son muy cortas ---

def def_procesar_hoy(dia, mes, fecha_completa):
    # Filtra solo la hoja que coincida con el día y la fecha exacta
    filtro = lambda h: h['dia'] == dia and h['fecha_correcta'] == fecha_completa
    ejecutar_proceso_base(mes, filtro)

def def_procesar_por_dia(dia, mes):
    # Filtra por el número de día
    filtro = lambda h: h['dia'] == dia
    ejecutar_proceso_base(mes, filtro)

def def_procesar_por_mes(mes):
    # No hay filtro, procesa todo el listado de hojas_totales
    ejecutar_proceso_base(mes)