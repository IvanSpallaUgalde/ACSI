import subprocess
import time

# Nombre del archivo de salida
nombre_archivo = "cpu_usage.txt"

# Abre el archivo en modo escritura
with open(nombre_archivo, "w") as archivo:
    # Ejecuta el comando y captura la salida en un bucle durante 20 iteraciones
    for _ in range(20):
        # Ejecuta el comando y captura la salida
        proceso = subprocess.Popen(["top", "-b", "-n1"], stdout=subprocess.PIPE)
        salida = subprocess.check_output(["grep", "-i", "%Cpu(s)"], stdin=proceso.stdout)
        proceso.wait()  # Espera a que el proceso termine

        # Obtiene el timestamp actual
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())

        # Escribe el timestamp y la salida en el archivo
        archivo.write(f"{timestamp} {salida.decode('utf-8')}")

        # Espera 2 segundos antes de la próxima muestra. El intervalo minimo es 1.84
        time.sleep(2)

print(f"Los resultados se han guardado en {nombre_archivo}")
