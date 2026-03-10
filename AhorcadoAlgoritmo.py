import random       

def tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero
    

def adivinar_letra(palabra, letras_adivinadas, letra):
    if letra in palabra:
        letras_adivinadas.append(letra)
        return True
    else:
        return False

def juego_ahorcado():
    palabras = ["manzana", "pepino", "berenjena"]
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("\nBienvenido al juego del ahorcado \n\nLa Palabra tiene", len(palabra), "letras\n" )

    while intentos > 0:
        print("\n" + tablero(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos)
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya habias adivinado esa letra. Volve a intentar")
            continue

        if adivinar_letra(palabra, letras_adivinadas, letra):
            print("CORRECTO adivinaste una letra.")
        else:
            print("INCORRECTO Intenta otra vez")
            intentos -= 1
        
        if len(letras_adivinadas) == len(set(palabra)):
            print("\n" + tablero(palabra, letras_adivinadas))
            print("FELICITACIONES Has adivinado la palabra.")
            break

        if intentos == 0:
            print("\nAy ay ay, agotaste todos los intentos")
            print("La palabra correcta era:", palabra)
            try:
                volver_intento = str(input("Quieres volver a intentarlo? Y/N: ")).lower()
                if volver_intento == 'y':
                    intentos = 6
                if volver_intento == 'n' or volver_intento is not 'y':
                    print("\nGracias por haber jugado")
                    break
            except ValueError:
                print("INGRESE CORRECTAMENTE LOS DATOS")

juego_ahorcado()