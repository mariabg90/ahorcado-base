import pygame as pg
from hangman import utils
from hangman.constants import BLUE, GRAPHICS, GREY, LINE_WIDTH

display = pg.display.set_mode((500, 500), 0, 32)
pg.display.set_caption('Juego del ahorcado')
clock = pg.time.Clock()

playing = True

counter = 0
status = -1
while playing:
    clock.tick(20)
    counter += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    utils.draw_base(display)

    if counter % 20 == 0:
        status += 1

    for index, key in enumerate(GRAPHICS):
        if index <= status:
            utils.draw_part(display, key, True)
    pg.display.flip()
