import csv
from decimal import Decimal, getcontext

# Ajuste de los decimales para manejar floats
getcontext().prec=2

# Nombre del archivo de entrada y salida
nombre_archivo_entrada = "cpu_usage.txt"
nombre_archivo_salida = "cpu_usage.csv"

def process_idle(idle):
    parts = idle.split(',')
    resp = ""
    for part in parts:
        if part == "ni":
            pass
        else:
            resp = resp + f"{part}."

    resp = resp[:len(resp)-1]
    return resp

# Función para procesar una línea de la salida y extraer los valores
def procesar_linea(linea):
    # Separa la línea en partes usando los espacios como delimitador
    partes = linea.split()
    # El primer elemento es el timestamp
    timestamp = partes[0] + " " + partes[1]
    # Busca los índices de los elementos relevantes
    indice_user = partes.index("us,")
    indice_system = partes.index("sy,")
    indice_idle = partes.index("id,")
    # Extrae los valores de User, System e Idle
    user = partes[indice_user - 1]
    system = partes[indice_system - 1]
    idle = partes[indice_idle - 1]
    idle = process_idle(idle)
    # Calcula el valor de Global
    idle = float(idle)
    global_value = (Decimal(100.0) - Decimal(idle))
    global_value = str(global_value).replace(".",",")
    # Devuelve los valores procesados
    return timestamp, user, system, global_value

# Abre el archivo de entrada y lee las líneas
with open(nombre_archivo_entrada, "r") as entrada:
    lineas = entrada.readlines()

# Abre el archivo de salida CSV y escribe los datos procesados
with open(nombre_archivo_salida, "w", newline="") as salida_csv:
    escritor_csv = csv.writer(salida_csv)
    # Escribe la cabecera del CSV
    escritor_csv.writerow(["Timestamp", "User", "System", "Global"])
    # Procesa cada línea y escribe los datos en el CSV
    for linea in lineas:
        # Procesa la línea
        timestamp, user, system, global_value = procesar_linea(linea)
        # Escribe los valores en el archivo CSV
        escritor_csv.writerow([timestamp, user, system, global_value])

print(f"Conversion de {nombre_archivo_entrada} a {nombre_archivo_salida} exitosa")
