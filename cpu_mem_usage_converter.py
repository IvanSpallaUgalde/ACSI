import csv
from decimal import Decimal, getcontext

factor = (2**20/10**6)

getcontext().prec=2

name_doc = "cpu_mem_usage.txt"
name_csv = "cpu_mem_usage.csv"


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


def process_cpu_line(line):
    # Separa la línea en partes usando los espacios como delimitador
    partes = line.split()
    # Busca los índices de los elementos relevantes
    indice_idle = partes.index("id,")
    # Extrae los valores de User, System e Idle
    idle = partes[indice_idle - 1]
    idle = process_idle(idle)
    idle = float(idle)
    # Calcula el valor de Global
    global_value = (Decimal(100.0) - Decimal(idle))
    # Devuelve los valores procesados
    return global_value

def process_mem_line(line):
    # Separa la linea en partes usando los espacios como delimitador
    partes = line.split()
    # Obtener los valores que buscamos
    capacidad_total = partes[3].replace(',', '.')
    capacidad_total = round((float(capacidad_total) * factor)*1000,2)
    capacidad_usada = partes[7].replace(',', '.')
    capacidad_usada = round((float(capacidad_usada) * factor)*1000,2)
    mem_usada = Decimal(float(capacidad_usada)/float(capacidad_total))*100


    return capacidad_usada, mem_usada


with open(name_doc, "r") as input:
    lines = input.readlines()

with open(name_csv, "w", newline="") as output:
    writer = csv.writer(output)

    writer.writerow(["Timestamp", "% global CPU", "Used mem(KB)", "% Used mem"])
    for i in range(0, len(lines), 3):
        # Get the timestamp
        timestamp_row = lines[i].split()
        timestamp = timestamp_row[1]

        # Get the %Cpu usage
        cpu_usage = process_cpu_line(lines[i+1])

        # Get memory data

        used_memory, used_memory_100 = process_mem_line(lines[i + 2])

        # Write data
        writer.writerow([timestamp, cpu_usage, used_memory, used_memory_100])

print(f"Conversion de {name_doc} a {name_csv} exitosa")