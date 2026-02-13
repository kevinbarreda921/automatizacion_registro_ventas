import pandas as pd
import re
import json

Lista_grifos_credito=[
"Main/Grifos/brasil/leercreditos/14 VIRU  SIGES  ENERO 2026.xlsx"
]
def procesar_listado_hojas(hojas,mes_param):
    lista_resultado = []
    anio_actual = "2026"
    # Formateamos mes y año para asegurar 2 dígitos (ej: '01' y '26')
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



mes_param='02'
# # Cargamos el objeto Excel sin leer los datos aún
for list in Lista_grifos_credito:
    print(list)
    excel_file = pd.ExcelFile(list)
    nombres_hojas = excel_file.sheet_names
    resultado = procesar_listado_hojas(nombres_hojas,mes_param)
    # print(json.dumps(resultado, indent=2))
    
    for ss in resultado:
        print(ss['dia'])
        print(ss['fecha_correcta'])
        print(ss['libro'])
        print("--------------")
    

    



