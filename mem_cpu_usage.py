import subprocess
import time

# Número de iteraciones
iterations = 2400  # Puedes ajustar este valor según sea necesario

# Abrir un archivo para escribir la salida combinada de todas las iteraciones
with open('cpu_mem_usage.txt', 'w') as output_file:
    # Bucle para ejecutar el comando 'top -b -n1' y guardar la salida en el archivo
    for i in range(iterations):
        # Ejecutar el comando 'top -b -n1' en bash
        result = subprocess.run(['top', '-b', '-n1'], capture_output=True, text=True)

        # Obtener la salida del comando
        output_lines = result.stdout.split('\n')

        # Filtrar y guardar solo las líneas que contienen '%Cpu(s)' o 'MiB Mem'
        filtered_lines = [line for line in output_lines if '%Cpu(s)' in line or 'MiB Mem' in line]

        # Timestamp
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        output_file.write(f'timestamp: {timestamp}\n')
        # Escribir las líneas filtradas en el archivo
        output_file.write('\n'.join(filtered_lines))
        output_file.write("\n")

        # Esperar 3 segundos antes de la próxima iteración
        time.sleep(3)

print(f"Los datos se han guardado en cpu_mem_usage.txt")
