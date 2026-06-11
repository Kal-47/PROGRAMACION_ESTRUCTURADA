"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.

funciones:
count()
index()
"""

print("\033c")

paises1 = ("México","Canada","EUA")
paises3 = ["México","Canada","EUA"]
varios = ("Hola",True,33,3.1416)

paises3[1] = "Brazil"

print(paises1)
print(paises3)
print(varios)


for i in paises1:
  print(i)

for i in range(0,len(paises1)):
  print(paises1[i])

# z = 0
# while z < 3:
#   print(paises1[z])
#   z+= 1

print(f"El pais que inaugura la copa del mundo 2026 es: {paises1[0]}")

##Uso de count
edades = (23,24,18,20,20,23,24,19,24)

cuantos_edades= edades.count(24)
print(cuantos_edades)

##Crear un programa que me lea un numero y me digan en que posiciones se encuentra
###Usando listas
num = int(input("Inserta un numero entero: "))

numeros=(10,10,5,5,3,6,7)
posiciones = []
for i in range(0,len(numeros)):
  if num == numeros[i]:
    # i+=1
    posiciones.append(i)

tupla_pos = tuple(posiciones)

print(tupla_pos)

# for i in tupla_pos:
#   print(f"el numero {num} se encontro en las posicion {tupla_pos}")

print(f"el numero {num} se encontro en las posiciones {posiciones}")

'''usando sets

num = int(input("Inserta un numero entero: "))

numeros=(10,10,5,5,3,6,7)
posiciones = {""}
posiciones.clear
for i in range(0,len(numeros)):
  if num == numeros[i]:
    # i+=1
    posiciones.add(i)

tupla_pos = tuple(posiciones)

print(tupla_pos)

# for i in tupla_pos:
#   print(f"el numero {num} se encontro en las posicion {tupla_pos}")

print(f"el numero {num} se encontro en las posiciones {posiciones}")

'''