print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
print(numeros)
lista = "["
for i in numeros:
    lista += str(i)+", "
lista+="]"
print(lista)

lista = "["
for i in range(0,len(numeros)):
    lista += f"{numeros[i]}, "
lista+="]"
print(lista)

lista = "["
i=0
while i < len(numeros):
    lista += f"{numeros[i]}, "
    i+=1
lista+="]"
print(lista)
# Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD","Tercer","Cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()

if palabra in palabras:
    print(f"Encontre la Palabra {palabra} en la lista.")
else:
    print(f"No Encontre la Palabra {palabra} en la lista.")

# 2DA FORMA
palabras=["UTD","Tercer","Cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()

encontro=False
for i in palabras:
    if i == palabra:
        encontro = True

if encontro:
    print(f"Encontre la Palabra {palabra} en la lista.")
else:
    print(f"No Encontre la Palabra {palabra} en la lista.")

        
#3er FORMA con un 
palabras=["UTD","Tercer","Cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()

for i in range(0,lenght(palabras)):
    if palabra[i]==palabra:
        encontro+True
if encontro:
    print(f"Encontre la Palabra {palabra} en la lista.")
else:
    print(f"No Encontre la Palabra {palabra} en la lista.")        

#4a Forma
palabras=["UTD","Tercer","Cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()

encontro=False
i=0
while i<len(palabras):
        if palabra[i]==palabra:
            encontro=True
if encontro:
    print(f"Encontre la Palabra {palabra} en la lista.")
else:
    print(f"No Encontre la Palabra {palabra} en la lista.")   
  
# Ejemplo 3 Añadir elementos a la lista
lista = []
    # lista[0] ="Hi"
    # lista[1] ="Hello"

valor = input("Dame un Valor: ").strip()
#opcion 1 con variables logicas
true = True
while true:
    lista.append(input("Dame un Valor)").strip())
    lista.append(valor)
    true = input("Ingresa True/False para continuar: ").strip
    if true == "True":
        true=False

print(lista)

##Opcion 2 con variable String
true = "S"
while true == "S":
    lista.append(input("Dame un Valor)").strip())
    lista.append(valor)
    true = input("Ingresa S/N para continuar: ").strip().upper()
    
# Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
            ["Carlos","6181234567"],
            ["Adrian","61812332456"],
            ["Carlos","6182223444"],
       ]

# print(agenda)

# for i in agenda:
#     print (i)

# for r in range(0,3):
#     for c in range(0,2):
#         print(agenda[r][c])

lista=""
for r in range(0,3):
    lista += "["
    for c in range(0,2):
       lista+=f"{agenda[r][c]}, "
    lista+="]"
    lista+="\n"

print(lista)