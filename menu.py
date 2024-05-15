
from funciones_matematicas import *

def menu()->str:
    """_summary_

    Returns:
        str: _description_
    """
    limpiar_pantalla()
    print(f"{'menu de opciones':^50s}")
    print("1- Ingresar 1er operando")
    print("2- Ingresar 2do operando")
    print("3- Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5- Salir")
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
    
def calculo_operaciones(a: int, b: int)->list:
    """
    Calcula todas las operaciones matemáticas (suma, resta, división, multiplicación y factoriales) utilizando los operandos dados.

    Args:
        a (int): El primer operando.
        b (int): El segundo operando.

    Returns:
        list: Una lista que contiene los resultados de todas las operaciones.
    """
    resultados = [sumar(a, b),
        restar(a, b),
        dividir(a, b),
        multiplicar(a, b),
        factorial(a),
        factorial(b)]
        
    return resultados
    
def informe_resultado(resultados):
    """
    Muestra los resultados de las operaciones matemáticas.

    Args:
        resultados (list): Una lista que contiene los resultados de las operaciones.
    """
    operaciones = ["A+B", "A-B", "A/B", "A*B", "factorial de A", "factorial de B"]
    for i, operacion in enumerate(operaciones):
        print(f"El resultado de {operacion} es: {resultados[i]}")
    
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