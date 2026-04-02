#1. Verificación de Números Primos
#Escribe una función llamada exprimo que reciba un número entero y determine si es un número
# primo. Un número primo es aquel que solo es divisible por él mismo y por 1.
# • Entrada: 5
# • Salida Esperada: True
# • Entrada: 10
# • Salida Esperada: False
# Restricciones:
# • No puedes usar módulos externos.
# • La solución debe tener una complejidad de tiempo razonable. 
def exprimo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True
print(exprimo(5))
print(exprimo(10))