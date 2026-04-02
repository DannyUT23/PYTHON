# 5. Eliminar Elementos Duplicados en una Lista
# Implementa una función eliminar_duplicados que reciba una lista de números (que pueden estar
# repetidos) y devuelva una nueva lista sin elementos duplicados, manteniendo el orden original.
# • Entrada: [1, 2, 2, 3, 4, 4]
# • Salida Esperada: [1, 2, 3, 4]
# • Entrada: [5, 5, 5, 6, 7]
# • Salida Esperada: [5, 6, 7]
# Restricciones:
# • No puedes usar el tipo de dato set.
# • Mantén el orden de aparición de los elementos en la lista original
def eliminar_duplicados(listas):
    resultado =[]

    for elemento in listas:
        if elemento not in resultado:
            resultado.append(elemento)


    return resultado

print(eliminar_duplicados([1, 2, 2, 3, 4, 4 ]))
print(eliminar_duplicados([5, 5, 5, 6, 7]))