from Main.BusinessLogic import Process
import time
from Main.Services.Date_Timer import def_mostrar_tiempo

inicio = time.time()

# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","23.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","22.01.26")
Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","21.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","20.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","19.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","18.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","17.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","16.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","15.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","14.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","13.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","12.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","11.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","10.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","09.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","08.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","07.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","06.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","05.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","04.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","03.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","02.01.26")
# Process.def_RunProcess("Main/Grifos/brasil/21.01.26/PARTE DIARIO -SIGES- 3ENERO- BRASIL.xlsx","01.01.26")

fin = time.time()

print(f"Tiempo de ejecución: {def_mostrar_tiempo(inicio,fin)}")



