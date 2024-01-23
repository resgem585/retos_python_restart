"""Descripción: Escribe una función que tome una cadena de caracteres que contiene solo paréntesis ( y ) y determine si la secuencia de paréntesis es válida. Una secuencia de paréntesis es válida si cada paréntesis abierto se cierra con un paréntesis correspondiente en el orden correcto. Por ejemplo, "(())()" y "()" son secuencias válidas, pero ")(" y "(()" no lo son.
"""

def es_secuencia_valida(secuencia):
    pila = []  # Usaremos una lista como pila

    for caracter in secuencia:
        if caracter == '(':
            pila.append(caracter)  # Empujar paréntesis abierto a la pila
        elif caracter == ')':
            if not pila:  # Si la pila está vacía, no hay paréntesis abierto correspondiente
                return False
            else:
                pila.pop()  # Pop para emparejar con el último paréntesis abierto

    return not pila  # La secuencia es válida si la pila está vacía al final

# Ejemplos de uso:
print(es_secuencia_valida("(())()"))  # True
print(es_secuencia_valida("()"))      # True
print(es_secuencia_valida(")("))      # False
print(es_secuencia_valida("(()"))     # False