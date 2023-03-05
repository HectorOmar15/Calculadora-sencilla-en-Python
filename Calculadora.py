"#Calculadora Básica, creada por: Héctor Omar García Ballesteros"

#El programa debe de cumplir con estas sentencias derivativas de operaciones básicas matemáticas:
#1 - Suma
#2 - Resta
#3 - Multiplicacion
#4 - Division

#Con el fin de crear un código capaz de ejecutar correctamente la lógica de una calculadora básica de mano

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def raizcuadrada(a):
    return pow(a, 1/2)
def raizcuadrada(b):
    return pow(b, 1/2)
def potencia(a):
    return a * a
def potencia(b):
    return b * b




print("Por favor, escoga la operación que desee")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicacion")
print("4 - Division")
print("5 - Potencia del PRIMER NUMERO")
print("6 - Potencia del SEGUNDO NUMERO")
print("7 - Raiz Cuadrada del PRIMER NUMERO")
print("8 - Raiz Cuadrada del SEGUNDO NUMERO")


while True:
    opcion = input("Por favor, escoga una opcion ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8):")
    if opcion in ('1', '2', '3', '4', '5', '6', '7', '8'):
        num1 = float(input("Por favor, introduzca su primer numero: "))
        num2 = float(input("Por favor, introduzca su segundo numero: "))
        if opcion == '1':
            print(f"{num1} + {num2} = ", suma(num1, num2))
        elif opcion == '2':
            print(f"{num1} - {num2} = ", resta(num1, num2))
        elif opcion == '3':
            print(f"{num1} * {num2} = ", multiplicacion(num1, num2))
        elif opcion == '4':
            print(f"{num1} / {num2} = ", division(num1, num2))
        elif opcion == '5':
            print(f"{num1} * {num1} = ", potencia(num1))
        elif opcion == '6':
            print(f"{num2} * {num2} = ", potencia(num2))
        elif opcion == '7':
            print(f"{num1} * {0.5} = ", raizcuadrada(num1))
        elif opcion == '8':
            print(f"{num2} * {0.5} = ", raizcuadrada(num2))





    else:
        print("Tu opcion no es valida.")
    if opcion not in ('1', '2', '3', '4'):
        print("La opción que escogiste no es válida")




    # Preguntar al usuario si quiere seguir continuando en la interfaz de usuario o si gusta retirarse
    sigue_corriendo = input("Te gustaria continuar? Si o No?")
    if sigue_corriendo in ('Si', 'SI', 'S', 'ESTA_BIEN', 'YES'):
        continue
    else:
        break

