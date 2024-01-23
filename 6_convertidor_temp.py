def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Bienvenido al convertidor de temperaturas")

    while True:
        print("\nOpciones:")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            resultado = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {resultado:.2f} grados Fahrenheit.")

        elif opcion == "2":
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            resultado = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit son {resultado:.2f} grados Celsius.")

        elif opcion == "3":
            print("Gracias por usar el convertidor de temperaturas. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

if __name__ == "__main__":
    main()
