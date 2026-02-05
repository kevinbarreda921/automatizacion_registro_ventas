
import pandas as pd

# Dias = ["21.01.26","20.01.26","19.01.26","18.01.26","17.01.26","16.01.26","15.01.26","14.01.26","13.01.26","12.01.26","11.01.26","10.01.26","09.01.26","08.01.26","07.01.26","06.01.26","05.01.25","04.01.26","03.01.26","02.01.26","01.01.26"]

Dias = ["21.01.26"]
# ,"06.01.26","05.01.26","04.01.26","03.01.26","02.01.26","01.01.26"
Ruta_excel="Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx"
Lista_clientes_credito = []

for li in Dias:
    # print("dia procesado: "+li)
    df = pd.read_excel(Ruta_excel, sheet_name=li, header=None)
    
    Contador_credito = 14

    if str(df.iloc[Contador_credito, 0]) != "nan":
        while True:
            Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", ""))
            Cliente_credito_total = float(
                str(df.iloc[Contador_credito, 6]).replace(",", "")
            )
            if Contador_credito == 14:
                Lista_clientes_credito.append(
                    {"fecha":li,"cliente": Cliente_credito, "monto": Cliente_credito_total}
                )
            else:
                if Cliente_credito == " ":
                    break
                encontrado = False
                for Lista in Lista_clientes_credito:
                    if Lista["cliente"] == Cliente_credito:
                        Lista["monto"] = round(
                            Lista["monto"] + Cliente_credito_total, 2
                        )
                        encontrado = True
                        
                if not encontrado:
                    Lista_clientes_credito.append(
                        {"fecha":li,"cliente": Cliente_credito, "monto": Cliente_credito_total}
                    )
            Contador_credito += 1

    Contador_credito += 1
    Cliente_credito = " "
    Cliente_credito_total = 0

    if str(df.iloc[Contador_credito, 0]) != "nan":
        while True:
            Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", ""))
            Cliente_credito_total = float(
                str(df.iloc[Contador_credito, 6]).replace(",", "")
            )
            if Cliente_credito == " ":
                break
            encontrado = False
            for Lista in Lista_clientes_credito:
                if Lista["cliente"] == Cliente_credito:
                    Lista["monto"] = round(Lista["monto"] + Cliente_credito_total, 2)
                    encontrado = True
                    break
            if not encontrado:
                Lista_clientes_credito.append(
                    {"fecha":li,"cliente": Cliente_credito, "monto": Cliente_credito_total}
                )
            Contador_credito += 1
    
for Lista in Lista_clientes_credito:
    print(f"Lista_clientes_credito : {Lista}")
