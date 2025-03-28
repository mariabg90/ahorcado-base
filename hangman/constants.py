""""
Este módulo define constantes utilizadas en el juego del ahorcado.

Constantes:
    BLACK (tuple): Color RGB para negro.
    GREY (tuple): Color RGB para gris.
    WHITE (tuple): Color RGB para blanco.
    RED (tuple): Color RGB para rojo.
    GREEN (tuple): Color RGB para verde.
    BLUE (tuple): Color RGB para azul.

    LINE_WIDTH (int): Ancho de las líneas utilizadas en los gráficos.

    WINDOW_W (int): Ancho de la ventana del juego.
    WINDOW_H (int): Altura de la ventana del juego.

    GRAPHICS (dict): Diccionario que contiene los elementos gráficos del ahorcado.
        - 'baseline': Coordenadas para la base de la estructura del ahorcado.
        - 'stick1': Coordenadas para el palo vertical de la estructura del ahorcado.
        - 'stick2': Coordenadas para el palo horizontal de la estructura del ahorcado.
        - 'rope': Coordenadas para la cuerda.
        - 'head': Coordenadas y radio para la cabeza del ahorcado.
        - 'body': Coordenadas para el cuerpo del ahorcado.
        - 'lefthand': Coordenadas para la mano izquierda del ahorcado.
        - 'righthand': Coordenadas para la mano derecha del ahorcado.
        - 'leftleg': Coordenadas para la pierna izquierda del ahorcado.
        - 'rightleg': Coordenadas para la pierna derecha del ahorcado."
"""

BLACK = (0, 0, 0)

GREY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LINE_WIDTH = 8

WINDOW_W = 700
WINDOW_H = 500

GRAPHICS = {
    'baseline': [(0, 350), (290, 350)],
    'stick1': [(40, 0), (40, 350)],
    'stick2': [(40, 10), (240, 10)],
    'rope': [(140, 10), (140, 50)],
    'head': [(140, 100), 50],
    'body': [(140, 150), (140, 250)],
    'lefthand': [(140, 160), (90, 200)],
    'righthand': [(140, 160), (190, 200)],
    'leftleg': [(140, 250), (90, 300)],
    'rightleg': [(140, 250), (190, 300)],
}
