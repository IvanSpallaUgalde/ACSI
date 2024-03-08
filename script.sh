#!/bin/bash

# Ejecuta los scripts de Python
python3 cpu_usage.py
python3 cpu_usage_converter.py

python3 mem_usage.py
python3 mem_usage_converter.py

python3 mem_cpu_usage.py
python3 cpu_mem_usage_converter.py

# Mover a los subdirectorios

mv cpu_usage.txt txt/
mv mem_usage.txt txt/
mv cpu_mem_usage.txt txt/

mv cpu_usage.csv csv/
mv mem_usage.csv csv/
mv cpu_mem_usage.csv csv/
