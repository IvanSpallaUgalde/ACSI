import csv
from decimal import Decimal

name_doc = "cpu_mem_usage.txt"
name_csv = "cpu_mem_usage.csv"
def process_cpu_line(line):
    # Separa la línea en partes usando los espacios como delimitador
    partes = line.split()
    # Busca los índices de los elementos relevantes
    indice_idle = partes.index("id,")
    # Extrae los valores de User, System e Idle
    idle = partes[indice_idle - 1].replace(',', '.')
    # Calcula el valor de Global
    global_value = (Decimal(100.0) - Decimal(idle))
    # Devuelve los valores procesados
    return global_value

def process_mem_line(line):
    # Separa la linea en partes usando los espacios como delimitador
    partes = line.split()
    # Obtener los valores que buscamos
    capacidad_total = partes[3].replace(',', '.')
    capacidad_usada = partes[7].replace(',', '.')
    mem_usada = round((Decimal(float(capacidad_usada))/Decimal(float(capacidad_total)))*100, 2)


    return capacidad_usada, mem_usada


with open(name_doc, "r") as input:
    lines = input.readlines()

with open(name_csv, "w", newline="") as output:
    writer = csv.writer(output)

    writer.writerow(["Timestamp", "% global CPU", "Used mem", "% Used mem"])
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

print(f"Los datos se han guardado en {name_csv}")