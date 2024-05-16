
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
        print(f"Operando 1 (A) = {a}")
    if b is not None:
        print(f"Operando 2 (B) = {b}")
    return input("Ingrese una opcion: ")

def operando1():
    """
    Solicita al usuario que ingrese el valor del primer operando.

    Returns:
        int: El valor del primer operando ingresado por el usuario.
    """
    a = int(input("Ingrese el valor de A: "))
    return a
    
def operando2():
    """
    Solicita al usuario que ingrese el valor del segundo operando.

    Returns:
        int: El valor del segundo operando ingresado por el usuario.
    """
    b = int(input("Ingrese el valor de B: "))
    return b
    
    
def menu_operaciones():
    """
    Muestra un menú de operaciones y solicita al usuario que seleccione una opción.

    Returns:
        str: La opción seleccionada por el usuario.
    """
    limpiar_pantalla()
    print(f"{'Menu de Operaciones':^50s}")
    print("a) Calcular la suma (A+B)")
    print("b) Calcular la resta (A-B)")
    print("c) Calcular la división (A/B)")
    print("d) Calcular la multiplicación (A*B)")
    print("e) Calcular factorial (A!)")
    return input("Ingrese una opción: ")

def calculo_operaciones(a: int, b: int, operacion: str):
    """
    Realiza la operación matemática seleccionada utilizando los operandos dados.

    Args:
        a (int): El primer operando.
        b (int): El segundo operando.
        operacion (str): La operación a realizar (opciones: 'a', 'b', 'c', 'd', 'e').
    """
    if operacion == "a": 
        return sumar(a, b)
    elif operacion == "b": 
        return restar(a, b)
    elif operacion == "c":  
        if b != 0:
            return dividir(a, b)
        else:
            return "No es posible dividir por cero"
    elif operacion == "d":  
        return multiplicar(a, b)
    elif operacion == "e": 
        return factorial(a), factorial(b)
    else:
        return "Operación no válida"
    
def informe_resultado(operacion, resultado, a=None, b=None):
    """
    Muestra el resultado de la operación seleccionada
    """
    if operacion == 'a':
        print(f"El resultado de {a}+{b} es: {resultado}")
    elif operacion == 'b':
        print(f"El resultado de {a}-{b} es: {resultado}")
    elif operacion == 'c':
        if resultado == 0:
            print("no se puede dividir por cero")
        else:
            print(f"El resultado de {a}/{b} es: {resultado}")
    elif operacion == 'd':
        print(f"El resultado de {a}*{b} es: {resultado}")
    elif operacion == 'e':
        print(f"El factorial de {a} es: {resultado[0]} y El factorial de {b} es: {resultado[1]}")
    else:
        print("Operación no válida")
    
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