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

# buscar_hombres(lista_personajes, "genero")


"""B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F"""

def buscar_mujeres(lista: list, clave: str):
    
    cantidad = len(lista)

    for i in range(cantidad):
        if lista[i][clave] == "F":
            print(lista[i]["nombre"])

# buscar_mujeres(lista_personajes, "genero")



print("------------------------------------------------------------------------------------------")



"""C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"""

def masculino_altura_maxima(lista:list, clave: str):
    
    masculino_datos = []

    for personaje in lista:
        if personaje[clave] == "M":
            masculino_datos.append(personaje)
    
       
        
    masculino_datos = f"el heroe más alto mide {calcular_maximo(masculino_datos, "altura")}"
    return masculino_datos


# print(masculino_altura_maxima(lista_personajes, "genero"))


"""D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"""

def femenina_altura_maxima(lista: list, clave: str):
     
    femenino_datos = []
    
    for personaje in lista:
        if personaje[clave] == "F":
            femenino_datos.append(personaje)
    
    femenino_datos = f"La heroina más alta mide {calcular_maximo(femenino_datos, "altura")}"
    return femenino_datos

# print(femenina_altura_maxima(lista_personajes, "genero"))


"E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M"

def masculino_altura_minima(lista: list, clave: str):
   
    masculino_datos = []

    for personaje in lista:
        if personaje[clave] == "M":
            masculino_datos.append(personaje)
    
       
        
    masculino_datos = f"el heroe más bajo mide {calcular_minimo(masculino_datos, "altura")}"
    return masculino_datos

# print(masculino_altura_minima(lista_personajes, "genero"))


"F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F"

def femenina_altura_minima(lista: list, clave: str):
   
    femenino_datos = []
    
    for personaje in lista:
        if personaje[clave] == "F":
            femenino_datos.append(personaje)
    
    mujer_minima = calcular_minimo(femenino_datos, "altura")
    return mujer_minima

# print(femenina_altura_minima(lista_personajes, "genero"))


"""G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M"""


def altura_promedio_hombres(lista:list, clave:str):
    
    masculino_datos = []

    for personaje in lista:
        if personaje[clave] == "M":
            masculino_datos.append(personaje)
    
       
        
    masculino_datos = f"la altura promedio de los hombres es de {promediar_datos(masculino_datos)}"
    return masculino_datos

#print(altura_promedio_hombres(lista_personajes, "genero"))


"""H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F"""

def altura_promedio_mujeres(lista:list, clave:str):
   
    femenino_datos = []

    for personaje in lista:
        if personaje[clave] == "F":
            femenino_datos.append(personaje)
    
       
        
    femenino_datos = f"la altura promedio de las mujeres es de {promediar_datos(femenino_datos)}"
    return femenino_datos

# print(altura_promedio_mujeres(lista_personajes, "genero"))


"""I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)"""


"""J. Determinar cuántos superhéroes tienen cada tipo de color de ojos."""

def agrupamiento_por_clave(lista: list, clave: str) -> int:
    cantidad = len(lista)
    heroes_ojos_marrones = 0
    heroes_ojos_amarillos = 0
    heroes_ojos_azules = 0
    heroes_ojos_verdes = 0
    heroes_ojos_amarillos_variacion = 0
    heroes_ojos_plateados = 0
    heroes_ojos_rojos = 0
    heroes_ojos_hazel = 0

    for i in range(cantidad):
        if lista[i][clave] == "Brown":
            heroes_ojos_marrones = heroes_ojos_marrones + 1
            
        elif lista[i][clave] == "Yellow":
            heroes_ojos_amarillos = heroes_ojos_amarillos + 1 
            
        elif lista[i][clave] == "Blue" or lista[i][clave] == "blue":
            heroes_ojos_azules = heroes_ojos_azules + 1
        
        elif lista[i][clave] == "Green":
            heroes_ojos_verdes = heroes_ojos_verdes + 1
            
        elif lista[i][clave] == "Yellow (without irises)":
            heroes_ojos_amarillos_variacion = heroes_ojos_amarillos_variacion + 1
            
        elif lista[i][clave] == "Silver":
            heroes_ojos_plateados = heroes_ojos_plateados + 1

        elif lista[i][clave] == "Red":
            heroes_ojos_rojos = heroes_ojos_rojos + 1

        elif lista[i][clave] == "Hazel":
            heroes_ojos_hazel = heroes_ojos_hazel + 1    
    
    print(heroes_ojos_marrones)
    print(heroes_ojos_amarillos)
    print(heroes_ojos_azules)
    print(heroes_ojos_verdes)
    print(heroes_ojos_amarillos_variacion)
    print(heroes_ojos_plateados)
    print(heroes_ojos_rojos)
    print(heroes_ojos_hazel)
            
    
print(agrupamiento_por_clave(lista_personajes, "color_ojos"))







