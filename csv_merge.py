import os
#import pandas as pd
import csv

# Ruta de la carpeta que contiene los archivos CSV
carpeta = r'C:\Python\trabajo3\archivos'

# Lista para almacenar todos los dataframes de los archivos CSV
data = []
datas = []
encabezado = []

# Recorrer la carpeta y leer cada archivo CSV
for archivo in os.listdir(carpeta):
    if archivo.endswith('.csv'):
        data = []
        ruta_completa = os.path.join(carpeta, archivo)

        with open(ruta_completa, newline="\n") as archivo:
            arch_csv = csv.reader(archivo)
            for fila in arch_csv:
                data.append(fila)
            if len(encabezado)==0: 
                encabezado = data[0]
            del(data[0])
    datas.extend(data)
datas.insert(0,encabezado)

# Guardar el dataframe final en un nuevo archivo CSV

with open('archivo_final.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",",quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(datas)