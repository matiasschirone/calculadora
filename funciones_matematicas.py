def sumar(a, b):
    
    return a + b

def restar(a, b):
    
    return a - b

def dividir(a, b):
    
    if b == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicar(a, b):
   
    return a * b

def factorial(n):
    """Devuelve el factorial de n"""
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# print (sumar(4,4))
# print (restar(4,3))
# print (dividir(4,2))
# print (factorial(4))
# print (factorial(8))