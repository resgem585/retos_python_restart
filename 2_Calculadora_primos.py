def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si tiene algún divisor además de 1 y él mismo, no es primo

    return True  # Si no se encontraron divisores, es primo

def main():
    # Solicitar al usuario ingresar un número
    try:
        numero_usuario = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        return

    # Verificar si el número es primo utilizando la función es_primo
    if es_primo(numero_usuario):
        print(f"{numero_usuario} es un número primo.")
    else:
        print(f"{numero_usuario} no es un número primo.")

# Llamar a la función principal
if __name__ == "__main__":
    main()