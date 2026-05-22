def function1(): # <- Procedimiento
    nombre = input("Ingrese su nombre:\n").upper().strip()
    apellidos = input("Ingrese sus apellidos:\n").upper().strip()
    print(f"El nombre del alumno es: {nombre} {apellidos}")


def funcion3(nom, ape): # <- Funcion que recibe pero no retorna
    nombre = nom
    apellidos = ape
    print(f"El nombre del alumno es: {nombre} {apellidos}")

def funcion2(): # <- # Funcion que retorna pero no recibe
    nombre = input("Ingrese su nombre:\n").upper().strip()
    apellidos = input("Ingrese sus apellidos:\n").upper().strip()
    return nombre,apellidos

def funcion3(nom, ape): # <- Funcion que recibe para retornar
    nombre = nom
    apellidos = ape
    return nombre,apellidos

def funcion4(nom,ape):
   nombre = nom
   apellidos = ape
   return nombre,apellidos


function1()
nombre = input("Ingrese su nombre:\n").upper().strip()
apellidos = input("Ingrese sus apellidos:\n").upper().strip()

funcion3(nombre,apellidos)

nombre, apellidos = funcion2()
print(f"El nombre del alumno es {nombre} {apellidos}")

nom = input("Ingrese su nombre:\n").upper().strip()
ape = input("Ingrese sus apellidos:\n").upper().strip()

nombre,apellidos = funcion4(nom, ape)
print(f"El nombre del alumno es {nombre} {apellidos}")