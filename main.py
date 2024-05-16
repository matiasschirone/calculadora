
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
                operacion = menu_operaciones()
                resultados = calculo_operaciones(a, b, operacion)
                print("Operación realizada.")
            else:
                print("Debes ingresar ambos operandos antes de realizar operaciones.")
        case "4":
            if resultados is not None:
                informe_resultado(operacion, resultados, a, b)
            else:
                print("Debes realizar una operación primero.")
        case "5":
            break
        
    pausar()