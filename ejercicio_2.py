# 2. Contar Palabras en una Cadena
# Implementa una función contar_palabras que reciba una cadena de texto y devuelva la cantidad
# de palabras que contiene. Se debe considerar como palabras aquellas que estén separadas por
# espacios.
# • Entrada: "Python es un lenguaje de programación"
# • Salida Esperada: 5
# • Entrada: "Hola"
# • Salida Esperada: 1
# Restricciones:
# • La cadena no tendrá signos de puntuación.
# • Los espacios adicionales al principio o final de la cadena deben ser ignorados
def contar_palabras(cadena):
    cadena = cadena.strip()

    if cadena == "":
        return 0
    
    palabras = cadena.split()

    return len(palabras)

print(contar_palabras("Python es un lenguaje de programación"))
print(contar_palabras("Hola"))