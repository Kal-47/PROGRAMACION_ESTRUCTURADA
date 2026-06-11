# 1er utilizar los modulos 
import modulos

modulos.borrar_pantalla()
modulos.funcion1()

nom="Daniel"
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre: {name} \nApellidos:{lastname}")

#2da formar de utilizar modulos
    #from modulos import *(importa TODAS las funciones)
from modulos import borrar_pantalla,funcion1,funcion4

borrar_pantalla()
funcion1()

nom="Daniel"
ape="Carreon"

name,lastname=funcion4(nom,ape)
print(f"Nombre: {name} \nApellidos:{lastname}")
