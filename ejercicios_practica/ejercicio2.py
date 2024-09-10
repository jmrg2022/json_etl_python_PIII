# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Ing. Jesús González 
# # Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt

def bar_plot(lista_userId,lista_completed):
    
    fig = plt.figure()
    fig.suptitle('Títulos completados por usuario', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(lista_userId, lista_completed, label='Cantidad de títulos')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

     # Crear el gráfico

    response = requests.get(url)
    data = json.loads(response.text)
    data = response.json()

    lista_userId=[1,2,3,4,5,6,7,8,9,10]
    lista_completed=[]

    for i in lista_userId:
        suma = 0
        for user in data:
            if user['userId'] == i and user['completed'] == True:
                suma = suma + 1
        lista_completed.append(suma)
        
    #print(lista_completed)        

    bar_plot(lista_userId,lista_completed)

    print("terminamos")