
def busqueda_secuencial(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

entrada = input("Ingresa una lista de números separados por comas: ")
mi_lista = [int(x.strip()) for x in entrada.split(',')]
buscar = int(input("Ingresa el número que deseas buscar: "))

resultado = busqueda_secuencial(mi_lista, buscar)

if resultado != -1:
    print(f"Elemento encontrado en la posición {resultado}.")
else:
    print("Elemento no encontrado.")
