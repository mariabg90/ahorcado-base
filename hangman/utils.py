import pygame as pg

from .constants import BLUE, GRAPHICS, GREEN, GREY, LINE_WIDTH, RED, WHITE, WINDOW_H, WINDOW_W


def draw_base(screen, margin_x=10, margin_y=50):
    """Dibuja el ahorcado completo deactivado."""
    for key in GRAPHICS:
        draw_part(screen, key, False, margin_x, margin_y)


def offset_point(point, margin_x, margin_y):
    return (point[0] + margin_x, point[1] + margin_y)


def draw_part(screen, key, active=False, margin_x=10, margin_y=50):
    color = GREY
    if active:
        color = BLUE
    if key == 'head':
        center = offset_point(GRAPHICS.get(key)[0], margin_x, margin_y)
        radius = GRAPHICS.get(key)[1]
        pg.draw.circle(screen, color, center, radius, LINE_WIDTH)
    else:
        start = offset_point(GRAPHICS.get(key)[0], margin_x, margin_y)
        end = offset_point(GRAPHICS.get(key)[1], margin_x, margin_y)
        pg.draw.line(screen, color, start, end, LINE_WIDTH)


def draw_word(screen, font, word):
    word_surface = font.render(word, True, WHITE)
    word_width, word_height = word_surface.get_size()
    screen.blit(word_surface, ((WINDOW_W-word_width) //
                2, WINDOW_H-word_height*1.5))


def draw_letters(screen, font: pg.font.SysFont, x, y, fail='', success=''):
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
        pos_x, pos_y = draw_letter(
            screen, font, x, char_width, line_height, pos_x, pos_y, ascii, color)

        if ascii == n:
            pos_x, pos_y = draw_letter(
                screen, font, x, char_width, line_height, pos_x, pos_y, nn, color)


def draw_letter(screen, font, x, char_width, line_height, pos_x, pos_y, ascii, color):
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
