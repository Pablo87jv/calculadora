from os import system
# Funciones para calculos aritméticos.
def sumar(num: float, num_2:float)->float:
    """ suma dos números.

    Args:
        num (float): se pide ingresar un numero flotante
        num_2 (float): se pide ingresar un numero flotante

    Returns:
        float: devuevle la suma de dos flotantes.
    """
    return num + num_2

def restar(num: float, num_2:float)->float:
        """ resta dos números.

        Args:
            num (float): pide un número
            num_2 (float): pide un número

        Returns:
            float: Devuelve la resta de dos flotantes.
        """
        return num - num_2


def multiplicar(num: float, num_2:float)->float:
    """pide 2 números y los multiplica.

    Args:
        num (float): pide un número.
        num_2 (float): pide un número.

    Returns:
        float: Devuelve la multiplicación de dos flotantes.
    """
    return num * num_2
    
def dividir(num: float, num_2:float)->float:
    """pide 2 números y los divide.

    Args:
        num (float): pide un número.
        num_2 (float): pide un número.

    Returns:
        float: Devuelve la división de dos flotantes.
    """
    if num_2 != 0:
        return num / num_2
    else:
        print("¡Error! No es posible dividir por cero.")

def factorial(numero_natural: int)->int:
    """muestra por pantalla el factorial de un número.

    Args:
        numero_natural (_type_): int numero a factoriar.
    Returns:
        int retorna un número entero, devuelve 0 si el número no es natural.
    """
    if numero_natural >= 0:
        if numero_natural == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, numero_natural + 1):
                factorial *= i
            return factorial
    else:
        return 0

#Funciones generales menu/pantalla, etc.

def limpiar_pantalla()->None:
    """limpia la pantalla.
    """
    system("cls")

def pausar ()->None:
    """Pausa la ejecucion para ver el Menu.
    """
    system("pause")

def menu(operando_a: float, operando_b: float) -> str:
    """Muestra las opciones disponibles para navegar por el menú.

    Args:
        operando_a (float): Primer operando.
        operando_b (float): Segundo operando.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    limpiar_pantalla()
    print("        Menu de Opciones")
    print(f"1- Ingresar primer operando (A = {operando_a})")
    print(f"2- Ingresar segundo operando (B = {operando_b})")
    print("3- Calcular todas las operaciones")
    print("4- Informar resultados")
    print("5- Salir")
    return input("Ingrese Opción: ")

def menu_aritmetico()->str:
    """Muestra un menú aritmético para utilizar los operandos a y b.

    Returns:
        str: Devuelve un str.
    """
    limpiar_pantalla()
    print("       ¿Que operación desea realizar?")
    print("a- Sumar")
    print("b- Restar")
    print("c- Multiplicar")
    print("d- Dividir")
    print("e- Factorial")
    return input("Ingrese Opción: ")
