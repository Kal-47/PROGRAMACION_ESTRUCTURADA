# Variables
def borrar_pantalla():
    print("\033c")
def autos(continuar,ingresados,total):

    while (continuar == "SI"):
        borrar_pantalla()
        # Entrada
        marca = input("Marca: ").strip().upper()
        origen = input("Origen: ").strip().upper()
        precio = float(input("Precio: "))

        # Proceso
        imp = 0

        if origen == "ALEMANIA":
            imp = 0.30
        if origen == "JAPON":
            imp = 0.20
        if origen == "ITALIA":
            imp = 0.15
        if origen == "USA":
            imp = 0.08

        num_imp = precio*imp
        subt = precio+num_imp

        # Salida
        print(f"Precio total: ${subt:.2f}\nImpuesto: ${num_imp:.2f}")
        print(salida)
        continuar = input("¿Ingresar otro vehículo?: [Si/No]: ").strip().upper()

continuar = "SI"
ingresados = 0
total = 0
autos()
print(
    f"Total de carros ingresados: {ingresados}\nPrecio total por todos los carros: ${total}")