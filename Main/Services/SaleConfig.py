import Main.Config.Config_celdas_grifos as config_celdas

def def_obtener_config_celdas_grifo(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['Fila'] for item in registros}
    
    return objeto_mapeo
