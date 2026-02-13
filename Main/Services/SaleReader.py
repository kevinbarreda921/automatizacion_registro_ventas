import pandas as pd
from Main.Entity.VentaDTO import Venta 
from Main.Services.SaleConfig import def_obtener_celdas_a_leer_letra,def_obtener_celdas_a_leer_numero


def def_Leer_parte_diario(Ruta_excel,Grifo,dia_a_procesar):
    
    df = pd.read_excel(Ruta_excel, sheet_name=dia_a_procesar, header=None)
    # print("[INFO] Obteniendo Data...")
    df.columns = generar_letras_excel(len(df.columns))
    
    Venta_DTO=Venta()
    Venta_DTO.Grifo=Grifo
    
    Venta_DTO.Dia=dia_a_procesar
    
    ConfigColumReadNumero = def_obtener_celdas_a_leer_numero(Grifo)
    ConfigColumReadLetra = def_obtener_celdas_a_leer_letra(Grifo)
    # Data venta Liquidos, GLP, GNV, Cofide
    if(ConfigColumReadLetra['Total_venta_acumulada']!=''):
        Venta_DTO.Total_venta_acumulada = float(str(df.loc[ConfigColumReadNumero['Total_venta_acumulada']-1, ConfigColumReadLetra['Total_venta_acumulada']]).replace(",", "").replace("-", ""))
    if(ConfigColumReadLetra['Venta_GPL']!=''):
        Venta_DTO.Venta_GPL = float(str(df.loc[ConfigColumReadNumero['Venta_GPL']-1, ConfigColumReadLetra['Venta_GPL']]).replace(",", ""))
    if(ConfigColumReadLetra['Venta_GNV']!=''):
        Venta_DTO.Venta_GNV = float(str(df.loc[ConfigColumReadNumero['Venta_GNV']-1, ConfigColumReadLetra['Venta_GNV']]).replace(",", ""))
    if(ConfigColumReadLetra['Total_Tarjeta_de_Credito_Liquidos']!=''):
        Venta_DTO.Total_Tarjeta_de_Credito_Liquidos = float(str(df.loc[ConfigColumReadNumero['Total_Tarjeta_de_Credito_Liquidos']-1, ConfigColumReadLetra['Total_Tarjeta_de_Credito_Liquidos']]).replace(",", "").replace("-", ""))
    if(ConfigColumReadLetra['Total_Tarjeta_de_Credito_GLP']!=''):
        Venta_DTO.Total_Tarjeta_de_Credito_GLP = float(str(df.loc[ConfigColumReadNumero['Total_Tarjeta_de_Credito_GLP']-1, ConfigColumReadLetra['Total_Tarjeta_de_Credito_GLP']]).replace(",", "").replace("-", ""))
    if(ConfigColumReadLetra['Total_Tarjeta_de_Credito_GNV']!=''):
        Venta_DTO.Total_Tarjeta_de_Credito_GNV = float(str(df.loc[ConfigColumReadNumero['Total_Tarjeta_de_Credito_GNV']-1, ConfigColumReadLetra['Total_Tarjeta_de_Credito_GNV']]).replace(",", "").replace("-", ""))
    
    if(ConfigColumReadLetra['Recaudo_Cofide_GNV']!=''):
        Venta_DTO.Recaudo_Cofide_GNV = float(str(df.loc[ConfigColumReadNumero['Recaudo_Cofide_GNV']-1, ConfigColumReadLetra['Recaudo_Cofide_GNV']]).replace(",", ""))
    if(ConfigColumReadLetra['Gastos']!=''):
        Venta_DTO.Gastos = float(str(df.loc[ConfigColumReadNumero['Gastos']-1, ConfigColumReadLetra['Gastos']]).replace(",", "").replace("-", ""))
    #LEER Error de Máquina		0.00	0.00 FILA 27 COLUMNA 15   VALOR 26
    # PONERLO EN AV
    if(ConfigColumReadLetra['Ventas_con_transferencia']!=''):
        Venta_DTO.Ventas_con_transferencia = float(str(df.loc[ConfigColumReadNumero['Ventas_con_transferencia']-1, ConfigColumReadLetra['Ventas_con_transferencia']]).replace(",", ""))
    
    # Data Hermes
    Venta_DTO.Hermes_monto_liquido = float(0)
    Venta_DTO.Hermes_monto_GLP = float(0)
    Venta_DTO.Hermes_monto_GNV1 = float(0)
    Venta_DTO.Hermes_monto_GNV2 = float(0)
    Hermes_contar_gnv= float(0)
    contador_buscar_cuadro_hermes = 55

    while True:
        contador_buscar_cuadro_hermes+=1
        if(contador_buscar_cuadro_hermes==400):
            print(f"[ \u274C ERROR] No existe cuadro Hermes")
            continue
        else:
            tipo_combustible = str(df.loc[contador_buscar_cuadro_hermes, ConfigColumReadLetra['Tipo_Hermes']])
            if(tipo_combustible=='TIPO'):
                contador_buscar_cuadro_hermes+=1
                while True:
                    
                    tipo_combustible = str(df.loc[contador_buscar_cuadro_hermes, ConfigColumReadLetra['Tipo_Hermes']])
                    if (tipo_combustible!='nan'):
                        tipo_combustible_precio = float(str(df.loc[contador_buscar_cuadro_hermes, ConfigColumReadLetra['Importe_Hermes']]).replace(",", ""))
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
                            print(f"[ \u274C ERROR] Nuevo combustible de cuadro Hermes")
                        contador_buscar_cuadro_hermes+=1
                    else:
                        break
            else:
                continue
                    
        break

    contador_buscar_tabla_credito_padel = 10
    while True:
        contador_buscar_tabla_credito_padel+=1
        if(contador_buscar_tabla_credito_padel==15):
            print(f"[ \u274C ERROR] No existe cuadro Hermes")
            continue
        else:
            Buscar_tabla_credito = str(df.iloc[contador_buscar_tabla_credito_padel, 0])
            if(Buscar_tabla_credito=='CLIENTE'):
                contador_buscar_tabla_credito_padel+=1
                
                # Total crédito
                Lista_clientes_credito = []
                Contador_credito = contador_buscar_tabla_credito_padel
                
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
                            
            else:
                continue
                    
        break            
            
    return Venta_DTO        


def generar_letras_excel(n):
    letras = []
    # Esto genera A, B... Z, AA, AB...
    for i in range(1, n + 1):
        col = ""
        while i > 0:
            i, rem = divmod(i - 1, 26)
            col = chr(65 + rem) + col
        letras.append(col)
    return letras