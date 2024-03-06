import subprocess
import time

#Total mem K
total_mem = 15984224
def obtener_informacion_vmstat():
    # Ejecutar el comando vmstat y capturar la salida
    proceso = subprocess.Popen(['vmstat', '-s'], stdout=subprocess.PIPE)
    salida, _ = proceso.communicate()
    lineas = salida.decode().split('\n')

    # Recogemos la informacion en la quinta linea (K memoria libre)
    libre_line = lineas[4].split()
    utilizada_line = lineas[1].split()
    # timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    # Capacidad disponible
    capacidad_disponible = libre_line[0]
    # Capacidad usada
    capacidad_utilizada = utilizada_line[0]
    # Porcentaje de memoria utilizada
    porcentaje_memoria_utilizada = round((int(capacidad_utilizada) / total_mem)*100, 2)


    return timestamp, capacidad_disponible, capacidad_utilizada, porcentaje_memoria_utilizada


def guardar_resultados_en_archivo(nombre_archivo, num_iteraciones):
    with open(nombre_archivo, 'a') as archivo:
        for _ in range(num_iteraciones):
            # Obtener información vmstat
            timestamp, capacidad_disponible, capacidad_utilizada, porcentaje_memoria_utilizada = obtener_informacion_vmstat()

            # Escribir la información en el archivo
            archivo.write(f"{timestamp} {capacidad_disponible} {capacidad_utilizada} {porcentaje_memoria_utilizada}\n")
            archivo.flush()  # Para asegurarnos de que los datos se escriban inmediatamente

            # Esperar 5 segundos antes de volver a obtener información
            time.sleep(5)


nombre_archivo = 'mem_usage.txt'
num_iteraciones = 5
guardar_resultados_en_archivo(nombre_archivo, num_iteraciones)
