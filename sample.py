import pygame as pg
from hangman import utils
from hangman.constants import BLACK, BLUE, GRAPHICS, GREY, LINE_WIDTH, WHITE, WINDOW_H, WINDOW_W

pg.init()
display = pg.display.set_mode((WINDOW_W, WINDOW_H), 0, 32)
pg.display.set_caption('Juego del ahorcado')
clock = pg.time.Clock()
font_name = pg.font.get_default_font()
font = pg.font.SysFont(font_name, 70)
letters_font = pg.font.SysFont(font_name, 60)

playing = True

counter = 0
status = -1
while playing:
    clock.tick(20)
    counter += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    utils.draw_base(display, 30)

    if counter % 20 == 0:
        status += 1

    for index, key in enumerate(GRAPHICS):
        if index <= status:
            utils.draw_part(display, key, True, 30)

    utils.draw_word(display, font, '-ee---d---')
    utils.draw_letters(display, letters_font, 360, 50, 'aeiou', 'bc')

    pg.display.flip()
