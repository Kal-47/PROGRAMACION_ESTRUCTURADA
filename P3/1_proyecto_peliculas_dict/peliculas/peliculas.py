import funciones

""" pelis{
    "nombre":"Toy Story 5",
    "duracion":"120"
    "idioma":"español",
    "clasificacion":"A",
    "genero":"animada"
}       """


def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion = input(
        "\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion


def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica = input(
        "Introducir el nombre de la caracteristica: ").upper().strip()
    valor = input("Introducir el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica] = valor
    pelis.append(peli)
    funciones.accionExitosa()


def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULAS ::::...\n")
    if len(pelis) > 0:
        print("\tCaracteristica\t\tValor\n")
        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\t...No Hay caracteristicas a mostrar...")


def limpiarPeliculas(pelis):
    if len(pelis) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input(
                "¿Deseas borrar TODAS las características (Si/No)? ").lower().strip()
        if opc == "si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...")


def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica = input("Escribir el nombre de la caracteristica: ").upper().strip()4

    noencontro = False
    for i in pelis:
        if caracteristica == i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i+1}\t\t{pelis[i]}")
            noencontro = True
        funciones.espereTecla()

    if not (noencontro):
        input("...No existe la pelicula que estas buscando, verifique...")


def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica = input(
        "Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro = false
    for i in pelis:
        if caracteristica == i:
            opc = ""
            while opc != "si" and opc != "no":
                opc = input(
                    "¿Deseas borrar la caracteristica (Si/No)? ").lower().strip()
                if opc == "si":
                    pelis.pop(caracteristica)
                    funciones.accionExitosa()
                    noencontro = True
    if not (noencontro):
        input("...¡No exite la caracteristica que estas buscando, verifique!...")


def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR El BALOR DE LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica = input("Escribir el valor: ").upper().strip()
    noencontro = True
    for i in pelis:
        if caracteristica == i:
            opc = ""
            while opc != "si" and opc != "no":
                opc = input(
                    f"¿Deseas modificar el valor de la caracteristica {caracteristica} con el valor {i} de la pelicula (Si/No)? ").lower().strip()
            if opc == "si":
                pelis[caracteristica] = input(
                    "Escribe el nuevo valor de la caracteristica: ").upper().strip()
                noencontro = False
                funciones.accionExitosa()

    if noencontro:
        input("...¡No exite la caracteristica que estas buscando, verifique!...")
