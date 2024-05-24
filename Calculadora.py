from modulo_calculadora import *

flag_operando_a = False
flag_operando_b = False
flag_factorial = False
a = 'x'
b = 'y'

while True:
    match menu(a, b):
        case "1":
            a = float(input("Ingrese primer operando:\n"))
            
            flag_operando_a = True
        case "2":
            if flag_operando_a == True:
                b = float(input("Ingrese segundo operando:\n"))
                flag_operando_b = True
            else:
                print("primero debes ingresar el operando a.")
        case "3":
            if flag_operando_a and flag_operando_b:
                match menu_aritmetico():
                    case "a":
                        resultado = sumar(a, b)
                    case "b":
                        resultado = restar(a, b)
                    case "c":
                        resultado = multiplicar(a, b)
                    case "d":
                        resultado = dividir(a, b)
                    case "e":
                        a_int = int(a)
                        resultado = factorial(a_int)
                        b_int = int(b)
                        resultado_2 = factorial(b_int)
                        flag_factorial = True
                print("Se guardó el resultado...")
            elif flag_operando_a == False:
                print("Falta ingresar el primero operando.")
            else:
                print("Falta ingresar el segundo operando.")
                
        case "4":
            if flag_operando_a and flag_operando_b:
                flag_operando_a = False
                flag_operando_b = False
                a = 'x'
                b = 'y'
                if flag_factorial == True:
                    print(f"El factorial del primer operando es: {resultado}")
                    print(f"El factorial del segundo operando es: {resultado_2}")
            else:
                print("No hay ningún resultado guardado.")
                
        case "5":
            fin = input("¿Desea salir del programa? si/no:\n").lower()
            if fin == "si" or fin == "sí":
                break
    
    pausar()
    
print("Fin del programa.")