from datetime import date

def def_obtener_fecha_actual():
    return date.today()

def def_mostrar_tiempo(inicio,fin):
    segundos_totales =  fin-inicio
    m, s = divmod(segundos_totales, 60)
    h, m = divmod(m, 60)
    
    if h > 0:
        return f"{int(h)} Hora con {int(m)} Minutos y {s:.2f} Segundos"
    elif m > 0:
        return f"{int(m)} Minutos {s:.2f} Segundos"
    else:
        return f"{s:.4f} Segundos"

