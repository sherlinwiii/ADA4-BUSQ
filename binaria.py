def busqueda_binaria(lista, objetivo):
    
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1
entrada = input("Ingresa una lista ordenada de números separados por comas: ")
mi_lista = [int(x.strip()) for x in entrada.split(',')]

if mi_lista != sorted(mi_lista):
    print("La lista no está ordenada. La búsqueda binaria requiere una lista ordenada.")
else:
    buscar = int(input("Ingresa el número que deseas buscar: "))

    resultado = busqueda_binaria(mi_lista, buscar)

    if resultado != -1:
        print(f"Elemento encontrado en la posición {resultado}.")
    else:
        print("Elemento no encontrado.")
