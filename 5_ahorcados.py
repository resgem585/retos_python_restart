import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "computadora", "inteligencia"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar_ahorcado():
    intentos_maximos = 6
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = intentos_maximos

    print("¡Bienvenido al juego del ahorcado!")
    print(mostrar_palabra(palabra_secreta, letras_adivinadas))

    while intentos_restantes > 0:
        guess = input("Adivina una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if guess in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(guess)

        if guess not in palabra_secreta:
            intentos_restantes -= 1
            print(f"Incorrecto. Te quedan {intentos_restantes} intentos.")
        else:
            print("¡Correcto!")
        
        palabra_actual = mostrar_palabra(palabra_secreta, letras_adivinadas)
        print(palabra_actual)

        if "_" not in palabra_actual:
            print("¡Felicidades! Has adivinado la palabra.")
            break

    if "_" in palabra_actual:
        print(f"Lo siento, te has quedado sin intentos. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()
