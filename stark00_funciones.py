from data_stark import lista_personajes

#TP STARK 00

"""
Nombre y apellido: Osorio Brenda
Division: 113
Profesores: Christian Baus, 

"""

#------------------------------------------------------


"""Consignas:

A. Analizar detenidamente el set de datos
I. Ordenar el código implementando una función para cada uno de los valores
informados.
"""

   

"""B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe"""

def imprimir_informacion_superheroe(lista: list, clave: str):
    """Funcion que nos imprime por consola un dato especifico de cada super heroes de la lista


    Args:
        lista (list): La lista se compone 
        de diccionarios que contienen informacion de cada super heroe. por ejemplo
        nombre, altura, inteligencia, fuerza, empresa, etc. 
    """

    for i in range(len(lista)):
        print(lista[i][clave])


#imprimir_informacion_superheroe(lista_personajes, "nombre")

#_________________________________________________________________________________________________

"""C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo"""

def nombre_y_altura(lista:list):

    for i in range(len(lista)):
        print(lista[i]["nombre"], lista[i]["altura"])

# nombre_y_altura(lista_personajes)

#__________________________________________________________________________________________________

"""D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)"""

def calcular_maximo(lista: list, clave: str)-> float:
    puerta_maximo = True
    maximo = None

    for i in range(len(lista)):
        if puerta_maximo == True:
            puerta_maximo = False
            maximo = float(lista[i][clave])
        
        else:
            if maximo < float(lista[i][clave]):
                maximo = float(lista[i][clave])
                puerta_maximo = False

    return maximo

#_______________________________________________________________________________________________

"""E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)"""

def calcular_minimo(lista: list, clave: str)-> float:
    puerta_minimo = True
    minimo = None

    for i in range(len(lista)):
        if puerta_minimo == True:
            puerta_minimo = False
            minimo = float(lista[i][clave])
        
        else:
            if minimo > float(lista[i][clave]):
                minimo = float(lista[i][clave])
                puerta_minimo = False

    return minimo

# print(calcular_minimo(lista_personajes, "altura")) 
# print(calcular_maximo(lista_personajes, "altura"))

#_________________________________________________________________________________________
        
"""F. Recorrer la lista y determinar la altura promedio de los superhéroes'
(PROMEDIO)"""

def totalizar_datos(lista:list, clave:str) ->int:
    cantidad = len(lista)
    total = 0
    
    for i in range(cantidad):
        numero = float(lista[i][clave])
        total = total + numero
    return total


def promediar_datos(lista: list):
    largo_lista = len(lista)
    total = totalizar_datos(lista, "altura")

    promedio = total / largo_lista

    return promedio

# print(totalizar_datos(lista_personajes, "altura"))
# print(promediar_datos(lista_personajes))

#___________________________________________________________________________________

"""G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)"""

def nombre_maximo_minimo(lista: list, clave:str, maximo: bool = True):
    total_indices = len(lista)

    if maximo == True: 
        calculo = calcular_maximo(lista, clave)

    else:
        calculo = calcular_minimo(lista, clave)
    
    for i in range(total_indices):
        if float(lista[i][clave]) == calculo:
            print(F"El nombre del superheroe más alto es {lista[i]["nombre"]} y mide {lista[i][clave]}")
    
    
    
# print(nombre_maximo_minimo(lista_personajes, "altura", True))

#____________________________________________________________________________________________________________

"""H. Calcular e informar cual es el superhéroe más y menos pesado."""


def mas_pesado(lista: list, clave: str):
    total_indices = len(lista)
    calculo = calcular_maximo(lista, clave)
    
    for i in range(total_indices):
        if float(lista[i][clave]) == calculo:
            print(F" El nombre del superheroe más pesado es {lista[i]["nombre"]} y pesa {lista[i][clave]}")
    
    

#print(mas_pesado(lista_personajes, "peso"))
#___________________________________________________________________________________________________________

def menos_pesado(lista: list, clave: str):
    total_indices = len(lista)
    calculo = calcular_minimo(lista, clave)
    
    for i in range(total_indices):
        if float(lista[i][clave]) == calculo:
            print(F"El nombre del superheroe menos pesado {lista[i]["nombre"]} y pesa {lista[i][clave]}")
    

# print(menos_pesado(lista_personajes, "peso"))









    


