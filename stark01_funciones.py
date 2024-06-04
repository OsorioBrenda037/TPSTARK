from data_stark import lista_personajes
from stark00_funciones import *

#TP STARK 01

"""
Nombre y apellido: Osorio Brenda
Division: 113
Profesores: Christian Baus, 

"""

#------------------------------------------------------
"""



E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia 
"""


"""A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M"""

def buscar_hombres(lista: list, clave: str):
    
    cantidad = len(lista)

    for i in range(cantidad):
        if lista[i][clave] == "M":
            print(lista[i]["nombre"])

#buscar_hombres(lista_personajes, "genero")


"""B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F"""

def buscar_mujeres(lista: list, clave: str):
    
    cantidad = len(lista)

    for i in range(cantidad):
        if lista[i][clave] == "F":
            print(lista[i]["nombre"])

buscar_mujeres(lista_personajes, "genero")


"""C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"""

def masculino_max(lista:list, clave: str):
    
    cantidad = len(lista)
    
    for i in range(cantidad):
        if lista[i][clave] == "M":
            print(calcular_maximo(lista_personajes, "altura"))
            break

masculino_max(lista_personajes, "genero")


"""D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"""

def femenino_max(lista:list, clave:str):
    cantidad = len(lista)
    
    for i in range(cantidad):
        if lista[i][clave] == "F":
            print(f"La mujer más alta mide {calcular_maximo(lista_personajes, "altura")}")
            break

femenino_max(lista_personajes, "genero")





