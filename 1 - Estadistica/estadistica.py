import numpy as np
import math
import matplotlib.pyplot as plt

# calcular media
def calular_media_no_librerias(datos):
    suma = 0
    for numero in datos:
        suma += numero
    
    media = suma / len(datos)
    return media

def calcular_media_con_numpy(datos):
    media = np.mean(datos)
    return media

def dicionario_datos(datos):
    diccionario = {}
    for numero in datos:
        if numero in diccionario:
            diccionario[numero] += 1
        else:
            diccionario[numero] = 1
    return diccionario

def calular_mediana_no_librerias(datos):
    diccionario = dicionario_datos(datos)
    suma = 0
    
    for clave, valor in diccionario.items():
        suma += clave * valor

    return suma / len(datos)

def calcular_mediana_con_numpy(datos):
    media = np.median(datos)
    return media

def calular_moda_con_mumpy(datos):
    moda = np.mode(datos)
    return moda

def calcular_desviacion_estandar_con_mumpy(datos):
    desv_est = np.std(datos)
    return desv_est

def calcular_desviacion_estandar(datos):
    diccionario = dicionario_datos(datos)
    suma = 0
    for numero in datos:
        valor = numero - (diccionario(numero) / len(datos))
        suma += math.pow(valor, 2)

    return math.sqrt( suma / len(datos) )

def calcular_percentil(datos, numero):
    numero = np.percentile(datos, numero)
    return numero

def crear_histograma(datos):
    plt.hist(datos, bins=10)
    plt.show()

# Generamos una muestra aleatoria de datos
datos = np.random.normal(loc=5, scale=2, size=100)

print(f"La media es: (Sin librerias) { calular_media_no_librerias(datos) }")
print(f"La media es: (Con librerias) { calcular_media_con_numpy(datos) }")
print("\n")

print(f"La mediana es: (Sin librerias) { calular_mediana_no_librerias(datos) }")
print(f"La mediana es: (Con librerias) { calcular_mediana_con_numpy(datos) }")
print("\n")

print(f"La moda es: { calular_moda_con_mumpy(datos) }")
print("\n")

print(f"La desviación estándar es: (Sin librerias) { calcular_desviacion_estandar(datos) }")
print(f"La desviación estándar es: (Con librerias) { calcular_desviacion_estandar_con_mumpy(datos) }")
print("\n")

for numero in datos:
    print(f"El percentil { numero } es: { calcular_percentil(datos, numero) }")
    print("\n")

crear_histograma(datos)