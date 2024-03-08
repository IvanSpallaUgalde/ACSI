import csv

input_name = "mem_usage.txt"
output_name = "mem_usage.csv"


def process_line(line):
    parts = line.split()
    timestamp = parts[0] + " " + parts[1]

    free_mem = parts[2]

    used_mem = parts[3]

    mem_percent = parts[4]

    return timestamp, free_mem, used_mem, mem_percent

with open(input_name, "r") as input:
    lines = input.readlines()

with open(output_name, "w") as output:
    writer = csv.writer(output)

    writer.writerow(["Timestamp", "Capacidad disponible(KB)", "Capacidad utilizada(KB)", "% Memoria utilizada"])

    for line in lines:
        timestamp, free_mem, used_mem, mem_percent = process_line(line)
        writer.writerow([timestamp, free_mem, used_mem, mem_percent])

print(f"Conversion de {input_name} a {output_name} exitosa")