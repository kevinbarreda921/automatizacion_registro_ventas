import pandas as pd

# Dias = ["21.01.26","20.01.26","19.01.26","18.01.26","17.01.26","16.01.26","15.01.26",
#         "14.01.26","13.01.26","12.01.26","11.01.26","10.01.26","09.01.26","08.01.26",
#         "07.01.26","06.01.26","05.01.25","04.01.26","03.01.26","02.01.26","01.01.26"]
Dias = ["21.01.26"]

Ruta_excel = "Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx"
Lista_clientes_credito = []

for li in Dias:
    print(f"Procesando día: {li}")
    df = pd.read_excel(Ruta_excel, sheet_name=li, header=None)
    
    Contador_credito = 14

    while Contador_credito < len(df):
        valor_actual = df.iloc[Contador_credito, 0]

        # REGLA: Si la celda actual está vacía...
        if pd.isna(valor_actual) or str(valor_actual).strip() == "":
            
            # ...verificamos si hay una fila siguiente
            if Contador_credito + 1 < len(df):
                valor_siguiente = df.iloc[Contador_credito + 1, 0]
                
                # Si la siguiente TAMBIÉN está vacía, paramos por completo el día
                if pd.isna(valor_siguiente) or str(valor_siguiente).strip() == "":
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
    print(f"Cliente encontrado: {cliente}")