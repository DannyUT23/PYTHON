# 3. . Suma de Elementos en una Lista
# Escribe una función llamada sumar_lista que reciba una lista de números y devuelva la suma de
# todos los elementos. La lista podría contener cualquier cantidad de elementos.
# • Entrada: [1, 2, 3, 4]
# • Salida Esperada: 10
# • Entrada: [5, 10, 15]
# • Salida Esperada: 30
#Restricciones:
#• No puedes utilizar la función sum() de Python.
def sumar_lista(lista):
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma

print(sumar_lista([1, 2, 3, 4]))
print(sumar_lista([5, 10, 15]))