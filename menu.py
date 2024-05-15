
from funciones_matematicas import *

def menu()->str:
    limpiar_pantalla()
    print(f"{'menu de opciones':^50s}")
    print("1- Ingresar 1er operando")
    print("2- Ingresar 2do operando")
    print("3- Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5- Salir")
    return input("Ingrese una opcion: ")

def operando1():
    a = int(input("Ingrese el valor de A: "))
    return a
    
def operando2():
    b = int(input("Ingrese el valor de B: "))
    return b
    
def calculo_operaciones(a, b):
    resultados = {
        "suma": sumar(a, b),
        "resta": restar(a, b),
        "division": dividir(a, b),
        "multiplicacion": multiplicar(a, b),
        "factorial_a": factorial(a),
        "factorial_b": factorial(b)
    }
    return resultados
    
def informe_resultado(resultados):
    print(f"El resultado de A+B es: {resultados['suma']}")
    print(f"El resultado de A-B es: {resultados['resta']}")
    print(f"El resultado de A/B es: {resultados['division']}" if resultados['division'] != "No es posible dividir por cero" else resultados['division'])
    print(f"El resultado de A*B es: {resultados['multiplicacion']}")
    print(f"El factorial de A es: {resultados['factorial_a']} y el factorial de B es: {resultados['factorial_b']}") 
    
def pausar():
    import os
    os.system("pause")
    
def limpiar_pantalla():
    import os
    os.system("cls")