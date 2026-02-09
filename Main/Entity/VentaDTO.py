from Main.Entity.ClienteCreditoDTO import ClienteCredito

class Venta:
    def __init__(self, 
                    Dia='',
                    Total_venta_acumulada='', 
                    Venta_GPL='',
                    Venta_GNV='',
                    Total_Tarjeta_de_Credito_Liquidos='',
                    Total_Tarjeta_de_Credito_GLP='',
                    Total_Tarjeta_de_Credito_GNV='',
                    Recaudo_Cofide_GNV='',
                    Gastos='',
                    Ventas_con_transferencia='',
                    Hermes_monto_liquido='',
                    Hermes_monto_GLP='',
                    Hermes_monto_GNV1='',
                    Hermes_monto_GNV2=''):
        self.Dia=Dia
        self.Total_venta_acumulada = Total_venta_acumulada
        self.Venta_GPL = Venta_GPL
        self.Venta_GNV = Venta_GNV
        self.Total_Tarjeta_de_Credito_Liquidos = Total_Tarjeta_de_Credito_Liquidos
        self.Total_Tarjeta_de_Credito_GLP = Total_Tarjeta_de_Credito_GLP
        self.Total_Tarjeta_de_Credito_GNV = Total_Tarjeta_de_Credito_GNV
        self.Recaudo_Cofide_GNV = Recaudo_Cofide_GNV
        self.Gastos = Gastos
        self.Ventas_con_transferencia = Ventas_con_transferencia
        self.Hermes_monto_liquido = Hermes_monto_liquido
        self.Hermes_monto_GLP = Hermes_monto_GLP
        self.Hermes_monto_GNV1 = Hermes_monto_GNV1
        self.Hermes_monto_GNV2 = Hermes_monto_GNV2
        self.ListClienteCredito = [] 
        
    def agregar_cliente_credito(self, Cliente, Monto):
        nuevo_cliente = ClienteCredito(Cliente, Monto)
        self.ListClienteCredito.append(nuevo_cliente)
        
