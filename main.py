
from menu import *

a = None
b = None
resultados = None

while True:
    
    match menu(a, b):
        case "1":
            a = operando1()
        case "2":
            b = operando2()
        case "3":
            if a is not None and b is not None:
                resultados = calculo_operaciones(a, b)
            else:
                print("Debes ingresar ambos operandos antes de calcular las operaciones.")
        case "4":
            if resultados is not None:
                informe_resultado(resultados)
            else:
                print("Primero debes calcular las operaciones.")
        case "5":
            break
        
    pausar()