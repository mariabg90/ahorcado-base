import pygame as pg
from hangman import utils
from hangman.constants import GRAPHICS, WINDOW_H, WINDOW_W
from jugador import Jugador
from palabras import Palabras

# inicialización
pg.init()
display = pg.display.set_mode((WINDOW_W, WINDOW_H), 0, 32)
pg.display.set_caption('Juego del ahorcado')
clock = pg.time.Clock()
font_name = pg.font.get_default_font()
font = pg.font.SysFont(font_name, 70)
letters_font = pg.font.SysFont(font_name, 60)

# tengo acceso a los datos y funciones que he definido en mis clases:
palabras_juego = Palabras()
jugador = Jugador()


counter = 0
status = -1
playing = True

# bucle principal
while playing:
    clock.tick(20)
    counter += 1

    # evento para salir al cerrar la ventana
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

        if event.type == pg.KEYDOWN:
            # verificar si lo que se ha pulsado es una letra
            if event.unicode.isalpha(): 
                letra_intentada = event.unicode
                jugador.intentar_letra(letra_intentada)
                print(f'Letras intentadas{jugador.letras_intentadas}')

    # dibuja el ahorcado completo desactivado
    utils.draw_base(display, 30)

    # cada segundo activa una parte del ahorcado
    # simulando la evolución del juego
    if counter % 20 == 0:
        status += 1
    if counter > 220:
        status = -1

    for index, key in enumerate(GRAPHICS):
        if index <= status:
            utils.draw_part(display, key, True, 30)

    # dibuja una palabra de prueba a medio adivinar
    utils.draw_word(display, font, palabras_juego.crear_palabra_oculta())

    # dibuja el abecedario con algunas letras probadas
    # erróneas y otras letras válidas
    utils.draw_letters(display, letters_font, 360, 50, 'amu', 'ed')

    pg.display.flip()
