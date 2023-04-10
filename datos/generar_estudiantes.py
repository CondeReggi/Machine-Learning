from faker import Faker
import random
import os

fake = Faker()

dir_actual = os.getcwd()
ruta_archivo = os.path.join(dir_actual, 'datos.csv')

with open(ruta_archivo, 'w') as file:
    # Escribimos la cabecera del archivo

    file.write('Nombre,Edad,Sexo,Nota\n')
    for i in range(500):
        nombre = fake.name()
        edad = random.randint(18, 40)
        sexo = random.choice(['M', 'F'])
        nota = round(random.uniform(0,10), 2)
        file.write(f'{nombre},{edad},{sexo},{nota}\n')