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



print("Por favor, escoga la operación que desee")
print("1 - Suma")
print("2 - Resta")
print("1 - Multiplicacion")
print("2 - Division")

while True:
    opcion = input("Por favor, escoga una opcion ( 1 | 2 | 3 | 4):")
    if opcion in ('1', '2', '3', '4'):
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

    else:
        print("Tu opcion no es valida.")
    if opcion not in ('1', '2', '3', '4'):
        print("La opción que escogiste no es válida")




    # Preguntar al usuario si quiere seguir continuando en la interfaz de usuario o si gusta retirarse
    keep_running = input("Te gustaria continuar? Si o No?")
    if keep_running in ('Si', 'SI', 'S', 'ESTA_BIEN', 'YES'):
        continue
    else:
        break
