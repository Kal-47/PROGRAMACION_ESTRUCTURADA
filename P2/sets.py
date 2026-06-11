"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

# set1={"Hola","123","123","Mexico","Holanda"}
# print(set1)

# set1.add("Ganador")
# print(set1)


##ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en#Solucion 1a pantalla los email sin duplicados

##Solucion 1
lista=[]
mail_f={}
conf = "S"
while conf == "S":
  lista.append(input("Ingresa un valor: "))
  conf = input("Repetir? (S/N)").upper()

mail_f = set(lista)
print(mail_f)

##Solucion 2

  



