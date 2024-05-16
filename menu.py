
from funciones_matematicas import *

def menu(a, b)->str:
    """
    Muestra un menú de opciones y solicita al usuario que ingrese una opción.

    Args:
        a (int): El valor actual del primer operando (A).
        b (int): El valor actual del segundo operando (B).

    Returns:
        str: La opción seleccionada por el usuario. 
    """
    limpiar_pantalla()
    print(f"{'menu de opciones':^50s}")
    print("1- Ingresar 1er operando")
    print("2- Ingresar 2do operando")
    print("3- Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5- Salir")
    if a is not None:
        print(f"Operando A= {a}")
    if b is not None:
        print(f"Operando B= {b}")
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in ['1', '2', '3', '4', '5']:
            return opcion
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

def operando1():
    """
    Solicita al usuario que ingrese el valor del primer operando.

    Returns:
        int: El valor del primer operando ingresado por el usuario.
    """
    while True:
        try:
            a = int(input("Ingrese el valor de A: "))
            return a
        except ValueError:
            print("Por favor, ingrese un valor entero válido para A.")
    
def operando2():
    """
    Solicita al usuario que ingrese el valor del segundo operando.

    Returns:
        int: El valor del segundo operando ingresado por el usuario.
    """
    while True:
        try:
            b = int(input("Ingrese el valor de B: "))
            return b
        except ValueError:
            print("Por favor, ingrese un valor entero válido para B.")
    
    
def menu_operaciones():
    """
    Muestra un menú de operaciones y solicita al usuario que seleccione una opción.

    Returns:
        str: La opción seleccionada por el usuario.
    """
    while True:
        limpiar_pantalla()
        print(f"{'Menu de Operaciones':^50s}")
        print("a) Calcular la suma (A+B)")
        print("b) Calcular la resta (A-B)")
        print("c) Calcular la división (A/B)")
        print("d) Calcular la multiplicación (A*B)")
        print("e) Calcular factorial (A!)")

        opcion = input("Ingrese una opción: ")
        if opcion in ['a', 'b', 'c', 'd', 'e']:
            return opcion
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

def calculo_operaciones(a: int, b: int, operacion: str):
    """
    Realiza la operación matemática seleccionada utilizando los operandos dados.

    Args:
        a (int): El primer operando.
        b (int): El segundo operando.
        operacion (str): La operación a realizar (opciones: 'a', 'b', 'c', 'd', 'e').
    """
    try:
        if operacion == "a": 
            return sumar(a, b)
        elif operacion == "b": 
            return restar(a, b)
        elif operacion == "c":  
            return dividir(a, b)
        elif operacion == "d":  
            return multiplicar(a, b)
        elif operacion == "e": 
            return factorial(a), factorial(b)
        else:
            return "Operación no válida"
    except ZeroDivisionError:
        return "No es posible dividir por cero"
    
def informe_resultado(operacion, resultado, a=None, b=None):
    """
    Muestra el resultado de la operación seleccionada
    """
    if operacion == 'a':
        print(f"El resultado de {a}+{b} es: {resultado}")
    elif operacion == 'b':
        print(f"El resultado de {a}-{b} es: {resultado}")
    elif operacion == 'c':
        print(f"El resultado de {a}/{b} es: {resultado}")
    elif operacion == 'd':
        print(f"El resultado de {a}*{b} es: {resultado}")
    elif operacion == 'e':
        print(f"El factorial de {a} es: {resultado[0]} y El factorial de {b} es: {resultado[1]}")
    
    
def pausar():
    """
    Pausa la ejecución del programa hasta que el usuario presione una tecla.
    """
    import os
    os.system("pause")
    
def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    import os
    os.system("cls")