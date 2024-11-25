'''
Estudiante: Santiago Gamboa Martínez
Aplicar un método de ordenamiento burbuja a un vector de números.
'''
def ordenamiento_vector(numeros):
    for i in range(len(numeros)): # Se asegura se repita según el número de elementos en la lista.
        for j in range(len(numeros)-1): # Se asegura que se compare cada elemento con el siguiente.
            if numeros[j] > numeros[j+1]: # Si el elemento actual es mayor al siguiente, se intercambian.
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j] # Intercambia los elementos.
    return numeros

opcion = True
while opcion: # Permite que el usuario pueda usar el programa cuantas veces quiera

    # Comprueba que los elementos ingresados sean números enteros.
    try: 
        lista = input("Ingrese los números separados por espacio: ")
        numeros = list(map(int, lista.split())) # Convierte la cadena de texto en una lista de enteros.
    except ValueError:
        print("Ingrese solo números enteros y tome en cuenta que deben estar separados por espacio.")
        continue

    # Comprueba que el vector no esté vacío.
    if len(numeros) == 0:
        print("No se ingresaron números. Intente de nuevo.")
        continue 

    print(f"Vector original: {numeros}")
    numeros_ordenados = ordenamiento_vector(numeros)
    print(f"Vector ordenado: {numeros_ordenados}")
    
    opcion_usuario = input("¿Desea ordenar otro vector? (s/n): ").lower()
    if opcion_usuario != "s":
        opcion = False
        print("Gracias por usar mi programa :D")