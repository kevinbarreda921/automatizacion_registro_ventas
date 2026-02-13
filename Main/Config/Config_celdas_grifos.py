config_celdas_grifos = {
    'BRASIL': [
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '32. BRASIL',  'Dato': 'Hoja_registro_ventas'},
        {'ReadNum': 12,     'ReadLetra': 'P'  ,'Write': 'C',  'Dato': 'Total_venta_acumulada'},
        {'ReadNum': 8,      'ReadLetra': 'P'  ,'Write': 'D',  'Dato': 'Venta_GPL'},
        {'ReadNum': 9,      'ReadLetra': 'P'  ,'Write': 'E',  'Dato': 'Venta_GNV'},
        {'ReadNum': 28,     'ReadLetra': 'P'  ,'Write': 'F',  'Dato': 'Recaudo_Cofide_GNV'},
        {'ReadNum': 17,     'ReadLetra': 'P'  ,'Write': 'AO', 'Dato': 'Total_Tarjeta_de_Credito_Liquidos'},
        {'ReadNum': 18,     'ReadLetra': 'P'  ,'Write': 'AP', 'Dato': 'Total_Tarjeta_de_Credito_GLP'},
        {'ReadNum': 19,     'ReadLetra': 'P'  ,'Write': 'AQ', 'Dato': 'Total_Tarjeta_de_Credito_GNV'},
        {'ReadNum': 29,     'ReadLetra': 'P'  ,'Write': 'BY', 'Dato': 'Gastos'},
        {'ReadNum': 31,     'ReadLetra': 'P'  ,'Write': 'AY', 'Dato': 'Ventas_con_transferencia'},
        {'ReadNum': '',     'ReadLetra': 'Q'  ,'Write': '',   'Dato': 'Tipo_Hermes'},
        {'ReadNum': '',     'ReadLetra': 'O'  ,'Write': '',   'Dato': 'Importe_Hermes'},
        {'ReadNum': 'AUTO', 'ReadLetra': 'O'  ,'Write': 'AX', 'Dato': 'Hermes_monto_liquido'},
        {'ReadNum': 'AUTO','ReadLetra': 'O'   ,'Write': 'BD', 'Dato': 'Hermes_monto_GLP'},
        {'ReadNum': 'AUTO', 'ReadLetra': 'O'  ,'Write': 'BE', 'Dato': 'Hermes_monto_GNV1'},
        {'ReadNum': 'AUTO', 'ReadLetra': 'O'  ,'Write': 'BF', 'Dato': 'Hermes_monto_GNV2'}
    ],
    'PUENTE PIEDRA': [
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '01. PUENTE P.',  'Dato': 'Hoja_registro_ventas'},
        {'ReadNum': 11,     'ReadLetra': 'P'  ,'Write': 'C',  'Dato': 'Total_venta_acumulada'},
        {'ReadNum': 8,      'ReadLetra': 'P'  ,'Write': 'D',  'Dato': 'Venta_GPL'},
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '',   'Dato': 'Venta_GNV'},
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '',   'Dato': 'Recaudo_Cofide_GNV'},
        {'ReadNum': 16,     'ReadLetra': 'P'  ,'Write': 'AK', 'Dato': 'Total_Tarjeta_de_Credito_Liquidos'},
        {'ReadNum': 17,     'ReadLetra': 'P'  ,'Write': 'AL', 'Dato': 'Total_Tarjeta_de_Credito_GLP'},
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '',   'Dato': 'Total_Tarjeta_de_Credito_GNV'},
        {'ReadNum': 28,     'ReadLetra': 'P'  ,'Write': 'BN', 'Dato': 'Gastos'},
        {'ReadNum': 30,     'ReadLetra': 'P'  ,'Write': 'AP', 'Dato': 'Ventas_con_transferencia'},
        {'ReadNum': '',     'ReadLetra': 'Q'  ,'Write': '',   'Dato': 'Tipo_Hermes'},
        {'ReadNum': '',     'ReadLetra': 'O'  ,'Write': '',   'Dato': 'Importe_Hermes'},
        {'ReadNum': 'AUTO', 'ReadLetra': 'O'  ,'Write': 'AT', 'Dato': 'Hermes_monto_liquido'},
        {'ReadNum': 'AUTO', 'ReadLetra': 'O'  ,'Write': 'BA', 'Dato': 'Hermes_monto_GLP'},
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '',   'Dato': 'Hermes_monto_GNV1'},
        {'ReadNum': '',     'ReadLetra': ''   ,'Write': '',   'Dato': 'Hermes_monto_GNV2'}
    ]
}

# REVISAR POSISION
 #{'ReadNum': 30,     'ReadLetra': 'P'  ,'Write': 'AP', 'Dato': 'Ventas_con_transferencia'},


# config_celdas_grifos = {
#     'BRASIL': [
#         {'Fila': '32. BRASIL',  'Dato': 'Hoja_registro_ventas'},
#         {'Fila': 'C',  'Dato': 'Total_venta_acumulada'},
#         {'Fila': 'D',  'Dato': 'Venta_GPL'},
#         {'Fila': 'E',  'Dato': 'Venta_GNV'},
#         {'Fila': 'F',  'Dato': 'Recaudo_Cofide_GNV'},
#         {'Fila': 'AO', 'Dato': 'Total_Tarjeta_de_Credito_Liquidos'},
#         {'Fila': 'AP', 'Dato': 'Total_Tarjeta_de_Credito_GLP'},
#         {'Fila': 'AQ', 'Dato': 'Total_Tarjeta_de_Credito_GNV'},
#         {'Fila': 'BY', 'Dato': 'Gastos'},
#         {'Fila': 'AY', 'Dato': 'Ventas_con_transferencia'},
#         {'Fila': 'AX', 'Dato': 'Hermes_monto_liquido'},
#         {'Fila': 'BD', 'Dato': 'Hermes_monto_GLP'},
#         {'Fila': 'BE', 'Dato': 'Hermes_monto_GNV1'},
#         {'Fila': 'BF', 'Dato': 'Hermes_monto_GNV2'}
#     ],
#     'PUENTE PIEDRA': [
#         {'Fila': '01. PUENTE P.',  'Dato': 'Hoja_registro_ventas'},
#         {'Fila': 'C',  'Dato': 'Total_venta_acumulada'},
#         {'Fila': 'D',  'Dato': 'Venta_GPL'},
#         {'Fila': '',  'Dato': 'Venta_GNV'},
#         {'Fila': '',  'Dato': 'Recaudo_Cofide_GNV'},
#         {'Fila': 'AK', 'Dato': 'Total_Tarjeta_de_Credito_Liquidos'},
#         {'Fila': 'AL', 'Dato': 'Total_Tarjeta_de_Credito_GLP'},
#         {'Fila': '', 'Dato': 'Total_Tarjeta_de_Credito_GNV'},
#         {'Fila': 'BN', 'Dato': 'Gastos'},
#         {'Fila': 'AV', 'Dato': 'Ventas_con_transferencia'},
#         {'Fila': 'AT', 'Dato': 'Hermes_monto_liquido'},
#         {'Fila': 'BA', 'Dato': 'Hermes_monto_GLP'},
#         {'Fila': '', 'Dato': 'Hermes_monto_GNV1'},
#         {'Fila': '', 'Dato': 'Hermes_monto_GNV2'}
#     ]
    
# }
