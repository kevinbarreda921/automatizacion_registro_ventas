import pandas as pd
from Main.Entity.VentaDTO import Venta 

def def_Leer_parte_diario(Ruta_excel, dia_a_procesar):
    
    df = pd.read_excel(Ruta_excel, sheet_name=dia_a_procesar, header=None)
    # print("[INFO] Obteniendo Data...")
    
    Venta_DTO=Venta()
    Venta_DTO.Dia=dia_a_procesar

    # Data venta Liquidos, GLP, GNV, Cofide
    Venta_DTO.Total_venta_acumulada = float(str(df.iloc[11, 15]).replace(",", ""))
    Venta_DTO.Venta_GPL = float(str(df.iloc[7, 15]).replace(",", ""))
    Venta_DTO.Venta_GNV = float(str(df.iloc[8, 15]).replace(",", ""))
    
    Venta_DTO.Total_Tarjeta_de_Credito_Liquidos = float(str(df.iloc[16, 15]).replace(",", "").replace("-", ""))
    Venta_DTO.Total_Tarjeta_de_Credito_GLP = float(str(df.iloc[17, 15]).replace(",", "").replace("-", ""))
    Venta_DTO.Total_Tarjeta_de_Credito_GNV = float(str(df.iloc[18, 15]).replace(",", "").replace("-", ""))
    
    Venta_DTO.Recaudo_Cofide_GNV = float(str(df.iloc[27, 15]).replace(",", ""))
    Venta_DTO.Gastos = float(str(df.iloc[28, 15]).replace(",", ""))
    Venta_DTO.Ventas_con_transferencia = float(str(df.iloc[30, 15]).replace(",", ""))
    
    # Data Hermes
    Venta_DTO.Hermes_monto_liquido = float(0)
    Venta_DTO.Hermes_monto_GLP = float(0)
    Venta_DTO.Hermes_monto_GNV1 = float(0)
    Venta_DTO.Hermes_monto_GNV2 = float(0)
    Hermes_contar_gnv = int(0)
    contador_hermes = 120
    Buscar_tabla_hermes=0
    while True:
        Buscar_tabla_hermes+=1
        contador_hermes+=1
        tipo_combustible = str(df.iloc[contador_hermes, 16])
        if(Buscar_tabla_hermes==10):
            continue
        else:
            if(tipo_combustible=='TIPO'):
                contador_hermes+=1
                for i in range(4):
                    tipo_combustible = str(df.iloc[contador_hermes, 16])
                    tipo_combustible_precio = float(str(df.iloc[contador_hermes, 14]).replace(",", ""))
                    if tipo_combustible == "Líquido":
                        Venta_DTO.Hermes_monto_liquido = tipo_combustible_precio
                    elif tipo_combustible == "GLP":
                        Venta_DTO.Hermes_monto_GLP = tipo_combustible_precio
                    elif tipo_combustible == "GNV":
                        Hermes_contar_gnv += 1
                        if Hermes_contar_gnv == 1:
                            Venta_DTO.Hermes_monto_GNV1 = tipo_combustible_precio
                        else:
                            Venta_DTO.Hermes_monto_GNV2 = tipo_combustible_precio
                    else:
                        print(f"[ \u274C ERROR] Se cambio el formato para tabla hermes")
                    contador_hermes = contador_hermes + 1
                break
            
    # Total crédito
    Lista_clientes_credito = []
    Contador_credito = 14
    
    if str(df.iloc[Contador_credito, 0]) != "nan":
        while True:
            Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", "")).strip()
            if Contador_credito == 14:
                Cliente_credito_total = float(str(df.iloc[Contador_credito, 6]).replace(",", ""))
                Lista_clientes_credito.append(
                    {"cliente": Cliente_credito, "monto": Cliente_credito_total}
                )
            else:
                if Cliente_credito == "":
                    break
                encontrado = False
                Cliente_credito_total = float(str(df.iloc[Contador_credito, 6]).replace(",", ""))
                for Lista in Lista_clientes_credito:
                    if Lista["cliente"] == Cliente_credito:
                        Lista["monto"] = round(
                            Lista["monto"] + Cliente_credito_total, 2
                        )
                        encontrado = True
                        break
                if not encontrado:
                    Lista_clientes_credito.append(
                        {"cliente": Cliente_credito, "monto": Cliente_credito_total}
                    )
            Contador_credito += 1

    # Total Padel
    Contador_credito += 1
    Cliente_credito = " "
    Cliente_credito_total = 0

    if str(df.iloc[Contador_credito, 0]) != "nan":
        while True:
            Cliente_credito = str(df.iloc[Contador_credito, 0].replace("  ", "")).strip()
            if Cliente_credito == "":
                break
            encontrado = False
            Cliente_credito_total = float(str(df.iloc[Contador_credito, 6]).replace(",", ""))
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
        Venta_DTO.agregar_cliente_credito(Lista['cliente'],Lista['monto'])

    return Venta_DTO        
