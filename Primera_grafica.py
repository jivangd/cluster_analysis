# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:35:08 2024

@author: usuario1
"""
import matplotlib.pyplot as plt
import pandas as pd


#URL de la gráfica : https://www.nytimes.com/2023/04/27/learning/whats-going-on-in-this-graph-may-3-2023.html
df = pd.read_csv('Average_time.csv') #Url del dataset https://www.baseball-reference.com/leagues/majors/misc.shtml#teams_standard_misc
df.info() #Observamos que la columna Time no esta en tipo date

df['Time'] = pd.to_datetime(df['Time'], format='%H:%M') #La convertimos a fecha para poder manipular mejor los datos

# Creamos el gráfico de series de tiempo con Matplotlib
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Time'], marker='o')

# Cambiar el color para la línea entre 2022 y 2023
plt.plot(df['Year'][1:3], df['Time'][1:3], marker='o', color='yellow')
plt.title('Average Game Duration (1980-2024)')
plt.grid(True)
plt.xticks(df['Year'][4::10], rotation=45) #Va de 10 en 10 el eje x empezando por 1980
plt.tight_layout()

# Agregar etiquetas para los puntos de interés
plt.text(2022, df['Time'][2], '2022', ha='center', va='bottom')
plt.text(2023, df['Time'][1], '2023', ha='center', va='bottom')

# Anotar la duración promedio por partido en 2022 y 2023
plt.annotate(df['Time'][2].strftime('%H:%M:%S'), (2022, df['Time'][2]), textcoords="offset points", xytext=(-20,-15), ha='center')
plt.annotate(df['Time'][1].strftime('%H:%M:%S'), (2023, df['Time'][1]), textcoords="offset points", xytext=(25,15), ha='center')

# Establecer el límite inferior del eje Y a las 02:15 para homologar con la imagen
plt.ylim(pd.Timestamp('1900-01-01 02:15:00'), pd.Timestamp('1900-01-01 03:15:00'))

plt.show()
