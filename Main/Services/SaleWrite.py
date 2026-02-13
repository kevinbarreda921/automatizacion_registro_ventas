import openpyxl
import pandas as pd
from datetime import datetime
from Main.Entity.VentaDTO import Venta
import json
import Main.Config.Config_credit_grifos as Config_credit_grifos
from Main.Services.SaleConfig import def_obtener_celdas_a_escribir

def def_escribir_parte_diario(List_ventas_procesadas,FILE_REGISTRO_VENTAS):
    # Buscar Fila para insertar datos
    Venta_DTO=Venta()
    
    wb = openpyxl.load_workbook(FILE_REGISTRO_VENTAS)
    for venta in List_ventas_procesadas:
        Venta_DTO=venta
        print(f"[INFO] Registrando {Venta_DTO.Grifo} del día {Venta_DTO.Dia}")
        
        ConfigColumnWrite = def_obtener_celdas_a_escribir(Venta_DTO.Grifo)
        
        df = pd.read_excel(
            FILE_REGISTRO_VENTAS,
            sheet_name=ConfigColumnWrite['Hoja_registro_ventas'],
            header=None,
        )
        Fila_insert = 0
        Fecha_Procesar=datetime.strptime(Venta_DTO.Dia, "%d.%m.%y").strftime("%Y-%m-%d")
    
        for t in range(420):
            try:
                valor_celda = df.iloc[t, 1]
    
                # Intentamos convertir solo esta celda
                fecha_dt = pd.to_datetime(valor_celda, errors='coerce')
                
                # Si la conversión fue exitosa (no es NaT)
                if pd.notnull(fecha_dt):
                    if fecha_dt.strftime('%Y-%m-%d') == Fecha_Procesar:
                        Fila_insert = t + 1
                        break
            except:
                break

        if (Fila_insert==0):
            print("[ \u274C ERROR] No existe el día a registrar")
        else:
            
            nombre_hoja = ConfigColumnWrite['Hoja_registro_ventas']
            sheet = wb[nombre_hoja]
            
            Campo_VentaLiquidos = ConfigColumnWrite['Total_venta_acumulada'] + str(Fila_insert)
            Campo_venta_glp = ConfigColumnWrite['Venta_GPL'] + str(Fila_insert)
            Campo_venta_gnv = ConfigColumnWrite['Venta_GNV'] + str(Fila_insert)
            Campo_venta_rec_cofide = ConfigColumnWrite['Recaudo_Cofide_GNV'] + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_Liquidos = ConfigColumnWrite['Total_Tarjeta_de_Credito_Liquidos'] + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GLP = ConfigColumnWrite['Total_Tarjeta_de_Credito_GLP'] + str(Fila_insert)
            Campo_Total_Tarjeta_de_Credito_GNV = ConfigColumnWrite['Total_Tarjeta_de_Credito_GNV'] + str(Fila_insert)  
            Campo_Gastos = ConfigColumnWrite['Gastos'] + str(Fila_insert)
            Campo_Ventas_con_transferencia = ConfigColumnWrite['Ventas_con_transferencia'] + str(Fila_insert)
            Campo_Hermes_monto_liquido = ConfigColumnWrite['Hermes_monto_liquido'] + str(Fila_insert)
            Campo_Hermes_monto_GLP = ConfigColumnWrite['Hermes_monto_GLP'] + str(Fila_insert)
            Campo_Hermes_monto_GNV1 = ConfigColumnWrite['Hermes_monto_GNV1'] + str(Fila_insert)
            Campo_Hermes_monto_GNV2 = ConfigColumnWrite['Hermes_monto_GNV2'] + str(Fila_insert)  

            if(ConfigColumnWrite['Total_venta_acumulada']!=''):
                sheet[Campo_VentaLiquidos] = '='+str(Venta_DTO.Total_venta_acumulada)+'-'+Campo_venta_glp+'-'+Campo_venta_gnv
            if(ConfigColumnWrite['Venta_GPL']!=''):
                sheet[Campo_venta_glp] = Venta_DTO.Venta_GPL
            if(ConfigColumnWrite['Venta_GNV']!=''):
                sheet[Campo_venta_gnv] = Venta_DTO.Venta_GNV
            if(ConfigColumnWrite['Recaudo_Cofide_GNV']!=''):
                sheet[Campo_venta_rec_cofide] = Venta_DTO.Recaudo_Cofide_GNV        
            if(ConfigColumnWrite['Total_Tarjeta_de_Credito_Liquidos']!=''):
                sheet[Campo_Total_Tarjeta_de_Credito_Liquidos] = Venta_DTO.Total_Tarjeta_de_Credito_Liquidos
            if(ConfigColumnWrite['Total_Tarjeta_de_Credito_GLP']!=''):
                sheet[Campo_Total_Tarjeta_de_Credito_GLP] = Venta_DTO.Total_Tarjeta_de_Credito_GLP
            if(ConfigColumnWrite['Total_Tarjeta_de_Credito_GNV']!=''):
                sheet[Campo_Total_Tarjeta_de_Credito_GNV] = Venta_DTO.Total_Tarjeta_de_Credito_GNV
            if(ConfigColumnWrite['Gastos']!=''):
                if Venta_DTO.Gastos != 0.0:
                    sheet[Campo_Gastos] = Venta_DTO.Gastos
            
            if(ConfigColumnWrite['Ventas_con_transferencia']!=''):
                if Venta_DTO.Ventas_con_transferencia != 0.0:
                    sheet[Campo_Ventas_con_transferencia] = Venta_DTO.Ventas_con_transferencia

            if(ConfigColumnWrite['Hermes_monto_liquido']!=''):
                sheet[Campo_Hermes_monto_liquido] = Venta_DTO.Hermes_monto_liquido
            if(ConfigColumnWrite['Hermes_monto_GLP']!=''):
                sheet[Campo_Hermes_monto_GLP] = Venta_DTO.Hermes_monto_GLP
            if(ConfigColumnWrite['Hermes_monto_GNV1']!=''):
                sheet[Campo_Hermes_monto_GNV1] = Venta_DTO.Hermes_monto_GNV1
            if(ConfigColumnWrite['Hermes_monto_GNV2']!=''):
                sheet[Campo_Hermes_monto_GNV2] = Venta_DTO.Hermes_monto_GNV2        
            
            if(Venta_DTO.Grifo=='BRASIL'):
                for Lista in Venta_DTO.ListClienteCredito:
                    registro = next((u for u in Config_credit_grifos.Lista_credito_brasil if u["CLiente"] == Lista.Cliente), None)
                    if(registro!=None):
                        Campo_dinamico = registro['Fila'] + str(Fila_insert)
                        sheet[Campo_dinamico] = Lista.Monto  
            else:
                for Lista in Venta_DTO.ListClienteCredito:
                    registro = next((u for u in Config_credit_grifos.Lista_credito_puentepiedra if u["CLiente"] == Lista.Cliente), None)
                    if(registro!=None):
                        Campo_dinamico = registro['Fila'] + str(Fila_insert)
                        sheet[Campo_dinamico] = Lista.Monto    
    
    wb.save(FILE_REGISTRO_VENTAS)
    
    
    


