import Main.Config.Config_celdas_grifos as config_celdas

def def_obtener_celdas_a_escribir(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['Write'] for item in registros}
    
    return objeto_mapeo

def def_obtener_celdas_a_leer_letra(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['ReadLetra'] for item in registros}
    
    return objeto_mapeo
def def_obtener_celdas_a_leer_numero(nombre_grifo):
    registros = config_celdas.config_celdas_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['ReadNum'] for item in registros}
    
    return objeto_mapeo