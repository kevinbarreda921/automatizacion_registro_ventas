import pandas as pd

df = pd.read_excel(
    "Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx",
    sheet_name="21.01.26",
    header=None,
)

Total_venta_acumulada = float(str(df.iloc[11, 15]).replace(",", ""))
print(f"Venta_GNV : {Total_venta_acumulada}")

Venta_GPL = float(str(df.iloc[7, 15]).replace(",", ""))
Venta_GNV = float(str(df.iloc[8, 15]).replace(",", ""))
print(f"Venta_GPL : {Venta_GPL}")
print(f"Venta_GNV : {Venta_GNV}")


Total_Tarjeta_de_Credito_Liquidos = float(
    str(df.iloc[16, 15]).replace(",", "").replace("-", "")
)
Total_Tarjeta_de_Credito_GLP = float(
    str(df.iloc[17, 15]).replace(",", "").replace("-", "")
)
Total_Tarjeta_de_Credito_GNV = float(
    str(df.iloc[18, 15]).replace(",", "").replace("-", "")
)

print(f"Total_Tarjeta_de_Credito_Liquidos : {Total_Tarjeta_de_Credito_Liquidos}")
print(f"Total_Tarjeta_de_Credito_GLP : {Total_Tarjeta_de_Credito_GLP}")
print(f"Total_Tarjeta_de_Credito_GNV : {Total_Tarjeta_de_Credito_GNV}")
print(f"Venta_GNV : {Total_Tarjeta_de_Credito_Liquidos+Total_Tarjeta_de_Credito_GLP}")

Recaudo_Cofide_GNV = float(str(df.iloc[27, 15]).replace(",", ""))
Gastos = float(str(df.iloc[28, 15]).replace(",", ""))
print(f"Recaudo_Cofide_GNV : {Recaudo_Cofide_GNV}")
print(f"Gastos : {Gastos}")

Hermes_monto_liquido = float(0)
Hermes_monto_GLP = float(0)
Hermes_monto_GNV = float(0)

contador_hermes = 124

for i in range(4):
    tipo_combustible = str(df.iloc[contador_hermes, 16])
    tipo_combustible_precio = float(str(df.iloc[contador_hermes, 14]).replace(",", ""))
    if tipo_combustible == "Líquido":
        Hermes_monto_liquido = tipo_combustible_precio
    elif tipo_combustible == "GLP":
        Hermes_monto_GLP = tipo_combustible_precio
    elif tipo_combustible == "GNV":
        Hermes_monto_GNV = Hermes_monto_GNV + tipo_combustible_precio
    else:
        print(f"Error: Se cambio el formato para tabla hermes")
    contador_hermes = contador_hermes + 1

print(f"Hermes_monto_liquido : {Hermes_monto_liquido}")
print(f"Hermes_monto_GLP : {Hermes_monto_GLP}")
print(f"Hermes_monto_GNV : {Hermes_monto_GNV}")

# Venta_credito_cliente = str(df.iloc[18, 0])
# print(f"Venta_credito_cliente : {Venta_credito_cliente}")

# Total crédito
Lista_clientes_credito = []
Contador_credito = 14

if str(df.iloc[Contador_credito, 0]) != "nan":
    while True:
        Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", "")).strip()

        Cliente_credito_total = float(
            str(df.iloc[Contador_credito, 6]).replace(",", "")
        )
        if Contador_credito == 14:
            Lista_clientes_credito.append(
                {"cliente": Cliente_credito, "monto": Cliente_credito_total}
            )
        else:
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
                    {"cliente": Cliente_credito, "monto": Cliente_credito_total}
                )
        Contador_credito += 1

for Lista in Lista_clientes_credito:
    print(f"Lista_clientes_credito : {Lista}")

# Total Padel
Lista_clientes_padel = []
Contador_credito += 1
Cliente_credito = " "
Cliente_credito_total = 0

if str(df.iloc[Contador_credito, 0]) != "nan":
    while True:
        Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", "")).strip()
        Cliente_credito_total = float(
            str(df.iloc[Contador_credito, 6]).replace(",", "")
        )
        if Cliente_credito == " ":
            break
        encontrado = False
        for Lista in Lista_clientes_padel:
            if Lista["cliente"] == Cliente_credito:
                Lista["monto"] = round(Lista["monto"] + Cliente_credito_total, 2)
                encontrado = True
                break
        if not encontrado:
            Lista_clientes_padel.append(
                {"cliente": Cliente_credito, "monto": Cliente_credito_total}
            )
        Contador_credito += 1

for Lista in Lista_clientes_padel:
    print(f"Lista_clientes_padel : {Lista}")
