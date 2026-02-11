import Main.Config.Config_file as config_grifos


def def_obtener_config_grifo(nombre_grifo):
    registros = config_grifos.config_grifos.get(nombre_grifo)
    if not registros:
        return None
    
    objeto_mapeo = {item['Dato']: item['Fila'] for item in registros}
    
    return objeto_mapeo
