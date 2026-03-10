import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

palabras = ['manzana', 'pepino', 'naranja']

pygame.init()

screen_widht = 800
screen_height = 600
ventana = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption('Juego del Ahorcado')

letras_adivinadas = []
intentos = 6
letra_actual = ''

def seleccionar_palabra():
    return random.choice(palabras)

# Función para dibujar el ahorcado
def dibujar_ahorcado(intentos):
    # Dibujar la horca
    pygame.draw.line(ventana, BLACK, (150, 450), (550, 450), 5)
    pygame.draw.line(ventana, BLACK, (350, 450), (350, 100), 5)
    pygame.draw.line(ventana, BLACK, (350, 100), (500, 100), 5)
    pygame.draw.line(ventana, BLACK, (500, 100), (500, 150), 5)

    if intentos < 6:
        # Dibujar la cabeza
        pygame.draw.circle(ventana, BLACK, (500, 180), 30, 5)

    if intentos < 5:
        # Dibujar el cuerpo
        pygame.draw.line(ventana, BLACK, (500, 210), (500, 350), 5)

    if intentos < 4:
        # Dibujar el brazo izquierdo
        pygame.draw.line(ventana, BLACK, (500, 240), (450, 300), 5)

    if intentos < 3:
        # Dibujar el brazo derecho
        pygame.draw.line(ventana, BLACK, (500, 240), (550, 300), 5)

    if intentos < 2:
        # Dibujar la pierna izquierda
        pygame.draw.line(ventana, BLACK, (500, 350), (450, 400), 5)

    if intentos < 1:
        # Dibujar la pierna derecha
        pygame.draw.line(ventana, BLACK, (500, 350), (550, 400), 5)

# Función para mostrar el estado actual del juego
def mostrar_estado(letras_adivinadas, intentos_restantes):
    ventana.fill(WHITE)

    # Dibujar letras adivinadas
    fuente = pygame.font.SysFont('arial', 36)
    texto = fuente.render('Palabra: ', True, BLACK)
    ventana.blit(texto, (20, 400))

    letras = ''
    for letra in letras_adivinadas:
        letras += letra + ' '
    texto = fuente.render(letras, True, BLACK)
    ventana.blit(texto, (20, 60))

    # Dibujar intentos restantes
    texto = fuente.render('Intentos restantes: ' + str(intentos_restantes), True, BLACK)
    ventana.blit(texto, (20, 100))

    # Dibujar ahorcado
    dibujar_ahorcado(intentos_restantes)

    # Actualizar la ventana
    pygame.display.update()

# Función principal del juego
def jugar_ahorcado():
    palabra_seleccionada = seleccionar_palabra()
    letras_adivinadas = ['_'] * len(palabra_seleccionada)
    intentos_restantes = 6

    # Bucle principal del juego
    while True:
        # Gestionar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.unicode.isalpha():
                    letra_actual = evento.unicode.lower()

                    if letra_actual in letras_adivinadas:
                        continue

                    if letra_actual in palabra_seleccionada:
                        # La letra es correcta
                        for i in range(len(palabra_seleccionada)):
                            if palabra_seleccionada[i] == letra_actual:
                                letras_adivinadas[i] = letra_actual
                    else:
                        # La letra es incorrecta
                        intentos_restantes -= 1

        # Mostrar el estado actual del juego
        mostrar_estado(letras_adivinadas, intentos_restantes)

        # Comprobar si se ha ganado o perdido
        if '_' not in letras_adivinadas:
            print('¡Has ganado!')
            break

        if intentos_restantes == 0:
            print('¡Has perdido! La palabra era:', palabra_seleccionada)
            break

# Iniciar el juego
jugar_ahorcado()