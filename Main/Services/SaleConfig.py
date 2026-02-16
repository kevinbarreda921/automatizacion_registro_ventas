import Main.Config.Config_celdas_grifos as config_celdas
import re
import Main.Config.Config_celdas_grifos as Config_celdas_grifos
import os
from Main.Config.Global_parameters import GLOBAL_ANIO

def def_obtener_celdas_a_escribir(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['Write'] for item in registros}
    
    return objeto_mapeo

def def_obtener_celdas_a_leer_letra(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['ReadLetra'] for item in registros}
    
    return objeto_mapeo
def def_obtener_celdas_a_leer_numero(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['ReadNum'] for item in registros}
    
    return objeto_mapeo

def def_obtener_archivos_siges(ruta_carpeta):
    lista_grifos_a_procesar = []
    try:
        Listado_grifos = list(Config_celdas_grifos.config_celdas_grifos.keys())
        
        archivos = os.listdir(ruta_carpeta)
        print(f"\n[INFO] Analizando archivos en: {ruta_carpeta}\n")
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

                datos_grifo = {
                    'Grifo': lugar_detectado.upper(),
                    'Ruta': nombre_archivo
                    }
                lista_grifos_a_procesar.append(datos_grifo)
            else:
                print(f"[\u274C ERROR] NO REGISTRADO: El archivo '{nombre_archivo}' no coincide con ninguna palabra clave")
        if lista_grifos_a_procesar:
            print(f"\n[INFO] Archivos a procesar {len(lista_grifos_a_procesar)}:")
            for lst in lista_grifos_a_procesar:
                print(f"[INFO]: ✅ El archivo '{lst['Ruta']}' es un registro de [{lst['Grifo']}]")
            print(f"\n")
        return lista_grifos_a_procesar
    except FileNotFoundError:
        print("Error: No se encontró la carpeta especificada.")

def def_procesar_listado_hojas(hojas,mes_param):
    lista_resultado = []
    anio_actual = GLOBAL_ANIO
    mm = str(mes_param).zfill(2)
    yy = str(anio_actual)[-2:]
    
    for hoja in hojas:
        hoja = hoja.strip()
        if not hoja: continue
        
        fecha_normalizada = None
        dia_fecha = None
        # 1. CASO: TEXTO + FECHA (ej: SIGES 01-01-2026) -> Extraer y convertir
        # Busca patrones como DD-MM-YYYY, DD.MM.YY, etc.
        match_fecha = re.search(r'(\d{1,2})[-./](\d{1,2})[-./](\d{2,4})', hoja)
        if match_fecha:
            d, m, y = match_fecha.groups()
            fecha_normalizada = f"{d.zfill(2)}.{m.zfill(2)}.{y[-2:]}"
            dia_fecha=d.zfill(2)
        
        # 2. CASO: DIA.MES.AÑO (ej: 01.01.26) -> Ya está correcto
        elif re.match(r'^\d{2}\.\d{2}\.\d{2}$', hoja):
            fecha_normalizada = hoja
            dia_fecha=re.match(r'^\d{2}\$', hoja)

        # 3. CASO: DIA-MES (ej: 01-01) -> Completar con año
        elif re.match(r'^\d{1,2}-\d{1,2}$', hoja):
            dia, mes = hoja.split('-')
            fecha_normalizada = f"{dia.zfill(2)}.{mes.zfill(2)}.{yy}"
            dia_fecha=dia.zfill(2)
            
        # 4. CASO: SOLO DIA (ej: 05) -> Completar con mes y año
        elif re.match(r'^\d{1,2}$', hoja):
            fecha_normalizada = f"{hoja.zfill(2)}.{mm}.{yy}"
            dia_fecha=hoja.zfill(2)
        # Si logramos normalizar la fecha, la guardamos con su nombre original
        if fecha_normalizada:
            lista_resultado.append({
                "dia":dia_fecha,
                "fecha_correcta": fecha_normalizada,
                "libro": hoja
            })
            
    return lista_resultado