# Solicitar al usuario un número
while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Verificar si el número es impar
if numero % 2 != 0:
    print(f"{numero} es un número impar.")
else:
    print(f"{numero} es un numero par")