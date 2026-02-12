import openpyxl
import pandas as pd
from datetime import datetime
from Main.Entity.VentaDTO import Venta
import json
import Main.Config.Config_credit_grifos as Config_credit_grifos
from Main.Services.SaleConfig import def_obtener_config_celdas_grifo

def def_escribir_parte_diario(List_ventas_procesadas,FILE_REGISTRO_VENTAS):
    # Buscar Fila para insertar datos
    Venta_DTO=Venta()
    
    wb = openpyxl.load_workbook(FILE_REGISTRO_VENTAS)
    for venta in List_ventas_procesadas:
        Venta_DTO=venta
        print(f"[INFO] Registrando data:{Venta_DTO.Dia}")
        
        ConfigColumna = def_obtener_config_celdas_grifo('BRASIL')
        
        df = pd.read_excel(
            FILE_REGISTRO_VENTAS,
            sheet_name=ConfigColumna['Hoja_registro_ventas'],
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

        if (Fila_insert==0):
            print("[ \u274C ERROR] No existe el día a registrar")
        else:
            
            nombre_hoja = ConfigColumna['Hoja_registro_ventas']
            sheet = wb[nombre_hoja]
            
            Campo_VentaLiquidos = ConfigColumna['Total_venta_acumulada'] + str(Fila_insert)
            Campo_venta_glp = ConfigColumna['Venta_GPL'] + str(Fila_insert)
            Campo_venta_gnv = ConfigColumna['Venta_GNV'] + str(Fila_insert)
            Campo_venta_rec_cofide = ConfigColumna['Recaudo_Cofide_GNV'] + str(Fila_insert)
            
            sheet[Campo_VentaLiquidos] = '='+str(Venta_DTO.Total_venta_acumulada)+'-'+Campo_venta_glp+'-'+Campo_venta_gnv
            sheet[Campo_venta_glp] = Venta_DTO.Venta_GPL
            sheet[Campo_venta_gnv] = Venta_DTO.Venta_GNV
            sheet[Campo_venta_rec_cofide] = Venta_DTO.Recaudo_Cofide_GNV        
            Campo_Total_Tarjeta_de_Credito_Liquidos = ConfigColumna['Total_Tarjeta_de_Credito_Liquidos'] + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GLP = ConfigColumna['Total_Tarjeta_de_Credito_GLP'] + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GNV = ConfigColumna['Total_Tarjeta_de_Credito_GNV'] + str(Fila_insert)        
            sheet[Campo_Total_Tarjeta_de_Credito_Liquidos] = Venta_DTO.Total_Tarjeta_de_Credito_Liquidos
            sheet[Campo_Total_Tarjeta_de_Credito_GLP] = Venta_DTO.Total_Tarjeta_de_Credito_GLP
            sheet[Campo_Total_Tarjeta_de_Credito_GNV] = Venta_DTO.Total_Tarjeta_de_Credito_GNV        
            if Venta_DTO.Gastos != 0.0:
                Campo_Gastos = ConfigColumna['Gastos'] + str(Fila_insert)
                #PONERLO PUENTE PIDRA EN BN
                sheet[Campo_Gastos] = Venta_DTO.Gastos
            
            if Venta_DTO.Ventas_con_transferencia != 0.0:
                Campo_Ventas_con_transferencia = ConfigColumna['Ventas_con_transferencia'] + str(Fila_insert)
                sheet[Campo_Ventas_con_transferencia] = Venta_DTO.Ventas_con_transferencia        
            Campo_Hermes_monto_liquido = ConfigColumna['Hermes_monto_liquido'] + str(Fila_insert)
            Campo_Hermes_monto_GLP = ConfigColumna['Hermes_monto_GLP'] + str(Fila_insert)
            Campo_Hermes_monto_GNV1 = ConfigColumna['Hermes_monto_GNV1'] + str(Fila_insert)
            Campo_Hermes_monto_GNV2 = ConfigColumna['Hermes_monto_GNV2'] + str(Fila_insert)        
            sheet[Campo_Hermes_monto_liquido] = Venta_DTO.Hermes_monto_liquido
            sheet[Campo_Hermes_monto_GLP] = Venta_DTO.Hermes_monto_GLP
            sheet[Campo_Hermes_monto_GNV1] = Venta_DTO.Hermes_monto_GNV1
            sheet[Campo_Hermes_monto_GNV2] = Venta_DTO.Hermes_monto_GNV2        
            
            for Lista in Venta_DTO.ListClienteCredito:
                registro = next((u for u in Config_credit_grifos.Lista_credito_brasil if u["CLiente"] == Lista.Cliente), None)
                if(registro!=None):
                    Campo_dinamico = registro['Fila'] + str(Fila_insert)
                    sheet[Campo_dinamico] = Lista.Monto        
    
    wb.save(FILE_REGISTRO_VENTAS)
    
    
    


