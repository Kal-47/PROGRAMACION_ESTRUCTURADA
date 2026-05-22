'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Sin estructuras de control
    2.- Sin funciones
'''

print("\033c")

# Entrada
num = int(input("Número para la tabla de multiplicar: "))

# Proceso
salida = f"{num} x 1 = {(num*1)}\n{num} x 2 = {(num*2)}\n{num} x 3 = {(num*3)}\n{num} x 4 = {(num*4)}\n{num} x 5 = {(num*5)}\n{num} x 6 = {(num*6)}\n{num} x 7 = {(num*7)}\n{num} x 8 = {(num*8)}\n{num} x 9 = {(num*9)}\n{num} x 10 = {(num*10)}"

# Salida
print(salida)

'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Con estructuras de control
    2.- Sin funciones
'''
num = int(input("Número para la tabla de multiplicar: "))
for x in range(1, 11):
    result = num*x
    print(f"{num} x {x} = {result}")

'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Con estructuras de control con for con decrementos de 10 en 10
    2.- Sin funciones
'''

num = int(input("Número para la tabla de multiplicar: "))
for x in range(100, 0, -10):
    result = num*x
    print(f"{num} x {x} = {result}")

'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Con estructuras de control con while con decrementos de 10 en 10
    2.- Sin funciones
'''

num = int(input("Número para la tabla de multiplicar: "))
step = 100
while step > 0:
    result = num*step
    print(f"{num} x {step} = {result}")
    step -= 10

'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Sin estructuras de control
    2.- Con funciones
'''


def mult(numero, multiplicador):
    mult_result = numero*multiplicador
    return mult_result


num = int(input("Número para la tabla de multiplicar: "))
salida = f"{num} x 1 = {mult(num, 1)}\n{num} x 2 = {mult(num, 2)}\n{num} x 3 = {mult(num, 3)}\n{num} x 4 = {mult(num, 4)}\n{num} x 5 = {mult(num, 5)}\n{num} x 6 = {mult(num, 6)}\n{num} x 7 = {mult(num, 7)}\n{num} x 8 = {mult(num, 8)}\n{num} x 9 = {mult(num, 9)}\n{num} x 10 = {mult(num, 10)}"

'''
    Crear un programa que calcule e imprima cualquier tabla de multiplicar

    Restricciones:
    1.- Sin estructuras de control
    2.- Con funciones
'''


def mult(numero, multiplicador):
    mult_result = numero*multiplicador
    return mult_result


num = int(input("Número para la tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{num} x {i} = {mult(num, i)}")
