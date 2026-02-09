import openpyxl
import pandas as pd
from datetime import datetime
from Main.Entity.VentaDTO import Venta
import json

def def_escribir_parte_diario(List_ventas_procesadas):
    # Buscar Fila para insertar datos
    Venta_DTO=Venta()
    
    wb = openpyxl.load_workbook("Main/Grifos/brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx")
    for venta in List_ventas_procesadas:
        Venta_DTO=venta
        print(f"[INFO] Registrando data:{Venta_DTO.Dia}")

        df = pd.read_excel(
            "Main/Grifos/brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx",
            sheet_name="32. BRASIL",
            header=None,
        )
        Fila_insert = 0
        Fecha_Procesar=datetime.strptime(Venta_DTO.Dia, "%d.%m.%y").strftime("%Y-%m-%d")
    
        for t in range(420):
            try:
                t += 5
                Buscar_Fecha = str(df.iloc[t, 1].date())
                if Buscar_Fecha == Fecha_Procesar:
                    Fila_insert = t + 1
                    break
            except:
                break

        if (Fila_insert==420):
            print("[ \u274C ERROR] No existe el día a registrar")
        else:
            nombre_hoja = "32. BRASIL"
            sheet = wb[nombre_hoja]
            
            Campo_VentaLiquidos = "C" + str(Fila_insert)
            Campo_venta_glp = "D" + str(Fila_insert)
            Campo_venta_gnv = "E" + str(Fila_insert)
            Campo_venta_rec_cofide = "F" + str(Fila_insert)
            
            sheet[Campo_VentaLiquidos] = '='+str(Venta_DTO.Total_venta_acumulada)+'-'+Campo_venta_glp+'-'+Campo_venta_gnv
            sheet[Campo_venta_glp] = Venta_DTO.Venta_GPL
            sheet[Campo_venta_gnv] = Venta_DTO.Venta_GNV
            sheet[Campo_venta_rec_cofide] = Venta_DTO.Recaudo_Cofide_GNV        
            Campo_Total_Tarjeta_de_Credito_Liquidos = "AO" + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GLP = "AP" + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GNV = "AQ" + str(Fila_insert)        
            sheet[Campo_Total_Tarjeta_de_Credito_Liquidos] = Venta_DTO.Total_Tarjeta_de_Credito_Liquidos
            sheet[Campo_Total_Tarjeta_de_Credito_GLP] = Venta_DTO.Total_Tarjeta_de_Credito_GLP
            sheet[Campo_Total_Tarjeta_de_Credito_GNV] = Venta_DTO.Total_Tarjeta_de_Credito_GNV        
            if Venta_DTO.Gastos != 0.0:
                Campo_Gastos = "BY" + str(Fila_insert)
                sheet[Campo_Gastos] = Venta_DTO.Gastos
            
            if Venta_DTO.Ventas_con_transferencia != 0.0:
                Campo_Ventas_con_transferencia = "AY" + str(Fila_insert)
                sheet[Campo_Ventas_con_transferencia] = Venta_DTO.Ventas_con_transferencia        
            Campo_Hermes_monto_liquido = "AX" + str(Fila_insert)
            Campo_Hermes_monto_GLP = "BD" + str(Fila_insert)
            Campo_Hermes_monto_GNV1 = "BE" + str(Fila_insert)
            Campo_Hermes_monto_GNV2 = "BF" + str(Fila_insert)        
            sheet[Campo_Hermes_monto_liquido] = Venta_DTO.Hermes_monto_liquido
            sheet[Campo_Hermes_monto_GLP] = Venta_DTO.Hermes_monto_GLP
            sheet[Campo_Hermes_monto_GNV1] = Venta_DTO.Hermes_monto_GNV1
            sheet[Campo_Hermes_monto_GNV2] = Venta_DTO.Hermes_monto_GNV2        
            Lista_credito_brasil = [
                {'Fila':'H','CLiente':'COMMUNICATIONS AND SYSTEMS DEVELOPMENT SOCIEDAD ANONIMA CERRADA'},
                {'Fila':'I','CLiente':'FUERO MILITAR POLICIAL'},
                {'Fila':'J','CLiente':'ALMACENES ASOCIADOS SOCIEDAD ANONIMA CERRADA'},
                {'Fila':'L','CLiente':'C & M SERVICENTROS SOCIEDAD ANONIMA CERRADA'},
                {'Fila':'N','CLiente':'FONDO NACIONAL DE DESARROLLO PESQUERO'},
                {'Fila':'T','CLiente':'RED DE COMBUSTIBLES LIQUIDOS SAC REDCOL SAC'},
                {'Fila':'U','CLiente':'UNIDAD EJECUTORA 004 - FONDO DE COOPERACION PARA EL DESARROLLO SOCIAL'},
                {'Fila':'V','CLiente':'MUNICIPALIDAD DE JESUS MARIA'},
                {'Fila':'Y','CLiente':'SEGURO INTEGRAL DE SALUD'},
                {'Fila':'AC','CLiente':'INSTITUTO NACIONAL DE SALUD DEL NIñO'},
                {'Fila':'AL','CLiente':'ALMACENERA MERCANTIL SOCIEDAD COMERCIAL DE RESPONSABILIDAD LIMITADA'}
            ]
            # for s in Lista_clientes_credito:
            #     print(s)
            for Lista in Venta_DTO.ListClienteCredito:
                registro = next((u for u in Lista_credito_brasil if u["CLiente"] == Lista.Cliente), None)
                if(registro!=None):
                    Campo_dinamico = registro['Fila'] + str(Fila_insert)
                    sheet[Campo_dinamico] = Lista.Monto        
    
    wb.save("Main/Grifos/brasil/REGISTRO VENTAS -  2026- 01 (1).xlsx")


