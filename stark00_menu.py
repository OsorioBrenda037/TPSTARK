from data_stark import lista_personajes
from stark00_funciones import *
from os import system

def pausar():
    """Funcion que pause el programa 
    hasta que el usuario presione alguna tecla.
    """
    system("pause")


"J. Construir un menú que permita elegir qué dato obtener"

def menu():
    print("STARK INDUSTRIES")
    print("-----------------")
    print("Opciones:")
    print("A) Conocer superheroes")
    print("B) Nombre y altura de cada heroe")
    print("C) Mayor altura")
    print("D) Menor altura")
    print("E) Promedio de altura de todos los heroes")
    print("F) Nombre del heroe más alto")
    print("G) Nombre del here mas bajo")
    print("H) Nombre y peso del heroe más pesado")
    print("I) Nombre y peso de heroe menos pesado")
    print("J) salir")

    opcion = input("Bievenido: Elija lo que desee ver: ")
    print(system("cls"))
    return opcion


desea_seguir = "s"

while desea_seguir == "s":

    opcion = menu()

    match(opcion):
        case "A":
            print("Nombre")
            print(imprimir_informacion_superheroe(lista_personajes, "nombre"))
        
        case "B":
            print("Nombre                       Altura")
            print(nombre_y_altura(lista_personajes))
        
        case "C": 
            print(f"El heroe más alto mide: {calcular_maximo(lista_personajes, "altura")}")
        
        case "D":
            print(f"El heroe más bajo mide {calcular_minimo(lista_personajes, "altura")}")
        
        case "E":
            print(f"EL promedio de altura entre todos los personajes es {promediar_datos(lista_personajes)}")
        
        case "F":
            nombre_maximo_minimo(lista_personajes, "altura", True)
        
        case "G":
            nombre_maximo_minimo(lista_personajes, "altura", False)
        
        case "H":
            mas_pesado(lista_personajes, "peso")
        
        case "I":
            menos_pesado(lista_personajes, "peso")
        
        case "J":
            desea_seguir = input("presione s para continuar, de lo contrario presione n: ")

            if desea_seguir == "n":
                break
    pausar()

    
    



