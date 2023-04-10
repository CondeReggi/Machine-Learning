import pandas as pd
from estadistica import calular_media_no_librerias, calular_mediana_no_librerias, calcular_desviacion_estandar, calcular_percentil, crear_histograma

df = pd.read_csv('C:\Develop\Machine Learning\Machine-Learning\datos\datos.csv');

print(df.head())

# for numero in df['Nota']:
#     print(numero)

print("Media:", df['Nota'].mean())
print("Mediana:", df['Nota'].median())
print("Desviación estándar:", df['Nota'].std())

print("\n")

print("Media mia:", calular_media_no_librerias(df['Nota']))
print("Mediana mia:", calular_mediana_no_librerias(df['Nota']))
print("Desviación estándar mia:", calcular_desviacion_estandar(df['Nota']))