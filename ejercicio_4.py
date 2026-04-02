# 4. Invertir una Cadena
# Crea una función llamada invertir_cadena que reciba una cadena de texto y devuelva la misma
# cadena, pero con los caracteres en orden inverso.
# • Entrada: "python"
# • Salida Esperada: "nohtyp"
# • Entrada: "curso"
# • Salida Esperada: "osruc"
# Restricciones:
# • No puedes utilizar la función reverse() de listas ni [::-1].
def invertir_cadena (cadena):
    resultado = ""

    for caracter in cadena:
        resultado = caracter + resultado

    return resultado

print(invertir_cadena("python"))
print(invertir_cadena("curso"))