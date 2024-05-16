
from menu import *

operando_a = None
operando_b = None
resultados = None

while True:
    
    match menu(operando_a, operando_b):
        case "1":
            operando_a = operando1()
        case "2":
            operando_b = operando2()
        case "3":
            if operando_a is not None and operando_b is not None:
                operacion = menu_operaciones()
                resultados = calculo_operaciones(operando_a, operando_b, operacion)
                print("Operación realizada.")
            else:
                print("Debes ingresar ambos operandos antes de realizar operaciones.")
        case "4":
            if resultados is not None:
                informe_resultado(operacion, resultados, operando_a, operando_b)
            else:
                print("Debes realizar una operación primero.")
        case "5":
            break
        
    pausar()