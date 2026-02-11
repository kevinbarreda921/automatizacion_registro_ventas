import pandas as pd

Lista_grifos_credito=[
"Main/Grifos/brasil/leercreditos/01 PARTE DIARIO ENERO 2026 EDS CATACAOS.xlsx",
"Main/Grifos/brasil/leercreditos/01 PARTE DIARIO ENERO 2026 PUENTE PIEDRA.xlsx",
"Main/Grifos/brasil/leercreditos/14 VIRU  SIGES  ENERO 2026.xlsx",
"Main/Grifos/brasil/leercreditos/50 TULIS  ENERO 2026.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE DIARIA SIGES - QUISTOCOCHA ENERO 2026.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE DIARIO 3 ENERO 2026-ENACE.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE DIARIO 3 ENERO BRASIL.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE DIARIO ACAPULCO-ENERO.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE_DIARIO_MAKITA 2026.xlsx",
"Main/Grifos/brasil/leercreditos/PARTE_DIARIO_SAN PABLO ENERO 2026.xlsx",
"Main/Grifos/brasil/leercreditos/R.PARTE DIARIO ENERO 2026-CHILCA.xlsx",
"Main/Grifos/brasil/leercreditos/REPORTE PARTE DIARIO VELITA  ENERO 2026.xlsx",
"Main/Grifos/brasil/leercreditos/REPORTE SIGES ENERO 2026-HUANCHACO.xlsx",
"Main/Grifos/brasil/leercreditos/REPORTE SIGES MARIAEUGUENIA-ENERO.xlsx",
"Main/Grifos/brasil/leercreditos/REPORTE SIGES SAN MARCOS-ENERO.xlsx"
]

# # Cargamos el objeto Excel sin leer los datos aún
for list in Lista_grifos_credito:
    print(list)
    excel_file = pd.ExcelFile(list)
    nombres_hojas = excel_file.sheet_names
    Lista_clientes_credito = []
    for l in nombres_hojas:
        # print(f"Procesando día: {li}")
        df = pd.read_excel(list, sheet_name=l, header=None)
    
        Contador_credito = 14
    
        while Contador_credito < len(df):
            valor_actual = df.iloc[Contador_credito, 0]
    
            # REGLA: Si la celda actual está vacía...
            if pd.isna(valor_actual) or str(valor_actual).strip() == "":
    
                # ...verificamos si hay una fila siguiente
                if Contador_credito + 1 < len(df):
                    valor_siguiente = df.iloc[Contador_credito + 1, 0]
    
                    # Si la siguiente TAMBIÉN está vacía, paramos por completo el día
                    if pd.isna(valor_siguiente) or str(valor_siguiente).strip().replace("  ", "") == "":
                        break 
                    else:
                        # Si la siguiente tiene datos, saltamos la actual y seguimos
                        Contador_credito += 1
                        continue
                else:
                    # Si no hay fila siguiente, simplemente paramos
                    break
    
            # --- PROCESAMIENTO NORMAL ---
            Cliente_credito = str(valor_actual).strip()
    
            if not any(c["cliente"] == Cliente_credito for c in Lista_clientes_credito):
                Lista_clientes_credito.append({"cliente": Cliente_credito})
    
            Contador_credito += 1
        
        # Imprimir resultados
    for cliente in Lista_clientes_credito:
        print(f"- : {cliente}")


