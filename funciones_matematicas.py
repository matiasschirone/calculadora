def sumar(a: int, b: int)->int:
    """Realiza la suma de dos valores

    Args:
        a (int): Primer entero de la suma
        b (int): Segundo entero de la suma

    Returns:
        int: Devuelve la suma del entero a  y el entero b
    """
    return a + b

def restar(a: int, b: int)->int:
    """Realiza la resta de dos valores

    Args:
        a (int): Primer valor ingresado
        b (in): Segundo valor ingresado

    Returns:
        int: Devuelve la resta entre el valor a y el valor b
    """
    return a - b

def dividir(a: int, b: int)->float:
    """Realiza una division del valor a sobre el valor b 
    Args:
        a (int): Primer valor ingresado (dividendo)
        b (int): Segundovalor ingresado (divisor)

    Returns:
        Devuelve la division entre los valores ingresados (a/b)
    """
    return a / b

def multiplicar(a: int, b: int)->int:
    """Realiza la multiplicacion entre los valores ingresados

    Args:
        a (int): Primer valor ingresado
        b (int): Segundo valor ingresado

    Returns:
        int: Devuelve la multiplicacion entre los valores a y b
    """
    return a * b

def factorial(n: int)-> int:
    """
    Calcula el factorial de un número entero n.

    Args:
        n (int): El número del cual se va a calcular el factorial.

    Returns:
        int: El factorial de n.
        str: Un mensaje de error si n es un número negativo.
    """
    if isinstance(n, bool):
        raise TypeError("No se aceptan Booleanos")
    elif isinstance(n, int):
        if n < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo")
        fact = None
        if n == 0 or n ==1:
            fact = 1
        else:
            fact = n * factorial(n - 1)
        return fact
    else:
        raise TypeError("No es un numero")

