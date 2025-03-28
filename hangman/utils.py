import pygame as pg

from .constants import BLUE, GRAPHICS, GREEN, GREY, LINE_WIDTH, RED, WHITE, WINDOW_H, WINDOW_W


def draw_base(screen, margin_x=10, margin_y=50):
    """
    Dibuja la estructura base del juego del ahorcado en la pantalla proporcionada.

    Esta función itera a través de todas las partes definidas en el diccionario 
    GRAPHICS y las dibuja en su estado inicial (no reveladas). La posición de la 
    base puede ajustarse utilizando los parámetros margin_x y margin_y.

    Args:
        screen: La superficie o pantalla donde se dibujará la estructura base.
        margin_x (int, opcional): El margen horizontal para ajustar la posición del dibujo. Por defecto es 10.
        margin_y (int, opcional): El margen vertical para ajustar la posición del dibujo. Por defecto es 50.

    Retorna: None
    """
    
    for key in GRAPHICS:
        draw_part(screen, key, False, margin_x, margin_y)


def draw_part(screen, key, active=False, margin_x=10, margin_y=50):
    """
    Dibuja una parte de la figura del ahorcado en la pantalla proporcionada.

    Args:
        screen (pygame.Surface): La superficie en la que se dibujará la parte del ahorcado.
        key (str): La parte del ahorcado a dibujar. Puede ser 'head' u otras partes del cuerpo.
        active (bool, opcional): Indica si la parte debe resaltarse. Por defecto es False.
        margin_x (int, opcional): Margen horizontal para ajustar el dibujo. Por defecto es 10.
        margin_y (int, opcional): Margen vertical para ajustar el dibujo. Por defecto es 50.

    Retorna: None
        
    Notas:
        - Si el valor de `key` es 'head', se dibuja un círculo que representa la cabeza.
        - Para otras claves, se dibuja una línea entre dos puntos.
        - El color de la parte se determina por el parámetro `active`.
    """

    color = GREY
    if active:
        color = BLUE
    if key == 'head':
        center = __offset_point(GRAPHICS.get(key)[0], margin_x, margin_y)
        radius = GRAPHICS.get(key)[1]
        pg.draw.circle(screen, color, center, radius, LINE_WIDTH)
    else:
        start = __offset_point(GRAPHICS.get(key)[0], margin_x, margin_y)
        end = __offset_point(GRAPHICS.get(key)[1], margin_x, margin_y)
        pg.draw.line(screen, color, start, end, LINE_WIDTH)


def draw_word(screen, font, word):
    """
    Dibuja una palabra centrada en la pantalla.

    Args:
        screen (pygame.Surface): La superficie en la que se dibujará la palabra.
        font (pygame.font.Font): La fuente utilizada para renderizar la palabra.
        word (str): La palabra que se mostrará.

    Retorna: None
    """

    word_surface = font.render(word, True, WHITE)
    word_width, word_height = word_surface.get_size()
    screen.blit(word_surface, ((WINDOW_W-word_width) // 2, WINDOW_H-word_height*1.5))


def draw_letters(screen, font, x, y, fail='', success=''):
    """
    Dibuja las letras del alfabeto en la pantalla, resaltando letras según su estado.

    Esta función muestra las letras de la A a la Z y la letra Ñ en la pantalla. Las letras
    pueden resaltarse en diferentes colores dependiendo de si están en las listas `fail` o `success`.

    Args:
        screen: La superficie en la que se dibujarán las letras.
        font: El objeto de fuente utilizado para renderizar las letras.
        x (int): La coordenada x inicial para dibujar las letras.
        y (int): La coordenada y inicial para dibujar las letras.
        fail (str, opcional): Una cadena que contiene letras para resaltar en rojo. Por defecto es ''.
        success (str, opcional): Una cadena que contiene letras para resaltar en verde. Por defecto es ''.

    Retorna: None
    """

    a = ord('A')
    z = ord('Z')
    n = ord('N')
    nn = ord('Ñ')
    char_width = 45
    line_height = 55
    pos_x = x
    pos_y = y
    for ascii in range(a, z+1):
        color = GREY
        if chr(ascii) in fail.upper():
            color = RED
        elif chr(ascii) in success.upper():
            color = GREEN
        pos_x, pos_y = __draw_letter(
            screen, font, x, char_width, line_height, pos_x, pos_y, ascii, color)

        if ascii == n:
            pos_x, pos_y = __draw_letter(
                screen, font, x, char_width, line_height, pos_x, pos_y, nn, color)


################### PENSADAS PARA USO INTERNO ###################


def __offset_point(point, margin_x, margin_y):
    """
    Ajusta un punto dado sumando márgenes específicos a sus coordenadas.
    Está pensada para uso interno.

        point (tuple): Una tupla que representa el punto original (x, y).
        margin_x (float o int): El valor a sumar a la coordenada x.
        margin_y (float o int): El valor a sumar a la coordenada y.

    Retorna:
        tuple: Una nueva tupla que representa el punto ajustado (x + margin_x, y + margin_y).
    """

    return (point[0] + margin_x, point[1] + margin_y)


def __draw_letter(screen, font, x, char_width, line_height, pos_x, pos_y, ascii, color):
    """
    Dibuja una sola letra en la pantalla en la posición especificada.
    Está pensada para uso interno.

        screen (pygame.Surface): La superficie en la que se dibujará la letra.
        font (pygame.font.Font): La fuente utilizada para renderizar la letra.
        x (int): La coordenada x inicial para el área de dibujo.
        char_width (int): El ancho asignado para cada carácter.
        line_height (int): La altura de cada línea de texto.
        pos_x (int): La coordenada x actual donde se dibujará la letra.
        pos_y (int): La coordenada y actual donde se dibujará la letra.
        ascii (int): El valor ASCII del carácter que se dibujará.
        color (tuple): El color de la letra en formato RGB.

    Retorna:
        tuple: Coordenadas actualizadas (pos_x, pos_y) después de dibujar la letra.
    """

    letter = font.render(chr(ascii), True, color)
    w, h = letter.get_size()
    top = pos_y + line_height - h
    left = pos_x + (char_width - w) // 2
    screen.blit(letter, (left, top))
    pos_x = pos_x + char_width
    if pos_x >= WINDOW_W - char_width:
        pos_y = pos_y + line_height
        pos_x = x
    return pos_x, pos_y
