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
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener"""

print(len(lista_personajes))


#Convierto todos los numeros a enteros/flotantes
def normalizar_datos(Lista:list):

    for i in range(len(lista_personajes)):
        if lista_personajes[i]["altura"] != float:
            casteado = float(lista_personajes[i]["altura"])
        
        if lista_personajes[i]["peso"] != float:
            casteado = float(lista_personajes[i]["peso"])
        
        if lista_personajes[i]["fuerza"] != int:
            casteado = int(lista_personajes[i]["fuerza"])
    
    return casteado


    

'B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe'

def imprimir_nombre_superheroe(lista: list):
    """Funcion que nos imprime por consola el nombre de cada super heroes de la lista


    Args:
        lista (list): La lista se compone 
        de diccionarios que contienen informacion de cada super heroe. por ejemplo
        nombre, altura, inteligencia, fuerza, empresa. etc
    """

    for i in range(len(lista)):
        print(f"El nombre del superheroe es: {lista[i]["nombre"]}")


imprimir_nombre_superheroe(lista_personajes)



'C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a'
'la altura del mismo'

def nombre_y_altura(lista:list):

    for i in range(len(lista)):
        print(f"El nombre y la altura del superheroe es: {lista[i]["nombre"], lista[i]["altura"]}")

nombre_y_altura(lista_personajes)



'D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)'

def calcular_maximo(lista: list, clave: str):
    puerta_maximo = True
    maximo = None

    for i in range(len(lista)):
        if puerta_maximo == True:
            puerta_maximo = False
            maximo = lista[i][clave]
        
        else:
            if maximo < lista[i][clave]:
                maximo = lista[i][clave]
                puerta_maximo = False

    return maximo



'E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)'

def calcular_minimo(lista: list, clave: str):
    puerta_minimo = True
    minimo = None

    for i in range(len(lista)):
        if puerta_minimo == True:
            puerta_minimo = False
            minimo = lista[i][clave]
        
        else:
            if minimo > lista[i][clave]:
                minimo = lista[i][clave]
                puerta_minimo = False

    return minimo

print(calcular_minimo(lista_personajes, "altura")) 
print(calcular_maximo(lista_personajes, "altura"))


"ARREGLAR ESTO MAÑANA"
        
        
'F. Recorrer la lista y determinar la altura promedio de los superhéroes'
'(PROMEDIO)'

def promedio(lista: list):
    pass



