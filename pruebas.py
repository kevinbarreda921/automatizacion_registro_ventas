
class Experiencia:
    def __init__(self, nombre_empresa, cargo):
        self.nombre_empresa = nombre_empresa
        self.cargo = cargo
        
class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        # Inicializamos la lista aquí, igual que en el constructor de C#
        self.experiencias = [] 

    def agregar_experiencia(self, empresa, cargo_ocupado):
        # Creamos el objeto 'detalle' y lo metemos en la lista
        nueva_exp = Experiencia(empresa, cargo_ocupado)
        self.experiencias.append(nueva_exp)
        
# 1. Creamos al empleado (Cabecera)
empleado = Empleado("Ana García", "Senior Developer")

# 2. Agregamos detalles a su lista interna
empleado.agregar_experiencia("Google", "Junior Dev")
empleado.agregar_experiencia("Netflix", "Mid Dev")

# 3. Accedemos a los datos
print(f"Empleado: {empleado.nombre}")
print("Historial Laboral:")

for exp in empleado.experiencias:
    print(f"- Empresa: {exp.nombre_empresa}, Cargo: {exp.cargo}")
    