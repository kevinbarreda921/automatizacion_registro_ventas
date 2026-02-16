from datetime import datetime 
import os
from Main.BusinessLogic.Process import def_procesar_hoy,def_procesar_por_dia,def_procesar_por_mes

def def_formatear_mes(entrada):
    try:
        mes = int(entrada)
        if 1 <= mes <= 12:
            return str(mes).zfill(2)
        else:
            return "Error: El mes debe estar entre 1 y 12."
    except ValueError:
        return "Error: Entrada no válida, por favor ingresa un mes."
    
def def_formatear_dia(entrada):
    try:
        mes = int(entrada)
        if 1 <= mes <= 31:
            return str(mes).zfill(2)
        else:
            return "Error: El día debe estar entre 1 y 31."
    except ValueError:
        return "Error: Entrada no válida, por favor ingresa un día."
    
def def_limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def def_run_menu():
    while True:
        BLUE = '\033[94m'
        RESET = '\033[0m'
        
        menu = f"""
        {BLUE}╔══════════════════════════════════════════╗
        ║             PANEL DE CONTROL             ║
        ╠══════════════════════════════════════════╣{RESET}
        1. Procesar Hoy ({datetime.now().strftime('%d.%m.%y')})
        2. Procesar Día
        3. Procesar Mes
        4. Salir
        {BLUE}╚══════════════════════════════════════════╝{RESET}
        """
        print(menu)
        
        opcion = input("Elige una opción (1-4): ")
        
        match opcion:
            # 1. Procesar Hoy
            case "1":
                try:
                    dia_actual = datetime.now().strftime('%d')
                    mes_actual = datetime.now().strftime('%m')
                    fecha_actual = datetime.now().strftime('%d.%m.%y')
                    print("\n==============================================================================\n")
                    print("[INICIO] PROCESO INICIADO")
                    print(F"[INFO] Procesar hoy : {fecha_actual}")                  
                    def_procesar_hoy(dia_actual,mes_actual,fecha_actual)
                except ValueError:
                    print("Error: Por favor ingresa números válidos.")
            # 2. Procesar Día        
            case "2":
                try:
                    entrada_dia = input("\nIngresa el día: ")
                    dia_sel = def_formatear_dia(entrada_dia)

                    if "Error" in dia_sel:
                        print(dia_sel)
                    else:
                        entrada_mes = input("Ingresa el mes: ")
                        mes_sel = def_formatear_mes(entrada_mes)
                        
                        if "Error" in mes_sel:
                            print(mes_sel)
                        else:
                            print("\n==============================================================================\n")
                            print("[INICIO] PROCESO INICIADO")
                            print(F"[INFO] Procesar Dia : {dia_sel}")    
                            def_procesar_por_dia(dia_sel,mes_sel)
                
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")
            # 3. Procesar Mes
            case "3":
                try:
                    mes = int(input("\nIngresa el mes: "))
                    mes_seleccionado = def_formatear_mes(mes)
                    if "Error" in mes_seleccionado:
                        print(mes_seleccionado)
                    else:
                        # print(mes_seleccionado)
                        print("\n==============================================================================\n")
                        print("[INICIO] PROCESO INICIADO")
                        print(F"[INFO] Procesar mes : {mes_seleccionado}")  
                        def_procesar_por_mes(mes_seleccionado)
                    
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")
            # 4. Salir
            case "4":
                print("Cerrando")
                break
            case _:
                print("Opción incorrecta")
                def_limpiar_consola()

