import pygame as pg

from .constants import BLUE, GRAPHICS, GREY, LINE_WIDTH


def draw_base(screen):
    for key in GRAPHICS:
        draw_part(screen, key)


def draw_part(screen, key, active=False):
    color = GREY
    if active:
        color = BLUE
    if key == 'head':
        center = GRAPHICS.get(key)[0]
        radius = GRAPHICS.get(key)[1]
        pg.draw.circle(screen, color, center, radius, LINE_WIDTH)
    else:
        start = GRAPHICS.get(key)[0]
        end = GRAPHICS.get(key)[1]
        pg.draw.line(screen, color, start, end, LINE_WIDTH)
