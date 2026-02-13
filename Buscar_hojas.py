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
    for l in nombres_hojas:
        print(f"{l}")
    
    

        

